---
type: theme
tags: [nvda, supply-chain, ai, ecosystem]
last_updated: 2026-05-09
last_full_review: 2026-05-09
sources: 1
---

# NVDA Supply Chain & Direct Investments

## What this is
A map of the public companies that **build for, ship to, or are funded by** [[NVDA]] — and a rough sense of where each one sits on conviction. NVIDIA's economic gravity has reshaped the entire semiconductor stack, the optical / networking layer, the server OEMs, and the data center power supply chain. Several of these names have been pulled into NVDA's orbit through direct equity stakes ($1B-$4B checks) since late 2025.

Treat this page as the index for second-order [[ai-capex-cycle]] plays. Drill into each ticker page for the bull/bear and what to watch.

> **Note on competitors:** [[AMD]] and [[AVGO]] also sit in this ecosystem as **alternatives** to NVDA (AMD via MI400/Helios; AVGO via custom XPU for 6 hyperscalers). They are NOT in NVDA's supply chain — they are part of the same AI capex theme but compete for the same hyperscaler wallet. See [[NVDA]] for the competitive dynamic and the AMD/AVGO pages for the standalone theses.

## The stack — by layer

### IP / CPU architecture
- [[ARM]] — every NVIDIA "Vera" CPU in the [[NVDA|Vera Rubin]] generation is built on **Arm v9.2-A** (88-core, custom "Olympus" design); royalty stream scales with Vera Rubin volumes ramping 2H 2026

### Foundry
- [[TSM]] — sole foundry for advanced AI chips; NVDA has **booked >50% of [[TSM|TSMC]]'s CoWoS capacity for 2026-27** and is set to capture **>70% of N3 wafer capacity by 2027** (per [[2026-05-09-dwarkesh-dylan-semianalysis]]). On A16 (N2 variant), the **first customer is AI, not [[AAPL]]**.

### Memory (HBM is the binding constraint)
- [[MU]] — preferred HBM supplier; HBM3E + HBM4 ramp; **HBM capacity sold out through 2026** across the industry
- [[SNDK]] — NAND flash for AI data; 528% YTD in 2026 on AI memory supercycle
- [[WDC]] — storage / HDDs; AI generates "data exhaust"; debt-free post-SanDisk spin

### Advanced packaging (CoWoS bottleneck)
- [[ASX]] — ASE Technology, market-leading OSAT; advanced packaging sales **doubling in 2026**
- [[AMKR]] — Amkor; **2026 capex $2.5-3B** (~3x prior); Peoria Arizona campus = US end-to-end advanced packaging
- [[CAMT]] — Camtek; inspection / AOI for advanced packaging; CoWoS adjacent

### Equipment (wafer fab)
- [[AMAT]] — Applied Materials; broadest WFE portfolio (deposition + etch + ion implant + CMP); **>50% of HBM equipment value**; **>20% growth guide for 2026**; 12-24 months forward visibility
- [[KLAC]] — [[KLAC|KLA]]; process control / metrology; **Jefferies $1,500 PT (Dec 2025)**; benefits from AI chip yield complexity
- [[LRCX]] — Lam Research; deposition / etch; Systems revenue est **$14.5B FY26 (+26%)**; HBM is wafer-intensive
- [[ASML]] — EUV monopoly. Per [[2026-05-09-dwarkesh-dylan-semianalysis]]: **THE 2028-2030 binding constraint** of all AI compute. ~70 tools/yr → ~100 by 2030; 3.5 tools = 1 GW of AI capacity. Critical sub-suppliers: **Cymer** (San Diego, EUV source — ASML-owned subsidiary) and **Carl Zeiss** (Europe, multi-layer mirror lens stack). Both are physically constrained, not commercially constrained.
- [[KEYS]] — Keysight; test & measurement (not WFE) — design verification adjacent
- [[TER]] — Teradyne; chip-final test (separate from WFE bucket); **Q1 2026 revenue +87% YoY; 70% AI exposure**

### Fab consumables & specialty materials (the "invisible" layer)
- [[ENTG]] — Entegris; FOUPs (wafer carriers), ultra-pure materials, gas/liquid filtration; content-per-wafer growth from AI complexity
- [[APD]] — Air Products; **build-own-operate industrial gas plants** at fabs (N2/O2/Ar/H2 + NF3 chamber clean + specialty gases); **Samsung Pyeongtaek** largest semi investment in APD history; new facilities onstream 2028-2030

### Networking & optical (the data center fabric)
- [[COHR]] — Coherent; **NVDA $2B direct investment** (March 2026, split with LITE); CPO partner
- [[GLW]] — Corning; **NVDA $3.2B direct investment** (May 2026); 3 new US optical fiber factories; near-monopoly in high-perf fiber
- [[FN]] — Fabrinet; contract manufacturer for transceivers/modules
- [[LITE]] — Lumentum; **NVDA $2B direct investment** (March 2026, with COHR); OCS backlog $400M+
- [[APH]] — Amphenol; connectors / cables / interconnect

### Server OEMs (the Blackwell / Rubin assemblers)
- [[DELL]] — PowerEdge XE9812 (Vera Rubin NVL72), GB300 desktop first-mover, full Blackwell portfolio
- [[HPE]] — Hewlett Packard Enterprise; Juniper-acquired networking + full Blackwell+Rubin AI Factory portfolio; sovereign AI focus
- [[SMCI]] — Super Micro; deep Blackwell support but lingering accounting / legal overhang
- [[JBL]] — Jabil; Intelligent Infrastructure +52% YoY; **AI-related rev $13.1B FY26 (+46%)**
- **Foxconn** *(no page yet)* — top-tier ODM assembler for hyperscaler-direct AI server programs; ships modular factory-integrated rack/skid units to data center sites
- **Victory Giant** *(no page yet)* — Chinese PCB supplier; one of the largest providers of PCBs to Nvidia per [[2026-05-09-dwarkesh-dylan-semianalysis]]

### Power systems (data center scale)
- [[FLEX]] — Flex Ltd; contract manufacturer for power infrastructure
- [[VRT]] — Vertiv; Q1 2026 rev **$2.65B (+30% YoY)**, **$9.5B backlog**; only large player covering power AND cooling
- [[ETN]] — Eaton; **Beam Rubin DSX with NVDA**; 800V DC architecture; Q4 2025 orders +200%
- [[GEV]] — GE Vernova; combined-cycle gas turbines; lead times beyond 2030 on specific blades
- [[BE]] — Bloom Energy; fuel cells; SemiAnalysis bullish 18+ months on production-ramp speed
- **Mitsubishi, Siemens Energy** *(no pages yet — international)* — other two of the three Western combined-cycle GT OEMs

### Power electronics (the chip-level power stack)
- [[STM]] — STMicroelectronics; part of NVDA 800V DC ecosystem
- [[ADI]] — Analog Devices; part of NVDA 800V DC ecosystem
- [[MPWR]] — Monolithic Power Systems; PMIC for AI servers
- [[NVTS]] — Navitas; GaN/SiC; **800V→50V DC-DC platform for AI servers**; Blackwell rack ramp drives content
- [[ON]] — onsemi; SiC; part of NVDA 800V DC ecosystem

### Direct equity investments (NVDA wrote a check)
- [[CRWV]] — CoreWeave (neocloud); NVDA **$250M IPO anchor**; Meta deal ~$35B total
- [[NBIS]] — Nebius (neocloud); NVDA **$2B investment**; Meta $27B contract
- [[NOK]] — Nokia; NVDA **$1B investment** (Oct 2025); AI-RAN, 6G; T-Mobile trials 2026
- [[SNPS]] — Synopsys; NVDA **$2B minority stake**; AI/GPU-accelerated EDA
- [[LITE]], [[GLW]], [[COHR]] — see networking layer above (also direct investments)
- [[ORCL]] — Oracle (not a direct equity investment, but a major OpenAI compute partner with multi-year deals; rides NVDA's offtake structure)

## Why this whole map matters for portfolio construction

1. **Beta to NVDA without owning NVDA.** Many of these names give targeted exposure to specific bottlenecks (HBM via [[MU]], CoWoS via [[AMKR]], optical via [[COHR]]/[[GLW]]) at lower starting valuations than NVDA itself.

2. **Bottleneck = pricing power.** HBM, CoWoS, EUV, advanced fiber — these are the **physically constrained** parts of the stack. Pricing power lives where capacity can't ramp fast enough.

3. **NVDA's direct investments are a signal.** When NVDA writes $1-4B checks, they are subsidizing capacity expansion in their own bottlenecks. That's both a tailwind for the recipient (capital + offtake) and a structural read on where NVDA sees risk.

4. **But concentration is duplicated.** Owning NVDA + MU + AMKR + COHR is **not five bets** — it's five expressions of the same AI capex thesis. See [[market-concentration]].

## Bull case (own the supply chain)
- Demand visibility better than NVDA's own (NVDA's customers commit ahead of fab capacity)
- Cheaper entry valuations than the Mag 7
- Direct beneficiaries of NVDA's $1T+ AI demand commitment

## Bear case (own less of the supply chain)
- Cyclicality magnified — when AI capex slows, the supply chain slows first and harder
- Customer concentration: many of these names have NVDA / hyperscalers as 50%+ of revenue
- Some of the YTD moves (NVTS +88%, SNDK +528%) leave little margin for execution misses
- See [[ai-bubble-debate]] — if AI capex pauses, this entire map re-rates simultaneously

## Watch items at the layer level
- **HBM:** quarterly capacity prints from MU / SK Hynix / Samsung
- **CoWoS:** TSMC + AMKR / ASX capex follow-through
- **Optical / CPO:** COHR / LITE book-to-bill; CPO production milestones
- **Power:** VRT / ETN order books; 800V DC adoption pace
- **Direct investments:** CRWV / NBIS utilization rates; SNPS NVDA-EDA product launches

## Related
[[NVDA]] · [[ai-capex-cycle]] · [[bottleneck-roadmap]] · [[semiconductors]] · [[cloud-hyperscalers]] · [[market-concentration]] · [[ai-bubble-debate]] · [[overview]]

## Citations (key sources powering this map)
- IntuitionLabs GB200 supply chain: https://intuitionlabs.ai/articles/nvidia-gb200-supply-chain
- 24/7 Wall St on NVDA empire: https://247wallst.com/investing/2026/02/25/nvidia-is-building-an-ai-infrastructure-empire/
- 24/7 Wall St on NVDA's March 2026 commitments: https://247wallst.com/investing/2026/04/01/nvidia-commits-billions-to-lumentum-synopsys-nokia-xai-openai-intel-in-march-alone/
- CNBC NVDA-Corning: https://www.cnbc.com/2026/05/06/nvidia-corning-optical-factories-nc-texas-ai.html
- CNBC NVDA-Coherent/Lumentum: https://www.cnbc.com/2026/03/02/nvidia-investment-coherent-lumentum.html
- 24/7 Wall St on Nebius/CoreWeave: https://247wallst.com/investing/2026/03/11/after-2-billion-nvidia-investment-nebius-group-just-became-the-real-neocloud-winner/
- Eaton-NVDA DSX: https://www.eaton.com/us/en-us/company/news-insights/news-releases/2026/eaton-collaborates-with-nvidia-to-unveil-its-beam-rubin-dsx-platform.html
- ARM Vera Rubin: https://newsroom.arm.com/blog/arm-rubin-converged-ai-datacenter
- TSMC CoWoS NVDA capacity: https://www.digitimes.com/news/a20251210PD218/tsmc-cowos-capacity-nvidia-equipment.html

## Sources
1. [[2026-05-09-dwarkesh-dylan-semianalysis]] — primary source for >70% N3 by 2027, Carl Zeiss / Cymer / Foxconn / Victory Giant linkages, A16-first-customer-is-AI dynamic
