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

## Tool stack — INFOGRAPHIC STYLE (updated 2026-05-15)

**Style target:** animated charts, big text overlays, number counters, minimal stock footage, single bold color scheme. Think Visual Capitalist, Statista, animated finance shorts. NOT talking-head with stock b-roll.

| Tool | Purpose | Monthly cost | URL |
|---|---|---|---|
| **Canva** (Magic Studio) ⭐ | Animated infographic templates + thumbnails + Magic AI generation | $13 | https://canva.com |
| **Flourish Studio** | Animated finance charts (bar race, line, pie) — the killer data-viz tool | Free / $69 | https://flourish.studio |
| **Eleven Labs** | Premium AI voiceover (consistent voice = your brand) | $22 | https://elevenlabs.io |
| **CapCut** | Free editor to combine voiceover + Flourish chart + Canva | Free | https://capcut.com |
| **Opus Clip** | Auto-clip long video into more shorts (optional) | $19 | https://opus.pro |
| **YouTube Studio** | Upload + schedule + analytics | Free | studio.youtube.com |

**Recommended starter (cheapest path): $35/mo** = Canva + Eleven Labs + free Flourish + free CapCut. Add Opus Clip later if you also produce long-form.

**Even simpler — Canva-only ($13/mo):** Canva alone has animated finance infographic templates + Magic Studio AI generation + voiceover input + 9:16 vertical export. For non-savvy audience that won't notice the difference, this is enough.

## Why this stack changed from the original recommendation

The original stack (InVideo AI + stock footage) is the "talking explainer with b-roll" style. **The infographic style is fundamentally different** — animated numbers, charts, and text overlays drive engagement, not stock footage. Tool choice has to match style choice.

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

### Step 3: Generate visuals (15 min)

For infographic style, this is a 2-tool combo: Flourish for animated charts + Canva for text overlays + branding.

**Sub-step 3a — Build animated chart in Flourish (5 min):**
- Open Flourish Studio → "New visualization"
- For "Top N" lists: pick **Bar chart race** template
- For "X over time" stories: pick **Line chart with animation**
- For "before vs after": pick **Bar chart with counter animation**
- Paste your data (e.g., CSV: Ticker, Value, Date)
- Pick brand colors (consistent navy/cream/orange palette)
- Export as MP4 video, 1920×1080 or 1080×1920 (vertical for shorts)

**Sub-step 3b — Add text overlays + branding in Canva (8 min):**
- Open Canva → search "animated finance infographic" template (vertical 1080×1920 for shorts; 1920×1080 for long-form)
- Pick a template, customize:
  - Replace headline with your title (2-3 words)
  - Replace stat with your number
  - Replace ticker with the one your video is about
  - Apply your consistent color palette
- Upload your Flourish chart MP4 as a video element
- Position chart prominently — chart is the visual anchor
- Add timing: text overlays appear at script beats

**Sub-step 3c — Combine voiceover (in CapCut OR Canva) (2 min):**
- Drag Eleven Labs voiceover MP3 onto timeline
- Trim or stretch chart animation timing to match voiceover
- Add background music at low volume (Canva has built-in royalty-free; CapCut has "Trending sounds")
- Auto-captions: CapCut has free auto-captions; Canva has Magic Captions in Pro

**Even simpler — Canva-only path:**
- Skip Flourish; use Canva's built-in animated chart elements
- Slightly less polished but 60% faster — fine for the audience
- Total time for visuals: 8 minutes

**Export:** 9:16 MP4 for shorts; 16:9 MP4 for long-form. 1080p, H.264.

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

- **Pixel-perfect chart styling.** Flourish defaults are fine.
- **Custom music.** Canva/CapCut built-in tracks work.
- **Hand-drawn animations.** Stick to Flourish's auto-animation presets.
- **Color grading.** Skip entirely.
- **Custom intro animation.** Skip; jump straight to the hook. Save 10 seconds at top = better retention.
- **Multiple animation styles.** Pick one chart type (bar race OR line OR pie) per video. Mixing styles confuses retail viewers.

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

## Daily Substack + YouTube combined workflow (infographic style)

| Time | Task | Tool |
|---|---|---|
| 8:30 AM | Write Substack article | Wiki + Claude.ai |
| 9:30 AM | Publish Substack | Substack |
| 9:35 AM | Generate voiceover | Eleven Labs |
| 9:45 AM | Build animated chart | Flourish (or skip if Canva-only) |
| 9:55 AM | Build infographic + text overlays | Canva |
| 10:05 AM | Combine voiceover + visuals + music | CapCut (or directly in Canva) |
| 10:15 AM | Make thumbnail | Canva |
| 10:20 AM | Upload + schedule YouTube long-form (16:9 version) | YouTube Studio |
| 10:25 AM | Build 1-3 vertical short versions (re-use chart, vertical text) | Canva |
| 10:35 AM | Cross-post shorts to TikTok + Reels + YT Shorts | Native uploads |
| 10:40 AM | Post takes to Twitter | Twitter |

**Total: ~130 min/day for ONE article published across 5 platforms with infographic style.** Slightly more than stock-footage style because chart-building takes a few extra minutes. Still sustainable in 8-hour day.

**Speed shortcut:** if Substack is your primary, you can skip long-form YouTube some days and ONLY do the 9:16 vertical shorts (60-90 seconds each). Total time drops to ~75 min/day for Substack + 3 vertical shorts cross-posted to all 3 short platforms.

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
