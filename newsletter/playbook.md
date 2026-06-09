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

- Gamma levels (zero-gamma flip, call/put walls): not yet sourced. Try SpotGamma/Menthor Q/OptionCharts commentary via search; log here which source actually yields numbers, and at what time of day they're fresh.
- Unusual options activity: treat single-source flow reports as weak evidence; they're often stale or misread. Two corroborating sources or it stays out of the reasoning.

## Retired

*(empty — falsified lessons land here with the evidence that killed them)*
