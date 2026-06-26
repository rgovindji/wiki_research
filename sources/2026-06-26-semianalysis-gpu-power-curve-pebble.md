---
date: 2026-06-26
type: podcast
publisher: SemiAnalysis / Sale Media (GTC 2026, "Researcher Conversations")
url: https://www.youtube.com/watch?v=OpL-Q0YAKJU
raw_path: raw/podcasts/2026-06-26-semianalysis-gpu-power-curve.txt
touches: [bottleneck-roadmap, ai-capex-cycle, inference-economics, ai-bubble-debate, MU]
---

# The GPU power-performance curve most clusters ignore — Kav Ul Shah (Pebble) @ GTC 2026

Tier-3 technical, short (~1,700-word) GTC interview. Kav Ul Shah of **Pebble**, a startup doing data-center
energy optimization ("more tokens per watt"). Interviewer: Jordan Anos (SemiAnalysis).
**Bias flag:** founder sells exactly this — strong incentive to claim the inefficiency he optimizes is
large. Treat the magnitude as talk-his-book; the *physics* and the 100 GW figure are the durable takeaways.

## TL;DR
- **The GPU power→performance curve is non-linear and saturates.** Past a point you burn more watts
  without making more tokens. Effective compute is materially below nameplate power — independent
  corroboration of the "utilization waste" leg (MFU ~60–70%) in [[ai-bubble-debate]].
- **Inference is memory-bound:** the power goes to reading model weights into HBM during decode, while
  prefill SMs sit idle waiting. Reinforces memory centrality ([[MU]]) and that decode dominates power.
- **~100 GW of "flexible power" is available in the US** to data centers that can be **grid-responsive**
  (curtail at peak periods) — a real lever on the near-term power bottleneck.

## Key facts / claims (and confidence)
- **Non-linear power/performance.** "You crank up more power… but there's a point on the curve where it
  diminishes or saturates — consuming more power but not producing as many tokens." Two causes: (1) the
  voltage/power/clock-frequency relationship in a GPU is physically non-linear; (2) inference is
  memory-bound — power is spent moving weights into HBM; SMs (prefill) idle while decode runs. (High
  confidence on the physics; the *size* of the savings is the founder's sell.)
- **Pebble's mechanism:** per-GPU dynamic power-capping + clock-frequency tuning, driven by telemetry
  (vLLM/SGLang metrics + NVIDIA GPU power exporters). Helm install on Kubernetes/Slurm; ~a few days to
  learn a workload before applying caps, to avoid breaking SLAs/SLOs. Handles bursty/diurnal inference
  load. (Product detail; standard infra plumbing.)
- **100 GW of flexible US power.** "There's 100 GW of flexible power out there in the US. If data centers
  can demonstrate they can curtail power for certain peak periods, they can get access to it for certain
  trade-offs." Pebble building grid-responsive AI-workload power management. (Specific, checkable claim;
  ~matches DOE/Duke "Rethinking Load Growth" demand-flexibility research — likely the source.)

## Why it matters (investable read)
- **Power bottleneck has a software/demand-response release valve.** The near-term *deployment*
  bottleneck in [[bottleneck-roadmap]] (power 2026–28) is partly addressable without new generation: if
  AI clusters become grid-flexible, ~100 GW of existing headroom unlocks. Bullish for buildout pace /
  [[ai-capex-cycle]]; a partial counter to the "power wall caps everything" view. Watch for hyperscaler
  demand-response / curtailable-PPA announcements as confirmation.
- **Effective-compute < nameplate (capex-waste bear leg).** Power/performance saturation + memory-bound
  decode = gross capex overstates effective token output. Pairs with the SemiAnalysis RL-MFU ~10.5% and
  Latent Space MFU ~60–70% datapoints in [[ai-bubble-debate]]. Cuts both ways: waste = inefficiency
  today, but also = optimization headroom (you don't need to add GPUs to serve more if you tune the curve).
- **Memory-bound inference reinforces [[MU]]:** decode power is dominated by HBM weight reads — the
  inference workload is memory-throughput-limited, not just FLOP-limited.

## Quotes worth keeping
> "There's a point on the power-performance curve where it actually starts to diminish or saturate —
> you're consuming more power but not producing as many tokens."

> "There's 100 gigawatts of flexible power out there in the US… if data centers can demonstrate they can
> curtail power for certain peak periods, they can get access to it."

## Wiki updates made
- [[bottleneck-roadmap]] — 100 GW grid-flexible-power release valve on the power bottleneck.
- [[ai-capex-cycle]] — demand-response unlock = a buildout-pace lever.
- [[ai-bubble-debate]] — power/performance saturation = another effective-compute-<-nameplate datapoint.
- [[inference-economics]] — memory-bound decode dominates inference power; tokens-per-watt as the metric.
- [[MU]] — memory-bound inference (HBM weight reads dominate decode power).
