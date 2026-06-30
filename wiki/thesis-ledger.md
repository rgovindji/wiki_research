---
type: thesis-ledger
tags: [thesis-ledger, current-beliefs, synthesis]
last_updated: 2026-06-30
last_full_review: 2026-06-30
---

# Thesis Ledger — the wiki's current beliefs

**Read this first, every session.** This is the compact, always-loaded spine: the live cross-cutting theses that drive the book, each with a stance, an honest conviction, the load-bearing evidence (links), and the **falsifier** that would change the mind. It is deliberately small — for per-name stances see [[watchlist]]; for the day-by-day tape see [[overview]]; for any detail, run `wikidb ask` and read the linked page.

> **How to use:** start from the relevant thesis here, then `wikidb ask` to pull the current evidence, then answer. **How to maintain:** when a source moves a thesis's evidence, conviction, or falsifier, edit the entry and date it (don't append). Conviction is honest — risk theses are first-class, not footnotes. Stance flips need user sign-off.

---

## Demand & the cycle

### T1 · AI capex cycle — expanding, not yet topping
**Stance:** intact · **Conviction:** medium-high · **Updated:** 2026-06-26
Supply-side (AMAT raised CY26 WFE to >30%, Cisco AI orders $5B→$9B) and demand-side (ORCL RPO $638B, Anthropic $30B ARR, inference already the majority → 80%+) keep confirming. **No hyperscaler has cut capex guidance** — that's the master switch.
**Falsifier:** a hyperscaler cuts Q2 capex guide *with* cloud-rev deceleration + shrinking RPO (= demand crack); or memory contract prices / CoWoS lead times roll over. **Next read: late-July Q2 prints.**
→ [[ai-capex-cycle]] · [[inference-economics]] · [[ai-value-migration-capex-unwind-playbook]]

### T2 · Inference economics is the better lens than raw capex
**Stance:** rising importance · **Conviction:** medium · **Updated:** 2026-06-28
Inference is already the majority of compute (RL post-training + synthetic data are inference workloads); the demand bid under [[NVDA]]/[[CRWV]]/[[NBIS]]/memory survives even if *pretraining* scaling plateaus. Per-task cost falls 10–100×/cycle (deflationary for app-layer) but TAM expands (Jevons). Margin accrues to whoever captures the serving layer.
**Falsifier:** inference demand fails to inflect with capacity; spot GPU rents roll over for two+ quarters.
→ [[inference-economics]] · [[ai-software-disruption]]

### T3 · Memory super-cycle — ASP-led, the cleanest pricing leg
**Stance:** intact · **Conviction:** high (with a cyclical caveat) · **Updated:** 2026-06-23
WSTS: 2026 memory ~+250% YoY to >$800B (the majority of the year's semi growth); DRAM contract +90% in Q1. [[MU]] is the preferred NVDA HBM supplier, sold out through 2026. **Caveat to bank:** distinguish *durable HBM franchise* from *cyclical rent-capturer* (commodity DRAM/NAND).
**Falsifier:** DRAM/HBM contract prices decelerate; Samsung HBM4 share gains compress MU's premium; a take-or-pay counterparty walks a floor.
→ [[MU]] · [[semiconductors]] · [[bottleneck-roadmap]]

## Supply & structure

### T4 · The chokepoints are the durable moats — [[ASML]], [[TSM]]
**Stance:** intact · **Conviction:** high · **Updated:** 2026-06-20
Two high-credibility voices (Patel, Katti) call ASML "the single choke point of the whole supply chain"; all advanced AI silicon flows through TSMC, whose wafer allocation *structurally* guarantees a multi-vendor silicon market. These survive a capex wobble better than the rented-shovel layer.
**Falsifier:** a credible EUV alternative materializes (xLight ~2028+); a real second-source appears at the advanced node.
→ [[ASML]] · [[TSM]] · [[bottleneck-roadmap]]

### T5 · Custom silicon coexists with NVDA — it doesn't displace it
**Stance:** intact · **Conviction:** medium-high · **Updated:** 2026-06-29
AVGO/MRVL/QCOM each win sockets, but TSMC wafer allocation + the CUDA moat keep NVDA the platform; the custom-ASIC moat is *contestable, not won* (AVGO/MediaTek traded TPU SerDes sockets in a single week). [[NVDA]] held bull/high (at ceiling).
**Falsifier:** a custom-silicon socket materially erodes NVDA share/margins; BUDA/Modular-style portability dents CUDA in production.
→ [[NVDA]] · [[AVGO]] · [[QCOM]] · [[semiconductors]]

### T6 · Power/grid + construction labor = most defensible AI-infra exposure
**Stance:** intact · **Conviction:** high · **Updated:** 2026-06-29
Backlogs lock pricing forward and carry lower duration than the chip names: [[VRT]]/[[ETN]]/[[GEV]] (power & cooling) and [[FIX]]/[[EME]]/[[PWR]] (mech/electrical/grid, ~$76B contracted). **Caveat (Dylan):** power may not be *the* single binding constraint — wafers/packaging compete.
**Falsifier:** backlog conversion stalls; a behind-the-meter / power glut emerges; equipment lead times start compressing.
→ [[datacenter-construction]] · [[bottleneck-roadmap]] · [[ai-capex-cycle]]

### T7 · Neoclouds — owned-power + goodput quality survives; dumb shells don't
**Stance:** intact · **Conviction:** medium · **Updated:** 2026-06-30
Real-TCO varies 10–50% at identical GPU price once goodput is counted, so operators with software/optimization + owned power ([[NBIS]]) screen above commodity shells against the Chanos short. [[NBIS]] bull/medium (great company, demanding price); [[CRWV]] bull/high but more commodity-exposed.
**Falsifier:** spot GPU rents roll over; a hyperscaler insources; a dilutive convert wave lands in a weak tape.
→ [[NBIS]] · [[CRWV]] · [[2026-06-30-nbis-neocloud-buy-zones]] · [[inference-economics]]

## Risk & macro

### T8 · Not a fundamentals bubble — yet; it's a positioning/valuation risk
**Stance:** "NOT a top call" · **Conviction:** medium · **Updated:** 2026-06-26
Earnings are real (real GMs, signed commitments, largely self-funded capex) — unlike 1999. But CAPE ~39.8 (highest since 2000) and Mag-7 ~35% of the S&P (matching the dot-com peak) mean **sentiment alone can compress the multiple** without fundamentals breaking. Position-management framework fires when 3+ late-cycle indicators are simultaneously on (current state).
**Falsifier (to *real* bear):** a demand crack (capex cut + backlog shrink), or the AI-infra-debt contagion (T9) fires.
→ [[ai-bubble-debate]] · [[valuation-environment]] · [[market-concentration]]

### T9 · AI-infrastructure debt is the systemic contagion vector
**Stance:** watch-flag · **Conviction:** medium on existence, low on timing · **Updated:** 2026-06-20
~$120B of DC debt shifted off bank balance sheets via SRT into private credit/insurance/pensions; AI = >33% of 2025 private-credit deals. The closest 2008-style transmission mechanism — even if the capex itself is justified.
**Trigger/falsifier:** a credit event at a named DC borrower (ORCL-leased, tier-2 neoclouds); lab lockup-expiry deleveraging. Absence of stress over several quarters de-risks it.
→ [[ai-infrastructure-debt]] · [[financials]] · [[ai-bubble-debate]]

### T10 · Rates/macro is the binding overlay — higher-for-longer
**Stance:** intact · **Conviction:** medium-high · **Updated:** 2026-06-17
Warsh's first FOMC was hawkish (dots show a 2026 *hike*; PCE marked up; 30Y >5%; supercore sticky). Higher-for-longer marks down the longest-duration multiples first (GOOGL/MSFT/META before short-cycle AI-hardware) — a rotation driver, not a demand signal.
**Falsifier:** inflation cools decisively (cuts back on the table) → duration bid returns; or an actual hike lands → sharper repricing.
→ [[fed-policy]] · [[inflation-tariffs]] · [[valuation-environment]]

## Operating posture

### T11 · Regime: bull-under-stress → barbell, don't chase
**Stance:** current posture · **Conviction:** n/a (this is the playbook) · **Updated:** 2026-06-26
Index below the ~7,450 dealer-gamma flip; the 7,300 floor has held on a closing basis. Discipline: **hold structural compounders at reduced size · trim the leveraged cyclical/duration tails (commodity memory, rate-sensitive neoclouds) · bias adds to backlog-protected infra (T6) · keep hedges + dry powder for the air-pocket the "first capex cut gets misread as the bubble" dynamic implies.**
**Falsifier of the posture:** a close back above ~7,450 with breadth (shock absorbers re-stack → add) or a confirmed demand crack (de-risk broadly).
→ [[overview]] · [[hedging-risk]] · [[ai-value-migration-capex-unwind-playbook]]

---

## Open calls awaiting user sign-off
- **[[NBIS]]** — hold bull/medium vs downgrade to neutral at current valuation? (06-29 pullback-and-reclaim eases, doesn't resolve.) → [[2026-06-30-nbis-neocloud-buy-zones]]
- **[[GOOGL]]** — 5+ straight closes below Berkshire's $350 mark flagged ("googl-buffett-floor").
- **Memory (T3)** — the 05-13 grid says "hold, don't trim"; the 06-29 late-cycle framework says "trim the leveraged cyclical." More recent view leans trim.

## Related
[[overview]] · [[watchlist]] · [[ai-bubble-debate]] · [[ai-capex-cycle]] · [[inference-economics]] · [[bottleneck-roadmap]]
