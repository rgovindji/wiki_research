#!/usr/bin/env python3
"""Scan SemiWiki for new articles + forum threads and emit a digest.

Headless (plain HTTP, no browser) so it runs inside the scheduled daily
close run. Pulls the homepage, finds recent article + forum-thread links,
fetches each one's text, and prints a JSON digest. An incremental "seen"
cache (.semiwiki_seen.json, gitignored) means each run only surfaces
genuinely NEW pieces — so the daily wiki run can read EVERYTHING new
without re-reviewing the same 25 articles daily.

Per the curator's instruction (2026-06-14): do NOT pre-filter for
"importance" — surface the long tail so the daily run can catch
diamond-in-the-rough details. Curation happens in the wiki run, not here.

Usage:
    python3 scripts/semiwiki_scan.py                 # new items since last run
    python3 scripts/semiwiki_scan.py --all           # ignore seen cache
    python3 scripts/semiwiki_scan.py --limit 40      # cap items fetched
    python3 scripts/semiwiki_scan.py --no-update      # don't write seen cache
    python3 scripts/semiwiki_scan.py --chars 4000     # text length per item

Exit 0 always (a scan failure must not break the daily run); errors land
in the JSON under "errors".
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SEEN_PATH = REPO / ".semiwiki_seen.json"
HOME = "https://semiwiki.com/"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}

ARTICLE_RE = re.compile(
    r"https://semiwiki\.com/(?:eda|ip|semiconductor[\w-]*|artificial-intelligence|"
    r"semiconductor-manufacturers|semiconductor-services|forum/threads)/[\w./-]*?\d{3,}[\w./-]*",
    re.I)
JUNK_SUBSTRINGS = ("WP_Term", "term_id", "taxonomy", "[filter]", "category_", "cat_ID",
                   "term_group", "term_taxonomy", "Follow along with the video",
                   "View Profile", "View Forum Posts", "View Articles", "Private Message",
                   "install our site as a web app")


def fetch(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")


def clean_text(raw_html: str, url: str, max_chars: int) -> str:
    # Forum threads (XenForo): the first post body is in <div class="bbWrapper">.
    if "/forum/threads/" in url:
        blocks = re.findall(r'<div class="bbWrapper">(.*?)</div>\s*</article>', raw_html, re.S)
        if not blocks:
            blocks = re.findall(r'<div class="bbWrapper">(.*?)</div>', raw_html, re.S)
        chunks = []
        for b in blocks[:3]:
            t = html.unescape(re.sub(r"<[^>]+>", " ", b))
            t = re.sub(r"\s+", " ", t).strip()
            if len(t) > 40 and not any(j in t for j in JUNK_SUBSTRINGS):
                chunks.append(t)
        if chunks:
            return " ".join(chunks)[:max_chars]
    # WordPress articles: paragraph text.
    paras = re.findall(r"<p[^>]*>(.*?)</p>", raw_html, re.S | re.I)
    out = []
    for p in paras:
        t = html.unescape(re.sub(r"<[^>]+>", "", p)).strip()
        if len(t) < 50 or any(j in t for j in JUNK_SUBSTRINGS):
            continue
        out.append(t)
    if out:
        return " ".join(out)[:max_chars]
    # Last resort: og:description (works for forum + article).
    m = re.search(r'<meta property="og:description" content="([^"]+)"', raw_html)
    return html.unescape(m.group(1)).strip()[:max_chars] if m else ""


def extract_meta(raw_html: str) -> tuple[str, str]:
    title = ""
    m = re.search(r'<meta property="og:title" content="([^"]+)"', raw_html)
    if m:
        title = html.unescape(m.group(1)).strip()
    if not title:
        m = re.search(r"<title>(.*?)</title>", raw_html, re.S | re.I)
        if m:
            title = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip()
    date = ""
    m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', raw_html)
    if m:
        date = m.group(1)[:10]
    else:
        m = re.search(r"Posted on ([A-Z][a-z]+ \d{1,2}, \d{4})", raw_html)
        if m:
            try:
                date = dt.datetime.strptime(m.group(1), "%B %d, %Y").date().isoformat()
            except ValueError:
                pass
    return title, date


def collect_links(home_html: str, limit: int) -> list[str]:
    seen, ordered = set(), []
    for m in ARTICLE_RE.finditer(home_html):
        u = m.group(0).split("#")[0].rstrip("/")
        # forum thread canonical: strip trailing /page-N etc.
        if "/forum/threads/" in u:
            tm = re.search(r"(/forum/threads/\d+)", u)
            if tm:
                u = "https://semiwiki.com" + tm.group(1)
        if u not in seen:
            seen.add(u)
            ordered.append(u)
        if len(ordered) >= limit * 2:
            break
    return ordered


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="ignore the seen cache")
    ap.add_argument("--limit", type=int, default=30)
    ap.add_argument("--chars", type=int, default=3500)
    ap.add_argument("--no-update", action="store_true", help="don't write the seen cache")
    args = ap.parse_args()

    digest: dict = {"source": "semiwiki.com", "scanned": dt.datetime.now().isoformat(timespec="seconds"),
                    "items": [], "errors": []}
    seen: dict = {}
    if SEEN_PATH.exists() and not args.all:
        try:
            seen = json.loads(SEEN_PATH.read_text())
        except json.JSONDecodeError:
            seen = {}

    try:
        home = fetch(HOME)
    except (urllib.error.URLError, TimeoutError) as e:
        digest["errors"].append(f"homepage fetch failed: {e}")
        print(json.dumps(digest, indent=2))
        return 0

    links = collect_links(home, args.limit)
    new_links = [u for u in links if u not in seen][:args.limit]
    digest["found_total"] = len(links)
    digest["new_count"] = len(new_links)

    today = dt.date.today().isoformat()
    for u in new_links:
        try:
            h = fetch(u)
            title, date = extract_meta(h)
            text = clean_text(h, u, args.chars)
            item = {"url": u, "title": title, "date": date, "text": text}
            if len(text) < 80:
                item["note"] = "thin extract — fetch full page if title looks relevant"
            digest["items"].append(item)
            seen[u] = today
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            digest["errors"].append(f"{u}: {e}")

    if not args.no_update and not args.all:
        # prune cache to last 400 entries to bound growth
        if len(seen) > 400:
            seen = dict(sorted(seen.items(), key=lambda kv: kv[1])[-400:])
        SEEN_PATH.write_text(json.dumps(seen, indent=0))

    print(json.dumps(digest, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
