---
date: 2026-05-20
type: research-note
publisher: Morgan Stanley Research (synthesized from public references + Twitter discussion)
url: https://x.com/Aaronwei3n/status/2027xxxxxxxxxxxxxx
touches: [NVDA, MU, AVGO, IBDXY, AJINY, SOITEC, AXTI, ALAB, ai-capex-cycle, bottleneck-roadmap, nvda-supply-chain]
---

# Morgan Stanley VR200 "BOM" analysis — what it reveals about NVDA's revenue model

## TL;DR
- MS published a per-component pricing breakdown for the NVIDIA Vera Rubin VR200 NVL72 rack labeled as "BOM" — but the framing is misleading.
- **It's not a true BOM (NVDA's input cost)**. It's a **per-component price breakdown of what the CSP pays when procuring a full rack**. NVDA's markup is embedded within each line item, especially the GPU line.
- Approximate breakdown circulating: total ~$4M per rack, with **~$2.5M for 144 GPU dies (~$17,500/die)**, balance across HBM, networking, CPU, cooling, power.
- **The critical analytical insight from the secondary discussion** (Aaron Wei + Daniel Wu): "biggest risk to NVDA top line is if DRAM prices collapse, since NVDA is passing through HBM at full margin."
- Combined with Q1 FY27 print (Vera Rubin samples shipped + Networking +199% YoY + system pricing $5-7M VR200), this analysis exposes both NVDA's **vertical integration margin capture** AND the **HBM pass-through top-line risk**.

## Key facts (synthesized from public sources)

### What the MS analysis appears to show

| Component category | Approximate value | Per-unit price | Source |
|---|---|---|---|
| **GPU dies** | **$2.5M** | $17,500/die × 144 dies (72 packages × 2 dies) | Twitter via Aaron Wei |
| **HBM memory** | (passed through at full margin) | TBD per package | Implied from Daniel Wu observation |
| **Liquid cooling** | **$55,710** | $2,660/compute tray + switch tray | MS public note (Tom's Hardware) |
| **Networking (NVSwitch/NVLink)** | embedded in compute trays | — | NVDA Q1 +199% YoY confirms scale |
| **CPUs (Vera)** | new line item | $200B TAM per Jensen | NVDA Q1 commentary |
| **Power / NICs / PCB / storage** | balance | varies | implicit |
| **Total per rack** | **~$4M** (component sum) | — | Twitter via Aaron Wei |
| **System price (CSP pays)** | **$5-7M** | (VR200 NVL72); VR300 NVL144 up to $8.8M | Tom's Hardware |

### What this implies about NVDA gross margin sustainability

If components total ~$4M and CSP pays $5-7M, the **system integration + margin pool** = ~$1-3M per rack. Three scenarios:

1. **Server makers (SMCI, DELL, HPE) capture integration margin** (old model): NVDA sells $1.5M GPU package; server maker assembles $5M rack at thin margin
2. **NVDA captures integration margin** (new model per JPM analysis): NVDA sells $5M rack directly = NVDA gets BOTH GPU margin AND integration margin
3. **Mixed model**: NVDA + server maker split integration margin via commercial terms

The Q1 FY27 print (75% GM HOLDING despite higher rack-scale revenue mix) suggests NVDA is successfully capturing more of the integration margin.

### The Daniel Wu insight — HBM pass-through as top-line risk

The key analytical observation from the Twitter thread:
> "Perhaps biggest risk to NVDA top line is if DRAM prices collapse, since it is passing through HBM at full margin..."

**Implication**: NVDA's revenue includes HBM cost passed through to the CSP buyer (with NVDA margin on top). If HBM prices roll over:
- **Margin %** could stay flat (NVDA still earns same multiple on lower base)
- **Revenue $** would drop proportionally on the memory line
- The current cycle has HBM at ALL-TIME HIGHS (SK Hynix Q1 op margin 72% record per [[2026-05-18-sk-hynix-near-1T]])
- A HBM downcycle would hit NVDA's revenue line BEFORE / SIMULTANEOUSLY with [[MU]] / SK Hynix
- This is the [[ai-bubble-debate]] cyclical risk that Q1 FY27's print doesn't fully address

## Quotes worth keeping

> "Morgan Stanley is estimating what the CSP pays for each component category when procuring a full rack, not what it costs NVIDIA to build one. NVIDIA's markup should be already embedded within each line item, particularly the GPU line."
> — Aaron Wei (@Aaronwei3n), May 20, 2026

> "Perhaps biggest risk to NVDA top line is if DRAM prices collapse, since it is passing through HBM at full margin..."
> — Daniel Wu (@itsDanielWu), May 20, 2026

## Critical thinking — what this means for the wiki

### 1. The "BOM" naming is a market misnomer that confused readers

A traditional BOM is the manufacturer's input cost. This is the **per-component pricing the BUYER pays** — with the seller's margin embedded. The MS analyst chose imprecise language and the Twitter discussion correctly flagged it.

For wiki purposes: **never describe NVDA's per-rack revenue as "BOM"** — describe it as "per-component pricing realized by NVDA" or "rack-procurement breakdown."

### 2. NVDA's vertical integration is restructuring the supply chain margin pool

JPM separately reported NVDA is shifting from "components vendor" to "full-system seller starting with Vera Rubin." The MS rack pricing data confirms this — NVDA's $5-7M system price has a ~$1-3M integration margin pool that previously belonged to [[SMCI]] / [[DELL]] / [[HPE]] / [[JBL]] / [[FLEX]].

**Implications for server-maker wiki pages**:
- [[SMCI]] / [[DELL]] / [[HPE]] face margin compression on the rack-integration line as NVDA moves vertical
- [[FLEX]] / [[JBL]] (contract manufacturers) keep their assembly fee but lose integration margin
- [[VRT]] / [[NVT]] (power/cooling specialists) still get paid per their components

### 3. HBM pass-through means NVDA revenue is **cyclically exposed** to memory pricing

This is the most important analytical takeaway. NVDA's revenue line includes HBM cost-plus-margin. If/when HBM cycle peaks and ASPs roll over:
- NVDA revenue compresses on the memory line proportionally
- Even if GPU/networking margins hold, total revenue dollar drops
- **This is the cyclical risk that the bull case explicitly does NOT address**

**Watch trigger**: SK Hynix Q2 2026 (August) operating margin commentary. If 72% peak holds → HBM cycle has more runway. If it compresses → first signal of cycle turn.

### 4. The Networking +199% YoY in Q1 FY27 + MS BOM data confirms the supply-chain thesis

Networking $14.8B at 199% growth means the NVLink/Spectrum-X/Quantum-X CPO content per rack is scaling fast. The MS BOM line items for networking (NVSwitch trays, NVLink) align with the wiki's CPO/photonic-SOI/InP/ABF substrate thesis directly.

### 5. Vera CPU $200B TAM is a separate revenue line that doesn't have the HBM exposure

Per Jensen Q1 FY27 call: Vera standalone CPU = $200B TAM. This CPU revenue is NOT HBM-pass-through; it's discrete silicon margin. **Provides natural hedge** against HBM-cycle revenue volatility once Vera CPU ramps in Q3 2026.

## Wiki updates made
- Source summary saved
- [[NVDA]] — add HBM pass-through risk note in Bear case section
- [[MU]] — note that NVDA revenue is cyclically exposed to HBM pricing alongside MU
- [[ai-bubble-debate]] — HBM pass-through is the cyclical-revenue argument that the bull case explicitly does not address
- [[bottleneck-roadmap]] — confirms substrate stack capture thesis
- [[nvda-supply-chain]] — server-maker margin compression as NVDA goes vertical
- New theme page candidate: [[ai-rack-economics]] (deferred — covered adequately by this source summary + NVDA page updates)

## Honest caveat

I could not access the original Morgan Stanley research PDF (paywalled MS Research product). This source summary synthesizes:
- Public MS references (cooling cost analysis, demand forecast)
- Tom's Hardware coverage of rack pricing
- Twitter discussion from Aaron Wei + Daniel Wu (May 20)
- JPM cross-reference on NVDA vertical integration
- Q1 FY27 print confirmation of the framework

Numbers in the "approximately" range should be treated as directionally correct; precise line items would require access to the MS PDF itself. The analytical takeaways (HBM pass-through risk, vertical integration margin capture) are robust to small calibration changes.
