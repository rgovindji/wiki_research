#!/usr/bin/env bash
# Daily YouTube intelligence sweep — headless Claude run.
# Finds high-signal AI/semis/power/compute videos, transcribes the worthwhile ones via the
# scribetube-transcript skill, files source summaries + wiki patches, commits locally (no push).
# Feeds the $200K aggressive AI/tech book. Mirrors scripts/daily_claude.sh conventions.
#
# Scheduled via launchd/com.rgovindji.wiki-youtube-sweep.plist (~6:12 AM, before the morning brief).
# Manual run:  bash scripts/youtube_sweep.sh
#              bash scripts/youtube_sweep.sh --dry-run   # claude runs, but tell it not to commit

set -uo pipefail

REPO_DIR="${WIKI_REPO_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
CLAUDE_BIN="${CLAUDE_BIN:-$(command -v claude || echo /Users/rgovindji/.local/bin/claude)}"
LOG_DIR="${LOG_DIR:-$HOME/Library/Logs/wiki-daily}"
PROMPT_FILE="$REPO_DIR/scripts/youtube_sweep_prompt.md"

DRY_RUN="false"
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN="true"

mkdir -p "$LOG_DIR"
TODAY=$(date +%F)
LOG="$LOG_DIR/youtube-sweep-$TODAY.log"
exec >>"$LOG" 2>&1

echo "==== youtube-sweep $(date) ===="
echo "repo:   $REPO_DIR"
echo "claude: $CLAUDE_BIN"
cd "$REPO_DIR" || { echo "FATAL: cannot cd $REPO_DIR"; exit 1; }

# Sync (sweep commits locally; newsletter pushes, so pull to stay current)
git pull --rebase --autostash 2>&1 | tail -3 || echo "git pull skipped"

if [[ ! -f "$PROMPT_FILE" ]]; then echo "FATAL: missing $PROMPT_FILE"; exit 1; fi

HEADER="Today is $TODAY. Run the daily YouTube sweep exactly as specified below."
[[ "$DRY_RUN" == "true" ]] && HEADER="$HEADER (DRY RUN: do all research + write files but do NOT git commit.)"

echo "invoking claude -p ..."
# --dangerously-skip-permissions: unattended run, same rationale as daily_claude.sh.
"$CLAUDE_BIN" -p "$HEADER

$(cat "$PROMPT_FILE")" \
  --dangerously-skip-permissions \
  --output-format text \
  || { echo "claude exited non-zero ($?)"; exit 1; }

echo "==== youtube-sweep done $(date) ===="
