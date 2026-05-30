---
date: 2026-05-28
type: earnings
publisher: Dell Technologies
url: https://www.sec.gov/Archives/edgar/data/0001571996/000157199626000021/exhibit991earnings8kq1fy27.htm
raw_path: n/a (10-Q + press release public)
touches: [DELL, NVDA, MU, ALAB, VRT, JBL, APH, ANET, CLS, bottleneck-roadmap, ai-capex-cycle, nvda-supply-chain]
---

# DELL Q1 FY27 — The Largest AI Server Print in Corporate History

Dell Technologies delivered its Q1 FY27 print after-close on 2026-05-28. The numbers are exceptional in a way that resets the entire AI server narrative — and **the supply-constraint footnote is the most actionable signal the wiki has captured this quarter**.

## TL;DR

- **Revenue $43.84B (+88% YoY)** — fastest growth rate since Dell's 2018 return to public markets
- **Diluted EPS $5.24 (+282% YoY)** — destroyed consensus $2.91 expectation
- **ISG Revenue $29B (+181% YoY)** — 66% of total; 9 consecutive quarters of double-digit growth
- **🔥 AI Server Revenue $16.1B recognized (+757% YoY)** in single quarter
- **🔥 AI Orders $24.4B booked Q1** + **$51.3B backlog** (up from $43B start of FY27)
- **FY27 Revenue guide raised 20% to $165-169B** (from prior $138-142B)
- **Stock +40% AH** initially on the print
- **🔥 SUPPLY CONSTRAINT FOOTNOTE — the actionable read-through**: per Dell's own disclosures and industry commentary, **memory costs now account for 10-70% of Dell's bill of materials**; **HBM/DRAM prices jumped up to 414% in some regions**; PC mfrs bearing **110% higher memory prices in Q1 2026**; **each GB300 rack requires roughly 440,000 MLCCs** (multilayer ceramic capacitors) for power filtering and decoupling

## Why this matters beyond DELL itself

The print is so large that it's no longer a story about DELL — it's a story about who supplies DELL. **$51.3B AI backlog + $24.4B Q1 orders + guide raised 20%** means the second-derivative pull through Dell's upstream is enormous and ongoing. The wiki has covered some of this stack ([[NVDA]], [[MU]], [[ALAB]], [[VRT]], [[JBL]], [[APH]], [[IBDXY]], [[SOITEC]], [[AJINY]]) but has two important gaps surfaced by this print: **[[ANET]]** (rack networking) and **[[CLS]]** (Celestica — ODM with 70%+ AI exposure).

See [[2026-05-29-dell-upstream-second-derivative]] for the full upstream synthesis written same-day.

## Key facts (verbatim where possible)

| Metric | Q1 FY27 | Q1 FY26 | Δ |
|---|---|---|---|
| Revenue | $43.84B | ~$23.4B | **+88% YoY** |
| Diluted EPS | $5.24 | ~$1.37 | **+282% YoY** |
| Adj EPS | $4.86 | — | beat consensus $2.91 by 67% |
| ISG revenue | $29.0B | ~$10.3B | **+181% YoY** |
| AI server revenue (recognized) | **$16.1B** | ~$1.9B | **+757% YoY** |
| AI orders booked Q1 | **$24.4B** | — | new disclosure |
| AI backlog (end Q1) | **$51.3B** | $43B (start FY27) | +$8.3B sequential |

**FY27 guidance:**
- Prior: $138-142B
- **New: $165-169B (+20% raise)**

**Stock reaction:** +40% AH initially per TradingKey; consolidating into May 29 open.

## Supply chain implications (the actionable second-derivative)

### Bottleneck #1: Memory (HBM + DRAM + NAND)
- **Memory now 10-70% of Dell's BOM** — at the high end (AI servers), memory is the single largest cost line above silicon
- HBM/DRAM prices +up to 414% in some regions per industry coverage
- **Connect-the-dots with [[2026-05-26-micron-1T-ubs-1625-pt]]**: UBS reframed MU as AI infrastructure stock (TSMC-like multiple) on May 26 — DELL's print on May 28 *empirically* validates the reframing. Dell's actual BOM economics are the direct test of UBS's LTA framework
- **Read-through**: [[MU]] / SK Hynix / Samsung — all the wiki's memory bull cases are corroborated

### Bottleneck #2: PCIe / interconnect retimers
- **Every PowerEdge XE9812 (Vera Rubin NVL72)** and **XE9880L / XE9882L / XE9885L (HGX Rubin NVL8)** uses PCIe Gen 6 extensively
- **Each NVL72 rack contains dozens of PCIe Gen 6 retimers** — [[ALAB]] dominates this layer
- DELL's $16.1B AI server revenue this quarter implies ~50K-100K racks shipped depending on mix → **multi-million-unit PCIe retimer pull**
- Read-through: [[ALAB]] Q2 guide $355-365M may prove conservative vs. DELL's volumes

### Bottleneck #3: Liquid cooling
- **GB300 rack power density** (~135 kW/rack) is at the limit of air cooling
- Vera Rubin NVL72 (XE9812) is even higher
- **DELL's AI server ramp + 9 consecutive ISG growth quarters = sustained liquid-cooling pull**
- Read-through: [[VRT]] / [[MOD]] / [[NVT]] are the most direct beneficiaries; Goldman May 17 basket (also [[STRL]] / [[IESC]] / [[POWL]] / [[AGX]]) gets validated

### Bottleneck #4: 🆕 MLCC (multilayer ceramic capacitors) — **wiki gap**
- **Each GB300 rack requires ~440,000 MLCCs** for power filtering + decoupling
- DELL's AI server pace = potentially **billions of MLCCs/year** from one OEM customer
- Supply is **Japanese-dominated**: Murata (private), TDK (US ADR), Samsung Electro-Mechanics ([[SSEHY]] — already in wiki for ABF), Taiyo Yuden, Yageo
- **Wiki gap**: no dedicated MLCC analysis. Worth flagging for future expansion if user wants exposure to the most-under-priced AI-buildout layer
- Read-through: TDK / Murata exposure not currently in wiki; SSEHY already covered for substrates is dual-exposed

### Bottleneck #5: Networking (rack-scale switches)
- Dell's AI Factory racks integrate via Ethernet (with ANET / AVGO) or InfiniBand (with NVDA)
- **DELL's volume ramp pulls hyperscaler networking at the same pace**
- Read-through: [[ANET]] (Arista — **wiki gap; opening today**), [[AVGO]], [[CLS]] (Celestica — Arista's contract manufacturer for some 1.6T programs)

### Bottleneck #6: Substrates (ABF + photonic)
- Each GB300 + Vera Rubin uses ABF substrates ([[IBDXY]] / [[AJINY]] / [[SSEHY]] / [[ATSAY]] / [[UNIMICRON]])
- CPO transition starting on Vera Rubin H2 FY27 ([[SOITEC]] confirmed May 27)
- Read-through: All wiki substrate names are validated; SOITEC just printed FY26 Photonics-SOI >$100M ahead of plan

## Quotes worth keeping

> *"Q1 FY2027 revenue surged 88% year-over-year to $43.84 billion, the fastest growth rate since Dell's 2018 return to public markets"* — Dell press release / TradingKey coverage

> *"AI Server Revenue $16.1 billion recognized, with $24.4 billion in orders booked and $51.3 billion backlog reported"* — Dell IR

> *"Full-year revenue guidance was raised 20% to $165–$169 billion from prior range of $138–$142 billion."* — Dell IR

## Wiki updates made

| Page | Update |
|---|---|
| [[DELL]] | Add 2026-05-28 print to Recent developments; update conviction frontmatter (already high) |
| [[ANET]] | **New page** opened — Arista Networks, EtherLink AI portfolio, XPO MSA threat to pluggables, Meta + Microsoft hyperscaler base |
| [[CLS]] | **New page** opened — Celestica, hyperscaler ODM, 10 active 1.6T programs, Google + Meta exposure |
| [[ALAB]] | Recent developments — DELL print read-through; multi-million-unit PCIe Gen 6 pull |
| [[VRT]] | Recent developments — DELL volume validates liquid-cooling cycle |
| [[JBL]] | Recent developments — Dell-adjacent contract mfg validation |
| [[MU]] | Recent developments — DELL print empirically validates UBS LTA framework (May 26) |
| [[bottleneck-roadmap]] | Add MLCC layer as a new flagged bottleneck (Japanese-dominated; wiki coverage gap) |
| [[ai-capex-cycle]] | Top items — DELL $51.3B backlog as demand-side anchor |
| [[overview]] | May 28 daily summary |
| [[log]] | Earnings entry |
| [[index]] | Recent source ingests + ANET + CLS company pages |

## Open questions / what to watch

1. **DELL gross margin trajectory on AI servers** — Dell's "thin margin" historical pattern vs. supply-constrained pricing power
2. **GB300 vs. Vera Rubin transition** — H2 FY27 = Rubin volume; managing dual-platform inventory
3. **Tier-1 hyperscaler vs. Tier-2 mix** — hyperscalers go direct to ODMs (Foxconn/Quanta) historically; Dell's success at Tier-1 is the structural surprise
4. **MLCC supply** — TDK / Murata / Samsung E-M / Yageo are likely to disclose tightening; worth opening dedicated MLCC tracking
5. **PCIe Gen 7 / Scorpio** — ALAB's next-gen positioning at DELL platforms

## Cross-references

- [[2026-05-26-micron-1T-ubs-1625-pt]] — empirically validated by DELL BOM disclosure (memory 10-70% of BOM)
- [[2026-05-27-soitec-fy26-earnings]] — substrate-layer corollary (Vera Rubin H2 FY27 ramp pulls photonic substrates)
- [[2026-05-21-gavin-baker-invest-like-best]] — "$2-3T NVDA unconstrained TAM" framing; DELL print is one quarter's worth of the actual TSMC-constrained run-rate
- [[2026-05-27-anthropic-900B-surpasses-openai]] — Anthropic + OpenAI demand pull = Dell-scale orders downstream
