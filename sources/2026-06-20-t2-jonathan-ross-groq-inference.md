---
date: 2026-06-20
type: podcast
publisher: Jonathan Ross (Groq CEO) — Irish Open / Sohn conference (~May 2026)
url: https://www.youtube.com/watch?v=OBAXUdygTqQ
raw_path: raw/podcasts/2026-06-20-t2-jonathan-ross-groq-inference.txt
touches: [inference-economics, ai-capex-cycle, ai-bubble-debate, NVDA, MU]
---

# Jonathan Ross (Groq) — "The Inference Revolution" (~May 2026)

## TL;DR
- **Bottlenecks are transient by design — "the tall poppy gets chopped."** Any component that becomes a big enough cost/constraint gets *solved* (technologically or economically). Memory is today's bottleneck; Ross's bet is it gets solved too (more fabs + algorithmic compression). **Which means:** don't underwrite a thesis on a *single* persistent chokepoint — the binding constraint rotates.
- **Portability across architectures is dying → porting is now an economic handicap, not an engineering inconvenience.** This is the Groq pitch: inference is moving to specialized silicon where switching cost is real. (Self-serving — Groq sells inference ASICs/LPUs.)
- **Intelligence has *no* satiation point** (vs the diminishing-returns view). As long as cancer/aging/compute-scarcity exist, demand for more intelligence is unbounded; competition forces you to want the marginally-smarter model even when you can't perceive the difference. → bullish total inference demand.

## Key facts / claims (with confidence)
- **Memory was the most commoditized part of the semi supply chain; now it's the #1 AI bottleneck.** Framed via Giffen-good logic (raise the price of a staple and spend on it rises — until substitution kicks in). *His framework; directionally consistent with the wiki's memory thesis.*
- **DeepSeek V4 compressed KV cache by ~90%.** Ross frames the engineering effort as *opportunity cost* (forced by expensive memory) — the Jevons rebuttal is that cheaper memory would have freed those engineers for other gains. *Fact (the ~90% claim) high-confidence-as-reported; the framing is his.* — Note this V4 KV-cache point corroborates Simon Willison's "DeepSeek ~20× cheaper" claim from the same cluster.
- **Open-weight lags closed-weight by ~6 months** (Ross's number, stated as a given) → if intelligence has diminishing returns, open catches up. *But Ross personally disputes the diminishing-returns premise.* — **This is the moat-debate datapoint.**
- **Self-preference loop:** an LLM prefers resumes written by *itself*; recruiters now screen with LLMs → "agentic" = AI calling smarter AI, recognizing and routing to the better model even when humans can't tell the difference. *Anecdotal study, illustrative — but a real model-routing/lock-in argument.*
- **Models now improve at a "linear rate" via self-generated training data** (generate → prune to better → train → repeat). *His claim; no plateau in his view.* — Contrast with Dwarkesh's sample-efficiency-gap bear case already in the wiki.
- **Sentience defined as *rate of change* of intelligence** (idiosyncratic personal framework, not investable). Skip for portfolio purposes.

## Quotes worth keeping
> "Portability across architectures is diminishing and porting is no longer really an engineering inconvenience but has evolved into more of an economic handicap."
> "Every time a bottleneck gets big enough, people solve it … don't become too big of a problem because then it'll get solved."
> "There's no way to satiate the appetite for intelligence. The more intelligence you get, the more intelligence you want."

## Bias flags
- **STRONGEST BIAS IN THE CLUSTER. Ross is founder/CEO of Groq, which sells inference ASICs and competes directly with [[NVDA]].** Every structural claim — portability-is-dying (switching to specialized inference HW), bottlenecks-always-get-solved (incl. memory, where Groq's SRAM-heavy LPU sidesteps HBM), unbounded intelligence demand (more inference TAM) — is *talking his book*. Treat as the bull-case-for-inference-ASICs articulation, not neutral analysis.
- Also an active short-seller per the host's intro (entertainment framing) — independent of the inference thesis but a reminder he's a markets operator.
- Memory-gets-solved claim is in *tension* with the wiki's (and his own competitors') memory-scarcity bull thesis — surface, don't resolve.

## Wiki updates suggested
- Patch [[inference-economics]]: add "**binding constraint rotates / bottlenecks get solved**" as a counter-thesis to any single-chokepoint bet; add Ross's *no-satiation* demand view as the most aggressive Jevons/demand-side bull (bias-flagged).
- Touch [[MU]] / memory thesis: log Ross's *contrarian* "memory gets commoditized/solved again" call as contradicting evidence vs the current HBM-scarcity bull case (he's an interested party on both sides).
- Touch [[NVDA]]: "portability is dying → porting is an economic handicap" is the cleanest articulation of the inference-ASIC competitive-threat narrative (bias-flagged as Groq CEO).
- Note for the moat debate: Ross supplies a *third* lag number (~6 months) and uniquely argues against the diminishing-returns premise that would let open catch up.
