---
type: theme
tags: [ai, capex, hyperscalers]
last_updated: 2026-05-27
last_full_review: 2026-05-09
sources: 11
---

# AI Capex Cycle

## What this is
The multi-year, hundreds-of-billions-of-dollars buildout of AI compute infrastructure (chips, servers, data centers, power) by hyperscalers and sovereigns. The single most important driver of equity earnings in 2026 — and the single biggest risk if it disappoints.

## Why it matters now

- **🔥 2026-05-26-27 — Anthropic closes $30B at $900B+ valuation, surpasses OpenAI ($852B).** 2.4x rerating in 90 days (Feb 2026 $380B → May 2026 $900B+). Sequoia + Dragoneer + Altimeter + Greenoaks co-lead, each ~$2B. **Which means** the model-lab demand-pull at the top of the capex cycle now embeds ~$1.75T+ combined Anthropic+OpenAI private value backing forward compute purchases. Per Gavin Baker May 21: Anthropic added $11B ARR in March alone. Sustained 100%+ growth required to defend valuation = sustained capex demand pull through 2027. Per [[2026-05-27-anthropic-900B-surpasses-openai]]. **Hyperscaler revenue concentration risk strengthens** (Damodaran: MSFT 50%, ORCL 50%+, GOOGL 43%, AMZN 51% of cloud-AI revenue is at OpenAI+Anthropic).
- **🔥 2026-05-26 — Hyperscaler forward-funded capacity signal.** MSFT, GOOGL, AMZN reportedly proposing to fund SK Hynix capacity expansion in exchange for guaranteed HBM allocation through late 2020s. UBS reframes MU to $1,625 PT (3x), valuing memory as AI infrastructure not cyclical commodity. **Which means** capex regime is shifting from spot-pricing to contracted-pricing for the supply chain — bottleneck rents are now being prepaid. Per [[2026-05-26-micron-1T-ubs-1625-pt]].
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
- **Effective-FLOPs lever is independent of process shrinks (NEW 2026-05-16 per [[2026-05-16-horace-he-ml-systems]]):** Bit-precision trajectory: **V100 = FP16 → A100 = FP8 → B100 = FP4**. Every precision halving roughly doubles effective throughput per transistor *without* requiring a new fab node. **Which means:** Even if EUV / 2nm timelines slip (see [[bottleneck-roadmap]]), the compute-per-dollar curve keeps falling via precision drops. This is a separate axis of supply growth that bear cases tend to underweight — a node-stall does not stall effective-compute growth.
- **131K-GPU fault-tolerance ceiling (NEW 2026-05-16):** Llama 3 paper data — at 16K GPUs, mean time between failures ≈ 1.8 hrs; at **131K GPUs, ≈ 15 minutes**. **Which means:** the engineering complexity of frontier training scales worse than linearly with cluster size — only hyperscalers + a small set of neoclouds (CRWV/NBIS) have the systems-engineering depth to actually USE the GPUs they buy. Reinforces the **monopsony** framing on the buyer side. Tier-2 buyers rent hyperscaler-grade engineering rather than replicating it.
- **Robot-economy timeline overlay (NEW 2026-05-16 per [[2026-05-16-sergey-levine-physical-intelligence]]):** Sergey Levine median estimate: fully autonomous home robot in ~5 years; "GPT-5 equivalent for robotics" 2028-2030; flywheel deployment start 1-2 years. Robot arm cost: **$400K (2014) → $3K (today) → "small fraction of $3K" forward**. **Which means:** the 2028-2030 datacenter buildout (100-300 GW by 2030) may have a *demand-side* labor reinforcement — at $1-3K/arm, robots could meaningfully assist switchgear / solar / cabling work at the very moment the buildout hits peak labor demand. Not yet investable, but worth tracking — see [[datacenter-construction]] + [[robotics]].
- **Sovereign-AI gets a new technical mechanism: federated training (NEW 2026-05-16 per [[2026-05-16-yann-lecun-ame-labs]]).** Yann LeCun's separate "Tapestry" project (with the venture/research entity behind it) proposes a federated training scheme where contributors share *parameter vectors* across data centers rather than raw data — converging toward a "consensus" open foundation model that each country/region can then fine-tune for local language, culture, values. **Which means:** the sovereign-AI demand layer (UAE, Saudi, India, EU, France, Japan, Korea) now has a viable technical pattern that doesn't require data sharing — making local compute capex *additive* rather than redundant. Modest reinforcement of the second-buyer-base thesis underpinning [[NVDA]] / [[CRWV]] / [[NBIS]] long-horizon demand. Tapestry itself is conceptual today — too early to invest around — but watch for any 2027-28 announcements from non-US/non-China governments adopting federated open-foundation-model strategies.
- **Industrial process control = new adjacent TAM (NEW 2026-05-16 per [[2026-05-16-yann-lecun-ame-labs]]).** LeCun explicitly identifies B2B industrial applications as the near-term commercial target for world-model AI: *"a jet engine, a chemical plant, a power plant, some manufacturing line, a patient, a human cell — those are systems that are sufficiently complex that you can't model their behavior with a small number of equations."* AME Labs's stated customer base includes investors in healthcare, manufacturing, industrial process control. **Which means:** there's an under-mapped adjacent industrial-AI demand vector beyond hyperscaler / lab capex. Public-market companies that could benefit (not yet covered): Honeywell (HON), Emerson Electric (EMR), Rockwell Automation (ROK), ABB, Siemens, Schneider Electric. Already-covered exposure: [[GEV]] (gas turbines + grid). **Status: monitor; not a thesis yet.** Worth tracking if any of these names announces a world-model-AI partnership or platform play in 2027-2028.
- **Copper as the physical-layer commodity bottleneck (NEW 2026-05-16; full thesis at [[copper-thesis]]).** Per BNEF, AI data centers alone will consume 400-572kt/yr of copper through 2028, peaking at 1.1 Mt/yr by 2030 (Sprott — most aggressive estimate). Goldman: grid + power infrastructure drives **>60% of copper demand growth through 2030**, "adding another US" of demand. Supply side is broken: 15-20 yr mine permit cycles; $210B capex needed by 2035 vs only $76B invested over past 6 years. **Smart money converging**: Druckenmiller long copper futures ([[2026-05-16-druckenmiller-hard-lessons]]); Friedland "dawn of the copper age" $15K/tonne thesis; Larry Fink at BlackRock; Goldman Sachs confirms demand-outpaces-supply from 2029. **Which means:** the AI capex cycle has a *physical-layer commodity multiplier* that is being structurally under-supplied. Best exposure via CPER (copper futures ETF) for thesis purity; COPX for diversified miners; [[TECK]] / BHP / [[FCX]] for individual names.
- **Cost-curve quantification (NEW 2026-05-17 PM per SemiWiki forum "Is AI the automobile" thread)**: Xebec summarized AI cost trajectory: **energy per token improving >10x per year**; **hardware 20-50x per generation Hopper → Blackwell → Vera Rubin** (some scenarios 3-5x); **model cost per token ~10x per year for last 3 years and continuing** (DeepSeek-R1-style innovations); **capability-level-per-size improving** — **8B-27B models now outperforming 70B models from 1-2 years ago**. **Which means**: compute-per-dollar curve is falling faster than enterprise demand can absorb at any given price point — pricing is **bounded below by structural deflation** even as volume keeps growing. Reinforces [[GOOGL]] commoditization bull (Google has strongest incentive to BE the "budget AI" to retain Search); frontier labs face structural pricing compression on non-frontier tiers as fast-followers + Gemini commoditize. Industrial Revolution analogy (Xebec): required low-cost energy; Roman empire couldn't because slave labor was cheap → no incentive. **Modern parallel**: AI revolution requires falling token cost to be productive — and the curve is delivering.
- **Productivity-reset evidence (NEW 2026-05-17 per [[2026-05-16-dylan-patel-invest-like-best]]).** SemiAnalysis internal Claude Code spend: **$7M/yr vs $25M salary = 28% of payroll on AI**, trajected to exceed 100% of salary by year-end. Specific case studies: one person built energy data platform in 3 weeks (cost: $6K/day cloud) that competes with 100-person company that took a decade; SemiAnalysis economist built 2,000-task BLS rubric + benchmark with "phantom GDP" analysis solo. Dylan's framing: *"If you don't use more tokens, you'll never escape the permanent underclass."* **Which means:** the AI capex thesis is *more aggressive* than current $725B hyperscaler capex implies — enterprise token spend is materializing in real-time at the productivity-substitution layer, not just at the labs.
- **Anthropic ARR trajectory accelerating + lab compute-constrained (NEW 2026-05-17).** Per Dylan Patel: Anthropic ARR $9B → $30B → $40-45B "by airtime"; margins floor at 72% (vs ~30% start of 2026); **Anthropic now MORE compute-constrained than OpenAI**. Quote: *"Dario used to gloat about OpenAI being too aggressive on compute. Now Anthropic is like 'fuck, we wish we had more.'"* **Implication for capex cycle:** the labs cannot serve all available token demand — capacity, not demand, is the binding constraint at the top of the stack. This is *more bullish* for NVDA/CRWV/NBIS than a demand-constrained labs scenario would be.
- **Bull-case caveat — AI is still NET EXPENSE for non-chip Mag 7 (NEW 2026-05-16 per [[2026-05-16-damodaran-profg-markets]]).** Damodaran (NYU Stern): *"For the most of the other tech companies AI has been an expense rather than an income stream. So you take the rest of the Mac 7 — even if you just count the depreciation part of their capex, that by itself is putting downward pressure on earnings rather than upward pressure."* **Which means:** the wiki's bull case correctly attributes ~40% of S&P 500 EPS growth to AI — but this is concentrated at chip makers ([[NVDA]], [[AMD]], [[AVGO]], [[MU]], [[TSM]]). For [[MSFT]] / [[GOOGL]] / [[META]] / [[AMZN]], depreciation on AI capex is currently a *drag* on earnings, offset by cloud revenue growth + ad-business growth. Bull case on hyperscaler Mag 7 should be framed around *future* AI monetization (Anthropic/OpenAI revenue flowing back, cloud capacity sold to labs) rather than current earnings. Damodaran also notes: *"Without the AI spending we'd probably be looking at GDP growth in the negative"* — i.e., the AI capex cycle is itself the macro engine, which is its own bull-and-bear (bullish for capex-cycle continuation incentives; bearish for what happens to GDP if capex pauses).
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
2. [[2026-05-16-horace-he-ml-systems]] — FP4 precision lever; 131K-GPU fault-tolerance ceiling; hyperscaler engineering moat
3. [[2026-05-16-sergey-levine-physical-intelligence]] — robot-economy timeline overlay on 2028-2030 datacenter buildout
4. [[2026-05-16-yann-lecun-ame-labs]] — federated training mechanism for sovereign AI + industrial process control as adjacent TAM
5. [[2026-05-16-damodaran-profg-markets]] — AI as net expense for non-chip Mag 7; GDP-engine framing
6. [[2026-05-16-dylan-patel-invest-like-best]] — Anthropic ARR $40-45B; productivity reset evidence; compute-constrained labs (added 2026-05-17)
7. [[2026-05-16-john-arnold-invest-like-best]] — Energy as bottleneck for US innovation; permitting reform optimism (added 2026-05-17)
