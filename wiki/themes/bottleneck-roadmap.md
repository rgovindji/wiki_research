---
type: theme
tags: [ai, supply-chain, bottlenecks, semianalysis, robotics, wam]
last_updated: 2026-05-16
last_full_review: 2026-05-09
sources: 5
---

# Bottleneck Roadmap (2026 → 2030)

## What this is
A time-sequenced view of which physical resource is the binding constraint on AI compute scaling each year through the end of the decade. The bottleneck moves down the stack as supply chains catch up — and the pattern matters for portfolio construction because **the pricing power lives wherever the binding constraint is**.

Synthesized from the May 2026 Dwarkesh × Dylan Patel interview ([[2026-05-09-dwarkesh-dylan-semianalysis]]).

## The sequence

| Period | Binding constraint | Why | Beneficiaries (pricing power) |
|---|---|---|---|
| 2023 | **CoWoS packaging** | [[TSM|TSMC]]'s advanced packaging capacity couldn't keep up; Nvidia was supply-constrained | [[AMKR]], [[ASX]], [[CAMT]] (CoWoS overflow + inspection) |
| 2024 | **Power + data centers** | Hyperscalers ahead of grid availability; permitting gridlock | [[VRT]], [[ETN]], gas turbines |
| **2025-2026** | **Memory (HBM + DRAM)** | HBM4 ramp insufficient; consumer DRAM has to be destroyed to free wafers for AI | **[[MU]]**, SK Hynix, Samsung; HBM ASPs structurally up |
| **2027** | **Cleanroom space (fabs) + transformers** | Memory makers + foundries didn't build new fabs through the 2023 trough; takes 2 years to build a fab. **NEW:** transformers (medium/high-voltage substation gear) are emerging as a parallel grid-side bottleneck — [[GEV]] consolidated control via $5.3B Prolec buyout Feb 2026. | TSMC, Micron + foundry equipment ([[KLAC]], [[LRCX]], [[AMAT]], [[TER]]) + fab consumables ([[ENTG]]) + industrial gases ([[APD]] — multi-decade BOO contracts kick in 2028-2030) + transformer makers ([[GEV]]/Hitachi/Siemens) |
| **2028-2030** | **EUV tooling (ASML)** | Tool output capped at ~70-100/yr; supply chain (Carl Zeiss, Cymer) physically can't ramp faster | **[[ASML]]** — but it has not historically taken margin; pricing power is theoretical, not realized |
| **2030+** | **Labor + modularization** | Need to build hundreds of GW per year; 5,000 workers per 1.2 GW data center is the current ratio | Asian factory module assemblers (Foxconn, Korean ODMs); electricians (wage inflation); **mech/electrical contractors** — see [[datacenter-construction]]: [[FIX]] / [[EME]] / [[PWR]] |

## Why the sequence matters for portfolios

**The bottleneck is where the capital accrues.** When CoWoS was tight in 2023, [[AMKR]]/[[ASX]] got pricing power. When power was tight in 2024, gas-turbine OEMs got 4+ year backlogs. **Right now (2026), memory is where the pricing pressure is** — and the supply response (new fabs) takes 2 years, which is why the crunch will get worse before it gets better.

**The next pivot (2027-2028) is from memory back to logic / equipment.** Investors who chased memory in 2025 should be thinking about *where the bottleneck moves next* — fabs being built will need [[KLAC]] / [[LRCX]] / Applied Materials tools to fill them.

**The 2028-2030 binding constraint is ASML.** Theoretically the steepest pricing power of the decade — but Dylan's important nuance: **ASML has historically NOT taken margin commensurate with its monopoly position.** Carl Zeiss + Cymer are physically constrained, not commercially constrained. Whether ASML *finally* takes price is the single biggest "unknown unknown" of the 2028-2030 trade.

## The 2028-2030 EUV math (anchor numbers)

- ASML EUV output: ~**70 tools/yr now → 80 next year → ~100 by 2030** (aggressive case)
- Cumulative tools by EOD: **~700**
- 1 GW of AI capacity = ~**3.5 EUV tools' worth** of fab time
- 700 tools / 3.5 = **~200 GW/year of theoretical AI capacity by EOD** if 100% allocated to AI
- Sam Altman wants 52 GW/yr → 25% share is plausible
- Elon wants 100 GW/yr → 50% share is implausible
- Tool cost: **$300-400M** each
- $50B of data center CapEx per GW vs. only **$1.2B of EUV tooling** per GW → enormous leverage

## Sub-bottleneck: memory bandwidth (always-on within compute) — NEW 2026-05-16

Per Horace He (Meta PyTorch Compilers) — see [[2026-05-16-horace-he-ml-systems]]:

- On BERT-class workloads, **matmuls = 99.8% of FLOPs but only 61% of runtime**. The remaining 39% of runtime is non-matmul operations doing 0.2% of FLOPs — *almost entirely memory-bandwidth bound*.
- Horace: operator fusion is "by far the most important optimization in a deep learning compiler" — because the entire point is to avoid round-trips between SRAM and VRAM.
- A100 hardware ratio: ~15× cliff between matmul (1000 TFLOPS TF32) and non-matmul (67 TFLOPS FP32) compute.

**Which means:** the [[MU]] HBM thesis isn't just a 2025-2026 cycle — *every* compute generation runs into the same data-shuffling wall, which is why HBM density and bandwidth keep scaling alongside FLOPs. The structural reason memory is a perennial bottleneck (not a one-cycle event) is the architecture of GPUs themselves. HBM4 → HBM4E → HBM5 cadence isn't optional; without it, the next NVDA chip generation suffocates on its own matmul throughput.

**Cross-cycle note for robotics:** Sergey Levine ([[2026-05-16-sergey-levine-physical-intelligence]]) makes the same memory point in a different domain — π0 has only 1 second of visual context vs. human "hours to decades." Scaling robot context length requires the same memory hierarchy improvements that AI training does. Same vendors, same demand vector.

## What's NOT a bottleneck (per Dylan)

- **Power.** 16+ vendors of gas-power generation; aeroderivatives, reciprocating engines, ship engines, fuel cells, solar+battery. Behind-the-meter could be ~50% of new capacity by EOD. Could unlock 20% of US grid (~200 GW) just with peak-shaving batteries. Cost spread (combined-cycle $1,500/kW vs. alternatives $3,500/kW) translates to **only +10c/hr on a $1.40/hr Hopper TCO** — easy to absorb.
- **Land / permitting.** Texas, Wyoming, New Mexico solve it. Australia/Malaysia/Indonesia/India also building.
- **Networking switches** — within the constraint of optical/CPO suppliers but not the gate-keeping constraint.
- **GPUs themselves** (within the chip-supply ceiling) — Nvidia is making "X-1" but it's still huge.

## What this means for the wiki's stance

| Implication | Affected page |
|---|---|
| ASML → upgrade conviction over multi-year horizon | [[ASML]] |
| MU → add the consumer-destruction mechanism (smartphone volumes 1.4B → 500-600M is the *engine* that releases memory to AI) | [[MU]] |
| Power names ([[VRT]], [[ETN]], [[NVTS]]) — still bullish on growth, but **temper the "binding constraint" framing** | [[VRT]], [[ETN]], [[NVTS]] |
| AAPL → bear case strengthens (TSMC deprioritization + memory squeeze halves smartphone volumes) | [[AAPL]] |
| Equipment beneficiaries pivot from memory back to logic in 2027-2028 | [[KLAC]], [[LRCX]], [[AMAT]], [[TER]] |
| **Fab construction is the 2027 sweet spot** | [[AMAT]] (>50% of HBM equipment value), [[ENTG]] (FOUPs / materials), [[APD]] (industrial gases via 15-20 yr BOO contracts) |

## Open questions
- Does ASML *finally* take pricing power in 2028-2030, or remain the "generous monopolist"?
- Does 3D DRAM (late decade) collapse the EUV bottleneck on the memory side?
- Does China indigenize DUV by 2030 → is there a non-ASML path to scale at lagging nodes?
- What is the price elasticity at which AI labs *would* destroy demand? (Dylan: probably never, given token monetization)

## The parallel: Robotics bottleneck roadmap (NEW 2026-05-13)

The same time-sequenced bottleneck framework applies to the humanoid robotics buildout, offset by ~2 years. See [[robotics]] for the full sector primer.

| Period | Binding constraint | Why | Beneficiaries (pricing power) |
|---|---|---|---|
| **2026** | **Rare-earth NdFeB processing** | China controls ~90% of downstream processing; per-humanoid magnet content runs ~10x that of a passenger EV; no synthetic substitute at the required torque density | **[[MP]]** (only fully integrated US NdFeB producer), USAR, UUUU |
| **2027** | **Precision sensors + harmonic drives** | Force-torque sensing requires sub-Newton precision; harmonic drives dominated by Leader Drive (China) and Harmonic Drive Systems (Japan); Western alternatives subscale | [[OUST]] (lidar + stereo cameras), [[ALGM]] (magnetic position/current sensors), [[VPG]] (force-torque pure-play but valuation stretched) |
| **2027-2028** | **Edge AI inference SoCs** | Control loops need sub-10ms inference at single-digit-watt power; different stack than autonomous-driving compute | [[AMBA]] (vision SoCs), CEVA (DSP/NPU IP licensing), LSCC (low-power FPGAs for sensor fusion) |
| **2028-2030** | **Scaled actuator + battery manufacturing** | Chinese supply chain (Sanhua, Leader Drive, Inovance) is unavoidable; most are PRC-listed and inaccessible to Western retail without Stock Connect | Hard to play directly from Western markets — see [[humanoid-oems]] for OEM-side framing |

> **What this means:** Robotics has its own bottleneck cycle running 2-3 years behind AI's. Today, the constraint is rare-earth magnets — exactly the same "the supplier no one can substitute" pattern that made packaging (CoWoS) the 2023 trade and memory (HBM) the 2025-26 trade. The harvest is 2028-2030.

### The model + data layer (NEW 2026-05-16 per [[2026-05-16-jim-fan-nvda-robotics]])

The previous version of this roadmap covered only the **physical** bottlenecks (rare-earths → sensors → SoCs → actuators). Per Jim Fan (NVIDIA Robotics chief scientist), there's an upstream **model + data layer** that constrains the entire physical buildout:

| Period | Constraint | Why | Beneficiaries (pricing power) |
|---|---|---|---|
| **2024-2026** | **VLA pre-training data (egocentric video)** | Scaling laws now established for dexterity (clean log-linear; mirror of LLM 2018 moment). 10M+ hours/year of egocentric data needed. iPhone-scale data ingestion is the FSD-equivalent moment. | [[NVDA]] (Cosmos, Dream Zero, EgoScale, Dream Dojo); [[AAPL]] (iPhone as pocket world scanner — second-order optionality) |
| **2026-2027** | **World Action Model architecture (WAM)** | VLA → WAM paradigm shift; Dream Zero is first commercial example. Open-source diffusion (V3, Sora) provides pre-training backbone; closed-source action heads provide moat. | [[NVDA]] dominates; competitive landscape: Pi (Physical Intelligence) + Sunday + Groot (legacy VLA) — all venture-stage, not investable on public markets |
| **2027-2029** | **Neural simulator compute** | Dream Dojo-style learned simulators replace physics engines. Massively parallel RL across millions of environments. "Compute = environment = data." | [[NVDA]] GPU demand from robotics RL parallels AI training demand; second-order pull on [[VRT]] / [[ETN]] data center infrastructure |

**Why this matters for the physical bottleneck cohort:** the **dexterity scaling law** anchors the commercial timeline. If model improvements follow the same log-linear curve LLMs did 2018-2024, **humanoid robots cross the physical Turing test in 2028-2029** (Fan's prediction, ~15% discounted for self-promotional bias). Component supply chains need to be ready BEFORE that — meaning today's bottleneck names ([[MP]] / [[ALGM]] / [[VPG]] / [[ALNT]]) are paying their dues during the model-layer maturation NOW.

**The full cascade:** model layer (2024-2027 NVIDIA) → physical bottlenecks (2026-2030 component cohort) → OEM deployment (2028-2032) → mass commercial (2030+).

### Why both roadmaps reinforce each other (cross-cycle dynamic)
- **Power and grid:** the 2027 transformer / substation constraint applies to BOTH AI data centers AND robotics manufacturing facilities — [[GEV]] / Hitachi / Siemens benefit from both demand pulls
- **Edge inference vs. cloud inference:** robotics demands a different compute stack (low-latency, low-power, on-device) — this pulls volume away from [[NVDA]]'s data-center business toward smaller-cap NPU/FPGA players ([[AMBA]], LSCC, CEVA) — slight bear data point for NVDA's TAM dominance over very long timelines
- **Skilled labor (2030+):** the [[datacenter-construction]] labor bottleneck applies to both AI data centers and robotics manufacturing facilities — same union electricians, same wage inflation

## Related
[[ai-capex-cycle]] · [[ai-bubble-debate]] · [[nvda-supply-chain]] · [[datacenter-construction]] · [[robotics]] · [[humanoid-oems]] · [[semiconductors]] · [[ASML]] · [[AMAT]] · [[TER]] · [[ENTG]] · [[APD]] · [[MU]] · [[KLAC]] · [[LRCX]] · [[AMKR]] · [[VRT]] · [[ETN]] · [[FIX]] · [[EME]] · [[PWR]] · [[MP]] · [[OUST]] · [[ALGM]] · [[VPG]] · [[AMBA]] · [[overview]]

## Sources
1. [[2026-05-09-dwarkesh-dylan-semianalysis]] — primary source for the AI bottleneck synthesis
2. [[2026-05-13-x-stack-map-humanoid-robotics]] — primary source for the robotics bottleneck extension
3. [[2026-05-16-jim-fan-nvda-robotics]] — model + data layer extension; WAM paradigm; dexterity scaling law; 2040 endgame framing
4. [[2026-05-16-horace-he-ml-systems]] — memory-bandwidth sub-bottleneck; matmul/non-matmul 15× cliff; FP4 precision lever
5. [[2026-05-16-sergey-levine-physical-intelligence]] — robot-context memory parallel; "robotics is software AND industrial" reinforcement
