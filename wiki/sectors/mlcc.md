---
type: sector
tags: [components, mlcc, capacitors, passive-electronics, japan, ai-infrastructure, bottleneck]
last_updated: 2026-05-29
last_full_review: 2026-05-29
sources: 1
conviction: high (structural demand) / medium (Western-accessible names)
stance: bull
---

# Multilayer Ceramic Capacitors (MLCC)

## What this is

Multilayer ceramic capacitors (MLCCs) are passive components that filter power, decouple high-frequency noise, and stabilize voltage rails inside every modern electronic system. They sit alongside resistors and inductors at the absolute bottom of the BOM — historically commoditized, structurally invisible, and never the subject of investor narrative — but the **AI rack densification cycle** has changed the supply-demand equation in a way the market has not yet priced.

**The catalyst that surfaced this page** ([[2026-05-28-DELL-Q1-FY27-earnings]]): Dell's Q1 FY27 disclosures referenced **roughly 440,000 MLCCs per NVIDIA GB300 rack** for power filtering and decoupling. Vera Rubin NVL72 is denser still. This is the single most-under-discussed quantitative bottleneck in the entire AI buildout — and the wiki had zero coverage until 2026-05-29.

> **What this means:** Every NVDA GB300 / Vera Rubin rack consumes ~440K MLCCs. DELL alone is shipping at $16.1B/quarter AI server revenue, $51.3B AI backlog, FY27 guide $165-169B. Add [[HPE]] + [[SMCI]] + hyperscaler-direct ODMs (Foxconn / Quanta / Wiwynn / [[CLS]]) and you get **multiple billions of MLCCs per year of incremental demand from AI rack densification alone** — on top of the existing baseline of automotive, mobile, industrial, and consumer demand. The MLCC layer is the closest analog to ABF substrates ([[IBDXY]], [[AJINY]]) — invisible, Japanese-dominated, structural-pricing-power story that hasn't yet had its UBS-style reframing moment.

## Why it matters now

Four structural drivers compound through 2026-2028:

1. **AI rack densification.** GB300 = 440K MLCCs/rack. Vera Rubin denser. Every new generation of NVDA + AMD + custom-ASIC accelerator increases MLCC content per system, not decreases it. The historical "MLCCs are commodities" framing breaks down because **high-capacitance / high-voltage / high-reliability MLCCs are not interchangeable** with consumer-grade MLCCs — the AI-rack tier is a different market.
2. **Automotive electrification.** Each EV uses ~8,000-10,000 MLCCs vs. ~3,000 for an ICE vehicle. The automotive MLCC mix is high-reliability (AEC-Q200 qualified), high-margin, and supply-constrained.
3. **Humanoid robotics** ([[robotics]]). Tesla Optimus / Figure / Apptronik / 1X all use precision actuators with significant MLCC content. Per [[2026-05-13-x-stack-map-humanoid-robotics]] estimates, each humanoid robot may use 5,000-10,000 MLCCs depending on actuator count. BofA's 90K → 1.2M humanoid unit forecast (2026-2030) implies a multi-year incremental MLCC demand layer.
4. **Defense + aerospace.** Hypersonic, radar, EW, satellite all require high-reliability passives. Golden Dome program scale-up ([[aerospace-defense]]) pulls high-rel MLCC demand from a base where supply was already tight.

> **What this means:** four independent demand vectors are simultaneously ramping at structural rates, all converging on the same Japanese-dominated supply base. This is the classic bottleneck pattern the wiki tracks in [[bottleneck-roadmap]] — and like ABF substrates pre-2024, the equity market has not yet priced it.

## Supply structure: Japanese oligopoly + Korean + Taiwanese second tier

| Player | Listing | Global share (est.) | Wiki coverage | Notes |
|---|---|---|---|---|
| **Murata Manufacturing** | Japan 6981.T · OTC ADR **MRAAY** | ~40% global / >50% high-rel | NOT covered (gap) | The dominant player; high-end automotive + AI-rack tier exposure; structural pricing power |
| **TDK Corporation** | Japan 6762.T · OTC ADR **TTDKY** | ~10-15% MLCC + batteries + sensors | NOT covered (gap) | Diversified electronics conglomerate; Apple battery exposure dilutes the MLCC purity but provides cross-cycle stability |
| **Samsung Electro-Mechanics** | Korea 009150.KS · OTC ADR **[[SSEHY]]** | Significant — material global share | **DUAL-EXPOSED via existing wiki page for ABF substrates** | The cleanest existing-wiki name to upgrade for MLCC exposure without opening a new position |
| **Taiyo Yuden** | Japan 6976.T · less-liquid ADR | ~10% global | NOT covered (gap) | Pure-play passives — most MLCC-purity exposure; smaller scale + less institutional liquidity |
| **Yageo Corporation** | Taiwan 2327.TW · OTC ADR **YAGYY** | Growing global share | NOT covered (gap) | Acquired KEMET (Q3 2020) for Western channel access; aggressive M&A roll-up |

> **What this means:** The structurally cleanest single-name exposure is **Murata** — both because it has the largest share of the high-end AI-rack tier and because it is structurally priced as a "diversified Japanese conglomerate" rather than as an AI-bottleneck pure-play. The cleanest cross-exposure inside the existing wiki framework is **[[SSEHY]] dual coverage** — same position, two thesis legs.

## How to think about the MLCC bottleneck vs. other layers

The MLCC layer differs from other AI-infrastructure bottlenecks in three important ways:

1. **The unit economics are tiny but the volumes are gigantic.** A single high-end MLCC costs $0.01-$0.10. The pricing power doesn't come from selling more expensive parts — it comes from selling 100,000x more parts per system. Revenue scales with volume × pricing, and both are growing.
2. **The technology moat is in the dielectric materials science, not the manufacturing.** Modern AI-tier MLCCs use barium titanate dielectrics doped with rare earths (yttrium, dysprosium, neodymium) — connecting MLCC supply to the [[rare-earths]] bottleneck. This double-bottleneck framing is what makes the layer structurally hard to compete on cost.
3. **Capacity expansion takes 18-24 months.** Murata's last major MLCC capacity announcement (Fukui Plant phase III) took 30 months from announcement to commercial shipment. AI demand is accelerating faster than supply can ramp. **The 2026-2028 window is structurally tight regardless of capex response.**

## Investability tiers

| Tier | Name | Why now | Risk |
|---|---|---|---|
| **A — cleanest leverage** | **MRAAY (Murata)** | Largest global share; highest-margin AI-rack-tier exposure; structurally priced as conglomerate | OTC ADR liquidity; Japanese listing complications |
| **A — cleanest leverage via existing wiki position** | **[[SSEHY]]** | Already bull/medium-high for ABF substrates; **MLCC adds optionality without new position** | Korean-listing complications; already up materially |
| **B — diversified electronics** | **TTDKY (TDK)** | Lower MLCC pure-play exposure (battery + sensor dilution) but more US-investor-friendly | Apple battery business is a major cross-current |
| **B — passive pure-play** | **6976.T (Taiyo Yuden)** | Cleanest pure-play MLCC exposure | Smaller scale; less institutional access |
| **C — emerging-market consolidator** | **YAGYY (Yageo)** | Roll-up strategy; Western channel via KEMET | Taiwan geopolitical risk; less commentary on AI-rack tier |

## Why this fits the wiki framework

MLCC is **the passive-component layer of the bottleneck-roadmap** that the wiki has tracked through:

| Layer | Wiki coverage | MLCC analog |
|---|---|---|
| Compute (CoWoS) | [[NVDA]] · [[TSM]] · [[AMKR]] · [[ASX]] | ↔ tightening 2025-26 |
| Memory (HBM) | [[MU]] · SK Hynix · Samsung | ↔ tightening 2025-26 |
| ABF substrates | [[IBDXY]] · [[AJINY]] · [[SSEHY]] · [[ATSAY]] | ↔ tightening 2025-26 |
| Photonic substrates | [[SOITEC]] · [[AXTI]] | ↔ tightening 2026-27 |
| Power systems | [[VRT]] · [[ETN]] · [[GEV]] · [[BE]] | ↔ tightening 2026-28 |
| **MLCC (this page)** | **NEW 2026-05-29 — Murata + TDK + [[SSEHY]] + Taiyo Yuden + Yageo** | **↔ structurally tightening 2026-28, market-unpriced** |
| EUV | [[ASML]] | ↔ tightening 2028-30 |

The pattern repeats: invisible component layer → AI rack densification → demand acceleration → Japanese / Korean / Taiwanese supply oligopoly → multi-year pricing power. The MLCC layer is the **2026-2028 sweet spot** in this framework — earlier than EUV, later than memory.

## Open questions / what to watch

1. **Murata Q1 FY27 print** (early August 2026) — first opportunity to verify AI-tier MLCC mix and pricing
2. **TDK Q1 FY27 print** — Apple battery overhang vs. MLCC pull
3. **Any explicit NVDA / DELL MLCC supplier disclosure** — current disclosures are aggregate "passive components"
4. **Capex announcements at Murata / TDK / Samsung E-M** — capacity expansion lead time is the structural ceiling
5. **Rare-earth supply chain linkage** — barium titanate dielectric dopants connect MLCC to [[rare-earths]] bottleneck

## Risks / counter-thesis

- **MLCC supply could surprise on the upside.** Murata + TDK + Samsung E-M all have idle capacity from the 2022-2023 consumer-electronics downturn. AI demand could absorb the slack without triggering new-fab investment — limiting pricing power gains.
- **Per-system MLCC content could compress.** As power-management ICs (PMICs) integrate more on-die, discrete MLCC count per rack could fall over time. The 440K/rack number is a snapshot, not a trend line.
- **Chinese MLCC capacity (Eyang, Three-Circle, Fenghua) is growing.** Like CXMT in DRAM, Chinese passives are taking commodity tier share. Top-end / high-rel remains Japanese, but margin compression at the commodity tier could drag aggregate numbers.
- **Currency exposure.** Yen weakness has been tailwind for Japanese exporters; reversal (e.g., per [[2026-06-16-boj-decision]] playbook) would compress reported margins by 5-15%.

## Position sizing considerations

This is a **structural bull thesis** with **bottleneck-pricing-power dynamics** — similar in shape to ABF substrates 12 months ago. The cleanest sizing is:

1. **Existing [[SSEHY]] position** — already in wiki; MLCC adds optionality without additional capital outlay
2. **MRAAY** as a starter / non-core add — 1-2% position for AI-tier-exposed conglomerate
3. **Avoid concentration** — passive components are uncorrelated with most wiki bull names but highly correlated with AI capex factor; size accordingly per [[hedging-risk]] framework

**Not financial advice.** Per house rules, this page surfaces the thesis and counter-thesis. Sizing and execution are user decisions.

## Related

[[bottleneck-roadmap]] · [[rare-earths]] · [[SSEHY]] · [[IBDXY]] · [[AJINY]] · [[2026-05-28-DELL-Q1-FY27-earnings]] · [[2026-05-29-dell-upstream-second-derivative]] · [[ai-capex-cycle]] · [[nvda-supply-chain]] · [[hedging-risk]] · [[overview]] · [[watchlist]]

## Sources

1. [[2026-05-28-DELL-Q1-FY27-earnings]] — primary source for the 440K MLCCs / GB300 rack disclosure; the catalyst for this page
2. [[2026-05-29-dell-upstream-second-derivative]] — synthesis flagging MLCC layer as Tier-D wiki gap

## Citations

- TechInsights — MLCC content per AI server: https://www.techinsights.com (no specific URL; industry coverage)
- Murata Manufacturing Investor Relations: https://corporate.murata.com/en-global/ir
- TDK Corporation Investor Relations: https://www.tdk.com/en/ir/index.html
- Samsung Electro-Mechanics IR: https://www.samsungsem.com/global/ir/ir-information.do
- TrendForce — MLCC industry tracker: https://www.trendforce.com (industry analyst)
