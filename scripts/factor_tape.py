#!/usr/bin/env python3
"""Cross-asset 'factor tape' for the Reaction Desk.

Pulls the handful of macro drivers that push equity-sector/factor leadership
around — 10Y yield, oil, the dollar, VIX, gold — with today's move and a
short trend. Headless, no deps beyond stdlib. Errors land in the JSON; the
daily run must never break because a quote was missing.

Usage:
    python3 scripts/factor_tape.py            # JSON to stdout
    python3 scripts/factor_tape.py --pretty   # human-readable

The Reaction Desk agent reads this + the market_state event calendar to
produce its forward-looking, plain-English "what could move things" block.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}

# symbol -> (label, what it transmits to in equities — for the agent's reasoning)
FACTORS = {
    "^TNX":     ("10Y Treasury yield (%)", "up -> long-duration mega-cap/growth down, banks/value up"),
    "CL=F":     ("WTI crude ($)",          "up -> energy up, airlines/transports/consumer down"),
    "DX-Y.NYB": ("US dollar (DXY)",        "up -> multinationals/commodities/EM down"),
    "^VIX":     ("VIX (fear)",             "up -> risk-off, broad de-risking, leadership narrows"),
    "GC=F":     ("Gold ($)",               "up -> risk-off / debasement hedge"),
}


def fetch(sym: str) -> dict:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=10d"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
            res = json.loads(r.read())["chart"]["result"][0]
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError, IndexError) as e:
        return {"error": str(e)[:80]}
    closes = [c for c in res["indicators"]["quote"][0]["close"] if c is not None]
    if len(closes) < 2:
        return {"error": "insufficient data"}
    last, prev = closes[-1], closes[-2]
    wk = closes[-6] if len(closes) >= 6 else closes[0]
    day_chg = last - prev
    wk_chg = last - wk
    trend = "rising" if wk_chg > 0 else "falling" if wk_chg < 0 else "flat"
    return {
        "level": round(last, 2),
        "day_change": round(day_chg, 2),
        "day_change_pct": round(day_chg / prev * 100, 2) if prev else None,
        "5d_trend": trend,
        "5d_change": round(wk_chg, 2),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pretty", action="store_true")
    args = ap.parse_args()

    out = {"source": "yahoo", "factors": {}}
    for sym, (label, transmits) in FACTORS.items():
        d = fetch(sym)
        d["label"] = label
        d["transmits_to"] = transmits
        out["factors"][sym] = d

    if args.pretty:
        for sym, d in out["factors"].items():
            if "error" in d:
                print(f"{d['label']:26} ERR {d['error']}")
            else:
                print(f"{d['label']:26} {d['level']:>9}  today {d['day_change']:+}  ({d['5d_trend']} 5d)")
    else:
        print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
