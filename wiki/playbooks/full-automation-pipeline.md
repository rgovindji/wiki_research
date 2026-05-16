---
type: analysis
tags: [template, automation, n8n, youtube, mvp, runbook]
last_updated: 2026-05-15
last_full_review: 2026-05-15
sources: 0
status: mvp-build
---

# Full Automation Pipeline — MVP Runbook

> **Goal:** End-to-end automated pipeline. Substack publishes → AI generates video → uploads to YouTube + TikTok + Instagram + Reels. Hands-off after setup.

> **Architecture:** Local n8n (workflow engine) + 6 API services + 1 Google Sheet (idea queue) + 1 Creatomate template.

> **MVP scope:** Finance niche, daily output, 60-90 second shorts. Defer chart accuracy to v2 — for now, accept that AI-generated visuals are slop and iterate.

## The architecture

```
Google Sheet (idea queue)
    ↓ (daily schedule trigger)
n8n local (localhost:5678) — orchestrates everything
    ↓
OpenAI → script (~150 words)
    ↓
ElevenLabs → voiceover MP3
    ↓
OpenAI → 5 image prompts from script
    ↓
PiAPI (Flux) → 5 images
    ↓
[OPTIONAL v2: PiAPI Kling → image-to-video clips]
    ↓
Creatomate → assemble voiceover + images + captions + music → final MP4
    ↓
OpenAI → YouTube title + description + tags
    ↓
upload-post.com → publish to YouTube + TikTok + Instagram + Facebook
    ↓
Update Google Sheet (mark done)
    ↓
Discord webhook (completion notification)
```

## Local setup status

n8n is running locally at **http://localhost:5678** (started via npx, data persisted in `~/n8n-data`).

If you need to restart:
```bash
N8N_USER_FOLDER=~/n8n-data npx --yes n8n start
```

To run on Docker instead (more stable for production):
```bash
# First start Docker Desktop, then:
docker run -d --name n8n -p 5678:5678 \
  -v ~/n8n-data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

## API services — sign up & get keys

Do this BEFORE importing the workflow. Time: ~30-45 min for all signups.

| # | Service | URL | What you need | Cost |
|---|---|---|---|---|
| 1 | **OpenAI** | https://platform.openai.com | API key | ~$5-10/mo at daily volume |
| 2 | **ElevenLabs** | https://elevenlabs.io | API key + pick one voice → save voice_id | $22/mo Creator tier |
| 3 | **PiAPI** | https://piapi.ai | API key | ~$10-20/mo |
| 4 | **Creatomate** | https://creatomate.com | API key + create template → save template_id | $41/mo Starter |
| 5 | **upload-post.com** | https://upload-post.com | API key + connect YT/TT/IG/FB accounts | ~$10-15/mo |
| 6 | **Google Cloud** | https://console.cloud.google.com | OAuth credentials for Sheets API | Free |
| 7 | **Discord** | (your server) | Webhook URL for notifications | Free |

**Total monthly cost: ~$110-130/mo** (excluding n8n which is free self-hosted).

### Signup checklist (sequence matters for some)

1. **OpenAI first.** Sign up → billing → add $10 credit → API keys → create new key. Save as `OPENAI_API_KEY`.
2. **ElevenLabs.** Sign up → Voice Library → preview voices → pick ONE → click voice → copy voice_id. Profile → API key → save as `ELEVENLABS_API_KEY`.
3. **PiAPI.** Sign up → API keys → generate. Save as `PIAPI_KEY`.
4. **Creatomate.** Sign up → create one template (see template setup below) → save template_id. Profile → API key → save as `CREATOMATE_API_KEY`.
5. **upload-post.com.** Sign up → connect each platform via OAuth (YouTube, TikTok, Instagram, Facebook). API key under settings.
6. **Google Cloud Console.** Create project → enable Sheets API + Drive API → create OAuth 2.0 client → download JSON. Add as n8n credential.
7. **Discord webhook.** Your Discord server → settings → integrations → webhooks → new webhook → copy URL.

## Creatomate template setup (the most custom part)

You need to create a vertical (9:16) video template with these dynamic elements:

| Element name | Type | What it holds |
|---|---|---|
| `voiceover` | Audio | The ElevenLabs MP3 |
| `image-1` | Image | First Flux-generated image |
| `image-2` | Image | Second Flux image |
| `image-3` | Image | Third Flux image |
| `image-4` | Image | Fourth Flux image |
| `image-5` | Image | Fifth Flux image |
| `title-text` | Text | Big headline overlay |
| `subtitle-text` | Text | Secondary overlay (ticker / number) |
| `caption-text` | Text | Auto-captions (synced with audio) |

**Template duration:** 60 seconds (auto-trims to voiceover length)
**Aspect ratio:** 9:16 (1080 × 1920)
**Image behavior:** Ken Burns effect (slow zoom) on each image, ~12 seconds each
**Music:** Add background track at 15% volume

**Creatomate has a free "AI Shorts" template you can clone as starting point.**

Save the template_id from the URL: `creatomate.com/templates/<this-id>`

## Google Sheet — idea queue

Create a new Google Sheet with these columns:

| A: Date | B: Topic | C: Ticker | D: Key Number | E: Status | F: Video URL | G: Notes |
|---|---|---|---|---|---|---|
| 2026-05-18 | NVDA earnings preview | NVDA | $78.98B consensus | pending | | Monday macro |
| 2026-05-19 | AVGO deep dive | AVGO | 5GW TPU deal | pending | | |

n8n reads the next row where Status = "pending", processes it, updates Status to "done" + adds Video URL.

**You curate the topics + key numbers; AI does everything else.**

## Importing the n8n workflow

### Option 1: Start from existing template (fastest)

1. Open n8n at **http://localhost:5678**
2. Top right menu → "Templates"
3. Search "AI video generation multi-platform"
4. Pick: **"Fully automated AI video generation & multi-platform publishing"** (template ID 3442)
5. Click "Use this template"
6. n8n will prompt for credentials at each node — paste your API keys

### Option 2: Build from scratch (more control)

Use the architecture diagram above. Each node:

1. **Schedule Trigger** — daily 9:00 AM
2. **Google Sheets node** — read first row with Status="pending"
3. **OpenAI node** — script generation prompt:
   ```
   You are writing a 60-second YouTube Short script for retail investors. 
   Topic: {{topic}}. Ticker: {{ticker}}. Key number: {{key_number}}.
   Format: hook in first 8 seconds, body explains, end with "what this means for you".
   No jargon — define every acronym. Conversational tone. 150 words max.
   ```
4. **HTTP Request → ElevenLabs** — POST to `https://api.elevenlabs.io/v1/text-to-speech/{{voice_id}}`
5. **OpenAI node** — image prompt generation:
   ```
   For this script: {{script}}, generate 5 image prompts for finance b-roll. 
   Style: clean, modern, professional. Each prompt should match one chunk of the script. 
   Return JSON array of 5 strings.
   ```
6. **HTTP Request → PiAPI** — generate images via Flux
7. **HTTP Request → Creatomate** — POST to `/v1/renders` with template_id + all assets
8. **Wait node** — 90 seconds for render
9. **HTTP Request → Creatomate** — GET render status
10. **OpenAI node** — generate title + description:
    ```
    Generate YouTube Short metadata:
    - Title: 60 chars max, curiosity hook, no clickbait
    - Description: 200 chars, includes Substack link
    - Tags: 10 relevant tags
    Topic: {{topic}}, Ticker: {{ticker}}.
    ```
11. **HTTP Request → upload-post** — multi-platform publish
12. **Google Sheets node** — update row Status="done", paste video URL
13. **Discord node** — webhook notification with URL

## First video — runbook

After all credentials are in n8n:

### Step 1: Test the workflow manually (5 min)

- Open the workflow in n8n
- Add one test row to Google Sheet: `2026-05-15 | Test | NVDA | $216 | pending | | MVP test`
- Click "Execute workflow" (manual run, top right)
- Watch each node execute. Red ❌ = error; green ✓ = success
- Common first-run errors: API key not pasted, voice_id wrong, Creatomate template missing elements

### Step 2: Inspect each output

For each node that succeeded:
- **OpenAI script:** read it. Does it sound right? (If not, tweak prompt)
- **ElevenLabs MP3:** play it. Does the voice sound human? (If robotic, try different voice_id)
- **PiAPI images:** preview them. Do they roughly match the script? (If random, tighten image prompts)
- **Creatomate render:** open the URL. Does the video play? (If garbled, fix template element names)
- **upload-post output:** check YouTube. Did it appear? (May take 1-5 min to process)

### Step 3: Tweak prompts (the iteration loop)

The MVP will produce slop the first 5-10 runs. **Expected.**

Each iteration, tighten one thing:
- **Script prompt:** make hooks stronger, simplify language
- **Image prompt:** add style constraints ("clean infographic," "no people")
- **Title prompt:** add formula constraints ("must include number or ticker")

Aim for "good enough to publish" by run 10-15.

### Step 4: Activate the daily schedule

Once a test run produces an acceptable video:
- Go to Schedule Trigger node → "Active"
- n8n will fire daily at 9 AM
- You only need to: keep filling Google Sheet rows with topics + tickers + key numbers

## The realistic timeline

| Day | What happens |
|---|---|
| Day 1 (today) | Sign up for 6 API services, get keys. n8n already running. |
| Day 2 | Import workflow, paste credentials, configure Creatomate template. |
| Day 3 | First test run. Probably broken. Debug. |
| Day 4 | Second test run. Slop output. Iterate prompts. |
| Day 5 | Third test run. Closer. Iterate again. |
| Day 6-7 | 10th test run. Acceptable quality. Activate daily schedule. |
| Day 8+ | Daily videos publishing. Tweak as needed. |

**Total time to "publishing daily" MVP: 7 days.** First 3 days are heavy setup; rest is iteration.

## Dealing with slop (iteration roadmap)

The first 30 days will produce mediocre videos. Plan for this. Improvement priorities:

| Iteration phase | Focus | Expected improvement |
|---|---|---|
| **Days 1-7** | Make pipeline work end-to-end | "It runs!" |
| **Days 8-21** | Tighten script prompts (hook, structure, voice) | "It doesn't embarrass you" |
| **Days 22-45** | Tighten image prompts + Creatomate template polish | "Looks pro" |
| **Days 46-60** | Add Flourish chart generation for accuracy | "Differentiated from competitors" |
| **Day 60+** | A/B test thumbnails, titles, posting times | "Actually growing" |

## What NOT to optimize in MVP

- **Chart accuracy** — AI-generated charts will be wrong. Accept this for now. Add Flourish step in v2 (day 45+).
- **Brand consistency** — pick one Eleven Labs voice + one Creatomate template + one Canva thumbnail style. Don't iterate on these in MVP.
- **Multi-platform optimization** — upload same video to all platforms. Optimize aspect ratios in v2.
- **A/B testing** — wait until you have 20+ videos before A/B testing anything.

## Monitoring & quality control

### Daily check (5 min)

1. Discord channel: did the notification fire? (If no, the workflow broke)
2. Check the video on YouTube before it goes "Public"
3. If quality bad: don't publish; flag for prompt iteration

### Weekly check (30 min)

1. YouTube Studio: which videos got the most views/CTR?
2. Substack analytics: subscriber delta this week
3. Prompt iteration: tighten whichever stage is producing the worst output

## Cost monitoring

n8n has a "Track Cost" feature OR you can manually log per-video cost in the Google Sheet.

Expected per-video cost: **$0.30-0.80**
- OpenAI: ~$0.05 (3 calls @ ~1500 tokens total)
- ElevenLabs: ~$0.10 (60 seconds of audio)
- PiAPI Flux: ~$0.15 (5 images)
- Creatomate: ~$0.20 (60-second render)
- upload-post: included in monthly plan

**At 30 videos/month: ~$15-25 in API usage on top of base subscriptions.**

## When the pipeline breaks (it will)

Common failure modes:

| Failure | Cause | Fix |
|---|---|---|
| OpenAI rate limit | Daily quota hit | Add 2-min wait between calls; upgrade tier |
| ElevenLabs char limit | Script too long | Cap script generation prompt at 150 words |
| PiAPI timeout | Server overloaded | Retry logic in workflow (n8n has built-in retry) |
| Creatomate render fails | Template mismatch | Check template elements match node mapping |
| upload-post rejection | Platform spam filter | Add 30-min stagger between platform uploads |

**Add retry + error nodes to every external API call.** n8n makes this trivial.

## Going from MVP to v2 (after 30 days)

Once daily pipeline is stable:

1. **Add Flourish chart step** — pull data from Google Sheet, generate accurate chart MP4, insert into Creatomate template
2. **Add Opus Clip step** — auto-clip long-form videos (if you do them) into shorts
3. **Add Eleven Labs voice variants** — different voice per video category (macro / single-name / sector)
4. **Add SEO step** — TubeBuddy or VidIQ API for title/tag optimization
5. **Add scheduled long-form** — once a week, a 5-10 min YouTube long-form

## Related
[[youtube-pipeline]] · [[daily-substack-template]] · [[daily-2026-05-18-monday-macro]] · [[overview]]

## Sources
- [n8n Template #3442: Fully Automated AI Video Generation & Multi-Platform Publishing](https://n8n.io/workflows/3442-fully-automated-ai-video-generation-and-multi-platform-publishing/)
- [Creatomate: How to Automate Video Creation with n8n](https://creatomate.com/blog/how-to-automate-video-creation-with-n8n)
- [FluxNote: Faceless YouTube Automation Workflow](https://fluxnote.io/guides/faceless-youtube-automation-with-ai)
- [Virvid: AI Faceless YouTube 2026 Stack](https://virvid.ai/blog/ai-faceless-youtube-automation-stack-2026)
