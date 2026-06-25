---
date: 2026-06-25
type: article
publisher: SemiWiki (forum + front page)
url: https://semiwiki.com/forum/threads/25369
raw_path: null
touches: [semiconductors, bottleneck-roadmap, AVGO, ASML]
---

# SemiWiki daily sweep (4 new items): IBM 0.7nm "NanoStack" CFET + the official OpenAI/Broadcom Jalapeño unveil

## TL;DR
- **IBM announces a 0.7nm-equivalent "NanoStack" process** — the first publicly claimed sub-1nm node — built on a staggered sequential CFET with NMOS/PMOS on separately processed wafers cut on different crystal planes, bonded via a proprietary "device-scale" wafer-bonding step. Claims 50% logic / 40% SRAM scaling and 70% energy efficiency vs IBM's own 2nm.
- **OpenAI + Broadcom officially unveil "Jalapeño"** (already ingested June 24 from reporting) — now with the formal PR: GPT-5.3-Codex-Spark running on engineering samples in-lab, Broadcom Tomahawk networking silicon, Celestica as rack-integration partner, "performance per watt substantially better than current state-of-the-art," gigawatt-scale multi-generation roadmap.

## Key facts
- **IBM 0.7nm / NanoStack** (More than Moore / Ian Cuttress + BBC): staggered sequential CFET — NMOS and PMOS fabricated on *separate* wafers, NMOS on a <001> crystal plane and PMOS on <110> to optimize each carrier's mobility, then bonded. The enabling (proprietary) step is a "device-scale" wafer-bonding process. ~666M transistors/mm² claimed; ~100B transistors on a fingernail-sized die. IBM is acquiring a High-NA EUV machine ([[ASML]] read-through). 50% logic scaling, 40% SRAM scaling, 70% better energy efficiency vs IBM 2nm.
- **The skeptic's caveat (forum consensus):** IBM doesn't manufacture for itself or anyone; IBM's 2nm was "announced" in 2021 and is still 2+ years from a shipping product (only Rapidus in line). Pattern-matched to "an IBM press release about a revolutionary tech we'll never hear about again." Any foundry adopting it would need to license the bonding process and the differently-cut wafers — a real adoption-friction tell.
- **Jalapeño official unveil:** delivered by Hock Tan/Charlie Kawwas to Altman/Brockman; nine-month design-to-production; deploy end-2026; Microsoft ~40% of first allocation (from prior reporting). Engineering samples running ML workloads at production target frequency/power. Detailed technical report "in coming months."

## Key claims (and how confident)
- **IBM 0.7nm is a research milestone, not a thesis mover — medium-high confidence.** The sequential-CFET + cross-plane-wafer-bonding work is genuinely novel and points at where the sub-1nm logic roadmap goes (CFET after GAA), but IBM's history is research-leadership-without-manufacturing. The investable read-through is indirect: another High-NA buyer for [[ASML]]; a wafer-bonding/advanced-packaging complexity datapoint for [[bottleneck-roadmap]]; and a reminder that the leading-edge logic roadmap is increasingly a *packaging/bonding* problem, not just a litho one.
- **Jalapeño official PR adds confirmation, not new thesis — high confidence.** Celestica (rack integration) and Tomahawk (networking) name the full Broadcom-led stack; consistent with the [[AVGO]] custom-silicon hedge leg already in the book.

## Wiki updates made
- [[semiconductors]] — IBM 0.7nm NanoStack CFET (sub-1nm research milestone; sequential CFET + cross-plane wafer bonding).
- [[bottleneck-roadmap]] — device-scale wafer bonding as the next leading-edge enabler/friction (licensing-gated).
- [[AVGO]] — Jalapeño official unveil (Celestica + Tomahawk; confirmation of the June 24 reporting).
