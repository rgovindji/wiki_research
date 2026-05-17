---
type: sector
tags: [semis, ai, hardware]
last_updated: 2026-05-16
last_full_review: 2026-05-09
sources: 1
---

# Semiconductors

## What this is
The chip stack — design (GPUs, CPUs, custom silicon), foundry ([[TSM|TSMC]]), and equipment (ASML, Applied Materials). Currently the highest-conviction long-term sector of the AI capex cycle because demand is **observable and contracted**, not just projected.

## State of the sector (May 2026)
- **Industry revenue forecast 2026: +26.3% to $975.4B**
- **AI server spend (Bloomberg Intelligence): +45% YoY to $312B**
- **NVDA $1T confirmed AI chip demand through 2027**
- **TSMC 2026 capex: $52–56B** (raised from prior; signals strong leading-edge demand)
- **TSMC 2026 revenue growth: ~30%**
- **ASML market cap crossed $500B**

## Sub-segments and key players

### GPU / accelerator design
- [[NVDA]] — dominant; Blackwell ramping, Vera Rubin on deck. **Stance: bull, high conviction.**
- [[AMD]] — credible #2; OpenAI 6 GW + Meta 6 GW + Oracle 50K MI450 deals; Helios rack Q3 2026 on TSMC 2nm. **Stance: bull, high conviction.**
- [[AVGO]] — Broadcom custom XPU for 6 hyperscalers (OpenAI Project Titan 10 GW by 2029); Tomahawk 6 networking (102.4 Tbps); $100B AI rev target by 2027 per Hock Tan. **Stance: bull, high conviction.**
- Hyperscaler custom silicon — TPU ([[GOOGL]]), Trainium ([[AMZN]]), MTIA ([[META]]) — vertical-integration plays competing with NVDA at the margin (often designed *with* [[AVGO]])

### Foundry (chip manufacturing)
- [[TSM]] — sole producer of advanced (3nm/2nm) AI chips at scale. **Stance: bull, high conviction.** Geopolitical risk is the single biggest variable.
- Samsung Foundry — distant second; trying to break into leading-edge logic
- Intel Foundry — strategic question mark; US fab build-out story

### Lithography / equipment
- [[ASML]] — **EUV monopoly**, no substitute for advanced nodes. **Stance: bull, high conviction (multi-year)** post-podcast ingest — framed as the 2028-2030 binding constraint of all AI compute.
- [[AMAT]] — Applied Materials; broadest WFE portfolio; **>50% of HBM equipment value**; >20% growth guide 2026. **Stance: bull, high conviction.**
- [[LRCX]] — Lam Research; deposition / etch; HBM-content levered. **Stance: bull, high conviction.**
- [[KLAC]] — [[KLAC|KLA]]; process control / metrology; Jefferies $1,500 PT. **Stance: bull, high conviction.**
- [[TER]] — Teradyne; chip-final test (different bucket from WFE, but same fab buildout tailwind); **Q1 2026 revenue +87% YoY to $1.282B record; 70% AI exposure**. **Stance: bull, high conviction.**

### Fab consumables, specialty materials, industrial gases (the "invisible" layer)
- [[ENTG]] — Entegris; FOUPs / wafer carriers / ultra-pure materials / gas+liquid filtration; content-per-wafer scales with AI chip complexity. **Stance: bull, high conviction.**
- [[APD]] — Air Products; industrial gases for fabs (N2/O2/Ar/H2 + NF3 chamber clean); multi-decade BOO contracts bundled into fab construction; Samsung Pyeongtaek is APD's largest electronics investment in history. **Stance: bull, medium conviction** (slow-moving industrial).

### Networking / interconnect
- [[AVGO]] — see above. Tomahawk 6 (102.4 Tbps) + Jericho switching silicon + custom XPU = the credible non-NVDA fabric.

### Photonics substrates (the upstream CPO bottleneck) — NEW 2026-05-17
- [[SOITEC]] (SOI.PA, Paris-listed) — only qualified volume supplier of **photonics-grade SOI wafers** to TSMC, GlobalFoundries, and Tower Semiconductor. **Which means** every NVDA Spectrum-X / Quantum-X CPO switch, AVGO Davisson chiplet, and MRVL Celestial chiplet substrate is Soitec. Stance: bull / low-medium conviction; stock has rallied ~6x off Dec 2025 lows so valuation is the main pushback.

### Memory
- Micron, SK Hynix, Samsung — HBM (high-bandwidth memory) is the under-supplied input for AI chips *(no pages yet)*

## Bull case for the sector
- AI demand is **contracted** (NVDA backlog, hyperscaler capex commitments) → lower risk of bubble vs. application layer
- Leading-edge foundry capacity is **physically constrained** — TSMC bottleneck supports pricing and margins
- **Sovereign AI** adds a second buyer base (UAE, Saudi, EU, India) outside US hyperscalers
- **Architecture lock-in via Tensor Cores (NEW 2026-05-16 per [[2026-05-16-horace-he-ml-systems]]).** On A100, matmul ops run **~15× faster** than non-matmul ops (1000 TFLOPS TF32 vs 67 TFLOPS FP32). If you aren't doing matmuls, you get **7% of peak FLOP utilization**. **Which means:** the entire ML industry consolidated onto transformers because no other architecture could use modern Nvidia hardware efficiently. This is a *chip-level* reason for architecture monoculture, not a software fashion — and it locks in continued demand for matmul-specialized hardware (which is what every AI accelerator now is, including AMD MI400/MI450 and AVGO custom XPUs). The sector benefits from the architectural homogeneity it created.
- **Effective-FLOPs lever via precision drops (NEW 2026-05-16).** Bit-precision ladder: V100 = FP16 default → A100 = FP8 → B100 = FP4. Each halving roughly doubles effective throughput per transistor **without requiring a new fab node**. **Which means:** even if 2nm / 1.4nm timelines slip, the compute-per-dollar curve keeps falling via precision drops — supportive for the long-cycle demand thesis without requiring EUV bottleneck-relief.

## Bear case for the sector
- **Cyclicality** — semis have always been boom/bust; this cycle's amplitude could match the upside on the way down
- **Geopolitics** — Taiwan invasion / blockade is the tail risk; export controls the more probable risk
- **Hyperscaler custom silicon** — TPU, Trainium, MTIA could erode NVDA's moat over multiple years
- **Hardware obsolescence** — Blackwell → Rubin → next; every gen impairs prior gen's residual value
- **Margin compression** — as Blackwell production normalizes, NVDA gross margins likely compress from extreme highs

## Tactical watch list
- NVDA Q1 FY27 earnings: gross margin trajectory is the tell
- TSMC monthly revenue: leading indicator for advanced demand
- ASML order book replenishment: post-China-pull-forward normalization
- Hyperscaler capex commentary on custom silicon vs. NVDA splits

## Related
[[ai-capex-cycle]] · [[NVDA]] · [[TSM]] · [[ASML]] · [[cloud-hyperscalers]] · [[overview]]

## Sources
1. [[2026-05-16-horace-he-ml-systems]] — Tensor Core 15× cliff drives architecture monoculture; FP4 precision lever extends compute curve

## Citations
- Schwab Q1 tech earnings preview: https://www.schwab.com/learn/story/semiconductor-earnings-preview
- Nasdaq on TSMC vs. ASML for 2026: https://www.nasdaq.com/articles/only-semiconductor-stock-you-need-2026-tsmc-intel-asml-or-micron
- ts2 on TSMC capex / ASML mark: https://ts2.tech/en/semiconductor-stocks-rally-as-tsmc-lifts-2026-capex-to-56-billion-asml-hits-500-billion-mark/
- CNBC on TSMC + ASML earnings: https://www.cnbc.com/2026/04/16/taiwan-semi-tsm-asml-stock-earnings-ai-chips.html
- Yahoo TSM vs ASML: https://finance.yahoo.com/news/taiwan-semiconductor-manufacturing-vs-asml-183500365.html
- Marketshost top semi stocks 2026: https://www.marketshost.com/news/articles/top-semiconductor-stocks-to-watch-in-2026-ai-boom-breakout-charts-strong-buy-signals-102643
