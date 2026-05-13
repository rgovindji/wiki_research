---
type: source
title: "The Coding Assistant Breakdown: More Tokens Please (Hands On With GPT 5.5, Opus 4.7, DeepSeek V4, Why Benchmarks Are Bad, and Who's Going To Win)"
authors: Max Kan, Jordan Nanos, Samuel Kruse, and 4 others (SemiAnalysis)
publication: SemiAnalysis Newsletter
date_published: 2026-04-24
date_read: 2026-05-09
url: https://newsletter.semianalysis.com/p/the-coding-assistant-breakdown-more
local_file: raw/articles/The Coding Assistant Breakdown_ More Tokens Please.pdf
tags: [ai, model-labs, anthropic, openai, deepseek, value-capture, token-economics]
---

# 2026-04-24 — The frontier-model coding race (GPT-5.5 vs Opus 4.7 vs DeepSeek V4)

33-page hands-on breakdown of the major model releases since the Claude Code inflection point (Feb 5, 2026). Read pages 1-15.

## Pricing landscape (per 1M tokens)

| Model | Input | Output |
|---|---|---|
| GPT-5.4 — Standard | $2.50 | $15 |
| **Claude Opus 4.7 — Standard** | $5.00 | $25 |
| **GPT-5.5 — Standard** | $5.00 | $30 |
| GPT-5.4 — Priority | $5.00 | $30 |
| GPT-5.5 — Priority (2.5x rate) | $12.50 | $75 |
| **Claude Opus 4.6 — Fast mode** | $30 | $150 |
| GPT-5.4 Pro / GPT-5.5 Pro | $30 | $180 |

**Which means:** GPT-5.5 is now **more expensive than GPT-5.4** and slightly more than Opus 4.7 — a pricing inversion. SemiAnalysis explicitly calls out that **"cost per task, not cost per token, is the true north star metric"** — token-efficient models can be more expensive per token but cheaper per task.

## GPT-5.5 ("Spud") — key findings

- First public release based on OpenAI's "Spud" pretrain (Anthropic's parallel pretrain codename = "Capybara")
- Post-training (RL) only on a 100k GB200 NVL72 cluster — never achieved that scale in pretraining
- "Materially better at some tasks than all other models" per SemiAnalysis
- GPT-5.5 Pro got SOTA on BrowseComp and FrontierMath
- Token-efficient (~35% fewer tokens than GPT-5.4 for equivalent task) — implicit price cut

## Opus 4.7

- Drop-in replacement for Opus 4.6
- "Small improvement" — engineers are reluctant adopters
- **Fast mode does not exist yet** for 4.7 (vs Opus 4.6 Fast at $30/$150) — engineers willing to sacrifice quality for 2.5x speed
- **New tokenizer adds ~35% to token usage = implicit 35% price increase**
- Anthropic Apr 23 postmortem disclosed 3 separate bugs (Mar 4 – Apr 20) that degraded Opus 4.6 quality across weeks. Users had complained for weeks; Anthropic categorically denied; but users were right. **Which means:** Anthropic's QA discipline is being tested as Claude Code monetization explodes — operational risk for the model-labs value-capture thesis.

## Dylan's smoking-gun datapoint

> "Claude Code spend had gotten to **$10.95M runrate peak at SemiAnalysis**. But then Opus 4.7 saved me. More token efficient for tasks, smarter, and no fast mode. Thank you @AnthropicAI. You saved me from bankruptcy."

SemiAnalysis's own internal Claude Code burn rate was approaching $11M/yr — for a single firm. **Which means:** Anthropic's API monetization is exploding faster than even the bullish narrative suggests. Token consumption per power-user is multiples of pre-Claude-Code levels.

## DeepSeek V4 — open-source frontier

Two models: V4-Pro (1.6T total / 49B active) and V4-Flash (284B / 13B). Both have **1M-token context**, FP4+FP8 mixed precision.

### Major technical advances

- Compressed Sparse Attention (CSA)
- Heavily Compressed Attention (HCA)
- Manifold-Constrained Hyper-Connections (mHC)

### The KV-cache reduction headline

> "In the one-million-token context setting, DeepSeek-V4-Pro requires only **27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2**. That's a **90% reduction in KV Cache, way more impactful than Google's TurboQuant paper last month! NAND Flash investors, watch out."

**Which means (CRITICAL for [[SNDK]]):** SemiAnalysis explicitly flags KV cache reduction as a NAND demand headwind. The bull case for NAND has rested on "every AI inference call requires KV cache storage." If a 90% KV cache reduction generalizes, the marginal-token NAND demand could collapse — at least at the architectural level. This is a counter-data-point to the SNDK bull case and warrants downgrading conviction or at least adding to the bear case.

### Performance

- V4-Pro competitive on most agentic benchmarks but **Opus 4.7 still beats DeepSeek V4 Pro at Chinese writing** ("Claude mogs Chinese models in its own language")
- **Cheapest frontier alternative**, but capability still 1+ year behind closed frontier
- SemiAnalysis: "Workflows likely will not be cannibalized by DeepSeek"

**Which means:** the closed-source frontier still commands a premium, validating the [[2026-05-13-semianalysis-value-capture|model-labs value capture]] thesis even with capable open-source alternatives.

## The frontier monthly-release cadence

Visualized monthly model releases through 2026: a step-change increase since Jan 2026. **Which means:** the competitive pressure between OpenAI / Anthropic / Google / DeepSeek / Alibaba / xAI is forcing each lab to monetize faster — which feeds the compute demand spiral.

## Direct wiki implications

- **[[SNDK]]:** Add DeepSeek V4 KV cache reduction (90%) as a fundamental risk to the "AI data exhaust" NAND thesis. Conviction stays high in the near term (the HBF product is still real, datacenter rev $1.47B is real) but flag this as a 2027+ overhang.
- **[[NVDA]]:** Token-efficient frontier models = fewer FLOPs per task. But the rate of new tasks growing (multi-agent, Claude Code) more than offsets per-task efficiency gains. Net = more compute, not less. (Jevons.)
- **[[ai-capex-cycle]]:** Add the SemiAnalysis-internal $10.95M ARR data point as evidence of model-lab monetization velocity.
- **[[ai-bubble-debate]]:** The token-efficiency frontier means raw GPU-hour metrics overstate underlying capability cost — but ROI on AI tools is 5-10x, so demand stays inelastic at higher prices.

## Related

[[NVDA]] · [[SNDK]] · [[ai-capex-cycle]] · [[ai-bubble-debate]] · [[2026-04-01-semianalysis-gpu-rental-index]] · [[2026-05-13-semianalysis-value-capture]]
