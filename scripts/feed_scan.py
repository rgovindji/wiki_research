#!/usr/bin/env python3
"""Persona-tagged, incremental multi-source feed scanner for the daily ingestion ritual.

Companion to semiwiki_scan.py: where that scrapes one site, this sweeps a registry of
*programmatic* feeds — HuggingFace (builder/researcher signal), Hacker News (builder/
operator discourse), arXiv + lab blogs (research frontier), and analyst/investor RSS —
and returns only what's NEW since the last run (seen-cache .feeds_seen.json, gitignored),
grouped by persona so the curator can read each lens deliberately.

The persona lens (mirrors the YouTube sweep's 6 tiers, applied to feeds):
  builder    — what people on the cutting edge are shipping, and what's hard
  researcher — the capability/hardware frontier (papers, model releases)
  investor   — how the capital is valuing + forecasting the names
  operator   — what's actually happening in the supply chain / industry

Usage:
    python3 scripts/feed_scan.py                 # new items since last run (JSON digest)
    python3 scripts/feed_scan.py --all           # ignore the seen cache
    python3 scripts/feed_scan.py --no-update     # don't write the seen cache
    python3 scripts/feed_scan.py --persona builder
    python3 scripts/feed_scan.py --source hf-trending-models
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request
import urllib.parse
from pathlib import Path
from xml.etree import ElementTree as ET

REPO = Path(__file__).resolve().parents[1]
SEEN_PATH = REPO / ".feeds_seen.json"
UA = "investing-wiki-feedscan/1.0 (+research; contact rgovindji)"

# ── Source registry — persona-tagged. Extend freely; each source degrades gracefully. ──
SOURCES = [
    # Builders / cutting edge — what's being shipped, what's hard, what compute they need
    {"name": "hf-trending-models", "persona": "builder", "type": "hf_models", "limit": 8},
    {"name": "hn-ai-infra", "persona": "builder", "type": "hn", "limit": 10, "min_points": 40,
     "query": "AI OR GPU OR inference OR CUDA OR HBM OR datacenter OR Nvidia OR TPU OR LLM"},
    {"name": "r-localllama", "persona": "builder", "type": "reddit", "sub": "LocalLLaMA", "limit": 6},
    {"name": "arxiv-hardware", "persona": "researcher", "type": "rss", "limit": 6,
     "url": "http://export.arxiv.org/rss/cs.AR"},
    # Researchers / frontier
    {"name": "hf-daily-papers", "persona": "researcher", "type": "hf_papers", "limit": 6},
    # Investors — valuation, forecasting, positioning
    {"name": "damodaran", "persona": "investor", "type": "rss", "limit": 4,
     "url": "https://aswathdamodaran.blogspot.com/feeds/posts/default?alt=rss"},
    {"name": "hn-markets", "persona": "investor", "type": "hn", "limit": 6, "min_points": 60,
     "query": "valuation OR earnings OR semiconductor OR Nvidia OR bubble OR AI capex"},
    {"name": "r-stocks", "persona": "investor", "type": "reddit", "sub": "stocks", "limit": 5},
    # Operators / industry analysts
    {"name": "semianalysis", "persona": "operator", "type": "rss", "limit": 5,
     "url": "https://semianalysis.com/feed/"},
]


def fetch(url: str, timeout: int = 25, accept: str = "*/*") -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def fetch_json(url: str, timeout: int = 25):
    return json.loads(fetch(url, timeout, accept="application/json"))


def _clip(s: str, n: int = 400) -> str:
    s = " ".join((s or "").split())
    return s[:n] + ("…" if len(s) > n else "")


# ── per-type collectors: each returns list of {id, title, url, published, summary} ──

def collect_rss(src: dict) -> list[dict]:
    xml = fetch(src["url"], accept="application/rss+xml, application/xml, text/xml")
    root = ET.fromstring(xml)
    items = []
    # RSS 2.0
    for it in root.iter("item"):
        link = (it.findtext("link") or "").strip()
        guid = (it.findtext("guid") or link).strip()
        items.append({
            "id": guid or link,
            "title": _clip(it.findtext("title") or "", 200),
            "url": link,
            "published": (it.findtext("pubDate") or "").strip(),
            "summary": _clip(it.findtext("description") or ""),
        })
    # Atom fallback
    if not items:
        ns = "{http://www.w3.org/2005/Atom}"
        for e in root.iter(f"{ns}entry"):
            link_el = e.find(f"{ns}link")
            link = (link_el.get("href") if link_el is not None else "") or ""
            items.append({
                "id": (e.findtext(f"{ns}id") or link).strip(),
                "title": _clip(e.findtext(f"{ns}title") or "", 200),
                "url": link,
                "published": (e.findtext(f"{ns}updated") or "").strip(),
                "summary": _clip(e.findtext(f"{ns}summary") or ""),
            })
    return items[: src.get("limit", 8)]


def collect_hn(src: dict) -> list[dict]:
    q = urllib.parse.quote(src["query"])
    url = (f"https://hn.algolia.com/api/v1/search_by_date?query={q}"
           f"&tags=story&hitsPerPage={src.get('limit', 10) * 3}")
    data = fetch_json(url)
    out = []
    for h in data.get("hits", []):
        if (h.get("points") or 0) < src.get("min_points", 0):
            continue
        out.append({
            "id": "hn-" + str(h.get("objectID")),
            "title": _clip(h.get("title") or "", 200),
            "url": h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
            "published": h.get("created_at", ""),
            "summary": f"{h.get('points', 0)} points · {h.get('num_comments', 0)} comments · "
                       f"discuss: https://news.ycombinator.com/item?id={h.get('objectID')}",
        })
        if len(out) >= src.get("limit", 10):
            break
    return out


def collect_hf_models(src: dict) -> list[dict]:
    data = fetch_json(f"https://huggingface.co/api/models?sort=trendingScore&limit={src.get('limit', 8)}")
    out = []
    for m in data:
        mid = m.get("id", "")
        tags = [t for t in (m.get("tags") or []) if not t.startswith(("region:", "license:"))][:8]
        out.append({
            "id": "hf-model-" + mid,
            "title": f"{mid}  [{m.get('pipeline_tag', '?')}]",
            "url": f"https://huggingface.co/{mid}",
            "published": m.get("createdAt", ""),
            "summary": f"♥{m.get('likes', 0)} · ↓{m.get('downloads', 0):,} · trending={m.get('trendingScore', 0)} · "
                       + " ".join(tags),
        })
    return out


def collect_hf_papers(src: dict) -> list[dict]:
    data = fetch_json(f"https://huggingface.co/api/daily_papers?limit={src.get('limit', 6)}")
    out = []
    for entry in data:
        p = entry.get("paper", entry)
        pid = p.get("id", "")
        out.append({
            "id": "hf-paper-" + pid,
            "title": _clip(p.get("title") or "", 220),
            "url": f"https://huggingface.co/papers/{pid}",
            "published": entry.get("publishedAt", p.get("publishedAt", "")),
            "summary": _clip(p.get("summary") or "", 480),
        })
    return out


def collect_reddit(src: dict) -> list[dict]:
    # Unauthenticated Reddit is often blocked on cloud IPs; try, degrade to [] with a note.
    sub = src["sub"]
    url = f"https://www.reddit.com/r/{sub}/top.json?t=day&limit={src.get('limit', 6) * 2}"
    try:
        data = fetch_json(url)
    except Exception as e:
        print(f"[feed_scan] reddit r/{sub} unavailable ({e}); needs OAuth creds — skipping",
              file=sys.stderr)
        return []
    if not isinstance(data, dict) or "data" not in data:
        print(f"[feed_scan] reddit r/{sub} returned non-JSON (blocked); needs OAuth — skipping",
              file=sys.stderr)
        return []
    out = []
    for c in data["data"].get("children", []):
        d = c.get("data", {})
        out.append({
            "id": "reddit-" + d.get("id", ""),
            "title": _clip(d.get("title") or "", 220),
            "url": "https://www.reddit.com" + d.get("permalink", ""),
            "published": str(d.get("created_utc", "")),
            "summary": f"▲{d.get('ups', 0)} · {d.get('num_comments', 0)} comments · "
                       + _clip(d.get("selftext") or "", 300),
        })
        if len(out) >= src.get("limit", 6):
            break
    return out


COLLECTORS = {
    "rss": collect_rss, "hn": collect_hn, "hf_models": collect_hf_models,
    "hf_papers": collect_hf_papers, "reddit": collect_reddit,
}


def main() -> int:
    ap = argparse.ArgumentParser(description="Persona-tagged incremental feed scanner")
    ap.add_argument("--all", action="store_true", help="ignore the seen cache")
    ap.add_argument("--no-update", action="store_true", help="don't write the seen cache")
    ap.add_argument("--persona", help="only this persona (builder/researcher/investor/operator)")
    ap.add_argument("--source", help="only this source name")
    args = ap.parse_args()

    seen = set()
    if SEEN_PATH.exists() and not args.all:
        try:
            seen = set(json.loads(SEEN_PATH.read_text()))
        except Exception:
            seen = set()

    digest: dict[str, list] = {}
    errors = []
    new_ids = []
    for src in SOURCES:
        if args.persona and src["persona"] != args.persona:
            continue
        if args.source and src["name"] != args.source:
            continue
        collector = COLLECTORS.get(src["type"])
        if not collector:
            continue
        try:
            items = collector(src)
        except Exception as e:
            errors.append({"source": src["name"], "error": str(e)})
            continue
        fresh = [it for it in items if it["id"] not in seen]
        for it in fresh:
            new_ids.append(it["id"])
            it["source"] = src["name"]
            it["persona"] = src["persona"]
            digest.setdefault(src["persona"], []).append(it)

    out = {
        "new_items": sum(len(v) for v in digest.values()),
        "by_persona": digest,
        "errors": errors,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))

    if not args.no_update and not args.source and not args.persona:
        merged = list(seen) + new_ids
        SEEN_PATH.write_text(json.dumps(merged[-3000:], indent=0))  # bound growth
    return 0


if __name__ == "__main__":
    sys.exit(main())
