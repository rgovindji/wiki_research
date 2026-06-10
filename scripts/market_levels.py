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
import math
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
    """Adaptive pacing: run full speed (paid plans allow it); the first 429
    flips on free-plan pacing for the rest of the session."""

    def __init__(self, key: str):
        self.key = key
        self.paced = False
        self._last_call = 0.0

    def _fetch(self, url: str) -> tuple[int, dict]:
        if self.paced:
            wait = FREE_PLAN_PACING_S - (time.time() - self._last_call)
            if wait > 0:
                time.sleep(wait)
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
                    self.paced = True
                    time.sleep(20 * (attempt + 1))
                    continue
                return e.code, body
            except (urllib.error.URLError, TimeoutError) as e:
                if attempt < 2:
                    time.sleep(5)
                    continue
                return 0, {"error": str(e)}
        return 0, {"error": "unreachable"}

    def get(self, path: str, params: dict | None = None) -> tuple[int, dict]:
        q = dict(params or {})
        q["apiKey"] = self.key
        return self._fetch(f"{API}{path}?{urllib.parse.urlencode(q)}")

    def get_url(self, url: str) -> tuple[int, dict]:
        """Follow a next_url from pagination (already has params)."""
        sep = "&" if "?" in url else "?"
        return self._fetch(f"{url}{sep}apiKey={self.key}")


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


RISK_FREE = 0.04


def _bs_gamma(S: float, K: float, T: float, iv: float) -> float:
    """Black-Scholes gamma (same for calls and puts)."""
    if T <= 0 or iv <= 0 or S <= 0 or K <= 0:
        return 0.0
    d1 = (math.log(S / K) + (RISK_FREE + iv * iv / 2) * T) / (iv * math.sqrt(T))
    return math.exp(-d1 * d1 / 2) / math.sqrt(2 * math.pi) / (S * iv * math.sqrt(T))


def _flip_by_iteration(contracts: list[tuple], spot: float) -> float | None:
    """True zero-gamma estimate: recompute net dealer GEX at a grid of spot
    levels (±7%) using BS gamma from each contract's IV, and find where the
    curve crosses zero (linear-interpolated). This is what 'the flip' means;
    the cumulative-by-strike version is only a positioning picture."""
    lo, hi = spot * 0.93, spot * 1.07
    n = 56
    prev_s = prev_v = None
    for i in range(n + 1):
        S = lo + i * (hi - lo) / n
        net = 0.0
        for strike, t_years, iv, oi, ctype in contracts:
            g = _bs_gamma(S, strike, t_years, iv)
            v = g * oi * 100 * S * S * 0.01
            net += v if ctype == "call" else -v
        if prev_v is not None and (prev_v < 0 <= net or prev_v > 0 >= net):
            return round(prev_s + (S - prev_s) * (0 - prev_v) / (net - prev_v), 1)
        prev_s, prev_v = S, net
    return None


# Normalized contract: (strike, dte_days, t_years, iv, oi, ctype, snap_gamma)

def load_polygon_contracts(pg: Polygon, underlying: str, spot: float | None) -> tuple[list | None, dict]:
    """Paginate the Polygon chain snapshot into normalized contracts."""
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
        return None, {"reason": "options chain snapshot requires Polygon Options Starter ($29/mo); free plan returns 403"}
    if status != 200:
        return None, {"reason": f"http {status}: {d.get('error', '')[:120]}"}

    contracts: list[tuple] = []
    spot_seen = spot
    pages = 0
    while True:
        pages += 1
        for c in d.get("results") or []:
            det = c.get("details") or {}
            gamma = (c.get("greeks") or {}).get("gamma")
            oi = c.get("open_interest")
            strike = det.get("strike_price")
            ctype = det.get("contract_type")
            iv = c.get("implied_volatility")
            exp = det.get("expiration_date")
            ua = (c.get("underlying_asset") or {}).get("price")
            if ua:
                spot_seen = ua
            if not (gamma and oi and strike and ctype and exp):
                continue
            try:
                dte = (dt.date.fromisoformat(exp) - today).days
            except ValueError:
                continue
            contracts.append((strike, dte, max(dte, 0.5) / 365.0, iv, oi, ctype, gamma))
        nxt = d.get("next_url")
        if not nxt or pages >= 120:
            break
        status, d = pg.get_url(nxt)
        if status != 200:
            break
    return contracts, {"spot": spot_seen, "pages": pages}


CBOE_CHAIN_URL = "https://cdn.cboe.com/api/global/delayed_quotes/options/_SPX.json"


def load_cboe_contracts() -> tuple[list | None, dict]:
    """CBOE's free delayed SPX chain — the whole thing in one GET, with OI,
    greeks, and IV. Independent of Polygon; used as the cross-check source
    (and the same feed gamma-desk runs on)."""
    try:
        with urllib.request.urlopen(CBOE_CHAIN_URL, timeout=30) as r:
            d = json.loads(r.read())
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        return None, {"reason": f"cboe fetch failed: {e}"}
    data = d.get("data", {})
    spot = data.get("current_price") or data.get("close")
    today = dt.date.today()
    contracts: list[tuple] = []
    for c in data.get("options") or []:
        sym = c.get("option", "")
        oi = c.get("open_interest")
        gamma = c.get("gamma")
        iv = c.get("iv")
        if not (sym and oi and gamma):
            continue
        # SPXW260622P07285000 -> root + YYMMDD + C/P + strike*1000
        tail = sym[-15:]
        try:
            exp = dt.date(2000 + int(tail[:2]), int(tail[2:4]), int(tail[4:6]))
            ctype = {"C": "call", "P": "put"}[tail[6]]
            strike = int(tail[7:]) / 1000.0
        except (ValueError, KeyError):
            continue
        if spot and not (spot * 0.85 <= strike <= spot * 1.15):
            continue
        dte = (exp - today).days
        if dte < 0 or dte > 45:
            continue
        contracts.append((strike, dte, max(dte, 0.5) / 365.0, iv, oi, ctype, gamma))
    if not contracts:
        return None, {"reason": "cboe chain parsed but no usable contracts"}
    return contracts, {"spot": spot}


def compute_levels(contracts: list, spot: float | None, max_dte: int, want_flip: bool) -> dict:
    """Net dealer GEX by strike within a DTE window -> walls (+ flip)."""
    by_strike: dict[float, float] = {}
    flip_inputs: list[tuple] = []
    s_ref = spot
    for strike, dte, t_years, iv, oi, ctype, snap_gamma in contracts:
        if dte > max_dte:
            continue
        s = s_ref or strike
        gex = snap_gamma * oi * 100 * s * s * 0.01
        by_strike[strike] = by_strike.get(strike, 0.0) + (gex if ctype == "call" else -gex)
        if iv:
            flip_inputs.append((strike, t_years, iv, oi, ctype))
    if not by_strike:
        return {"error": f"no contracts within {max_dte}d"}

    out = {
        "window": f"<={max_dte}d",
        "call_wall": max(by_strike, key=lambda s: by_strike[s]),
        "put_wall": min(by_strike, key=lambda s: by_strike[s]),
        "net_gex_usd": round(sum(by_strike.values())),
        "n_contracts": len(flip_inputs),
    }
    if want_flip and flip_inputs and spot:
        flip = _flip_by_iteration(flip_inputs, spot)
        out["zero_gamma_flip"] = flip
        out["flip_method"] = ("spot-iterated BS-gamma zero crossing (±7% grid)" if flip is not None
                              else "no zero crossing within ±7% of spot — short gamma at all nearby levels")
    return out


def fetch_gamma(pg: Polygon, underlying: str, spot: float | None) -> dict:
    """Polygon-primary GEX with a CBOE cross-check, each split into the
    aggregate (<=45d) wall structure and the near-view (<=2DTE) shelf that
    intraday flows actually fight over. Top-level fields mirror the
    aggregate for backward compatibility."""
    contracts, meta = load_polygon_contracts(pg, underlying, spot)
    if contracts is None:
        return {"available": False, **meta}
    if not contracts:
        return {"available": False, "reason": "snapshot returned no usable contracts (greeks/OI missing)"}
    spot_seen = meta.get("spot") or spot

    agg = compute_levels(contracts, spot_seen, 45, want_flip=True)
    near = compute_levels(contracts, spot_seen, 2, want_flip=False)

    out = {
        "available": True,
        "underlying": underlying,
        "spot": spot_seen,
        "zero_gamma_flip": agg.get("zero_gamma_flip"),
        "call_wall": agg.get("call_wall"),
        "put_wall": agg.get("put_wall"),
        "net_gex_usd": agg.get("net_gex_usd"),
        "flip_method": agg.get("flip_method"),
        "aggregate": agg,
        "near_view": near,
        "contracts_pages": meta.get("pages"),
        "model": "naive dealer (long calls/short puts), +/-15% strikes; aggregate <=45d, near-view <=2DTE",
    }

    cboe_contracts, cboe_meta = load_cboe_contracts()
    if cboe_contracts:
        cboe_spot = cboe_meta.get("spot")
        out["crosscheck"] = {
            "source": "cboe-delayed",
            "spot": cboe_spot,
            "aggregate": compute_levels(cboe_contracts, cboe_spot, 45, want_flip=True),
            "near_view": compute_levels(cboe_contracts, cboe_spot, 2, want_flip=False),
        }
    else:
        out["crosscheck"] = {"source": "cboe-delayed", "error": cboe_meta.get("reason")}
    return out


def audit_gamma(gamma: dict) -> dict:
    """Sanity-check computed gamma against the tape and against the latest
    market_state snapshot's (snippet-sourced) levels. Returns a report dict;
    'verdict' is pass / suspect / fail. Per playbook: computed levels must
    earn trust side-by-side before becoming the sole source."""
    report: dict = {"checks": [], "verdict": "pass"}

    def check(name: str, ok: bool | None, detail: str) -> None:
        status = "pass" if ok else ("skip" if ok is None else "FAIL")
        report["checks"].append({"check": name, "status": status, "detail": detail})
        if ok is False:
            report["verdict"] = "fail" if report["verdict"] == "fail" else "suspect"

    if not gamma.get("available"):
        report["verdict"] = "skip"
        report["reason"] = gamma.get("reason")
        return report

    spot = gamma.get("spot")
    flip, cw, pw = gamma.get("zero_gamma_flip"), gamma.get("call_wall"), gamma.get("put_wall")
    scaled = gamma.get("spx_scaled") or {}
    # When SPY-derived, audit the SPX-scaled values against SPX references.
    a_flip = scaled.get("zero_gamma_flip", flip)
    a_cw = scaled.get("call_wall", cw)
    a_pw = scaled.get("put_wall", pw)
    a_spot = spot * 10 if scaled and spot else spot

    if all(isinstance(x, (int, float)) for x in (a_pw, a_cw)) and a_spot:
        check("wall-ordering", a_pw < a_cw, f"put wall {a_pw} < call wall {a_cw}")
        check("spot-between-walls", a_pw * 0.97 <= a_spot <= a_cw * 1.03,
              f"spot {a_spot:.0f} vs walls [{a_pw}, {a_cw}] (3% grace)")
    if isinstance(a_flip, (int, float)) and a_spot:
        check("flip-near-spot", abs(a_flip - a_spot) / a_spot < 0.06,
              f"flip {a_flip} is {abs(a_flip - a_spot) / a_spot * 100:.1f}% from spot {a_spot:.0f}")

    # Compare with the latest market_state snapshot (snippet-sourced levels)
    snaps = sorted((REPO / "newsletter" / "market_state").glob("*.json"))
    ref = {}
    if snaps:
        try:
            ref = (json.loads(snaps[-1].read_text()).get("key_levels", {}).get("gamma") or {})
        except json.JSONDecodeError:
            pass
    for name, computed, snippet in (("flip", a_flip, ref.get("zero_gamma_flip")),
                                    ("call_wall", a_cw, ref.get("call_wall")),
                                    ("put_wall", a_pw, ref.get("put_wall"))):
        if isinstance(computed, (int, float)) and isinstance(snippet, (int, float)):
            diff = abs(computed - snippet) / snippet * 100
            check(f"vs-snippet-{name}", diff < 1.5,
                  f"computed {computed:.0f} vs snippet {snippet:.0f} ({diff:.2f}% apart)")
        else:
            check(f"vs-snippet-{name}", None, "no snippet reference to compare")

    # Cross-source: Polygon-computed vs CBOE-computed (independent feeds,
    # same model). Disagreement here means a data problem, not a model one.
    cc = (gamma.get("crosscheck") or {}).get("aggregate") or {}
    for name, ours, theirs in (("flip", a_flip, cc.get("zero_gamma_flip")),
                               ("call_wall", a_cw, cc.get("call_wall")),
                               ("put_wall", a_pw, cc.get("put_wall"))):
        if isinstance(ours, (int, float)) and isinstance(theirs, (int, float)):
            diff = abs(ours - theirs) / theirs * 100
            check(f"vs-cboe-{name}", diff < 1.0,
                  f"polygon {ours:.0f} vs cboe {theirs:.0f} ({diff:.2f}% apart)")
        else:
            check(f"vs-cboe-{name}", None, "cboe crosscheck unavailable")
    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", help="comma-separated override")
    ap.add_argument("--skip-closes", action="store_true")
    ap.add_argument("--skip-gamma", action="store_true")
    ap.add_argument("--audit", action="store_true",
                    help="append a sanity/side-by-side audit of the computed gamma levels")
    args = ap.parse_args()

    load_env()
    key = os.environ.get("POLYGON_KEY") or os.environ.get("POLYGON_API_KEY")
    if not key:
        print(json.dumps({"error": "no POLYGON_KEY in .env"}))
        return 1

    pg = Polygon(key)
    out: dict = {"source": "polygon.io", "generated": dt.datetime.now().isoformat(timespec="seconds")}

    if not args.skip_closes:
        tickers = (args.tickers.split(",") if args.tickers
                   else portfolio_tickers() + EXTRA_TICKERS)
        out["closes"] = fetch_closes(pg, tickers)

    if not args.skip_gamma:
        spy = (out.get("closes", {}).get("prices", {}).get("SPY") or {}).get("close")
        if not spy:
            # gamma-only run still needs spot for the strike filter
            _, d = pg.get("/v2/aggs/ticker/SPY/prev", {"adjusted": "true"})
            results = d.get("results") or []
            spy = results[0].get("c") if results else None
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
        if args.audit:
            out["audit"] = audit_gamma(gamma)

    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
