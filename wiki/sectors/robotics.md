---
type: sector
tags: [robotics, humanoid, physical-ai, rare-earths, sensors, edge-ai]
last_updated: 2026-05-13
last_full_review: 2026-05-13
sources: 1
---

# Robotics & Humanoid Buildout

## What this is

The component supply chain enabling general-purpose humanoid robots and adjacent physical-AI form factors. Covers rare-earth permanent magnets, precision sensors (force-torque, position, vision/lidar), harmonic drives, edge AI inference SoCs, and the actuator/battery stack that determines unit economics.

## Why it matters now

Humanoid robotics in 2026 maps to AI infrastructure in mid-2023: the narrative is louder than the revenue, but supply chains are being negotiated **now** for a buildout that's plausibly contracted by 2027 and scaled by 2028–2030. Counterpoint Research counted ~16,000 humanoid units installed globally in 2025 with cumulative deployments expected to exceed 100,000 by 2027. The investable thesis between now and 2027 is positioning into bottleneck suppliers before the second-derivative revenue actually arrives.

The same [[bottleneck-roadmap]] frame the wiki applies to the AI capex cycle transfers cleanly: pricing power lives wherever the binding physical constraint is, and in robotics that constraint **starts with rare-earth processing (now), moves to precision sensors and harmonic drives (2027), and ends at scaled actuator and battery-density manufacturing (2028–2030).**

> **What this means:** Humanoid robots are 2-3 years from being a real industry — but the suppliers who will build them are being chosen *right now*. The same playbook that worked for AI chips (find the bottleneck supplier whose product no one else can make, buy them years before their revenue inflects) applies. The rare-earth magnet maker today is the equivalent of the GPU packager in 2023.

## Market sizing

Estimates vary by an order of magnitude across firms:

| Firm | 2030 forecast | CAGR | Methodology note |
| ABI Research | $6.5B | 138% | Hardware shipments; very small 2024 base |
| MarketsandMarkets | $15.26B | 39.2% | Includes hardware + software + services |
| Grand View | ~$4B | Conservative | Hardware only |
| Future Market Insights | $10B+ by 2027–28 | 37.0% (to 2035) | Crosses $10B threshold 2027–28 |
| Morgan Stanley | $5T by 2050 | n/a | Long-horizon framing; ~900M units |

Working assumption for the wiki: ~$2–3B TAM in 2025 (depending on scope), inflection 2027, $10B threshold late 2027 / early 2028, with the 2030 number sitting in a wide band of $6–15B depending on adoption pace. **Even the aggressive case has only ~115,000 units shipped in 2027 — the harvest is 2028–2030, not 2027.**

## Key drivers

- **NdFeB magnet demand.** Per-humanoid permanent-magnet content runs ~10× that of a passenger EV. No synthetic substitute at the torque density humanoids require. China controls ~90% of downstream rare-earth processing — single largest supply-chain risk in the sector.
- **OEM production commitments.** Tesla Optimus (factory conversion at Fremont), Figure 02 (deployed at BMW Spartanburg), Agility Digit (RoboFab in Salem OR with 10,000-unit annual capacity), plus Chinese OEMs led by AgiBot (~31% market share), Unitree (~27%), UBTECH (~5%). Western and Chinese OEMs run on overlapping component supply chains.
- **World-model AI maturation.** NVIDIA Cosmos, Google Gemini Robotics, and similar foundation models for embodied AI are closing the perception-to-action gap that previously required hand-crafted policies. This is the single largest unlock for general-purpose use cases.
- **Force-torque sensing precision.** Dexterous manipulation requires sub-Newton force-feedback precision, which is where [[VPG]] and competing precision-measurement vendors live.
- **Spatial awareness.** Lidar + stereo cameras + IMU sensor fusion for navigation and obstacle avoidance. [[OUST]] is the highest-quality Western pure-play.
- **Edge AI inference latency.** Control loops require sub-10ms inference at single-digit-watt power budgets — a different stack than autonomous-driving compute. Favors low-power FPGA + DSP/NPU IP licensing over bulk GPU.

## Beneficiaries

**Tier 1 — Real bottleneck (small/mid-cap, humanoid demand is material):**

- [[MP]] — only fully integrated US NdFeB producer. Stillwater commercial ramp H1 2026.
- [[USAR]] — Round Top Texas deposit. Pre-revenue speculation; highest-beta domestic rare-earth play.
- [[UUUU]] — uranium miner with secondary rare-earth separation. Humanoid attach is real but secondary to uranium thesis.
- [[OUST]] — lidar + stereo cameras for spatial awareness. Q1 2026 +49% YoY.
- [[ALGM]] — magnetic position and current sensors. Attaches mechanically to every motor joint.
- [[CEVA]] — DSP/NPU IP licensing. Royalty leverage to whichever robotics SoC vendor wins design wins.
- [[LSCC]] — low-power FPGAs for sensor fusion and motor control. Power-efficient compute fits battery-bound form factor.
- [[ALNT]] — motion control small-cap. Only motion-control name on common "stack maps" small enough for humanoid revenue to actually move the P&L.

**Tier 2 — Coincidental exposure (mega-caps, humanoid is a rounding error):**

[[NVDA]], [[AMD]], [[QCOM]], [[TXN]], [[ON]], [[CSCO]], [[ABB]], [[ROK]], [[PH]], [[STM]], [[AMBA]], [[RBC]]. Real component sales into humanoid programs but immaterial revenue contribution through at least 2028. Own these on their primary theses, not as humanoid plays.

**Tier 3 — Stretch / narrative inclusion:**

IRDM, SLAB, NVTS, MPWR, VSH, NOVT, AME, RRX, MBLY, AEVA. Fit category labels in viral "stack maps" but weak attach to actual humanoid programs.

**Inaccessible to most Western retail (China-listed, designed-in across Tesla/Figure programs):**

- Sanhua Intelligent Controls (002050.SZ) — thermal management, valves
- Leader Drive (688017.SS) — harmonic drives
- Inovance — servo systems

Accessible only via Stock Connect or wrapper ETFs.

## Risks / counter-thesis

- **Timeline slip is the base case.** IDTechEx tracks fewer than 100 humanoids actively deployed in warehouse pilots as of early 2025. Warehouse pilot-to-rollout cycles are 18–30 months. Tesla, Figure, Agility have all missed prior unit guidance. A 2-year slip from 2027 to 2029 pushes second-derivative revenue at every Tier 1 supplier out the same distance.
- **Multiple expansion is doing most of the work.** [[VPG]] is up ~4× in 12 months on narrative repricing, not earnings. [[MP]] has run on DoD partnership news. [[USAR]] is pre-revenue at $1B+. Same pattern as AI infra 2023–2024 but at smaller cap base — corrections will be sharper.
- **China is the supply chain.** Cleanest design-in suppliers (Sanhua, Leader Drive, Inovance) are PRC-listed. Cheapest unit-economics OEMs (Unitree, AgiBot, UBTECH) are Chinese. A reciprocal US export-control regime restricting Western component sales into Chinese humanoid programs damages Tier 1 names alongside Chinese OEMs.
- **Sensors have substitutes; magnets don't.** Force-torque, position, and vision sensors face competing chemistries (capacitive vs. magnetic, lidar vs. camera-only vs. radar). Bottleneck rents diffuse. NdFeB magnets have no equivalent substitute path — concentration favors rare-earth plays over sensor plays.

## Open questions

- Does [[MP]]'s Stillwater plant hit commercial NdFeB magnet production on the H1 2026 schedule, or slip into late 2026? First-shipment confirmation is the single most material near-term datapoint for Tier 1.
- How does [[VPG]]'s Q2 2026 print read against the "Physical AI" pivot narrative? P/E of 135–215 leaves no margin for execution stumble.
- Does any Western harmonic-drive maker hit volume parity with Leader Drive by 2027?
- When does the first Western humanoid OEM (Figure, Agility, Apptronik) confirm a multi-thousand-unit production commitment with named component suppliers?
- Does [[OUST]] hit operating-cash-flow-positive in H2 2026 without further dilution beyond the $100M ATM already in flight?
- Does Tesla Optimus reach the announced 2026 internal-deployment target (low-thousands inside Tesla factories), and if so, do component suppliers get publicly named?

## Related

[[ai-capex-cycle]] · [[bottleneck-roadmap]] · [[semiconductors]] · [[market-concentration]]

## Sources

1. `sources/2026-05-13-x-stack-map-humanoid-robotics.md` — viral X "humanoid stack" thread and stock screenshots that prompted this primer.
2. ABI Research — *Humanoid Robot Market Size, 2024 to 2030*. URL: https://www.abiresearch.com/news-resources/chart-data/humanoid-robot-market-size-outlook
3. MarketsandMarkets — *Humanoid Robot Market Size, Share & Trends, 2025 To 2030*. URL: https://www.marketsandmarkets.com/Market-Reports/humanoid-robot-market-99567653.html
4. Counterpoint Research — January 2026 humanoid robot installation report (cited in third-party coverage).
5. Future Market Insights — *Humanoid Robot Market | Global Market Analysis Report - 2035*.
6. Morgan Stanley — *Humanoid Robot Market Expected to Reach $5 Trillion by 2050* (Adam Jonas).
7. IDTechEx — *Humanoid Robots 2025-2035: Technologies, Markets and Opportunities*.
8. Wedbush — MP Materials coverage initiation at Outperform / $90 PT (Dan Ives, April 2026).
