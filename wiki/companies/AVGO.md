---
type: company
ticker: AVGO
tags: [ai, semis, custom-silicon, networking, hyperscaler]
last_updated: 2026-05-14
last_full_review: 2026-05-09
sources: 0
conviction: high
stance: bull
---

# Broadcom (AVGO)

**Stance:** bull · **Conviction:** high · **Time horizon:** long-term

> **DEVELOPMENT 2026-05-14 (mildly bearish near-term, thesis intact):** Reports indicate **Broadcom's custom AI hardware plan with OpenAI hit a financing roadblock** — Broadcom will only finance Project Titan's first phase if **Microsoft commits to buying ~40% of the chips**. **OpenAI's first-gen XPU with Broadcom now expected to deploy in volume in 2027 at >1 GW** (was previously framed as mass production late 2026 — material timing slip). **Stock dropped ~3% on the report.** Net read: doesn't change the structural bull case (Anthropic's 5 GW TPU + Broadcom partnership and existing 5-customer pipeline are intact) but materially de-emphasizes Project Titan as the near-term catalyst the wiki was tracking. Watch for: (a) MSFT commitment language on Project Titan, (b) Q3 2026 update on OpenAI XPU deployment timeline.

## One-line thesis
The non-Nvidia AI infrastructure pure play — designs custom AI accelerators (XPUs) for **six hyperscalers** (Google, Meta, ByteDance, Anthropic, OpenAI, plus one more), ships the world's first **102.4 Tbps switching silicon** (Tomahawk 6), and projects **$100B AI revenue by 2027**. The OpenAI "Project Titan" deal alone targets **10 GW of deployed compute by 2029**. The single best NVDA hedge.

## Role in the NVDA stack
- **Custom XPU (AI accelerator) silicon** — directly competes with NVDA for hyperscaler in-house silicon mandates
  - **Google TPU** — Broadcom is the design partner (multi-generation, including Anthropic's Ironwood TPU v7)
  - **Meta MTIA** — co-developed; **1GW+ first phase**, multi-gigawatt rollout
  - **OpenAI "Project Titan"** — co-developed custom inference engine, **10 GW deployed by 2029, mass production late 2026**
  - **ByteDance** — confirmed partner
- **Tomahawk 6** — first-to-market 102.4 Tbps switching silicon (volume early 2026); **doubles bandwidth vs. predecessor**
- **Jericho** — long-haul AI fabric switching silicon
- "Walled garden" via integrated **XPU + Jericho + Tomahawk + custom optics** = a full alternative to NVIDIA NVLink/Spectrum-X stack
- **VMware** — software / virtualization layer providing FCF ballast

## Snapshot (as of May 2026; verify before any decision)
| Metric | Value | As of |
|---|---|---|
| Q1 FY2026 AI revenue | **$8.4B (+106% YoY)** | Q1 FY2026 |
| 2027 AI revenue target (CEO Hock Tan) | **~$100B** | management commentary |
| Confirmed custom XPU customers | **6 hyperscalers** | early 2026 |
| OpenAI Project Titan target | 10 GW by 2029 | 2026 |
| Meta XPU deal | 1+ GW first phase | Q2 2026 |

## Bull case
- **OpenAI Project Titan is a category-defining deal.** 10 GW by 2029 — that is comparable in magnitude to entire hyperscaler 2026 capex programs. Mass production late 2026.
- **AI revenue +106% YoY to $8.4B in Q1 FY2026** — re-acceleration evidence
- **$100B AI run-rate by 2027** per Hock Tan — implied multi-year compounding
- **Tomahawk 6 monopoly** — first-to-market 102.4 Tbps; only viable alternative to NVDA's NVLink/Spectrum-X for million-node clusters
- **Hyperscaler "walled garden"** — once a hyperscaler commits to Broadcom's full stack (XPU + switch + optics), switching costs are enormous
- **The non-NVDA hedge** — only public name with credible custom-silicon scale; if hyperscalers shift incremental dollars away from NVDA, AVGO is the largest beneficiary
- **VMware FCF ballast** — software annuity reducing dependence on the cyclical chip business

## Bear case / risks
- **Customer concentration risk masked by partnership structure** — Google + Meta + OpenAI are huge, but losing one is catastrophic
- **Per Broadcom: "AI companies can't make their own silicon"** — but they ARE making it (with Broadcom). The thesis depends on hyperscalers continuing to outsource design to AVGO rather than going fully in-house long-term
- **NVDA defense (CUDA + ecosystem moat)** — even with custom silicon, training stays sticky on Nvidia
- **Premium multiple already paid** — much of the AI thesis is in the price; downside on any execution miss is sharp
- **VMware integration ongoing** — pricing strategy controversies with customers
- **Hock Tan succession risk** — long-tenured CEO concentration
- **Dependence on [[TSM|TSMC]]** — same fab capacity issues as everyone else

## Key questions / what to watch
1. **Project Titan production milestones** — late 2026 mass production is the gate
2. **Q2-Q4 FY2026 AI revenue trajectory** — does the +106% sustain?
3. **Tomahawk 6 deployment scale** — early hyperscaler rollouts
4. **Meta XPU revenue contribution** quarter-over-quarter
5. **VMware revenue / margin trajectory** — software ballast holding?
6. **6th hyperscaler customer** — public disclosure?

## Recent developments
- **2026-04** — Broadcom shares +6% on **Alphabet + Anthropic multi-year deals** (custom silicon revenue lock-in)
- **2026-04** — Meta announced **expanded co-development of custom AI silicon** with Broadcom (1 GW+ first phase)
- **2026-Q1** — Project Titan disclosed: OpenAI custom inference XPU; mass production late 2026; 10 GW by 2029
- **2026-Q1** — AI revenue $8.4B (+106% YoY)
- **2026-Q1** — Tomahawk 6 (102.4 Tbps) shipping in volume
- **2026-05-17 — Tomahawk 6 shipping with 200G/lane CPO + photonic substrates** per [[2026-05-17-multi-agent-research-batch]] Agent C. The networking-silicon stack now has full optical integration — direct read-through to [[SOITEC]] photonics-SOI substrates supplying the CPO module beneath the switch silicon. Goldman: silicon photonics revenue doubling in 2026 across foundries. **Which means**: AVGO's network-silicon moat is compounding with the optical-integration moat; Tomahawk 6 is a generation ahead of the MRC industry consortium (which Google's Apollo/Palomar already obsoleted per [[2026-05-17-semiwiki-forum-sweep-2]] Thread B).

## Related
[[NVDA]] · [[nvda-supply-chain]] · [[GOOGL]] · [[META]] · [[CRWV]] · [[NBIS]] · [[ai-capex-cycle]] · [[cloud-hyperscalers]] · [[bottleneck-roadmap]] · [[overview]]

## Citations
- FinancialContent on Alphabet + Anthropic deals: https://markets.financialcontent.com/stocks/article/marketminute-2026-4-7-broadcoms-custom-silicon-strategy-propels-shares-6-as-alphabet-and-anthropic-lock-in-multi-year-ai-deals
- Invezz / TradingView on AVGO Wall Street favorite 2026: https://www.tradingview.com/news/invezz:7324249d0094b:0-broadcom-stock-is-becoming-wall-street-s-favourite-ai-trade-for-2026-here-s-why/
- The Register on Q1 FY2026: https://www.theregister.com/2026/03/05/broadcom_q1_2026/
- Meta's announcement on Broadcom partnership: https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/
- FinancialContent "Bespoke Billion" deep-dive: https://markets.financialcontent.com/stocks/article/tokenring-2026-2-6-the-bespoke-billion-how-broadcom-is-architecting-the-post-nvidia-ai-era-through-custom-silicon-and-light
- io-fund AI monetization piece: https://io-fund.com/ai-stocks/broadcom-stock-silent-winner-ai-monetization
- FinancialContent Broadcom deep dive: https://markets.financialcontent.com/stocks/article/finterra-2026-3-10-the-architect-of-the-ai-era-a-deep-dive-into-broadcom-inc-avgo
- The Index Times on Tomahawk 6: https://www.theindextimes.com/post/avgo-broadcom-ships-the-world-s-first-102-4-tbps-switch-as
- FinancialContent Custom Silicon Gold Rush: https://markets.financialcontent.com/stocks/article/tokenring-2026-1-22-the-custom-silicon-gold-rush-how-broadcom-and-the-cloud-titans-are-challenging-nvidias-ai-dominance
