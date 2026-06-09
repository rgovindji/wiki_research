#!/usr/bin/env bash
# Daily newsletter runs — uses Claude Code (Max plan) for research + writing,
# render_newsletter.py + AWS SES for the email.
#
# Two editions, two launchd jobs:
#   --edition morning  →  Before the Bell brief (launchd/com.rgovindji.wiki-morning.plist, ~6:45 AM)
#                         light research sweep, writes newsletter/issues/DATE-morning.md
#   --edition close    →  full wiki update + After Hours letter (com.rgovindji.wiki-daily.plist, 5 PM)
#                         writes newsletter/issues/DATE-afterhours.md (default edition)
#
# Flow:
#   1. launchd fires this script on schedule
#   2. git pull --rebase to sync with any remote changes
#   3. claude -p with the edition's prompt template (uses your Anthropic Max plan, NOT API credits)
#   4. If Claude wrote new content: git add + commit + push
#   5. Render + send the issue Claude wrote via scripts/render_newsletter.py (SES)
#
# Usage:
#   bash scripts/daily_claude.sh                     # full close-of-market run
#   bash scripts/daily_claude.sh --edition morning   # morning brief run
#   bash scripts/daily_claude.sh --dry-run           # claude runs but no commit/push/email
#   bash scripts/daily_claude.sh --skip-email        # commit + push but don't send
#   bash scripts/daily_claude.sh --skip-claude       # skip the LLM call (commit + email whatever's already on disk)
#
# Environment:
#   WIKI_REPO_DIR        — repo root (default: this script's parent's parent)
#   CLAUDE_BIN           — path to claude CLI (default: from PATH)
#   PYTHON_BIN           — python3 with boto3 (default: python3 from PATH)
#   LOG_DIR              — log destination (default: ~/Library/Logs/wiki-daily)
#   EMAIL_TO / SES_SENDER / AWS_REGION — read by render_newsletter.py (or repo-root .env)

set -uo pipefail

REPO_DIR="${WIKI_REPO_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
CLAUDE_BIN="${CLAUDE_BIN:-$(command -v claude || echo /Users/rgovindji/.local/bin/claude)}"
PYTHON_BIN="${PYTHON_BIN:-$(command -v python3 || echo /usr/bin/python3)}"
LOG_DIR="${LOG_DIR:-$HOME/Library/Logs/wiki-daily}"

EDITION="close"
DRY_RUN="false"
SKIP_EMAIL="false"
SKIP_CLAUDE="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --edition)      EDITION="${2:?--edition needs morning|close}"; shift 2 ;;
    --dry-run)      DRY_RUN="true"; shift ;;
    --skip-email)   SKIP_EMAIL="true"; shift ;;
    --skip-claude)  SKIP_CLAUDE="true"; shift ;;
    --help|-h)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    *) echo "unknown flag: $1" >&2; exit 2 ;;
  esac
done

case "$EDITION" in
  morning)
    PROMPT_BASENAME="morning_prompt.md"
    ISSUE_SLUG="morning"
    COMMIT_TITLE="Morning brief" ;;
  close)
    PROMPT_BASENAME="daily_prompt.md"
    ISSUE_SLUG="afterhours"
    COMMIT_TITLE="Daily auto-update" ;;
  *) echo "unknown edition: $EDITION (use morning|close)" >&2; exit 2 ;;
esac

mkdir -p "$LOG_DIR"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)-${EDITION}"
RUN_LOG="$LOG_DIR/run-${RUN_ID}.log"

log() { printf "[%s] %s\n" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$RUN_LOG"; }
fail() { log "ERROR: $*"; exit 1; }

log "=== daily_claude.sh started ==="
log "edition:   $EDITION"
log "repo:      $REPO_DIR"
log "claude:    $CLAUDE_BIN"
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
  PROMPT_FILE="$REPO_DIR/scripts/$PROMPT_BASENAME"
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
        commit -m "${COMMIT_TITLE} ${TODAY_UTC}

Automated ${EDITION}-edition run via Claude Code (Max plan) + local launchd.
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

# ----- 5. Render + send the newsletter issue via SES -----
TODAY_UTC="$(date -u +%Y-%m-%d)"
ISSUE_FILE="$REPO_DIR/newsletter/issues/${TODAY_UTC}-${ISSUE_SLUG}.md"
EMAILED="false"
if [[ "$SKIP_EMAIL" == "true" ]]; then
  log "email skipped per --skip-email"
elif [[ ! -f "$ISSUE_FILE" ]]; then
  # The prompt skips writing an issue on market holidays; otherwise this is a failure.
  log "WARNING: no issue file at $ISSUE_FILE — nothing to send (holiday, or Claude failed to write it)"
elif [[ "$DRY_RUN" == "true" ]]; then
  log "DRY-RUN: would render + send $ISSUE_FILE"
  "$PYTHON_BIN" "$REPO_DIR/scripts/render_newsletter.py" "$ISSUE_FILE" --dry-run 2>&1 | tee -a "$RUN_LOG"
else
  log "rendering + sending $ISSUE_FILE"
  if "$PYTHON_BIN" "$REPO_DIR/scripts/render_newsletter.py" "$ISSUE_FILE" 2>&1 | tee -a "$RUN_LOG"; then
    EMAILED="true"
  else
    log "ERROR: newsletter send failed — issue is on disk at $ISSUE_FILE; send manually with:"
    log "    python3 scripts/render_newsletter.py $ISSUE_FILE"
    exit 6
  fi
fi

log "=== daily_claude.sh completed ==="
log "summary: edition=$EDITION dirty=$DIRTY pushed=$PUSHED emailed=$EMAILED"
exit 0
