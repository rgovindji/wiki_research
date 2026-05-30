# scripts/ — wiki tooling

Three small Python tools that automate the heavy lifting of the wiki workflow.
Each is single-file, stdlib-first, no heavyweight frameworks.

| Tool | What it does |
|---|---|
| `wikidb.py` | SQLite FTS5 index over `wiki/` + `sources/` (full-text search) |
| `ingest.py` | URL or file → `raw/` + Anthropic-generated source summary |
| `daily_email.py` | Render the latest log entry as styled HTML and email it via Gmail SMTP |

## Setup

Python 3.11+ recommended (we use it on 3.12). All three tools work without any pip installs, except `ingest.py` needs the `anthropic` package for the summarization step.

```bash
# (optional) virtualenv
python3 -m venv .venv && source .venv/bin/activate

# only needed if you want ingest.py to call Anthropic
pip install -r scripts/requirements.txt
```

Copy the env template and fill in secrets:

```bash
cp scripts/.env.example .env
$EDITOR .env
```

`.env` is gitignored. Both `daily_email.py` and `ingest.py` will load it from the repo root automatically.

## 1. `wikidb.py` — FTS5 search

```bash
# Build/refresh the index (run after editing wiki or adding sources)
python scripts/wikidb.py build

# Full-text search; supports FTS5 query syntax
python scripts/wikidb.py search "MLCC bottleneck"
python scripts/wikidb.py search '"vera rubin" OR "GB300"'
python scripts/wikidb.py search "anthropic AND valuation"

# Pages that have changed on disk since last index build
python scripts/wikidb.py stale

# Index stats + most-referenced wiki link targets
python scripts/wikidb.py stats

# Show a page's frontmatter + wikilinks
python scripts/wikidb.py page MU
python scripts/wikidb.py page wiki/sectors/mlcc.md
```

The DB lives at `wiki.db` at the repo root (gitignored). Default scope is `wiki/` + `sources/`. To also index the gitignored `raw/` directory locally, run with `--include-raw` or set `RAW_INDEX=1`.

## 2. `ingest.py` — URL/file → source summary

Automates the ingest half of the CLAUDE.md workflow. It deliberately stops short of editing wiki pages — those edits stay manual to keep editorial judgement in the loop. The generated summary lists every wiki page it would touch in a "Wiki updates that should be made" section so you can review and apply them yourself.

```bash
# Fetch an article, save to raw/, call Anthropic for a wiki-format summary
python scripts/ingest.py "https://example.com/article" --type article

# Ingest a local transcript file as a podcast summary
python scripts/ingest.py ~/Downloads/transcript.txt --type podcast --slug my-pod-2026-05-29

# Just save the raw + open a blank summary template (no LLM)
python scripts/ingest.py "https://..." --no-llm

# Preview the plan without writing anything
python scripts/ingest.py "https://..." --dry-run
```

Outputs:
- `raw/{articles|podcasts|filings|reports}/YYYY-MM-DD-slug.md` — full source content (gitignored)
- `sources/YYYY-MM-DD-slug.md` — wiki-format summary, ready to commit

After ingest, the script prints every `[[wikilink]]` the summary contains as a checklist of pages to update. Re-run `python scripts/wikidb.py build` to add the new summary to the search index.

## 3. `daily_email.py` — log entry → styled HTML email

Pulls the most recent `## [YYYY-MM-DD] type | title` block from `log.md`, converts it to HTML with the wiki's dark-glass aesthetic, and sends to your inbox via Gmail SMTP.

```bash
# Preview without sending (HTML to stdout)
python scripts/daily_email.py --dry-run

# Preview and save HTML to disk for browser inspection
python scripts/daily_email.py --dry-run --save /tmp/preview.html

# Send the latest daily-update entry
python scripts/daily_email.py

# Send a specific date
python scripts/daily_email.py --date 2026-05-27

# Send any entry type (default filter is daily/analysis/earnings/ingest/research)
python scripts/daily_email.py --type all

# Override the recipient
python scripts/daily_email.py --to someone@else.com
```

### Gmail App Password setup

Gmail SMTP requires an **App Password**, not your account password. Steps:

1. Enable 2-Step Verification on your Google account (required for App Passwords)
2. Visit https://myaccount.google.com/apppasswords
3. Create an app password named "Investing Wiki" or similar
4. Copy the 16-character password into `.env` as `GMAIL_APP_PASSWORD`

The script never logs the password and never writes it to disk.

## Suggested workflow: one-command daily update

After your daily-update session in Claude Code, the typical flow is:

```bash
# 1. (in Claude Code) — the daily update runs, log.md is appended, commit lands
# 2. Re-index search after commit
python scripts/wikidb.py build

# 3. Email yourself the summary
python scripts/daily_email.py
```

If you want this as one command, add to your shell:

```bash
alias wiki-mail='cd ~/Projects/Investing && python3 scripts/wikidb.py build && python3 scripts/daily_email.py'
```

## Scheduling (optional)

To get the daily email automatically every weekday at 5 PM, add a launchd or cron job:

```bash
# crontab -e
0 17 * * 1-5 cd /Users/rgovindji/Projects/Investing && /usr/bin/python3 scripts/daily_email.py >> /tmp/wiki_email.log 2>&1
```

(The script returns non-zero if the latest entry is older than today, so cron emails won't spam you with stale content.)

## Why no python-dotenv / markdown / requests

These tools are intentionally stdlib-only (except `anthropic` for the optional LLM step) so they keep working when you switch Python versions, on a fresh machine, or in any CI environment. The `.env` loader and markdown→HTML renderer are small and inlined.

If you outgrow the inlined markdown renderer (e.g., need GitHub-flavored task lists, footnotes, math), swap in `python-markdown` or `markdown-it-py` — `daily_email.py`'s `markdown_to_html()` function is the only place to edit.
