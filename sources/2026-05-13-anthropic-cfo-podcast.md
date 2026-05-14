---
date: 2026-05-13
type: podcast
publisher: Invest Like the Best (Patrick O'Shaughnessy)
url: n/a (transcript provided by user)
raw_path: raw/podcasts/anthropic_cfo_podcast.txt
touches: [ai-capex-cycle, ai-bubble-debate, NVDA, GOOGL, AMZN, AVGO, MSFT, CRWV, NBIS, bottleneck-roadmap, overview, semiconductors]
---

# Anthropic CFO Krishna Rao on Invest Like the Best — Source Summary

## TL;DR

The single most-substantive insider data point on Anthropic the wiki has captured. CFO Krishna Rao directly confirms:

- **ARR: started 2026 at $9B → ended Q1 at >$30B run-rate** (~3.3x in a single quarter)
- **$75B raised in last 2 years; $50B more committed** from recent Amazon + Google deals = **~$125B+ total capital**
- **>$100B in committed compute spend** — 5 GW Google+Broadcom TPU deal starting 2027 + up to 5 GW Amazon Tranium deal
- **9 of Fortune 10 are customers**; **net dollar retention >500% annualized**
- **90+% of Anthropic's code is written by Claude Code** itself (recursive self-improvement at production scale)
- Multi-platform compute strategy: NVDA GPU + AWS Tranium + Google TPU used **fungibly** — Anthropic claims to be "the only language lab using all three chip platforms"
- Mythos = newest, most-powerful model tier (above Opus 4.7); cyber-capable; **phased release** due to misuse risk
- Pricing strategy: brought Opus 4.5 price DOWN, saw **Jevons-paradox-style consumption explosion**

## Why this matters strategically

This is the strongest single bull data point the wiki has captured for the AI thesis. **It validates simultaneously:**

1. **Hyperscaler capex is earning its cost of capital** — Anthropic's ARR explosion proves demand at scale (per [[ai-bubble-debate]])
2. **Memory + accelerator buildout is structurally supported** — Anthropic alone is committing >$100B in compute over the next ~3 years
3. **TPU + Tranium are credible NVDA alternatives in the lab tier** — not just hyperscalers using them, but the labs themselves designing around fungibility
4. **NVDA share-of-wallet at top labs is meaningful but NOT 100%** — Anthropic deliberately diversified, started TPU at v3
5. **Coding is the leading edge of AI productivity** — internal data: 90+% of Anthropic's code written by Claude Code

## Key facts (verbatim from podcast)

### Revenue trajectory

- **First $ of revenue: March 2024** (just 2+ years of revenue history)
- **First frontier model: also March 2024**
- Series D: closed during FTX liquidation (raw fundraising environment)
- Series E: closed end of 2024 at ~$1B run rate; first close coincided with DeepSeek news
- **Start of 2026: ~$9B ARR**
- **End of Q1 2026: >$30B ARR** (~3.3x in a quarter)

### Capital raised

- **~$75B raised in 2 years** (since CFO joined)
- **~$50B more committed** from May 2026 Amazon + Google deals
- **Total: ~$125B+ capital raised/committed**
- CFO: "the reason we raise this capital is more because of the cone of uncertainty than to fund actual losses in the business today"

### Compute deals (May 2026)

| Deal | Counterparty | Scale | Start |
|---|---|---|---|
| TPU | **Google + Broadcom** | **5 GW** | 2027 |
| Tranium | **Amazon (AWS)** | **up to 5 GW** | ramp through 2026 |
| Memphis (Colossus facility, near-term) | xAI/SpaceX-related | smaller scale | already landing |
| **Total committed compute** | — | **>$100B** | layered through 2027+ |

### Compute platform strategy

- **Three chip platforms used fungibly:** AWS Tranium, Google TPU, NVIDIA GPU
- **Multi-generation:** TPU v5e/v6/v7, Tranium 2/3
- Started TPU at v3 (was early adopter)
- **"Built our own compilers"** — chip-level optimization
- **Anthropic claims:** "most efficient users of compute amongst any frontier labs"
- "We are the only language lab using all three of these chip platforms" + "only model on all three clouds"

### Customer base

- **9 of Fortune 10 are customers**
- **Net Dollar Retention >500% annualized**
- CFO anecdote: "I signed two double digit million-dollar commits in a 20-minute Uber ride"
- Verticals launched: **Claude for financial services, life sciences, security**
- Strategy: "mostly horizontal" platform with select verticals where Anthropic adds value
- Customer concentration unclear (CFO emphasized breadth)

### Product cadence

- **30 product/feature releases in January 2026 alone**
- Models: Haiku, Sonnet, Opus (4.5 → 4.6 → 4.7), **Mythos** (newest tier)
- **Mythos**: most capable model; cyber-spike found 250 security vulnerabilities in an open-source codebase (vs prior model's 22); **phased release** due to misuse potential — first model with explicit safety-driven release approach
- Cloud Code (developer tool) → **Co-Work** (knowledge-work extension)
- 70+ Claude skills repository for finance

### Pricing dynamics (KEY for [[ai-capex-cycle]])

- Pricing largely stable across Haiku / Sonnet / Opus
- **Brought Opus 4.5 price DOWN** → Jevons-paradox-style consumption explosion (usage went up way more than expected)
- **Mythos pricing "quite high"** (premium tier)
- "Pricing stability is important" — CFO wants to proliferate intelligence, not maximize per-token rates
- CFO: "we feel really good about where we are from the return on compute perspective"

### Recursive self-improvement

- **"90+% of Anthropic's code is written by Claude Code"**
- "A lot of Cloud Code is written by Cloud Code"
- This is why Anthropic allocates compute to internal use even at opportunity cost of foregone revenue
- "We could serve billions of dollars of revenue with the compute we allocate to employees internally, but we want to take a long-term view"
- Translation: **internal compute → faster model R&D → faster customer-revenue compounding**

### Pricing power proof

- $9B → $30B ARR in one quarter cannot have happened from compute additions in that quarter
- "Compute comes based on a ramp determined 12 months ago"
- Implication: **revenue is growing faster than compute is being added** = pricing leverage / efficiency gains, not just volume

### Talent / culture

- **7 co-founders, all still at company**
- "Vast majority of first 20-30 employees still at company"
- Meta poaching attempt: "we lost 2 people, other labs lost dozens"
- Culture interview gate is real — "wouldn't hire someone failing it even if smartest person we've met"
- "Talent density beats talent mass"

### Government / regulatory

- **Department of War interaction confirmed** (significant — direct US government defense engagement)
- Government floating pre-release model approval framework (CFO acknowledged "couple days ago")
- **"America first" approach** explicitly articulated
- Mythos release coordinated with administration

### What could derail (CFO-articulated risks)

1. **Diffusion rate within enterprise customers slowing** — "humans in big orgs slow to change"
2. **Scaling laws breaking down** (not seeing it, but not 100% certain)
3. **Anthropic falling off the frontier** (competitive risk)

## Key claims and confidence

- **Claim:** ARR $9B → $30B+ in one quarter. → **High confidence (CFO direct on-record).**
- **Claim:** Combined compute commitment >$100B. → **High confidence (CFO direct).**
- **Claim:** 9 of Fortune 10 customers + 500% NDR. → **High confidence.**
- **Claim:** Multi-platform fungibility is competitive moat. → **Medium-high.** Plausible but hard to verify externally.
- **Claim:** Scaling laws "alive and well". → **Medium confidence.** CFO's claim is consistent with public model performance trajectory.
- **Claim:** Mythos cyber capability validates phased release. → **Medium confidence.** 250-vs-22 vulnerability example is suggestive; broader pattern unclear.

## Implications for wiki

### [[ai-bubble-debate]] — STRONG BULL POINT

The existing "Anthropic margins say earnings are real" section gets a major upgrade. New data:
- $9B → $30B ARR explosion confirmed at the CFO level (not just SemiAnalysis estimate)
- 9 of Fortune 10 + 500% NDR validates demand durability at the enterprise level
- $100B+ compute commitment proves Anthropic believes demand sustains years out
- This is the single sharpest answer to the "AI capex doesn't earn its cost of capital" bear case the wiki has captured

### [[ai-capex-cycle]] — second-wave buyer commitment

Anthropic alone committing >$100B in compute. **This is a SECOND wave of buyer demand beyond the $725B Big-4 hyperscaler capex** — labs are independently locking in compute, not just hyperscalers serving them. Extends the cycle.

### [[NVDA]] — share-of-wallet nuance

Anthropic uses NVDA but ALSO Tranium and TPU fungibly. "Started TPU at v3 (was early adopter)" implies share-of-wallet at top labs is not 100% NVDA. **Sharpens the bear case data point on custom silicon competitive risk.** That said, NVDA is still in the ecosystem ("our partners in Amazon, Google, Microsoft, but also with Broadcom and Nvidia").

### [[GOOGL]] — TPU validation

**5 GW TPU deal from Google + Broadcom starting 2027** is enormous validation of TPU TAM. Anthropic — the frontier lab Google does NOT own — is choosing TPU at scale. This is the strongest external validation of TPU competitiveness vs NVDA the wiki has captured.

### [[AMZN]] — Tranium validation

**5 GW Tranium deal** is the strongest external validation of AWS custom-silicon strategy. Counter-balances the [[2026-05-12-stratechery-amazon-durability]] bear case framing — at least at the silicon layer, Tranium is winning real workloads.

### [[AVGO]] — Broadcom partnership confirmation

Broadcom + Google in the TPU deal reinforces [[AVGO]]'s custom-silicon thesis. Anthropic = additional named customer for the Broadcom-co-designed TPU pipeline.

### [[CRWV]] / [[NBIS]] — Anthropic uses Neoclouds too

Memphis Colossus partnership (xAI-related infrastructure) for near-term compute proves Anthropic supplements hyperscaler offtake with Neocloud/specialty providers. Adjacent to but not directly substitutable for the [[NBIS]] Anthropic deal already in the wiki.

### [[bottleneck-roadmap]] — 2027 ramp confirmed

Anthropic's 5 GW TPU + 5 GW Tranium deals "starting 2027" reinforce the [[bottleneck-roadmap]] timing of memory→cleanroom→EUV. Hyperscalers AND labs are independently locking 2027 capacity.

## Quotes worth keeping

> "If you buy too much compute, you go out of business. If you buy too little compute, you can't serve your customers and you're not at the frontier — same thing." — Krishna Rao on compute decisions

> "We started the year with about $9 billion of run rate revenue and we ended the quarter with north of $30 billion of run rate revenue." — Rao on Q1 2026

> "90 plus percent of our code is actually written by Claude Code right now within the company. A lot of Cloud Code is written by Cloud Code." — Rao on recursive self-improvement

> "Our net dollar retention rate is over 500% on an annualized basis." — Rao on customer expansion

> "On the way here I was in an Uber and I signed two double digit million-dollar commits in the car ride which was like 20 minutes." — Rao on enterprise demand velocity

> "The reason we raise this capital is more because of the cone of uncertainty than to fund actual losses in the business today." — Rao on the $125B+ capital raised

> "We're the only model that's on all three clouds today. We're the only language lab using all three of these chip platforms." — Rao on multi-vendor strategy

> "Each model generation gives you the chance to do more with it, to do it better, to do it more efficiently because we think the returns to frontier intelligence are extremely high. And it's extremely high especially in enterprise." — Rao on the frontier-intelligence thesis

## Open follow-ups

- Mythos pricing details (deferred from API price index in [[2026-04-24-semianalysis-coding-assistant]])
- Anthropic vertical product traction (Cloud for financial services / life sciences / security)
- Department of War contract scale + scope
- Government model-pre-release framework — implications for [[NVDA]] / Anthropic / OpenAI
- Implications for [[MSFT]] OpenAI exclusivity — Anthropic's deals with both AWS and Google break the "lab-tied-to-one-cloud" pattern

## Related

[[ai-capex-cycle]] · [[ai-bubble-debate]] · [[NVDA]] · [[GOOGL]] · [[AMZN]] · [[AVGO]] · [[CRWV]] · [[NBIS]] · [[bottleneck-roadmap]] · [[2026-05-13-NBIS-Q1-2026-earnings]] · [[2026-05-07-CRWV-Q1-2026-earnings]] · [[2026-05-13-semianalysis-value-capture]]
