---
type: analysis
tags: [template, youtube, faceless, automation, pipeline, publication]
last_updated: 2026-05-15
last_full_review: 2026-05-15
sources: 0
status: template
---

# YouTube Pipeline — Faceless Video Production Runbook

> **Goal:** Convert each Substack article into a YouTube video + 3 shorts in ~35 minutes of post-writing work. Audience doesn't care about polish; volume and consistency win.

## Tool stack

| Tool | Purpose | Monthly cost | URL |
|---|---|---|---|
| **InVideo AI** | Article → video automation | $30 | invideo.io |
| **Eleven Labs** | Premium AI voiceover (consistent voice = your brand) | $22 | elevenlabs.io |
| **Canva** | Thumbnails (the single biggest factor in CTR) | $13 | canva.com |
| **Opus Clip** | Auto-clip long video into shorts | $19 | opus.pro |
| **YouTube Studio** | Upload + schedule + analytics | Free | studio.youtube.com |

**Total: $84/mo.** Pays back at ~5,000 subscribers + monetization.

## Pre-flight setup (one-time, ~3 hours)

### 1. Eleven Labs voice selection (45 min)

- Sign up; go to Voice Library
- Test 8-10 voices from "narration" and "American male/female finance" categories
- **Pick ONE voice.** This becomes your brand. Don't change it.
- Recommended characteristics: mid-range pitch, professional but conversational, clear enunciation
- Save the voice ID — you'll reuse for every video
- **Test:** Generate 30 seconds of sample text. Listen on phone speakers (most YouTube watch happens on phones). If it sounds robotic on phone, try another voice.

### 2. Canva thumbnail templates (60 min)

- Search "finance YouTube thumbnail" in Canva templates
- Pick 3 base templates you like
- Customize colors to your brand (suggest: navy/white/orange-accent — looks like WSJ, not MrBeast)
- Set fixed fonts (one display font, one mono font for tickers)
- Save as "MY-THUMBNAIL-TEMPLATE-1/2/3"
- **Rule:** Same template family for every video = brand recognition

### 3. YouTube channel setup (30 min)

- Channel name: short, memorable, no numbers
- Banner: simple. "Daily AI + Markets Research" tagline.
- Channel trailer: 60-90 sec, "what this channel is" — can record this separately or use first long video as trailer
- About section: link to Substack + Twitter + feedback-log on GitHub
- Custom URL once eligible (100 subs + 30 days)
- **Critical:** Set Default Upload Settings → tags, end screens, cards as defaults

### 4. End screen + Cards (15 min, recurring per video)

- Default end screen: "Subscribe" + "Latest video" + "Substack link"
- Card at 30-second mark: "Subscribe to Substack" (no link in YouTube; use pinned comment with link)
- Pinned comment template: *"Daily AI + markets research at [Substack URL]. Track record at [feedback-log URL]. This is research, not advice."*

## Per-video workflow (~35 min after writing)

### Step 1: Write video script (10 min)

Convert Substack article to video script. **Key differences from article:**

| Article | Video script |
|---|---|
| Information-dense | Conversation-paced |
| Long sentences OK | Short sentences only |
| Sub-headers organize | Verbal transitions ("Here's the thing…") |
| Lede explains | **First 8 seconds: hook** |
| Conclusion summarizes | **End with call-to-action** |

**Rule:** Read it out loud. If you stumble, simplify.

**Length:** ~150 words/minute spoken. So a 6-minute video = ~900 words.

### Step 2: Generate voiceover in Eleven Labs (5 min)

- Open Eleven Labs → select your saved voice
- Paste script
- Generate. Listen back.
- Re-generate any awkward sections (paste just that paragraph)
- Download MP3
- File naming: `voiceover-YYYY-MM-DD-slug.mp3`

### Step 3: Generate visuals in InVideo AI (10 min)

**Option A: Paste script (recommended for control)**
- InVideo AI → "Generate Video" → "From Script"
- Paste script
- Settings: 16:9 aspect ratio, 1080p, "explainer/educational" template
- InVideo auto-matches stock footage to script lines
- Pre-built music bed; usually fine — pick "documentary" or "corporate"

**Option B: Paste Substack URL (faster, less control)**
- InVideo AI → "Generate Video" → "From Article URL"
- Paste your published Substack URL
- Tool auto-extracts text, generates script, matches visuals

**Replace voiceover with Eleven Labs MP3:**
- InVideo → upload your `voiceover-X.mp3`
- Sync to timeline; mute InVideo's default voiceover
- Auto-sync may need 1-2 manual nudges

**Tweak any visuals that look obviously wrong:**
- InVideo sometimes picks weird stock footage (e.g., "the stock market" → random unrelated office shot)
- Replace from InVideo's library — usually 2-3 swaps per video
- For finance-specific shots: trader floor, charts, ticker boards, executives, data centers

**Export:** 1080p, MP4, H.264

### Step 4: Thumbnail in Canva (5 min)

Use saved template. Replace:
- Headline (2-3 words max — *"NVDA EARNINGS"*, *"AI BUBBLE?"*, *"BUY OR SELL"*)
- Ticker symbol (large, mono font)
- One number or chart element
- Keep colors consistent across all videos

**Test:** Shrink to 200px wide and check if it's still readable. If not, the text is too small for the recommended sidebar.

Export 1280x720 PNG.

### Step 5: YouTube upload + metadata (5 min)

**Title formula:**
- *"NVDA Earnings: What to Watch Tonight"* — direct, search-optimized
- *"Why AVGO Could Outperform NVDA"* — comparison hook
- *"3 Things About [Ticker] Most Investors Miss"* — listicle

**Avoid:** "INSANE!!!", clickbait, all caps, exclamation marks.

**Description template:**
```
[2-sentence summary of the video]

📊 Read the full research: [Substack URL]
📈 Track record (show your misses): [Feedback log URL]
🐦 Daily takes: [Twitter URL]

— TIMESTAMPS —
0:00 Intro
0:30 [Topic 1]
2:00 [Topic 2]
4:30 [Topic 3]
6:00 What to watch next

— DISCLOSURE —
This is research, not investment advice. Stances are research stances. Verify before any decision.

#NVDA #AI #investing
```

**Tags (10-15):** mix of specific (NVDA earnings) + broad (stock market, AI investing) + niche (faceless finance, daily research)

**Thumbnail upload:** custom PNG from Canva (don't use auto-generated)

**End screen:** subscribe button + latest video + Substack link

**Schedule:** Same time every day (suggest 9:00 AM ET or 6:00 PM ET — finance audience peaks pre-market and after-close)

### Step 6: Auto-shorts via Opus Clip (5 min)

- Open Opus Clip → upload your finished YouTube video
- Click "ClipAnything" → AI selects 3-5 best moments
- Each short = 30-60 sec with auto-captions, vertical 9:16 reframe
- Review captions for finance terms (Opus sometimes mis-transcribes tickers — fix manually if needed)
- Export 3 best shorts
- Schedule to YouTube Shorts + TikTok + Instagram Reels (Opus has direct publishing for all 3)

**Pro tip:** title shorts with curiosity gaps: *"Most investors don't know this about NVDA…"* — drives swipe-through.

## Quality control checklist (per video, ~2 min)

Before publish:

- [ ] Voiceover audio levels even (no spikes or dips)
- [ ] No InVideo default voiceover bleeding through
- [ ] No obviously wrong stock footage (e.g., medical scene during "AI capex" line)
- [ ] Captions correctly spell tickers (NVDA not "envidia")
- [ ] Thumbnail readable at 200px width
- [ ] Title doesn't have clickbait phrases
- [ ] Description has Substack link + disclosure
- [ ] End screen has subscribe + Substack
- [ ] Schedule time set, not "Public" immediately (consistency > immediacy)

## What to NOT optimize (intentional shortcuts)

These are NOT worth your time if audience is non-savvy:

- **Perfect b-roll matching.** InVideo's stock footage is "good enough."
- **Custom music.** Built-in tracks are fine.
- **Transitions/animations.** Simple cuts work better than fancy transitions for retail.
- **Color grading.** Skip entirely.
- **Custom intro animation.** Skip; just start talking. Save 10 seconds at top = better retention.

## What IS worth time

- **Thumbnail.** Single biggest factor in CTR. Spend the 5 min.
- **Title.** Iterate before publish. Use TubeBuddy if you want A/B test feedback.
- **First 8 seconds of video.** Hook decides retention. Re-record voiceover until it lands.
- **Consistent voice/branding.** Same voice, same thumbnail family, same upload schedule.

## Realistic timeline

| Month | Subscribers | Watch time | What's happening |
|---|---|---|---|
| 1-3 | 0-100 | Low | Building. First 30-50 videos. Most subs from network. |
| 3-9 | 100-1,000 | Building | Apply for partner program ~month 6 (need 1K subs + 4K watch hours). |
| 9-18 | 1,000-10,000 | Compounding | Algorithm starts working. First viral video likely. |
| 18-36 | 10,000-50,000+ | High | $2-10K/mo possible at this scale in finance niche. |

**Critical:** 95% of finance YouTube channels die before 50 videos. Plan for 100 videos minimum before evaluating success.

## Daily Substack + YouTube combined workflow

| Time | Task | Tool |
|---|---|---|
| 8:30 AM | Write Substack article | Wiki + Claude.ai |
| 9:30 AM | Publish Substack | Substack |
| 9:35 AM | Generate voiceover | Eleven Labs |
| 9:45 AM | Generate video visuals | InVideo |
| 9:55 AM | Make thumbnail | Canva |
| 10:00 AM | Upload + schedule YouTube | YouTube Studio |
| 10:05 AM | Auto-clip shorts | Opus Clip |
| 10:10 AM | Cross-post shorts to TikTok + Reels | Opus / native |
| 10:15 AM | Post takes to Twitter | Twitter |

**Total: ~105 min/day for ONE article published across 5 platforms.** Daily cadence sustainable in 8-hour work day with hours to spare for engagement / research / wiki maintenance.

## What to track (weekly)

| Metric | Target month 3 | Target month 6 | Target month 12 |
|---|---|---|---|
| YouTube subs | 100 | 500 | 2,500 |
| Substack subs | 200 | 1,000 | 5,000 |
| Average video CTR | 4%+ | 5%+ | 6%+ |
| Average view duration | 40%+ | 45%+ | 50%+ |
| Substack open rate | 50%+ | 45%+ | 40%+ (declines with growth, normal) |
| Cross-platform share | 1-2/week | 5-10/week | 20+/week |

If CTR is <3% by month 3 → thumbnails are the problem. If view duration is <30% → hook is the problem. If subscribers aren't growing → upload more, or distribution is broken (work Twitter harder).

## Related
[[daily-substack-template]] · [[weekly-synthesis-template]] · [[overview]]
