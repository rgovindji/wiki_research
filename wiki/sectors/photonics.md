---
type: sector
tags: [photonics, silicon-photonics, cpo, optical-interconnect, pic, ai-infrastructure]
last_updated: 2026-06-23
last_full_review: 2026-06-14
sources: 6
conviction: medium
---

# Silicon Photonics & Optical Interconnect

## What this is
The layer of the AI stack that moves data with light instead of electrons. As compute scales, the bottleneck shifts from the chip to the **interconnect** — getting data between GPUs, between packages, and (eventually) between compute and memory — fast enough and at low enough power. Photonics is how that wall gets pushed back. This page is the investable sector view; the technical layer-by-layer map lives in [[2026-05-17-photonic-memory-stack]].

## Why it matters now
- **Optics is moving physically closer to compute.** The roadmap progression: pluggable transceivers → onboard optics → **linear-drive pluggable optics (LPO)** → **co-packaged optics (CPO)**. Each step removes electrical SerDes power and latency. CPO is the inflection that turns optical interconnect from an accessory into a structural part of the AI package. (Theme captured from SemiWiki "optics moving closer to compute" / STRL discussions, June 2026.)
- **AI interconnect is a power problem.** A large fraction of an AI rack's power goes to moving data, not computing on it. Optical interconnect is the lever on the one constraint — power — that gates how big data centers can get ([[ai-capex-cycle]] bottleneck has shifted to power).
- **PIC manufacturing is scaling out of the lab.** Photonic IC production is ramping across datacom, telecom, AI infrastructure, sensing, and quantum — driving demand for specialized manufacturing analytics and yield tooling ([[2026-06-10-semiwiki-photonics-pic-production]]).

## The roadmap (why timing matters)
| Stage | What it is | Status 2026 | Beneficiaries shift |
|---|---|---|---|
| Pluggable transceivers (800G / 1.6T) | Optics in a separate module | Shipping, the cash cow today | [[COHR]] · [[LITE]] · [[FN]] · [[AAOI]] |
| Linear-drive pluggable (LPO) | Drops the DSP/retimer; lower power | Early ramp | transceiver makers + ASIC vendors |
| Co-packaged optics (CPO) | Optics integrated into the switch/compute package | Ramping at the leading edge | [[AVGO]] (Tomahawk 6 + Davisson) · [[NVDA]] (Spectrum-X / Quantum-X) · [[MRVL]] (Teralynx) |
| Photonic fabric / interposer | Optical bridge compute↔HBM at package level | Frontier, barely commercial | [[MRVL]] (Celestial AI, acq. May 2026), Lightmatter (private) |

The investable nuance: the transition from pluggables to CPO is **disruptive to today's module makers** even as it grows the overall optical TAM — own the layer, not just the name.

## Beneficiaries by layer
- **Substrate:** [[SOITEC]] (photonics-SOI — every silicon-photonic chip starts here); InP for lasers (AXTI ~36% share).
- **Foundry/process:** [[TSM]] (COUPE silicon-photonics process), Tower (TSEM).
- **EDA / design IP:** [[SNPS]] · [[CDNS]] — photonic + electrical co-design.
- **Pluggable modules (today's revenue):** [[COHR]] · [[LITE]] · [[FN]] · [[AAOI]] (small-cap, US-mfg, 800G→1.6T hyperscaler ramp — high-beta, see page).
- **CPO / switch silicon:** [[AVGO]] · [[NVDA]] · [[MRVL]].
- **Optical fiber / connectivity:** [[GLW]] (Corning).
- **Diamond-in-the-rough / watch-only:** **Black Semiconductor** (private, Germany — *integrated graphene photonics* (IGP); FabONE 300mm electronic-photonic line operational end-2026, "first of its kind"; graphene's no-bandgap property — what killed it for transistors — makes it a broadband on-wafer modulator+photodetector; claims 100x interconnect scaling vs copper; added 2026-06-15, [[2026-06-15-semiwiki-graphene-photonics-colossus-token-throttle]]); **NewPhotonics** (private — PIC maker scaling production on yieldHUB analytics; second production-discipline datapoint 2026-06-15); Lightmatter (private, photonic interposer); **POET** — see [[POET]], the wiki's canonical AVOID (narrative-trading small-cap photonics name; do not conflate with the real stack).

## Risks / counter-thesis
- **CPO timing risk** — the transition has been "two years away" for several years; pluggables keep getting cheaper and good-enough, deferring CPO economics.
- **Disruption cuts both ways** — CPO adoption compresses the pluggable-module franchise that is today's [[COHR]]/[[LITE]]/[[FN]] cash flow.
- **Narrative conflation** — "photonic memory" as a discrete product does not exist; small-cap names trade on the confusion (see [[2026-05-17-photonic-memory-stack]] and [[POET]]).
- **Reliability / yield at scale** — PIC manufacturing adds optical variables (waveguide uniformity, coupling efficiency, packaging tolerances) that electrical chips don't have; yield is the gating variable as volumes rise.
- **The device is not the product — the "realization corridor" is** (2026-06-18, SemiWiki EORB thread, [[2026-06-18-semiwiki-apple-intel-google-tpu-packaging-samsung-dram]]). A useful frame for handicapping CPO/optical-I/O winners: the modulator or optical engine is the breakthrough, but the *product* is the full electro-optical realization path — electrical launch → optical conversion → driver integration → package/substrate interface → alignment stability → thermal-drift control → fiber attach → SI/PI behavior → test coverage → yield learning → reliability. **Which means**: bet on whoever proves the whole corridor can be manufactured, tested, cooled, aligned and qualified at scale, not on the best optical device in isolation — it sharpens the existing yield-is-the-gate risk into a selection rule (favor integrated package+test+reliability competence, e.g. [[AVGO]]/[[TSM]]-COUPE/advanced-packaging incumbents, over pure-device storylines).
- **The CPO link-quality race is now measurable — Intel and Nvidia are trading conference blows on bandwidth-vs-error-rate** (2026-06-23, SemiWiki forum, [[2026-06-23-semiwiki-daily]]). Two head-to-head DWDM optical-link datapoints: **Nvidia (ISSCC Feb 2026): BER <1e-12 at 256 Gb/s/fiber** (32 Gb/s/λ, 3D-stacked 7nm EIC / 65nm PIC); **Intel (VLSI Jun 2026): 800 Gb/s/fiber at BER <1e-9** (microring-based, open-cavity package). **Which means**: Intel is pushing ~3× the per-fiber bandwidth but at a *1,000× worse* raw error rate (1e-9 vs 1e-12) — the engineering frontier is the bandwidth-density / link-integrity / FEC trade-off, not raw speed alone, and microring (Intel) vs bandpass-filtered clock-forwarding (Nvidia) are diverging architectural bets. A diamond-in-the-rough tell for handicapping CPO: watch whose approach holds BER as bandwidth scales without burning the power/FEC budget — that's the realization-corridor gate (above) stated in numbers.

## Open questions
- When does CPO cross from leading-edge-only to mainstream switch deployment — and which transceiver makers successfully pivot vs get disrupted?
- Does an optical compute↔memory interposer ([[MRVL]]/Celestial, Lightmatter) reach commercial volume this cycle, or stay frontier?
- Which private PIC names (NewPhotonics, Lightmatter, Ayar Labs) reach the public market, and on what timeline?

## Related
[[2026-05-17-photonic-memory-stack]] · [[semiconductors]] · [[ai-capex-cycle]] · [[nvda-supply-chain]] · [[bottleneck-roadmap]] · [[COHR]] · [[LITE]] · [[FN]] · [[AAOI]] · [[AVGO]] · [[MRVL]] · [[SOITEC]] · [[GLW]] · [[overview]]

## Sources
1. [[2026-05-17-photonic-memory-stack]] — layer-by-layer technical map + per-layer tickers
2. [[2026-06-10-semiwiki-photonics-pic-production]] — PIC production scaling; NewPhotonics + yieldHUB analytics
3. SemiWiki "Optics is moving closer to compute" / STRL discussions (June 2026) — FRO→TRO→LPO→CPO roadmap framing
