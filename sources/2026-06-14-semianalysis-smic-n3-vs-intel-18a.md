---
date: 2026-06-14
type: report
publisher: SemiAnalysis
url: https://newsletter.semianalysis.com/p/steel-smic-n3-teardown
raw_path: n/a (web-fetched; partially paywalled)
touches: [INTC, TSM, semiconductors, us-china-relations]
---

# Is SMIC N+3's Metal Pitch Smaller than Intel 18A's? (SemiAnalysis STEEL teardown, Jun 14 2026)

## TL;DR
- SMIC N+3 (in Huawei's Kirin 9030) hits a *tighter* M0 metal pitch (32.5 nm) than Intel 18A's shipping 36 nm — but SemiAnalysis calls this "an incomplete cherry-picked metric": N+3 reaches only TSMC **N6-class** density via brute-force DUV multi-patterning, with worse efficiency, process control, and core performance.
- The Kirin 9030 performs like "three-year-old Android flagships"; its prime CPU core is ~Arm Cortex-X2 class (2021), while Apple M5 P-core is ~2.7× faster absolute and far more power-efficient. SMIC has **not** overtaken Intel or TSMC.
- First public report from SemiAnalysis's new **STEEL** teardown lab (Oregon) — a credible independent rival to TechInsights. Investment read-through: export controls aren't freezing China, but they raise cost and stretch timelines; the *node gap* (no EUV, no N3/N4 access) matters more than any single density metric.

## Key facts (with confidence)
- **High confidence (measured/stated in the public portion):**
  - Metal pitches: SMIC N+3 M0 = 32.5 nm (SAQP), M1 = 38, M2 = 40, M3 = 44. Intel 18A M0 minimum 32 nm but ships 36 nm on Panther Lake (HP library). TSMC N6 ≈ 40 nm class.
  - Transistor density: SMIC N+3 ≈ 113.4 MTr/mm² vs TSMC N6 ≈ 107.7 MTr/mm². Standard cell height 228 nm (~5% < N6's 240). Contacted gate pitch 57 nm.
  - Density gap cited in coverage: Kirin N+3 ~38% behind Intel 18A on transistor density (despite tighter M0).
  - Performance: Kirin prime core ~Cortex-X2 (2021); Apple M5 P-core ~60% higher per-clock, ~2.7× absolute; integer efficiency Apple low-power ~1W vs Huawei ~4.5W for similar output. DRAM = Samsung 1a (current gen); 12GB LPDDR5X-9600.
  - STEEL = SemiAnalysis Teardown Engineering & Evaluation Lab, Oregon, launched ~1.5 yrs ago; claims revenue exceeding TechInsights, founder-led, no VC/PE.
- **Medium confidence (analysis/projection in public portion):**
  - Theoretical SMIC N+4 could reach ~138 MTr/mm² (≈ TSMC N5) but integration cost/difficulty rises sharply without EUV.
  - Huawei "LogicFolding" 3D-stacking strategy (ultra-fine-pitch hybrid bonding, logic split across active tiers) measures transistors per *package footprint*, not per die — not a like-for-like density claim.
- **Behind paywall:** detailed material/process-flow analysis of N+3 and package teardown.

## Key claims (and how confident)
- "N+3 reaches the density of TSMC N6 through aggressive DUV multi-patterning … but it pays for that in complexity, efficiency and process control." — well-supported by the measured data.
- "SMIC has not overtaken Intel or TSMC." — the central, high-confidence conclusion; tighter M0 ≠ better process (M0 is local intra-cell routing; the full stack/perf/efficiency is what counts).
- Strategic-sufficiency read: N6-class logic is enough for domestic AI inference, networking, security — China gets *good enough*, not *leading edge*.

## Quotes worth keeping
> "N+3 reaches the density of TSMC N6 through aggressive DUV multi-patterning … but it pays for that in complexity, efficiency and process control."

> "SMIC has not overtaken Intel or TSMC. It uses aggressive DUV scaling and DTCO to reach N6-class density, but that density doesn't translate into comparable performance and efficiency."

## Bias / access notes
- **Bias:** STEEL is SemiAnalysis's own commercial teardown lab — this report doubles as marketing for it ("behind the paywall, we show what else STEEL can do"). The measurements appear rigorous, but the "we beat TechInsights" framing is self-promotional. Headline ("smaller metal pitch than 18A") is engineered to be provocative, then debunked in-body — note the gap between the headline and the conclusion when citing.
- **Paywall:** PARTIALLY PAYWALLED — die shots, architecture, and process/density analysis are public; material-science and detailed package flow behind the wall.

## Wiki updates suggested (NOT made in this task)
- [[INTC]] — add to bull/process section: independent teardown confirms Intel 18A retains a meaningful density/performance lead over SMIC's best (N+3 ~38% behind on density); Intel's looser shipping M0 (36 nm) reflects PowerVia backside-power strategy, not a process deficiency. Mildly supportive of the 18A-competitiveness leg of the binary thesis (but doesn't resolve *yield*, the real question).
- [[TSM]] — note N6 still competitive 2-3 yrs on; the China gap is about node access (no N3/N4, no EUV) and performance, not headline density. Reinforces TSMC's leading-edge moat.
- [[us-china-relations]] — key data point: export controls are raising China's cost and stretching timelines, not freezing progress; SMIC achieves "strategic sufficiency" (N6-class for inference/networking) but remains generations behind on perf/efficiency. Knowledge diffusion to HLMC/Hua Hong + design houses (T-Head, Cambricon) reduces single-point-of-failure risk.
- [[semiconductors]] — add STEEL (SemiAnalysis Oregon teardown lab) as a new independent reverse-engineering source rivaling TechInsights.
