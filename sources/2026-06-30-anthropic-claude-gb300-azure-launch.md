---
date: 2026-06-30
type: article
publisher: NVIDIA Blog / Investing.com / Microsoft
url: https://blogs.nvidia.com/blog/anthropic-nvidia-gb300-blackwell-ultra-microsoft-azure/
raw_path:
discovery: feed_scan r/stocks (investor) → DeepSeek triage 7/10 → verified
touches: [NVDA, MSFT, ai-capex-cycle]
---

# Anthropic's Claude goes GA on Microsoft Azure (Foundry), running on NVIDIA GB300 Blackwell Ultra

## TL;DR
- Anthropic's Claude models (Haiku, Sonnet, Opus) are now **generally available in Microsoft Foundry on Azure**, running on **NVIDIA GB300 NVL72 (Blackwell Ultra)** systems with Quantum-X800 InfiniBand — announced 2026-06-29. This is the **first concrete deployment milestone** of the Nov 2025 Microsoft–NVIDIA–Anthropic strategic partnership.
- It operationalizes Anthropic's **$30B Azure compute commitment** (plus up to ~1 GW of additional contracted capacity); the same Nov-2025 deal had Microsoft investing up to $5B and NVIDIA up to $10B into Anthropic at a ~$350B valuation.
- For [[NVDA]] this is notable because it is the **first time Anthropic runs production inference on NVIDIA silicon** (Anthropic historically leaned on AWS Trainium + Google TPU); for [[MSFT]] it adds Claude as a first-party Azure model alongside OpenAI.

## Key facts
- **What deployed:** Claude Haiku, Sonnet, Opus, GA in Microsoft Foundry on Azure, on **NVIDIA GB300 NVL72** rack-scale systems (72 Blackwell Ultra GPUs + 36 Grace CPUs, fully liquid-cooled) with **Quantum-X800 InfiniBand** networking. (High — NVIDIA + Microsoft blogs, 2026-06-29.)
- **Regions:** Live in **East US and West Europe** at launch; **Southeast Asia, Australia East, UK South** by mid-July 2026. (High.)
- **Deal context (Nov 2025):** Anthropic committed to **$30B of Azure compute** and to contract **up to ~1 gigawatt** of additional capacity; **Microsoft to invest up to $5B**, **NVIDIA up to $10B** into Anthropic; valuation put in the **~$350B** range. (High — CNBC, Microsoft blog, Anthropic, 2025-11-18.)
- **Strategic framing:** NVIDIA describes this as "the first time NVIDIA and Anthropic are establishing a deep technology partnership." Positions GB300 for large agentic systems / specialized sub-agents. (High — NVIDIA blog.)
- **Prices (verified via Polygon, ticker_ta.py, close 2026-06-29):** [[NVDA]] **$194.97** (below EMA20 $204.65 / EMA50 $205.05, above EMA200 $188.29; off the 2026-05-14 high of $236.54). [[MSFT]] **$368.57** (below all three EMAs — 20 $387.80 / 50 $400.67 / 200 $428.25; deep in a downtrend off the 2025-10-28 high of $553.72).

## Key claims (and how confident)
- **This is the first Anthropic-on-NVIDIA production deployment.** (Medium-high — consistent with prior wiki notes that Anthropic ran fungibly on Trainium + TPU + some NVDA GPU; the "first deep partnership" language is NVIDIA's. Anthropic was already a named Vera CPU early customer per [[2026-06-01-nvda-rtx-spark-computex-keynote]], so NVIDIA share-of-wallet at Anthropic was already rising.)
- **Demand-side anchor for NVDA, not a fundamental re-rate.** A GA launch in two regions is a milestone, not a volume disclosure — no GPU count or revenue figure attached. (High on the caveat.)
- **For MSFT, this is incremental model breadth, not margin.** Claude on Foundry is Azure renting capacity to a lab that also competes with MSFT's own MAI models and OpenAI; the $30B is Anthropic *spending on* Azure, which is Azure revenue. (Medium — directionally clear, no segment detail.)

## Quotes worth keeping
> "Claude in Microsoft Foundry accelerated by NVIDIA GB300 GPUs on Azure builds on the strategic partnership Microsoft, NVIDIA and Anthropic announced in November." — NVIDIA blog, 2026-06-29

## Wiki updates made
- Added dated connect-the-dots bullet to [[NVDA]] `## Recent developments` (first Anthropic-on-NVIDIA production inference; $30B Azure / ~1 GW deal operationalized).
- Added dated connect-the-dots bullet to [[MSFT]] `## Recent developments` (Claude GA on Foundry; Azure as the compute landlord for the $30B Anthropic commitment).
- Light note to [[ai-capex-cycle]] — the Nov-2025 circular-financing structure (NVDA/MSFT invest into Anthropic, Anthropic commits to Azure on NVDA silicon) now has product behind it.
