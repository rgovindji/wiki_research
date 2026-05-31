# Local daily-update via Claude Code (Max plan)

The daily wiki update runs on your Mac via launchd, uses Claude Code (covered by your Anthropic Max plan), then triggers the AWS Lambda to send the overview email via SES.

## Architecture

```
launchd  com.rgovindji.wiki-daily
  └─ scripts/daily_claude.sh
       ├─ git pull --rebase
       ├─ claude -p (uses Max plan — zero marginal cost)
       │    ├─ WebSearch / WebFetch
       │    ├─ writes source summaries to sources/
       │    ├─ appends to wiki/ pages
       │    └─ prepends entry to log.md
       ├─ git commit + push
       └─ aws lambda invoke wiki-daily-update (skip_update=true)
              └─ Lambda fetches latest log entry via GitHub API → SES email
```

Why this beats the pure-AWS API setup: zero marginal Anthropic cost — your $200/mo Max plan already covers the daily Claude Code run.

## Setup (one-time)

```bash
# 1. Install the launchd job
bash scripts/install_daily_cron.sh

# 2. (Optional) wake the Mac at 16:55 weekdays so the 17:00 run actually fires
sudo pmset repeat wakeorpoweron MTWRF 16:55:00
# (or pass --wake-mac to the install script)

# 3. Trigger an immediate test run
bash scripts/install_daily_cron.sh --run-now

# 4. Watch logs
tail -f ~/Library/Logs/wiki-daily/launchd-stdout.log
tail -f "$(ls -t ~/Library/Logs/wiki-daily/run-*.log | head -1)"
```

The launchd schedule is **Mon-Fri 17:00 LOCAL TIME**. Edit `launchd/com.rgovindji.wiki-daily.plist` and re-run install to change.

## Day-to-day commands

```bash
# Status check
bash scripts/install_daily_cron.sh --status

# Run immediately (out of schedule)
bash scripts/install_daily_cron.sh --run-now

# Manual run with options
bash scripts/daily_claude.sh                # full run
bash scripts/daily_claude.sh --dry-run      # claude runs but no commit/push/email
bash scripts/daily_claude.sh --skip-email   # commit + push but skip SES
bash scripts/daily_claude.sh --skip-claude  # just commit + email anything already dirty

# Uninstall
bash scripts/install_daily_cron.sh --uninstall
sudo pmset repeat cancel    # if you set the wake schedule
```

## What Claude Code is allowed to do

The prompt at `scripts/daily_prompt.md` instructs Claude to:

- **Read**: CLAUDE.md, MEMORY.md, index.md, log.md, watchlist.md, then specific wiki/sources files as needed
- **Search**: up to ~20 WebSearch calls for news, earnings, long-form podcasts/Substacks
- **Fetch**: up to ~10 WebFetch calls for full-article ingest
- **Write**:
  - New source summaries to `sources/YYYY-MM-DD-slug.md`
  - Append bullets to `## Recent developments` in existing wiki pages
  - Prepend a new entry to `log.md`
  - Update `index.md` if new sources/pages were added
- **Not allowed**:
  - Flip stances (bull→bear or vice versa) — must flag for user sign-off
  - Change conviction on high-importance positions unilaterally
  - Modify frontmatter (except `last_updated` and `sources` count)
  - Create new top-level wiki pages without clear demand signal
  - Touch `MEMORY.md` or anything under `.claude/`
  - Commit or push (the wrapper script does that)

The Claude Code invocation uses `--dangerously-skip-permissions` because launchd has no user to approve permission prompts, and the prompt constrains the blast radius.

## Logs

| Path | What's in it |
|---|---|
| `~/Library/Logs/wiki-daily/launchd-stdout.log` | launchd's view of script stdout (rotates per fire) |
| `~/Library/Logs/wiki-daily/launchd-stderr.log` | launchd stderr |
| `~/Library/Logs/wiki-daily/run-YYYYMMDDTHHMMSSZ.log` | Per-run structured log from `daily_claude.sh` |
| `~/Library/Logs/wiki-daily/prompt-YYYYMMDDTHHMMSSZ.md` | Exact prompt that was sent to Claude (with today's date substituted) |
| `~/Library/Logs/wiki-daily/lambda-YYYYMMDDTHHMMSSZ.json` | Lambda response payload |
| CloudWatch `/aws/lambda/wiki-daily-update` | Lambda execution + SES MessageId |

## Cost

| Service | Cost |
|---|---|
| Anthropic Max plan | $200/mo (already paying — covers Claude Code daily run) |
| AWS Lambda (1 invocation/day × ~3s) | <$0.01/mo |
| AWS SES (1 email/day) | negligible |
| Secrets Manager (2 secrets for Lambda's GitHub PAT + the unused Anthropic API key) | $0.80/mo |
| **Marginal cost vs. doing nothing on AWS** | **~$1/mo** |

Compare to ~$25–$55/mo if we ran the research via the Anthropic API on Lambda instead.

## When the Mac is asleep

`StartCalendarIntervalAcceptsAsleep: true` in the plist means launchd will queue missed runs and fire as soon as the Mac wakes. So:

- **Mac wakes before 17:00**: runs on time
- **Mac asleep at 17:00, wakes by 17:30**: runs late (~when Mac wakes)
- **Mac asleep through 17:00 and woken next day**: queued run fires next morning

If you want guaranteed runs, set the pmset wake schedule:
```bash
sudo pmset repeat wakeorpoweron MTWRF 16:55:00
```

(Cancel with `sudo pmset repeat cancel`.)

## Failure modes + recovery

| Failure | Effect | Fix |
|---|---|---|
| `git pull` fails (network, conflict) | Script exits 3 before Claude runs; no API cost | Resolve manually, re-run with `bash scripts/install_daily_cron.sh --run-now` |
| Claude Code rate-limited on Max plan | Script exits 4 | Wait + re-run; verify Max plan status |
| Claude wrote bad content / made a stance flip | Commit lands in main; email sends bad content | `git revert HEAD && git push`; iterate on `scripts/daily_prompt.md` |
| `git push` fails (auth, conflict) | Script exits 5; commit lands locally only | Manually push: `cd ~/Projects/Investing && git push` |
| Lambda invoke fails | Script logs error but exits 0 | Manually re-trigger: `aws lambda invoke --function-name wiki-daily-update --payload '{"skip_update":true}' --cli-binary-format raw-in-base64-out /tmp/out.json` |
| Email goes to spam | wiki@decideai.xyz is a new sender to your address | Mark as Not Spam; first-email-from-domain is normal |

## How this compares to the AWS-only setup

The AWS-only setup (Lambda + Anthropic API) still works — it's deployed and tested. To switch back:

1. Top up Anthropic API credits at https://console.anthropic.com/settings/billing
2. Enable the EventBridge schedule: `bash aws/deploy.sh --enable-schedule --skip-build`
3. Uninstall the local cron: `bash scripts/install_daily_cron.sh --uninstall`

You can also run both — the Lambda's schedule and the local cron — though that would double-write each day. Not recommended.
