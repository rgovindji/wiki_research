---
type: theme
tags: [robotics, humanoid, oems, private-companies, supply-chain, china]
last_updated: 2026-05-16
last_full_review: 2026-05-13
sources: 2
---

# Humanoid OEMs (Original Equipment Manufacturers)

The companies actually *building* humanoid robots — most of which are private. Public-market investors can't own them directly (with the exception of [[TSLA]] for Optimus), but the OEM landscape determines which **public component suppliers** ([[MP]], [[OUST]], [[ALGM]], [[VPG]], [[AMBA]]) get design wins and which don't. This page is the OEM-side counterpart to the [[robotics]] sector primer.

## Why this matters for investors

Even though you can't buy Figure or Agility on a stock exchange, the production decisions these private OEMs make in 2026 determine the 2027-2030 revenue trajectory for every public component supplier in the [[robotics]] sector. **The OEM that wins becomes the customer concentration risk for its supply chain — and the OEM that fails takes those suppliers' growth narratives down with it.**

> **There is no "Nvidia of robotics" yet (NEW 2026-05-16 per [[2026-05-16-sergey-levine-physical-intelligence]]).** Sergey Levine (Physical Intelligence co-founder, UC Berkeley): "I would really like to see a world where there's a lot of heterogeneity in robots." **Which means:** the OEM landscape is *deliberately* heterogeneous and likely to stay that way through at least 2028-2030. **Direct portfolio implication: do not concentrate in single humanoid OEMs.** The TSLA Optimus thesis already on AVOID; private OEMs (Figure / Apptronik / Agility) are venture-stage. Value accrues to (a) foundation-model layer (mostly Meta-PyTorch + Google-Gemma + private labs like Physical Intelligence), (b) **diversified component supply chain that ships into multiple OEMs** (MP, OUST, ALGM, AMBA, VPG, ALNT), (c) compute/inference (CRWV/NBIS).

### The cost-curve unlock (NEW 2026-05-16)

Per Levine, the manipulation-arm cost curve has been faster than almost any other hardware category:

| Year | Cost / arm |
|---|---|
| 2014 (PR2 research robot) | $400,000 |
| Early-2020s (Berkeley research) | $30,000 |
| **2026 (Physical Intelligence)** | **~$3,000** |
| Forward | "A small fraction of $3,000" |

**~100× cost decline in ~10 years**, with line-of-sight to another order of magnitude by 2028-2030. **Which means:** OEM unit-economics models (which currently assume $5K-$30K per arm/limb) are likely *too conservative*. Unitree's $16K humanoid pricing isn't a floor — it's a *ceiling* that could compress by 5-10× over the decade. This radically expands TAM but also compresses OEM margins → reinforces "no winner-take-all OEM" thesis (heterogeneity).

> **What this means:** You can't directly invest in most humanoid robot makers (Figure, Agility, Apptronik are private; Chinese ones aren't accessible to most US retail). But the supplier stocks you *can* buy — rare-earth, sensors, edge AI — only matter if those private OEMs actually scale. Watching the OEMs is how you handicap the suppliers.

## The Western OEM landscape

### [[TSLA|Tesla Optimus]] — the only public OEM (proxy)

| Item | Detail |
|---|---|
| **Form factor** | Bipedal humanoid, V3 generation as of 2026 |
| **Manufacturing** | Fremont, CA — factory conversion underway |
| **Target deployment** | Low-thousands inside Tesla factories by EOY 2026 |
| **Compute** | In-house Dojo / Cortex; FSD-derived vision stack |
| **Battery** | Tesla 2170/4680 cells |
| **Suppliers** | Mostly Tesla-internal; **but uses Chinese-supplied thermal (Sanhua) and rare-earth magnets** |
| **Vertical integration** | Highest among all humanoid OEMs |
| **Stock implication** | [[TSLA]] is the only direct equity exposure to humanoid OEM upside — but Optimus represents <5% of TSLA's current valuation case; primary thesis is still EV / FSD / robotaxi |

**Tesla strategic note:** Optimus's vertical integration is a *negative* for public component suppliers — Tesla designs around them where possible. The supply chain plays better aligned with non-Tesla OEMs.

### Figure AI

| Item | Detail |
|---|---|
| **Form factor** | Figure 02 (current production) |
| **Deployment** | **BMW Spartanburg, SC** — operating in BMW's body shop on production work |
| **Compute** | NVIDIA-based (rumored — NVIDIA Cosmos integration confirmed at GTC 2026) |
| **Funding** | Microsoft, NVIDIA, OpenAI all invested ($675M round 2024 at $2.6B valuation; subsequent rounds higher) |
| **Stock implication** | Best non-Tesla proxy on [[NVDA]] robotics platform success. Component suppliers ([[ALGM]] sensors, [[OUST]] vision) most likely to win design slots here. |

### Agility Robotics

| Item | Detail |
|---|---|
| **Form factor** | Digit — bipedal, designed for warehouse logistics |
| **Manufacturing** | **RoboFab** in Salem, Oregon — claims 10,000-unit annual capacity |
| **Deployment** | GXO Logistics, Amazon warehouse pilots |
| **Funding** | DCVC, Playground Global, Amazon Industrial Innovation Fund |
| **Stock implication** | Closest thing to a "real revenue" Western humanoid story (logistics customers paying for hours of work). If Digit hits unit-economics inflection by 2027, sensor/actuator suppliers benefit first. |

### Apptronik (UPDATED 2026-05-17 PM)

| Item | Detail |
|---|---|
| **Form factor** | Apollo — bipedal, general-purpose |
| **Manufacturing** | **[[JBL\|Jabil]] is manufacturing partner** (announced) — direct public-market exposure layer |
| **Deployment** | Mercedes-Benz factories + GXO Logistics |
| **Compute** | **NVIDIA Jetson AGX Orin (275+ TOPS)** |
| **Valuation** | **$5B Feb 2026 Series A extension ($520M); $935M total Series A** |
| **Backers** | Google + Mercedes-Benz + AT&T Ventures + John Deere + Qatar Investment Authority + (prior: Microsoft, NVIDIA, Capital Factory) |
| **Roadmap** | Commercial-scale deployment 2026; fine manipulation + multi-step tasks 2027 |
| **Stock implication** | **[[JBL]] is the cleanest direct exposure**; Google's repeat investment validates Gemini Robotics integration roadmap; NVIDIA Jetson dependency = [[NVDA]] embedded |

### Agility Robotics (UPDATED 2026-05-17 PM)

| Item | Detail |
|---|---|
| **Form factor** | Digit — bipedal, designed for warehouse logistics |
| **Manufacturing** | RoboFab Salem Oregon — 10K units/yr capacity target; **<1,000 units actually shipped** |
| **Deployment** | **Amazon (narrow "tote recycling" R&D pilot only — NOT broad warehouse)** + Toyota (Feb 2026), Mercado Libre (Dec 2025), GXO, Schaeffler |
| **Valuation** | **$1.75-2.12B Series C** ($400M Jun-Sep 2025, tranched reports) |
| **Amazon stake** | $150M |
| **2026 milestone** | CEO Peggy Johnson: Digit "interoperate near humans" by mid-2026 |
| **Stock implication** | **Amazon's narrow Digit pilot contradicts "soon at scale" hype** — slower commercial trajectory than other OEMs |

### Boston Dynamics (UPDATED 2026-05-17 PM, Hyundai-owned 005380.KS)

| Item | Detail |
|---|---|
| **Form factor** | Atlas Gen 3 — most technically advanced bipedal |
| **2026 production** | **Entirely reserved for Hyundai RMAC + Google DeepMind** — no external commercial sales |
| **Manufacturing** | Hyundai $26B US investment; **30K units/yr factory by 2028** (Savannah Metaplant); Atlas deployment 2028-2030 |
| **Compute** | **Google DeepMind Gemini Robotics — NOT NVIDIA GR00T** |
| **Financials (BDX standalone)** | Revenue ~$100M (150.1B won); **loss 528.4B won = 3.5x revenue burn ratio** |
| **Internal valuation** | $20-21B (24x since 2021 acquisition) — appears promotional |
| **IPO** | **Nasdaq listing expected early 2027** |
| **Stock implication** | **Hyundai ADR (HMG)** for indirect exposure; **[[GOOGL]] gets Atlas as Gemini Robotics customer**; BDX IPO at $20B may be a sell-the-news given burn rate |

### XPENG IRON (NEW 2026-05-17 PM — promoted to Western/global category)

| Item | Detail |
|---|---|
| **Form factor** | IronMan/IRON humanoid; 5th-generation |
| **Listed parent** | **XPEV (NYSE ADR)** — see [[XPEV]] |
| **Commitment** | **¥100B (~$13.7B) to IronMan program** |
| **Compute** | **Vertical: in-house Turing AI chip** (parallels Tesla AI5) |
| **Production target** | **1,000+ units/month by late 2026 mass production** |
| **Leadership** | Former NVIDIA Android manager leads robotics |
| **Stock implication** | **Only US-listed pure-play humanoid OEM at scale outside Tesla**; significantly under-covered in US financial media; speculative bull / low-medium conviction |

## The Chinese OEM landscape (much larger market share than US)

Chinese OEMs collectively hold the majority of installed humanoid units globally as of early 2026 — Counterpoint Research data. The supply chain for Western and Chinese OEMs **overlaps significantly** at the component level (both buy from Sanhua, Inovance, often the same Asian factory floors).

### AgiBot

| Item | Detail |
|---|---|
| **Market share** | ~31% (highest globally per recent industry data) |
| **Backing** | State-supported; ties to Chinese government robotics initiative |
| **Stock implication** | No direct Western retail access |

### Unitree Robotics

| Item | Detail |
|---|---|
| **Market share** | ~27% globally |
| **Famous for** | Quadrupeds (Go1, Go2); now expanding to humanoids (H1, G1) |
| **Pricing** | **Aggressive — Unitree G1 humanoid priced at ~$16,000**, vastly undercutting Western OEMs |
| **Stock implication** | If Unitree's price-point becomes the global anchor, Western OEM unit economics get squeezed — bad for *Western* component suppliers betting on Western OEM scale |

### UBTECH

| Item | Detail |
|---|---|
| **Market share** | ~5% |
| **Listed** | Hong Kong (HKEx) — accessible via international brokers |
| **Focus** | Educational + service robots; now industrial humanoids |
| **Stock implication** | The only directly-investable humanoid OEM globally — but at small size and primarily a story stock |

## The strategic question: Western vs. Chinese supply chain decoupling

> **What this means:** Today, Tesla Optimus and Figure both buy components from Chinese suppliers (thermal valves, magnets, motors). If the US restricts those imports — or if China restricts exports — every public Western humanoid component supplier becomes radically more valuable overnight. Conversely, if the relationship stays open, Chinese suppliers (which are 30-50% cheaper) keep winning the design slots and the Western component thesis weakens.

The single most important macro variable for the [[robotics]] thesis is **whether the US-China decoupling that's happened in advanced semiconductors extends to robotics components**. Three scenarios:

| Scenario | Probability | Implication for public suppliers |
|---|---|---|
| **A. Status quo (selective decoupling)** | ~60% | Western OEMs source critical magnets domestically (good for [[MP]]) but use Chinese commodity components (Sanhua, Inovance) — mixed for public sensor/actuator names |
| **B. Full robotics decoupling** | ~25% | All Western humanoid components must come from non-PRC suppliers → massive uplift for [[MP]], [[OUST]], [[ALGM]], [[VPG]] — the public Western supply chain becomes irreplaceable |
| **C. China weaponizes rare earths** | ~15% | Even more bullish for [[MP]] specifically (US strategic asset positioning); negative for *every* Western humanoid OEM in the short term as supply chains scramble |

See [[us-china-relations]] for the broader bilateral framing.

## OEM-to-supplier mapping (high-conviction matches)

This is the design-win logic — which public suppliers benefit from which OEMs scaling. Largely inferred from public statements, partnerships, and component reverse-engineering teardowns.

| Public supplier | Most-likely OEM customer | Confidence | Why |
|---|---|---|---|
| **[[MP]]** | All Western OEMs + DoD | High | Only domestic NdFeB; strategic asset status |
| **[[OUST]]** | Figure, Agility | Medium | Lidar + stereo cameras align with NVIDIA-based perception stacks |
| **[[ALGM]]** | All Western OEMs | Medium | Magnetic position/current sensors are commodity-with-IP at every motor joint |
| **[[VPG]]** | Apptronik, Agility | Low | Force-torque is real but no design-win disclosures yet |
| **[[AMBA]]** | Lower-tier OEMs | Low | Edge AI SoCs face NVIDIA + Qualcomm competition at top of market |
| **CEVA** (no page) | Multiple via IP licensing | Medium | Royalty model = bet on whoever wins, not on any single OEM |
| **LSCC** (no page) | All OEMs (FPGA for sensor fusion) | Medium | Lattice FPGAs are quiet workhorses in motion control |

## Watch items (next 12 months)

1. **Tesla Optimus internal deployment count by EOY 2026.** Tesla has guided low-thousands; actual delivery vs guide is the most material near-term datapoint for the entire humanoid thesis.
2. **First publicly-named component supplier on a Western humanoid OEM program.** Any disclosure (Figure naming OUST, Apptronik naming ALGM, etc.) materially re-rates that public supplier.
3. **Unitree humanoid pricing trajectory.** If Unitree G1-equivalent stays at $16K and ships at volume, Western OEM economics get harder.
4. **Figure / Agility production milestone vs guide.** Both have committed to 2026-2027 capacity targets; slippage flows through to suppliers.
5. **DoD humanoid procurement.** Any defense contract for humanoid robots accelerates the supply-chain-decoupling timeline.
6. **Chinese rare-earth or component export-control announcement.** Biggest single catalyst for Western supply chain re-rating.

## Open questions

- Does Tesla open Optimus's supplier list publicly (most likely never, given Musk's preference for in-house framing)?
- Does any Western OEM (Figure, Agility, Apptronik) reach IPO by 2027-28? Figure has been rumored as the closest candidate.
- Do Chinese OEMs (Unitree, AgiBot, UBTECH) get *banned* from US deployment? If so, who picks up that share?
- Does NVIDIA take an equity position in a humanoid OEM beyond Figure? The [[NVDA]] playbook of equity-investing in customers ([[CRWV]], [[NBIS]], [[SNPS]]) suggests yes is plausible.

## Related

[[robotics]] · [[bottleneck-roadmap]] · [[ai-capex-cycle]] · [[us-china-relations]] · [[TSLA]] · [[MP]] · [[OUST]] · [[ALGM]] · [[VPG]] · [[AMBA]] · [[NVDA]] · [[GOOGL]] · [[overview]]

## Sources

1. [[2026-05-13-x-stack-map-humanoid-robotics]] — primary source for the public-supplier landscape
2. [[2026-05-16-sergey-levine-physical-intelligence]] — "no Nvidia of robotics" heterogeneity thesis; 100× arm-cost curve
3. Counterpoint Research humanoid installation data (Jan 2026 report) — Chinese OEM share data
4. Industry partnership disclosures: BMW × Figure, Mercedes-Benz × Apptronik, Amazon × Agility (publicly announced via OEMs' own communications)
