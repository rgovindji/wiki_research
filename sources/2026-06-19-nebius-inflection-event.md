---
date: 2026-06-19
type: podcast
publisher: Nebius ("Inflection" customer event, San Francisco)
url: https://www.nebius.com/ (event keynote + customer/agentic panels)
raw_path: n/a (transcript pasted in-session; no local raw saved — promotional keynote)
touches: [inference-economics, ai-capex-cycle, NBIS]
---

# Nebius "Inflection" event — keynote + customer panels

> **Bias flag:** This is Nebius's *own* hosted event. The keynote (CRO Borditzki, co-founder Chernin, CEO Volozh, recorded Jensen plug) is ~80% marketing — discount it. The **customer/agentic panels** (Databricks, Cognition/Devin, DataRobot; LangChain, Pinecone, Tavily, Guardrails) carry the durable signal.

## TL;DR
- **CIO cost backlash is now a named, multi-company narrative** — AI line items going from $30/user SaaS to *millions*; "relitigating the ROI"; explicitly compared to early-AWS sticker shock.
- **Model routing is standard practice** — frontier for the hard 10-20%, open-weight for the 80-90% ("10× cheaper/faster"); a live agent demo quantified one run at **$657 → $34 → $24** at near-equal accuracy.
- **NBIS is a real, fast-growing neocloud but a balanced bet, not asymmetric** — see snapshot below; the keynote framing should not set the tone.

## Key facts / claims (with confidence)
- **NBIS (independently researched, ~2026-06-18):** price ~$287, mkt cap ~$73B, ~256M shares, near 52-wk highs. Q1'26 rev $399M (+684% YoY); core AI-cloud ARR $1.92B (+54% QoQ); first-ever positive adj. EBITDA (+$130M); FY26 guide $3.0-3.4B rev / $7-9B ARR run-rate. **Earnings-quality caveat:** the headline Q1 net income (~$621M, ~99 P/E) is mostly a **non-cash ClickHouse revaluation gain** — strip it and core ops lost **~$100M**. Valuation ~62-83x sales / ~38x current ARR. **Consensus 12-mo target (~$242) sits *below* the price.** *Secondary-aggregator data (stockanalysis.com, press, SEC 6-K mirrors); verify exact EV/ARR vs the 6-K before publishing precise multiples.*
- **Financing fragility:** FY26 capex $20-25B vs ~$3.2B revenue; ~40% funded by equity + serial converts ($4.3B converts + $2B NVIDIA in 2026). Backlog ~$46B but concentrated in **Microsoft (~$19B) + Meta (~$27B)**, and Meta's piece is a *backstop* (buys excess capacity), not committed dedicated demand. Yandex lineage / governance overhang.
- **Vs CoreWeave:** CRWV ~10× the revenue, ~98% contracted, but trades ~7× sales vs NBIS ~62×. Analyst community split (CRWV on valuation, NBIS on growth + *owned* power + ClickHouse optionality). *Surface, don't resolve.*

## Panels — the durable signal
- **Cost backlash / "value-maxing not token-maxing"** (Databricks, DataRobot, Cognition). AI gateways + model routing + measuring outcomes, not tokens.
- **Open-weight closing the gap + model routing** — hard cost numbers (the $657→$24 demo); open-weight worked out-of-box, no fine-tuning.
- **"Agent as a user"** — a new infra persona needing API-first, programmable, observable, low-latency interfaces; the *harness* (orchestration/retrieval/observability/grounding/guardrails) matters as much as the model.
- **GPU crunch corroborated from the demand side** (Cognition literally asking Nebius to reserve GPUs); Jevons paradox visible in coding agents.

## Quotes worth keeping
> "Think value-maxing instead of token-maxing." (Chernin)
> "Production-ready is not the same as running and improving 100s of agents in production." (Nebius agentic panel)

## Wiki updates made
- Seeded [[inference-economics]] (cost backlash, model routing, agent-as-a-user, the harness layer) — one of its 3 founding sources.
- (Recommended, not yet created: a lean [[NBIS]] company page — neutral/medium, ClickHouse earnings-quality caveat front and center, CoreWeave valuation split as a Contradicting-evidence block. Awaiting user go-ahead.)
