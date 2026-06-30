---
date: 2026-06-30
type: article
publisher: SemiWiki + multi-source feeds (arXiv, HuggingFace, Reddit)
url: https://semiwiki.com/
raw_path: n/a (incremental scan via scripts/semiwiki_scan.py + scripts/feed_scan.py)
touches: [semiconductors, INTC, inference-economics, overview]
---

# SemiWiki + feeds daily — photonics test-scale, China memory capex, Intel Q2 date, HBM-disaggregation research

## TL;DR
- **Photonics manufacturing's hidden bottleneck is *repeatable* test, not one-off alignment** — CPO/optical-I/O scale needs probe stations that align light + measure electrically across many wafers/operators/lots. A standing-interest diamond for the [[COHR]]/[[LITE]]/[[GLW]] CPO layer.
- **China's two memory giants are tendering equipment in size:** CXMT US$5–6B (capacity +50–60k wspm), YMTC Phase-2 pipeline — the supply-build behind the CXMT-climbs-the-stack thread (commodity tier, not AI-grade).
- **Intel will report Q2 2026 on Thursday July 23 (AMC)** — the next hard yield/foundry-revenue checkpoint for the [[INTC]] binary.
- **Research tell — "HBM Is Not All You Need":** disaggregated LLM serving puts cheap GDDR accelerators on the memory-idle prefill phase, a marginal HBM-demand-relief vector (sibling to AMD's MEXT memory-tiering).

## Key facts
- **Photonics probing (Dr. Moh Kolbehdari, SemiWiki):** silicon photonics has proven lab-grade alignment (fibers, waveguides, grating/edge couplers, modulators, detectors), but the realization boundary for CPO/optical-I/O/PIC is **repeatability** — aligning + measuring + calibrating light *thousands of times* across wafers, operators, tools and lots. Photonics probe platforms (optical alignment + electrical probing + imaging + motion + calibration) are the R&D→manufacturing-confidence transition point. No near-term ticker, but the test/metrology layer is where CPO volume gets gated.
- **China semi-equipment inflection (Yole Group, SemiWiki):** Q2 2026 — **CXMT launched large-scale equipment tenders, ~US$5–6B procurement for a 50–60k wafers/yr capacity add**; **YMTC initiated a Phase-2 fab process-equipment tender (May 14)**. Synchronized memory-giant expansion is driving etch/deposition/CMP order volume. Forum tone: China semi compounds regardless of an AI-bubble break (import-substitution, large domestic market).
- **Goertek AR optical wafer plant (Shanghai Lingang):** China's first large-scale **12-inch transparent-substrate** fab for AR micro-nano optics started commercial production — CNY 3.28B (~US$457M), diffractive-waveguide design + SiC processing + **nanoimprint lithography**, making AR waveguide lenses / electrochromic lenses / microlens arrays. Signed Feb-2023 → production June-2026. AR/smart-glasses optics supply-build; photonics-adjacent.
- **Intel (INTC):** announced Q2 2026 results on **Thursday, July 23, 2026, after market close** (call 2pm PDT).
- **Research — "HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators" (arXiv 2606.29986):** decode is memory-bound (needs HBM) but **prefill is compute-bound and leaves HBM bandwidth idle** — so pair cheap GDDR-based accelerators for prefill with HBM GPUs for decode (MemHA). A demand-side *efficiency* vector that could trim HBM intensity at the margin.
- **Builder/researcher color:** NVIDIA shipped `Qwen3.6-27B-NVFP4` (NVFP4 4-bit inference format adoption); Huawei open-sourced OpenPangu-2.0-Flash (92B/6B-active); SemiWiki EDA threads frame AI's value in verification as a *people/throughput* unlock (root-cause in 30 min vs a week), reinforcing the [[SNPS]]/CDNS design-bottleneck thesis. Reddit retail piling into ASTS/RKLB (sentiment context only).

## Key claims (and how confident)
- China memory-equipment tenders are real and sized (Yole, named figures) — **high confidence**; impact is commodity-DRAM supply over a 2–3yr horizon, not near-term AI-grade.
- Photonics test-repeatability as the CPO scaling gate — **medium** (vendor-adjacent framing, but mechanistically sound and consistent with the advanced-packaging-is-the-constraint thread).
- HBM-disaggregation as a demand-relief vector — **low/medium** (research paper; marginal, like MEXT — watch, don't underwrite).

## Quotes worth keeping
> "Precision creates the first result. Repeatability creates confidence. Confidence creates manufacturing evidence. Manufacturing evidence enables scale." — Kolbehdari, on photonics probing
> "Even if the AI bubble broke hard tomorrow, I suspect China's Semi market would continue to compound annually at a decent rate for at least the next 5 years." — SemiWiki forum, on China equipment localization

## Wiki updates made
- Added a SemiWiki/feeds bullet to [[semiconductors]] Recent developments (photonics test-scale + China memory capex + Goertek AR + HBM-disaggregation research)
- Added the **July 23 Q2 earnings date** to [[INTC]] Recent developments
- Added the breakout/regime note to [[overview]] (separate market-tape entry)
