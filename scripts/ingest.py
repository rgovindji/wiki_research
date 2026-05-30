#!/usr/bin/env python3
"""Ingest pipeline: URL or file → raw/ → Anthropic-generated source summary → sources/.

This automates the CLAUDE.md ingest workflow. It does NOT modify wiki pages —
those edits stay manual to keep editorial judgement in the loop. The Anthropic
summary names every wiki page it would touch so you can review before applying.

Usage:
    python scripts/ingest.py <URL>              # fetch URL, save raw, summarize
    python scripts/ingest.py path/to/file.md    # read local file, summarize
    python scripts/ingest.py <URL> --dry-run    # fetch + show plan, no writes
    python scripts/ingest.py <URL> --slug my-slug --type article

Env:
    ANTHROPIC_API_KEY   required for the summarization step
    INGEST_MODEL        override model (default: claude-opus-4-7)

The script is intentionally idempotent: re-running on the same URL with the
same date+slug overwrites the raw file but never the source summary unless
--force is passed.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "raw"
SOURCES_DIR = REPO_ROOT / "sources"
WIKI_DIR = REPO_ROOT / "wiki"

# Map of suffix → raw/ subdirectory.
RAW_SUBDIRS = {
    "article": "articles",
    "podcast": "podcasts",
    "filing": "filings",
    "report": "reports",
}

SUMMARY_SYSTEM_PROMPT = """You are an editorial AI maintaining the user's Investing
wiki. The user is a long-term equity investor focused on AI / semis / Mag 7.

You will be given the raw content of a source (article, podcast transcript,
filing, or report). Produce a wiki-format source summary in markdown following
this exact structure:

```
---
date: YYYY-MM-DD
type: {type}
publisher: {publisher}
url: {url}
raw_path: {raw_path}
touches: [comma-separated wiki page names you would update]
---

# {Title}

## TL;DR
- 3-7 bullets capturing the most important data points and claims

## Key facts (verbatim where possible)
- specific numbers, dates, quotes, with attribution

## Key claims (and confidence)
| Claim | Confidence | Notes |
|---|---|---|
| ... | High / Medium / Low | ... |

## Quotes worth keeping
> direct verbatim quotes

## Wiki updates that should be made
- **[[PageName]]**: what to change and why
- (one bullet per touched page)

## Cross-references
- [[other-relevant-source-or-page]]
```

Hard rules:
- Cite the date of every metric inline.
- Connect-the-dots writing — every analytical statement gets a "Which means..."
  implication line.
- Flag contradictions with existing wiki claims explicitly. Do NOT silently
  overwrite.
- If the source is paywalled or copyrighted, do not reproduce more than
  short fair-use quotes.

Output ONLY the markdown source summary. Do not preface with explanation."""


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    s = re.sub(r"\s+", "-", s)
    return s[:80] or "untitled"


def today() -> str:
    return dt.date.today().isoformat()


def fetch_url(url: str) -> tuple[str, str]:
    """Return (raw_text, derived_title). Uses stdlib only."""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; InvestingWikiIngest/1.0)",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read()
    except urllib.error.URLError as e:
        raise SystemExit(f"[ingest] fetch failed: {e}")
    # Decode reasonably
    encoding = "utf-8"
    if "charset=" in content_type:
        encoding = content_type.split("charset=", 1)[1].split(";", 1)[0].strip()
    text = raw.decode(encoding, errors="replace")
    # Strip script/style + collapse to readable text for HTML pages
    if "html" in content_type or text.lstrip().startswith("<"):
        # Title
        title_m = re.search(r"<title>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
        title = title_m.group(1).strip() if title_m else url
        # Remove scripts/styles
        text = re.sub(r"<script[^>]*>.*?</script>", " ", text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.IGNORECASE | re.DOTALL)
        # Block-level → newline
        text = re.sub(r"</(p|div|h[1-6]|li|tr|article|section)>", "\n", text, flags=re.IGNORECASE)
        text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
        # Strip tags
        text = re.sub(r"<[^>]+>", " ", text)
        # Decode common entities
        for ent, ch in {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"', "&#39;": "'", "&nbsp;": " "}.items():
            text = text.replace(ent, ch)
        # Whitespace
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text).strip()
        return text, title
    return text, url


def save_raw(content: str, slug: str, source_type: str, url: str) -> Path:
    subdir = RAW_SUBDIRS.get(source_type, "articles")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    target_dir = RAW_DIR / subdir
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / f"{today()}-{slug}.md"
    header = f"<!--\nsource_url: {url}\nfetched_at: {dt.datetime.now().isoformat()}\n-->\n\n"
    path.write_text(header + content, encoding="utf-8")
    return path


def list_wiki_pages() -> list[str]:
    """Return the set of wiki page basenames (without .md) to hint the model."""
    pages = []
    for p in WIKI_DIR.rglob("*.md"):
        pages.append(p.stem)
    return sorted(set(pages))


def call_anthropic(raw_text: str, source_type: str, publisher: str, url: str, raw_path: Path) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit(
            "[ingest] ANTHROPIC_API_KEY not set. "
            "Export it in your shell or .env. Skipping summarization step.\n"
            "To still save the raw + open a blank source summary, pass --no-llm."
        )
    try:
        from anthropic import Anthropic  # type: ignore
    except ImportError:
        raise SystemExit(
            "[ingest] anthropic Python SDK not installed.\n"
            "Run: pip install anthropic\n"
            "Or pass --no-llm to skip summarization."
        )
    model = os.environ.get("INGEST_MODEL", "claude-opus-4-7")
    client = Anthropic(api_key=api_key)
    # Truncate very long inputs (200k context window plenty, but stay safe)
    if len(raw_text) > 180000:
        raw_text = raw_text[:180000] + "\n\n[... truncated for length ...]"
    wiki_pages = list_wiki_pages()
    user = (
        f"Source type: {source_type}\nPublisher: {publisher}\nURL: {url}\n"
        f"Raw path (local): {raw_path.relative_to(REPO_ROOT)}\n\n"
        f"Existing wiki page basenames (use exact names in [[wikilinks]] when relevant):\n"
        f"{', '.join(wiki_pages)}\n\n"
        f"--- BEGIN RAW SOURCE ---\n{raw_text}\n--- END RAW SOURCE ---"
    )
    print(f"[ingest] calling {model} ({len(raw_text):,} chars input)…", file=sys.stderr)
    response = client.messages.create(
        model=model,
        max_tokens=8000,
        system=SUMMARY_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user}],
    )
    parts = [b.text for b in response.content if getattr(b, "type", None) == "text"]
    return "".join(parts).strip()


def open_in_editor(path: Path) -> None:
    editor = os.environ.get("EDITOR", "")
    if editor:
        os.system(f"{editor} '{path}'")
    else:
        print(f"[ingest] EDITOR not set — open {path} manually to review/edit", file=sys.stderr)


def detect_publisher(url: str) -> str:
    m = re.match(r"https?://([^/]+)/", url + "/")
    if not m:
        return "unknown"
    host = m.group(1).removeprefix("www.")
    # Trim common subdomains
    return host


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Ingest a URL or file → raw/ + sources/ summary")
    p.add_argument("source", help="URL or local file path")
    p.add_argument("--type", choices=list(RAW_SUBDIRS.keys()), default="article")
    p.add_argument("--slug", help="override slug (default: derived from title)")
    p.add_argument("--publisher", help="override publisher (default: derived from URL host)")
    p.add_argument("--dry-run", action="store_true", help="print plan; write nothing")
    p.add_argument("--no-llm", action="store_true", help="skip Anthropic; just save raw + blank summary template")
    p.add_argument("--force", action="store_true", help="overwrite existing source summary")
    args = p.parse_args(argv)

    src = args.source
    is_url = src.startswith("http://") or src.startswith("https://")

    if is_url:
        print(f"[ingest] fetching {src}")
        text, title = fetch_url(src)
        publisher = args.publisher or detect_publisher(src)
        url = src
    else:
        path = Path(src).expanduser().resolve()
        if not path.exists():
            print(f"[ingest] file not found: {path}", file=sys.stderr)
            return 1
        text = path.read_text(encoding="utf-8", errors="replace")
        title = path.stem
        publisher = args.publisher or "user-provided"
        url = f"file://{path}"

    slug = args.slug or slugify(title.split("|")[0].split("-", 1)[-1].strip())
    print(f"[ingest] title={title!r} slug={slug!r} publisher={publisher!r}")
    if args.dry_run:
        print(f"[ingest] dry-run; raw would go to raw/{RAW_SUBDIRS[args.type]}/{today()}-{slug}.md")
        print(f"[ingest] source summary would go to sources/{today()}-{slug}.md")
        print(f"[ingest] {len(text):,} chars of source text")
        return 0

    raw_path = save_raw(text, slug, args.type, url)
    print(f"[ingest] raw saved: {raw_path.relative_to(REPO_ROOT)}")

    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    source_path = SOURCES_DIR / f"{today()}-{slug}.md"
    if source_path.exists() and not args.force:
        print(f"[ingest] source summary already exists: {source_path.relative_to(REPO_ROOT)}")
        print("[ingest] pass --force to overwrite")
        return 0

    if args.no_llm:
        template = (
            f"---\ndate: {today()}\ntype: {args.type}\npublisher: {publisher}\nurl: {url}\n"
            f"raw_path: {raw_path.relative_to(REPO_ROOT)}\ntouches: []\n---\n\n"
            f"# {title}\n\n## TL;DR\n- ...\n\n## Key facts\n- ...\n\n"
            f"## Quotes worth keeping\n> ...\n\n## Wiki updates made\n- ...\n"
        )
        source_path.write_text(template, encoding="utf-8")
        print(f"[ingest] blank template saved: {source_path.relative_to(REPO_ROOT)}")
        open_in_editor(source_path)
        return 0

    try:
        summary = call_anthropic(text, args.type, publisher, url, raw_path)
    except SystemExit as e:
        # Still useful: save the raw and exit non-zero so user can rerun with --no-llm
        print(str(e), file=sys.stderr)
        return 2

    source_path.write_text(summary + "\n", encoding="utf-8")
    print(f"[ingest] source summary saved: {source_path.relative_to(REPO_ROOT)}")

    # Suggest cross-references: extract [[Names]] from the summary so user can scan
    refs = sorted({m.group(1) for m in re.finditer(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", summary)})
    if refs:
        print(f"\n[ingest] suggested cross-references ({len(refs)}):")
        for r in refs:
            print(f"  [[{r}]]")
    print("\n[ingest] next: review the summary, then update wiki pages manually.")
    print("[ingest] re-index search: python scripts/wikidb.py build")
    return 0


if __name__ == "__main__":
    sys.exit(main())
