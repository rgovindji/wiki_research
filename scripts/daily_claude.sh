#!/usr/bin/env bash
# Daily wiki update — uses Claude Code (Max plan) for research, AWS SES for email.
#
# Architecture (Option C from the design discussion):
#   1. launchd fires this script on schedule (configured in launchd/com.rgovindji.wiki-daily.plist)
#   2. git pull --rebase to sync with any remote changes
#   3. claude -p with the prompt template (uses your Anthropic Max plan, NOT API credits)
#   4. If Claude wrote new content: git add + commit + push
#   5. Invoke AWS Lambda with skip_update=true → Lambda emails the latest log entry via SES
#
# Why this beats the pure-API setup: zero marginal Anthropic cost (covered by Max plan).
# Why this beats GitHub Actions: keeps secrets on your Mac and in AWS (not GitHub).
#
# Usage:
#   bash scripts/daily_claude.sh                 # full run
#   bash scripts/daily_claude.sh --dry-run       # claude runs but no commit/push/email
#   bash scripts/daily_claude.sh --skip-email    # commit + push but don't trigger Lambda
#   bash scripts/daily_claude.sh --skip-claude   # skip the LLM call (just commit + email anything that's already dirty)
#
# Environment:
#   WIKI_REPO_DIR        — repo root (default: this script's parent's parent)
#   CLAUDE_BIN           — path to claude CLI (default: from PATH)
#   AWS_LAMBDA_NAME      — Lambda function name (default: wiki-daily-update)
#   AWS_REGION           — default us-east-1
#   LOG_DIR              — log destination (default: ~/Library/Logs/wiki-daily)
#   EMAIL_ON_LOW_SIGNAL  — "true" to send email even on low-signal days (default: true)

set -uo pipefail

REPO_DIR="${WIKI_REPO_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
CLAUDE_BIN="${CLAUDE_BIN:-$(command -v claude || echo /Users/rgovindji/.local/bin/claude)}"
AWS_LAMBDA_NAME="${AWS_LAMBDA_NAME:-wiki-daily-update}"
AWS_REGION="${AWS_REGION:-us-east-1}"
LOG_DIR="${LOG_DIR:-$HOME/Library/Logs/wiki-daily}"
EMAIL_ON_LOW_SIGNAL="${EMAIL_ON_LOW_SIGNAL:-true}"

DRY_RUN="false"
SKIP_EMAIL="false"
SKIP_CLAUDE="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)      DRY_RUN="true"; shift ;;
    --skip-email)   SKIP_EMAIL="true"; shift ;;
    --skip-claude)  SKIP_CLAUDE="true"; shift ;;
    --help|-h)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    *) echo "unknown flag: $1" >&2; exit 2 ;;
  esac
done

mkdir -p "$LOG_DIR"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)"
RUN_LOG="$LOG_DIR/run-${RUN_ID}.log"

log() { printf "[%s] %s\n" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$RUN_LOG"; }
fail() { log "ERROR: $*"; exit 1; }

log "=== daily_claude.sh started ==="
log "repo:      $REPO_DIR"
log "claude:    $CLAUDE_BIN"
log "lambda:    $AWS_LAMBDA_NAME (region $AWS_REGION)"
log "dry-run:   $DRY_RUN"
log "log file:  $RUN_LOG"

cd "$REPO_DIR" || fail "cannot cd to $REPO_DIR"

# ----- 1. Pre-flight: clean working tree + git pull -----
if [[ -n "$(git status --porcelain)" ]]; then
  log "WARNING: working tree is dirty before run; stashing for safety"
  git stash push -u -m "daily_claude.sh auto-stash $RUN_ID" >>"$RUN_LOG" 2>&1 || true
fi

log "git fetch + pull"
git fetch origin --quiet 2>&1 | tee -a "$RUN_LOG"
git checkout main --quiet 2>&1 | tee -a "$RUN_LOG"
git pull --rebase --quiet origin main 2>&1 | tee -a "$RUN_LOG" || {
  log "ERROR: git pull failed; aborting"
  exit 3
}

BEFORE_SHA=$(git rev-parse HEAD)
log "starting at sha: $BEFORE_SHA"

# ----- 2. Run Claude Code (unless skipped) -----
if [[ "$SKIP_CLAUDE" == "false" ]]; then
  TODAY_UTC="$(date -u +%Y-%m-%d)"
  PROMPT_FILE="$REPO_DIR/scripts/daily_prompt.md"
  [[ -f "$PROMPT_FILE" ]] || fail "prompt template missing: $PROMPT_FILE"

  TMP_PROMPT="$LOG_DIR/prompt-${RUN_ID}.md"
  sed "s/__TODAY__/$TODAY_UTC/g" "$PROMPT_FILE" > "$TMP_PROMPT"

  log "invoking claude -p (today=$TODAY_UTC, prompt=$TMP_PROMPT)"

  # Run Claude with dangerous-skip-permissions because:
  # - We're on the owner's Mac
  # - The prompt explicitly constrains writes to raw/sources/wiki/index/log
  # - Headless launchd context means there's no user to approve permission prompts
  set +e
  "$CLAUDE_BIN" -p "$(cat "$TMP_PROMPT")" \
    --dangerously-skip-permissions \
    --output-format text \
    2>&1 | tee -a "$RUN_LOG"
  CLAUDE_EXIT=$?
  set -e

  if [[ $CLAUDE_EXIT -ne 0 ]]; then
    log "ERROR: claude exited $CLAUDE_EXIT"
    exit 4
  fi
  log "claude completed"
fi

# ----- 3. Detect changes -----
DIRTY="false"
if [[ -n "$(git status --porcelain)" ]]; then
  DIRTY="true"
  log "working tree changed:"
  git status --short | tee -a "$RUN_LOG"
else
  log "no changes — Claude declared low-signal day (or nothing to commit)"
fi

# ----- 4. Commit + push (unless dry-run or no changes) -----
PUSHED="false"
if [[ "$DIRTY" == "true" ]]; then
  if [[ "$DRY_RUN" == "true" ]]; then
    log "DRY-RUN: would commit and push the above changes"
  else
    TODAY_UTC="$(date -u +%Y-%m-%d)"
    log "committing"
    git add -A 2>&1 | tee -a "$RUN_LOG"
    git -c user.name="wiki-bot (local cron)" \
        -c user.email="wiki-bot@decideai.xyz" \
        commit -m "Daily auto-update ${TODAY_UTC}

Automated daily research sweep via Claude Code (Max plan) + local launchd.
Generated by scripts/daily_claude.sh.

Co-Authored-By: Claude Code (local) <noreply@anthropic.com>" 2>&1 | tee -a "$RUN_LOG"
    log "pushing"
    git push origin main 2>&1 | tee -a "$RUN_LOG" || {
      log "ERROR: git push failed; manual intervention required"
      exit 5
    }
    PUSHED="true"
    AFTER_SHA=$(git rev-parse HEAD)
    log "pushed: $BEFORE_SHA → $AFTER_SHA"
  fi
fi

# ----- 5. Trigger AWS Lambda for email -----
if [[ "$SKIP_EMAIL" == "true" ]]; then
  log "email skipped per --skip-email"
elif [[ "$DRY_RUN" == "true" ]]; then
  log "DRY-RUN: would invoke Lambda for email"
elif [[ "$DIRTY" == "false" && "$EMAIL_ON_LOW_SIGNAL" != "true" ]]; then
  log "no changes and EMAIL_ON_LOW_SIGNAL=false; skipping email"
else
  log "invoking Lambda for email"
  if ! command -v aws >/dev/null 2>&1; then
    fail "aws CLI not on PATH — install with: brew install awscli"
  fi
  LAMBDA_OUT="$LOG_DIR/lambda-${RUN_ID}.json"
  aws lambda invoke --region "$AWS_REGION" \
    --function-name "$AWS_LAMBDA_NAME" \
    --payload '{"skip_update":true,"send_email":true}' \
    --cli-binary-format raw-in-base64-out \
    "$LAMBDA_OUT" 2>&1 | tee -a "$RUN_LOG"
  log "lambda response:"
  cat "$LAMBDA_OUT" | tee -a "$RUN_LOG"
  echo "" | tee -a "$RUN_LOG"
fi

log "=== daily_claude.sh completed ==="
log "summary: dirty=$DIRTY pushed=$PUSHED"
exit 0
