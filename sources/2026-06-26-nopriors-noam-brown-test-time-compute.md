---
date: 2026-06-26
type: podcast
publisher: No Priors (Sarah Guo / Conviction)
url: https://www.youtube.com/watch?v=AZrU6y3pUcU
raw_path: raw/podcasts/2026-06-26-nopriors-noam-brown-benchmarks.txt
touches: [inference-economics, ai-bubble-debate, bottleneck-roadmap, ai-software-disruption, ai-capex-cycle]
---

# Noam Brown (OpenAI) on No Priors — test-time compute, broken evals, and why there's no overnight takeoff

Tier-3 source. Noam Brown is the OpenAI research scientist who pioneered reasoning / inference-time
(test-time) compute (poker/Diplomacy → o-series). Published 2026-06-26, ~7,700-word transcript.
**Bias flag:** OpenAI insider — incentive to frame test-time compute (and therefore inference demand)
as the central scaling axis (bullish OpenAI's compute story). BUT his headline call (no fast takeoff,
time-bottlenecked, gradual) cuts *against* AI hype, which raises its credibility.

## TL;DR
- **Model capability is now a function of dollars/compute you spend at inference.** "$10 vs $10K vs
  $10M budget" produce very different results on the same model — unlike GPT-3, where extra test-time
  compute bought almost nothing. Benchmarks that report one number per model are now "measuring the
  wrong thing" because they don't control for test-time compute.
- **GPT-5.5's real gain over 5.4 is efficiency, not a headline-benchmark jump.** On the grid 5.5 looked
  only "a few percentage points" better; controlling for thinking time, it's a "substantial jump" — 5.5
  reaches the same answer with far less test-time compute. Day-to-day users felt it; the grid hid it.
- **No overnight intelligence explosion.** Because top capability *requires* large-scale test-time
  compute, "time itself becomes the bottleneck" — models must run for weeks/months to do the powerful
  stuff. RSI is "transforming researchers, not replacing them"; gradual takeoff, not instant superhuman.

## Key facts / claims (and confidence)
- **Test-time-compute scaling is far from plateau.** Modern models, "scaffolded reasonably well, can
  think for weeks" before benchmark performance plateaus — vs GPT-3 (2022) which plateaued fast. US AI
  Safety Institute cyber evals reportedly *still improving at 100M tokens*. (High confidence it's his
  view; the 100M-token figure is a specific, checkable claim.)
- **Latent capability overhang in *already-released* models.** OpenAI used an internal model to disprove
  the Erdős unit-distance conjecture "at a dirt-cheap budget." Post-hoc, people extracted the same
  disproof from public **GPT-5.5** with a general-purpose scaffold — est. **$1K–$100K of inference per
  run**. "Nobody had explored what $100K of compute into 5.5 could do." → enormous untapped inference
  demand sitting in deployed models. (Med-high; the dollar range is his ballpark.)
- **Per-task cost deflation: 10–100×+ per release cycle**, and cycles are now **every ~2–3 months**.
  The "why engineer when the next model makes it 100× cheaper in two months" meme — he half-concedes it.
- **Eval/safety gap:** responsible-scaling / preparedness frameworks were built in the ChatGPT era and
  "don't account for test-time compute" — they ask "what can the model do?" when the real question is
  "at what budget?" The only way to *fully* know what an agent can do after a month is to run it a month
  — impossible inside a 2–3 month release cadence under competitive pressure. (His central essay thesis.)
- **Where test-time compute does NOT help:** factual retrieval (knowing Lincoln's birthdate doesn't
  improve with a week of thinking) and **research taste** (models still can't synthesize the literature
  into a genuinely novel better algorithm, even given lots of time). Sudoku-like search problems are the
  opposite extreme (improve without limit). Real tasks live in between.
- **Routing-layer skepticism (investable):** model-router / "consensus among models" middleware shows
  benchmark gains, but "once you control for test-time compute, is it actually doing better than just
  letting one model think longer?" Often the gain is benchmark-specific and doesn't survive real use.
- **Trust:** he now trusts model output for tax/real-estate decisions "arguably more than an expert human."

## Why it matters (investable read)
- **Inference-demand bullish, structurally.** If capability scales with inference spend and there's a
  $100K-scaffold overhang in *today's* models, the demand ceiling for inference compute is far higher
  than current utilization implies. Efficiency gains (5.5) don't shrink demand — they get spent on
  harder/longer tasks (Jevons). Feeds [[inference-economics]] and the bull leg of [[ai-capex-cycle]].
- **Tempers BOTH bubble extremes.** A credible OpenAI insider says there is **no imminent hard takeoff**
  — progress is fast but *time-bottlenecked* and gradual. That undercuts the "AGI any minute justifies
  any capex" bull AND the "it's all hype, nothing works" bear. Base case = intense, grinding competition
  among the labs. Logged to [[ai-bubble-debate]].
- **Per-task cost falls 10–100×/cycle** → deflationary unit economics for app-layer software, but TAM
  expands as new tasks become affordable. Relevant to [[ai-software-disruption]] (and the routing-layer
  middleware moat question — he's skeptical it's durable value).

## Contradictions / tensions to surface
- **vs the "AI capex is a bubble, demand is fabricated" bear** ([[ai-bubble-debate]]): Brown argues the
  opposite — real, under-exploited inference demand overhang. But note the bias: an OpenAI scientist
  benefits from "buy more inference." Weigh against the bear's unit-economics case, don't let it override.
- **vs "imminent RSI / fast-takeoff" bulls:** Brown explicitly rejects overnight intelligence explosion.

## Quotes worth keeping
> "We're in a world now where the capability of the model is a function of how much money you put into it."

> "Nobody actually knows what the ceiling of capabilities are for these models because nobody's actually
> run them for long enough to really tell."

> "Ultimately I think the biggest bottleneck for all of us is time… that's why all the researchers are
> working so intensely right now."

## Wiki updates made
- [[inference-economics]] — test-time-compute-as-demand-driver + the $100K-scaffold overhang; routing-layer skepticism.
- [[ai-bubble-debate]] — credible-insider "no fast takeoff, time-bottlenecked" datapoint (tempers both extremes).
- [[bottleneck-roadmap]] — "time is the bottleneck" framing alongside power/wafer.
- [[ai-software-disruption]] — per-task cost deflation 10–100×/cycle + routing-middleware moat doubt.
