---
type: source
title: "The EDA Primer: From RTL to Silicon (Laying the Groundwork of the Current Chip Design Paradigm)"
authors: Gerald Wong, Dylan Patel, Sravan Kundojjala (SemiAnalysis)
publication: SemiAnalysis Newsletter
date_published: 2026-05-11
date_read: 2026-05-09
url: https://newsletter.semianalysis.com/p/the-eda-primer-from-rtl-to-silicon
local_file: raw/articles/The EDA Primer_ From RTL to Silicon.pdf
tags: [ai, semis, eda, snps, cdns, siemens]
---

# 2026-05-11 — The EDA Primer (Part 1 of 3-part series)

51-page primer establishing the EDA industry context. Future parts: (2) EDA market analysis incl. SNPS/CDNS/Siemens business models, Chinese efforts, IP licensing, transition to Customer Owned Tooling (COT) with hyperscaler ASIC designs; (3) AI disruption to EDA incl. agentic chip design flows from NVDA and the Big Three.

## The setup: a perfect storm at the design stage

Three converging trends:

1. **Chip complexity exploding** — AMD MI455X packs **320 billion transistors across 12 logic dies** on 2nm/3nm with Hybrid Bonding 3D stacking, HBM4 integration, 224G SerDes.
2. **Talent base shrinking** — One-third of US semiconductor workforce is over 55. Apple's New Silicon Initiative has barely moved the needle. Engineering hours have grown ~50% per chip generation since 28nm; EE degree pipeline is flat-to-declining.
3. **Time-to-market pressure** — A 3-month delay = "billions of dollars."

**Which means:** the chip design bottleneck is now **software, not silicon** — and the only relief valve is EDA + AI automation. This is the structural tailwind for [[SNPS]] and Cadence (CDNS, not yet in wiki).

### Specific data points

- **67K semiconductor worker shortage in US by 2030** (Siemens estimate)
- **$300M+ first-time total silicon design cost** at 3nm node
- **Chip complexity grows ~50%/yr** (new nodes + larger SoCs)
- **Design productivity grows only ~20%/yr** — productivity gap widens every generation
- **Verification engineers are the fastest-growing job category** in chip development; industry "still cannot hire them fast enough"
- **Verification = up to 70% of total project effort** (was lower historically)
- **Mean verification engineers per project surpassed design engineers between 2007 and 2016** — and the gap is widening

## The Big Three

| Company | Founded | Key product | Notes |
|---|---|---|---|
| Synopsys ([[SNPS]]) | 1986 | Design Compiler (1987) — first commercial logic synthesis | Founded by Aart de Geus from GE research |
| Cadence (CDNS) | 1988 | IC layout + place-and-route | Merger of SDA Systems + ECAD |
| Siemens EDA | 2017 (acq.) | Mentor Graphics → Siemens for $4.5B in 2017 | Rebranded Siemens EDA in 2021 |

**Which means (investment thesis):** EDA is a 3-vendor oligopoly with extreme switching costs, regulatory tailwinds (US export controls limit Chinese EDA penetration), and AI-driven product premium opportunities. Pricing power is durable. The structural moat is the qualified-cell-library + foundry-PDK relationships that take a decade to build.

## The 13-stage chip design waterfall

The diagram lays out 13 stages from blank whiteboard to volume production:
1. Planning (PPA goals)
2. Architecture
3. RTL Design (SystemVerilog)
4. RTL Verification (UVM, formal, coverage)
5. RTL Freeze
6. FW/SW Development (parallel)
7. Physical Design (synthesis → P&R)
8. Signoff (STA, DRC, LVS, power)
9. Foundry Handoff (GDSII → masks) — "tapeout"
10. Fabrication
11. Post-Silicon Validation
12. System Integration
13. Production

EDA tools are needed at virtually every stage from #3 onward. **Which means:** EDA revenue per chip program is rising as designs get larger and verification consumes a bigger share of project hours.

## Investment implications

- **[[SNPS]]:** Reaffirm bull / medium conviction. The "shrinking talent base + exploding complexity = EDA revenue compounding" thesis is fully validated by Part 1 data. NVDA $2B AI-EDA partnership announced earlier is exactly the agentic-flow theme Part 3 will cover.
- **CDNS (off-watchlist, NEW research candidate):** Co-leader with Synopsys. Adding to "next research targets" — CDNS deserves the same coverage as SNPS.
- **Siemens / SIE.DE (off-watchlist, international):** Could be a third-leg play but international listing and conglomerate structure dilute exposure.
- **AI disruption to EDA (Part 3 forthcoming):** Synopsys DSO.ai and NVDA agentic chip design flows are the next frontier — model labs and EDA vendors converging.

## Direct wiki implications

- **[[SNPS]]:** Add EDA primer data points (67K talent shortage, $300M design cost, 70% verification share, 50% complexity vs 20% productivity).
- **[[watchlist]]:** CDNS already in "Not yet covered" list — bump priority.
- **[[ai-capex-cycle]]:** Note EDA as the under-discussed compounder in the AI infra stack.

## Related

[[SNPS]] · [[NVDA]] · [[TSM]] · [[AMD]] · [[ai-capex-cycle]] · [[bottleneck-roadmap]]
