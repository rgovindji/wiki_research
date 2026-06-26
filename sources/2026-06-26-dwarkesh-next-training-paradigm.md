---
date: 2026-06-26
type: podcast
publisher: Dwarkesh Patel (blog narration / YouTube)
url: https://www.youtube.com/watch?v=20p5-kQXF_Q
raw_path: raw/podcasts/2026-06-26-dwarkesh-next-training-paradigm.txt
touches: [inference-economics, ai-capex-cycle, ai-bubble-debate, bottleneck-roadmap]
---

# Dwarkesh Patel — "What does the next training paradigm look like?"

*Bias: low. Independent commentator/essayist, no financial book; thoughtful and skeptic-leaning on the *current* paradigm's deficits (sample efficiency, continual learning). Follow-up to [[2026-06-20-dwarkesh-sample-efficiency]]. The Mercury segment is a sponsor ad — ignore.*

## TL;DR
- **The labs' AGI bet = RLVR (RL with verifiable rewards) across millions of tasks / thousands of environments will *generalize* into a general agent.** Whether it generalizes is unresolved and empirical; Dwarkesh leans skeptical, citing Dario's context-degradation remark as a hint that short-horizon RL training may not generalize to long-horizon performance. **This is the deepest both-sides for the whole capex/AGI thesis.**
- **"Verifiable isn't enough — a domain must be *grindable*"** (replayable against a deterministic, resettable simulator with thousands of parallel rollouts). That's why coding/math raced ahead and **computer-use lagged** (you can't farm 1,000 parallel Amazon-checkout rollouts). Building high-fidelity app clones is the labor/compute-intensive unlock — and a great coding-RL objective itself.
- **Continual learning is the missing piece, and it requires writing learnings back into the *weights*** — in-context/KV-cache doesn't scale across users; today's online learning only works for one narrow shared objective (Cursor Tab: same target across **400M requests/day**).
- **"Dreaming" / test-time training is floated as a potential *fourth axis of scaling*** (alongside pretraining, RL, inference-time compute): the model writes its own RL environments and trains against them — **"incinerates huge amounts of compute."** Speculative, but a named *new compute sink* if it works.
- **Continual-learning-from-deployment (2027-28 scenario):** capability stops coming mainly from pre-release training and starts coming from **broad deployment** — learning from all users. Makes inference/deployment the capability driver → a distribution/scale flywheel.

## Key facts
- **~30-50% of a lab's compute goes to inference, and that compute "is currently not playing any productive role in helping improve the model"** — Dwarkesh calls it a huge waste/opportunity (continual learning would make deployment compute *also* improve the model).
- **Computer-use lag explained:** verifiable ≠ grindable. Coding works because you can spin 1,000 identical containers; web tasks don't (you can't hammer real Amazon/Slack/Gmail). Cloning apps is currently "labor-intensive and unscalable."
- **RLVR generalization is the crux:** "If the labs went from billions to a *trillion* dollars on RL environments, would you get human-like general intelligence within the context window?" — open question. Dario's quote (context-length you *train* at vs *serve* at → degradation) hints generalization isn't infinitely strong.
- **OPSD (on-policy self-distillation):** distill a long-session "teacher" back into base weights; denser signal than RL, preserves RL's sparse-update property (doesn't overwrite the base model), beats naive SFT. (Ties to [[2026-06-24-dwarkesh-sasha-rush-on-policy-distillation]].)
- **"Dreaming" / test-time training:** /dream instead of /compact — model builds a "video-game version" of what it's seeing and trains against it; potential 4th scaling axis. Analogy: **EfficientZero** (post-AlphaZero) beat novice humans on new Atari games by playing dozens of simulated games per real step.
- **Online learning is narrow today:** Cursor Tab online-learns one objective (which edits got accepted) across 400M req/day; no per-user/per-deployment learning yet because one session isn't enough data to move a model's weights.

## Key claims (and how confident)
- **The RLVR-generalization question is genuinely unresolved (high confidence it's the crux; Dwarkesh's skeptic lean is a *view*, not proof).** If RLVR generalizes → AGI → capex justified. If it doesn't → the "scale solves everything" paradigm hits a wall → bad for the capex bull. Low-bias source makes this a clean both-sides for [[ai-bubble-debate]].
- **"Grindable, not just verifiable" is a real, under-rated constraint (high).** Explains the coding-first reality and implies environment-building (deterministic simulators) + the CPU/sandbox compute to run them is a genuine demand vector (RL-environment vendors + verifier compute).
- **"Dreaming" as a 4th scaling axis (low confidence / speculative, high optionality).** If it works it's a massive new compute-demand vector (bullish [[NVDA]]/memory). Flag, don't underwrite.
- **Continual-learning-from-deployment shifts the capability driver to inference/deployment scale (medium).** Reinforces inference-is-the-future + distribution/data-as-moat; bullish sustained compute on a multi-year horizon, and a flywheel that favors labs/platforms with the most users.

## Quotes worth keeping
> "It is not enough for a domain to be verifiable. It also has to be very grindable... run lots of parallel rollouts against a deterministic and replayable simulator."

> "Around 30 to 50 percent of a lab's compute goes to inference, and that compute is currently not playing any productive role in helping improve the model. This seems like a huge waste."

> "Instead of hitting /compact... you hit /dream. And this incinerates huge amounts of compute to build and train against a video-game version of what the model is witnessing in the real world."

> "If it works, it would become a fourth axis of scaling alongside pretraining, RL, and inference-time compute."

> "The main way that AIs get better is not from the training they have received before they are released... it's from all this experience that they'll be accumulating from being broadly deployed in the economy."

## Wiki updates made
- [[inference-economics]] — the 30-50%-of-compute-is-inference-and-wasted point + continual-learning-from-deployment future + "dreaming"/test-time-training as a potential 4th scaling axis (new compute sink) + the grindable-not-just-verifiable constraint.
- [[ai-capex-cycle]] — "dreaming"/4th-axis + continual-learning-from-deployment as forward compute-demand vectors; RL-environment spend (billions → trillion) as a demand quantum.
- [[ai-bubble-debate]] — the RLVR-generalization-is-unresolved both-sides (low-bias skeptic; Dario context-degradation hint) — the deepest question under the AGI/capex bet.
- [[bottleneck-roadmap]] — "grindable" environment-building (deterministic replayable simulators) as the real constraint on agent progress → RL-environment + CPU/sandbox verifier compute demand.
