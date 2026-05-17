---
type: sector
tags: [robotics, humanoid, physical-ai, rare-earths, sensors, edge-ai]
last_updated: 2026-05-16
last_full_review: 2026-05-13
sources: 4
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

### Model paradigm shift: VLA → WAM (NEW 2026-05-16 per [[2026-05-16-jim-fan-nvda-robotics]])

Per NVIDIA Robotics chief scientist Jim Fan, the dominant model architecture is shifting:

| | Vision-Language-Action (OLD — Pi, Groot) | World Action Models (NEW — Dream Zero) |
|---|---|---|
| Built on | VLM with grafted action head ("LVA — language-heavy") | Video world models like V3 that learn physics by predicting pixels |
| Strength | Encoding nouns, knowledge | Physics, verbs, generalization |
| Weakness | Physics, generalization | Still early; "AI video slop" but learning physics by accident |
| Action vocabulary | Trained motion vocab | Open-ended natural language ("Dream Zero is GPT-2 for motion") |

**Why this matters for the supply chain:** WAMs accelerate the commercial timeline. If pixel-prediction video models can be action-fine-tuned into policies that handle 22-DOF dextrous hands (as EgoScale demonstrated), the perception-to-action software gap closes faster than expected. **OEMs need components ready earlier.**

### The data revolution — teleop → wearables → egocentric video

| Method | Scale ceiling | Status |
|---|---|---|
| **Teleop** | 24 hr/robot/day max (3 hr real) | Dying per Fan |
| **UMI / wearables** | 100k hours/year | Active; spawned unicorns Generalist + Sunday |
| **Egocentric video (NVIDIA EgoScale)** | **10M+ hours/year potential** | NVIDIA going all-in |

**The dexterity scaling law (NEW):** EgoScale discovered a clean log-linear relationship between pre-training hours of egocentric video and validation loss — 6 years after the original LLM scaling law. **Robotics now has its own neuroscaling law.** Implication: throwing more egocentric data at the model produces predictable improvements, just like LLMs from 2018-2023.

### The 2040 endgame (Fan framework)

| Achievement | Timeline | Description |
|---|---|---|
| **Physical Turing test** | **2-3 years (2028-2029)** | Can't distinguish human vs robot doing a task |
| **Physical API** | Mid-2030s | Robots configured via API/CLI; lights-out factories |
| **Physical auto-research** | By 2040 | Robots designing next-gen robots |

Fan's anchor: AlexNet (2012) → AI ascent (2026) = 14 years. Another 14 years → 2040. **95% confidence on full endgame by 2040.**

**Bias caveat:** Fan is NVIDIA's chief scientist of Robotics speaking at NVIDIA's conference. Discount certainty by ~15% for self-promotional bias. But even at 80% confidence, the framework reshapes the wiki's robotics timeline from "speculative" to "credibly priced 5-15 year buildout."

### Independent timeline anchor — Sergey Levine (NEW 2026-05-16 per [[2026-05-16-sergey-levine-physical-intelligence]])

Sergey Levine, co-founder of **Physical Intelligence** (the leading independent robotics foundation-model lab, currently funded by Jeff Bezos / Khosla / Lux at $2.4B valuation) and UC Berkeley professor, gives an independent timeline that **partly corroborates and partly contradicts Jim Fan's framework**:

| Milestone | Levine | Fan | Wiki resolution |
|---|---|---|---|
| Useful narrow deployment ("flywheel start") | **1-2 years** | Implicit in 2-3yr Physical Turing test | Aligned |
| GPT-5-equivalent robotics | **2028-2030** | "Physical Turing test 2-3 years (2028-2029)" | Aligned (~6 months apart) |
| Fully autonomous home robot | **~5 years median** | n/a (different metric) | Levine more measured |
| Full endgame / "Physical auto-research" | n/a | **2040, 95% confidence** | Fan more aggressive |

**Combined envelope: 2-5 years for first major commercial deployment, 5-10 years for broad capability, 10-15 years for full endgame.** Two top-lab researchers from competing organizations (NVIDIA + Physical Intelligence) converging on a 3-5 year horizon for the first capability inflection is the strongest cross-validation signal the wiki has captured.

### The cost-curve unlock — "what makes this different from 2009 self-driving"

Per Levine, robot arms have collapsed in price faster than almost any hardware category:

| Period | Cost/arm | Notes |
|---|---|---|
| 2014 | **$400,000** | PR2 research robot |
| Early-2020s | $30,000 | Berkeley research lab |
| **2026 today** | **~$3,000** | Physical Intelligence per-arm cost |
| Forward | **"A small fraction of $3,000"** | Levine guidance |

That's **~100× cost decline in ~10 years**, with line-of-sight to another order of magnitude. **Which means:** by 2028-2030 a humanoid-equivalent arm could be a few-hundred-dollar capex item. At that price point, the *deployment-velocity* assumption in market sizing (16K units 2025 → 115K by 2027) is almost certainly underestimating the back half of the decade — and the [[datacenter-construction]] labor shortage of 2028-2030 has a potential robotic-labor offset.

### The data flywheel framing

Levine: "What I tend to think about in terms of timelines is not the date when it will be done, but the date when the flywheel starts." Physical Intelligence's robot dataset is currently **1-2 orders of magnitude smaller** than multimodal LLM training data — bottleneck but not catastrophic. The flywheel starts when robots deployed for real human-paying tasks begin generating training data faster than teleop can. Levine estimate: **1-2 years** to that inflection.

**Manipulation > driving for flywheel speed:** Self-driving took 15+ years (Google 2009 → Waymo 2024) because mistakes are catastrophic. Manipulation mistakes are usually recoverable → data flywheel can spin faster than AVs did. **Counter-argument to "robotics will be slow like AVs."**

### Foundation-model architecture: "literally the same model as LLMs"

Physical Intelligence's π0 model = **Google's open-source Gemma VLM + grafted action expert** (mixture-of-experts using flow matching for continuous action outputs). The robotics stack is not a separate field — it's PyTorch + open-source LLM + action head. **Investment implications:**
- **GOOGL** (Gemma) gets ecosystem influence at the foundation-model layer of robotics (see [[GOOGL]])
- **META** (PyTorch) gets training-framework lock-in across the entire robotics research community (see [[META]])
- **Independent robot OEMs** lose any "AI moat" claim — they're all building on the same open substrate, which is why Levine explicitly argues **"there is no Nvidia of robotics" yet**

### "No Nvidia of robotics" — heterogeneity thesis

Levine: "I would really like to see a world where there's a lot of heterogeneity in robots." His framing: no single robot OEM will dominate; **value will accrue to (a) foundation-model layer, (b) component suppliers across heterogeneous form factors, (c) compute**. Direct portfolio implications:
- **Bearish for single humanoid OEMs** (TSLA Optimus — already AVOID; Figure / Apptronik / Agility — private)
- **Bullish for the Tier 1 component basket** (MP, OUST, ALGM, AMBA, VPG, ALNT) — diversified across whichever form factor wins
- **Bullish for off-board compute** (CRWV/NBIS — robots will likely stream sensor data to cloud GPUs for low-cost form factors; see below)

### Off-board inference: the latent neocloud demand vector

Levine: low-cost robots will likely stream sensor data to **cloud GPUs**, with on-board inference reserved for outdoor / reliability-critical use cases. **Which means:** if a billion robots deploy in 2030+ each pulling control commands from cloud GPUs, that's a **new compute load class** (high QPS, low-batch, latency-sensitive) — different from LLM training/inference, additive to it. [[CRWV]] / [[NBIS]] / [[ORCL]] all latent beneficiaries; nobody is pricing this yet.

## Adjacent: autonomous trucking is *applied AI in the physical world*, ahead of humanoids on commercial traction (NEW 2026-05-16)

The wiki tracks humanoid robotics as the canonical "physical AI" thesis (this page + [[humanoid-oems]]). Worth noting that **autonomous trucking is the OTHER physical-AI category** — and it's *meaningfully ahead* of humanoids on commercial-revenue traction:

| | Humanoid robots (2026) | Autonomous trucking (2026) |
|---|---|---|
| Public pure-plays | None (private: Figure, Apptronik, Agility, Physical Intelligence) | **2** — [[AUR]] (Aurora), KDK (Kodiak AI, IPO Sept 2025) |
| Commercial revenue today | ~$0 from humanoids; component cohort revenue from EVs/wind | **$1M Q1 2026 (Aurora) — Berkshire-backed McLane** as first driverless paying customer |
| Timeline to "real" commercial scale | Levine: 5 yrs; Fan: 2-3 yrs Turing test | 2026-2027 active scale-up (200 trucks Aurora EOY 2026) |
| NVIDIA stack | GR00T + Cosmos + Dream Zero (model layer) | **Drive Thor + Blackwell** (commercial hardware in production) |

**Which means:** for investors who want exposure to the "AI applied to the physical world" thesis BEFORE humanoid revenue inflects (still 2-5 yrs away), **autonomous trucking is the only category with paying customers today**. See [[AUR]] for the bull/bear deep dive. The trade-off: AUR has real revenue but valuation prices 5+ years of perfection (~$15.7B market cap on $14-16M 2026 revenue guide).

The component-supplier thesis on this page (MP / OUST / ALGM / AMBA / VPG) is **agnostic** to humanoids vs. trucks — most of the same sensor / rare-earth / edge-AI content goes into both form factors. Autonomous trucking actually de-risks the component thesis by providing earlier-cycle revenue validation for the supply chain.

## Dylan Patel: Few-shot learning breakthrough in 6-18 months (NEW 2026-05-17)

Per [[2026-05-16-dylan-patel-invest-like-best]]: Dylan Patel's robotics timeline is **more aggressive than Levine (5yr) or Fan (2-3yr Turing test)**:

> *"In the next 6 to 18 months we'll start seeing real breakthroughs in robotics that enable few-shot learning... there's a pre-trained robot model and now there's a robot that you have hired or bought or whatever. You show it a few examples and it's able to do it."*

Dylan's view of the architecture race:
- **VLA models are dead-end** ("inefficient in data") — aligns with LeCun's framing
- **Large-scale pre-training of robot models** is the unlock — same way humans are sample-efficient because of accumulated experience
- **Software-only singularity** is "a blip" — once software automation is mature, physical world catches up because models can now write the firmware and microcontroller code that previously bottlenecked robotics development
- **Robots become "a model package you download onto your standard robot"** — i.e., commoditized SaaS-like distribution

**The four-way researcher contradiction now sharpens to a near-consensus**:

| Source | Timeline | Architecture view |
|---|---|---|
| Jim Fan (NVIDIA) [[2026-05-16-jim-fan-nvda-robotics]] | 2-3yr physical Turing test | VLA→WAM (generative) |
| Levine (Physical Intelligence) [[2026-05-16-sergey-levine-physical-intelligence]] | 5yr fully autonomous | VLA + action expert (pragmatic) |
| LeCun (AME Labs) [[2026-05-16-yann-lecun-ame-labs]] | 5yr paradigm shift | JEPA only |
| **Dylan Patel (SemiAnalysis) NEW** | **6-18mo for few-shot breakthrough** | **Large-scale pre-train + sample-efficient transfer** |

**Implication for the wiki's stance**: The compression of the 6-18mo timeline by Dylan (most aggressive yet) reinforces the 2026-2030 component supply chain buildout window. **Bullish for [[MP]], [[OUST]], [[ALGM]], [[AMBA]], [[VPG]] timing.** The component cohort is being chosen *right now* by OEMs for the breakthrough wave that Dylan thinks lands in 18 months.

## Adjacent commodity bottleneck — copper (NEW 2026-05-16)

Per [[copper-thesis]]: humanoid robots are copper-intensive. Each humanoid contains copper-wound motors, batteries with copper current collectors, and high-density wiring harnesses — exact tonnages are not yet quantified for scaled deployment, but on the demand-curve compounding logic, robotics adds to the AI/EV/grid demand vectors already locking in a structural copper deficit by 2029+ (Goldman). For investors playing the robotics buildout, copper exposure (CPER futures or COPX miner ETF) is an indirect but high-conviction parallel position to the component-supplier basket on this page. **The Tier 1 robotics component stack (MP, OUST, ALGM, AMBA, VPG, ALNT) is the closest direct play; copper is the broader-market commodity expression of the same buildout.**

## Architecture contradiction — three top researchers disagree (NEW 2026-05-16)

Per the wiki house rule (contradictions surfaced, not resolved): in a 72-hour window the wiki ingested three top researchers — one from NVIDIA, one from the leading independent robotics-foundation-model lab, one Turing Award winner who just left Meta to start his own lab — and they **disagree on the architecture** for robotics foundation models even while broadly agreeing on the 3-5 year timeline horizon.

| Researcher | Architecture view | Robotics timeline |
|---|---|---|
| **Jim Fan** (NVIDIA Robotics chief scientist) [[2026-05-16-jim-fan-nvda-robotics]] | VLA → **WAM (World Action Models)** is the future. Generative video models (Dream Zero) learn physics by predicting pixels. "Dream Zero is GPT-2 for motion." | Physical Turing test 2-3 years; 2040 full endgame, 95% confident |
| **Sergey Levine** (Physical Intelligence co-founder) [[2026-05-16-sergey-levine-physical-intelligence]] | **VLA + action expert IS working**. π0 = Gemma VLM + flow-matching action head (mixture-of-experts). Pragmatist — "it's literally the same model as LLMs." | Median 5-year fully autonomous home robot; flywheel start 1-2 years |
| **Yann LeCun** (AME Labs, ex-Meta FAIR) [[2026-05-16-yann-lecun-ame-labs]] | **VLA = "pretty much now seen as a failure."** Generative video world models = "losing proposition." Only **JEPA** (joint-embedding predictive architecture, predicts in *representation space* not pixel space) works. | Within ~5 years; "paradigm shift to world models will be obvious by early 2027" |

**Common ground:** all three see a 3-5 year horizon for the first major capability inflection.

**Divergence:** they disagree on WHICH architecture gets there. The wiki does not resolve this — both because the user decides, and because each researcher has both expertise and self-interest baked into their position (Fan promotes NVIDIA tooling; Levine has shipping product on VLA; LeCun is raising money for a JEPA-bet lab).

### Why this matters for the wiki's positioning

**Investment implication: the architecture uncertainty does NOT change demand for the underlying components.** Compute, rare-earths, sensors, harmonic drives, edge AI SoCs — all required regardless of which architecture wins. **Which means** the [[robotics]] Tier 1 component basket ([[MP]], [[OUST]], [[ALGM]], [[AMBA]], [[VPG]], [[ALNT]]) wins regardless. The diversified bottleneck-supplier thesis is *reinforced* by this contradiction, not weakened.

**Investment implication: do NOT concentrate in any single robotics-foundation-model story.** Public-market exposure to robotics foundation models flows through NVDA (Cosmos/Dream Zero/Groot platform) and indirectly via GOOGL (Gemma substrate for Physical Intelligence π0). Pure-play model labs are venture-stage (Physical Intelligence, AME Labs, Skild, Sunday, Pi). Tesla Optimus already on AVOID for unrelated reasons; the architecture contradiction reinforces de-rating any single private-OEM concentration in [[humanoid-oems]].

**Investment implication: LeCun timing is independent corroboration.** When three researchers from three different organizations all forecast a 3-5yr horizon, the architecture disagreement matters less than the timeline convergence. The 2026-2028 component build-out window is supported regardless of who's "right" on architecture.
- **Force-torque sensing precision.** Dexterous manipulation requires sub-Newton force-feedback precision, which is where [[VPG]] and competing precision-measurement vendors live.
- **Spatial awareness.** Lidar + stereo cameras + IMU sensor fusion for navigation and obstacle avoidance. [[OUST]] is the highest-quality Western pure-play.
- **Edge AI inference latency.** Control loops require sub-10ms inference at single-digit-watt power budgets — a different stack than autonomous-driving compute. Favors low-power FPGA + DSP/NPU IP licensing over bulk GPU.

## OEM landscape May 2026 — production-rate data (NEW per [[2026-05-17-robotics-multi-agent-batch]])

**Quantitative production-rate snapshot (most current data — May 2026)**:

| OEM | Listing | Valuation | Production rate (2025-2026) | Customer base | Foundation model |
|---|---|---|---|---|---|
| **Unitree** (Hangzhou) | Shanghai STAR IPO ~$610M filed | Private | **5,500 units 2025 → 20K target 2026** ($13.5-73.9K/unit) | Researcher + consumer + early industrial | Proprietary |
| **AgiBot** (Shanghai) | Private | Unicorn (>$1B) | **5,000 units by end 2025** + multi-fold 2026 | China industrial; gov-backed (Xi visited Apr 2025) | Proprietary |
| **Figure AI** (US) | Private | **$39B Sept 2025** | **150 units 2025 → 240/month April 2026 → 100K over 4 yrs** | BMW Spartanburg (30K+ X3 vehicles in 11mo pilot); Leipzig expansion summer 2026 | Helix VLA (in-house, ended OpenAI 2/2025) |
| **Tesla Optimus** | TSLA NASDAQ | (parent) | **Gen 3 July-Aug 2026; 50-100K target 2026; 1M/yr by EOY** | Zero external; "primarily for learning" Q4 2025 | Proprietary on AI5/Samsung Texas |
| **UBTECH** | 9880.HK | (listed) | **800M yuan+ Walker S/S2 orders 2025** | BYD + Geely factories | Proprietary |
| **XPENG IRON** | XPEV NYSE | (parent) | **1,000+/month late 2026 target**; ¥100B commit | China automotive | Proprietary on Turing AI chip |
| **Apptronik** (Austin) | Private | **$5B Feb 2026** ($935M Series A total) | Roadmap: commercial scale 2026 | Mercedes-Benz factories + GXO Logistics | NVIDIA Jetson AGX Orin |
| **Agility Robotics** | Private | **$1.75-2.12B** | **<1,000 shipped** vs 10K/yr capacity target | Amazon (narrow R&D), Toyota, Mercado Libre, GXO, Schaeffler | Proprietary |
| **Boston Dynamics** | Hyundai 005380.KS subsidiary | $20-21B internal | 2026 production reserved for Hyundai + Google DeepMind | Hyundai factories (2028 deploy); Spot + Stretch enterprise | **Google Gemini Robotics (NOT GR00T)** |
| **1X Technologies** | OpenAI portfolio | Private | Neo pre-orders $20K + $499/mo; **2026 units rely on human teleoperators (NOT autonomous yet)** | Consumer pre-orders | Proprietary |
| **Sanctuary AI** (Vancouver) | Private | ~$140M total raised | Gen-8 Phoenix; "candidate for acquisition" | None disclosed | Magna manufacturing partner |
| **Fourier Intelligence** | Private | (China) | GR-2 (53 DOF) targeting 2026 mass production | Industrial | Proprietary |

**Cross-cutting observations**:
- **Unitree is the world's TOP humanoid producer 2025** (5.5K) — more than Tesla + Figure + Agility combined
- **Figure is operationally ahead of Tesla in commercial deployment** (30K+ BMW vehicles delivered in 11mo pilot)
- **Tesla's prediction-market consumer-launch probability: ONLY 6%** for June 2026
- **Bank of America forecasts: 90K humanoid units shipped 2026 → 1.2M by 2030**

## Foundation-model layer (NEW 2026-05-17 PM)

The robotics foundation-model space is bifurcating into **closed-proprietary** vs **open-ecosystem**:

| Player | Valuation | Funding | Strategy | Commercial state |
|---|---|---|---|---|
| **Skild AI** (Pittsburgh) | **$14B** Jan 2026 Series C ($1.4B) | NVDA + Lightspeed + Coatue + SoftBank + Bezos | Closed-model platform | **$30M+ ARR**; Foxconn/NVIDIA, ABB, Universal Robots deployments |
| **Physical Intelligence (π)** | $11B (in talks for $1B raise; $600M Series B late 2025) | Bezos + OpenAI + Thrive | **Open-source (Gemma3 backbone)** | π0.6 with 1000+ citations; no named commercial customers yet |
| **NVIDIA GR00T** | (NVDA segment) | N/A | **Hybrid (N1.7 commercial license; N2 open)** | Partners: Figure, Skild, ABB, FANUC, KUKA, Universal Robots, Franka, AGIBOT, YASKAWA |
| **Google Gemini Robotics** | (GOOGL segment) | N/A | Proprietary | Boston Dynamics Atlas runs on this |
| **Tesla Optimus** | (TSLA segment) | N/A | Closed vertical | Internal only |

**"Linux of robotics" hypothesis**: π0's open Gemma-based stack is the most likely commoditizer. Skild's $14B valuation is **threatened by open-source adoption** — 11+ commercial VLA deployments by Q1 2026 signal moat narrowing.

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

**Tier 1.5 — Humanoid-specific public-market plays (NEW 2026-05-17 PM)**:

| Ticker | Listing | Why exposed |
|---|---|---|
| **[[XPEV]]** | NYSE ADR | **¥100B IronMan commitment; 1K+/month late 2026 mass production target**; vertical-integrated Turing AI chip; only US-listed pure-play humanoid OEM at scale (outside Tesla) |
| **HMG (Hyundai)** | NYSE ADR | Boston Dynamics owner; 30K Atlas units/yr factory 2028; Atlas uses Google DeepMind Gemini Robotics |
| **HNHPF (Foxconn)** | OTC US | Industrial humanoid manufacturing partner (revealed at NVIDIA GTC 2026); Vietnam/Mexico expansion |
| **MGA (Magna)** | NYSE | Sanctuary AI manufacturing + equity partner |
| **[[JBL]] (Jabil)** | NYSE | **Apptronik manufacturing partner** — humanoid revenue layer beyond AI servers |
| **KOID / KSTR** | NYSE ETFs | KraneShares Humanoid Robotics + STAR Market ETFs — diversified A-share exposure (Leader Drive 300695.SZ, Inovance 300124.SZ, Estun 002747.SZ) without QFII requirement |

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

## 🔥 Rare earth validation event (NEW 2026-05-17 PM)

**Musk publicly confirmed May 2026**: Tesla Optimus production HIT BY China rare earth export controls; Tesla seeking licenses.

**Hard demand math** (each Optimus = 3.5kg NdFeB):
- Tesla Optimus alone: **50-100K units 2026 = 175-350 tonnes NdFeB**
- At 1M units/yr by EOY 2026: **3,500 tonnes NdFeB annual** (Tesla alone)
- Add Figure (240/month → BotQ 12K/yr target), Apptronik (Mercedes commercial), Agility (10K/yr capacity), Unitree (20K target 2026): **multi-OEM stacked demand**

**Which means**: the rare-earth bottleneck has moved from theoretical to actively-blocking-production at the marquee customer. [[MP]] thesis sharpens materially.

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
- [[2026-05-17-robotics-multi-agent-batch]] — May 17 PM comprehensive update: 6 parallel Haiku subagents covering Tesla Optimus production state, Figure AI deployments, Apptronik/Agility/Boston Dynamics OEMs, Skild/Pi/1X/Sanctuary foundation models, China supply chain + Foxconn, NVIDIA GR00T ecosystem. Quantitative OEM production rates, valuations, customer wins, foundation-model bifurcation, rare-earth validation event

## Earlier sources

1. `sources/2026-05-13-x-stack-map-humanoid-robotics.md` — viral X "humanoid stack" thread and stock screenshots that prompted this primer.
2. [[2026-05-16-jim-fan-nvda-robotics]] — NVIDIA Robotics chief scientist on VLA→WAM, dexterity scaling law, 2040 endgame
3. [[2026-05-16-sergey-levine-physical-intelligence]] — Physical Intelligence co-founder + Berkeley professor: 5-yr timeline anchor, 100× arm cost decline, data flywheel framing, "no Nvidia of robotics"
4. [[2026-05-16-yann-lecun-ame-labs]] — Turing Award winner + AME Labs founder: VLA = failure, generative video world models = losing proposition, only JEPA / joint-embedding works — completes the 3-way architecture contradiction
5. [[2026-05-16-dylan-patel-invest-like-best]] — Dylan Patel: 6-18 month few-shot learning breakthrough timeline (most aggressive yet); large-scale pre-train + sample-efficient transfer (added 2026-05-17)
2. ABI Research — *Humanoid Robot Market Size, 2024 to 2030*. URL: https://www.abiresearch.com/news-resources/chart-data/humanoid-robot-market-size-outlook
3. MarketsandMarkets — *Humanoid Robot Market Size, Share & Trends, 2025 To 2030*. URL: https://www.marketsandmarkets.com/Market-Reports/humanoid-robot-market-99567653.html
4. Counterpoint Research — January 2026 humanoid robot installation report (cited in third-party coverage).
5. Future Market Insights — *Humanoid Robot Market | Global Market Analysis Report - 2035*.
6. Morgan Stanley — *Humanoid Robot Market Expected to Reach $5 Trillion by 2050* (Adam Jonas).
7. IDTechEx — *Humanoid Robots 2025-2035: Technologies, Markets and Opportunities*.
8. Wedbush — MP Materials coverage initiation at Outperform / $90 PT (Dan Ives, April 2026).
