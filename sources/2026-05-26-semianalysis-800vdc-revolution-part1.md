---
date: 2026-05-26
type: report
publisher: SemiAnalysis
url: https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part
raw_path: n/a (web-fetched; partially paywalled)
touches: [VRT, NVTS, MPWR, ON, ai-capex-cycle, datacenter-construction]
---

# Inside the 800VDC Revolution – Part 1 (SemiAnalysis, May 26 2026)

## TL;DR
- As AI racks push past ~600kW, 48-54V DC distribution breaks down (too much copper, current, conversion loss). Moving to **800VDC** cuts current ~15× and resistive losses ~219× (54V→800V), enabling denser, cheaper, more efficient power delivery — SemiAnalysis frames it as a physics-and-economics-driven *inevitable* architecture shift.
- Two new product categories emerge: **Power Rack / Sidecar Units** (TAM peaks ~$11B in 2028) and **Solid-State Transformers (SST)** (TAM ~$13B headline / ~$32B in deeper figure by 2030); ~39GW of incremental 800VDC capacity by 2030.
- Four-phase migration 2026→post-2029, from white-space retrofit to a full facility-level SST end-state. Winners = power-electronics/SST/SiC vendors; **losers = traditional central-UPS and AC-distribution vendors** (Schneider, Eaton, *and Vertiv* are named as losing the central-UPS role as it gets disaggregated). Part 2 covers the power-semiconductor layer.

## Key facts (with confidence)
- **High confidence (public portion):**
  - Current reduction 15× (54V→800V), 16.7× (48V→800V); resistive loss reduction 219× (54V baseline), 278× (48V baseline).
  - Rack power: Kyber Ultra ~660kW; Vera Rubin NVL72 ~180-220kW (Phase 1/2); target 600-800kW (Phase 2/3).
  - TAM: Sidecar/power-rack peaks ~$11B (2028); SST ~$13B headline (by 2030) — a deeper figure cites SST ~$32B by 2030 (note the discrepancy; cite the lower/headline number unless modeling). ~39GW incremental 800VDC capacity by 2030.
  - Content $/MW: power rack ~$400-500k/MW; battery rack ~$200k/MW; SST $1.0-1.5M/MW.
  - Cumulative efficiency: AC baseline 82.0% → Phase1 83.7% → Phase2 86.5% → Phase3 86.9% → Phase4 87.4%; ~50-69MW continuous grid savings at 1GW scale.
  - Topology options: 800V monopolar vs ±400V bipolar.
- **Medium confidence (named in public portion; winner/loser ranking is behind paywall):**
  - Beneficiaries named: Infineon (BBU, SiC MOSFETs, SST), Wolfspeed (10kV SiC), Delta, Advanced Energy, TE Connectivity (busbars), Legrand, Danfoss, ABB; startups DG Matrix (ABB-backed, Infineon partner), Amperesand, Heron Power, Novos, Aran, VIOX.
  - Disrupted: central-UPS vendors (Schneider, Eaton, **Vertiv**) lose the centralized LV-UPS role by Phase 3; LV transformers / AC switchboards / AC floor PDUs eliminated; conventional iron-core transformers replaced by SSTs.
- **Dated catalysts:** DG Matrix SST UL cert targeted end-Q2 2026; OCP standards targeting end-2026; NEC 2029 partial 800VDC code support (full ~2032-35); NERC Essential Actions Alert issued May 2026.

## Key claims (and how confident)
- 800VDC is "inevitable" above ~600kW racks — strong physics argument (loss scales with current², voltage↑ → current↓), high confidence on direction; timing/phase split is SemiAnalysis's model.
- Migration phases: P1 (2026-27) white-space retrofit (Google/Meta early, sidecar AC→800VDC); P2 (2027-28) 800VDC-native compute (Kyber, Vera Rubin Ultra) makes sidecar *mandatory*; P3 (late-28/29) facility-level 800VDC + central UPS eliminated; P4 (>2029) SST end-state, direct MV→800VDC.
- Notable bear-for-Vertiv signal: the *central* UPS box is disaggregated/disintermediated; whether VRT recaptures value via row-level BBU/battery racks + cooling is the open question (likely the crux of the paywalled winner/loser section).

## Quotes worth keeping
> "Behind paywall we will now discuss the main winners and losers of the 800VDC revolution, and who is better positioned to be benefited from the transition."

(Public text emphasizes that raising distribution voltage from 54V to 800V at 600kW racks "reduces current by ~15× and resistive conductor losses by ~219×.")

## Bias / access notes
- **Bias:** SemiAnalysis is structurally bullish on the AI-infrastructure buildout; the TAM figures are their bottom-up model and carry an internal discrepancy (SST cited as both ~$13B and ~$32B by 2030 across sources — flag, don't average). The named-beneficiary list in the public portion skews toward power-electronics startups and merchant-silicon vendors; the *ranked* winner/loser call is paywalled, so the "Vertiv loses" read is directional, not their final verdict.
- **Paywall:** PARTIALLY PAYWALLED — ~60-70% public (physics, phases, TAM, named players); the explicit winners-vs-losers ranking is paid-only. **This matters:** the part most relevant to [[VRT]] (does Vertiv win or lose net?) is behind the wall.

## Wiki updates suggested (NOT made in this task)
- [[VRT]] — add a **contradiction / risk flag**: SemiAnalysis Part 1 lists Vertiv among central-UPS vendors that *lose* the centralized LV-UPS role by Phase 3 as power disaggregates to row-level. This is a partial counter to VRT's bull/high stance — surface both views per house rules. The open question (recapture via row-level battery racks + cooling) is paywalled. Add to "Bear case / risks" and Recent developments; do NOT change stance without the paywalled winner/loser section.
- [[NVTS]] / [[ON]] / [[MPWR]] — 800VDC shifts the power-semi BOM toward higher-voltage SiC/GaN and on-blade conversion; Part 2 ("the semiconductor revolution underneath it") is the direct power-semi read-through. Add a watch-item: Part 2 will name the silicon winners. (Note: this article's named power-semi beneficiaries are Infineon/Wolfspeed, not NVTS/MPWR/ON specifically — flag that the wiki's power-semi names aren't called out here; confirm in Part 2.)
- [[ai-capex-cycle]] — add the "power leg": 800VDC + SST is a ~$11B (sidecar) + ~$13-32B (SST) content category by 2028-30 atop ~39GW incremental capacity; another second-derivative beneficiary set of the AI capex cycle.
- [[datacenter-construction]] — add 800VDC migration phases and the elimination of AC switchgear / LV transformers / floor PDUs in Phase 3 as a structural change to electrical buildout.
- Consider a new theme page `wiki/themes/800vdc-power-architecture.md` if Part 2 + further sources warrant it (currently coverage lives inside [[VRT]]).
