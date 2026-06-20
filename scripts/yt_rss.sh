#!/usr/bin/env bash
# yt_rss.sh — reliable YouTube video-ID discovery via channel RSS feeds.
# Fixes the Tier-3/6 gap where WebSearch returns playlists/Substack instead of watch URLs.
#
# Usage:
#   scripts/yt_rss.sh <handle|channel_id|channel_url> [DAYS]
#     <handle>      e.g. @LatentSpacePod  (resolved to channel_id automatically)
#     <channel_id>  e.g. UCxBcwypKK-W3GHd_RZ9FZrQ (used directly)
#     [DAYS]        only show videos published within the last N days (default 45)
#
#   scripts/yt_rss.sh --roster [DAYS]      # sweep every channel in the roster below
#
# Output (tab-separated): PUBLISHED_DATE  VIDEO_ID  TITLE
# Feed the VIDEO_IDs to the scribetube skill. RSS only returns the latest ~15 uploads per channel.

set -uo pipefail
DAYS_DEFAULT=45

# --- known channels (handle  channel_id-or-empty) — extend as the roster grows ---
read -r -d '' ROSTER <<'EOF'
@LatentSpacePod UCxBcwypKK-W3GHd_RZ9FZrQ
@AswathDamodaranonValuation UCLvnJL8htRR1T9cbSccaoVw
@DwarkeshPatel
@bg2pod
@NoPriorsPodcast
@interconnects
@SemiAnalysis
@thatsamir
@sequoiacapital
@a16z
@theprofg
@ThisWeekinStartups
EOF

resolve_id() {
  # echo a channel_id (UC...) for a handle/URL/id
  local in="$1"
  case "$in" in
    UC*) echo "$in"; return 0 ;;
  esac
  local url="$in"
  case "$in" in
    @*) url="https://www.youtube.com/$in" ;;
    http*) url="$in" ;;
    *) url="https://www.youtube.com/@$in" ;;
  esac
  # scrape the channel page for the canonical channelId
  curl -s -A "Mozilla/5.0" "$url" \
    | grep -o '"channelId":"UC[A-Za-z0-9_-]\{22\}"' | head -1 \
    | sed 's/"channelId":"//; s/"//'
}

fetch_feed() {
  local cid="$1" days="$2" label="$3"
  [ -z "$cid" ] && { echo "  (could not resolve channel_id for $label)" >&2; return 1; }
  local cutoff; cutoff=$(date -v-"${days}"d +%Y-%m-%d 2>/dev/null || date -d "-${days} days" +%Y-%m-%d)
  curl -s "https://www.youtube.com/feeds/videos.xml?channel_id=${cid}" \
  | awk -v cutoff="$cutoff" '
      /<yt:videoId>/ { gsub(/.*<yt:videoId>|<\/yt:videoId>.*/,""); vid=$0 }
      /<title>/ && vid!="" && title=="" { t=$0; gsub(/.*<title>|<\/title>.*/,"",t); title=t }
      /<published>/ { gsub(/.*<published>|<\/published>.*/,""); pub=substr($0,1,10);
                      if (vid!="" && pub>=cutoff) printf "%s\t%s\t%s\n", pub, vid, title;
                      vid=""; title="" }
    '
}

if [ "${1:-}" = "--roster" ]; then
  DAYS="${2:-$DAYS_DEFAULT}"
  echo "# Roster RSS sweep — videos in last ${DAYS}d (PUBLISHED  VIDEO_ID  TITLE)"
  while read -r handle cid; do
    [ -z "$handle" ] && continue
    [ -z "${cid:-}" ] && cid="$(resolve_id "$handle")"
    echo "## $handle ($cid)"
    fetch_feed "$cid" "$DAYS" "$handle"
  done <<< "$ROSTER"
  exit 0
fi

[ $# -lt 1 ] && { grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 2; }
CID="$(resolve_id "$1")"
fetch_feed "$CID" "${2:-$DAYS_DEFAULT}" "$1"
