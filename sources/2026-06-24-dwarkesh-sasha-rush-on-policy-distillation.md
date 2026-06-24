---
date: 2026-06-24
type: podcast
publisher: Dwarkesh Patel (clip w/ Sasha Rush, Cursor)
url: https://www.youtube.com/watch?v=wxOZWD6wYVY
raw_path: raw/podcasts/2026-06-24-dwarkesh-sasha-rush-on-policy-distillation.txt
touches: [inference-economics, ai-software-disruption]
bias_flag: LOW-MED — Cursor researcher describing Cursor's own training method; technical, not a market call, but talks his employer's model
---

# Sasha Rush (Cursor) on on-policy / off-policy self-distillation — how Composer 2.5 was trained (Dwarkesh clip)

## TL;DR
- A **technical truth-layer** explainer (Tier-3) on how **Cursor's in-house coding model, Composer 2.5**, was trained — confirming Cursor is doing its *own* frontier RL post-training, not just wrapping someone else's model.
- The method (**off-policy self-distillation**): with *no* better teacher model available, Cursor *synthesizes* a teacher by injecting targeted **text feedback** into a rollout's trajectory at the exact spot a reader-model flags an error, then re-scores log-probs and back-props it alongside RL. Improves **credit assignment** in long (hundreds-of-turn) agentic RL.
- **Honest limiter (cuts against "training is getting trivially cheap"):** Rush says it is *"not at the point yet where it replaces aspects of RL"* — runs *in conjunction with* full RL, only fixes *"easily identifiable"* errors, and yields *"slightly better, a little bit at a time"* local corrections, not step-changes.

## Why it matters (investable signal — modest)
- **Vertical model strategy is real at the app layer.** Cursor training a competitive coding model with novel methods is a datapoint for the [[ai-software-disruption]] survivor debate: the strongest application-layer players are moving *down* the stack into their own models (margin + moat), not staying pure wrappers.
- **Marginal training-efficiency win.** Targeted text-feedback distillation gets specific errors fixed *"much quicker than the full RL process"* — a small tailwind to the cost-of-RL / inference-economics curve. But the explicit *"doesn't replace RL"* caveat is a check on the bull claim that post-training is collapsing toward free — it's incremental, not a regime change. Neutral-to-mildly-supportive for the RL-compute-demand (NVDA/compute) side.
- No tickers, no capex numbers, no dated catalyst — included as the Tier-3 technical balance to the day's Tier-1 CEO promo, not as a position-mover.

## Quotes worth keeping
> "We don't have a better model, but we can pretend we have a better model... the feedback is going to be this extra information that we inject into this trajectory."
> "It's not at the point yet where it kind of replaces aspects of RL — we're still doing this in conjunction with the actual system."
> "It is a frustrating aspect of modern RL that even though we can read trajectories and they're bad... we can't inject that information directly."

## Wiki updates made
- Patched [[inference-economics]] — small dated bullet: Cursor Composer 2.5 off-policy self-distillation = marginal RL-efficiency win, but "doesn't replace RL" (sources bump).
- Patched [[ai-software-disruption]] — datapoint: app-layer leaders (Cursor) moving into in-house frontier models.
