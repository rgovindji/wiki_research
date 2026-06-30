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
import os
import subprocess
import sys
import urllib.request
import urllib.parse
from pathlib import Path
from xml.etree import ElementTree as ET

REPO = Path(__file__).resolve().parents[1]
SEEN_PATH = REPO / ".feeds_seen.json"
UA = "investing-wiki-feedscan/1.0 (+research; contact rgovindji)"
# Reddit blocks our IP directly, so reddit sources route through Webshare proxies with a
# browser UA. Reddit's own .json is the data source — the proxy only changes the source IP.
REDDIT_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
             "(KHTML, like Gecko) Chrome/121.0 Safari/537.36")
_PROXIES = None


def load_env() -> None:
    env = REPO / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip().strip("'\""))

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
    {"name": "r-wallstreetbets", "persona": "investor", "type": "reddit", "sub": "wallstreetbets", "limit": 5, "sort": "hot"},
    {"name": "r-investing", "persona": "investor", "type": "reddit", "sub": "investing", "limit": 4},
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


def socks_proxy() -> str | None:
    """Webshare rotating residential SOCKS5 endpoint from WEBSHARE_PROXY_USER/PASS.
    (Reddit 403s its .json everywhere now and the HTTP proxy can't CONNECT for TLS;
    the residential SOCKS5 endpoint + Reddit's still-public .rss feed is the way in.)"""
    u = os.environ.get("WEBSHARE_PROXY_USER")
    p = os.environ.get("WEBSHARE_PROXY_PASS")
    if not (u and p):
        return None
    host = os.environ.get("WEBSHARE_PROXY_HOST", "p.webshare.io")
    port = os.environ.get("WEBSHARE_PROXY_PORT", "1080")
    return f"socks5h://{u}:{p}@{host}:{port}"


def fetch_via_proxy(url: str, ua: str = REDDIT_UA, timeout: int = 30, retries: int = 3) -> str:
    """Fetch through the rotating SOCKS5 proxy via curl. We shell out to curl (not requests)
    because Reddit fingerprints and 403s Python's TLS stack, while curl's passes cleanly."""
    proxy = socks_proxy()
    if not proxy:
        raise RuntimeError("no proxy configured (WEBSHARE_PROXY_USER/PASS)")
    cmd = ["curl", "-s", "--max-time", str(timeout), "--proxy", proxy,
           "-A", ua, "-H", "Accept-Language: en-US,en;q=0.9", "-w", "\n%{http_code}", url]
    last = "no attempt"
    for _ in range(retries):
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
        except Exception as e:
            last = str(e)
            continue
        out = res.stdout
        nl = out.rfind("\n")
        body, code = (out[:nl], out[nl + 1:].strip()) if nl != -1 else (out, "")
        if code == "200" and body.strip():
            return body
        last = f"HTTP {code or '?'}"
    raise RuntimeError(f"{retries} curl attempts failed (last: {last})")


def parse_feed(xml: str, limit: int) -> list[dict]:
    """Parse RSS 2.0 or Atom into {id, title, url, published, summary}."""
    root = ET.fromstring(xml)
    items = []
    for it in root.iter("item"):  # RSS 2.0
        link = (it.findtext("link") or "").strip()
        guid = (it.findtext("guid") or link).strip()
        items.append({
            "id": guid or link,
            "title": _clip(it.findtext("title") or "", 220),
            "url": link,
            "published": (it.findtext("pubDate") or "").strip(),
            "summary": _clip(it.findtext("description") or ""),
        })
    if not items:  # Atom (Reddit's .rss is Atom)
        ns = "{http://www.w3.org/2005/Atom}"
        for e in root.iter(f"{ns}entry"):
            link_el = e.find(f"{ns}link")
            link = (link_el.get("href") if link_el is not None else "") or ""
            items.append({
                "id": (e.findtext(f"{ns}id") or link).strip(),
                "title": _clip(e.findtext(f"{ns}title") or "", 220),
                "url": link,
                "published": (e.findtext(f"{ns}updated") or e.findtext(f"{ns}published") or "").strip(),
                "summary": _clip(e.findtext(f"{ns}content") or e.findtext(f"{ns}summary") or ""),
            })
    return items[:limit]


def _clip(s: str, n: int = 400) -> str:
    s = " ".join((s or "").split())
    return s[:n] + ("…" if len(s) > n else "")


# ── per-type collectors: each returns list of {id, title, url, published, summary} ──

def collect_rss(src: dict) -> list[dict]:
    xml = fetch(src["url"], accept="application/rss+xml, application/xml, text/xml")
    return parse_feed(xml, src.get("limit", 8))


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
    # Reddit 403s its .json everywhere; the still-public .rss feed via residential SOCKS5 works.
    sub = src["sub"]
    limit = src.get("limit", 6)
    if not socks_proxy():
        print(f"[feed_scan] reddit r/{sub}: no WEBSHARE_PROXY_USER/PASS — skipping", file=sys.stderr)
        return []
    sort = src.get("sort", "top")
    url = (f"https://www.reddit.com/r/{sub}/.rss" if sort == "hot"
           else f"https://www.reddit.com/r/{sub}/{sort}/.rss?t=day")
    try:
        xml = fetch_via_proxy(url)
    except Exception as e:
        print(f"[feed_scan] reddit r/{sub} via proxy failed ({e}) — skipping", file=sys.stderr)
        return []
    items = parse_feed(xml, limit)
    for it in items:
        it["id"] = "reddit-" + (it["id"] or it["url"])
        it["summary"] = f"r/{sub} · " + (it["summary"] or "")
    return items


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
    load_env()

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
