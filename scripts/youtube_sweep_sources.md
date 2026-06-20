# Curated YouTube source list — daily sweep

Purpose: a maintained roster so the daily sweep finds high-signal AI/semis/power/compute
videos instead of relying on ad-hoc keyword search. **Lesson (2026-06-20):** name-based
searches ("Dylan Patel interview") miss conference talks like the Baseten "inference billion-x"
and Katti talks. Fix = enumerate CHANNELS/PLAYLISTS + search by THEME/CONFERENCE, and when a
transcript names a person/company, queue their recent talks.

## Search strategy (run all four passes each sweep)
1. **Channel/playlist enumeration** — for each channel below, WebFetch the `/videos` page (or playlist) and pull video IDs uploaded since the last sweep date.
2. **Conference-series enumeration** — the Stanford "Economics of AI / AI supercycle" series hosts Katti + Baseten; enumerate the host channel/playlist for sibling talks.
3. **Theme search** — WebSearch dated theme queries: "AI inference scaling 2026 talk", "data center power 2026 keynote", "RL environments agents 2026", "custom silicon ASIC 2026 interview", "memory HBM supercycle 2026".
4. **Citation chase** — when a new transcript names a person/company/chip, queue that name's recent videos next sweep.

## Expert roster (search each + chase new uploads)
- **Nathan Lambert** (Interconnects / Ai2) — open models, RL post-training. View: "open models in perpetual catch-up" (leans Katti's 6-month-lead side of the [[inference-economics]] moat debate). HIGH PRIORITY — not yet ingested.
- **Dylan Patel** (SemiAnalysis) — semis/compute supply chain. [ingested 5/9, 5/16, 6/20 x2]
- **Dwarkesh Patel** — frontier AI. [ingested 5/9, 6/20]
- **Tuhin Srivastava** (Baseten) — inference infra/economics. [ingested 6/20]
- **Sachin Katti** (OpenAI) — industrial compute. [ingested 6/20]
- Sholto Douglas / Trenton Bricken (Anthropic) — scaling, interpretability
- Tri Dao (Together) — kernels/efficiency
- Jonathan Ross (Groq) — inference ASIC
- Chip Huyen — ML systems/economics
- Gavin Baker (Atreides) — public markets AI. [ingested 5/21]

## Channels / shows (enumerate recent uploads)
- BG2 Pod (Gerstner/Gurley) [ingested 6/20 x3]
- Invest Like the Best (Patrick O'Shaughnessy) [ingested 5/16, 5/21]
- No Priors (Sarah Guo / Elad Gil) [ingested 6/20]
- Latent Space (swyx)
- a16z
- Sequoia Capital (Training Data)
- Stratechery / Sharp Tech (Ben Thompson)
- Stanford eCorner / GSB / "Economics of AI" series (Katti + Baseten origin)
- TBPN / All-In (macro + AI, lower signal — skim)
- SemiAnalysis (own channel)
- Interconnects (Nathan Lambert)

## Macro / power / energy
- Nuclear/SMR + grid + datacenter-power interviews (search "AI data center power 2026", "SMR datacenter PPA 2026")
- Fed/rates interviews when they move the discount rate (rates drive the whole book)

## Relevance filter (only transcribe if it clears the bar)
Transcribe a video only if it plausibly contains NEW, specific, investable signal on: AI compute
demand/supply, semis (logic/memory/networking/custom silicon/CPU), power/cooling/nuclear,
inference economics, model-lab capex commitments, robotics/physical AI, or a falsifiable
dated catalyst. Skip pure news recaps, price-target listicles, and vendor PR.
Always check sources/ + log.md first to avoid re-ingesting.
