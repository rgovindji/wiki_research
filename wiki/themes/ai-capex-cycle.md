---
type: theme
tags: [ai, capex, hyperscalers]
last_updated: 2026-05-09
last_full_review: 2026-05-09
sources: 1
---

# AI Capex Cycle

## What this is
The multi-year, hundreds-of-billions-of-dollars buildout of AI compute infrastructure (chips, servers, data centers, power) by hyperscalers and sovereigns. The single most important driver of equity earnings in 2026 — and the single biggest risk if it disappoints.

## Why it matters now

- AI investment is driving **~40% of S&P 500 earnings growth** in 2026 (Inc. / FactSet).
- **Cloud computing companies plan to spend ~$670B on AI infra in 2026** (incl. all hyperscalers).
- **MSFT + AMZN + GOOGL + META** alone: **~$600B in 2026** capex (per [[2026-05-09-dwarkesh-dylan-semianalysis]] — close to wiki's prior $200B figure once you include all data center capex, not just AI infra)
- **Whole supply chain capex (incl. fab construction, turbine deposits, etc.): ~$1T (NEW).** Big 4 hyperscaler capex is roughly 60% of total supply-chain capex; the rest is at [[TSM|TSMC]], ASML, memory makers, power vendors, OEMs.
- **2026 incremental US data center capacity: ~20 GW critical IT** (per Dylan)
- **OpenAI + Anthropic each at ~2-2.5 GW now** → targeting **5-6 GW by EOY 2026**, **~10 GW by EOY 2027**
- **Bloomberg Intelligence:** AI server spend **+45% YoY to $312B** in 2026.
- **JPM Global Research:** AI supercycle driving above-trend EPS growth of **13–15% for at least two years**.
- **Cumulative trajectory:** AI capex projected at **$1.6 trillion through 2029** (Vanguard).
- **Demand is under-estimated across the supply chain (NEW).** Per Dylan: "OpenAI and Anthropic know they need X. Nvidia is not quite as AGI-pilled — they're building X-1. You go down the supply chain, everyone's doing X-1. In some cases X÷2." This is a structural mispricing of demand by the supply chain, which has supported the bull case repeatedly through 2024-2026.

## Key drivers
- **Hyperscaler competition** — none of MSFT/AMZN/GOOGL/META can afford to under-invest if a competitor's models pull ahead
- **Sovereign AI** — country-level AI factory build-outs (UAE, Saudi, EU, India) are a second buyer beyond the US hyperscalers
- **Frontier model training costs** — each GPT/Gemini/Claude generation costs more compute than the last
- **Inference scaling** — as AI products get user adoption, inference becomes a larger share of compute spend
- **Power constraints** — increasingly the binding constraint, not chips → utilities, nuclear, gas turbines as second-order plays

## Beneficiaries (the picks-and-shovels)

### Tier 1 (direct chip / fab exposure)
- [[NVDA]] — GPU dominance; **$1T confirmed AI chip demand through 2027**; Blackwell sold out mid-2026
- [[TSM]] — sole foundry for advanced AI chips; 2026 capex $52–56B; rev growth ~30%
- [[ASML]] — EUV monopoly; no advanced AI chip is made without their machines

### Tier 2 (hyperscalers — buyers but also monetizers)
- [[MSFT]] — Azure + Copilot
- [[AMZN]] — AWS + Trainium custom silicon
- [[GOOGL]] — GCP + TPU custom silicon (NVDA alternative)
- [[META]] — internal AI infra ("personal superintelligence")

### Tier 3 (custom silicon, networking, memory) — *not yet covered*
- AVGO (Broadcom) — XPU custom silicon for hyperscalers
- AMD — MI series GPUs
- Memory: Micron, SK Hynix (HBM)

### Tier 4 (power & data center infra)
- Power infrastructure: [[VRT]] (power+cooling), [[ETN]] (Beam Rubin DSX), [[GEV]] (gas turbines), [[BE]] (fuel cells)
- Power electronics: [[STM]], [[ADI]], [[MPWR]], [[NVTS]], [[ON]] (800V DC architecture)
- **Construction labor** (see [[datacenter-construction]]): [[FIX]] (mech/HVAC), [[EME]] (MEP), [[PWR]] (transmission/grid) — ~$76B contracted backlog across three names
- Still not yet covered: nuclear utilities (CEG/VST/TLN), industrial gases (APD/LIN), data center REITs (DLR/EQIX)

## The bull thesis (capex pays back)
- AI delivers real, measurable productivity gains in software, customer service, R&D
- Hyperscalers' AI revenue grows fast enough to justify capex within 3-5 years
- Compute supply remains tight → pricing power for chips, fabs, and AI services
- This is more like the rollout of cloud (10-year payoff) than the rollout of fiber telecoms in 1999

## The bear thesis (capex hangover) — see [[ai-bubble-debate]]
- **Demand uncertainty** — current AI demand curves are extrapolations; if enterprise adoption stalls, ROI lags
- **Hardware obsolescence** — Blackwell → Vera Rubin → next gen; every cycle accelerates write-offs
- **Datacenter overbuild** — fixed-cost assets that depreciate fast if utilization falls short
- **Returns dispersion** — even if AI is real, the LLM layer may commoditize while hardware (NVDA/TSM) and applications (TBD) capture the value
- Vanguard's framing: "**Economic upside, stock market downside**" — AI may be net-positive for GDP and net-negative for the stocks priced for monopolistic outcomes

## Tactical signals to watch
- **Hyperscaler quarterly capex guides** — any cut signals capex peak
- **NVDA gross margins** — if Blackwell margins compress, the cycle is maturing
- **TSMC monthly revenue** — leading indicator for advanced-chip demand
- **Hyperscaler AI-attached revenue** — Azure / GCP / AWS AI revenue mix disclosures
- **Power / data center commentary** — bottleneck has shifted to power

## Open questions
- What's the right way to size NVDA + GOOGL + MSFT + META exposure given they're correlated by the same capex cycle?
- When will the first hyperscaler **cut** AI capex guidance — and what triggers it?
- Does the sovereign AI demand keep the cycle going past hyperscaler peak?

## Related
[[NVDA]] · [[TSM]] · [[ASML]] · [[MU]] · [[MSFT]] · [[AMZN]] · [[GOOGL]] · [[META]] · [[semiconductors]] · [[cloud-hyperscalers]] · [[bottleneck-roadmap]] · [[datacenter-construction]] · [[ai-bubble-debate]] · [[market-concentration]] · [[overview]]

## Citations
- Inc. on AI capex driving SP500 EPS: https://www.inc.com/phil-rosen/stock-market-outlook-earnings-ai-capex-estimates/91341117
- JPM Global Research market outlook: https://www.jpmorgan.com/insights/global-research/outlook/market-outlook
- Vanguard 2026 outlook (AI exuberance): https://corporate.vanguard.com/content/dam/corp/research/pdf/isg_vemo_2026.pdf
- NVDA Q4 FY2026 results / Q1 guide: https://fortune.com/2026/02/25/nvidia-nvda-earnings-q4-results-jensen-huang/
- NVDA Q1 FY2026 financial release: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026
- Intellectia on $1T AI demand: https://intellectia.ai/blog/nvidia-stock-analysis-2026-ai-demand
- Morgan Stanley AI market trends: https://www.morganstanley.com/insights/articles/ai-market-trends-institute-2026
- Oliver Wyman on bubble burst: https://www.oliverwyman.com/our-expertise/insights/2026/jan/impact-ai-bubble-burst-on-global-financial-markets.html

## Sources
1. [[2026-05-09-dwarkesh-dylan-semianalysis]] — primary source for $1T full supply chain figure, gigawatt cadence, and X-1 demand-underestimation pattern
