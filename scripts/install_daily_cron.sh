#!/usr/bin/env bash
# Install / uninstall the daily wiki update launchd job.
#
# Usage:
#   bash scripts/install_daily_cron.sh              # install + load
#   bash scripts/install_daily_cron.sh --uninstall  # stop + unload + remove
#   bash scripts/install_daily_cron.sh --status     # show status
#   bash scripts/install_daily_cron.sh --run-now    # trigger an immediate run
#   bash scripts/install_daily_cron.sh --wake-mac   # also set pmset wake schedule (sudo)
#
# What this does:
#   - Copies launchd/com.rgovindji.wiki-daily.plist → ~/Library/LaunchAgents/
#   - launchctl bootstrap to load it for the current user
#   - (optional) pmset to wake the Mac at 16:55 weekdays so the 17:00 run actually fires

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLIST_SRC="$REPO_DIR/launchd/com.rgovindji.wiki-daily.plist"
PLIST_NAME="com.rgovindji.wiki-daily"
PLIST_DST="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"
UID_NUM="$(id -u)"

ACTION="install"
WAKE_MAC="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --uninstall) ACTION="uninstall"; shift ;;
    --status)    ACTION="status"; shift ;;
    --run-now)   ACTION="run-now"; shift ;;
    --wake-mac)  WAKE_MAC="true"; shift ;;
    --help|-h)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    *) echo "unknown flag: $1" >&2; exit 2 ;;
  esac
done

case "$ACTION" in

  install)
    [[ -f "$PLIST_SRC" ]] || { echo "missing source plist: $PLIST_SRC" >&2; exit 3; }

    mkdir -p "$HOME/Library/LaunchAgents"
    mkdir -p "$HOME/Library/Logs/wiki-daily"

    # If already loaded, unload first so we pick up changes
    if launchctl print "gui/${UID_NUM}/${PLIST_NAME}" >/dev/null 2>&1; then
      echo "==> unloading existing job"
      launchctl bootout "gui/${UID_NUM}" "$PLIST_DST" || true
    fi

    echo "==> copying plist"
    cp "$PLIST_SRC" "$PLIST_DST"
    chmod 644 "$PLIST_DST"

    echo "==> loading"
    launchctl bootstrap "gui/${UID_NUM}" "$PLIST_DST"

    echo "==> enabling"
    launchctl enable "gui/${UID_NUM}/${PLIST_NAME}"

    echo "==> installed: $PLIST_DST"
    echo ""
    echo "Schedule: Mon-Fri 17:00 LOCAL TIME"
    echo "Logs:     $HOME/Library/Logs/wiki-daily/"
    echo ""
    echo "Verify:   launchctl print gui/${UID_NUM}/${PLIST_NAME} | head -20"
    echo "Run now:  bash scripts/install_daily_cron.sh --run-now"
    echo "Status:   bash scripts/install_daily_cron.sh --status"
    echo "Logs:     ls -lt ~/Library/Logs/wiki-daily/ | head"

    if [[ "$WAKE_MAC" == "true" ]]; then
      echo ""
      echo "==> setting pmset wake schedule (requires sudo)"
      echo "    will wake Mac at 16:55 weekdays so 17:00 job actually fires"
      sudo pmset repeat wakeorpoweron MTWRF 16:55:00
      echo "==> verify with: pmset -g sched"
    else
      echo ""
      echo "TIP: if your Mac sleeps at 17:00, the run will be missed."
      echo "     Set up a wake schedule with:"
      echo "         sudo pmset repeat wakeorpoweron MTWRF 16:55:00"
      echo "     or pass --wake-mac to this install script."
    fi
    ;;

  uninstall)
    if launchctl print "gui/${UID_NUM}/${PLIST_NAME}" >/dev/null 2>&1; then
      echo "==> stopping + unloading"
      launchctl bootout "gui/${UID_NUM}" "$PLIST_DST" || true
    else
      echo "==> not currently loaded"
    fi
    if [[ -f "$PLIST_DST" ]]; then
      echo "==> removing plist"
      rm "$PLIST_DST"
    fi
    echo "==> done"
    echo ""
    echo "If you also set a pmset wake schedule, cancel it with:"
    echo "    sudo pmset repeat cancel"
    ;;

  status)
    if launchctl print "gui/${UID_NUM}/${PLIST_NAME}" >/dev/null 2>&1; then
      echo "==> loaded and enabled"
      launchctl print "gui/${UID_NUM}/${PLIST_NAME}" | grep -E 'state|last exit|schedule|path|stdout|stderr' | head -10
    else
      echo "==> NOT loaded"
    fi
    echo ""
    echo "Recent logs:"
    ls -lt "$HOME/Library/Logs/wiki-daily/" 2>/dev/null | head -5 || echo "  (none yet)"
    if pmset -g sched 2>/dev/null | grep -q wakeorpoweron; then
      echo ""
      echo "pmset wake schedule:"
      pmset -g sched 2>/dev/null
    fi
    ;;

  run-now)
    echo "==> triggering run via launchctl kickstart"
    launchctl kickstart -k "gui/${UID_NUM}/${PLIST_NAME}"
    echo "==> kicked. Tail logs:"
    echo "    tail -f ~/Library/Logs/wiki-daily/launchd-stdout.log"
    echo "    tail -f \$(ls -t ~/Library/Logs/wiki-daily/run-*.log | head -1)"
    ;;
esac
