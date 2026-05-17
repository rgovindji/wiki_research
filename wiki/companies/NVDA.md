---
type: company
ticker: NVDA
tags: [ai, semis, mag7]
last_updated: 2026-05-17
last_full_review: 2026-05-09
sources: 7
conviction: high
stance: bull
---

# NVIDIA (NVDA)

**Stance:** bull · **Conviction:** high · **Time horizon:** long-term (multi-year) with tactical entry/exit windows

> **NEAR-TERM CATALYST (Updated 2026-05-15):** NVDA reports **Q1 FY27 earnings on May 20, 2026** after the close. Street consensus: **$1.77 EPS, ~78% YoY revenue growth** (guide was $78B ± 2%). **NVDA hit ATH market cap $5.4T on May 13.** Jensen joined Trump's Beijing delegation last-minute. **H200 CHINA DEAL IN LIMBO (May 15):** US approved sales to ~10 Chinese firms (Alibaba, Tencent, ByteDance, JD.com, Lenovo, Foxconn + 4 others); each customer up to 75,000 chips. But **China has NOT approved the purchases from its side**. **Trump (May 15): "they want to develop their own."** Stock -4% Friday intraday after Thursday's +4.4% pop. **Net read:** the chip-carve-out from Trump-Xi summit was symbolic, not transformational — exactly what wiki Scenario A "Theater" predicted. Bull case unchanged because near-term China revenue was never the wiki's thesis; analyst Q&A on May 20 now has a clean question: "Are H200 China shipments factored into Q2 guide or not?"

## One-line thesis
The dominant supplier of AI accelerators with a $1T confirmed demand backlog through 2027 and a deepening software/networking moat (CUDA, NVLink, Spectrum-X) — the canonical picks-and-shovels long-term hold for the AI capex cycle.

## Snapshot (as of May 2026; verify before any decision)
| Metric | Value | As of |
|---|---|---|
| Q1 FY2027 data center revenue | **$39.1B (+69% YoY)** | calendar Q1 2026 release |
| Q1 FY2027 revenue (total, guided) | **~$78B** | management guide |
| AI chip demand confirmed through 2027 | **~$1T** | Intellectia / company commentary |
| Blackwell platform | **sold out through mid-2026** | management commentary |

*All figures should be re-verified at next earnings; market cap and forward P/E intentionally not pinned without a fresh source.*

## Bull case
- **Demand is contracted, not extrapolated.** Hyperscaler orders for Blackwell are firm; the $1T figure is from cumulative confirmed demand, not analyst speculation.
- **$90B of long-term supply contracts secured (NEW).** Per [[2026-05-09-dwarkesh-dylan-semianalysis]]: NVDA secured [[TSM|TSMC]] + memory capacity earlier and harder than Google/Amazon — non-cancelable, non-returnable terms with deposits. Result: NVDA is set to capture **>70% of N3 wafer capacity by 2027.**
- **The "X-1 not AGI-pilled" gap (NEW).** Even Nvidia is building "X-1" while OpenAI/Anthropic want X. The supply chain is consistently *under-supplying* labs' demand → backlog momentum. This pushes back on the "demand is over-extrapolated" bear case.
- **An H100 is worth MORE today than 3 years ago (NEW).** Labs signing $2.40/hr 2-3yr deals on $1.40/hr build TCO. Falsifies the Michael Burry / short-depreciation bear case at the asset-economics level.
- **CUDA + ecosystem moat.** Switching costs at the software/dev tooling layer are deeper than the hardware comparison alone suggests.
- **Vera Rubin roadmap.** Next-gen platform behind Blackwell ensures product cadence stays ahead of competition.
- **Networking + system business.** Spectrum-X, NVLink, full-stack systems (DGX, GB200) increase ASPs and lock in customers at the rack level, not just the chip.
- **Sovereign AI demand.** UAE, Saudi, India, EU — adds a second buyer base beyond US hyperscalers (see [[ai-capex-cycle]]).
- **Robotics moat is deeper than chips (NEW 2026-05-16).** Per chief scientist Jim Fan ([[2026-05-16-jim-fan-nvda-robotics]]): NVIDIA leads the **VLA→WAM paradigm shift** with **Dream Zero** (world action model that learns physics from video). EgoScale discovered a **clean log-linear scaling law for dexterity** (21k hours egocentric video + only 4 hours teleop). **Dream Dojo** is a neural simulator (no physics engine, no graphics engine) enabling massively parallel robot RL. NVIDIA owns the model layer + data scaling law + simulator infrastructure — three additional moats stacked on the chip moat. Fan: **physical Turing test 2-3 years away; full robotics endgame by 2040 with 95% certainty**.
- **Tensor Cores are a structural hardware moat, not just CUDA (NEW 2026-05-16).** Per Horace He (Meta PyTorch Compilers) [[2026-05-16-horace-he-ml-systems]]: on A100, matmul ops run **~15× faster** than non-matmul ops (1000 TFLOPS TF32 vs 67 TFLOPS FP32). If you're not doing matmuls on a GPU, you get **~7% of peak FLOP utilization** — full stop. This is *the* underlying reason transformers consolidated as the only architecture; non-matmul-heavy models literally cannot use modern Nvidia hardware efficiently. **Which means**: bear cases that lean on "AMD ROCm will catch up because software is converging" understate the depth of the moat — the architectural lock-in compounds at every precision drop (FP16 → FP8 → FP4), and the programming-model layer (CUDA, NVLink, FlexAttention, torch.compile) is a *separate* moat on top of the hardware. Each generation widens both.
- **Hyperscaler engineering complexity is a customer-stickiness moat (NEW 2026-05-16).** Llama 3 paper data: at 16K GPUs, mean time between failures ≈ 1.8 hrs; at **131K GPUs ≈ 15 minutes**. Only hyperscalers + a handful of neoclouds have the systems-engineering depth to actually USE the GPUs they order at frontier scale. **Which means** NVDA's top customers are *captive* on engineering capability, not just contractual commitment — and tier-2 buyers (CRWV, NBIS) win by *renting* hyperscaler-grade engineering rather than replicating it.
- **Anthropic now MORE compute-constrained than OpenAI (NEW 2026-05-17 per [[2026-05-16-dylan-patel-invest-like-best]]).** Dylan Patel: *"Dario used to gloat about OpenAI being too aggressive on compute and Anthropic was more sensible. Now Anthropic is like 'fuck, we wish we had more.'"* Anthropic gross margins now floor at **72%** (was "30-something%" at start of 2026 per leaked funding docs). **Which means** for [[NVDA]]: top-tier labs are compute-constrained, not demand-constrained — the labs cannot serve all available token demand. Margin expansion at the lab tier means more capex they can fund, more NVDA orders. Reinforces "demand is contracted, not extrapolated" core bull thesis.
- **Huawei compute = 4% of NVDA 2026 / 2% 2027 (NEW 2026-05-17 per [[2026-05-14-anthropic-2028-ai-leadership]]).** Anthropic's "2028: Two Scenarios for Global AI Leadership" paper provides the cleanest quantitative data point on the US-China compute gap the wiki has captured: **Huawei will produce only 4% of NVIDIA's 2026 aggregate compute, dropping to 2% in 2027**. Anthropic also claims strengthened export controls could give the US access to **~11× more compute than China's AI sector**. **Which means**: the NVDA moat is not just CUDA ecosystem and Tensor Core hardware — it's *literal manufacturing-scale dominance* over the only credible chip-side competitor. The gap *widens* in 2027 absent Chinese SME breakthrough. This is the strongest quantitative refutation the wiki has of the "China will catch up" bear case, even acknowledging Anthropic's policy-advocacy bias. Reinforces [[ASML]] / [[AMAT]] / [[KLAC]] / [[LRCX]] supply-side moats (SME export controls preserve the gap).
- **Drive Thor commercial deployment via Aurora (NEW 2026-05-16).** [[AUR]] launched **first US driverless commercial freight** for McLane (Berkshire Hathaway) on Dallas-Houston in April 2026 — powered by **dual NVIDIA Drive Thor SoCs (Blackwell architecture)**. Continental manufactures production hardware kit at scale starting 2027. Hirschbach 500-truck MOU = multi-year revenue pipeline. **Which means** Drive Thor is now a *commercial* revenue line, not just a development platform — Aurora is the flagship deployment outside robotaxi (Waymo) and consumer cars. Validates NVDA's automotive-AI compute moat, and if Aurora scales, pulls more design wins at Toyota / Mercedes-Benz / BYD (Drive Thor partners announced at CES 2025/2026).

## Bear case / risks
- **Gross margin compression.** Industry-leading margins are unsustainable through Blackwell ramp + competitive intensity. The single most important variable to watch.
- **Hyperscaler custom silicon via [[AVGO]] (NEW concrete escalation).** Broadcom now has **6 confirmed hyperscaler customers** for custom XPUs, with **OpenAI Project Titan targeting 10 GW of deployed compute by 2029** (mass production late 2026) and Meta's first phase >1 GW. This is more concrete than the prior "custom silicon could erode share" framing — Broadcom has crossed from theoretical threat to material concrete commitment.
- **[[AMD]] as the credible #2 GPU.** OpenAI 6 GW + Meta 6 GW + Oracle 50K MI450 deals are real. Helios rack Q3 2026 finally addresses NVDA's NVLink rack-scale moat. ROCm still trails CUDA, but inference workloads (where Lisa Su sees the largest deployments) are exactly where multi-vendor is most plausible.
- **Hyperscaler custom silicon (broader).** TPU ([[GOOGL]]), Trainium ([[AMZN]]), MTIA ([[META]]) erode NVDA's wallet share over time. Not a near-term threat; very real over 3-5 years.
- **Demand cycle peak risk.** If hyperscaler capex pauses (see [[ai-capex-cycle]]), the entire bull case re-rates simultaneously.
- **China export controls.** Geopolitical revenue cap; unpredictable policy environment.
- **Export-control diversion risk + Culper short thesis (NEW 2026-05-13 — see [[2026-05-13-culper-nvda-short-thesis]]).** **DoJ indicted SMCI cofounder + sitting board member Wally Liaw on March 19, 2026** for conspiring to illegally export ≥$2.5B in NVDA AI tech to China through SE Asian intermediaries (SMCI -33% on the news). **Culper Research is now publicly short NVDA** alleging the pattern extends through Megaspeed (Singapore), Speedmatrix, Novagate Cloud, Aivres Systems, Giga Computing, and YTL AI Cloud Malaysia — claiming >20% of FY26 compute revenue is China-attributed via diversion. NYT (Paul Mozur) published parallel reporting. **Which means:** the export-control compliance dimension has shifted from policy risk to active prosecutorial enforcement. More DoJ indictments of intermediaries are plausible. Jensen's optics — in Beijing with Trump's delegation this week while DoJ prosecutes diversion through an NVDA Elite OEM — are a real management-risk vector that didn't exist 30 days ago. **May 20 Q1 FY27 earnings call now has a new analyst-question dimension** on China revenue mix + export control compliance.

> **What this means:** Nvidia's bull case is intact — its earnings power is from US hyperscalers, not China, and the DoJ is prosecuting middlemen (SMCI cofounder, fixers), not Nvidia leadership. But this isn't nothing. A sitting board member of an Nvidia Elite OEM was indicted for $2.5B of diversion. The Justice Department is actively investigating the broader pattern. A credible short-seller (Culper) has published a thesis that mainstream press (NYT) has independently validated parts of. Jensen will face questions on the May 20 earnings call that didn't exist before. Position-size discipline matters more than the bull thesis changing.
- **Hardware obsolescence cycle.** Each new generation depreciates the prior; impacts hyperscaler ROI calculations and resale value. **NEW 2026-05-17 — bear case weakens significantly**: Per Dylan Patel ([[2026-05-16-dylan-patel-invest-like-best]]), "GPU useful life is clearly not 5 years. It's maybe even 7 or 8." Hopper clusters resigning for 3-4 more years; A100s for another 2+. **Directly refutes the Burry-style depreciation bear** that the wiki tracks. Cluster gross margins thus higher than reported. **Implication**: amortization-period extension supports higher steady-state ROI for hyperscaler GPU capex, indirectly bullish for NVDA pricing power (customers willing to pay more for assets that hold value longer).
- **Concentration in S&P 500.** Largest stock by market cap → tied to passive flow risk (see [[market-concentration]]).

## Sizing-discipline anchor — the Druckenmiller anti-pattern (NEW 2026-05-16, ~March 2026 dated)

Per [[2026-05-16-druckenmiller-hard-lessons]]: Stan Druckenmiller bought NVDA at ~$150 (pre-ChatGPT, mid-2022), doubled after ChatGPT, doubled again on Morgan Stanley analyst commentary. Said publicly in a 2024 interview (at $390): *"I cannot possibly see myself selling Nvidia over the next two or three years."* Then sold at $800. NVDA went to $1,400 in 5 weeks. His own framing:

> *"I knew through years of experience when you have massive massive change investors just can't make themselves keep up with it. I cannot possibly see myself selling Nvidia… The stock can't not go up for at least 3 years. So then the stock goes to 800 and I violated everything I said. I couldn't stand success."*

**Which means** for any wiki user holding [[NVDA]]: this is the canonical anti-pattern for trimming AI winners. A legendary macro investor *who explicitly knew better* sold 5 weeks before a 75% run. The encoded lesson: when massive secular change is unfolding AND your sizing has remained correct, the default bias should be **HOLD over TRIM** unless valuations actively impair the thesis (gross-margin compression, demand-side disappointment, NVDA-specific corporate-governance event). The "lock in gains" instinct that feels like prudence usually isn't.

**Calibration**: this is *wisdom*, not a current data point. The wiki's bull thesis on NVDA is currently held on Tensor Core hardware moat + $1T contracted demand + Vera Rubin roadmap (not on momentum). But sizing discipline matters more than directional conviction at current levels — see the chip-sector top warning from Damodaran ([[2026-05-16-damodaran-profg-markets]]) for the counter-anchor.

## Key questions / what to watch
1. **Q1 FY27 gross margin print** (calendar Q2 2026 release) — direction and management commentary on Blackwell mix
2. **Hyperscaler capex commentary** — every MSFT / AMZN / GOOGL / META quarterly call is an NVDA read-through
3. **Vera Rubin pricing and timing** — is the cycle still accelerating?
4. **TPU / custom silicon disclosures from GOOGL, AMZN** — are hyperscalers reducing NVDA dependence?
5. **Sovereign AI deal flow** — incremental demand or replacement?

## Recent developments
- **2026-05-17** — Q1 FY27 earnings preview (Tuesday May 20). Street consensus: **$78.78B revenue, $1.76 adj EPS** (+78.8% YoY). Q2 consensus: **$86.08B** (+9.3% sequential). Goldman calling "major re-rating" pre-earnings; BofA $320 PT on $1.7T AI data center TAM forecast. **Historical pattern**: NVDA has fallen on 4 of last 5 earnings despite revenue beats of 3-4%; avg implied move 5-6%, realized 4.23%. **Tactical read**: forward guide on Q2 > $86B is what matters; Q1 beat is priced.
- **2026-05-13** — Source ingest [[2026-05-13-semianalysis-value-capture]]. SemiAnalysis pricing model on Vera Rubin NVL72:
  - **Cost floor**: $4.92/GPU-hour (5-yr, 15% prepay, 15.6% IRR baseline)
  - **Value ceiling**: $12.25/GPU-hour ($/PFLOP parity with GB300); conservative $9.63
  - Current pricing yields $0.28/PFLOP — **below historical trend**
  - **~40% NVDA price increase still leaves neocloud margin headroom**
  - **SOCAMM** (socketed memory in VR NVL72): $8/GB Q1 → potentially **>$13/GB by EOY 2026**; ~60% gross margin disaggregated pricing not possible on GB300's soldered LPDDR5X. Material new revenue line.
  - Capex per watt only ticked $37.4/W → $38.1/W despite nearly doubled TDP — NVDA "leaving value on the table"
  - GB300 vs H100: 17x throughput FP8, 32x FP4 — productivity multiplier real
  - **Counter-tension to bear case**: Anthropic inference gross margin 38% → 70%+ on ARR explosion $9B → $44B. If margins are 70%, capex IS earning its cost of capital.
- **2026-05-13** — Cerebras (CBRS) IPO May 13 at $48.8B valuation. Wafer-scale competitor. 86% UAE customer concentration limits immediate hyperscaler threat. See [[CBRS]].
- **2026-05-09** — Source ingest [[2026-05-09-dwarkesh-dylan-semianalysis]] adds: $90B long-term contracts; >70% of N3 by 2027; "X-1 not AGI-pilled" supply-chain framing; H100-worth-more-today economics; Samsung Texas LPU launch (a separate non-TSMC supply line for Nvidia, paired with Tesla's robot chips).
- **2026-02-25** — Q4 FY26 earnings: $68B revenue; Q1 FY27 outlook framed by Fortune as "quashing AI bubble talk." [Fortune](https://fortune.com/2026/02/25/nvidia-nvda-earnings-q4-results-jensen-huang/)
- **2026 (ongoing)** — Blackwell platform sold out through mid-year; backlog into Vera Rubin
- **2026-05** — analyst commentary highlighting earnings catalyst + Vera Rubin demand as bullish setup. [earezki.com](https://earezki.com/ai-financial-news/2026-05-06-nvda/)

## Related
[[nvda-supply-chain]] · [[ai-capex-cycle]] · [[bottleneck-roadmap]] · [[semiconductors]] · [[TSM]] · [[ASML]] · [[ARM]] · [[MU]] · [[AMKR]] · [[KLAC]] · [[LRCX]] · [[AMAT]] · [[COHR]] · [[LITE]] · [[GLW]] · [[DELL]] · [[HPE]] · [[VRT]] · [[ETN]] · [[AMD]] · [[AVGO]] · [[GOOGL]] · [[MSFT]] · [[AMZN]] · [[META]] · [[market-concentration]] · [[ai-bubble-debate]] · [[overview]]

> **Competitors:** [[AMD]] (MI400/MI450/Helios) and [[AVGO]] (custom XPU for 6 hyperscalers) are the two material non-NVDA hedges in the wiki.

> See [[nvda-supply-chain]] for the full ecosystem map: every public company that builds for, ships to, or has been funded by NVIDIA.

## Citations
- NVIDIA Q1 FY26 release: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026
- Fortune on Q4 FY26: https://fortune.com/2026/02/25/nvidia-nvda-earnings-q4-results-jensen-huang/
- S&P Global Q1 FY26 preview: https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/05/nvidia-earnings-preview-fiscal-q1-2026
- Intellectia $1T demand: https://intellectia.ai/blog/nvidia-stock-analysis-2026-ai-demand
- Intellectia May 2026 analysis: https://intellectia.ai/blog/nvidia-stock-analysis-may-2026
- IG Q1 2026 preview: https://www.ig.com/en/news-and-trade-ideas/nvidia-q1-2026-earnings-preview--what-to-expect-amid-ai-boom-250527
- TIKR strong signal piece: https://www.tikr.com/blog/nvidia-just-sent-a-strong-signal-heres-what-comes-next-in-2026
- earezki 21-day outlook: https://earezki.com/ai-financial-news/2026-05-06-nvda/

## Sources
1. [[2026-05-09-dwarkesh-dylan-semianalysis]] — primary source for $90B contracts, "X-1" framing, H100 long-life depreciation
2. [[2026-05-13-culper-nvda-short-thesis]] — DoJ indictment of SMCI cofounder + Culper short thesis on export-control diversion to China via SE Asian intermediaries
3. [[2026-05-13-anthropic-cfo-podcast]] — Anthropic CFO confirms 9 of Fortune 10 customers + 500% NDR + $9B→$30B ARR; multi-platform compute strategy (Anthropic uses NVDA GPU + Tranium + TPU fungibly = NVDA share-of-wallet at top labs is not 100%)
4. [[2026-05-16-jim-fan-nvda-robotics]] — NVDA chief scientist Jim Fan on robotics moat layers (VLA→WAM, EgoScale scaling law, Dream Dojo simulator)
5. [[2026-05-16-horace-he-ml-systems]] — Meta PyTorch compilers lead Horace He: Tensor Core 15× moat, FP4 precision lever, 131K-GPU fault-tolerance ceiling
6. [[2026-05-16-druckenmiller-hard-lessons]] — Druckenmiller "couldn't stand success" exit anti-pattern at $800 → $1,400; sizing-discipline wisdom anchor (~March 2026 dated, stale)
7. [[2026-05-14-anthropic-2028-ai-leadership]] — Anthropic policy paper with Huawei = 4%/2% NVDA-compute data point + 11x US-China compute ratio claim (added 2026-05-17)
8. [[2026-05-16-dylan-patel-invest-like-best]] — Dylan Patel: GPU 7-8 yr useful life (refutes Burry depreciation bear); Anthropic compute-constrained (added 2026-05-17)
