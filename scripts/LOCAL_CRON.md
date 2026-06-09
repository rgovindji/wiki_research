# Local daily newsletters via Claude Code (Max plan)

Two newsletter runs fire on your Mac via launchd each weekday, both using Claude Code (covered by your Anthropic Max plan) and sending email locally via SES with `scripts/render_newsletter.py`:

| Job | Time (local) | Edition | What it does |
|---|---|---|---|
| `com.rgovindji.wiki-morning` | Mon-Fri 06:45 | **Before the Bell** | Light pre-market research → writes + sends the morning brief |
| `com.rgovindji.wiki-daily` | Mon-Fri 17:00 | **After Hours** | Full wiki update (the 8-step ritual) → writes + sends the close-of-market letter |

## Architecture

```
launchd  com.rgovindji.wiki-morning / com.rgovindji.wiki-daily
  └─ scripts/daily_claude.sh --edition {morning|close}
       ├─ git pull --rebase
       ├─ claude -p with scripts/{morning_prompt,daily_prompt}.md  (Max plan — zero marginal cost)
       │    ├─ WebSearch / WebFetch
       │    ├─ (close only) source summaries → sources/, wiki page updates, index.md, log.md
       │    ├─ (close only) market intelligence → newsletter/market_state/DATE.json
       │    │     (gamma levels, VIX/flow, technicals, regime call, event calendar)
       │    ├─ (close only) prediction accounting → newsletter/predictions.json + playbook.md
       │    │     (resolve due calls, write WHY, distill lessons; Friday = weekly distillation)
       │    ├─ (close only) closing prices → newsletter/portfolio.json
       │    └─ writes newsletter/issues/DATE-{morning|afterhours}.md
       ├─ git commit + push
       └─ python3 scripts/render_newsletter.py <issue>   → SES email
            (skipped if the issue file is unchanged from before the run — no duplicate sends)
```

### The self-improvement loop

Three files make the letters compound instead of drift:

- **`newsletter/predictions.json`** — every falsifiable call a letter makes is logged (claim, confidence, horizon, explicit falsifier; max 3/issue). The evening run resolves due calls with a mechanism-level explanation and keeps a calibration tally.
- **`newsletter/market_state/DATE.json`** — the daily dashboard (SPX/SPY gamma levels, VIX + term structure, put/call, unusual options flow, technicals, regime call, key levels, event calendar). Reasoning fuel only — the reader sees conclusions, never the dashboard.
- **`newsletter/playbook.md`** — operating lessons distilled from resolutions, read by both prompts before writing. Hypotheses promote to Active after two confirmations; falsified lessons retire with evidence. Friday runs consolidate.
- **`newsletter/yolo.json`** — the YOLO desk: one defined-risk, paper-only intraday options idea per morning brief, keyed to the levels; the close run resolves it against the tape and keeps the public win/loss record. The renderer turns a `{{LEVELS_CHART}}` token in any issue into a QuickChart PNG of SPX vs the gamma walls/flip and support/resistance from `market_state/`.

Reader-facing effects: a Scorecard section when calls resolve (wrong calls get the autopsy), a plain-English "tomorrow's setup" with levels-and-why, and occasional clearly-fenced high-risk ideas — logged and scored like everything else, never added to the model portfolio.

Voice rules for both letters live in `scripts/newsletter_style.md` (newsletter voice, no wiki references in the reader-facing copy, anti-AI-tell bans). `newsletter/issues/2026-06-01-inception.md` is the canonical voice example.

The old path — AWS Lambda emailing the latest `log.md` entry — is retired but still deployed; nothing invokes it anymore.

## Setup (one-time)

```bash
# 1. Install both launchd jobs
bash scripts/install_daily_cron.sh

# 2. Make sure repo-root .env exists (gitignored) with at least:
#      EMAIL_TO=...   SES_SENDER=wiki@decideai.xyz   AWS_REGION=us-east-1

# 3. (Optional) wake the Mac for the evening run (pmset supports ONE repeating event)
sudo pmset repeat wakeorpoweron MTWRF 16:55:00

# 4. Trigger an immediate test run
bash scripts/install_daily_cron.sh --run-now            # evening
bash scripts/install_daily_cron.sh --run-now-morning    # morning

# 5. Watch logs
tail -f "$(ls -t ~/Library/Logs/wiki-daily/run-*.log | head -1)"
```

Schedules live in `launchd/com.rgovindji.wiki-{morning,daily}.plist`; edit and re-run install to change.

## Day-to-day commands

```bash
# Status of both jobs
bash scripts/install_daily_cron.sh --status

# Manual runs with options
bash scripts/daily_claude.sh                          # full close-of-market run
bash scripts/daily_claude.sh --edition morning        # morning brief run
bash scripts/daily_claude.sh --dry-run                # claude runs but no commit/push/email
bash scripts/daily_claude.sh --skip-email             # commit + push but skip SES
bash scripts/daily_claude.sh --skip-claude            # commit + send whatever's already on disk

# Re-send an issue that's already written
python3 scripts/render_newsletter.py newsletter/issues/2026-06-09-afterhours.md
python3 scripts/render_newsletter.py <issue> --dry-run --save /tmp/preview.html   # preview

# Uninstall both jobs
bash scripts/install_daily_cron.sh --uninstall
sudo pmset repeat cancel    # if you set the wake schedule
```

## What Claude Code is allowed to do

**Evening run** (`scripts/daily_prompt.md`): the full wiki ritual plus the letter —

- **Read**: CLAUDE.md, MEMORY.md, index.md, log.md, watchlist.md, newsletter style guide + recent issues
- **Search/Fetch**: up to ~32 WebSearch / ~10 WebFetch calls
- **Write**: source summaries, `## Recent developments` bullets on existing wiki pages, log.md entry, index.md, `newsletter/portfolio.json` closing prices, `newsletter/market_state/DATE.json`, `newsletter/predictions.json`, `newsletter/playbook.md`, `newsletter/issues/DATE-afterhours.md`
- **Not allowed**: stance flips (flag for sign-off), unilateral conviction changes on high-importance names, new top-level wiki pages, touching MEMORY.md / `.claude/`, changing portfolio holdings or cost bases, inventing prices, committing/pushing (wrapper does it)

**Morning run** (`scripts/morning_prompt.md`): newsletter only —

- **Read**: style guide, recent issues, watchlist/overview as background
- **Search**: ~12 WebSearch / ~4 WebFetch calls (futures, overnight sessions, pre-market movers, today's calendar)
- **Write**: `newsletter/issues/DATE-morning.md` + a one-line log.md note. **No wiki ingestion** — the evening run owns the wiki.

Both invocations use `--dangerously-skip-permissions` because launchd has no user to approve prompts; the prompts constrain the blast radius.

## Logs

| Path | What's in it |
|---|---|
| `~/Library/Logs/wiki-daily/launchd-stdout.log` / `-stderr.log` | launchd's view of the evening job |
| `~/Library/Logs/wiki-daily/launchd-morning-stdout.log` / `-stderr.log` | launchd's view of the morning job |
| `~/Library/Logs/wiki-daily/run-YYYYMMDDTHHMMSSZ-{morning,close}.log` | Per-run structured log from `daily_claude.sh` |
| `~/Library/Logs/wiki-daily/prompt-*.md` | Exact prompt sent to Claude (date substituted) |

## Cost

| Service | Cost |
|---|---|
| Anthropic Max plan | $200/mo (already paying — covers both daily Claude Code runs) |
| AWS SES (2 emails/day) | negligible |
| **Marginal cost vs. doing nothing** | **~$0/mo** (the Lambda is no longer invoked) |

## When the Mac is asleep

`StartCalendarIntervalAcceptsAsleep: true` means launchd queues missed runs and fires on next wake. A 06:45 brief that fires when you open the laptop at 8:00 is still useful (market opens 8:30 CT); a brief that fires at noon is stale but harmless. For guaranteed runs, set the pmset wake schedule (one repeating event only — the evening run gets it by default since it also maintains the wiki):

```bash
sudo pmset repeat wakeorpoweron MTWRF 16:55:00
```

## Failure modes + recovery

| Failure | Effect | Fix |
|---|---|---|
| `git pull` fails (network, conflict) | Script exits 3 before Claude runs | Resolve manually, re-run with `--run-now` |
| Claude Code rate-limited on Max plan | Script exits 4 | Wait + re-run; verify Max plan status |
| Claude wrote a bad letter / stance flip | Commit lands in main; email sends | `git revert HEAD && git push`; iterate on the prompt files |
| Claude didn't write the issue file | Script logs WARNING, sends nothing, exits 0 | Check the run log; re-run, or write the issue by hand and `--skip-claude` |
| `git push` fails | Script exits 5; commit local only | `git push` manually |
| SES send fails | Script exits 6; issue is on disk | `python3 scripts/render_newsletter.py <issue>` after fixing creds |
| Email goes to spam | New sender to your address | Mark as Not Spam; normal for first sends |

## The retired Lambda path

The AWS Lambda (`wiki-daily-update`) that emailed the raw `log.md` entry is still deployed but unused. To remove it entirely, see `aws/README.md`. To temporarily fall back to it:

```bash
aws lambda invoke --function-name wiki-daily-update \
  --payload '{"skip_update":true,"send_email":true}' \
  --cli-binary-format raw-in-base64-out /tmp/out.json
```
