---
type: theme
tags: [ai, supply-chain, bottlenecks, semianalysis]
last_updated: 2026-05-09
last_full_review: 2026-05-09
sources: 1
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

## Related
[[ai-capex-cycle]] · [[ai-bubble-debate]] · [[nvda-supply-chain]] · [[datacenter-construction]] · [[semiconductors]] · [[ASML]] · [[AMAT]] · [[TER]] · [[ENTG]] · [[APD]] · [[MU]] · [[KLAC]] · [[LRCX]] · [[AMKR]] · [[VRT]] · [[ETN]] · [[FIX]] · [[EME]] · [[PWR]] · [[overview]]

## Sources
1. [[2026-05-09-dwarkesh-dylan-semianalysis]] — primary source for this synthesis
