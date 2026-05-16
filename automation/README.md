# Automation — MVP Build Directory

This directory contains the assets needed to wire up the full automation pipeline. See [[wiki/playbooks/full-automation-pipeline.md]] for the full runbook.

## Contents

- `README.md` — this file
- `google-sheet-template.csv` — starter rows for the idea queue. Import into a new Google Sheet.
- `n8n-credentials.template.env` — template for your API keys (DO NOT COMMIT FILLED VERSION — added to .gitignore)
- `creatomate-template-spec.md` — exact element structure for the Creatomate video template

## Quick start

1. **n8n local** — already running at http://localhost:5678 (started via npx; restart with `N8N_USER_FOLDER=~/n8n-data npx --yes n8n start`)
2. **Sign up for 6 services** (see playbook): OpenAI, ElevenLabs, PiAPI, Creatomate, upload-post.com, Google Cloud
3. **Import n8n template 3442** from https://n8n.io/workflows/3442-fully-automated-ai-video-generation-and-multi-platform-publishing/
4. **Paste credentials** into each n8n node
5. **Create Google Sheet** from `google-sheet-template.csv`
6. **Create Creatomate template** per `creatomate-template-spec.md`
7. **Test run** with the first row in the sheet
8. **Iterate prompts** until output is acceptable
9. **Activate daily schedule**

## Cost expectations

| Item | Monthly |
|---|---|
| n8n (self-hosted) | $0 |
| OpenAI API | $5-10 |
| ElevenLabs Creator | $22 |
| PiAPI | $10-20 |
| Creatomate Starter | $41 |
| upload-post.com | $10-15 |
| Per-video API costs (~$0.50 × 30) | $15 |
| **Total** | **$103-123** |

## Security

API keys go in `n8n-credentials.template.env` locally, OR directly into n8n's credentials UI (recommended — encrypted at rest). NEVER commit filled credentials to git.
