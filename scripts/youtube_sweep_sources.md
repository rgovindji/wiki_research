# Curated source roster + search algorithm — daily sweep (and general web research)

Purpose: a maintained roster + repeatable algorithm so the daily sweep (and any ad-hoc web
research) finds high-signal AI/semis/power/compute material instead of relying on ad-hoc keyword
search. **Lesson (2026-06-20):** name-based searches miss conference talks (e.g. the Baseten
"inference billion-x" and Katti talks). Fix = **persona-tiered discovery** below + citation-chase.

This algorithm applies to **both YouTube transcription AND general WebSearch/WebFetch research.**

---

## THE 6-TIER PERSONA ALGORITHM (run every tier each sweep)

For each tier: search recent (last ~30-60 days) talks/interviews/posts; dedupe vs `sources/` +
`log.md`; keep only items clearing the relevance filter; cap the whole sweep at ~3-5 transcribes/day
(rotate which tiers get the slots so all six get covered across a week).

### Tier 1 — Major players (thought leaders; what they say shapes the future)
Frontier-lab + key-company leadership. Their roadmap statements ARE the forward signal.
- Sam Altman (OpenAI) · Dario Amodei (Anthropic) · Demis Hassabis (DeepMind) · Jensen Huang (NVDA)
- Satya Nadella (MSFT) · Sundar Pichai (GOOGL) · Mark Zuckerberg (META) · Elon Musk (xAI/Tesla)
- Lisa Su (AMD) · Ilya Sutskever (SSI) · Mira Murati (Thinking Machines) · C.C. Wei (TSMC) · Mustafa Suleyman
- Search: "<name> interview 2026", "<name> keynote 2026", "<name> fireside 2026"

### Tier 2 — Tier-2 leaders (execs + scaled-startup founders one rung down)
Operators building the actual infra/products; often more candid than Tier 1.
- Brad Lightcap / Greg Brockman / Kevin Weil (OpenAI) · Mike Krieger (Anthropic) · Aravind Srinivas (Perplexity)
- Arthur Mensch (Mistral) · Jonathan Ross (Groq) · Tuhin Srivastava (Baseten) [ingested] · Sachin Katti (OpenAI compute) [ingested]
- Alexandr Wang (Meta/Scale) · Clem Delangue (HuggingFace) · Thomas Kurian (Google Cloud) · Matt Garman (AWS) · Cristiano Amon (Qualcomm) · Scott Wu (Cognition/Devin)
- Search: "<name> 2026 talk/interview", + the companies' eng/keynote channels

### Tier 3 — Researchers / academics / analysts (PhDs, the technical truth layer)
The people who know what's actually happening under the hood; least hype, most falsifiable.
- Dylan Patel (SemiAnalysis) [ingested x4] · Nathan Lambert (Ai2 / Interconnects) [QUEUED — high priority]
- Sholto Douglas · Trenton Bricken · Chris Olah (Anthropic) · Tri Dao (Together) · Noam Brown (OpenAI)
- Andrej Karpathy · Jim Fan / Sergey Levine (robotics) · Yann LeCun · Percy Liang · Jared Kaplan · Horace He · Chip Huyen
- Outlets: semianalysis.com, Epoch AI, SemiWiki, Interconnects, Ai2
- Search: "<name> talk 2026", "<lab> research talk 2026", conference enum (NeurIPS/ICML/ISCA/Hot Chips/GTC)

### Tier 4 — Major investors (where the capital + positioning is going)
- Gavin Baker (Atreides) [ingested] · Brad Gerstner + Bill Gurley (BG2/Altimeter) [ingested x3]
- Stanley Druckenmiller · Philippe Laffont (Coatue) · Josh Wolfe (Lux) · Chamath Palihapitiya
- Vinod Khosla · Marc Andreessen / Ben Horowitz (a16z) · Mary Meeker (BOND) · Sarah Guo / Elad Gil (No Priors) [ingested]
- Hosts to enum: Invest Like the Best, BG2, No Priors, a16z, Sequoia Training Data, Bg2
- Search: "<name> AI 2026 interview", "<fund> AI outlook 2026"

### Tier 5 — Contrarians / bears (the falsifiable other side — REQUIRED for anti-sycophancy)
- Ed Zitron · Paul Kedrosky · Jim Chanos · Michael Burry · Gary Marcus · Daron Acemoglu
- Aswath Damodaran (NYU) · David Cahn (Sequoia "$600B question") · Jeremy Grantham (GMO)
- Search: "AI bubble 2026 <name>", "AI capex skeptic 2026", "data center overbuild 2026"
- Goal: keep the bear watch-list in [[ai-bubble-debate]] fed with the strongest opposing case.

### Tier 6 — Developers using LLMs (ground truth on real adoption + unit economics)
What practitioners actually ship reveals demand/ROI before it shows in financials.
- swyx (Latent Space) · Simon Willison · Mitchell Hashimoto · antirez · Theo (t3.gg) · Geoffrey Huntley
- Pieter Levels · the Cursor / Cognition / Windsurf / Replit teams · indie-hacker + agent-builder talks
- Search: "AI coding agents 2026 real usage", "<dev> LLM 2026 talk", "Claude Code / Codex production 2026"
- Signal to extract: token-consumption reality, which models win in practice, where agents break.

---

## Cross-cutting passes (run alongside the tiers)
1. **Conference-series enumeration** — Stanford "Economics of AI", GTC, Hot Chips, Latent Space LIVE, a16z/Sequoia summits host the Tier-1/2/3 talks that name-search misses.
2. **Citation-chase** — when a new transcript names a person/company/chip, queue them next sweep.
3. **Channel RSS enumeration (most reliable ID source)** — use `scripts/yt_rss.sh <channel_id|@handle> [DAYS]` or `scripts/yt_rss.sh --roster 45`. RSS (`youtube.com/feeds/videos.xml?channel_id=…`) returns the latest ~15 uploads with dates — far more reliable than WebSearch for Tier-3/6. **Handle→ID auto-resolve is flaky → hardcode channel_ids in the script roster.** Confirmed IDs: Latent Space `UCxBcwypKK-W3GHd_RZ9FZrQ`, Damodaran `UCLvnJL8htRR1T9cbSccaoVw`. TODO: resolve + cache channel_ids for Dwarkesh, BG2, No Priors, Interconnects, SemiAnalysis (the daily sweep should resolve once and append to the roster).
4. **Macro/power** — nuclear/SMR/grid + Fed/rates when they move the discount rate.

## Relevance filter (transcribe only if it clears the bar)
NEW + specific + investable signal on: AI compute demand/supply, semis (logic/memory/networking/
custom-silicon/CPU), power/cooling/nuclear, inference economics, model-lab capex commitments,
robotics/physical AI, or a falsifiable dated catalyst. Skip news recaps, PT listicles, vendor PR.
Always check `sources/` + `log.md` first to avoid re-ingesting.

## Already ingested (do not re-propose)
BG2 ×3 (buildout / china-rareearths / bubble-stablecoin) · Dylan Patel ×4 (Dwarkesh 5/9, ILTB 5/16,
Daytona, No Priors 127) · Dwarkesh sample-efficiency · Katti Stanford · Baseten/Tuhin · Gavin Baker ILTB 5/21.
