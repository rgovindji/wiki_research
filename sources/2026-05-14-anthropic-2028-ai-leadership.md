---
date: 2026-05-14
type: research_paper
publisher: Anthropic
url: https://www.anthropic.com/research/2028-ai-leadership
title: "2028: Two Scenarios for Global AI Leadership"
touches: [us-china-relations, ai-bubble-debate, NVDA, ai-capex-cycle]
---

# Anthropic — "2028: Two Scenarios for Global AI Leadership"

## TL;DR
- **Anthropic-authored research/policy paper (May 14, 2026)** explicitly arguing that the US currently holds a "commanding advantage" in frontier AI compute over China, but is at risk of losing it within 2-3 years absent policy action.
- **Headline quantitative claims**: Huawei will produce only **4% of NVIDIA's 2026 aggregate compute, 2% in 2027**; strengthened export controls could give US access to **~11× more compute than China's AI sector**.
- **Safety disparity**: DeepSeek R1 complied with **94% of malicious requests vs. 8% for US frontier models** — sharpest concrete claim of US-frontier-lab safety lead.
- **Anthropic's policy ask**: close chip-smuggling loopholes; restrict distillation attacks (legislation + threat-intelligence sharing); export US AI globally.
- **Two scenarios for 2028**: (Optimistic) US maintains 12-24 month lead, sets global AI norms; (Pessimistic) Chinese models reach near-parity, China exports "good enough" AI globally, PLA gains cyber advantages.

## Key facts and quantitative claims

| Claim | Value | Implication |
|---|---|---|
| Huawei compute / NVDA 2026 | **4%** | NVDA moat is massive in absolute terms |
| Huawei compute / NVDA 2027 | **2%** | Gap *widens* without policy change |
| US compute ratio with strong controls | **11× China** | The "11x lead" is the bull case for US lab moat |
| DeepSeek R1 malicious-request compliance | **94%** | vs. US models at 8% |
| Chinese AI labs publishing safety evals | **3 of 13** | Most don't even publish safety methodology |
| US model intelligence lead | "Several months" | Frontier-edge moat, not commodity-tier |

## The two scenarios (paraphrased)

**Optimistic (US maintains lead)**:
- US holds 12-24 month intelligence lead
- American AI becomes the global standard
- Democracies set governance norms
- US cyber security improves

**Pessimistic (China reaches parity)**:
- Chinese models reach near-parity with US
- Beijing achieves rapid domestic adoption
- PLA gains AI-enabled cyber capabilities
- China exports cheaper "good enough" AI globally — *exactly the dynamic the wiki tracked yesterday via the OpenRouter 36% Chinese token share data point*

## Military / national-security claims (Anthropic-stated)

- PLA views "intelligentization" as means to surpass US military
- AI-enabled cyber ops pose grave threats to critical infrastructure
- Frontier AI could enable "automated repression at scale"
- "Compute advantage compounds into military advantage"
- DeepSeek models cited as deployable for: swarm-coordination of unmanned vehicles, cyber-offense capabilities

## Anthropic's policy recommendations

1. **Close smuggling/overseas access loopholes** — enforcement + semiconductor manufacturing equipment (SME) controls
2. **Restrict distillation attacks** — legislation + threat-intel sharing among US labs
3. **Export American AI globally** — lock in democratic influence over infrastructure

## Key claims (and how confident)

- **High confidence (Anthropic-stated, quantitative)**: Huawei compute = 2-4% of NVDA's compute in 2026-2027. This is the most useful single data point for the wiki. Verifiable from chip-production data.
- **High confidence (Anthropic-stated, quantitative)**: DeepSeek R1 vs US frontier models on safety compliance (94% vs 8%). Anthropic's framing but consistent with broader red-teaming research.
- **Medium confidence (policy-motivated)**: The "11× compute advantage with strong controls" claim is a *conditional* — assumes successful control implementation, which is uncertain.
- **Speculative (Anthropic's own framing)**: The military / cyber-offense / repression-at-scale claims are forward-looking policy framing — true that capabilities exist but the deployment claims are unverified.

## Key quotes (paraphrased — verify against full paper if quoting)

> "Democracies currently hold a commanding advantage in frontier AI but risk losing it without immediate policy action."

> [On DeepSeek] "DeepSeek trained its latest model on advanced US chips that are banned from sale to China."

> "Compute advantage compounds into military advantage."

## Connect-the-dots / investment implications

1. **The single most important data point for [[NVDA]] bulls is the 4%/2% Huawei compute share.** This is the cleanest quantitative answer the wiki has captured to "how big is China's compute gap?" The answer: roughly 25-50x smaller than NVDA's output. **Which means** the NVDA moat is not just qualitative ecosystem lock-in but *literal hardware-production scale dominance* — and the gap is widening in 2027 unless China can substitute on the semiconductor-manufacturing-equipment side (ASML lithography, AMAT etch/depo, KLAC inspection). **Reinforces [[NVDA]], [[ASML]], [[AMAT]], [[KLAC]], [[LRCX]] core bull theses.**

2. **The 94% vs 8% malicious-compliance gap is a real product differentiator.** This is the steelman for why enterprise buyers pay Anthropic/OpenAI premium prices over open-weight Chinese models even when "performance" is similar. **Frontier-lab pricing power is durable on safety/compliance dimensions even if not on raw capability.** Supports the bull case for Anthropic / OpenAI premium-tier pricing the wiki has been tracking via [[ai-capex-cycle]].

3. **LeCun's accusation (from [[2026-05-16-yann-lecun-ame-labs]]) is contextually validated**: Anthropic IS doing policy advocacy that benefits its commercial position. LeCun called this "regulatory capture" framing. The 2028 paper is exactly that — a frontier lab arguing for export controls that protect its compute advantage. **Both can be true**: Anthropic's analysis is empirically grounded AND commercially self-serving. Discount the policy recommendations accordingly.

4. **The paper essentially names the China problem the wiki tracked yesterday**: per the May-16 HN thread analysis, 36% of OpenRouter token volume is Chinese open-weight models. Anthropic's pessimistic scenario (China exports "good enough" AI globally) is *already happening* at the inference-platform layer. The paper is a Hail Mary attempt to stop the slide by tightening chip controls.

5. **Trade-policy implication for the wiki**: If Anthropic's policy proposals get adopted in the next administration, this is bullish for ASML (SME controls = preserve EUV monopoly), AMAT (etch/depo controls), and KLAC (inspection controls). If they don't, the Chinese open-weight tier continues to commoditize Western pricing at the second-tier.

## Wiki updates made

- Added Huawei compute = 4% of NVDA 2026 / 2% 2027 data point to [[NVDA]] bull case
- Added Anthropic 2028 paper + safety-compliance disparity (94% vs 8%) to [[us-china-relations]]
- Added "Anthropic-as-regulatory-capture vs. Anthropic-as-empirically-correct" both-and framing to [[ai-bubble-debate]]
- Cross-referenced to yesterday's [[2026-05-17 OpenRouter 36% Chinese tokens]] entry (added 2026-05-17)

## What's NOT in this summary
- Full reasoning on each policy recommendation
- Specific details on alleged DeepSeek military deployments (paper is light on this)
- Anthropic's CSO methodology for the 94%/8% test
