---
type: sector
tags: [semis, ai, hardware]
last_updated: 2026-06-29
last_full_review: 2026-05-09
sources: 10
---

# Semiconductors

## What this is
The chip stack — design (GPUs, CPUs, custom silicon), foundry ([[TSM|TSMC]]), and equipment (ASML, Applied Materials). Currently the highest-conviction long-term sector of the AI capex cycle because demand is **observable and contracted**, not just projected.

## State of the sector (May 2026)
- **🔥 WSTS Spring-2026 (2026-06-19): the official scorekeeper goes huge — 2026 $1.51T (+90% y/y), Memory ~+250% to >$800B, Logic +37%; 2027 $1.9T (+27%)** ([[2026-06-19-semiwiki-asml-china-wsts-tsmc-troll-intel-pdf]]). Memory alone is the majority of the year's growth (Americas +112%, more than doubling). Sits between the conservative baseline and UBS; the memory concentration is the headline — confirms the [[MU]] pricing leg while sharpening the [[ai-bubble-debate]] "narrow, ASP-led, not unit-driven" bear.
- **🔥 UBS (2026-06-12): "generational" boom — sell-in $1.62T 2026 → $2.38T 2027; memory $961B → $1.638T; cycle green into late 2027** ([[2026-06-12-ubs-semi-2.38T-2027]]). Far above the +26.3%/$975.4B baseline below — UBS is the high-side anchor on the demand lens; weigh vs late-cycle valuation warnings ([[valuation-environment]]).
- **🔥 Foundry diversification has begun (2026-06-08): Google ordered >3M TPUs from Intel Foundry for 2028; Nvidia evaluating Intel** ([[2026-06-08-google-intel-3m-tpu-2028]]). TSMC's sold-out AI capacity is pushing designers to a credible second source ([[INTC]] via EMIB-T packaging). Slow, multi-year share-of-marginal-growth shift; TSMC scale dominance intact.
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

## Recent developments
- **2026-06-29 — SemiWiki sweep (11 items): Qualcomm's $8–10B Tenstorrent move, China memory signs LTAs, Foundry 2.0 +23% YoY** ([[2026-06-29-semiwiki-daily]]). Four threads worth banking. **(1) Merchant AI-DC consolidation:** Qualcomm ([[QCOM]]) reportedly in talks to buy **Tenstorrent for $8–10B** — its 3rd DC acquisition (after Ventana RISC-V + $2.4B Alphawave) — for the **BUDA** software stack (run non-NVIDIA silicon without a CUDA rewrite) + **Tensix training cores**; the CUDA-moat attack now has a third well-funded attacker. **(2) China memory climbs the stack:** **CXMT signs a ~$3B LTA with Tencent** (see [[MU]]) — China's #1 maker now behaving like the oligopoly (signing take-or-pay, not flooding); bit share 9%→12% by 2027, ~17% of global DRAM capacity by end-2028 ("still far from flooding"). **(3) Foundry 2.0 +23% YoY to $86B** (Counterpoint, Q1 2026): **TSMC +41% YoY** ([[TSM]]), full-year ~36%; OSATs Amkor +25% / ASE +18% as advanced packaging becomes the binding constraint; TPU/ASIC tightening leading edge opens a door for Intel Foundry/Samsung. **(4) Dylan Patel "Tokens to Infrastructure" (SEMI ISS):** the token-factory frame — HBM shortage through 2027, the HBM transition *worsens* commodity-DRAM shortage ("double-shortage dilemma"), AI cloud contracts ~$10–13/watt/yr (corroborates [[inference-economics]]/[[ai-capex-cycle]]). Long-tail tell: **AOC calls to break up Apple** over the $200 RAM-driven price hikes — the memory cost-push is now a *political* event. No stance changes.
- **2026-06-26 — SemiWiki sweep (7 items): Samsung pushes on HBM4E *and* a $648B bet, Arm hits ~50% of AI-DC compute, the power layer surfaces as the next bottleneck** ([[2026-06-26-semiwiki-daily]]). **(1) Memory:** Samsung ships **industry-first 12-layer HBM4E samples** (14–16 Gbps, 3.6 TB/s/stack, 48 GB, 1c DRAM + 4nm base die) and reportedly readies a **~$648B / 1,000T-won 10-year** Korea investment (~300T won for new fabs) — both cut against a "supply-disciplined trio / durable Micron HBM lead" read (see [[MU]]). China's **CXMT** disclosed a **64-layer 3D DRAM test vehicle** reaching ~525 Mb/mm² (into the ~1c <600 Mb/mm² range) — the slow-burn density-catch-up via stacking, not shrink. **(2) Compute share:** **Arm has reached ~50% of compute shipped into top AI data centers** (see [[ARM]]) — the x86→Arm server shift is now realized, not forecast. **(3) Power:** Nvidia's **800VDC** rack push could swing **silicon-carbide / power semis** (Wolfspeed, Rohm, Taiwan's Episil) from oversupply toward shortage — "the next AI bottleneck may have nothing to do with GPUs" (ties to [[VRT]]/[[ETN]] 800V architecture). **(4) Logic:** Intel detailed **18A-P** (~9% perf / ~18% power / 20–40% lower thermal resistance vs 18A, drop-in compatible; volume this month) — the N5P/N3P-style optimizer before 14A (see [[INTC]]). **Which means:** the memory competitive front is widening (Samsung HBM4E + CXMT density), the CPU mix-shift to Arm is a banked fact, and the substrate/power layer (SiC) is the fresh dual-use bottleneck to track. No stance changes.
- **2026-06-25 — Memory ASP inflation goes consumer-visible; IBM claims a sub-1nm "0.7nm" CFET node** ([[2026-06-25-memory-cost-device-makers-fade]], [[2026-06-25-semiwiki-daily]]). Two threads. **(1) The memory cost-push is now a retail-price event:** [[AAPL]] (+$300 on Macs/iPads) and [[MSFT]] (+$100–150 on Xbox) raised end-product prices on memory/storage costs, with Microsoft guiding console memory **+2.5x and doubling again by fall 2027**. **Which means** the sector's ASP supercycle (bull for [[MU]]/the memory trio) is now flowing through to consumer BOMs as cost-push inflation — visible, dated confirmation of pricing power, and the seed of the downstream PC/phone-unit-demand bear. **(2) IBM "NanoStack" 0.7nm:** the first publicly claimed sub-1nm node — a staggered sequential CFET with NMOS/PMOS on *separate* wafers cut on different crystal planes (<001>/<110>) and bonded via a proprietary "device-scale" wafer-bonding step; claims 50% logic / 40% SRAM scaling + 70% energy vs IBM 2nm, and IBM is buying a High-NA tool ([[ASML]]). **Which means** the leading-edge logic roadmap (CFET-after-GAA) is increasingly a *wafer-bonding/packaging* problem — but IBM doesn't manufacture and its 2021 "2nm" still isn't in a shipping product, so treat it as a directional research tell (and a licensing-friction datapoint), not a near-term mover. No stance changes.
- **2026-06-24 — SemiWiki sweep (9 items): a Broadcom/MediaTek SerDes swap, broad MediaTek price hikes, Qualcomm buys Modular, GaN-on-SiC tightening, an EUV alternative funds up** ([[2026-06-24-semiwiki-daily]]). Headline AI-silicon items: **OpenAI × [[AVGO]] "Jalapeño"** inference chip unveiled (9-mo design→tape-out, deploy end-2026, MSFT ~40%) — but **MediaTek won the Google TPU v9 SerDes socket** with a **336G** solution after Google's 448G target hit signal-integrity/thermal walls, and **Broadcom "lost its leading position for now"** (448G DSPs may need 2nm, ~2028-29). The long tail: **MediaTek raising prices 10-20%** across mobile SoCs+PMICs (component shortages/capacity/lead-times — a broad cost-push tell, in line with memory & CPU vendors); **Qualcomm ([[QCOM]]) buying Modular ~$4B** (silicon-agnostic AI software stack — build-once-run-anywhere across CPU/GPU/NPU/ASIC, deepening its data-center software moat); **GaN-on-SiC foundry slots tightening** (Feb-2026 DoD emergency-procurement prioritizing military GaN over commercial 5G/consumer, *plus* NVIDIA reportedly moving to **silicon-carbide interposers in next-gen Rubin** — redirecting SiC capacity to data centers, squeezing RF supply → [[bottleneck-roadmap]]); and **xLight** ([[ASML]] context) raising $350M for a free-electron-laser EUV alternative (Gelsinger chair, US-gov-backed, 2028 prototype). **Which means**: the custom-ASIC moat is contestable (one socket won, one lost across AVGO/MediaTek in a week), cost-push is now broad-based (MediaTek joins memory/CPU on price), and the SiC/GaN substrate layer is a fresh dual-use (defense + AI-interposer) bottleneck to watch. No stance changes.
- **2026-06-23 — Global memory rout; plus four SemiWiki long-tail tells worth banking** ([[2026-06-23-memory-rout-niles-bofa-hawkish]], [[2026-06-23-semiwiki-daily]]). The headline event was the **~13% memory selloff** (KOSPI −10% circuit-breaker, [[MU]] −13%, SOXX −7.9%) on Dan Niles' AI "speed-bump" + BofA's 75bp-of-*hikes* call — a valuation reset of the most crowded trade, not a contracted-demand change (see bull-case point 1). Underneath, four diamonds-in-the-rough:
  - **The "DRAM can't shrink below 10nm" inflection.** A SemiWiki forum thread cites Deutsche Bank modeling **the DRAM supply gap persisting to 2030+** — and the structural reason: DRAM has historically grown bits via shrinks with little capex, but **sub-10nm shrinks are basically done**, so future bit-growth requires explosive *capacity* capex (analogized to 3D NAND's inflection 13 years ago). **Which means** the supply side is even more capex-gated (and slower) than the ASP debate implies — bullish-tight for the memory trio, but also why the cycle is unusually capex-heavy.
  - **AMD acquires MEXT** (memory-tiering startup) — AI software that makes **NAND flash appear as DRAM to the OS**, prefetching pages before they're needed, to cut hyperscalers' DRAM bill. A demand-side *efficiency* vector against the DRAM shortage (relieves some pressure at the margin); folds into AMD's data-center portfolio.
  - **Intel + AMD co-author "ACE" (Advanced Compute Extensions)** — an x86 spec adding dedicated matrix hardware (keeps AVX10 registers, adds OCP MX block-scaled formats, up to 16× ops/instruction vs AVX10) to make **CPUs viable for small-model / latency-sensitive / edge inference** without a GPU. Not a GPU threat at training scale, but a structural nibble at the inference-everywhere TAM and a rare Intel/AMD standards collaboration.
  - **New inference entrants:** **Semidynamics** (European RISC-V) brought a full silicon-to-rack 3nm inference stack to ISC-HPC, pitching memory-centric "usable compute" over peak TOPS; **Chips&Media** signed an **AV2 video-codec IP** license with a North-American big-tech (30–50% better compression than AV1) for AI-infra SoCs. Both are credible-alternative / long-tail tells, not stance-movers.

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
