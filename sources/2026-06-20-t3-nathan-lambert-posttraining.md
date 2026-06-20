---
date: 2026-06-20
type: podcast
publisher: Nathan Lambert (Interconnects / Ai2) × Finbarr Timbers
url: https://www.youtube.com/watch?v=sbXEPxIazqY
raw_path: raw/podcasts/2026-06-20-t3-nathan-lambert-posttraining.txt
touches: [inference-economics, ai-bubble-debate, ai-capex-cycle, MISTRAL]
---

# Nathan Lambert × Finbarr Timbers — Frontier Post-Training Recipe Review (~Jun 16 2026)

## TL;DR
- **The frontier post-training recipe has converged on "multi-tier on-policy distillation" (MOPD).** Train many domain-specialist experts (math, code, search, reasoning, safety) → have the general student model sample its own trajectories → route each to the matching expert → train with a distillation KL loss. Seen across **DeepSeek V4, Kimi K2.5, GLM-5, MiMo-Flash v2, Nvidia Nemotron-3 Ultra.** This is an *industrial org-chart problem* now, not an elegant research recipe.
- **Open / academic post-training is forking away from the frontier.** Ai2's Olmo 3 is "stuck" at a simpler 3-stage (SFT→DPO→RL) recipe because scaling the *recipe* means scaling the *org chart* — and academic labs can't. The gap is organizational capacity, not just compute.
- **The real moat color: post-training recipes are sticky for "order of years" once built, but rebuildable.** Lambert does *not* frame the moat as either Dwarkesh-thin or Katti-enormous — his cut is **operational/organizational**: the recipe shape lasts years and is hard to rebuild from scratch, but the *techniques* diffuse fast via Chinese-lab papers.

## Key facts / claims (with confidence)
- **Recipe lineage (4 canonical eras):** InstructGPT 3-stage RLHF → Llama-3/Tulu-3 practical RLHF → DeepSeek-R1 (RL-first, reasoning) → 2026 MOPD/distillation era. *High confidence — this is Lambert's central framework, well-sourced to public papers.*
- **DPO is being dropped at the frontier;** persists only in bootstrap/academic recipes (Olmo 3) where SFT data is distilled from stronger open-weights (Qwen/DeepSeek) and needs cleanup. *High confidence (his read of the papers).*
- **Chinese labs share far more nitty-gritty technical detail** (difficulty curricula, temperature schedules) than US labs; Kimi K2.5 and GLM-5 give *opposite* temperature-schedule advice. *Medium — informative but anecdotal.*
- **Chinese labs converging on sparse attention; US labs (Nvidia, Ai2) on hybrid attention** (Mamba). *Medium-confidence observation, flagged as a real architectural divergence.*
- **Lambert rejects "Chinese labs are more efficient."** His thesis: a US frontier lab serving billions of tokens has a *stronger* market incentive for efficiency (1% efficiency = "fat stacks of profit") than a Chinese lab. *His opinion, explicitly hedged.* — **Directly inference-economics-relevant.**
- **RL-environment market is real but messy.** Quote: ~$100k upfront + ~$50k/yr to build one sophisticated web-app environment (e.g. a DoorDash clone), software only — prompts/training-data extra and command a big premium. Vendors try to resell the same environment to multiple labs (so an exclusive can run ~$500k). *High confidence — firsthand sales-call data.*
- **Tinker-style fine-tuning APIs:** "a better business than most people expected," but margin sits *between* selling compute (worst business) and selling inference (best business). **Existential for these vendors to convert fine-tuning into an inference/token business** (lock-in via train-on-our-inference-engine). RL-fine-tuning-as-a-service has historically *not* taken off (OpenAI shutting down RL fine-tuning). *High confidence — sharp unit-economics framing.*
- **Pre-train vs post-train compute allocation is the single most guarded lab secret** — it reveals where each lab thinks the marginal ROI is. *High confidence.*

## Quotes worth keeping
> "Selling compute [is] not the best business. Selling inference [is a] great business. And Tinker-like APIs … [are] somewhere in between the two."
> "I think the financial pressures of serving billions and billions of tokens is probably a better motivator for efficiency … if you make a GPT model 1% more efficient, you're making fat stacks of profit."
> "Modern post-training is … your ability to wrangle compute [and] data into a workstream. And in order to do that … you really are wrangling an org chart."
> "Order of years" — expected lifespan of a converged recipe shape.

## Bias flags
- **Practitioner/researcher, not a seller.** Lambert just left Ai2; ex-HuggingFace/DeepMind-adjacent. Pro-open-science prior (wants Nvidia to release teacher models for study) → mildly biased *toward* the "open is tractable / catching up" framing, but he is candid about the org-capacity ceiling that holds open labs back. No financial book disclosed.
- Heavy inside-baseball; some claims are explicitly "my hypothesis" (DPO, efficiency). Treat the efficiency and attention-divergence claims as informed opinion.

## Wiki updates suggested
- Patch [[inference-economics]]: (1) the **fine-tuning-API → inference-token margin ladder** (compute < tinker-API < inference) sharpens the "where margin sits" section; (2) RL-environment unit-economics (~$100k/env) is a concrete data point for the "data/RL-env vendor" bucket; (3) Lambert's "serving-billions-of-tokens drives efficiency" view is a *demand-side* counter to the China-efficiency narrative.
- Patch [[ai-capex-cycle]]: MOPD makes post-training a *multi-expert RL* workload → more inference-shaped compute demand even absent pretrain scaling.
- Touch [[ai-bubble-debate]] / [[MISTRAL]]: recipe-diffusion via Chinese-lab transparency supports the "techniques commoditize" leg; org-capacity ceiling is the *counterweight* (frontier execution is hard to copy).
- Add as a 4th source to [[inference-economics]] on the open-weight-moat debate (organizational-stickiness angle, distinct from Dwarkesh vs Katti).
