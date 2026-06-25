---
type: theme
tags: [ai, software, saas, agents, disruption, saaspocalypse]
last_updated: 2026-06-25
last_full_review: 2026-06-22
sources: 7
---

# AI Software Disruption ("AI eats SaaS")

## What this is
The live thesis that LLM **agents disrupt the per-seat SaaS business model** — "agents are the new seats." When an AI agent does the work a human seat used to, seat-based software revenue is structurally exposed: fewer seats, and the value migrates to whoever owns the agent/model. Distinct from [[inference-economics]] (the unit economics of serving AI) — this page is about *which application-layer incumbents get eaten vs. which survive*.

## Why it matters now (2026)
- **The "SaaSpocalypse" (2026-06).** Per [[2026-06-20-dario-anthropic-965b]], Anthropic's own product launch (Claude Code / Cowork) is credited with a **~$285B single-event wipeout of software-stock market cap**. Software de-rated *on good news* through June (Adobe −6% on a beat; Salesforce at 52-week lows; CRM/NOW/VEEV/DUOL all near 52-wk lows).
- **Confirmed seat erosion.** [[CRM]]'s own service customers reportedly show **~10% seat reduction** from AI — the agent-eats-seats mechanism is no longer theoretical.
- **Pricing-power inversion.** Per [[2026-06-20-t6-simon-willison-coding]]: peers now ship 70-80% agent-written code; the SaaS *pricing honeymoon is ending* while the labs raise prices (Opus 4.7 ~+40% effective, GPT-5.5 2× GPT-5.4) — value accruing to the model layer, not the app.
- **Investor framing.** Philippe Laffont ([[2026-06-20-laffont-coatue-bubble]]): "models are digital 3D printers — bad for software." Software trades ~5.2x fwd rev vs a ~7x 10-yr average; the de-rate is multiple compression on *fear*, largely ahead of revenue evidence.
- **2026-06-25 — The incumbent counter-narrative: "data is the moat, models commoditize."** Per [[2026-06-25-latentspace-zaharia-databricks-agent-cloud]] (Databricks CTO Matei Zaharia — promotional, private co. selling exactly this), frontier models are "now pretty good," so the moat shifts to **getting the right data in place, then "slap an agent on top"** — and "many traditional software will be rewritten" on that paradigm. The bullish read for a *data-platform* incumbent (Databricks vs [[CRM]]/per-seat SaaS): if data + governance + the agent harness is where value accrues, the platforms that own the data layer survive the seat-erosion they sell against. **Which means:** a self-serving but coherent map of *who survives* "AI eats SaaS" — the data/governance layer, not the application seat. Treat as talk-their-book.

## The key reconciliation: it's a *growth* re-rate, not a *replacement* story (2026-06-23)
The most useful framing of *why* quality SaaS keeps bleeding even though it won't be ripped out — the bear isn't "AI replaces Salesforce," it's **"AI flattens *seat growth*, so the multiple collapses from a compounder (~30x) to an entrenched utility (~12x)."** Lock-in is real (an F500 took ~18 months to leave CRM); but if agents stop *new seat* growth, the business becomes GDP+low-single-digits and **loses the premium multiple regardless of how sticky it is.** That single fact reconciles everything that looks "irrational": *entrenched + cheap + still falling daily* all coexist because the market is re-rating *terminal value*, which ignores near-term NRR.
- **CRM datapoint (2026-06-23):** −30% in 14 straight red days to **~10.5x forward** (lowest since Jan-2023), with NRR still >110% and double-digit organic growth — i.e. the market is pricing *utility-or-worse* on a business whose current numbers don't show decline. **At 10.5x it's a clean "utility-not-death" bet:** cheap if you accept "entrenched low-growth utility," a value trap if agentic disruption is genuinely terminal. The swing factor is whether **consumption revenue (Agentforce) out-grows seat erosion** — the one print that flips the narrative.
- **Sentiment marker:** retail capitulation is loud (viral r/StockMarket "software massacre… detached from fundamentals" posts; "I've deployed all my cash averaging down" — the classic out-of-ammo-at-the-bottom mistake). Capitulation + a factor-driven de-rate (quality and garbage sold identically) is *typically* late in a move, not early.
- **The mechanical reversal trigger:** this is largely a **liquidity rotation** (sell software/value to fund the semi/memory melt-up). So paradoxically, **the catalyst that revives software is the *semis/memory trade cracking*** — when that liquidity rotates back. Near-term tell: the MU print. Plus re-discrimination (the market stops treating all SaaS as one trade) and forced-selling exhaustion.

## The survival spectrum (most → least resilient)
From the cluster-D research ([[2026-06-20]] sweep). The question for each name: **does AI eat it, or feed it?**

| Name | Verdict | Why |
|---|---|---|
| [[VEEV]] | **Most resilient** | Regulated, validated, vertical life-sciences workflows + proprietary data = the hardest profile for a horizontal agent to replicate. Cheapest multiple too. |
| [[NOW]] | **Credible #2** | "System of action" — *monetizes* agents (the distribution layer) rather than being replaced; but full seat-model exposure + unproven agentic-ARR ramp. |
| [[DDOG]] | **Tailwind, not target** | Usage-based (telemetry), not per-seat → more agents = more to monitor. (Cut from the core book on *factor/sentiment* risk, not thesis — see [[ai-bubble-debate]].) |
| [[CRM]] | **Target** | The defining agent-eats-seats case; ~10% seat erosion in its own data. Cheap (fwd P/E ~11) for the most fundamental reason. |
| [[DUOL]] | **Most exposed** | "The model *is* the product" — free LLM tutoring substitutes the core; highest multiple, decelerating DAU. |

**The fault line:** *usage-based / vertical / regulated / proprietary-data* software survives (even benefits); *horizontal / per-seat / generic-workflow* software is the target.

## Who captures the value instead
- **The model labs / agent layer** — OpenAI, Anthropic (the disruptors; see [[ai-capex-cycle]] demand-pull).
- **The harness/infra layer** — orchestration, observability, retrieval (sticky; see [[inference-economics]]).
- **The app-layer winners moving *down* the stack into their own models** — datapoint (2026-06-24): Cursor's Sasha Rush detailing how **Composer 2.5** was trained with novel RL methods ([[2026-06-24-dwarkesh-sasha-rush-on-policy-distillation]]) confirms the strongest coding-agent player is building a *vertical in-house frontier model*, not wrapping someone else's. **Which means** the durable margin at the app layer may accrue to those who own both the workflow *and* the model — a moat the pure-seat incumbents (CRM) don't have and the pure-wrappers can't defend.
- **NOT** the per-seat incumbents, unless they convert to consumption pricing faster than seats erode.

## Risks / counter-thesis
- **Mostly multiple compression, not revenue collapse — yet.** The de-rate is running ahead of hard revenue evidence; a single strong software AI-revenue print (e.g. Agentforce consumption out-growing seat erosion) could snap the rotation back hard.
- **Incumbents have distribution + data moats.** Salesforce/ServiceNow sit on workflow data + enterprise relationships agents can't trivially replace; "agents are the new seats" assumes a clean substitution that enterprise procurement may resist.
- **Survivors are cheap.** VEEV/NOW at compressed multiples with intact moats could be the contrarian longs if the fear overshoots.

## Open questions
- Does any incumbent prove *consumption revenue out-grows seat erosion* (the bull trigger)? Watch CRM Agentforce, NOW agentic ARR.
- Is the de-rate a generational re-rating of software multiples, or an overshoot to fade?
- Where does the harness/agent margin ultimately sit — labs, clouds, or a new app layer?

## Related
[[inference-economics]] · [[ai-bubble-debate]] · [[ai-capex-cycle]] · [[CRM]] · [[NOW]] · [[VEEV]] · [[DUOL]] · [[DDOG]] · [[valuation-environment]] · [[overview]]

## Sources
1. [[2026-06-20-dario-anthropic-965b]] — Anthropic products + the ~$285B "SaaSpocalypse" wipeout (lab-CEO bias)
2. [[2026-06-20-t6-simon-willison-coding]] — 70-80% agent-written code; SaaS pricing honeymoon ending
3. [[2026-06-20-laffont-coatue-bubble]] — "models are digital 3D printers — bad for software"
4. [[2026-06-20-nopriors-127-dylan-patel]] — code is the biggest/fastest-growing API use case
5. Cluster-D company research (2026-06-20): [[CRM]] / [[NOW]] / [[VEEV]] / [[DUOL]] survival spectrum
6. [[2026-06-24-dwarkesh-sasha-rush-on-policy-distillation]] — Cursor Composer 2.5 trained in-house with off-policy self-distillation; app-layer leaders building vertical models (added 2026-06-24)
