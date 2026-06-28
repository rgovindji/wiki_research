---
date: 2026-06-28
type: podcast
publisher: Latent Space (Cooking series)
url: https://www.youtube.com/watch?v=fpAthTtha8c
raw_path: raw/podcasts/2026-06-28-latentspace-mark-chen-openai.txt
touches: [ai-bubble-debate, inference-economics, ai-capex-cycle]
bias_flag: HIGH — Mark Chen is OpenAI's Chief Research Officer; maximally talks his book on scaling/AGI. Treat scaling-conviction claims as the strongest bull-side framing, not neutral evidence.
---

# Mark Chen (OpenAI Chief Research Officer) — Latent Space "Cooking" interview

## TL;DR
- OpenAI's research chief "firmly" rejects every bear take on scaling: pre-training is **underrated, not dead**; scaling laws "held for almost 10 orders of magnitude, no reason it should not keep holding."
- "AGI is coming soon." OpenAI's **3-year roadmap goal = end-to-end autonomous research** — models that generate the ideas, have research taste at parity, and do self-sustaining research. He thinks the remaining big bets are few and the window before models drive the innovation is "small."
- Research is already shifting to **orchestration**: "vibe researchers" supply taste/ideas, the model does implementation/execution. Plus an **"evals crisis"** — canonical benchmarks are saturated and "bench-maxing" is real.

## Key facts / claims (and confidence)
- **Scaling conviction (high-conviction, talk-his-book):** "I firmly believe in being on the exponential and in scaling laws… any of these bear takes I fairly strongly disagree with." The "pre-training is dead" narrative recurs every cycle and has always been broken by better engineering/data/research. Asked overrated/underrated: pre-training is **underrated**; tying research primitives to real agentic use cases is also underrated ("can't build everything in a vacuum").
- **Reasoning was the hard bet:** o1 was launched into a world where "pre-training + post-training" felt complete; took heavy top-down steering (credits Jakub, Ilya) to get the company behind reasoning. Frames reasoning as the template for taking high-risk bets that look crazy until they hit.
- **RL's frontier:** RL takes off where there's "cold hard truth" (math, code — provably right/wrong); struggles in subjective domains (creative writing). Coding/co-working chosen as the domain that tests **high-context, real-world, long-horizon** learning.
- **Coding-agent inflection:** "People woke up at the start of this year [2026] and realized agents are working in my profession… models can do long-horizon meaningful work." (Corroborates the 2026 agent-adoption step-change.)
- **Compute allocation:** ~3–5 big bets per org (pre-training / RL / alignment+post-training) wired into the main roadmap, with directive compute to big bets plus flexible pools; reviews ~300 project ideas every 1–2 months. High-level roadmap stable; implementation/sequencing/resourcing flexes.
- **Evals crisis:** few canonical gold-standard benchmarks left; all the great ones (SAT-style) are saturated. Internal "bench-maxing" = overfitting to a benchmark's distribution without generalizing. Fix = representative eval mixtures, constantly creating new evals, and **separating the eval-building team from the model-optimizing team** (adversarial incentives). "Once an eval is out in the world it's already not a good eval." Deploying models is itself an eval (watch where they fall over in the wild).
- **Continual learning / long context:** continual learning is "a basic primitive you have to unlock," not framed as a single breakthrough; "many shots on goal, I'm pretty sure they'll work." Long context done *well* ≠ just bigger windows — compaction (compress working state/insights) shortcuts the expensive native-long-context primitives. (Echoes the "context rot" concern.)
- **One model for all modalities:** strong bias to keep as few architectures as possible — cost of maintaining/scaling many infra stacks is underestimated; core research carries across modalities.
- **Talent war aside:** confirms the Zuckerberg "soup/poaching" episode; "matters calmed down… we came out on top."

## Quotes worth keeping
> "I firmly believe in being on the exponential and in scaling laws… it's held for almost 10 orders of magnitude, but there's no reason it should not keep holding."
> "If you still have a pre-training-is-dead view of the world… pre-training is definitely not dead, it's underrated."
> "We really are kind of in an evals crisis… all the really great evals we know growing up are fully saturated."
> "You're starting to see a lot of the work become mostly orchestration-focused — the researcher comes up with the idea and the model is great enough to do the implementation by itself."

## Wiki updates made
- [[ai-bubble-debate]] — added Mark Chen as the strongest Tier-1 bull-side scaling-conviction datapoint (bias-flagged) in the June ledger.
- [[inference-economics]] — added "vibe-researcher / research-as-orchestration" shift + the "evals crisis / bench-maxing" caveat (headline benchmark scores are gameable; trust representative mixtures).
- [[ai-capex-cycle]] — noted the OpenAI roadmap framing: ~3–5 big compute bets/org, AGI/self-sustaining-research as the demand-durability narrative (bias-flagged).
