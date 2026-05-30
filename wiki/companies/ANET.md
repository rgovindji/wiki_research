---
type: company
ticker: ANET
tags: [ai, networking, ethernet, hyperscaler, ai-infrastructure]
last_updated: 2026-05-29
last_full_review: 2026-05-29
sources: 2
conviction: medium-high
stance: bull
---

# Arista Networks (ANET)

**Stance:** bull · **Conviction:** medium-high · **Time horizon:** 2026-2030 hyperscaler 800G + 1.6T networking cycle

> **Why this page was opened 2026-05-29:** the wiki had a structural gap at the rack-scale Ethernet networking layer. [[DELL]]'s May 28 print ($16.1B AI server revenue, +757% YoY, $51.3B backlog) makes the upstream networking pull massive and immediate. Arista is the single most direct beneficiary among networking pure-plays — but the stock fell -14% post-Q1-earnings (May 5) on a "garden variety beat" reaction, the same pattern that has hit [[NVDA]] and [[CBRS]]. **Conviction medium-high, not high**, because NVDA NVLink + Spectrum-X is the existential rack-fabric competitor.

## One-line thesis

**The cleanest pure-play public name on hyperscaler Ethernet AI networking.** Q1 2026: rev **$2.709B (+35.1% YoY)** beat $2.6B guide. **AI revenue target raised to $3.5B for FY26**; full-year revenue guide raised to **$11.5B (+27.7%)**. EtherLink portfolio at 800G already deployed at scale. **XPO MSA** (Ethernet Port Optics) is a structural attack on traditional pluggable optics — Arista's 2027 product line aims to reduce networking racks 75% and floor space 44%. **Which means** ANET is positioned to capture the 1.6T + scale-out networking transition that's about to ramp at every hyperscaler that buys [[DELL]] / [[HPE]] / [[SMCI]] AI servers — but the stock has been treated as "AI exposed" already, so the marginal buyer is fatigued at peak expectations.

> **What this means:** Every AI cluster needs networking. Every hyperscaler that doesn't lock in 100% with NVDA NVLink uses Ethernet at scale. Arista has 70%+ of the high-end Ethernet AI networking market. The fundamentals are exceptional but the post-earnings -14% drop shows the marginal buyer has already priced in the bullish case — so returns from here require continued AI revenue acceleration *and* XPO MSA execution beating the optical-pluggable layer that [[COHR]] / [[LITE]] / [[FN]] currently own.

## Role in the AI / networking stack

- **Leaf-spine Ethernet at 400G / 800G / 1.6T** — the standard data-center fabric outside InfiniBand (NVDA-Mellanox) clusters
- **EtherLink portfolio**: AI-specific Ethernet leaf + spine at 800G; targets both **synchronous training flows** (multi-GPU collective communications) and **low-latency inference swarms**
- **Arista 7800 series** — the spine switch used by Meta + Microsoft + Oracle hyperscale AI clusters
- **XPO MSA** (new 2026) — Ethernet Port Optics, designed to reduce networking racks 75% and floor space 44% vs. traditional pluggables; first products 2027
- **EOS (Extensible Operating System)** — software moat; multi-decade stickiness
- Upstream: AVGO (Tomahawk + Jericho ASICs power Arista switches); CLS (Celestica is contract manufacturer for some 1.6T programs)
- Downstream: [[DELL]] / [[HPE]] / [[SMCI]] rack-scale solutions + hyperscaler direct deployments
- Competitors: NVDA NVLink + Spectrum-X (the rack-fabric existential threat), Cisco (enterprise lock-in), Juniper (acquired by HPE), Marvell custom XPUs

## Snapshot (Q1 2026, as of 2026-05-28)

| Metric | Value | As of |
|---|---|---|
| Stock | **$157.17** | 2026-05-28 |
| Market cap | **$195.5B** | 2026-05-28 |
| P/E (trailing) | **52.84** | 2026-05-28 |
| Q1 2026 revenue | **$2.709B (+35.1% YoY)** | Q1 2026 |
| Q1 2026 vs. guide | beat $2.6B guide | Q1 2026 |
| Q1 2026 cash flow ops | $1.69B | Q1 2026 |
| FY26 revenue guide (raised) | **$11.5B (+27.7%)** | mgmt |
| FY26 AI revenue target (raised) | **$3.5B** | mgmt |
| Post-earnings reaction (May 5) | **-14%** | Q1 print |
| Daily volume May 28 | 7.19M (vs 10.18M avg) | 2026-05-28 |
| Customer concentration | Meta + Microsoft + Oracle = >50% historically | structural |

## Bull case

- **EtherLink at 800G is shipping at hyperscaler scale today.** Not narrative — Q1 disclosure confirmed 800G deployments at the leaf-spine layer for both training (synchronous flows) and inference (low-latency concurrent swarms). **Which means** the moat is operational, not aspirational.
- **AI revenue target raised to $3.5B FY26** — explicit, segment-disclosed, accelerating. Q4 FY25 had AI revenue at ~$2.5B run-rate; the $3.5B target represents 40%+ growth in the AI mix alone.
- **EOS software moat.** ANET runs the same EOS image across leaf, spine, campus, and edge — the operational simplicity of a single OS at hyperscale is a multi-year switching cost. Cisco's equivalent (IOS XE + NX-OS + IOS XR + others) is fragmented; Cisco's enterprise lock-in doesn't translate to hyperscale.
- **XPO MSA is the existential offensive move.** If Arista can land Ethernet Port Optics in 2027, **it captures revenue currently flowing to [[COHR]] / [[LITE]] / [[FN]] at the transceiver layer**. 75% rack reduction + 44% floor savings is the value prop. **Which means** ANET's TAM expands materially if XPO works — and ANET's margin profile (high software + ASIC partnership) is structurally better than the transceiver layer's.
- **DELL May 28 print = direct demand corroboration.** [[DELL]] AI server revenue +757% YoY, $51.3B backlog — every PowerEdge XE9812 / XE9880L customer that's not InfiniBand-only buys Arista at the spine.
- **CLS guides 10 active 1.6T networking programs** — Celestica's hyperscaler 1.6T ramp is partly Arista 7800 series 1.6T (Arista 7800R3 + 7800R4 platforms). **Independent supply-chain confirmation** that 1.6T volume is coming.
- **Hyperscaler customer concentration is actually a moat at this scale.** Meta + Microsoft + Oracle (and increasingly OpenAI direct) consume more capacity than the next 100 customers combined; Arista's structural advantage at this tier is the EOS / sales / operations stack.
- **Cash flow $1.69B in Q1** + **net cash >$10B** — ANET can buy back ~5% of float per year or fund the XPO MSA buildout without dilution.

## Bear case / risks

- **NVDA NVLink + Spectrum-X is the existential rack-fabric competitor.** Per [[NVDA]] page Q1 FY27 disclosures: Networking $14.8B (+199% YoY). NVDA grew networking 5x faster than Arista grew Ethernet networking in the same window. **Which means** the rack-fabric layer is being claimed by NVDA, not Arista — Arista's growth at 35% YoY looks slow next to NVDA at 199%.
- **Post-earnings -14% on May 5** despite raising guide. **The marginal buyer is fatigued at peak expectations** — the same "garden variety beat priced in" pattern that hit NVDA on May 20 and CBRS post-IPO. This is the **single biggest tactical signal** on ANET right now: ATH-priced AI exposure that didn't catch a bid on a beat.
- **Customer concentration cuts both ways.** Meta + Microsoft + Oracle = >50% revenue. If any single hyperscaler shifts to NVDA-direct (Spectrum-X), Arista loses material revenue. Microsoft has been the most likely defector based on its NVDA partnership depth.
- **XPO MSA is unproven.** First products 2027. The MSA path means Arista is *betting* against the established pluggable-optics ecosystem ([[COHR]] / [[LITE]] / [[FN]] all very entrenched). If XPO slips or hyperscalers reject the new form factor, Arista loses the offensive move.
- **52.84 P/E is structurally elevated.** Comparable hyperscaler-exposed names: AVGO ~35x, NVDA ~50x. ANET trades like a pure AI play but has 65% non-AI revenue — multiple compression risk if AI revenue mix stops growing.
- **Cisco + Juniper (HPE) consolidation pressure** — HPE's Juniper acquisition gave them a credible enterprise Ethernet offering. The mid-market gets harder; high-end hyperscaler remains Arista's stronghold but is also where NVDA competes hardest.
- **800G commoditization.** As 1.6T ramps in 2027-28, 800G becomes commodity infrastructure — margin compression possible on the older generation while Arista's AI revenue concentrates in the new generation.

## Why this fits the wiki framework

ANET is **the Ethernet-fabric layer of the AI capex cycle** that the wiki has tracked through:
- Compute: [[NVDA]] / [[AMD]] / [[AVGO]] / [[CBRS]]
- Memory: [[MU]] / SK Hynix / Samsung
- Substrates: [[IBDXY]] / [[SOITEC]] / [[AJINY]] / [[SSEHY]] / [[ATSAY]]
- Optical: [[COHR]] / [[LITE]] / [[FN]]
- Power: [[VRT]] / [[ETN]] / [[GEV]] / [[BE]]
- Server OEM: [[DELL]] / [[HPE]] / [[SMCI]] / [[JBL]]
- **Networking (this page): ANET — the cleanest hyperscaler Ethernet AI fabric play**
- ODM: [[CLS]] (newly opened) / [[JBL]]

The post-earnings -14% drop (May 5) and the 52.84 P/E mean **this is not a dislocation entry — it's a momentum entry**. Position sizing should reflect that.

## Key questions / what to watch

1. **Q2 2026 AI revenue mix** — is the $3.5B AI FY26 target still trending, or is it back-half-loaded?
2. **Microsoft NVDA-direct vs. ANET balance** — the highest-stakes single-customer signal
3. **XPO MSA — first product launches 2027** — milestone tracking; any hyperscaler endorsement is bullish
4. **1.6T networking volume ramp** — Arista 7800R4 + EtherLink 1.6T
5. **DELL + HPE rack-scale platform attach rate** — every DELL XE9812 deployment that uses Ethernet is incremental ANET revenue
6. **NVDA Spectrum-X share at hyperscalers** — direct competitive read-through from NVDA quarterly disclosures

## Position sizing considerations

This is a **medium-high conviction bull** with a **post-earnings tactical caveat** — the May 5 -14% drop on a raised guide is the kind of signal that historically precedes either (a) base building before a second leg up, or (b) extended consolidation if AI revenue growth disappoints. **Pre-earnings adds should be sized small**; full-conviction adds wait for AI revenue mix confirmation in Q2 print (early August 2026).

**Hedging-risk framework**: ANET trades >50x P/E and is hyperscaler-concentrated. Per [[hedging-risk]] tier-1 indicators, a portfolio that's bull NVDA + bull MU + bull ANET is over-concentrated in the same AI capex factor — sizing should reflect the correlation, not just the standalone thesis.

## Related

[[NVDA]] · [[AVGO]] · [[DELL]] · [[HPE]] · [[CLS]] · [[COHR]] · [[LITE]] · [[FN]] · [[ALAB]] · [[ai-capex-cycle]] · [[nvda-supply-chain]] · [[semiconductors]] · [[hedging-risk]] · [[overview]] · [[watchlist]]

## Sources

1. [[2026-05-28-DELL-Q1-FY27-earnings]] — DELL print establishing the demand-side anchor for ANET upstream
2. [[2026-05-29-dell-upstream-second-derivative]] — synthesis of unre-rated Dell-upstream second-derivative plays

## Citations

- [Arista Q1 2026 earnings transcript](https://www.fool.com/earnings/call-transcripts/2026/05/05/arista-anet-q1-2026-earnings-transcript/)
- [Arista 8-K press release Q1 2026](https://www.sec.gov/Archives/edgar/data/0001596532/000159653226000074/ex991q126-earningsrelease.htm)
- [TipRanks coverage on AI-fueled Arista surge](https://www.tipranks.com/news/company-announcements/arista-networks-earnings-call-highlights-ai-fueled-surge)
- [Tikr — Arista fell 14% after earnings; CFO commentary](https://www.tikr.com/blog/arista-networks-fell-14-after-earnings-heres-what-the-cfo-said-9-days-later)
