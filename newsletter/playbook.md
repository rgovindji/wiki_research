# Playbook — what the letters have learned

This file is the newsletter's accumulated judgment. **Both prompts read it before writing; the close-of-market run updates it.** It grows from one source only: resolved predictions in `predictions.json` and observed process failures. No lesson enters without evidence; every lesson cites the resolution(s) that earned it.

## Rules for maintaining this file

- **Add** at most one lesson per day, only when a prediction resolution or clear process failure teaches something. Cite the prediction id or date.
- **Promote** a Hypothesis to Active only after it's been right twice (or right once in a high-stakes spot with a clean mechanism).
- **Retire** (don't delete) lessons that get falsified — move to Retired with the falsifying evidence. A playbook that only grows is a playbook nobody prunes.
- **Friday close runs** do the weekly distillation: merge duplicates, check Active lessons against the week's resolutions, keep Active under ~20 entries.
- Lessons are written as **operating instructions** ("when X, do Y"), not observations ("X happened").

## Calibration snapshot

As of 2026-06-09: 0 resolved (ledger seeded today). Update this line whenever `predictions.json` calibration changes, including hit rate by confidence tier — if "high confidence" calls don't hit more often than "low", confidence labels are decoration and sizing language must get humbler.

## Active lessons

1. **Guidance beats earnings in a late-cycle tape.** AVGO beat Q2 revenue and EPS on June 3 but guided AI sales flat vs estimates → -14% next day, dragged the whole sector. When previewing a print, frame the guide as the event, not the beat. *(Origin: 2026-06-04 AVGO; wiki feedback-log.)*
2. **One green dip-buy session resolves nothing.** June 8's bounce recovered part of June 5's damage and felt like an all-clear; June 9 opened green and flushed 1.5% by lunch. Don't let a single up session flip the regime call — require a close above a named resistance level. *(Origin: 2026-06-08/09 tape.)*
3. **Small-cap "partnership pop + cash raise" is a rug signature.** Partnership announced with warrants → stock pops → company dumps equity into the pop within 48h. Any high-risk idea in a small cap must check for this pattern first. *(Origin: POET, 4 validations, wiki feedback-log 2026-05-15.)*
4. **Process: no falsifier, no call.** Every "our take" with a directional implication gets a ledger entry with an explicit falsifier, or gets rewritten until it has one. Vague conviction is the failure mode that makes scorecards impossible. *(Origin: ledger design, 2026-06-09.)*

## Hypotheses under test

- **Oil is the tell on war headlines.** Equity reaction to Middle East headlines follows crude, not the headline text — if oil doesn't confirm, fade the equity move. *(Testing via `2026-06-09-oil-is-the-tell`, resolves ~June 16.)*
- **Core-vs-headline asymmetry on energy-driven CPI.** Market can absorb scary headline inflation if core stays tame and the energy driver has a visible off-ramp (ceasefire). *(Testing via `2026-06-09-cpi-core-asymmetry`, resolves June 10.)*
- **Index-inclusion bids defend prices in twitchy tapes.** *(Testing via `2026-06-09-mrvl-inclusion-bid`, resolves June 22. Low confidence on purpose — this one is a genuine experiment.)*

## Data-source notes

*(Live-tested 2026-06-09, ~16:15 CT; Polygon wired ~19:25 CT)*

- **Polygon API (`scripts/market_levels.py`): closes WORK on the free plan.** Exact daily closes for all portfolio tickers + SPY/QQQ, cross-validated against stockanalysis.com on 2026-06-09 (13/13 match). Primary price source — run it first in the close run; it's paced ~3 min on the free tier's 5 req/min. SPY×10 ≈ SPX (ratio 10.02 on 2026-06-09).
- **Polygon gamma: LIVE as of 2026-06-09 evening (Options Starter, $29/mo).** `market_levels.py --audit` computes flip/walls/net GEX from the full SPX chain (~11.7k contracts, ~1 min unpaced). **Day-1 side-by-side vs snippet sources: call wall and put wall 0.00% apart, flip 0.30% apart (computed 7462 via spot-iterated BS-gamma vs 7440 snippet), net GEX −$35B consistent with the short-gamma tape. Audit verdict: pass 6/6.** Trust period: run the audit nightly through ~2026-06-23, log any day the audit fails or levels diverge >1.5%; after a clean run, computed becomes primary and snippets become the cross-check.
- **CBOE delayed chain = free second computed source (wired 2026-06-09 night).** One GET (`cdn.cboe.com/.../\_SPX.json`), full SPX chain with OI/greeks/IV — same feed gamma-desk uses. Day-1 cross-source result: flip 0.05% apart (7462 Polygon vs 7459 CBOE), call wall exact, **put wall disagreed 7300 vs 7385** — which is information, not error: the put side is a ZONE (7300–7385, with the ≤2DTE shelf at 7355 inside) when fresh hedging is stacking up. Letters should describe put-side support as a zone whenever sources disagree; the near-view shelf is the first ledge intraday flows fight, the aggregate wall is the big magnet. (Near-view 7355 independently matched gamma-desk's level.)
- **Flip methodology note:** the cumulative-by-strike "flip" is NOT the flip — in deeply negative regimes it never crosses zero (failed on day 1, 6785 artifact). The real estimate recomputes net GEX across a spot grid using each contract's IV (BS gamma) and finds the sign change. That's what `market_levels.py` does now; if it reports "no zero crossing within ±7%", that itself means deeply pinned short-gamma — say so in the letter rather than inventing a level.
- **Probed the free-plan workaround (2026-06-09) — don't re-litigate.** Free DOES allow: options contract reference and per-contract EOD price bars (200s). Free does NOT allow: greeks or open interest anywhere (snapshots 403, open-close 403). No OI = no positioning data = no real walls; volume-weighted proxies measure activity, not positioning. (Historical note — account upgraded same day.)
- **Gamma levels (zero-gamma flip, call/put walls): WORKS via WebSearch snippets, not direct fetch.** Query shape that worked: "SPX zero gamma flip level call wall put wall {date}" — Barchart/InsiderFinance/OptionCharts pages get indexed and the snippet carries the numbers. Direct WebFetch of those pages is paywalled/JS-blocked; don't bother. **Mandatory sanity check before using a level:** it must cohere with the tape (2026-06-09: put wall 7300 vs defended low 7297 — pass). A level that doesn't line up with recent price action is stale; drop it.
- **VIX: level findable same-day via search** (intraday reads from StreetStats and similar get indexed); closing value sometimes lags to next morning. Term structure (front vs 3-month) rarely surfaces in snippets — treat as a bonus, not a required field.
- **Put/call ratio: lags 1-2 trading days** in free sources (ycharts/MacroMicro index CBOE data late). Use it as positioning *context*, never as a same-day signal.
- **Unusual options activity: NOT reliably sourceable free.** Aggregators (OptionStrat, Barchart UOA, OptionCharts trending) are paywalled or JS-rendered; fetch returns navigation shells. Searches return education pages, not trades. Only include flow when a specific large trade made the *news* (e.g., a reported Burry-style position) — and then it's one corroborated fact, not a feed. Revisit if a paid source is added.

## Retired

*(empty — falsified lessons land here with the evidence that killed them)*
