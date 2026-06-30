#!/usr/bin/env python3
"""Pull verified daily OHLC from Polygon and compute technicals for an equity analysis.

The standard data layer for the wiki's analysis artifacts: every price/level comes from
the Polygon API (never a WebSearch snippet), and the technicals (EMAs, gaps, swing-low
supports, recent range) are computed from real bars — ready to drop into the marked
TradingView Lightweight-Charts HTML.

Usage:
    python scripts/ticker_ta.py NBIS                 # human-readable TA summary
    python scripts/ticker_ta.py NBIS --json out.json # full structured data -> file
    python scripts/ticker_ta.py NBIS --chart-js      # `const CHART_DATA={...}` for embedding
    python scripts/ticker_ta.py NBIS --bars 130 --asof 2026-06-29

Reads POLYGON_KEY from .env (same key market_levels.py uses).
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
API = "https://api.polygon.io"


def load_env() -> None:
    env = REPO_ROOT / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip().strip("'\""))


def polygon_key() -> str | None:
    return os.environ.get("POLYGON_KEY") or os.environ.get("POLYGON_API_KEY")


def fetch_daily(ticker: str, start: str, end: str) -> list[dict]:
    key = polygon_key()
    if not key:
        raise SystemExit("[ticker_ta] no POLYGON_KEY in .env")
    url = (f"{API}/v2/aggs/ticker/{ticker.upper()}/range/1/day/{start}/{end}"
           f"?adjusted=true&sort=asc&limit=50000&apiKey={key}")
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            d = json.load(r)
    except Exception as e:  # network / HTTP
        raise SystemExit(f"[ticker_ta] Polygon request failed: {e}")
    if d.get("status") not in ("OK", "DELAYED") or not d.get("results"):
        raise SystemExit(f"[ticker_ta] no data for {ticker} ({d.get('status')}, "
                         f"results={len(d.get('results', []))})")
    out = []
    for b in d["results"]:
        day = datetime.datetime.fromtimestamp(b["t"] / 1000, datetime.UTC).strftime("%Y-%m-%d")
        out.append({"d": day, "o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"], "v": b["v"]})
    return out


def ema(vals: list[float], n: int) -> list[float]:
    k = 2 / (n + 1)
    e = vals[0]
    out = [e]
    for v in vals[1:]:
        e = v * k + e * (1 - k)
        out.append(e)
    return out


def add_emas(bars: list[dict]) -> None:
    closes = [b["c"] for b in bars]
    for name, n in (("e20", 20), ("e50", 50), ("e200", 200)):
        for b, val in zip(bars, ema(closes, n)):
            b[name] = round(val, 2)


def swing_lows(bars: list[dict], window: int = 5, lookback: int = 120) -> list[dict]:
    out = []
    lo = max(window, len(bars) - lookback)
    for i in range(lo, len(bars) - window):
        if bars[i]["l"] == min(b["l"] for b in bars[i - window:i + window + 1]):
            out.append({"date": bars[i]["d"], "low": round(bars[i]["l"], 2)})
    return out


def gaps(bars: list[dict], lookback: int = 60) -> list[dict]:
    out = []
    for i in range(max(1, len(bars) - lookback), len(bars)):
        p, c = bars[i - 1], bars[i]
        if c["o"] > p["h"] * 1.01:
            filled = any(b["l"] <= p["h"] for b in bars[i:])
            out.append({"date": c["d"], "type": "up", "from": round(p["h"], 2),
                        "to": round(c["o"], 2), "filled": filled})
        elif c["o"] < p["l"] * 0.99:
            filled = any(b["h"] >= p["l"] for b in bars[i:])
            out.append({"date": c["d"], "type": "down", "from": round(p["l"], 2),
                        "to": round(c["o"], 2), "filled": filled})
    return out


def window_low(bars: list[dict], n: int) -> dict:
    seg = bars[-n:]
    b = min(seg, key=lambda x: x["l"])
    return {"date": b["d"], "low": round(b["l"], 2)}


def window_high(bars: list[dict], n: int) -> dict:
    seg = bars[-n:]
    b = max(seg, key=lambda x: x["h"])
    return {"date": b["d"], "high": round(b["h"], 2)}


def summarize(ticker: str, bars: list[dict]) -> dict:
    last = bars[-1]
    emas = {"e20": last["e20"], "e50": last["e50"], "e200": last["e200"]}
    pos = {k: ("above" if last["c"] >= v else "below") for k, v in emas.items()}
    return {
        "ticker": ticker.upper(),
        "last": {"date": last["d"], "close": round(last["c"], 2),
                 "high": round(last["h"], 2), "low": round(last["l"], 2)},
        "emas": emas,
        "price_vs_ema": pos,
        "recent_high_20d": window_high(bars, 20),
        "recent_high_60d": window_high(bars, 60),
        "recent_high_180d": window_high(bars, 180),
        "recent_low_10d": window_low(bars, 10),
        "recent_low_20d": window_low(bars, 20),
        "recent_low_60d": window_low(bars, 60),
        "swing_lows": swing_lows(bars),
        "gaps": gaps(bars),
    }


def chart_payload(bars: list[dict], n: int) -> dict:
    seg = bars[-n:]
    return {
        "candle": [{"time": b["d"], "open": round(b["o"], 2), "high": round(b["h"], 2),
                    "low": round(b["l"], 2), "close": round(b["c"], 2)} for b in seg],
        "e20": [{"time": b["d"], "value": b["e20"]} for b in seg],
        "e50": [{"time": b["d"], "value": b["e50"]} for b in seg],
        "e200": [{"time": b["d"], "value": b["e200"]} for b in seg],
    }


def print_summary(s: dict) -> None:
    last = s["last"]
    print(f"\n=== {s['ticker']} technicals  (close {last['date']}) ===")
    print(f"  Last close : ${last['close']:.2f}   (day range ${last['low']:.2f}–${last['high']:.2f})")
    print(f"  EMA20/50/200: ${s['emas']['e20']:.2f} / ${s['emas']['e50']:.2f} / ${s['emas']['e200']:.2f}"
          f"   (price {s['price_vs_ema']['e20']}/{s['price_vs_ema']['e50']}/{s['price_vs_ema']['e200']})")
    print(f"  Recent high : ${s['recent_high_180d']['high']:.2f} ({s['recent_high_180d']['date']}, 180d)")
    print(f"  Recent lows : 10d ${s['recent_low_10d']['low']:.2f} · "
          f"20d ${s['recent_low_20d']['low']:.2f} · 60d ${s['recent_low_60d']['low']:.2f}")
    print("  Swing lows (support candidates):")
    for sl in s["swing_lows"]:
        print(f"    {sl['date']}  ${sl['low']:.2f}")
    print("  Gaps (last 60d):")
    for g in s["gaps"]:
        tag = "filled" if g["filled"] else "UNFILLED"
        print(f"    {g['date']}  {g['type']:>4}  ${g['from']:.2f}->${g['to']:.2f}  ({tag})")
    print()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Polygon daily OHLC + technicals for one ticker")
    p.add_argument("ticker")
    p.add_argument("--asof", help="end date YYYY-MM-DD (default: today)")
    p.add_argument("--history", type=int, default=460, help="calendar days of history to pull")
    p.add_argument("--bars", type=int, default=130, help="bars to include in --chart-js payload")
    p.add_argument("--json", metavar="PATH", help="write full {summary, chart} JSON to PATH")
    p.add_argument("--chart-js", action="store_true", help="print `const CHART_DATA={...}` for HTML embed")
    p.add_argument("--var", default="CHART_DATA", help="JS const name for --chart-js")
    args = p.parse_args(argv)

    load_env()
    end = datetime.date.fromisoformat(args.asof) if args.asof else datetime.date.today()
    start = end - datetime.timedelta(days=args.history)
    bars = fetch_daily(args.ticker, str(start), str(end))
    add_emas(bars)
    summary = summarize(args.ticker, bars)
    chart = chart_payload(bars, args.bars)

    if args.chart_js:
        print(f"const {args.var}=" + json.dumps(chart) + ";")
        return 0
    if args.json:
        Path(args.json).write_text(json.dumps({"summary": summary, "chart": chart}), encoding="utf-8")
        print(f"[ticker_ta] wrote {args.json}  ({len(bars)} bars, {len(chart['candle'])} in chart)")
    print_summary(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
