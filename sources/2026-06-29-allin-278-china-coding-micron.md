---
date: 2026-06-29
type: podcast
publisher: All-In Podcast (ep. 278)
url: https://www.youtube.com/watch?v=w8ah_tA0yfg
raw_path: raw/podcasts/2026-06-29-allin-278-china-coding-micron.txt
touches: [MU, inference-economics, ai-bubble-debate, bottleneck-roadmap, ai-capex-cycle, semiconductors]
---

# All-In #278 — "China Catches Up in Coding, AI Memory Crunch, Micron's Blowout"

*Bias: HIGH and self-interested across the board. Guests Gavin Baker (Atreides — long Micron, SpaceX, Anthropic, AI-infra) and Travis Kalanick (building "Adams"); hosts Chamath, Sacks (the sitting AI czar, policy agenda), Jason. AI-maximalist framing throughout. Discount the magnitudes; weight Baker's structural/industry points (he's a heavyweight the wiki already tracks) and bias-flag the SpaceX/orbital/Anthropic-valuation talk as book-talking.*

## TL;DR
- **Micron / DRAM (Baker, the most wiki-relevant):** "DRAM is THE most important bottleneck" — above lasers, capacitors, power semis, NAND, HDDs (he derides the "bottleneck bros" who hunt esoteric Japanese suppliers). MU's **SCAs are "transformational"** — floor+ceiling pricing, ~**50% of revenue across just ~4 customers**, and the **floor pricing sits ABOVE prior-cycle-peak gross margins.** DRAM trades **cheap vs the rest of AI**; he estimates **DRAM = 30-40% of all hyperscaler capex next year.** Independent heavyweight corroboration of the wiki's SCA-decoupling thesis ([[mu-core-book-reconsideration]]).
- **China open-weight catch-up:** Z.AI's **GLM 5.2** (744B params, 1M context, MIT license) scored **51 on Artificial Analysis (highest open-weight ever), beat GPT-5.5 on SWE coding, trails Claude Opus 4.8 by <1pp, ~85% cheaper API**, reportedly **trained entirely on Huawei Ascend 910b** chips. Founder told Musk open-weight "fable-level" by <Q1 2027. The hardest open-weight-commoditization datapoint yet.
- **Baker's "composable models / council of LLMs":** every enterprise routes ~85% of queries to a cheap open-weight model, frontier models "conduct"/check the hardest. **Open source shifts economic value from frontier-lab margins → infrastructure** ("great for AI infra"). Frontier tokens ≈ 90% of *economic value*; open-source ≈ 80%+ of *tokens processed*.
- **US self-handicap:** Anthropic's "Fable" was **rolled back after a jailbreak report**; GPT-5.6 stuck in new approval hoops — so the best *available* US models are in "purgatory," which is *why* GLM 5.2 now matches them. Sacks (AI czar) frames it as Dario-driven regulatory-capture risk and a China-race liability.
- **CXMT (China DRAM IPO) floods CONSUMER-grade DRAM, NOT AI-grade** — "the cure for Apple's ills" — but only 3 firms can make AI-server DRAM (HBM/SOCAMM/LPDDR). Contains the China-supply-flood bear to the commodity tier.

## Key facts / claims (and how confident)
- **SCAs cover ~50% of MU revenue across ~4 customers, floor pricing above prior-peak gross margins (Baker, medium-high — heavyweight but long MU).** Directly validates the take-or-pay de-cyclicalization thesis; counters the Shkreli "cancelable when supply floods" bear at least on the structural point that the floor is contractually above prior peaks. Still doesn't resolve enforceability in a true bust.
- **DRAM = 30-40% of hyperscaler capex next year (Baker estimate, directional).** If even close, hundreds of billions flow straight to memory — a huge bull sizing for the complex.
- **GLM 5.2 matches available US frontier on coding at ~85% lower cost, Huawei-trained (high confidence it exists/benchmarks; "Huawei-only training" is a claim, possibly smuggled NVDA — Sacks flags both).** The open-weight gap is now ~"<1pp from Opus 4.8" on coding — the strongest commoditization evidence the wiki has logged, and it's Chinese + indigenous-silicon, which compounds the geopolitical read.
- **Distillation confirmed (Baker):** GLM-class models built partly by harvesting frontier reasoning traces via masked-account "phone farms" — a "cheat sheet" to the frontier; but GLM 5.2 is now "good enough to do its own RL," so the catch-up may be self-sustaining.
- **Inference disaggregation extends GPU life to 7-12 years (Baker):** prefill (memory-capacity-bound) vs decode (memory-bandwidth-bound) are being split; Grok (now NVDA) / Cerebras decode-optimized chips placed in front of old H100s/A100s make them competitive → **lowers cost-to-finance the buildout** (counters the Burry 1-3yr depreciation bear).
- **Anthropic ≈ $3T if public, exiting 2026 >$100B revenue, ~85% inference gross margin (Baker, book-talking).** Bigger than the $900B private mark the wiki logged; treat as an enthusiastic estimate.
- **Memory inflating DC cost may be "good for society" (Baker):** 1GW DC ≈ $35B NVDA silicon + $25B power/cooling; rising memory cost slows the prisoner's-dilemma buildout, buying time to adapt.
- **NVDA = "the American open-source champion" (Sacks):** could release a GLM-beating open model anytime but won't (channel conflict with customers). Baker: if OpenAI (Jalapeño/Broadcom), Google (TPU), Elon all make silicon, NVDA could retaliate — even start an OpenAI competitor. Speculative.
- **Megapods / modular prefab data centers:** Tesla filed a "Megapod" trademark (modular DC-in-a-container); 90-day build cycle; DELL (racks) + Vertiv (modules) named beneficiaries. Orbital-compute pitch (SpaceX-promotional): $5B launch/GW once Starship reusable → space cheaper than terrestrial in 3-4 yrs.
- **Cerebras broke deal price post-IPO** → triggered "break-deal-price = forced selling" PM behavior + short pile-on; Baker's frame: for these IPOs, the only metric that matters is "how many megawatts can they bring on" (monetization rate is known).

## Quotes worth keeping
> "The bottleneck that matters is DRAM... not lasers, not capacitors, not power supply semiconductors, not NAND flash, not HDDs. DRAM." — Baker

> "The floor pricing in these new [SCA] contracts is ahead of prior cycle peaks from a gross-margin perspective... this may end up being very transformational for the industry." — Baker

> "Open source... shifts economic value from the margins of the frontier labs to the infrastructure. That's not bad for AI — it's great for [infra]." — Baker

> "DRAM is probably going to be 30 to 40% of all hyperscaler capex next year." — Baker

> "We're on a shot clock... they're 6 months behind on the model and 24 months behind on the silicon, yet only a few months behind in total. We are going to lose if we keep doing this stuff to ourselves." — Sacks (on the China AI race)

## Wiki updates made
- [[MU]] — Baker bull corroboration (DRAM = THE bottleneck; SCAs transformational ~50% rev/4 customers/floor>prior-peak GM; DRAM cheap vs AI; 30-40% of hyperscaler capex; CXMT floods consumer-not-AI-grade) — counters the Shkreli bear; stance held bull/high.
- [[inference-economics]] — GLM 5.2 open-weight datapoint + Baker composable-models/council-of-LLMs (value→infra) + inference disaggregation (prefill/decode, GPU 7-12yr life).
- [[ai-bubble-debate]] — China open-weight catch-up + US regulatory self-handicap (Fable rollback) as a competitive both-sides; Anthropic $3T/$100B; memory-slows-buildout framing.
- [[bottleneck-roadmap]] — Baker's "DRAM above all" heavyweight prioritization (tensions the multi-bottleneck/esoteric-supplier framing); CXMT consumer-vs-AI-grade; GPU-longevity via decode disaggregation.
- [[ai-capex-cycle]] — DRAM 30-40% of hyperscaler capex; Anthropic demand-pull update; megapods/modular DC (DELL/VRT); orbital-compute economics.
