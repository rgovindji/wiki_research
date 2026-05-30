---
date: 2026-05-29
type: analysis
publisher: wiki (synthesis)
url: n/a
raw_path: n/a
touches: [DELL, ANET, CLS, ALAB, VRT, MOD, NVT, JBL, APH, MU, IBDXY, AJINY, bottleneck-roadmap, ai-capex-cycle, watchlist]
---

# DELL-Upstream Second-Derivative — Which Suppliers the Market Hasn't Priced In Yet

User prompted the question 2026-05-29: *"If you feel like you're late, there's a lot of implications to Dell's upstream suppliers that markets might not have priced in yet."*

This synthesis answers it. Anchored on [[2026-05-28-DELL-Q1-FY27-earnings]] — the largest single-quarter AI server print in corporate history (revenue +88% YoY to $43.84B; AI server rev +757% YoY to $16.1B; **$51.3B AI backlog**; **FY27 guide raised 20% to $165-169B**).

## The framework

**The setup**: DELL has *already* moved on the print (+40% AH initially). The "easy money" on DELL itself is at least partly behind. But DELL is an integrator — its margin per unit is thin, and most of the value capture flows upstream. The question becomes: *which upstream layer has the most unre-rated valuation relative to the demand pull DELL has now confirmed?*

**The decision rule we're applying**: A name is "not yet priced in" when (1) it has direct DELL bill-of-materials exposure, (2) its valuation has not seen a structural reframing event (UBS-style PT step-change), and (3) its post-earnings reaction has been "garden variety beat priced in" rather than rerated.

## Tier A — under-priced upstream (cleanest entry)

### 1. **[[ANET]] — Arista Networks** *(new wiki page 2026-05-29)*
- **What it makes for DELL upstream**: 800G + 1.6T leaf-spine Ethernet at hyperscaler scale; EtherLink AI portfolio
- **DELL read-through**: every DELL XE9812 / XE988x customer that's not InfiniBand-only buys Arista at the spine
- **Why under-priced**: stock fell **-14% post Q1 2026 earnings (May 5)** despite raising AI revenue target to $3.5B and FY26 guide to $11.5B. "Garden variety beat priced in" pattern — same exhausted-buyer dynamic that hit [[NVDA]] and [[CBRS]]
- **Tradeoff**: P/E 52.84 is structurally elevated; NVDA NVLink + Spectrum-X is the existential rack-fabric competitor (NVDA networking +199% YoY vs. ANET +35% YoY)
- **Stance**: bull / medium-high

### 2. **[[CLS]] — Celestica** *(new wiki page 2026-05-29)*
- **What it makes for DELL upstream**: hyperscaler ODM contract mfg, specifically the actual hardware for ANET / AVGO networking platforms; 10 active 1.6T networking programs disclosed Q1 2026
- **DELL read-through**: DELL backlog → ANET design wins → CLS builds the boxes
- **Why under-priced (relative)**: stock hit ATH $422.21 April 27 — the AI-CM trade has worked, but CLS gives you **structurally lower beta to AI capex than ANET itself** while still capturing the 1.6T ramp. Headline framing per Seeking Alpha: "The AI Infrastructure Winner No One Wanted This Quarter"
- **Tradeoff**: contract-mfg historical low-margin pattern; customer concentration at Google + Meta; 8% adj op margin is already a multi-year high
- **Stance**: bull / medium-high

### 3. **[[ALAB]] — Astera Labs**
- **What it makes for DELL upstream**: PCIe Gen 6 retimers + Scorpio AI fabric switches
- **DELL read-through**: each DELL XE9812 rack uses **dozens of PCIe Gen 6 retimers**. DELL's $16.1B AI server rev this quarter = ~50-100K racks = multi-million-unit PCIe retimer pull from one OEM in one quarter
- **Why under-priced**: had a +12.58% one-day move May 19 on Evercore PT raise, but otherwise still trades on Q1 fundamentals (rev $308M, Q2 guide $355-365M) — those numbers likely look conservative against DELL volumes
- **Tradeoff**: hyperscaler customer concentration; NVDA NVLink is the bear case at rack-fabric
- **Stance**: bull / medium-high — conviction under active review for potential upgrade if Q2 print beats materially

## Tier B — sympathetic but partially priced in (good entries but less leveraged)

### 4. **[[VRT]] — Vertiv** (liquid cooling)
- GB300 power density (~135 kW/rack) at air-cooling limit; Vera Rubin NVL72 even higher
- Citi $414 PT (May 7); $1B high-density cooling acquisition Feb 2026
- Less leveraged than Tier A but cleaner entry than the substrate names; Goldman May 17 basket co-member

### 5. **[[MOD]] — Modine** (cooling sub-scale specialist)
- Performance Technologies SPINOFF catalyst
- 60%+ DC growth FY26
- Goldman May 17 basket co-member

### 6. **[[NVT]] — nVent** (liquid cooling enclosure + power)
- Q1 2026 +53% YoY; $2.3B backlog 3x
- <10% DC penetration today
- Goldman May 17 basket co-member

### 7. **[[JBL]] — Jabil** (contract mfg, diversified)
- AI revenue $13.1B FY26 (+46%)
- Lower beta than CLS due to humanoid + medical diversification; higher embedded optionality (Apptronik, NC megafactory)

### 8. **[[APH]] — Amphenol** (interconnect)
- Stargate signal win; AI rack interconnect
- Already in wiki bull; more priced in than ANET/CLS

## Tier C — already rerated this week (skip if you're "late")

### 9. **[[MU]] — Micron**
- **Just rerated +19% May 26** on UBS PT $1,625 (3x raise). Crossed $1T market cap. UBS reframed as AI infrastructure stock not cyclical commodity. **Not under-priced anymore** — this is the most recently rerated name in the stack.
- DELL print empirically validates UBS LTA framework (memory 10-70% of Dell's BOM)
- Still bull / high conviction but **entry today is into momentum, not dislocation**

### 10. **[[IBDXY]] — Ibiden** + **[[AJINY]] — Ajinomoto** + **[[SSEHY]] — Samsung Electro-Mechanics** + **[[ATSAY]] — AT&S** + **[[UNIMICRON]]**
- ABF substrate stack has moved 6-20x off lows; bottleneck-pricing-power thesis is now consensus
- DELL print validates demand but valuation already reflects it

### 11. **[[SOITEC]] — Soitec**
- Just printed FY26 May 27 with Photonics-SOI >$100M ahead of plan; stock +20.7% post-print
- **Just rerated this week** — conviction upgraded low-medium → medium

## Tier D — wiki coverage gap surfaced by the DELL print (action items)

### 12. **🆕 MLCC layer — Japanese-dominated, ZERO wiki coverage**
- **Each GB300 rack requires ~440,000 multilayer ceramic capacitors** for power filtering + decoupling
- DELL's AI server pace = potentially **billions of MLCCs/year from one OEM customer alone**
- Public-market exposure (none in wiki today):
  - **TDK Corp** (TDK / TTDKY) — Japanese, large diversified electronics; MLCC + battery + sensor
  - **Murata Manufacturing** — Japanese, world's largest MLCC supplier (~40% global share); high-end stickiness
  - **Samsung Electro-Mechanics** ([[SSEHY]] — already in wiki for ABF substrates; **dual-exposed to MLCC + ABF** — under-appreciated optionality)
  - **Taiyo Yuden** — Japanese; pure-play MLCC; smaller scale
  - **Yageo** — Taiwanese; KEMET acquisition (Q3 2020); growing global share
- **Verdict**: this is the **single biggest wiki coverage gap** the DELL print exposed. The "SSEHY dual exposure" framing is the most under-priced single name relative to the bottleneck reality

## The bottom line — if you're "late"

**Three names to focus on**, in order of cleanest under-pricing:

| Rank | Name | Stance | Why now |
|---|---|---|---|
| 🥇 | **[[ANET]]** | bull / medium-high | -14% post-earnings on raised guide; XPO MSA optionality; cleanest hyperscaler Ethernet pure-play |
| 🥈 | **[[CLS]]** | bull / medium-high | Lower beta than ANET; 10 active 1.6T programs locked in; "winner no one wanted" framing |
| 🥉 | **[[ALAB]]** | bull / medium-high (upgrade candidate) | DELL volumes likely make Q2 guide conservative; Gavin Baker explicit positive call May 21 |

**Plus a contrarian/under-explored angle**: open MLCC tracking on **TDK / Murata / [[SSEHY]] dual-exposure**. The 440K MLCC/rack number is the most under-discussed bottleneck in the entire AI buildout — and it's hiding inside Japanese conglomerates and the existing SSEHY page.

## Risk caveats

- The whole AI-capex factor is correlated; loading up on ANET + CLS + ALAB + VRT + JBL + APH + DELL + NVDA = single-factor exposure
- Hyperscaler capex moderation risk (Damodaran framework) is still live — DELL Q1 doesn't disprove it
- The exhausted-buyer pattern (NVDA -2% post-Scenario-A; CBRS -25% from peak; ANET -14% post-raised-guide) suggests the marginal AI buyer has been priced in across the stack — entry sizing should reflect that

## Cross-references

- [[2026-05-28-DELL-Q1-FY27-earnings]] — the primary anchor
- [[2026-05-26-micron-1T-ubs-1625-pt]] — MU as the "already rerated" reference point
- [[2026-05-27-soitec-fy26-earnings]] — substrate-layer first-print parallel
- [[2026-05-21-gavin-baker-invest-like-best]] — ALAB miscategorization framing
- [[bottleneck-roadmap]] — MLCC layer added 2026-05-29
