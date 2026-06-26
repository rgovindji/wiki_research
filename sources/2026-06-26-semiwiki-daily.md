---
date: 2026-06-26
type: article
publisher: SemiWiki (forum + articles)
url: https://semiwiki.com/
raw_path: n/a (semiwiki_scan.py incremental extract)
touches: [semiconductors, photonics, MU, ARM, INTC, VRT]
---

# SemiWiki daily sweep — 2026-06-26 (7 new items)

## TL;DR
- **Samsung is closing the HBM gap and pouring concrete:** ships industry-first **12-layer HBM4E samples** (14–16 Gbps, 3.6 TB/s/stack, 48 GB on 1c DRAM + 4nm logic base die) *and* reportedly readies a **~$648B / 1,000T-won, 10-year** Korea investment (≈300T won for new chip fabs). Both cut against the "memory trio stays supply-disciplined / Micron's HBM lead is durable" read.
- **Arm has reached ~50% of compute shipped into top AI data centers** — the x86→Arm server share shift is no longer a forecast; royalty-rich server sockets across NVDA/Google/Amazon/Microsoft/Qualcomm custom silicon.
- **The power layer is the next bottleneck:** Nvidia's push to **800VDC** racks revives silicon-carbide / power-semis (Wolfspeed, Rohm, Taiwan's Episil) — capacity going from oversupply toward shortage; ties to VRT/ETN's 800V architecture.

## Key facts (by item)
1. **Photonics — "device breakthrough is the spark, system realization is the revolution"** (Dr. Moh Kolbehdari forum essay). Ultra-fast modulators/photodetectors/plasmonics/atomic-scale switching matter for AI only when the *whole* electro-optical corridor — packaging, fiber attach, laser integration, thermal stability, calibration, test, burn-in, reliability — converges at scale. Restates the "realization corridor" selection rule for CPO winners. Photonics is a standing interest.
2. **Samsung HBM4E 12-layer samples** — industry-first; 14 Gbps stable (scalable to 16), 3.6 TB/s/stack, 48 GB (>30% capacity vs prior gen), built on 6th-gen 1c DRAM + Samsung Foundry 4nm base die; +16% energy efficiency, −14% thermal resistance vs HBM4. Mass production "aligned with customer schedules."
3. **Arm ~50% share of compute in top AI data centers** (senior exec, via Nikkei). Server royalties run higher than mobile; challenges x86 (Intel/AMD) directly. Major non-x86 server CPUs (Nvidia Grace, Google Axion, AWS Graviton, MSFT Cobalt, Apple, Qualcomm) are Arm.
4. **Samsung readies ~$648B (1,000T won) 10-year Korea bet** — AI data centers, batteries, displays, semis; ~300T won for new fabs in the southwest. Reflects memory/packaging as strategic national assets.
5. **CXMT 64-layer 3D DRAM test vehicle** — 5-layer horizontal cell (vertical WL, pillar capacitor), Ion/Ioff ~1e8, SS ~93 mV/dec; 0.280×0.435 µm cell → ~525 Mb/mm² at 64 layers, into the ~1c (<600 Mb/mm²) range. China's path to close the DRAM-density gap via stacking, not shrink.
6. **Nvidia 800VDC could revive SiC/power semis** (cwnewsroom). As AI DCs demand higher power efficiency, SiC and power semis may swing from oversupply to shortage; Wolfspeed, Rohm, Taiwan's Episil back in the spotlight — "the next AI bottleneck may have nothing to do with GPUs."
7. **Intel 18A vs 18A-P** — 18A-P (volume this month) adds ~9% perf at same power / ~18% lower power, ~20–40% lower thermal resistance, "Power Boost" RibbonFET variants, drop-in compatible with 18A. The N5P/N3P-style optimized node before 14A.

## Key claims (and confidence)
- Samsung HBM4E sampling first — **high** (vendor PR, dated). Competitive read-through for MU — **medium** (sampling ≠ qualified volume; Samsung has missed HBM windows before).
- Arm 50% DC compute share — **medium** (single exec, no methodology), but directionally corroborated by the named custom-silicon roster.
- SiC/power shortage swing — **medium** (analyst/newsletter thesis), but coheres with the 800VDC roadmap and VRT/ETN's stated architecture.
- CXMT 64-layer to ~1c density — **medium** (research test vehicle, not production) — slow-burn structural bear on the oligopoly's low-end DRAM.

## Wiki updates made
- [[semiconductors]] — Samsung HBM4E + $648B capex + CXMT 3D DRAM + Arm 50% DC share bullet
- [[MU]] — Samsung HBM4E competitive read-through (memory-trio supply/lead)
- [[photonics]] — Kolbehdari realization-corridor reinforcement
- [[ARM]] — 50% AI-data-center compute share
- [[INTC]] — 18A vs 18A-P node detail
- [[VRT]] — 800VDC / SiC power-bottleneck tie-in
