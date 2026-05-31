# aws/ — AWS Lambda daily-update automation

The daily wiki research sweep + overview email runs entirely on AWS:

```
EventBridge cron (22:00 UTC weekdays)
        ↓
Lambda  wiki-daily-update  (Python 3.12, 512 MB, 10-min timeout)
   ├─ reads ANTHROPIC_API_KEY + GITHUB_TOKEN from Secrets Manager
   ├─ fetches log.md, index.md, wiki/watchlist.md via GitHub Contents API
   ├─ calls Anthropic API with web_search tool (~12 searches max)
   ├─ commits source summaries / wiki appends / log entry via GitHub API
   ├─ renders overview email (editorial cream/serif/coral theme)
   └─ sends via SES sesv2 — wiki@decideai.xyz → rgovindji@gmail.com
        ↓
CloudWatch Logs /aws/lambda/wiki-daily-update (30-day retention)
```

No git binary, no checkout, no GitHub Actions runner. Everything flows through HTTPS APIs.

## Files

| File | Purpose |
|---|---|
| `lambda/handler.py` | Lambda function entry point + GitHub/Claude/SES orchestration |
| `template.yaml` | CloudFormation: Lambda, IAM role, Secrets Manager entries, EventBridge schedule |
| `deploy.sh` | Build + package + upload zip + `aws cloudformation deploy` |
| `build/handler.zip` | Generated build artifact (gitignored) |

## Initial setup (one-time)

```bash
# 1. Deploy the stack (creates Lambda + IAM + empty secrets + S3 bucket)
bash aws/deploy.sh

# 2. Populate secrets (one-time)
aws secretsmanager update-secret --region us-east-1 \
  --secret-id wiki/anthropic \
  --secret-string '{"api_key":"sk-ant-..."}'

aws secretsmanager update-secret --region us-east-1 \
  --secret-id wiki/github \
  --secret-string '{"token":"ghp_..."}'

# 3. Test with skip_update=true (email-only, no Claude call, no GitHub writes)
aws lambda invoke --region us-east-1 \
  --function-name wiki-daily-update \
  --payload '{"skip_update":true,"send_email":true}' \
  --cli-binary-format raw-in-base64-out \
  /tmp/out.json && cat /tmp/out.json

# 4. Full test (Claude + GitHub writes + email)
aws lambda invoke --region us-east-1 \
  --function-name wiki-daily-update \
  --payload '{"skip_update":false,"send_email":true}' \
  --cli-binary-format raw-in-base64-out \
  --cli-read-timeout 600 \
  /tmp/out.json && cat /tmp/out.json

# 5. Once tests pass, enable the EventBridge daily schedule
bash aws/deploy.sh --enable-schedule --skip-build
```

## Updating the code

After editing `lambda/handler.py` or `scripts/daily_email.py`:

```bash
bash aws/deploy.sh   # rebuilds zip, uploads, updates Lambda code
```

The deploy script uses a timestamped S3 key, so CloudFormation always sees a "new" zip and triggers a Lambda code update.

## Updating secrets

```bash
# Rotate Anthropic key
aws secretsmanager update-secret --region us-east-1 \
  --secret-id wiki/anthropic \
  --secret-string '{"api_key":"sk-ant-NEW..."}'

# Rotate GitHub PAT
aws secretsmanager update-secret --region us-east-1 \
  --secret-id wiki/github \
  --secret-string '{"token":"ghp_NEW..."}'
```

Lambda picks up the new values on the next invocation (no restart needed).

## Schedule customization

Edit `template.yaml`:

```yaml
ScheduleExpression:
  Type: String
  Default: 'cron(0 22 ? * MON-FRI *)'   # 22:00 UTC weekdays
```

Then `bash aws/deploy.sh --enable-schedule` to apply.

EventBridge cron quirks:
- Either day-of-month or day-of-week must be `?` (not `*`)
- Time is UTC
- Format: `cron(minute hour day month day-of-week year)`

Common alternatives:
- `cron(0 13 ? * MON-FRI *)` — 09:00 EDT pre-market
- `cron(30 21 ? * MON-FRI *)` — 17:30 EDT market close
- `cron(0 22 ? * * *)` — every day including weekends

## Manual invocations

```bash
# Email-only, no Claude
aws lambda invoke --region us-east-1 \
  --function-name wiki-daily-update \
  --payload '{"skip_update":true}' \
  --cli-binary-format raw-in-base64-out /tmp/out.json

# Override recipient
aws lambda invoke --region us-east-1 \
  --function-name wiki-daily-update \
  --payload '{"skip_update":true,"email_to":"someone@else.com"}' \
  --cli-binary-format raw-in-base64-out /tmp/out.json

# Dry-run: returns Claude's JSON plan but writes nothing
aws lambda invoke --region us-east-1 \
  --function-name wiki-daily-update \
  --payload '{"skip_update":false,"dry_run":true}' \
  --cli-binary-format raw-in-base64-out /tmp/out.json
```

## Logs

```bash
# Tail recent logs
aws logs tail /aws/lambda/wiki-daily-update --region us-east-1 --since 30m --format short

# Watch live (during a manual invoke)
aws logs tail /aws/lambda/wiki-daily-update --region us-east-1 --follow
```

## Cost rough estimate

For one daily run:

| Service | Per-run cost | Monthly (22 weekdays) |
|---|---|---|
| Anthropic Opus 4.7 (~250K input + ~5K output + 12 web searches) | ~$1.00–$2.50 | ~$25–$55 |
| Lambda (10 min × 512 MB) | ~$0.005 | ~$0.10 |
| SES (1 email/day) | ~$0.0001 | negligible |
| Secrets Manager (2 secrets) | — | $0.80 ($0.40 × 2) |
| CloudWatch Logs | — | <$0.50 |
| **Total** | | **~$25–$55/month** |

Anthropic cost is the dominant line. To reduce:
- Lower `ANTHROPIC_WEB_SEARCH_MAX_USES` in `handler.py` (default 12)
- Use `claude-sonnet-4-6` instead of `claude-opus-4-7` (~5× cheaper, slightly less analytical depth)
- Run weekly instead of daily

## Troubleshooting

**"anthropic SDK missing from Lambda package"**
The build pulled darwin/arm64 wheels instead of Linux x86_64. Re-run `bash aws/deploy.sh` — the script forces `--platform manylinux2014_x86_64` so this should not recur.

**"Your credit balance is too low to access the Anthropic API"**
Top up at https://console.anthropic.com/settings/billing.

**"Bad credentials" from GitHub API**
The GitHub PAT in Secrets Manager has expired or been revoked. Generate a new fine-grained PAT (Contents: Read and write, scope: this repo) and update the secret.

**"MessageRejected: Email address is not verified" from SES**
The `SES_SENDER` value isn't a verified identity in SES. Either change `SES_SENDER` to an existing verified identity or verify the new one:
```bash
aws sesv2 create-email-identity --email-identity wiki@example.com --region us-east-1
```

**Lambda timeouts (>10 min)**
Increase `Timeout` in `template.yaml` (max 15 min). If you hit 15 min consistently, the Claude call needs trimming — reduce `tail_log_entries(n)` from 80 or cap `ANTHROPIC_WEB_SEARCH_MAX_USES`.

## Why this isn't GitHub Actions

We previously had a GitHub Actions workflow doing the same thing. We migrated to Lambda because:
- Secrets stay in AWS (no GitHub Secrets sprawl)
- Tighter IAM (only Lambda execution role can read the secrets)
- CloudWatch consolidates logs with other AWS infra
- No GitHub Actions minute consumption on private repos

The old workflow at `.github/workflows/daily-update.yml` has its `schedule` block commented out; `workflow_dispatch` is preserved as an emergency manual fallback.
