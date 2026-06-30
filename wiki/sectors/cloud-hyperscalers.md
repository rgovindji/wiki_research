---
type: sector
tags: [cloud, ai, hyperscalers, mag7]
last_updated: 2026-06-30
last_full_review: 2026-05-09
sources: 0
---

# Cloud Hyperscalers

## What this is
The four companies running the cloud platforms that train and serve AI models: **Microsoft Azure, Amazon AWS, Google GCP, and Meta** (an internal hyperscaler — its capex matches the others even if no external cloud product). They are simultaneously the **biggest customers of the chip industry** and the **monetizers of AI services** to enterprises and consumers.

## Why the four matter together
- Combined 2026 AI infrastructure capex: **>$200B** (a meaningful chunk of total ~$670B cloud capex)
- They drive the demand side of [[ai-capex-cycle]]
- They are also four of the seven names that make up [[market-concentration]]
- Their quarterly capex guides are the **single most important leading indicator** for the AI cycle

## Players

| Company | Cloud product | Custom silicon (designed with) | AI revenue narrative |
|---|---|---|---|
| [[MSFT]] | Azure | (Maia, early) | Copilot + Azure AI; tightly coupled with OpenAI |
| [[AMZN]] | AWS | Trainium / Inferentia ([[AVGO]]) | Bedrock; customer breadth advantage |
| [[GOOGL]] | GCP | TPU ([[AVGO]] — mature, multi-generation) | Gemini + GCP; has the only credible NVDA alternative at scale |
| [[META]] | (internal) | MTIA ([[AVGO]]) | Personal superintelligence; ad-funded internal AI infra |

**Common thread:** every hyperscaler's custom silicon program is co-developed with [[AVGO]]. This makes Broadcom the **systematic non-NVDA hedge** — when hyperscalers reduce dependence on Nvidia, Broadcom is the disproportionate beneficiary.

## Bull case
- **The "tollbooth" thesis — token optimization is a *gift* to the hyperscalers (NEW 2026-06-30, [[2026-06-30-uncoveralpha-token-optimization-hyperscalers]]; bias HIGH).** As enterprises stop "token maxing" (always-buy-the-best-model) and start routing the routine ~80% to cheap/open-weight models, per-token price falls but **total volume explodes and almost every token crosses a hyperscaler's managed-inference toll** (AWS ~35-38% op margin, GCP >33%). The compression hits the *model* layer, not the *infra* layer — Jevons pointed at the cloud P&L. The orchestration layer (Bedrock 110+ models + Intelligent Prompt Routing + AgentCore; Azure Foundry; Vertex) is the durable capture point. **Caveat:** load-bearing assumption is that the toll stays sticky; managed inference is itself getting competitive. See [[inference-economics]]. Cleanest read for [[AMZN]]/AWS (pure tollbooth).
- Hyperscalers are the **only buyers at scale** for AI compute → they capture supplier rents from any chip vendor that doesn't have a defensible monopoly
- Cloud + AI is an **operating-leverage business** — incremental AI revenue largely drops to the gross margin line once infra is built
- Multi-product moats: AI is a feature on top of existing cloud + productivity products with sticky enterprise contracts

## Bear case
- They are **funding their suppliers' (NVDA) windfall** — if AI revenue doesn't compound fast enough, they take the capex write-down
- **Internal silicon** is a partial hedge but takes years to displace NVDA at scale
- All four are exposed to the same demand-curve risk if enterprise AI adoption is slower than projected
- Multiple compression risk if capex peaks while AI revenue is still ramping

## Scoreboard items to track each quarter
- **Capex guide** — direction matters more than absolute level
- **AI revenue contribution** — when companies disclose it (Azure AI, GCP AI, Bedrock revenue)
- **Cloud growth rates** — Azure vs. AWS vs. GCP — relative share-shift signals
- **Free cash flow** — AI capex pressures near-term FCF; the question is when it normalizes

## Cross-comparison
- **Cheapest:** [[GOOGL]] (fwd P/E ~29.7) — and has the only credible NVDA alternative (TPU)
- **Most AI-tightly-bound:** [[MSFT]] — Copilot + OpenAI partnership is a single bet on AI productivity
- **Highest optionality:** [[META]] — ad business funds AI without external pressure; "personal superintelligence" is high-risk/high-reward
- **Most diversified non-AI base:** [[AMZN]] — retail margin recovery is independent of AI

## Open questions
- Which hyperscaler hits **AI revenue / AI capex parity** first? That's the moment the market re-rates the leader vs. laggards.
- If one cuts capex in 2026, do the others follow (signaling cycle peak) or hold (signaling competitive escalation)?
- How much of the AI capex is **truly required** vs. competitive insurance?

## Related
[[ai-capex-cycle]] · [[MSFT]] · [[AMZN]] · [[GOOGL]] · [[META]] · [[market-concentration]] · [[overview]]

## Citations
- JPM Global Research: https://www.jpmorgan.com/insights/global-research/outlook/market-outlook
- Inc. on AI capex: https://www.inc.com/phil-rosen/stock-market-outlook-earnings-ai-capex-estimates/91341117
- Morgan Stanley AI market trends: https://www.morganstanley.com/insights/articles/ai-market-trends-institute-2026
- CNBC on AI market splintering: https://www.cnbc.com/2025/12/25/how-the-ai-market-could-splinter-in-2026-.html
