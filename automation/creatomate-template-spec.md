# Creatomate Template Specification

Create one template in Creatomate (https://creatomate.com/templates) with the structure below. Save the template ID — n8n will reference it.

## Format

- **Aspect ratio:** 9:16 (vertical)
- **Resolution:** 1080 × 1920
- **Duration:** 60 seconds (auto-trims to voiceover length)
- **Frame rate:** 30 fps

## Required dynamic elements (n8n maps to these by name)

| Element name | Type | Behavior | Notes |
|---|---|---|---|
| `voiceover` | Audio | Plays full duration, volume 100% | The ElevenLabs MP3 |
| `image-1` | Image | 0-12 sec, Ken Burns slow zoom | First Flux image |
| `image-2` | Image | 12-24 sec, Ken Burns slow zoom | Second image |
| `image-3` | Image | 24-36 sec, Ken Burns slow zoom | Third image |
| `image-4` | Image | 36-48 sec, Ken Burns slow zoom | Fourth image |
| `image-5` | Image | 48-60 sec, Ken Burns slow zoom | Fifth image |
| `title-text` | Text | Top overlay, 0-60 sec | Headline (2-3 words) |
| `subtitle-text` | Text | Below title, 0-60 sec | Ticker or key number |
| `caption-text` | Text | Bottom 1/3, auto-sync with audio | Generated captions |

## Static elements (set once, don't expose to API)

- **Background music:** royalty-free track from Creatomate library at 15% volume
- **Brand logo:** small in corner (your channel logo)
- **End card:** "Subscribe + Substack link" overlay last 3 seconds

## Style

- **Fonts:**
  - Title: bold sans-serif (Inter Black or similar)
  - Subtitle: monospace (JetBrains Mono — matches your wiki brand)
  - Captions: clean sans (Inter Regular) with shadow for readability
- **Colors:** navy (#11427d), cream (#fbfaf7), orange accent (#cc785c). Matches wiki design language.
- **Image filter:** subtle dark overlay (~20%) so text is readable over any image

## Starter template (clone these)

Creatomate has these free starter templates that match the structure:

1. **"AI Shorts Template"** — search Creatomate template library
2. **"Vertical Story Slideshow"** — has the 5-image structure with Ken Burns
3. **"News Update Vertical"** — finance-friendly aesthetic

Clone one, customize element names to match the table above, save. Done.

## How n8n references this template

In the n8n HTTP request to Creatomate, the body uses:

```json
{
  "template_id": "YOUR-TEMPLATE-ID-HERE",
  "modifications": {
    "voiceover.source": "{{$('ElevenLabs').item.json.audio_url}}",
    "image-1.source": "{{$('PiAPI Flux').item.json.images[0]}}",
    "image-2.source": "{{$('PiAPI Flux').item.json.images[1]}}",
    "image-3.source": "{{$('PiAPI Flux').item.json.images[2]}}",
    "image-4.source": "{{$('PiAPI Flux').item.json.images[3]}}",
    "image-5.source": "{{$('PiAPI Flux').item.json.images[4]}}",
    "title-text.text": "{{$('Google Sheet').item.json.Topic}}",
    "subtitle-text.text": "{{$('Google Sheet').item.json.Ticker}}",
    "caption-text.text": "{{$('OpenAI Script').item.json.captions}}"
  }
}
```

## Per-video customization

For each row in your Google Sheet, n8n auto-fills the dynamic elements. You only edit the template if you want a new style.

## Iteration plan

| Version | When | Changes |
|---|---|---|
| v1.0 | Day 1 | Static template, AI-generated images |
| v1.1 | Day 7 | Add brand logo overlay |
| v1.2 | Day 14 | Tune font/color based on viewer feedback |
| v2.0 | Day 45 | Replace one of image slots with Flourish chart MP4 for data accuracy |
