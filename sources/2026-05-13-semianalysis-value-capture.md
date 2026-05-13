---
date: 2026-05-13
type: article
publisher: SemiAnalysis
url: https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model
raw_path: raw/articles/2026-05-13-semianalysis-ai-value-capture.md
touches: [NVDA, TSM, ai-bubble-debate, ai-capex-cycle, bottleneck-roadmap, overview]
---

# SemiAnalysis — AI Value Capture: The Shift to Model Labs

## TL;DR
- **Thesis inversion:** From 2023-2025 the value accrued to infrastructure (NVDA, memory, power). Starting late 2025, value is shifting to **model labs** (Anthropic, OpenAI) which capture 70%+ inference gross margins.
- **Anthropic ARR: $9B → $44B** in months. Effective blended token price ~$0.99/MTok despite $5/$25 sticker (cache + efficiency).
- **NVDA "leaving value on the table"** — capex per watt only ticked from $37.4/W → $38.1/W (GB300 → VR NVL72) despite nearly doubled TDP. SemiAnalysis's pricing model says NVDA could raise VR NVL72 pricing **~40%** and still leave room for neocloud margin expansion.
- **SOCAMM as the leverage point:** $8/GB in Q1 2026 → potentially **>$13/GB by EOY 2026**. Socketed memory enables disaggregated pricing the way GB300's soldered LPDDR5X did not.
- **Supply constraints peak H2 2026:** N3 utilization >100%, DRAM fabs >90%. HBM short supply through 2027.

## Key facts

### Anthropic economics (the key new datapoint)
- ARR explosion: $9B → $44B
- Inference gross margin: 38% → 70%+
- Effective blended token price: ~$0.99/MTok on agentic tasks (vs $5/$25 sticker)
- Cache hit rates 90%+; input:output ratio ~300:1 (Claude Code)
- Premium SKUs introduced: Opus Fast 6x pricing, Mythos $25/$125 (5x Opus)

### Hardware throughput
- GB300 vs H100 FP8: 17x; FP4: 32x
- GB300 TCO ~70% higher than H100 despite leap
- B300 DeepSeek R1: 14x variance based on software optimization

### Memory trajectory
- SOCAMM $8 → ~$10 mid-year → potentially $13+/GB EOY 2026
- LPDDR5X +6x YoY pricing
- N3 wafer utilization >100% H2 2026
- DRAM fabs >90% utilization
- HBM short supply through 2027

### NVDA pricing framework
- VR NVL72 cost-based floor: **$4.92/GPU hour** (5-yr, 15% prepay, 15.6% IRR)
- Value-based ceiling: **$12.25/GPU hour** ($/PFLOP parity with GB300)
- Current pricing: **$0.28/PFLOP — below historical trend**
- Headroom: ~40% NVDA price hike still leaves neocloud margin

## Key claims (confidence-rated)

| Claim | Confidence | Why it matters |
|---|---|---|
| Anthropic gross margin 70%+ on inference | High (SemiAnalysis internal data) | Validates model-lab value capture; tensions infra-only AI narrative |
| NVDA could raise prices 40% w/o losing customers | Medium-High | Direct upside to [[NVDA]] thesis; potential gross margin re-rating |
| SOCAMM pricing $8 → $13 EOY 2026 | Medium-High | Adds direct revenue line to NVDA accelerator BOM |
| Memory crunch sustains through 2027 | High (cross-confirmed by SK Hynix/Samsung) | Supports [[MU]] / [[SNDK]] / [[WDC]] supercycle bull case |
| TSMC "leaving value on table" | Medium-High | Same dynamic as ASML — questions when bottleneck holders extract |

## Quotes worth keeping

> "Anthropic's ARR has exploded from $9B to over $44B today, their gross margins on their inference infrastructure have increased from 38% to over 70% over the same period."

> "Nvidia is functioning like a 'central bank of AI' — maintaining ecosystem health over near-term margin capture."

> "Despite Nvidia controlling the scarce resource (compute), TSMC controlling manufacturing, and memory vendors facing supply tightness, these entities are *not* repricing to capture full value."

## Wiki updates made

### Updates
- [[NVDA]] — Add SemiAnalysis SOCAMM pricing trajectory + "could raise 40% and still leave neocloud margin" framing. Add VR NVL72 cost-floor / value-ceiling numbers.
- [[ai-bubble-debate]] — Add Anthropic ARR $9B→$44B + 70%+ inference margin as confirmation of "earnings are real" bull case. Add "value capture shift" framing.
- [[ai-capex-cycle]] — Cross-reference Anthropic margin data point.
- [[bottleneck-roadmap]] — Reinforce N3 >100% utilization + DRAM >90% data point in 2026 row.
- [[TSM]] — Add "leaving value on table" framing alongside CPU>GPU allocation discipline.

### Contradictions flagged
- Counter-tensions Dylan Patel's "H100 worth more today than 3 yrs ago" framing in [[2026-05-09-dwarkesh-dylan-semianalysis]] — actually consistent (both argue NVDA hasn't extracted), but with a different lens (Dylan: NVDA chose not to; SemiAnalysis: NVDA can still extract +40% from here)
- Tensions the [[ai-bubble-debate]] capex-hangover bear thesis — if inference margins are 70%+, capex IS earning its cost of capital
