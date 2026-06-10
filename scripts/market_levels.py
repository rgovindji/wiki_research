#!/usr/bin/env python3
"""Pull market data from Polygon.io for the newsletter loop.

Two jobs, each degrading gracefully by plan tier:

  closes  — exact daily closes for the portfolio tickers + SPY/QQQ
            (works on the FREE plan; paced at ~5 req/min)
  gamma   — SPX/SPY dealer gamma exposure: net GEX by strike, zero-gamma
            flip, call wall, put wall, computed from the full options
            chain snapshot (greeks + open interest).
            REQUIRES Polygon Options Starter ($29/mo) or higher; on the
            free plan this section reports available: false and the
            daily runs keep using web-search levels instead.

Usage:
    python3 scripts/market_levels.py                 # closes + gamma attempt
    python3 scripts/market_levels.py --skip-closes   # gamma only (fast check)
    python3 scripts/market_levels.py --tickers NVDA,SPY

Output: one JSON object on stdout. The close-of-market run executes this
FIRST in its intelligence sweep and prefers its numbers over web search
(api > snippet). Errors never raise — they land in the JSON so the
headless run can keep going.

GEX model (standard, naive-dealer): dealers are assumed long calls /
short puts, so call gamma contributes positive dealer gamma and put
gamma negative. Per contract: gex_$ = gamma * open_interest * 100 *
spot^2 * 0.01 (dollar gamma per 1% move). Zero-gamma "flip" here is the
strike where cumulative net GEX crosses zero — a proxy for the true
spot-iterated flip. Paid services (SpotGamma etc.) add proprietary
adjustments; per playbook, run this side-by-side with snippet levels
before trusting it as sole source.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
API = "https://api.polygon.io"

PORTFOLIO = REPO / "newsletter" / "portfolio.json"
EXTRA_TICKERS = ["SPY", "QQQ"]

# Free plan: 5 requests/minute. Pace proactively, retry on 429.
FREE_PLAN_PACING_S = 12.5


def load_env() -> None:
    for env_path in (REPO / ".env", REPO / "fintwit-terminal" / ".env"):
        if not env_path.exists():
            continue
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


class Polygon:
    def __init__(self, key: str, paced: bool):
        self.key = key
        self.paced = paced
        self._last_call = 0.0

    def get(self, path: str, params: dict | None = None) -> tuple[int, dict]:
        if self.paced:
            wait = FREE_PLAN_PACING_S - (time.time() - self._last_call)
            if wait > 0:
                time.sleep(wait)
        q = dict(params or {})
        q["apiKey"] = self.key
        url = f"{API}{path}?{urllib.parse.urlencode(q)}"
        for attempt in range(3):
            self._last_call = time.time()
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    return r.status, json.loads(r.read())
            except urllib.error.HTTPError as e:
                body = {}
                try:
                    body = json.loads(e.read() or b"{}")
                except json.JSONDecodeError:
                    pass
                if e.code == 429 and attempt < 2:
                    time.sleep(20 * (attempt + 1))
                    continue
                return e.code, body
            except (urllib.error.URLError, TimeoutError) as e:
                if attempt < 2:
                    time.sleep(5)
                    continue
                return 0, {"error": str(e)}
        return 0, {"error": "unreachable"}

    def get_url(self, url: str) -> tuple[int, dict]:
        """Follow a next_url from pagination (already has params)."""
        sep = "&" if "?" in url else "?"
        for attempt in range(3):
            try:
                with urllib.request.urlopen(f"{url}{sep}apiKey={self.key}", timeout=30) as r:
                    return r.status, json.loads(r.read())
            except urllib.error.HTTPError as e:
                if e.code == 429 and attempt < 2:
                    time.sleep(20 * (attempt + 1))
                    continue
                return e.code, {}
        return 0, {}


def portfolio_tickers() -> list[str]:
    try:
        p = json.loads(PORTFOLIO.read_text(encoding="utf-8"))
        return [h["ticker"] for h in p.get("current_holdings", [])]
    except (OSError, json.JSONDecodeError, KeyError):
        return []


def fetch_closes(pg: Polygon, tickers: list[str]) -> dict:
    """Previous-session close per ticker via /v2/aggs/ticker/{t}/prev.
    Free-plan friendly (one call per ticker, paced)."""
    out: dict = {"as_of": None, "prices": {}, "errors": {}}
    for t in tickers:
        status, d = pg.get(f"/v2/aggs/ticker/{t}/prev", {"adjusted": "true"})
        results = d.get("results") or []
        if status == 200 and results:
            r = results[0]
            out["prices"][t] = {"close": r.get("c"), "high": r.get("h"), "low": r.get("l")}
            ts = r.get("t")
            if ts and not out["as_of"]:
                out["as_of"] = dt.datetime.fromtimestamp(ts / 1000, dt.timezone.utc).date().isoformat()
        else:
            out["errors"][t] = f"http {status}: {d.get('error') or d.get('status') or 'no results'}"
    return out


def fetch_gamma(pg: Polygon, underlying: str, spot: float | None) -> dict:
    """Chain snapshot -> net GEX by strike -> flip + walls.
    Returns available: false with the reason when the plan doesn't allow it."""
    today = dt.date.today()
    params = {
        "limit": 250,
        "expiration_date.lte": (today + dt.timedelta(days=45)).isoformat(),
        "expiration_date.gte": today.isoformat(),
    }
    if spot:
        params["strike_price.gte"] = round(spot * 0.85)
        params["strike_price.lte"] = round(spot * 1.15)

    status, d = pg.get(f"/v3/snapshot/options/{underlying}", params)
    if status == 403:
        return {"available": False,
                "reason": "options chain snapshot requires Polygon Options Starter ($29/mo); free plan returns 403"}
    if status != 200:
        return {"available": False, "reason": f"http {status}: {d.get('error', '')[:120]}"}

    by_strike: dict[float, float] = {}
    spot_seen = spot
    pages = 0
    while True:
        pages += 1
        for c in d.get("results") or []:
            det = c.get("details") or {}
            greeks = c.get("greeks") or {}
            gamma = greeks.get("gamma")
            oi = c.get("open_interest")
            strike = det.get("strike_price")
            ctype = det.get("contract_type")
            ua = (c.get("underlying_asset") or {}).get("price")
            if ua:
                spot_seen = ua
            if not (gamma and oi and strike and ctype):
                continue
            s = spot_seen or strike
            gex = gamma * oi * 100 * s * s * 0.01
            by_strike[strike] = by_strike.get(strike, 0.0) + (gex if ctype == "call" else -gex)
        nxt = d.get("next_url")
        if not nxt or pages >= 40:
            break
        status, d = pg.get_url(nxt)
        if status != 200:
            break

    if not by_strike:
        return {"available": False, "reason": "snapshot returned no usable contracts (greeks/OI missing)"}

    strikes = sorted(by_strike)
    net_total = sum(by_strike.values())
    call_wall = max(strikes, key=lambda s: by_strike[s])
    put_wall = min(strikes, key=lambda s: by_strike[s])

    flip = None
    cum = 0.0
    for s in strikes:
        prev = cum
        cum += by_strike[s]
        if prev < 0 <= cum or prev > 0 >= cum:
            flip = s
            if spot_seen and abs(s - spot_seen) / spot_seen < 0.10:
                break  # prefer a crossing near spot over far-wing noise

    return {
        "available": True,
        "underlying": underlying,
        "spot": spot_seen,
        "zero_gamma_flip": flip,
        "call_wall": call_wall,
        "put_wall": put_wall,
        "net_gex_usd": round(net_total),
        "contracts_pages": pages,
        "model": "naive dealer (long calls/short puts), <=45d expiries, +/-15% strikes, cumulative-GEX flip proxy",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", help="comma-separated override")
    ap.add_argument("--skip-closes", action="store_true")
    ap.add_argument("--skip-gamma", action="store_true")
    args = ap.parse_args()

    load_env()
    key = os.environ.get("POLYGON_KEY") or os.environ.get("POLYGON_API_KEY")
    if not key:
        print(json.dumps({"error": "no POLYGON_KEY in .env"}))
        return 1

    pg = Polygon(key, paced=True)
    out: dict = {"source": "polygon.io", "generated": dt.datetime.now().isoformat(timespec="seconds")}

    if not args.skip_closes:
        tickers = (args.tickers.split(",") if args.tickers
                   else portfolio_tickers() + EXTRA_TICKERS)
        out["closes"] = fetch_closes(pg, tickers)

    if not args.skip_gamma:
        spy = (out.get("closes", {}).get("prices", {}).get("SPY") or {}).get("close")
        # SPX index options are the cleaner read; SPY is the fallback. Both
        # 403 on the free plan; the first success wins on a paid plan.
        gamma = fetch_gamma(pg, "I:SPX", spy * 10 if spy else None)
        if not gamma.get("available"):
            spy_gamma = fetch_gamma(pg, "SPY", spy)
            if spy_gamma.get("available"):
                ratio = 10.0
                spy_gamma["spx_scaled"] = {
                    k: round(spy_gamma[k] * ratio, 0)
                    for k in ("zero_gamma_flip", "call_wall", "put_wall")
                    if spy_gamma.get(k)
                }
                spy_gamma["spx_scale_note"] = "SPY levels x10 nominal; quote SPX zones, not exact lines"
                gamma = spy_gamma
            else:
                gamma["spy_fallback_reason"] = spy_gamma.get("reason")
        out["gamma"] = gamma

    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
