---
date: 2026-06-09
type: report
publisher: SemiAnalysis
url: https://newsletter.semianalysis.com/p/deepseekv4-16t-day-0-to-day-43-performance
raw_path: n/a (partially paywalled, fetched via WebFetch ~2026-06-20)
touches: [inference-economics, ai-capex-cycle, NVDA, AMD]
---

# DeepSeekV4 1.6T — Day 0 to Day 43 Performance Over Time (GB300 NVL72, Huawei, MI355X, B200)

## TL;DR
- Tracks DeepSeek V4-Pro (1.6T MoE) inference perf across hardware for 43 days post-launch: enormous gains came almost entirely from **open-source software optimization** (kernels/serving), not new silicon.
- AMD MI355X went from barely working to **>100x throughput in <1 month**; B200 tokens/MW rose ~1.7x (300k→500k tok/s) on pure software. GB300 NVL72 leads at scale.
- Key thin-moat datapoint for the [[inference-economics]] / open-weight debate: a frontier open-weight Chinese model achieved Day-0 multi-vendor support and rapid cost-down — compressing inference economics and pressuring closed-model pricing power.

## Key facts (with confidence)
- **HIGH** — Authors: Bryan Shan, Cam Quilici, Kimbo Chen + others. Published Jun 9 2026.
- **HIGH** — DeepSeek V4-Pro = 1.6T-parameter MoE. SemiAnalysis benchmarks Day-0→Day-43 ramp across NVIDIA (B200, B300, GB300 NVL72, H200), AMD MI355X/ROCm, Huawei Ascend (950DT, CANN stack).
- **HIGH** — AMD MI355X: "over 100x improvement in throughput in less than a month" via kernel optimization (AMD/SGLang team led by HaiShaw). ROCm lagged at Day 0 but caught up fast.
- **HIGH** — B200 tokens-per-megawatt improved ~300k→~500k tok/s (~1.7x) from **software alone**.
- **HIGH** — Day-0 support stacks: NVIDIA CUDA (native vLLM/SGLang) and Huawei CANN. TensorRT-LLM needed ~1 week to fix a hidden-size mismatch bug. ROCm initially poor.
- **MEDIUM** — Disaggregated prefill + wide expert parallelism cited as the techniques driving perf/$ gains on a giant MoE.
- **MEDIUM** — Framed as proof of the "open native SGLang and native vLLM engine ecosystems" — i.e., open-source serving stacks now reach Day-0 frontier-model support across vendors.

## Quotes worth keeping
> "The improvement since then have been phenomenal—with the AMD team led by HaiShaw delivering an over 100x improvement"
> "This is a good case study that proves the strength of the open native SGLang and native vLLM engine ecosystems"

## Bias / paywall notes
- **PARTIALLY PAYWALLED — ~60–70% readable.** Final "B200 Tokens Per Megawatt Improvements" / deeper TCO + conclusions are paid-only. Major benchmark data IS visible.
- **Bias:** SemiAnalysis runs InferenceX (paid inference-benchmark product); article doubles as a showcase for that tooling. Benchmark direction (huge SW-driven gains) is credible; absolute numbers are SemiAnalysis's own and unaudited.
- No price targets. Investing signal is thematic (open-weight + multi-vendor inference cost-down).

## Wiki updates suggested (NOT made — per task scope)
- [[inference-economics]] — strong real-world datapoint: 100x (AMD) / 1.7x (B200) inference cost-down on a single open model in weeks, almost all software. Reinforces "inference cost falls fast; serving margins compress; capacity demand still rises (Jevons)."
- Open-weight / thin-moat debate — DeepSeek V4 achieving Day-0 support on AMD + Huawei + NVIDIA is evidence AGAINST a durable closed-model inference moat and FOR commoditization. Consider a dedicated `open-weight-models` or `deepseek` page if a 2nd source lands (currently no such page exists).
- [[AMD]] — MI355X reaching parity-class throughput on a frontier MoE within a month is a competitive-positioning positive vs NVIDIA on inference; note it required heavy AMD eng effort (ROCm Day-0 gap = ongoing software-moat risk for AMD).
- [[NVDA]] — GB300 NVL72 leadership at scale + CUDA Day-0 advantage = software moat intact; but the AMD/Huawei catch-up speed is a long-run bear nuance.
- [[ai-capex-cycle]] — Huawei Ascend Day-0 support relevant to China-domestic-compute substitution thesis.
