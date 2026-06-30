---
type: analysis
tags: [ai, neocloud, gpu-cloud, technicals, buy-zones]
last_updated: 2026-06-30
last_full_review: 2026-06-30
sources: 4
---

# NBIS — Neocloud Thesis + Buy Zones (as of 2026-06-29)

> **Verdict:** Great company, demanding price. Highest-quality public [[NBIS|neocloud]], thesis validated by Q1 — but priced like it. **Bull / medium.** Don't chase $261; accumulate in the marked buy zones. Prices Polygon-verified (close 2026-06-29). Companion artifact: `nbis_analysis_2026-06-29.html` (marked TradingView chart).

## Snapshot (verified — Polygon, 2026-06-29 close)
| Metric | Value | Note |
|---|---|---|
| Last (close) | **$261.15** | 2026-06-29 |
| Recent high | $299.86 | intraday 06-22 ($286.69 close 06-18) |
| Recent low | $234.40 | 06-26; retested $234.50 on 06-29 |
| Market cap | ~$62B | approx, at last |
| EV / ARR | ~32× / ~8× | trailing $1.92B / forward $7–9B target |
| 2026 rev guide | $3.0–3.4B | vs $530M in 2025 |
| Consensus PT | ~$242 | below spot; wide dispersion |
| 2026 capex | $20–25B | vs ~$3.2B revenue |

## Thesis in one paragraph
NBIS printed the strongest quarter any public neocloud has reported (Q1: rev +684% to $399M, profitable on Adj EBITDA at a 45% margin, $2.26B operating cash flow), backed by [[NVDA]]'s $2B stake and ~$44B of combined Microsoft + Meta contracts. The operational debate is settled; the live debate is **price**. The headline profit is mostly a non-cash ClickHouse revaluation (core ops still lose ~$100M/qtr), the Street's 12-mo target sits *below* spot, and FY26 capex of $20–25B on ~$3.2B revenue (~40% equity-funded via serial converts) is a real dilution vector. Underwrite on EV/ARR, not the P/E.

## Why it's the quality name (vs [[CRWV]])
- **Owned power** — ~4GW contracted for 2026, "sold out again," 4+ customers per cluster. Power, not GPUs, is the binding constraint.
- **Least commodity-like neocloud** — real software/optimization + a goodput moat ([[2026-06-28-semianalysis-true-cost-gpu-cluster]]) answers the "neoclouds = dumb shells" short; a semis L/S CIO singled NBIS out by name ([[2026-06-23-chanos-zlatev-ai-capex-debate]]).
- **Spot-inference optionality** — only ~50–60% contracted; the other ~40–50% sold at spot captures the +40–50%-since-January GPU rent inflection (cuts both ways). vs CRWV ~98% contracted at ~7× sales — cheaper stock, more commodity-exposed.

## Bear case / what breaks it
Demanding multiple with consensus PT below spot · "profit" is a non-cash mark · **extreme customer concentration** (MSFT + Meta *are* the story; Meta's ~$27B is a backstop, not dedicated demand) · dilution risk from the capex/convert math · fast GPU depreciation · legacy post-Yandex perception · macro multiple-compression overlay. Full bull/bear on [[NBIS]].

## Technicals & buy zones (daily, computed from Polygon via `scripts/ticker_ta.py NBIS`)
**Setup:** strong uptrend — price above a rising 50- and 200-EMA. Ran ~$200→$300 in June, gave back ~22% to $234.40 (06-26), then on 06-29 retested $234.50 intraday and reversed hard to close $261.15 — a double-bottom that reclaimed the 20-EMA ($248). Recent down-gaps (06-23, 06-26) already filled on the bounce → no near-term gap magnet; structure + EMAs are the guides.

| Level / zone | Price | What it is | How to use |
|---|---|---|---|
| Resistance | $287–300 | 06-18 close / 06-22 high | must clear to resume uptrend; trim/trail into it |
| Last | $261.15 | 06-29 close, above 20-EMA | mid-range — not an entry |
| **Buy Zone A** | $246–252 | reclaimed 20-EMA ($248) | momentum add if it pulls back and holds; lower conviction |
| **Buy Zone B ★** | $232–240 | double-bottom support ($234) | preferred R/R — defined risk, stop below $234 |
| **Buy Zone C** | $200–215 | breakout base ($200) + rising 50-EMA ($215) | deep-flush add zone; size here if the AI tape sells off |

**EMAs (06-29):** 20 = $248.42 · 50 = $215.30 · 200 = $140.44. **Invalidation:** a daily close below **$234** opens the 50-EMA / $215, then the $200 base.

## Falsifiers / tells to watch
- **Q2 print (master switch)** — does Adj EBITDA profitability hold?
- **ARR march to $7–9B** — any stall breaks the forward-multiple math.
- **A third hyperscaler customer** — the best de-risk on concentration.
- **Convert / equity issuance into a weak tape** — the dilution trigger.
- **Spot GPU rents rolling over** — the ~40–50% spot leg cuts both ways.
- **Technical:** daily close < $234.

## My read
Hold [[NBIS]] at **bull / medium** — strongest operational case in the group with a genuine owned-power + goodput moat, but forward returns are now a price question gated on Q2 durability and orderly financing. Don't chase $261. Accumulate in **Zone B ($232–240)**, back up the truck in **Zone C ($200–215)**, treat a close below $234 as the stop. This also informs the open curator question on the [[NBIS]] page (hold bull/medium vs downgrade to neutral): the 06-29 pullback-and-reclaim eases — but does not resolve — the valuation argument; **hold bull/medium**.

## Related
[[NBIS]] · [[CRWV]] · [[inference-economics]] · [[ai-capex-cycle]] · [[ai-bubble-debate]]

## Sources
1. `wiki/companies/NBIS.md` + [[2026-06-19-nebius-inflection-event]] · [[2026-06-23-chanos-zlatev-ai-capex-debate]] · [[2026-06-28-semianalysis-true-cost-gpu-cluster]]
2. Polygon API (daily OHLC, verified 2026-06-29) via `scripts/ticker_ta.py`
3. [TIKR — NBIS +167% in 2026](https://www.tikr.com/blog/nbis-has-gained-167-in-2026-the-revenue-chart-explains-why) · [Seeking Alpha — NBIS](https://seekingalpha.com/symbol/NBIS)
