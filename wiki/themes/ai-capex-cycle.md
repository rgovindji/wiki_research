---
type: theme
tags: [ai, capex, hyperscalers]
last_updated: 2026-05-12
last_full_review: 2026-05-09
sources: 4
---

# AI Capex Cycle

## What this is
The multi-year, hundreds-of-billions-of-dollars buildout of AI compute infrastructure (chips, servers, data centers, power) by hyperscalers and sovereigns. The single most important driver of equity earnings in 2026 — and the single biggest risk if it disappoints.

## Why it matters now

- AI investment is driving **~40% of S&P 500 earnings growth** in 2026 (Inc. / FactSet).
- **Big 4 hyperscaler 2026 capex = $725B (REVISED UP, May 2026; see [[2026-05-12-hyperscaler-capex-q1-revisions]])** — up **+77% YoY from $410B in 2025**. Breakdown: [[MSFT]] $190B (vs $152B consensus; CFO Hood explicitly attributes **$25B to rising memory chip costs**), [[GOOGL]] $190B (raised $5B; **cloud contract backlog doubled to $460B in one quarter**), [[AMZN]] $200B (held flat — only one not raising), [[META]] $125-145B (raised on "component pricing"). Including secondary hyperscalers (Oracle, ByteDance, Alibaba), **total ~$830B**.

> **What this means:** Microsoft, Google, Amazon, and Meta together are spending three-quarters of a *trillion* dollars in 2026 on AI infrastructure — nearly double what they spent in 2025. Microsoft alone is paying $25 billion *more* than it expected, just because memory chip prices have gotten so much more expensive. Google has already pre-sold $460 billion of cloud capacity. The takeaway: the companies actually writing the checks have not slowed down — they've accelerated.
- **MSFT + AMZN + GOOGL + META** alone: **$725B in 2026** capex (revised May 2026 from prior $600B estimate)
- **Whole supply chain capex (incl. fab construction, turbine deposits, etc.): ~$1T (NEW).** Big 4 hyperscaler capex is roughly 60% of total supply-chain capex; the rest is at [[TSM|TSMC]], ASML, memory makers, power vendors, OEMs.
- **2026 incremental US data center capacity: ~20 GW critical IT** (per Dylan)
- **OpenAI + Anthropic each at ~2-2.5 GW now** → targeting **5-6 GW by EOY 2026**, **~10 GW by EOY 2027**
- **Bloomberg Intelligence:** AI server spend **+45% YoY to $312B** in 2026.
- **JPM Global Research:** AI supercycle driving above-trend EPS growth of **13–15% for at least two years**.
- **Cumulative trajectory:** AI capex projected at **$1.6 trillion through 2029** (Vanguard).
- **Demand is under-estimated across the supply chain (NEW).** Per Dylan: "OpenAI and Anthropic know they need X. Nvidia is not quite as AGI-pilled — they're building X-1. You go down the supply chain, everyone's doing X-1. In some cases X÷2." This is a structural mispricing of demand by the supply chain, which has supported the bull case repeatedly through 2024-2026.
- **GPU rental capacity sold out (NEW — Apr 2026; see [[2026-04-01-semianalysis-gpu-rental-index]]).** SemiAnalysis launched a public H100 1-yr rental price index: **+40% in 5 months** ($1.70 → $2.35/hr from Oct 2025 to Mar 2026), still rising 15-20% MoM. **All Neocloud + Hyperscaler capacity coming online until August-September 2026 has already been booked.** Customers paying $14/hr/GPU for AWS p6-b200 spot. **Which means:** demand has been inelastic enough at current price points that rental rates can rise materially without curtailing demand — the ROI on AI tools is in the 5-10x range so token-buyers absorb price increases. This is the cleanest single data point refuting the "capex demand was over-extrapolated" bear case.
- **Anthropic ARR triple-step (NEW — Apr 2026).** $9B end-of-quarter → $30B+ current → SemiAnalysis's value-capture model has $44B+. **Which means:** model-lab monetization is scaling faster than infrastructure deployment. SemiAnalysis's own internal Claude Code burn rate hit **$10.95M ARR** before Opus 4.7's token-efficiency reset it. The token-consumption curve is accelerating.
- **Memory pricing parabolic (NEW — Jan 2026).** LPDDR5 contract prices +4x YoY, DDR5 +5x YoY (per SemiAnalysis Memory Model). **Which means:** AI server BoMs repriced 8-14% above September baselines, project IRRs compressed, some operators slow-rolled deployments — supply withheld → rental tightness compounds. Self-reinforcing dynamic.
- **GPU clusters = 80%+ of foundation-model startup funding (NEW; see [[2026-04-20-semianalysis-gpu-cluster-cost]]).** SemiAnalysis: "We know multiple companies spending over 80% of their initial funding on GPUs." **Which means:** the entire AI-native venture financing structure now revolves around GPU access, which directly underwrites [[NVDA]] / [[CRWV]] / [[NBIS]] revenue durability through 2027.
- **Bull-case caveat — token economics not uniform across knowledge work (NEW 2026-05-15 per Kedrosky/Plain English):** Claude Code's token consumption explosion ($30B Anthropic ARR run-rate) is concentrated among software engineers, whose work is **deterministic + expansive** (right/wrong answers + generates non-linear additional code via tests, build routines). White-collar work is largely **non-deterministic + compressive** (subjective + reduces large docs to bullets). **The wiki's implicit assumption that 100M knowledge workers will consume tokens like coders is unverified** and probably wrong on a per-worker basis. Jevons-paradox counter-argument (compute gets cheaper → use more) is speculative. Real impact: token volume growth may be more concentrated in coding + agentic technical workflows than the broad "AI for all knowledge workers" frame suggests. Does NOT invalidate the bull thesis — but right-sizes the addressable token pool.
- **Productivity math caveat (NEW 2026-05-15 per Kedrosky):** Q3 2026 US productivity +2.2% headline is not evidence of "AI is working" at the macro level. GDP = C+G+I+(X-M); I (investment) is parabolic from AI capex; hours worked are flat → productivity rises mechanically. Real AI-driven productivity will eventually show up in *labor output per hour* growth as agents deploy, but the current print is capex arithmetic, not validated output. Don't cite as bull evidence.
- **Supply-side validation — May 13-14 prints (NEW 2026-05-14 PM2):** Two AI capex supply-side prints confirmed the curve is *accelerating*, not plateauing:
  - **[[AMAT]] (May 14):** raised CY26 semi equipment growth guide from ">20%" to **">30%"** — first explicit annual-outlook upgrade this cycle. CEO: AI demand "now in full force." Direct supply-side validation of $725B+ hyperscaler capex commitments.
  - **Cisco Q3 FY26 (May 13):** **AI infrastructure orders guidance raised from $5B to $9B** for FY26 (80% increase). Data center switching orders +40% YoY. Networking growth accelerated to +25% YoY. Stock +20% on print; 6 firms raised PTs.
  - **Which means:** when both WFE and networking vendors **upgrade their own outlooks mid-year** while NVDA holds $1T+ confirmed demand through 2027 and Anthropic/CRWV/NBIS print profitability inflections — the bear case ("capex is over-extrapolated") gets harder to sustain. The supply chain isn't lagging behind demand anymore; it's pulling forward.

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

### Second-wave buyer commitment — Anthropic alone at $100B+ (NEW 2026-05-13)

From the Anthropic CFO Krishna Rao podcast (see [[2026-05-13-anthropic-cfo-podcast]]):

- **5 GW Google + Broadcom TPU deal starting 2027**
- **Up to 5 GW Amazon Tranium deal**
- **>$100B total compute commitment** (in addition to existing infrastructure)
- ARR $9B → >$30B in Q1 2026

**Which means:** The $725B Big-4 hyperscaler 2026 capex figure is only one layer of the demand stack. **Labs are independently locking in compute** — Anthropic alone committing $100B+ over the next 2-3 years means the hyperscalers' own capex is at least partly underwritten by labs paying them. The "demand is over-extrapolated" bear case requires both layers to break simultaneously. Both happening simultaneously is less likely than either one independently.

### Neocloud cohort breakout — Q1 2026 prints (NEW 2026-05-13)

The Neocloud category ([[CRWV]] + [[NBIS]]) decisively broke out from "speculative AI infrastructure" to "hyperscaler-quality scaled infrastructure" in Q1 2026:

| | CRWV Q1 2026 | NBIS Q1 2026 |
|---|---|---|
| Revenue | $2.078B (+112% YoY) | $399M (+684% YoY) |
| Adj EBITDA | $1.157B (56% margin) | $129.5M (profitability inflection from -$53.7M Y/Y) |
| Operating Cash Flow | $2.984B | $2.258B |
| Backlog / Contracted | **$99.4B** | $44.4B (MSFT $17.4B + Meta $27B) |
| New Customer Win | Anthropic multi-year Claude | — |
| Combined backlog | **$143.8B** across the two | |

**Which means:** The two largest public Neoclouds collectively have **~$144B of contracted AI infrastructure revenue** — that's the size of an entire mid-tier S&P 500 sector. The "is Neocloud a real category?" debate from 2024-2025 is over. The remaining debates are (a) financial leverage in rising-rate regime, (b) customer concentration sustainability, (c) capex pacing.

### Adjacent cycle: Robotics & humanoid buildout (NEW 2026-05-13; see [[robotics]])

The same [[bottleneck-roadmap]] framework applied to humanoid robotics yields its own parallel beneficiary stack. **Which means:** investors playing the AI capex cycle should view robotics not as a separate sector but as the *second leg* of the same multi-year compute-and-physical-AI buildout — supply chains are being negotiated now for a 2027-2030 buildout.

- **Rare-earth processing (binding now):** [[MP]] (only fully integrated US NdFeB producer), USAR, UUUU
- **Precision sensors / motion (binds 2027):** [[OUST]] (lidar + stereo cameras), [[ALGM]] (magnetic position + current sensors), [[VPG]] (force-torque pure-play)
- **Edge AI inference SoCs (2027-28):** [[AMBA]], CEVA, LSCC
- **Scaled actuator + battery mfg (2028-2030):** Chinese supply chain dominant — Sanhua (002050.SZ), Leader Drive (688017.SS), Inovance — mostly inaccessible to Western retail without Stock Connect

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
