---
date: 2026-06-17
type: forum
publisher: SemiWiki (+ BusinessWire, T. Rowe Price, Twitter leak)
url: https://semiwiki.com/forum/threads/25321
raw_path: n/a (semiwiki_scan.py incremental sweep)
touches: [TSM, AMKR, INTC, SNPS, photonics, semiconductors]
---

# SemiWiki daily sweep (9 new items): TSMC–Amkor 10-yr Arizona packaging pact, Intel 14A pitch leak, Synopsys multiphysics

## TL;DR
- **TSMC + Amkor sign a 10-year agreement** for TSMC to procure advanced packaging + test from Amkor in **Arizona** — the marquee external-OSAT validation the [[AMKR]] thesis was built on, and a US end-to-end (silicon → packaged/tested) supply-chain build.
- **Intel 14A pitch sizes leaked**: 14A (code 1280, G48H126, 28nm M0, 2028) and 14A2 (1280.1, G44H110, 21nm M0, 2030), with 14A2 moving from "backside-power-direct only" to a **dual-side** power/signal architecture — a concrete, net-new node-roadmap datapoint for [[INTC]].
- **Synopsys Multiphysics Fusion** unifies electrical/thermal/mechanical/optical (incl. **photonics**) analysis in one digital-twin — small but real [[SNPS]] + [[photonics]] datapoint as packaging/3DIC multiphysics goes mainstream.

## Key facts
- **TSMC–Amkor (BusinessWire, June 16):** 10-year agreement; TSMC procures advanced packaging + test services from Amkor in Arizona; both building in AZ (TSMC fabs + Amkor Peoria campus). Quotes from TSMC's Kevin Zhang ("long history… confident") and Amkor CEO Kevin Engel ("full U.S. supply chain from advanced silicon manufacturing to tested packaged devices"). No dollar figure or capacity number disclosed.
- **Intel 14A leak (Twitter, unverified):** 14A — code 1280, G48 (gate pitch 48nm) H126, M0 28nm, target 2028; 14A2 — code 1280.1, G44 H110, M0 21nm, target 2030. 14A = backside power "direct only" (nTSV power to transistors, frontside freed for signals); 14A2 = "dual side" (both sides carry power + signal + clock — higher density, better thermals, more complex). Ambitious if real.
- **Synopsys Multiphysics Fusion:** concurrent electrical/thermal/mechanical/EM analysis, shared data models, AI-assisted optimization; first wave targets advanced packaging, multi-die, **photonics**, thermal, reliability. Aimed at 2.5D/3D-IC where TSV/interposer/stacked-die interactions break siloed simulation.
- **PowerArtist RTL power → Keysight** ([[KEYS]]): shift-left RTL power estimation; cited wins — Intel 3% dynamic power via clock-gating, AMD 27% dynamic / 56% clock-gating on an IP, NVIDIA 3.5–4% net via RAM-access optimization.
- **Hot Chips 2026:** Aug 23–25, Stanford. Sessions flagged: HBM tutorial, RISC-V, advanced server CPUs, data-center AI GPUs, processing-in-memory, DC networking interconnects, custom hyperscaler training silicon.
- Lip-Bu Tan (Intel CEO) long-form interview on T. Rowe Price "The Long View" — transformation/AI-infra/supply-chain-resilience color, no hard datapoint.

## Key claims (and how confident)
- TSMC–Amkor is **structurally bullish for AMKR** and confirms the CoWoS-overflow-outsourcing thesis directly (high confidence — primary BusinessWire release; both named CEOs). It also de-risks the geographic-bottleneck concern (Taiwan-only packaging) the wiki has flagged.
- The Intel 14A pitches are **unverified Twitter leak** — treat as roadmap color, not confirmed (low confidence on the exact numbers; directionally consistent with Intel's published 14A/2028 cadence and backside-power direction).
- Multiphysics/photonics tooling is a slow-burn structural tailwind for EDA, not a near-term revenue mover (medium confidence).

## Wiki updates made
- Added Recent-developments bullet to [[TSM]] (TSMC–Amkor AZ packaging pact).
- Created Recent-developments section + bullet on [[AMKR]] (first source ingest, thesis-confirming).
- Added Recent-developments bullet to [[INTC]] (14A/14A2 pitch leak).
- Added datapoint to [[photonics]] (Synopsys multiphysics incl. photonics).
- Index + log updated.
