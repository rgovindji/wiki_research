#!/usr/bin/env python3
"""Claude-driven daily wiki update — runs inside GitHub Actions or locally.

Calls Claude (Anthropic API) with the web_search tool and a strict system
prompt that mirrors the human daily-update workflow. Claude does the news +
earnings + long-form sweep, curates signal vs. noise, and returns a single
JSON object describing exactly what to write:

  {
    "summary_one_liner": "...",            # short title for log entry
    "log_entry_body":    "...",             # markdown body for log.md
    "source_summaries":  [{"path": "sources/...", "content": "..."}, ...],
    "wiki_appends":      [{"path": "wiki/.../X.md", "after_heading": "Recent developments", "content": "..."}, ...]
  }

The script applies those writes deterministically. No automatic stance/
conviction flips — those still need human sign-off per house rules.

Usage:
    python scripts/run_daily_update.py             # full run
    python scripts/run_daily_update.py --dry-run   # print the plan; write nothing
    python scripts/run_daily_update.py --skip-search   # skip web_search tool (testing)

Env:
    ANTHROPIC_API_KEY    required
    ANTHROPIC_MODEL      optional override (default: claude-opus-4-7)
    DAILY_BUDGET_USD     optional cap on max_tokens-equivalent spend per run
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = REPO_ROOT / "log.md"
INDEX_PATH = REPO_ROOT / "index.md"
SOURCES_DIR = REPO_ROOT / "sources"
WIKI_DIR = REPO_ROOT / "wiki"

DEFAULT_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-7")
MAX_TOKENS = 16000

SYSTEM_PROMPT = """You are the editorial AI maintaining rgovindji's Investing wiki.
You are running INSIDE a daily-update workflow that has called you via the
Anthropic API. The user is a long-term equity investor focused on AI / semis /
Mag 7 with tactical 6-18mo swings.

You will be given:
- The current `index.md` (catalog of all wiki pages)
- The last ~80 log entries from `log.md` (so you know what's already been ingested)
- Today's date in UTC

Your job — execute the daily-update ritual without human input:

1. DISCOVER. Use the `web_search` tool to do parallel sweeps of:
   - Top AI / semi / Mag 7 news today and yesterday
   - Earnings prints from wiki tickers in the last 48h
   - Long-form sources (Stratechery, SemiAnalysis, Dwarkesh, BG2, Acquired,
     Invest Like the Best, Odd Lots, Capital Allocators podcasts)
   - 8-K filings; sector-specific tightening signals (memory, GPU rentals,
     fab capacity, power announcements)

2. CURATE. Apply the wiki's signal-vs-noise bar:
   - Ingest only net-new substantive info, contradictions to existing
     wiki claims, long-form deep dives, or conviction-changing data
   - Skip restatements, pure price-action narratives, opinion pieces, click-bait

3. PROPOSE. Output a single JSON object (no prose, no markdown wrapper) with:

   {
     "summary_one_liner": "<concise 6-12 word title for the log entry>",
     "log_entry_body":    "<markdown body for log.md — no heading; the script adds it>",
     "source_summaries":  [
       {
         "path":    "sources/YYYY-MM-DD-slug.md",
         "content": "<full markdown of source summary; include the frontmatter block>"
       }
     ],
     "wiki_appends": [
       {
         "path":           "wiki/companies/TICKER.md",
         "after_heading":  "Recent developments",
         "content":        "- **YYYY-MM-DD** — ... (markdown bullet to insert RIGHT AFTER the heading)"
       }
     ]
   }

HARD RULES:
- Output ONLY the JSON object. No prose before or after. No markdown code fences.
- Use `[[wikilinks]]` for every reference to wiki pages; the wiki page basename
  is the link target (e.g. [[MU]], [[ai-capex-cycle]]).
- Cite the date of every metric inline.
- Connect-the-dots writing: every analytical statement gets a "Which means..."
  implication line.
- DO NOT propose stance or conviction changes — flag them in `log_entry_body`
  as "needs user sign-off" but never write the edit.
- DO NOT modify frontmatter of existing wiki pages — only append to body
  sections via `wiki_appends`.
- If nothing material happened today, return a JSON object with empty
  source_summaries / wiki_appends arrays and a log_entry_body that says
  "Low-signal day — no ingests. Watched: <names>."
- For source summaries: use the CLAUDE.md template (frontmatter with date,
  type, publisher, url, raw_path, touches list; sections: TL;DR, Key facts,
  Key claims with confidence, Quotes worth keeping, Wiki updates that should
  be made, Cross-references).

The script will deterministically write your JSON to disk. Be precise."""


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def tail_log(n: int = 80) -> str:
    if not LOG_PATH.exists():
        return ""
    lines = LOG_PATH.read_text(encoding="utf-8").splitlines()
    # Find the boundaries of the last N "## [date]" blocks
    boundaries = [i for i, ln in enumerate(lines) if ln.startswith("## [")]
    if not boundaries:
        return "\n".join(lines[-400:])
    start = boundaries[-n] if len(boundaries) >= n else boundaries[0]
    return "\n".join(lines[start:])


def list_wiki_pages() -> list[str]:
    return sorted({p.stem for p in WIKI_DIR.rglob("*.md")})


def build_user_message(today: str) -> str:
    index_text = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.exists() else ""
    log_tail = tail_log()
    wiki_pages = list_wiki_pages()
    return (
        f"Today (UTC): {today}\n\n"
        f"=== CURRENT index.md ===\n{index_text}\n\n"
        f"=== RECENT log.md (last entries) ===\n{log_tail}\n\n"
        f"=== WIKI PAGE BASENAMES (use these in [[wikilinks]]) ===\n"
        f"{', '.join(wiki_pages)}\n\n"
        f"Run the daily update workflow and return the JSON object."
    )


def call_claude(model: str, skip_search: bool) -> dict:
    try:
        from anthropic import Anthropic  # type: ignore
    except ImportError:
        raise SystemExit("[daily] anthropic SDK not installed. pip install anthropic")
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("[daily] ANTHROPIC_API_KEY not set")
    client = Anthropic(api_key=api_key)
    today_iso = dt.datetime.utcnow().date().isoformat()
    tools = []
    if not skip_search:
        # Anthropic web_search tool; documented at
        # https://docs.anthropic.com/claude/docs/web-search-tool
        tools = [{"type": "web_search_20250305", "name": "web_search", "max_uses": 12}]
    print(f"[daily] calling {model} (web_search={'on' if tools else 'off'})", file=sys.stderr)
    resp = client.messages.create(
        model=model,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        tools=tools,
        messages=[{"role": "user", "content": build_user_message(today_iso)}],
    )
    text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text").strip()
    # Strip accidental code fences
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```\s*$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print("[daily] model returned invalid JSON — raw output below:", file=sys.stderr)
        print(text[:2000], file=sys.stderr)
        raise SystemExit(f"[daily] JSON decode error: {e}")


def apply_writes(plan: dict, dry_run: bool) -> None:
    # 1. Source summaries — new files
    for s in plan.get("source_summaries", []):
        rel = s.get("path")
        content = s.get("content", "")
        if not rel or not content:
            continue
        target = REPO_ROOT / rel
        if not str(target.resolve()).startswith(str(SOURCES_DIR.resolve())):
            print(f"[daily] refusing to write outside sources/: {rel}", file=sys.stderr)
            continue
        if target.exists():
            print(f"[daily] source summary already exists, skipping: {rel}")
            continue
        if dry_run:
            print(f"[daily] DRY: would write {rel} ({len(content)} chars)")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content + ("\n" if not content.endswith("\n") else ""), encoding="utf-8")
            print(f"[daily] wrote source summary: {rel}")

    # 2. Wiki appends — insert right after a heading line, never replace
    for a in plan.get("wiki_appends", []):
        rel = a.get("path")
        heading = a.get("after_heading")
        content = a.get("content", "").strip()
        if not rel or not heading or not content:
            continue
        target = REPO_ROOT / rel
        if not target.exists() or not str(target.resolve()).startswith(str(WIKI_DIR.resolve())):
            print(f"[daily] wiki page not found or outside wiki/: {rel}", file=sys.stderr)
            continue
        body = target.read_text(encoding="utf-8")
        pattern = re.compile(rf"^(##+ {re.escape(heading)}\s*\n)", re.MULTILINE)
        if not pattern.search(body):
            print(f"[daily] heading {heading!r} not found in {rel}; skipping append", file=sys.stderr)
            continue
        new_body = pattern.sub(rf"\1\n{content}\n", body, count=1)
        if dry_run:
            print(f"[daily] DRY: would append to {rel} under '{heading}' ({len(content)} chars)")
        else:
            target.write_text(new_body, encoding="utf-8")
            print(f"[daily] appended to wiki page: {rel}")

    # 3. Log entry — always at the top of log.md (after the # Log header)
    log_body = plan.get("log_entry_body", "").strip()
    if log_body:
        today = dt.datetime.utcnow().date().isoformat()
        title = plan.get("summary_one_liner", "auto-update").strip() or "auto-update"
        entry = f"## [{today}] daily | {title}\n\n{log_body}\n\n---\n\n"
        existing = LOG_PATH.read_text(encoding="utf-8") if LOG_PATH.exists() else "# Log\n\n"
        # Insert after the first horizontal rule (or after the header block)
        m = re.search(r"^---\s*$", existing, re.MULTILINE)
        if m:
            insertion_point = m.end() + 1
            new_log = existing[:insertion_point] + "\n" + entry + existing[insertion_point:]
        else:
            new_log = existing + "\n" + entry
        if dry_run:
            print(f"[daily] DRY: would prepend log entry [{today}] {title!r}")
        else:
            LOG_PATH.write_text(new_log, encoding="utf-8")
            print(f"[daily] log entry written: [{today}] {title}")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Claude-driven daily wiki update")
    p.add_argument("--dry-run", action="store_true", help="print plan; write nothing")
    p.add_argument("--skip-search", action="store_true", help="skip web_search tool (testing)")
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--save-plan", help="write the raw JSON plan to this path")
    args = p.parse_args(argv)

    load_dotenv(REPO_ROOT / ".env")
    load_dotenv(REPO_ROOT / "scripts" / ".env")

    plan = call_claude(args.model, args.skip_search)

    if args.save_plan:
        Path(args.save_plan).write_text(json.dumps(plan, indent=2), encoding="utf-8")
        print(f"[daily] plan saved to {args.save_plan}")

    n_sources = len(plan.get("source_summaries", []))
    n_appends = len(plan.get("wiki_appends", []))
    print(f"[daily] plan: {n_sources} new source summaries, {n_appends} wiki appends")
    print(f"[daily] one-liner: {plan.get('summary_one_liner', '<none>')}")

    apply_writes(plan, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
