---
type: theme
tags: [ai, supply-chain, bottlenecks, semianalysis, robotics, wam]
last_updated: 2026-06-20
last_full_review: 2026-05-09
sources: 12
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
| **2025-2026** | **x86 CPUs (parallel constraint)** | AI-driven Xeon scarcity is squeezing every Intel + AMD non-AI CPU; Intel "internal supply constraints" persist through 2026 per Q1 10-Q; **server ASPs +27% YoY but unit volumes -5%**; both Intel + AMD raised prices 10-15% in Apr 2026 | **[[AMD]]** (Q1 2026 +38% YoY revenue vs [[INTC]] +7%); **[[ARM]]** (cross-cycle royalty beneficiary as hyperscalers accelerate custom Arm-based server CPUs to bypass x86 shortage). Per [[2026-05-17-semiwiki-cpu-shortage-intel-18a]] |
| **2027** | **Cleanroom space (fabs) + transformers** | Memory makers + foundries didn't build new fabs through the 2023 trough; takes 2 years to build a fab. **NEW:** transformers (medium/high-voltage substation gear) are emerging as a parallel grid-side bottleneck — [[GEV]] consolidated control via $5.3B Prolec buyout Feb 2026. | TSMC, Micron + foundry equipment ([[KLAC]], [[LRCX]], [[AMAT]], [[TER]]) + fab consumables ([[ENTG]]) + industrial gases ([[APD]] — multi-decade BOO contracts kick in 2028-2030) + transformer makers ([[GEV]]/Hitachi/Siemens) |
| **2026-2028** | **Photonic substrates (Photonics-SOI, passive layer)** | CPO transition (NVDA Spectrum-X/Quantum-X launched 2025; AVGO Davisson, MRVL Celestial in pipeline) requires photonics-grade SOI wafers; sole qualified volume supplier at TSMC/GF/Tower | **[[SOITEC]]** (SOI.PA, Paris-listed) — Smart Cut patent moat (3,500+ patents); only Photonics-SOI is currently capacity-constrained, not all SOI segments |
| **2026-2028** | **InP substrates (active laser-source layer, NEW 2026-05-17 PM)** | Silicon is indirect-bandgap; can't emit light. Every CPO engine + transceiver needs an InP-based laser source (CW / DFB / EML). Goldman: 800G >34M units + 1.6T >25M units in 2026 — all require InP laser chips | **[[AXTI]]** (~36% global share; US-listed pure-play; ~$700M cap; +600% YTD; 100% China-mfg binary), Sumitomo Electric (~42%, ADR SMTOY conglomerate-diluted), JX Nippon (~13%, not separately tradeable) |
| **2026-2028** | **ABF substrates (advanced IC packaging, NEW 2026-05-17 PM)** | Ajinomoto Build-up Film is the dielectric layer in every advanced AI chip substrate (NVDA Blackwell/Rubin, AMD MI series, custom ASICs). **Top-tier AI accelerators use 15-18x more ABF than ordinary PC substrates.** Supply shortfall projected 10% H2 2026 → 21% 2027 → **42% in 2028**. **NVDA CoWoP architecture (late 2026) targets ABF substrates directly.** Taiwan media expects NVDA to lock up capacity via LTAs/prepayments/equity investments (pattern matches NVDA's COHR/LITE/GLW/NBIS/SNPS/NOK playbook). Ajinomoto **raising film prices 30% effective Q3 2026** — first major price action in years | **Film monopolist:** **[[AJINY]]** (Ajinomoto, 2802.T / AJINY ADR) — 95%+ ABF film share. **Substrate makers**: **[[IBDXY]]** (Ibiden, 4062.T / IBDXY ADR — 80%+ NVDA exposure; ¥500B FY26-28 capex; **highest NVDA-leverage stock outside NVDA itself**), **[[UNIMICRON]]** (3037.TW, ~25% share, Taiwan-only no ADR), **[[SSEHY]]** (Samsung Electro-Mechanics, 009150.KS / SSEHY ADR — **NVDA Groq3 LPU first vendor + AMD partner**, the rising challenger), **[[ATSAY]]** (AT&S, AT.VI / ATSAY ADR — only Western pure-play, AMD-primary). Top 5 substrate makers = ~70-74% combined. Shinko Electric privatized June 2025 (JIC/DNP/Mitsui consortium) — no longer publicly tradable |
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
- **Buyer-side confirmation (NEW 2026-06-20):** OpenAI's head of industrial compute Sachin Katti, asked for the single biggest unsolved infra problem, said fab capacity across logic + memory — then drilled to the root: *"if you dig down even deeper, it's ASML. For all of these you need ASML machines. That is the single choke point of the whole supply chain."* Per [[2026-06-20-katti-stanford-ai-supercycle]]. **Which means** the EUV-as-binding-constraint thesis is now stated by the person literally orchestrating OpenAI's gigawatt buildout, not just by analysts — a second independent, high-credibility confirmation of the anchor math above. See [[ASML]].

## Dylan Patel update: memory 2-3x and TSMC $100B 2028 capex (NEW 2026-05-17)

Per [[2026-05-16-dylan-patel-invest-like-best]] (Dylan's second deep podcast in a week — Invest Like the Best, mid-May 2026), two anchor numbers sharpen the memory + fab sequence on this page:

**1. DRAM pricing structurally 2-3x where it was**
> *"You can't make HBM with [non-extreme UV] tools. So the only way you make HBM is taking down DRAM capacity to convert it to HBM, which has been happening for the last two years, but the demand for DRAM keeps growing… So a lot of DRAM has been left to make HBM — that's part of why DRAM pricing has been 2-3x where it was."*

This *sharpens* the existing 2025-2026 memory-bottleneck row: it's not just HBM tightness anymore — **conventional DRAM is structurally re-priced** because the wafer-conversion math is one-way (you can't quickly re-allocate back to commodity DRAM). Reinforces [[MU]] medium-term thesis well beyond the HBM4 ramp.

**2. TSMC 2028 capex could approach $100B**
> *"TSMC's capex is increasing massively. It's like 56 billion this year. Wei said it'd go up next year. By 2028, the numbers I'm running, it's nearing 100 billion of capex from TSMC alone — almost as much as Nvidia is spending."*

This is the **single biggest upward revision** to the 2027 cleanroom-space bottleneck row. Prior wiki framing assumed TSMC capex flattening at the $55-65B range; Dylan's projection implies a 70-80% increase. Direct read-through:
- **[[KLAC]] / [[LRCX]] / [[AMAT]] / [[TER]]** addressable spend ~doubles vs. prior baseline
- **[[ENTG]] / [[APD]]** (fab consumables + industrial gases) — 15-20 yr BOO contracts capture the upside
- **[[TSM]] capex intensity** shifts from "high but stable" to "structurally rising for 3+ years"
- **Why TSMC can afford it**: per Dylan, "in five years TSMC will have a 100 billion dollar a year free cash flow business" — capex funded out of operating cash flow, not balance sheet stress

**Independent corroboration from SemiWiki (Daniel Nenni, May 15) — see [[2026-05-15-semiwiki-tsmc-tool-orders-capex]]:**
- TSMC Q1 2026 board capital appropriations: **$31.3B**, of which **$21.0B is Advanced Node equipment — the highest single-quarter authorization since tracking began Q4 2019**
- **Trailing-twelve-month Advanced Node equipment approvals ≈ $55B**, nearly consuming TSMC's full 2026 $56B CapEx guide
- Nenni's verdict: *"TSMC's current 2026 CapEx framework is already becoming too conservative"* — 2Q26 earnings (July 2026) upward revision probability "increasing"
- **Which means** Dylan's qualitative "$100B by 2028" projection has now been independently corroborated with hard tooling-order data from a different source class (industry insider vs. supply-chain analyst). The 2027 cleanroom-space bottleneck row is now backed by *measurable* equipment order flow, not just narrative.

**3. Independent supply-chain sold-out list (confirms multiple bottleneck rows)**
> *"It's even like a PCB to make a PCB requires copper foil and that copper foil is sold out and people are making prepayments for it… [Glass fibers] are completely sold out. Anything and everything that has a pulse and is sold out."*

Dylan's enumerated "sold out" list maps directly onto this page's bottleneck rows:
| Sold out (per Dylan) | Wiki row |
|---|---|
| HBM / DRAM | 2025-2026 |
| TSMC packaging | 2026-2027 |
| ASML EUV | 2028-2030 |
| Glass fiber substrates | 2027 (fab consumables) |
| **Copper foil for PCBs** | [[copper-thesis]] (independent confirmation) |

**Which means:** the wiki's bottleneck sequence has now been independently validated by Dylan in two separate appearances (this one + [[2026-05-09-dwarkesh-dylan-semianalysis]]) within 2 weeks. The numbers are sharpening upward, not downward. The 2027-2028 fab-equipment trade window is **wider** than this page previously implied.

## Sub-bottleneck: memory bandwidth (always-on within compute) — NEW 2026-05-16

Per Horace He (Meta PyTorch Compilers) — see [[2026-05-16-horace-he-ml-systems]]:

- On BERT-class workloads, **matmuls = 99.8% of FLOPs but only 61% of runtime**. The remaining 39% of runtime is non-matmul operations doing 0.2% of FLOPs — *almost entirely memory-bandwidth bound*.
- Horace: operator fusion is "by far the most important optimization in a deep learning compiler" — because the entire point is to avoid round-trips between SRAM and VRAM.
- A100 hardware ratio: ~15× cliff between matmul (1000 TFLOPS TF32) and non-matmul (67 TFLOPS FP32) compute.

**Which means:** the [[MU]] HBM thesis isn't just a 2025-2026 cycle — *every* compute generation runs into the same data-shuffling wall, which is why HBM density and bandwidth keep scaling alongside FLOPs. The structural reason memory is a perennial bottleneck (not a one-cycle event) is the architecture of GPUs themselves. HBM4 → HBM4E → HBM5 cadence isn't optional; without it, the next NVDA chip generation suffocates on its own matmul throughput.

**Cross-cycle note for robotics:** Sergey Levine ([[2026-05-16-sergey-levine-physical-intelligence]]) makes the same memory point in a different domain — π0 has only 1 second of visual context vs. human "hours to decades." Scaling robot context length requires the same memory hierarchy improvements that AI training does. Same vendors, same demand vector.

## Sub-bottleneck: advanced-packaging signoff is getting harder as packages get bigger (NEW 2026-06-19)

Per [[2026-06-19-semiwiki-asml-china-wsts-tsmc-troll-intel-pdf]] (the "Warpage-to-Impedance Causality Matrix," Dr. Moh Kolbehdari): in large AI packages — chiplets, HBM stacks, glass substrates, bridges, interposers, CoWoS/CoPoS, 2.5D/3D — substrate **warpage of just 50–100µm is no longer a purely mechanical pass/fail item**. That deformation perturbs impedance, return-current continuity, SI/PI margin, PDN resonance and thermal-current behavior — so mechanical stress "behaves like electrical noise," and signoff has to couple mechanical + electrical + thermal + reliability rather than clear each in its own silo. **Which means**: as packages scale up (the whole point of [[advanced-packaging|advanced packaging]] when transistor shrink stalls), the *integration/signoff* problem compounds faster than the part count — a quiet moat-deepener for incumbents who already own the data and the flow ([[TSM]] CoWoS, [[AMKR]], the EDA + test layer) and a real barrier for would-be second sources trying to package marquee AI silicon. It rhymes with the [[INTC]] yield story (June 19): at the bleeding edge, both *yield* and *packaging signoff* now need specialist analytics that favor whoever has the most production data.

## Sub-bottleneck: CPUs + RL-environment compute (NEW 2026-06-20)

Per [[2026-06-20-dylan-patel-daytona-cpu-bottleneck]] (Dylan Patel × Daytona Compute Conference): **server CPUs are the third near-term binding constraint of the agentic era** — after GPUs (2023-24) and DRAM/HBM (2025-26). This *extends* the "2025-2026 x86 CPUs (parallel constraint)" row in the table above with a fresh driver and named, dated catalysts. The sequence now reads: GPU (23-24) → memory/HBM (25-26) → **CPU (26)** → cleanroom/fabs (27) → EUV/ASML (28-30).

- **Intel + AMD both "fully sold out," price-increase notices issued, "not even competing with each other anymore."** "Over the last 6 months the entire cloud market ran out of CPUs"; Amazon installing **3x YoY** CPU servers. Server-CPU margins (historically thin) "creeping up." [[2026-06-20-nopriors-127-dylan-patel]] adds the GitHub-instability anecdote (MSFT sold spare CPUs to OpenAI/Anthropic).
- **The driver is RL + agents, not traditional compute.** Two forces: (1) **RL-environment verifier loops** getting tighter (a single Daytona customer ran 1M vCPU workloads in 6 hours; physics/biology-sim verifiers ahead); (2) **long-horizon agents** (Codex working 6-7hr) hammering CPU for tool calls, sandboxes, scraping, DB calls. The GPU:CPU ratio is collapsing — "warm-pool" CPUs kept hot so expensive GPUs never idle waiting on a verifier = structurally more CPU per GPU. **Which means:** the agentic-task unit cost now has a rising vCPU line (read-through to [[inference-economics]]).
- **CPU silicon is fragmenting (gold-rush "even broken pickaxes sell").** Beneficiaries: [[AMD]] (EPYC sold out, server-share gains), [[INTC]] (Xeon sold out + foundry-of-last-resort for vendors kicked off TSMC N3 — but Dylan *tempers* the bull: "not saved," short-term/cyclical not structural), **[[ARM]] launching its own standalone CPU "in a few weeks" that Meta + Cloudflare will adopt** (IP-licensing → selling silicon directly — a business-model shift), [[AMZN]] Graviton (5-6 gens, +3x install), [[NVDA]] Vera (Grace successor, late-2026/early-2027). **Catalyst to watch: ARM standalone-CPU launch + Meta/Cloudflare confirmation (~mid-2026).**
- **NAND catching up to DRAM (update, not contradiction).** Dylan: DRAM "+4x last year and still rising"; **SSD/NAND now +3-4x with "another ~60% to go."** This is sharper NAND inflation than the 2026-05-09 Dwarkesh read (NAND rising *less* than DRAM); NAND lagged but is now catching up — bullish near-term [[SNDK]]/[[WDC]], reinforces the memory row above and the [[MU]] thesis.
- **TSMC node-allocation squeeze (cross-ref):** all AI accelerators are on N3 → TSMC telling Apple/Qualcomm/MediaTek to "get off 3nm, move to 2nm faster," pushing mobile/PC vendors toward Intel (non-AI-competing foundry). NVDA's Groq acquisition partly = Groq-on-Samsung (no TSMC N3 capacity). Reinforces the [[AAPL]]-deprioritization flag.

## Copper: the parallel commodity bottleneck (NEW 2026-05-16)

Per the new [[copper-thesis]] page: copper is the **2026-2035 structural commodity bottleneck** running in parallel to the chip-stack bottleneck cycle on this page. It has the same shape (binding constraint → pricing power) as ASML/EUV but in the physical-buildout layer.

| Period | Binding constraint | Why | Beneficiaries |
|---|---|---|---|
| **2026-2028** | Copper futures price | AI data centers (400-572kt by 2028 per BNEF) + EV/grid demand outpaces mine supply ramp | Futures (CPER); diversified miners ETF (COPX) |
| **2029-2035** | Refined copper supply | Goldman: demand outpaces supply from 2029. 15-20 yr permit cycles mean mines that don't break ground by ~2025 are too late | Existing tier-1 miners ([[TECK]], BHP, [[FCX]]); Anglo merger entity post-2026 |
| **2035+** | Refining + smelting | Even with new mine supply, refining capacity may bottleneck. Chinese share of refining = 50%+ | Western refiners with capacity (limited) |

**Smart-money positioning**: Druckenmiller (long futures via CPER-equivalent — see [[2026-05-16-druckenmiller-hard-lessons]]); Friedland (Ivanhoe, $15K/tonne thesis); Larry Fink (BlackRock); Goldman Sachs (2029+ deficit confirmed); Pierre Andurand.

**Why this matters for the wiki framework**: pricing power lives at the binding constraint. The wiki has captured this pattern in the *digital* stack (memory 2025-26 → fabs 2027 → EUV 2028-30). The *physical* stack — copper, rare earths, transformers — runs on a slightly later cycle but with even longer lead times because mining permits take 15-20 years vs. fab construction at 2-3 years. The two cycles compound rather than substitute.

## 🆕 MLCC layer — wiki coverage gap CLOSED 2026-05-29 → see [[mlcc]]

> **Coverage status (updated 2026-05-29 post-MLCC sector page open)**: full sector tracking now lives at [[mlcc]]. Below is the original DELL-print-surfaced framing; the dedicated sector page expands the investability framework.

Per [[2026-05-28-DELL-Q1-FY27-earnings]]: **each NVIDIA GB300 rack requires roughly 440,000 multilayer ceramic capacitors (MLCCs)** for power filtering and decoupling. Vera Rubin NVL72 is denser still. DELL's Q1 FY27 AI server revenue of $16.1B (+757% YoY) + $51.3B backlog implies billions of MLCCs/year from one OEM customer — and that's before counting [[HPE]] / [[SMCI]] / hyperscaler-direct ODM volumes.

**Why this is a wiki gap**: the MLCC layer has had zero dedicated coverage despite being a structural bottleneck. Supply is **Japanese-dominated** with very high concentration:

| Player | Listing | Wiki status | MLCC exposure |
|---|---|---|---|
| **Murata Manufacturing** | Japan (6981.T); US ADR MRAAY | NOT covered | ~40% global share; world's largest MLCC supplier |
| **TDK Corp** | Japan (6762.T); US ADR TTDKY | NOT covered | Large diversified electronics; MLCC + battery + sensor |
| **Samsung Electro-Mechanics** | Korea (009150.KS); US ADR [[SSEHY]] | **Covered for ABF substrates — DUAL-EXPOSED to MLCC** | Material global share; the under-priced single name |
| **Taiyo Yuden** | Japan (6976.T) | NOT covered | Pure-play MLCC; smaller scale |
| **Yageo** | Taiwan (2327.TW); KEMET acquired Q3 2020 | NOT covered | Growing global share; western channel via KEMET |

**Verdict**: Open dedicated MLCC coverage as a future expansion. [[SSEHY]] dual exposure is the most-leveraged existing wiki name (already bull/medium-high for ABF; the MLCC angle adds optionality without requiring a new position).

## What's NOT a bottleneck (per Dylan)

- **Power.** 16+ vendors of gas-power generation; aeroderivatives, reciprocating engines, ship engines, fuel cells, solar+battery. Behind-the-meter could be ~50% of new capacity by EOD. Could unlock 20% of US grid (~200 GW) just with peak-shaving batteries. Cost spread (combined-cycle $1,500/kW vs. alternatives $3,500/kW) translates to **only +10c/hr on a $1.40/hr Hopper TCO** — easy to absorb.
- **Land / permitting.** Texas, Wyoming, New Mexico solve it. Australia/Malaysia/Indonesia/India also building.
- **Networking switches** — within the constraint of optical/CPO suppliers but not the gate-keeping constraint.
- **GPUs themselves** (within the chip-supply ceiling) — Nvidia is making "X-1" but it's still huge.

## 🆕 Baker: "the bottleneck trade is nearing its end" (2026-06-16)

Gavin Baker (Atreides — a source this wiki weights heavily): *"The bottleneck trade is nearing its end. That was the game for the last year. The next game is what has enduring franchise value on the other side of these bottlenecks, whenever that is."* ([[2026-06-16-baker-bottleneck-rotation-boj-hike]])

This is the cyclical-vs-secular distinction applied to the whole roadmap above. Bottleneck rents are self-liquidating by construction — the same scarcity that creates the rent funds the capex that ends it. The signal that the Street is late, not early: cyclical rents getting *secular* multiples ([[MU]] valued as "infrastructure not commodity"; [[AAOI]] ~14x fwd sales as a CPO-disruptable module maker).

**The actionable split** the roadmap now overlays on every layer — within the bottleneck basket, separate:
- **Durable franchise that is *also* bottlenecked** (keeps pricing power after supply catches up): [[TSM]] (process + capacity discipline + lock-in), [[ASML]] (EUV monopoly), [[MU]]'s **HBM** franchise specifically (vs commodity DRAM).
- **Pure cyclical rent-capturer** (owns nothing on the other side): [[AAOI]], AXT, commodity DRAM/NAND, pluggable optical modules.
- **The open question — [[NVDA]]:** CUDA + systems + pace = durable franchise, or is NVDA *itself* the bottleneck (GPU scarcity) that compresses as ASICs + the Intel-foundry diversification arrive?

**Live confirmation, same day:** June 16's BoJ-hike/Fed-eve session routed the supply-side book ([[MRVL]] −9.8%, [[ALAB]] −7.1%, [[MU]] −6.2%, [[AVGO]] −4.4%, [[TSM]] −3.5%) while demand-side/franchise/value held ([[GOOGL]] +1.1%, Dow record). One day isn't a trend — but it's the rotation in miniature.

**The hedge that governs timing — "whenever that is":** the wiki's own demand-underestimation evidence (HBM sold out to 2027-28, GPU rental booked out, Dylan's "everyone's building X-1") argues *against* being early. The price peak front-runs the fundamental resolution by quarters. **This is a framework to start tilting, not a switch to flip.** The tell that the rotation has actually begun: memory contract prices decelerating, CoWoS lead times shrinking, or a first hyperscaler capex guide-down. Also tensions the newsletter ledger's `2026-06-01-supply-over-demand` call directly.

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
[[ai-capex-cycle]] · [[ai-bubble-debate]] · [[nvda-supply-chain]] · [[datacenter-construction]] · [[robotics]] · [[humanoid-oems]] · [[semiconductors]] · [[ASML]] · [[AMAT]] · [[TER]] · [[ENTG]] · [[APD]] · [[MU]] · [[KLAC]] · [[LRCX]] · [[AMKR]] · [[SOITEC]] · [[VRT]] · [[ETN]] · [[FIX]] · [[EME]] · [[PWR]] · [[MP]] · [[OUST]] · [[ALGM]] · [[VPG]] · [[AMBA]] · [[overview]]

## Sources
1. [[2026-05-09-dwarkesh-dylan-semianalysis]] — primary source for the AI bottleneck synthesis
2. [[2026-05-13-x-stack-map-humanoid-robotics]] — primary source for the robotics bottleneck extension
3. [[2026-05-16-jim-fan-nvda-robotics]] — model + data layer extension; WAM paradigm; dexterity scaling law; 2040 endgame framing
4. [[2026-05-16-horace-he-ml-systems]] — memory-bandwidth sub-bottleneck; matmul/non-matmul 15× cliff; FP4 precision lever
5. [[2026-05-16-sergey-levine-physical-intelligence]] — robot-context memory parallel; "robotics is software AND industrial" reinforcement
6. [[2026-05-16-dylan-patel-invest-like-best]] — DRAM 2-3x pricing, TSMC 2028 ~$100B capex, supply-chain sold-out enumeration (added 2026-05-17)
7. [[2026-05-15-semiwiki-tsmc-tool-orders-capex]] — Daniel Nenni / SemiWiki: TSMC Q1 2026 board appropriations $31.3B with record $21B Advanced Node equipment line; TTM equipment orders forcing upward CapEx guide revision (added 2026-05-17)
8. [[2026-05-17-semiwiki-cpu-shortage-intel-18a]] — AI-driven x86 CPU shortage row added; INTC Q1 10-Q quoted; AMD vs Intel relative growth (added 2026-05-17)
9. [[2026-06-20-katti-stanford-ai-supercycle]] — OpenAI compute chief confirms ASML as "the single choke point of the whole supply chain"; memory architecture as the medium/long-term frontier (added 2026-06-20)
10. [[2026-06-20-dylan-patel-daytona-cpu-bottleneck]] — NEW server-CPU bottleneck (RL-environment verifiers + long-horizon agents); Intel/AMD sold out; ARM standalone CPU (Meta/Cloudflare); NAND catching DRAM; TSMC N3 squeeze (added 2026-06-20)
11. [[2026-06-20-nopriors-127-dylan-patel]] — multi-bottleneck confirmation; GitHub-instability/CPU-reallocation anecdote; GE turbine 4-8yr backlog; labor/electrician constraint (added 2026-06-20)
