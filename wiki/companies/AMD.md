---
type: company
ticker: AMD
tags: [ai, semis, gpu, cpu, datacenter]
last_updated: 2026-05-09
last_full_review: 2026-05-09
sources: 0
conviction: high
stance: bull
---

# Advanced Micro Devices (AMD)

**Stance:** bull · **Conviction:** high · **Time horizon:** long-term

## One-line thesis
The credible #2 AI GPU vendor — **OpenAI signed a 6 GW AMD GPU deal**, **Meta signed a 6 GW AMD deal** (with a 160M-share warrant), Oracle is deploying **50,000 MI450s** in superclusters. MI400/Helios rack on **[[TSM|TSMC]] 2nm** in Q3 2026 with 3 AI exaflops/rack. Unlike Broadcom's custom silicon thesis, AMD targets **inference** workloads where multi-vendor is real — and EPYC server CPUs are independently winning share against Intel.

## Role in the NVDA stack
- **AI GPU competitor** — Instinct MI400 / MI450 / MI455X / MI500 series
- **Helios rack platform** (Q3 2026) — 72 MI455X accelerators + 31TB HBM4 = 3 AI exaflops/rack; AMD's first credible answer to NVIDIA NVL72 / Vera Rubin NVL72
- **TSMC 2nm** — first-generation 2nm AI chips alongside Apple
- **EPYC** — server CPUs winning share at hyperscalers + enterprise; complementary to GPU thesis
- **ROCm** — open-source software stack vs. CUDA (still the biggest gap)

## Snapshot (as of May 2026; verify before any decision)
| Metric | Value | As of |
|---|---|---|
| OpenAI deal | **6 GW** AMD GPUs starting H2 2026 | Oct 2025 |
| Meta deal | **6 GW** Instinct GPUs + custom MI450 + 160M-share warrant | Feb 2026 |
| Oracle deal | **50,000 MI450s** in new AI superclusters | 2026 |
| Helios rack launch | **Q3 2026** | management |
| Process | TSMC 2nm (first-gen) | 2026-2027 |

## Bull case
- **Three landmark customer wins:** OpenAI 6 GW + Meta 6 GW + Oracle 50K MI450s — these are not POCs, they are committed deployments
- **Inference is where multi-vendor is real.** Per Lisa Su: largest AI deployments are inference-focused; ROCm + price/perf can win without dethroning CUDA on training
- **MI400/450 sampling to lead customers** — productization is already in motion
- **Helios rack-scale architecture** — finally addresses NVDA's biggest remaining moat (NVLink rack-scale)
- **EPYC franchise** is independently strong — server CPU share gains continue regardless of GPU wars
- **Smaller AI revenue base than NVDA = bigger relative growth** if any of OpenAI/Meta/Oracle deals scale
- **Per Dylan Patel** ([[2026-05-09-dwarkesh-dylan-semianalysis]]): AMD is one of the few names alongside NVDA holding TSMC capacity allocation cards

## Bear case / risks
- **CUDA / ecosystem moat at NVDA is real.** Even with comparable hardware, training stays sticky. If the AI workload mix doesn't shift to inference fast enough, AMD's TAM stays capped
- **Execution risk on MI450 ramp.** TSMC 2nm is brand new; Helios is a brand new rack architecture. Per Dylan: "this is a big risk for AMD that causes potential delays because it's a brand-new process technology"
- **Customer concentration in announced deals.** OpenAI + Meta + Oracle are huge, but losing one is material
- **Premium multiple** already pricing significant share gain
- **Custom silicon (AVGO partners) is a parallel threat.** If hyperscalers shift to in-house silicon via [[AVGO]], AMD is squeezed in the middle (between NVDA premium and bespoke cheaper alternatives)
- **HBM allocation** — same memory crunch as everyone else; AMD competes for HBM4 against NVDA + custom silicon
- **TSMC CPU > GPU allocation bias** (per Dylan) — AMD's CPU business may get priority over GPU at TSMC

## Key questions / what to watch
1. **MI450 production ramp** — does Helios ship Q3 2026 on schedule?
2. **OpenAI deployment milestones** — first MI450 data center online
3. **Meta deal revenue conversion** — quarterly disclosure
4. **EPYC share gains** vs. Intel — independent of AI thesis
5. **ROCm software adoption** — bridge to closing CUDA gap
6. **Gross margin trajectory** as AI mix grows
7. **HBM4 allocation** — does AMD secure enough?

## Recent developments
- **2026-05-17 — AMD outpacing Intel 5x in the AI-CPU shortage cycle** (per [[2026-05-17-semiwiki-cpu-shortage-intel-18a]]). **AMD Q1 2026 revenue +38% YoY vs Intel +7% YoY**. Both are supply-constrained, but AMD's relative-growth signal is the cleanest read in the CPU cycle — AMD is winning share AND benefiting from price hikes (10-15% recent industry-wide). **Which means** Intel's "AI CPU" narrative is hollowed out on a relative basis; the structural read is that AMD's EPYC + MI accelerator cross-sell is producing real wallet-share movement.
- **2026-05-11** — AMD provided **Q2 revenue guide ~$11.2B**, surpassing Wall Street consensus; **20+ brokerages raised price targets** post-print. AI revenue ramp clearly visible in the guide.
- **2026-Q1/Q2** — MI450 sampling to lead customers; production targets H2 2026
- **2026-02** — Meta announced 6 GW expanded partnership + custom MI450 + 160M-share warrant
- **2026-01 (CES)** — Helios AI rack details + MI400 lineup unveiled
- **2025-10** — OpenAI 6 GW GPU deal announced; first 1 GW data center on MI450

## Related
[[NVDA]] · [[nvda-supply-chain]] · [[TSM]] · [[AVGO]] · [[META]] · [[CRWV]] · [[ORCL]] · [[INTC]] · [[ARM]] · [[ai-capex-cycle]] · [[cloud-hyperscalers]] · [[bottleneck-roadmap]] · [[semiconductors]] · [[overview]]

## Citations
- DCD on MI400/MI500: https://www.datacenterdynamics.com/en/news/amd-unveils-full-mi400-product-lineup-claims-mi500-chips-will-deliver-1000x-increase-in-ai-performance/
- Wccftech on MI450 sampling: https://wccftech.com/amd-sampling-mi450-gpus-engaged-with-customers-on-mi500-largest-ai-deployments-are-for-inference/
- AMD Meta 6GW announcement: https://www.amd.com/en/newsroom/press-releases/2026-2-24-amd-and-meta-announce-expanded-strategic-partnersh.html
- TechTimes on Helios + MI400 (CES 2026): https://www.techtimes.com/articles/313781/20260106/ces-2026-amd-details-helios-ai-rack-next-gen-instinct-mi400-gpus.htm
- Tom's Hardware AMD-Oracle 50K MI450: https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-and-oracle-partner-to-deploy-50-000-mi450-instinct-gpus-in-new-ai-superclusters-deployment-of-expansion-set-for-2026-powered-by-amds-helios-rack
- TechNewsWorld AMD-OpenAI deal: https://www.technewsworld.com/story/why-amds-openai-deal-marks-a-new-era-for-ai-data-centers-179954.html
- Markets Daily Meta 6GW + warrant: https://www.themarketsdaily.com/2026/02/27/advanced-micro-devices-expands-meta-ai-deal-6gw-instinct-gpu-plan-custom-mi450-and-160m-share-warrant.html
- DigitalCitizen MI450 sampling: https://www.digitalcitizen.life/amd-starts-sampling-mi450-ai-gpus-as-inference-demand-grows/
- AMD CES 2026: https://www.amd.com/en/newsroom/press-releases/2026-1-5-amd-and-its-partners-share-their-vision-for-ai-ev.html
- FinancialContent AMD OpenAI deal: https://markets.financialcontent.com/stocks/article/marketminute-2025-10-9-amd-soars-to-new-heights-on-landmark-openai-deal-igniting-ai-market-optimism
