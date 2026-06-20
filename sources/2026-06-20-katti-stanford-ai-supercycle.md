---
date: 2026-06-20
type: podcast
publisher: Stanford (talk/interview)
url: https://www.youtube.com/watch?v=4k53z3Ysjg0
raw_path: raw/podcasts/2026-06-20-katti-stanford-ai-supercycle.txt
touches: [inference-economics, ai-capex-cycle, ai-bubble-debate, ASML, bottleneck-roadmap, INTC, MU, NVDA]
---

# Sachin Katti (OpenAI head of Industrial Compute, ex-Intel CTO) — The Economics of the AI Supercycle (Stanford)

> **Bias flag:** Katti runs OpenAI's compute buildout (Stargate) and was Intel CTO until Nov 2025 (still holds Intel stock). He is talking his book: long OpenAI, long NVDA, long infra, "scaling laws hold." Discount the boosterism; the operational detail is the value.

## TL;DR
- **Inference is already the majority of compute and heading to 80%+.** Scaling laws now span the whole lifecycle: pretrain + RL post-train + synthetic data + product serving — and post-train RL + synthetic data are *inference* workloads. (Independently corroborates [[2026-06-20-dwarkesh-sample-efficiency]]'s "RL = synthetic data" + "ran out of real data.")
- **Revenue is a lagging indicator for frontier labs** — "compute tripled YoY, revenue tripled YoY"; revenue = compute × utilization.
- **Power is the binding constraint, quantified:** ~100 GW of US hyperscaler buildout *beyond* OpenAI → double-digit % of the US grid; **1 GW ≈ $70B and ~half a million GPUs.**
- **ASML is "the single choke point of the whole supply chain"** (his biggest-unsolved-problem answer). Independent corroboration of the Dylan Patel EUV-bottleneck thesis.

## Key facts / claims (with confidence)
- **Inference already the majority, → 80%+ future.** *High confidence (insider).* Big input for [[inference-economics]].
- **Synthetic data because "we have run out of real-world data" — and it's an inference workload.** *Insider confirmation of the Dwarkesh RL point.*
- **Power/grid:** synchronized training jobs swing hundreds of MW → blackout risk; decoupling via natural gas + increasingly nuclear; ~100 GW US hyperscaler plans = double-digit % of grid. 1 GW ≈ $70B ≈ 500k GPUs. *High confidence; concrete.* → [[ai-capex-cycle]], power names [[NRG]]/[[GEV]]/[[BE]]/[[VRT]].
- **Heterogeneous compute is structural, not optional:** "can't deliver agentic UX economically on pure GPU." Cerebras *confirmed in production at OpenAI* for fast inference; long-context accelerators that hold state in memory (for coding); **CPUs making a comeback with agents.** *High confidence.*
- **TSMC wafer-allocation policy structurally guarantees multi-vendor accelerators** — TSMC deliberately spreads wafers to avoid single-customer concentration → multiple GPU/ASIC varieties must exist; at scale "we have to learn to use all of these chips." *Sharp structural point — supply-side reason custom silicon (Trainium ~$50B run-rate, TPU) coexists with NVDA rather than NVDA winner-take-all.*
- **Concentrated clusters win for now:** 1 GW cheaper per-MW than 50 MW; labor is the build bottleneck; **400-500ms prefill latency dominates** (Codex = 400k context) so edge placement doesn't help yet — until distillation shrinks models. *High confidence; tempers the near-term "edge inference" trade.*
- **AI designs next-gen AI infra** (models design the next chip + low-level software) to compress the ~3-yr chip cycle — "the only feasible way to bend the curve." *Concrete near-term version of Dwarkesh's "automate AI research."*
- **Memory architecture is the medium/long-term frontier** — "the compute-unit shape is known; it's the memory architecture around it that keeps changing." → [[MU]]/HBM.
- **Intel turning:** supply-constrained world rewards anyone who can *manufacture*; Intel = only leading-edge American manufacturer; CPUs comeback with agents. *Two tailwinds — but note his obvious Intel bias (ex-CTO, still holds stock).* → [[INTC]].
- **Value migrates up the stack over time** (mobile analogy: infra → apps → cloud services); infra has the profits "right now." **Short model wrappers; skeptical apps survive as the interface** (outcomes, not apps). **Long the lowest layer** (transformers, batteries, generation/distribution, cooling, materials) — differentiation sustainable (technical + scale). **First to $10T: NVIDIA.**

## The headline contradiction to surface (not resolve)
- **Open-weight lag: Katti "a SIX-MONTH lead is an ENORMOUS lead" vs Dwarkesh/Epoch "~4 months."** Same ~half-year gap, opposite spin. Katti (incentive: justify frontier capex) → decisive, defensible moat worth spending orders-of-magnitude more compute to keep. Dwarkesh → moat is thin/perishable because the driver (data) distills through the API. Filed to [[inference-economics]] / [[ai-bubble-debate]] as a live both-sides.

## Quotes worth keeping
> "A six-month lead in intelligence is an enormous lead."
> "ASML… that is the single choke point of the whole supply chain."
> "It's not that crazy to think every one of us should have a GPU." (7B × 1-2kW = 7 TW — two orders of magnitude beyond 30 GW.)
> "We want to get to a world where the human is the bottleneck."
> "Revenue is basically a lagging indicator for frontier lab companies."

## Wiki updates made
- Created [[inference-economics]] (inference-majority, model routing, heterogeneous compute, the moat contradiction).
- Patched [[ai-capex-cycle]] (inference-majority + synthetic-data-as-inference, power-as-constraint quantified, recursive AI-designs-chips, heterogeneous compute / TSMC wafer-allocation → multi-vendor).
- Patched [[ai-bubble-debate]] (the 4-vs-6-month moat contradiction; Katti's bull framing of scaling-laws-hold).
- Patched [[ASML]] + [[bottleneck-roadmap]] (ASML single-choke corroboration).
- Patched [[INTC]] (manufacturing-tailwind + CPU-comeback, with bias caveat) and [[MU]] (memory-architecture-as-frontier).
