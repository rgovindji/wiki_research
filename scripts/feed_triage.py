#!/usr/bin/env python3
"""DeepSeek triage layer over feed_scan — keep the firehose readable.

feed_scan.py now pulls ~50 items/day across builder/researcher/investor/operator feeds.
This scores each NEW item (0-10) for relevance + novelty + impact against the wiki's
tickers and live theses, tags the ticker/theme it touches, and recommends ingest / watch
/ skip — so the daily curator reads the diamonds first instead of all 50. Uses DeepSeek
(cheap) for the high-volume / low-stakes scoring; the expensive reasoning stays for the
actual analysis.

Usage:
    python3 scripts/feed_triage.py                 # run feed_scan (incremental), triage, ranked digest
    python3 scripts/feed_triage.py --all           # triage everything (ignore feed_scan seen-cache)
    python3 scripts/feed_triage.py --all --no-update  # ...and don't touch the cache (manual run)
    python3 scripts/feed_triage.py --min 6         # only show score >= 6
    python3 scripts/feed_triage.py --json out.json

Reads DEEPSEEK_API_KEY (+ optional DEEPSEEK_MODEL, default deepseek-chat) from .env.
Falls back to an unscored digest if DeepSeek is unavailable.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"


def load_env() -> None:
    env = REPO / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        v = v.strip()
        if v and v[0] in "\"'":  # quoted value — take up to the closing quote
            end = v.find(v[0], 1)
            v = v[1:end] if end != -1 else v[1:]
        elif " #" in v:  # strip trailing inline comment
            v = v.split(" #", 1)[0].strip()
        os.environ.setdefault(k.strip(), v)


def wiki_context() -> tuple[list[str], list[str]]:
    tickers = sorted(p.stem for p in (REPO / "wiki" / "companies").glob("*.md"))
    theses = []
    led = REPO / "wiki" / "thesis-ledger.md"
    if led.exists():
        for line in led.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("### T"):
                theses.append(line.lstrip("# ").strip())
    return tickers, theses


def run_feed_scan(all_flag: bool, no_update: bool) -> dict:
    cmd = ["python3", str(REPO / "scripts" / "feed_scan.py")]
    if all_flag:
        cmd.append("--all")
    if no_update:
        cmd.append("--no-update")
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    try:
        return json.loads(res.stdout)
    except Exception:
        print(f"[feed_triage] feed_scan failed:\n{res.stderr[:500]}", file=sys.stderr)
        return {"new_items": 0, "by_persona": {}}


def deepseek_score(items: list[dict], tickers: list[str], theses: list[str], model: str, key: str) -> dict:
    catalog = ", ".join(tickers)
    thesis_list = "\n".join(f"- {t}" for t in theses)
    compact = [{"id": it["id"], "persona": it["persona"], "source": it["source"],
                "title": it["title"], "summary": (it.get("summary") or "")[:300]} for it in items]
    system = (
        "You are the ingestion triage analyst for a long-term AI/semis/compute equity research "
        "wiki. Score each feed item for whether it is worth the curator's attention. Be a harsh "
        "filter — most items are noise. Reward NET-NEW, specific, investable signal: a datapoint "
        "that touches a tracked ticker or thesis, a builder demand/pain signal, an investor "
        "valuation/forecast framing, a supply-chain fact. Penalize restatements, vague opinion, "
        "memes, generic news, and anything off-topic."
    )
    user = (
        f"Tracked tickers: {catalog}\n\nLive theses:\n{thesis_list}\n\n"
        f"Score these {len(items)} items. For each return: id, score (0-10 integer), "
        "action ('ingest' >=7 worth a source summary/page update, 'watch' 4-6 note it, "
        "'skip' <=3 noise), tag (the single most relevant ticker symbol or thesis keyword, or "
        "'none'), why (<=12 words). Return ONLY JSON: {\"items\":[{\"id\":...,\"score\":...,"
        "\"action\":...,\"tag\":...,\"why\":...}]}.\n\nITEMS:\n" + json.dumps(compact, ensure_ascii=False)
    )
    body = json.dumps({
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0,
        "response_format": {"type": "json_object"},
    }).encode("utf-8")
    req = urllib.request.Request(DEEPSEEK_URL, data=body,
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            resp = json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode()[:300]}")
    content = resp["choices"][0]["message"]["content"]
    return json.loads(content)


def main() -> int:
    ap = argparse.ArgumentParser(description="DeepSeek triage over feed_scan")
    ap.add_argument("--all", action="store_true", help="triage everything (ignore feed_scan cache)")
    ap.add_argument("--no-update", action="store_true", help="don't update feed_scan's seen-cache")
    ap.add_argument("--min", type=int, default=0, help="only show items with score >= MIN")
    ap.add_argument("--json", metavar="PATH", help="write the scored items to PATH")
    args = ap.parse_args()
    load_env()

    digest = run_feed_scan(args.all, args.no_update)
    items = [it for v in digest.get("by_persona", {}).values() for it in v]
    if not items:
        print("[feed_triage] nothing new to triage.")
        return 0

    key = os.environ.get("DEEPSEEK_API_KEY")
    model = os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-flash")
    scored = {it["id"]: {"score": None, "action": "?", "tag": "", "why": ""} for it in items}
    if key:
        try:
            result = deepseek_score(items, *wiki_context(), model, key)
            for r in result.get("items", []):
                if r.get("id") in scored:
                    scored[r["id"]] = {"score": r.get("score"), "action": r.get("action", "?"),
                                       "tag": r.get("tag", ""), "why": r.get("why", "")}
        except Exception as e:
            print(f"[feed_triage] DeepSeek scoring failed ({e}); showing unscored digest.", file=sys.stderr)
    else:
        print("[feed_triage] no DEEPSEEK_API_KEY — showing unscored digest.", file=sys.stderr)

    for it in items:
        it.update(scored[it["id"]])
    ranked = sorted(items, key=lambda x: (x.get("score") if x.get("score") is not None else -1), reverse=True)

    counts = {"ingest": 0, "watch": 0, "skip": 0}
    for it in ranked:
        counts[it.get("action")] = counts.get(it.get("action"), 0) + 1
    print(f"## Feed triage — {len(ranked)} items · "
          f"{counts.get('ingest', 0)} ingest · {counts.get('watch', 0)} watch · {counts.get('skip', 0)} skip\n")
    for it in ranked:
        s = it.get("score")
        if s is not None and s < args.min:
            continue
        badge = {"ingest": "🟢", "watch": "🟡", "skip": "⚪"}.get(it.get("action"), "·")
        sc = f"{s}" if s is not None else "-"
        print(f"{badge} [{sc}] ({it['persona']}/{it['source']}) {it['title']}")
        meta = " · ".join(x for x in [it.get("tag"), it.get("why")] if x)
        if meta:
            print(f"      {meta}")
        print(f"      {it['url']}")
    if args.json:
        Path(args.json).write_text(json.dumps(ranked, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\n[feed_triage] wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
