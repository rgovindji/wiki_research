---
type: company
ticker: VRT
tags: [ai, power, cooling, data-center]
last_updated: 2026-06-01
last_full_review: 2026-05-09
sources: 2
conviction: high
stance: bull
---

# Vertiv (VRT)

**Stance:** bull · **Conviction:** high · **Time horizon:** long-term

## One-line thesis
The **only large player covering both power AND cooling** for AI data centers — Q1 2026 revenue **$2.65B (+30% YoY)** with a **$9.5B order backlog**. Power and thermal are the binding physical constraints on AI factory build-out.

## Role in the NVDA stack
- **UPS / PDU power infrastructure** for AI factories
- **Cooling systems** (liquid + air) for high-density GPU racks
- Part of NVIDIA's **800V DC power architecture** ecosystem alongside [[ETN]], ABB, Schneider, Infineon, [[STM]], Navitas
- Differentiated by single-vendor scope — covers both power AND cooling unlike most competitors

## Bull case
- **Q1 2026: $2.65B revenue (+30% YoY), $9.5B backlog**
- **Power + cooling combined** under one roof — uniquely positioned vs. pure-play power or cooling vendors
- **Fast delivery** has become a competitive moat in supply-constrained data center build-outs
- **AI factory unit economics** are increasingly limited by power/cooling — VRT is in the bottleneck
- **800V DC architecture transition** is a multi-year content tailwind
- **140 kW per rack is the new normal (NEW 2026-05-15).** Jane Street's Texas AI data center confirmed in a public facility tour: **140 kW per cabinet (14x traditional 10 kW density)**, liquid cooling with cold plates standard, retrofit of existing facility (suggests retrofit wave beyond greenfield). VRT covers both power distribution AND cooling — the only large vendor doing both — this is the single biggest density transition since modern DCs began, and every existing site needs to upgrade.

## Bear case / risks
- **Power is NOT going to be the binding AI constraint (NEW).** Per [[2026-05-09-dwarkesh-dylan-semianalysis]], power has **16+ vendors** of generation (combined-cycle, aeroderivatives, reciprocating engines, ship engines, fuel cells, solar+battery), and ~50% of new AI capacity by EOD will be behind-the-meter. Could unlock ~200 GW of US grid just with peak-shaving batteries. **Implication:** VRT keeps growing, but its *pricing-power* moat is bounded by power-side alternatives — the framing shifts from "scarcity" to "growth + execution."
- **AI capex cycle exposure** — slows hard if hyperscalers pause (see [[ai-capex-cycle]])
- **Premium multiple already paid** — much of the AI thesis priced in
- **Competition** — Eaton, Schneider, ABB are all formidable; BE/GEV/Siemens/Mitsubishi also serve adjacent power layers
- **Supply chain risk** — own components, copper, specialty cooling fluids
- **Order timing volatility** — can be lumpy quarter to quarter

## Key questions / what to watch
1. **Order book trajectory** — direction matters more than absolute level
2. **Backlog conversion** — how fast does $9.5B convert to revenue?
3. **800V DC product launches** and traction
4. **Operating margin** as scale builds
5. **Geographic / customer mix** disclosure

## Recent developments
- **🔥 2026-06-01 — GOOGL $80B raise + Berkshire $10B placement read-through:** Alphabet announced the largest equity raise in tech history ($30B underwritten + $40B ATM + $10B Berkshire private placement at $351.81 Class A / $348.20 Class C) explicitly to fund "AI compute infrastructure to meet unprecedented customer demand" — ~$50B is net-new AI capex above the prior $185-190B 2026 guide once the $30B RSU-tax mechanism is stripped out (see [[2026-06-01-googl-80B-equity-raise-berkshire]]). **Which means** [[VRT]] is at the front of the queue for GCP's incremental campus power + high-density cooling pull: every additional GCP hall built with TPU + NVDA Rubin racks at 140 kW/cabinet needs both UPS/PDU power distribution AND liquid cooling, and Vertiv is the only large vendor that covers both layers. The "unprecedented customer demand" wording (Anthropic 5 GW TPU + GCP backlog $460B) is a direct pull on VRT's $9.5B backlog conversion through 2027. Stance unchanged at bull / high. Watch: any explicit GCP design-win disclosure on Q2 print.
- **🔥 2026-05-28 — DELL Q1 FY27 print = direct liquid-cooling demand-side validation** (per [[2026-05-28-DELL-Q1-FY27-earnings]]). DELL AI server revenue $16.1B (+757% YoY); **$51.3B AI backlog**; FY27 guide raised 20% to $165-169B. **Read-through to VRT**: every DELL PowerEdge XE9812 (Vera Rubin NVL72) shipping at scale = liquid-cooling pull at the highest density tier — GB300 racks run ~135 kW/rack at air-cooling thermal limit; Vera Rubin NVL72 is even denser. **Which means** VRT's high-density cooling product mix is structurally pulled by DELL's $51.3B backlog ramp over the next 4-6 quarters. Per [[2026-05-29-dell-upstream-second-derivative]] synthesis: VRT is one of the three cleanest "DELL-upstream not yet rerated" plays (with [[MOD]] and [[NVT]] — Goldman May 17 basket cohort). Stance unchanged at bull. Watch: Q2 print + any explicit DELL-AI-Factory design win disclosure.
- **2026-05-13** — Feb 2026 detail surfaced: **$1B strategic acquisition** in high-density cooling solidified VRT's lead in GPU-cluster cooling. Market cap roughly **tripled since 2024**.
- **2026-05-07** — **Citi raised PT to $414 from $353**, Buy maintained. Citi: expects Vertiv to raise long-term organic growth outlook to **12-24% range**. Multi-year visibility to sales and earnings growth on AI-driven data center spending cited.

## Related
[[NVDA]] · [[nvda-supply-chain]] · [[ETN]] · [[GEV]] · [[BE]] · [[FLEX]] · [[NVTS]] · [[datacenter-construction]] · [[FIX]] · [[EME]] · [[ai-capex-cycle]] · [[bottleneck-roadmap]] · [[overview]]

## Sources
1. [[2026-05-09-dwarkesh-dylan-semianalysis]] — primary source for the "power is not the binding constraint" tempering note
2. [[2026-06-01-googl-80B-equity-raise-berkshire]] — GOOGL $80B equity raise + Berkshire $10B placement (added 2026-06-01)

## Citations
- damnang2 on AI datacenter power: https://damnang2.substack.com/p/ai-datacenter-power-investment-map
- Vertiv Frontiers 2026 Report: https://www.vertiv.com/48d902/globalassets/content---assets-2025/documents/vertiv-frontiers-2026-report-en-gl-web.pdf
- 24/7 Wall St on $1.4T data center electrification: https://247wallst.com/investing/2026/03/03/1-4-trillion-needed-for-ai-data-center-electrification-by-2030-chief-investment-officer/
- NVIDIA 800V HVDC architecture: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
