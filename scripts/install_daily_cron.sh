#!/usr/bin/env bash
# Install / uninstall the daily newsletter launchd jobs (both editions).
#
# Jobs:
#   com.rgovindji.wiki-morning  — Mon-Fri 06:45 local — Before the Bell brief
#   com.rgovindji.wiki-daily    — Mon-Fri 17:00 local — wiki update + After Hours letter
#
# Usage:
#   bash scripts/install_daily_cron.sh                    # install + load both
#   bash scripts/install_daily_cron.sh --uninstall        # stop + unload + remove both
#   bash scripts/install_daily_cron.sh --status           # show status of both
#   bash scripts/install_daily_cron.sh --run-now          # trigger the 17:00 job now
#   bash scripts/install_daily_cron.sh --run-now-morning  # trigger the 06:45 job now
#   bash scripts/install_daily_cron.sh --wake-mac         # also set pmset wake schedule (sudo)
#
# What this does:
#   - Copies launchd/com.rgovindji.wiki-{morning,daily}.plist → ~/Library/LaunchAgents/
#   - launchctl bootstrap to load them for the current user
#   - (optional) pmset to wake the Mac at 16:55 weekdays for the 17:00 run
#     (pmset supports only one repeating event; the evening run is the one
#     that does the wiki update, so it gets the wake slot)

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
JOBS=(com.rgovindji.wiki-morning com.rgovindji.wiki-daily)
UID_NUM="$(id -u)"

ACTION="install"
WAKE_MAC="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --uninstall)       ACTION="uninstall"; shift ;;
    --status)          ACTION="status"; shift ;;
    --run-now)         ACTION="run-now"; shift ;;
    --run-now-morning) ACTION="run-now-morning"; shift ;;
    --wake-mac)        WAKE_MAC="true"; shift ;;
    --help|-h)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    *) echo "unknown flag: $1" >&2; exit 2 ;;
  esac
done

install_job() {
  local name="$1"
  local src="$REPO_DIR/launchd/${name}.plist"
  local dst="$HOME/Library/LaunchAgents/${name}.plist"
  [[ -f "$src" ]] || { echo "missing source plist: $src" >&2; exit 3; }

  if launchctl print "gui/${UID_NUM}/${name}" >/dev/null 2>&1; then
    echo "==> [$name] unloading existing job"
    launchctl bootout "gui/${UID_NUM}" "$dst" || true
  fi

  echo "==> [$name] copying plist"
  cp "$src" "$dst"
  chmod 644 "$dst"

  echo "==> [$name] loading + enabling"
  launchctl bootstrap "gui/${UID_NUM}" "$dst"
  launchctl enable "gui/${UID_NUM}/${name}"
  echo "==> [$name] installed: $dst"
}

uninstall_job() {
  local name="$1"
  local dst="$HOME/Library/LaunchAgents/${name}.plist"
  if launchctl print "gui/${UID_NUM}/${name}" >/dev/null 2>&1; then
    echo "==> [$name] stopping + unloading"
    launchctl bootout "gui/${UID_NUM}" "$dst" || true
  else
    echo "==> [$name] not currently loaded"
  fi
  if [[ -f "$dst" ]]; then
    echo "==> [$name] removing plist"
    rm "$dst"
  fi
}

status_job() {
  local name="$1"
  if launchctl print "gui/${UID_NUM}/${name}" >/dev/null 2>&1; then
    echo "==> [$name] loaded and enabled"
    launchctl print "gui/${UID_NUM}/${name}" | grep -E 'state|last exit|schedule|path|stdout|stderr' | head -10
  else
    echo "==> [$name] NOT loaded"
  fi
  echo ""
}

case "$ACTION" in

  install)
    mkdir -p "$HOME/Library/LaunchAgents"
    mkdir -p "$HOME/Library/Logs/wiki-daily"

    for job in "${JOBS[@]}"; do
      install_job "$job"
      echo ""
    done

    echo "Schedules:"
    echo "  com.rgovindji.wiki-morning — Mon-Fri 06:45 LOCAL — Before the Bell brief"
    echo "  com.rgovindji.wiki-daily   — Mon-Fri 17:00 LOCAL — wiki update + After Hours letter"
    echo "Logs:     $HOME/Library/Logs/wiki-daily/"
    echo ""
    echo "Verify:   bash scripts/install_daily_cron.sh --status"
    echo "Run now:  bash scripts/install_daily_cron.sh --run-now           (evening)"
    echo "          bash scripts/install_daily_cron.sh --run-now-morning   (morning)"

    if [[ "$WAKE_MAC" == "true" ]]; then
      echo ""
      echo "==> setting pmset wake schedule (requires sudo)"
      echo "    will wake Mac at 16:55 weekdays so the 17:00 job actually fires"
      sudo pmset repeat wakeorpoweron MTWRF 16:55:00
      echo "==> verify with: pmset -g sched"
    else
      echo ""
      echo "TIP: if your Mac sleeps at 06:45 or 17:00, that run fires on next wake."
      echo "     pmset supports one repeating wake event; for the evening run:"
      echo "         sudo pmset repeat wakeorpoweron MTWRF 16:55:00"
      echo "     or pass --wake-mac to this install script."
    fi
    ;;

  uninstall)
    for job in "${JOBS[@]}"; do
      uninstall_job "$job"
    done
    echo "==> done"
    echo ""
    echo "If you also set a pmset wake schedule, cancel it with:"
    echo "    sudo pmset repeat cancel"
    ;;

  status)
    for job in "${JOBS[@]}"; do
      status_job "$job"
    done
    echo "Recent logs:"
    ls -lt "$HOME/Library/Logs/wiki-daily/" 2>/dev/null | head -5 || echo "  (none yet)"
    if pmset -g sched 2>/dev/null | grep -q wakeorpoweron; then
      echo ""
      echo "pmset wake schedule:"
      pmset -g sched 2>/dev/null
    fi
    ;;

  run-now)
    echo "==> triggering evening run via launchctl kickstart"
    launchctl kickstart -k "gui/${UID_NUM}/com.rgovindji.wiki-daily"
    echo "==> kicked. Tail logs:"
    echo "    tail -f ~/Library/Logs/wiki-daily/launchd-stdout.log"
    echo "    tail -f \$(ls -t ~/Library/Logs/wiki-daily/run-*.log | head -1)"
    ;;

  run-now-morning)
    echo "==> triggering morning run via launchctl kickstart"
    launchctl kickstart -k "gui/${UID_NUM}/com.rgovindji.wiki-morning"
    echo "==> kicked. Tail logs:"
    echo "    tail -f ~/Library/Logs/wiki-daily/launchd-morning-stdout.log"
    echo "    tail -f \$(ls -t ~/Library/Logs/wiki-daily/run-*.log | head -1)"
    ;;
esac
