# scripts/ — wiki tooling

Four single-file Python tools that automate the wiki workflow. Stdlib-first.

| Tool | What it does |
|---|---|
| `wikidb.py` | SQLite FTS5 index over `wiki/` + `sources/` (full-text search) |
| `ingest.py` | URL or file → `raw/` + Anthropic-generated source summary |
| `run_daily_update.py` | **Full Claude-driven daily update** — sweeps news via Anthropic web_search, writes source summaries + wiki appends + log entry |
| `daily_email.py` | Render the latest log entry as styled HTML and email it (AWS SES or Gmail SMTP) |

These run locally OR inside the **GitHub Actions workflow** at `.github/workflows/daily-update.yml` for fully unattended daily execution. See [Hosted automation](#hosted-automation) below.

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

## 3. `run_daily_update.py` — Claude-driven daily research sweep

Calls the Anthropic API with the `web_search` tool and a strict system prompt that mirrors the human daily-update workflow. Claude does the discover → curate → propose loop and returns a single JSON object the script deterministically writes to disk.

```bash
# Local dry-run (calls Claude, prints plan, writes nothing)
python scripts/run_daily_update.py --dry-run

# Full local run (writes source summaries + wiki appends + log entry)
python scripts/run_daily_update.py

# Save the raw JSON plan for debugging
python scripts/run_daily_update.py --save-plan /tmp/plan.json
```

What it writes:
- `sources/YYYY-MM-DD-slug.md` — new source summaries (only if file doesn't already exist)
- Inserts bullet entries right after named `## Recent developments` headings in existing wiki pages (never modifies frontmatter or other sections)
- Prepends a new `## [YYYY-MM-DD] daily | <title>` block to `log.md`

What it never does:
- Flip stance or conviction in any wiki page (per house rules — flagged in log entry as "needs user sign-off")
- Modify wiki page frontmatter
- Create new wiki pages (only adds to existing ones)
- Push to git (the GitHub Actions workflow handles that step)

Env: `ANTHROPIC_API_KEY` required. `ANTHROPIC_MODEL` optional override.

## 4. `daily_email.py` — log entry → styled HTML email (SES or SMTP)

Pulls the most recent `## [YYYY-MM-DD] type | title` block from `log.md`, converts it to HTML with the wiki's dark-glass aesthetic, and sends it via **AWS SES (recommended)** or **Gmail SMTP**.

```bash
# Preview without sending (HTML to stdout)
python scripts/daily_email.py --dry-run

# Preview and save HTML to disk for browser inspection
python scripts/daily_email.py --dry-run --save /tmp/preview.html

# Send via SES (default if EMAIL_BACKEND=ses in .env)
python scripts/daily_email.py

# Force a specific backend
python scripts/daily_email.py --backend ses
python scripts/daily_email.py --backend smtp

# Send a specific date
python scripts/daily_email.py --date 2026-05-27

# Send any entry type (default filter is daily/analysis/earnings/ingest/research)
python scripts/daily_email.py --type all

# Override the recipient
python scripts/daily_email.py --to someone@else.com
```

### AWS SES setup (recommended)

Set `EMAIL_BACKEND=ses` and `SES_SENDER` to a verified SES identity. The script uses the standard boto3 credentials chain (env vars, `~/.aws/credentials`, IAM role, etc.) — no explicit keys in the script.

List your verified identities:

```bash
aws sesv2 list-email-identities --region us-east-1
```

Verify a new sender:

```bash
aws sesv2 create-email-identity --email-identity wiki@yourdomain.com --region us-east-1
# then click the verification link from AWS in your inbox
```

If your account is in SES sandbox mode you'll also need to verify each recipient. The default config in this repo (account `637776813930`) is in **production** mode (50K/day, 14/sec) so any recipient works without per-recipient verification.

### Gmail App Password setup (fallback)

If you'd rather use Gmail SMTP, set `EMAIL_BACKEND=smtp` and:

1. Enable 2-Step Verification on the Google account
2. Visit https://myaccount.google.com/apppasswords
3. Create an app password and put it in `.env` as `GMAIL_APP_PASSWORD`

The script never logs the password and never writes secrets to disk.

## Suggested workflow: one-command daily update (local)

After your daily-update session in Claude Code, the typical flow is:

```bash
# 1. (in Claude Code) — the daily update runs, log.md is appended, commit lands
# 2. Re-index search after commit
python scripts/wikidb.py build

# 3. Email yourself the summary
python scripts/daily_email.py
```

If you want this as one command:

```bash
alias wiki-mail='cd ~/Projects/Investing && python3 scripts/wikidb.py build && python3 scripts/daily_email.py'
```

## Hosted automation

`.github/workflows/daily-update.yml` runs the full pipeline unattended on a schedule. Default cadence: **22:00 UTC on weekdays** (18:00 EDT / 17:00 EST). Also runnable on-demand via the GitHub Actions "Run workflow" button.

What the workflow does (in order):
1. Checks out the repo
2. Sets up Python 3.12, installs `boto3` + `anthropic`
3. Runs `python scripts/run_daily_update.py` — Claude does the discover/curate/propose loop and writes the day's source summaries + wiki appends + log entry
4. Commits any changes back to `main` as `wiki-bot <wiki-bot@decideai.xyz>`
5. Pushes
6. Runs `python scripts/daily_email.py` — emails the latest log entry via SES

### One-time GitHub Secrets setup

Go to **Settings → Secrets and variables → Actions → New repository secret** for each:

| Secret | Value | Where to get it |
|---|---|---|
| `ANTHROPIC_API_KEY` | `sk-ant-...` | https://console.anthropic.com/settings/keys |
| `AWS_ACCESS_KEY_ID` | IAM user with `ses:SendEmail` | Create in IAM console (see below) |
| `AWS_SECRET_ACCESS_KEY` | matching secret key | shown once at IAM user creation |
| `SES_SENDER` | `wiki@decideai.xyz` | already verified in your account |
| `EMAIL_TO` | `rgovindji@gmail.com` | the recipient |
| `AWS_REGION` *(optional)* | `us-east-1` | default if omitted |
| `ANTHROPIC_MODEL` *(optional)* | `claude-opus-4-7` | default if omitted |

### Recommended IAM policy (minimum send permission)

Create a dedicated IAM user (e.g. `wiki-bot-github`) with only this attached policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SESSend",
      "Effect": "Allow",
      "Action": ["ses:SendEmail", "ses:SendRawEmail"],
      "Resource": "*"
    }
  ]
}
```

Then generate access keys for that user and paste them into the GitHub secrets. Rotate periodically.

### Schedule customization

Edit the `cron` line in `.github/workflows/daily-update.yml`:

```yaml
on:
  schedule:
    - cron: '0 22 * * 1-5'   # 22:00 UTC weekdays
    # - cron: '0 13 * * 1-5' # 09:00 EDT / pre-market
    # - cron: '30 21 * * 1-5'# 17:30 EDT / market close
```

GitHub Actions cron uses UTC. Multiple `cron` lines are allowed.

### Manual / debug runs

In the Actions UI, choose **"Daily wiki update" → Run workflow** and you'll see:

- `send_email`: toggle to skip the email step
- `email_to`: override the recipient for that one run
- `skip_update`: skip the Claude API call and just email whatever the latest log entry already is

This is useful for testing the email pipeline without burning API tokens.

### Cost guard rails

- The Anthropic call uses `claude-opus-4-7` with up to 12 `web_search` uses; per-run cost is typically <$1 unless you increase `max_uses` or `max_tokens` in `run_daily_update.py`
- AWS SES at production volume: $0.10 per 1,000 emails — effectively free for daily personal use
- GitHub Actions on private repos: 2,000 free minutes/month on the free tier; each daily run takes ~3-5 min

## Why no python-dotenv / markdown / requests

These tools are intentionally stdlib-first (with `boto3` and `anthropic` as the only third-party deps) so they keep working when you switch Python versions, on a fresh machine, or in any CI environment. The `.env` loader and markdown→HTML renderer are small and inlined.

If you outgrow the inlined markdown renderer (e.g., need GitHub-flavored task lists, footnotes, math), swap in `python-markdown` or `markdown-it-py` — `daily_email.py`'s `markdown_to_html()` function is the only place to edit.
