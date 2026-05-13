---
type: source
title: "ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More"
authors: Afzal Ahmad, Gerald Wong, Daniel Nishball, and 4 others (SemiAnalysis)
publication: SemiAnalysis Newsletter
date_published: 2026-04-15
date_read: 2026-05-09
url: https://newsletter.semianalysis.com/p/issscc-2026-nvidia-and-broadcom-cpo
local_file: raw/articles/NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More.pdf
tags: [ai, semis, memory, hbm4, lpddr6, cpo, packaging, isscc]
---

# 2026-04-15 — ISSCC 2026 Technical Roundup

A 93-page technical deep dive on the ISSCC 2026 conference. Key categories: Memory, Optical Networking, High-Speed Electrical Interconnects, Processors. The most material findings for the wiki are around HBM4 competitive dynamics and the technology stack underpinning Rubin-generation accelerators.

## Samsung HBM4 — competitive dynamics shifting

**The headline:** Samsung's HBM4 is **competitive with peers** and can meet the pin-speed required for [[NVDA|NVIDIA]]'s Rubin while staying below 1V. **Which means:** the long-held assumption that [[MU|Micron]] is the safe second-source play behind SK Hynix and Samsung is a perennial laggard needs to be revisited. Samsung is closing the gap meaningfully.

### Specifications (Paper 15.6)

| Generation | HBM3E | HBM4 |
|---|---|---|
| Process | C&B-Die: 4th Gen 10nm DRAM | C-Die: 6th Gen 10nm DRAM (1c) / B-Die: 4nm Fin-FET |
| Supply Voltage | VDDC=1.1V, VDDQ=1.1V | VDDC=1.05V, VDDQ=0.75V |
| Max Data Rate | 10.0 Gb/s/pin | 13.0 Gb/s/pin |
| Bandwidth | 1.3 TB/s per cube | **3.3 TB/s per cube** |
| Max Density | 48GB (16-high) | 36GB (12-high) |

- JEDEC HBM4 baseline is 6.4 Gb/s pin / 2 TB/s. Samsung **demonstrates more than 2x the JEDEC pin speed** (13 Gb/s, 3.3 TB/s).
- Even at lower VDDC/VDDQ of 1.05V/0.75V, the device sustains **11.8 Gb/s**.

### Architecture differentiators

- **Logic base die on SF4 process** (vs SK Hynix using TSMC N12, Micron using internal CMOS). **Which means:** Samsung is the most aggressive on base-die node — higher cost but better speed/power. SF4 enables a fully programmable PMBIST (Memory Built-In Self-Test) that runs at full interface speed at any clock edge, dramatically improving debug efficiency and yield learning.
- **Adaptive Body-Bias (ABB) control + 2x DQ TSV count** improves tCCDR margin (constraint that governs parallel multi-channel reads) — operating speed up to 13 Gb/s/pin.
- **1c front-end yield was only ~50% last year**, gradually improving — this is the margin risk for Samsung HBM4 economics.

### Investment implications

- **[[MU]]:** Bull case rests on being NVDA's preferred HBM supplier. Samsung's HBM4 competitiveness narrows that moat. **Which means:** monitor 2026 NVDA design-win disclosures carefully; if Samsung wins meaningful share of Rubin HBM4 allocation, MU's pricing power weakens.
- **[[NVDA]]:** Multi-source HBM4 supply for Rubin is good for NVDA (de-risks supply, pressures memory makers' margins).

## Samsung LPDDR6 (Paper 15.8)

| Item | LPDDR5X | LPDDR6 |
|---|---|---|
| Channels | 1 / die | 2 sub-channels / die |
| Data Rate | 10,700 Mb/s | **14,400 Mb/s** |
| Pins | 16 DQ + 2DMI | 12 DQ + DBI / sub-channel |
| Power | VDD1: 1.8V / VDDQ: 0.5V | VDD1: 1.8V / VDDQ: 0.5V / VDD2D: 0.875V |
| ECC | 128+8 (SEC) | 256+16 (SEC-DED) |

- **Read power -27%, write power -22%** vs LPDDR5
- Uses **Wide-NRZ signaling** (12 DQ per sub-channel) — unlike GDDR7's PAM3
- Effective bandwidth at 14.4 Gb/s: **38.4 GB/s** per sub-channel
- I/O power-switching saves 9% IDD4R and 5% IDD4W at 3.2 Gb/s

**Investment implication:** LPDDR6 is the on-device memory for next-gen smartphones, PCs, and increasingly AI inference accelerators. Confirms [[MU]] / Samsung / SK Hynix are seeing a generational refresh window in 1H 2027 once LPDDR6 ramps. Combined with HBM4, this is the memory makers' second-leg revenue driver.

## Other ISSCC topics (deeper pages not read)

The 93-page document also covers GDDR7, NAND, **CPO (Co-Packaged Optics) from NVIDIA and Broadcom**, TSMC Active LSI (advanced packaging), Logic-Based SRAM, UCIe-S (chiplet die-to-die interface), and processors from MediaTek, AMD, NVIDIA, and Microsoft. These warrant a return pass if specific tickers in the supply chain become topical.

## Direct wiki implications

- **[[MU]]:** Add Samsung HBM4 competitive risk to bear case.
- **[[NVDA]]:** Add multi-source HBM4 supply as a margin-positive tailwind for the Rubin generation.
- **[[bottleneck-roadmap]]:** Confirm HBM4 ramp is the gating bottleneck for 2026-27 accelerator generation.

## Related

[[NVDA]] · [[MU]] · [[AVGO]] · [[TSM]] · [[bottleneck-roadmap]] · [[nvda-supply-chain]] · [[2026-05-09-dwarkesh-dylan-semianalysis]]
