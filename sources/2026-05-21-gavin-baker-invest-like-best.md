---
date: 2026-05-21
type: podcast
publisher: Invest Like the Best (Patrick O'Shaughnessy)
url: n/a (transcript provided by user)
raw_path: raw/podcasts/new_podcast.txt
touches: [ai-bubble-debate, ai-capex-cycle, ai-infrastructure-debt, bottleneck-roadmap, space-economy, sovereign-ai, NVDA, TSM, ALAB, MSFT, AMZN, GOOGL, META, AMD, INTC, TSLA, MU]
---

# Gavin Baker (Atreides) on Invest Like the Best — Source Summary

Gavin Baker's 6th appearance on Invest Like the Best with Patrick O'Shaughnessy. Recorded just before Google I/O (so ~May 16–20, 2026). Baker runs Atreides Management. The conversation is dense and ranges across AI economics, watts/wafers, orbital compute, hyperscalers, chip startups, and personal safety in an AI-political world.

## TL;DR

- **Anthropic added ~$11B of ARR in a single month (March 2026)** — more than Palantir + Snowflake + Databricks combined, who each took ~10 years. Baker: *"nothing like that has ever happened in the history of capitalism."*
- **March–April 2026 selloff = a buying window** analogous to DeepSeek Jan 2025. Strait of Hormuz closure was **net-bullish for US AI** (Henry Hub nat gas −20% while Asian/EU nat gas doubled/tripled → US manufacturing/electricity competitiveness improved).
- **TSMC capacity discipline is the single bubble-prevention mechanism.** If TSMC built what Nvidia wants, Nvidia could sell **$2–3T of GPUs** in 2026–27, which would guarantee an overbuild. Watch TSMC's capacity decisions to call the cycle.
- **Pareto frontier has reshuffled.** Anthropic + OpenAI now dominate; **Grok 4.3** is on the frontier; **Gemini 3.1** is "hanging on." Google **lost cost leadership** because of conservative TPU v8 design decisions. Anthropic's capital efficiency is ~5x OpenAI's (burned ~80% less for similar revenue scale).
- **AI shifted from all-you-can-eat to usage-based pricing.** $200–300/mo subs are getting "lobotomized" rate-limited Claude (Opus generating 70% fewer tokens per question). To see real frontier, you need an enterprise plan. This is **massively bullish for ARR** — same dynamic that ended cellular's growth era when it went to flat rate.
- **GPU useful lives extending to 10–15 years** via prefill/decode disaggregation. Cerebras / Groq LPUs handle prefill in front of Hopper/Ampere doing decode — **lowers AI buildout financing cost from ~7% to 5–6%** and "may single-handedly save private credit."
- **Orbital compute = "racks in space," not Pentagon-sized buildings.** SpaceX confidence on radiators + maintenance. Starlink V3 already operates at 20 kW per satellite; Blackwell rack is 100 kW. Will probably solve the watts shortage post-2028 if regulatory blowback constrains terrestrial DCs.
- **TerraFab** = SpaceX + Tesla JV with Intel partnership, aiming to build the world's largest fab in America. Bullish on its odds because (a) Elon recruits the best hardware engineers, (b) A-teams at ASML/KLA/LRCX/AMAT will rotate there for the same anti-monopsony reason they once helped TSMC catch up to Intel, (c) Intel partnership = access to 50 years of institutional knowledge.
- **Chip startup rule of thumb: 1% share = $100B outcome.** Must be "different AND hard." Cerebras is the exemplar of "wafer-scale = different + hard to copy." Don't try to build a better GPU; paint in the prefill canvas (memory capacity bound) or decode canvas (memory bandwidth bound).
- **Hyperscaler engagement-with-startups ranking:** Amazon + Nvidia >> Google > Broadcom >> ~0 from **AMD, Microsoft, Meta**. Baker thinks this gap matters in a world where best teams are no longer at big public companies.
- **Astera Labs miscategorized as a "copper loser"** — it's actually a switch company. Definitionally, a switch sits between accelerators and uses both copper and optics; can't be a "copper loser."
- **Satya is making the right courageous call** to use Microsoft's compute internally rather than reselling to OpenAI. *"Microsoft probably would be an $800 stock today if they were using their GPUs to serve OpenAI/Anthropic capacity instead of using them for their own products."*
- **Mythos 3/4 + the new prisoner's dilemma:** as Chinese open-weight models (with stolen American distillation traces) get good, frontier labs face a new game theory — do you release that next-gen model via API at all? If everyone agrees not to, Chinese open-source falls behind; if one defects, that lab pulls ahead irreversibly.

## Key claims (and confidence)

| Claim | Confidence | Notes |
|---|---|---|
| Anthropic added $11B ARR in a single month | **High** — Baker is very plugged in; consistent with Krishna Rao's $9B→$30B framing from [[2026-05-13-anthropic-cfo-podcast]] | Definitionally consistent: $30B − $9B = $21B Q1; mid-quarter pace ~$7B/mo and accelerating → $11B in March is plausible |
| TSMC discipline is the only bubble-prevention mechanism | **Medium-high** — strong directional claim but ignores demand-side discipline | A real and important framing: the cycle peak depends on whether Intel/Samsung break first on capacity |
| Google lost cost leadership due to TPU v8 conservative design | **Medium** — Baker's framing; aligns with what other sources have noted about TPU positioning but harder to verify directly | He's contrasting against TPU v7 which dominated Pareto frontier 9 months ago |
| GPU useful lives 10–15 years via prefill/decode disaggregation | **Medium** — directionally plausible, specific number is Baker's | If accurate, materially changes the AI-infrastructure-debt thesis — lowers financing cost ~150-200 bps |
| TerraFab will succeed because Elon recruits A-teams | **Medium** — speculative but reasonable | Long lead time; first chips likely 2028+ at earliest |
| Satya could've made MSFT an "$800 stock" | **Medium-low** — rhetorical / illustrative | The framing is interesting but the counterfactual is unverifiable |
| Anthropic could do $100–200B unconstrained ARR today | **Low-medium** — back-of-envelope from Baker | Useful for valuation framing only |
| Frontier tokens will continue commanding overwhelming majority of economic value at model layer | **Open question** — Baker explicitly flags as the key investor question | Watch for divergence: if not, app layer revalues |

## Pareto frontier composition (Baker's reading as of mid-May 2026)

Ranked by Baker's framing of intelligence-per-dollar:

1. **Anthropic** (Claude Opus 4.x) — dominant, plus best capital efficiency
2. **OpenAI** (GPT 5.x) — also on the frontier, less capital efficient
3. **Grok 4.3** (XAI) — clearly on the Pareto frontier as "best lowest-cost 500B-parameter model"
4. **Gemini 3.1 Pro** (Google) — *"hanging on to the Pareto frontier"*; Baker would bet they're subsidizing this out of pride
5. **Meta Muse** — first MSL model; not quite on frontier but close; *"big upside surprise"*
6. **Amazon Nova** — *"not where Muse is, but better than they get credit for"*

Key shift since the last Baker episode: **Google was at every point of the Pareto frontier 9 months ago**, with Anthropic/OpenAI/XAI strictly inside Google. That has fully reversed.

## Quotes worth keeping

> *"What was happening in AI was the most extraordinary moment in the history of capitalism. Anthropic added their combined businesses [Palantir + Snowflake + Databricks] in one month."*

> *"Microsoft probably would be an $800 stock today if they were using their GPUs to serve OpenAI and Anthropic's capacity instead of using them for their own products."*

> *"If Taiwan Semi did what Jensen wanted, Nvidia could sell $2 trillion of GPUs in '26 or '27, maybe $2.5 trillion, maybe $3 trillion."*

> *"Taiwan Semi, if we don't get a bubble, like we need to throw a party for them because they will have single-handedly prevented a bubble."*

> *"A violation of Richard Sutton's bitter lesson is for sure the biggest risk to this trade — to all of AI."*

> *"1% market share is going to be worth $100 billion. $100 billion is a pretty good venture outcome."*

> *"It's why I'm probably less worried about an edge-AI bear case than I was. We're going to consume as much compute as we can."*

> *"In a real bull market for a commodity, the commodity suppliers with the highest costs go up the most because it's the most beneficial to them. They go from on the verge of bankruptcy to gushing cash."*

> *"The Last Samurai... and at the end, he's massacred by a peasant with a machine gun. If we do not all become masters of the machine gun, we're going to get mastered."*

## Where Baker contradicts other wiki sources

- **vs LeCun ([[2026-05-16-yann-lecun-ame-labs]])** — Baker is much more confident in continued bitter-lesson scaling AND open to the possibility that ASI itself temporarily violates the bitter lesson by making itself more efficient. LeCun thinks LLMs are capped period.
- **vs Kedrosky / Zitron** — Baker rejects the "AI is a bubble" framing for now because (a) TSMC discipline holds, (b) capex is operating-cash-flow funded, (c) every GPU is at 100% utilization vs ~99% of fiber unutilized in 2000. He explicitly says he's worried about a "diversity breakdown" — i.e., he can't find anyone who's still meaningfully bearish on AI/DRAM, which itself is a late-cycle indicator.
- **vs Druckenmiller ([[2026-05-16-druckenmiller-hard-lessons]])** — Druckenmiller rotated AWAY from AI in mid-2025 on '99-rhyme valuations. Baker leaned IN during the March-April 2026 selloff. The two veteran investors are positioned opposite, which is itself informative.

## Wiki updates made

- **NEW**: `sources/2026-05-21-gavin-baker-invest-like-best.md` (this file)
- Updated `wiki/themes/ai-bubble-debate.md` — added Baker's TSMC-discipline-as-bubble-prevention framing, valuation cross-section paradox, low-quality-cyclicals dynamic, $11B/month ARR datapoint
- Updated `wiki/themes/ai-infrastructure-debt.md` — added GPU 10-15 year useful life thesis via prefill/decode disaggregation
- Updated `wiki/themes/space-economy.md` — added orbital compute "racks in space" reframing + TerraFab JV
- Updated `wiki/themes/bottleneck-roadmap.md` — added watts shortage 2027-28 alleviation timeline
- Updated `wiki/companies/ALAB.md` — added "miscategorized as copper loser" framing
- Updated `wiki/companies/MSFT.md` — added Satya $800-stock thesis
- Updated `wiki/companies/AMZN.md` — Trainium 3 scale-up network framing + robotics retail efficiency timeline
- Updated `wiki/companies/INTC.md` — TerraFab partnership angle
- Updated `wiki/companies/TSM.md` — Baker's cycle-peak framing (TSMC = bubble preventer)
- Updated `wiki/companies/NVDA.md` — Pareto frontier dominance + ~$2–3T unconstrained TAM datapoint
- Updated `index.md` + `log.md`
