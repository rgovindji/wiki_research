---
date: 2026-06-20
type: podcast
publisher: No Priors (Ep. 127) — Sarah Guo / Conviction
guest: Dylan Patel (founder / chief analyst, SemiAnalysis)
host: Sarah Guo
url: https://no-priors.com (Ep. 127)
raw_path: raw/podcasts/2026-06-20-nopriors-127-dylan-patel.txt
recording_estimate: ~mid-June 2026 (references OpenAI open-weight model "releasing this week," weights "accidentally leaked"; Cognition/Windsurf + KTO East-meets-West event recent)
touches:
  - inference-economics
  - ai-bubble-debate
  - ai-capex-cycle
  - bottleneck-roadmap
  - sovereign-ai
  - market-concentration
  - NVDA
  - AMD
  - AMZN
  - GOOGL
  - META
  - MSFT
  - ORCL
  - CRWV
  - NBIS
  - TSM
---

# Dylan Patel × No Priors (Ep. 127) — Open-Weight Models, the Anti-Nvidia Dragon & Neocloud Consolidation

## TL;DR
- **OpenAI's open-weight model "kneecaps" reasoning-model API margins.** First time the US has the best open-weight model since Llama 3.1 405B (Chinese labs — DeepSeek/Kimi/Qwen — held it ~6-12mo). Crucially it's **small enough to self-host** (vs Kimi "too big to run") AND OpenAI is shipping **optimized inference kernels + partner stacks day one** → commoditizes the closed-API non-frontier market faster. *Directly tensions the `[[inference-economics]]` open-weight-moat debate.*
- **THE KEY DATA POINT for `[[inference-economics]]`:** SemiAnalysis token-tracking shows **people aren't actually using reasoning/thinking models much in API.** Anthropic has eclipsed OpenAI in API revenue, and Anthropic's API revenue is **primarily NON-thinking (Claude in non-reasoning mode), with code the biggest, fastest-growing use case.** Reasoning is gated by **cost and latency**, not capability. Implication: a cheap small open-weight reasoner unlocks Jevons-paradox reasoning demand AND cuts margin out of the reasoning-API layer.
- **Why nothing dethrones Nvidia — the "three-headed dragon"** (hardware engineering + networking + 20yr software ecosystem). Best *realistic* second choices: **AMD GPUs or Amazon Trainium** (Google TPU great but internal-focused). **Architecture-specialization bets lose** because models evolve unpredictably (MoE/sparsity killed the big-systolic-array + big-on-chip-memory bets of Cerebras/Groq/SambaNova/Graphcore) while Nvidia's generality lets it "take steps toward" any workload and win on supply chain + cadence.
- **Neocloud reckoning: ~200 exist, most shouldn't.** Three survival paths: (1) go huge (Crusoe gigawatt DCs), (2) move up into the software/inference layer (Together, Nebius, CoreWeave rumored buying Fireworks), or (3) accept commercial-real-estate-style 10-15% ROE — which **fails VC-backed neoclouds** → consolidation + bankruptcies coming. CRE debt/equity now flowing into the space (chasing yield); short-lived asset vs CRE's long-lived = return-profile mismatch.
- **AMZN Trainium miss = rack-integration (supply chain), not silicon.** Amazon blamed its AWS revenue miss on Trainium "rack integration yield issues" — architecture is "what Google did 4-5 years ago," not aggressive. Hardware time-scales are long and unforgiving; "the whole stock market freaked out" over a few-percent AWS miss.
- **Power = multi-bottleneck, not one thing.** CoWoS + HBM + optical transceivers *still* bottlenecks AND now substations/transformers + gas turbines (4-8yr GE backlog) + grid + **labor/electricians** (wages soaring; Meta building tent structures; imported labor). Echoes but extends the "power is solvable" framing — solvable only by hyper-competent orgs willing to go non-standard.

## Key facts & quantitative claims (with confidence)

| Claim | Value | Confidence |
|---|---|---|
| Last time US had best open-weight model | Llama 3.1 405B (~6-12mo ago); Chinese labs since | High |
| OpenAI open-weight model | small enough to self-host; ships w/ optimized kernels + partners day 1; "boring"/standard architecture intentionally | Medium-High |
| Anthropic vs OpenAI API revenue | **Anthropic has eclipsed OpenAI in API revenue** | Medium-High (SemiAnalysis alt-data) |
| Anthropic API revenue mix | **primarily NON-thinking; code = biggest, fastest-growing** | Medium-High |
| Reasoning-model API adoption | low — gated by cost + latency, not capability | Medium-High (alt-data) |
| Historical reasoning-token pricing | o1/o3 priced ~4x GPT-4o per token "even though architecture basically same — pure margin" until recently cut | Medium |
| DeepSeek inference replica | ~160 GPUs (~$10M+ hardware) per replica + shared caching servers | Medium |
| # of neoclouds | ~200, "find a new one every day" | High |
| Neocloud CRE-style ROE | 10-15% (kills VC-backed ones) | Medium-High |
| Lambda on-demand GPUs | ~4,000 of 50,000+ are on-demand, always sold out | Medium |
| GE turbine backlog | 4-8 years | High (corroborates prior sources) |
| Best realistic Nvidia alternatives | AMD GPU, Amazon Trainium (Dylan's pick) | Medium (his opinion) |

## Why this is NEW vs. already-ingested Dylan content
- Prior Dylan sources covered supply-chain bottlenecks, GPU 7-8yr life, DRAM 2-3x, Anthropic margins, TSMC $100B.
- **NEW here:** (1) the **reasoning-models-barely-used-in-API** alt-data finding (cost/latency-gated, not capability) — a sharp, fresh `[[inference-economics]]` input; (2) **OpenAI open-weight model + day-1 kernels** as a margin-kneecapping event tensioning the open-weight-moat debate; (3) the **full "three-headed dragon / why specialization loses" anti-Nvidia teardown** (Cerebras/Groq/SambaNova/Graphcore memory-vs-compute bet failed on MoE sparsity); (4) **neocloud consolidation taxonomy** (3 survival paths, CRE money inflow, CoreWeave-buying-Fireworks rumor); (5) **Trainium miss = rack integration not silicon**; (6) sovereign/geopolitics value-stack framing (sell services > tokens > infra > GPUs; don't sell the chip-making tools).

## Key claims & how confident
- **Medium-High (SemiAnalysis alt-data):** reasoning models barely used in API; Anthropic > OpenAI in API revenue, non-thinking/code-dominated. *This is the single most decision-relevant new claim.*
- **Medium-High (analyst opinion, well-reasoned):** open-weight + day-1 kernels accelerates closed-API commoditization; neocloud consolidation; AMD/Trainium as best Nvidia alternatives.
- **Medium (Dylan's read / hand-wave):** Trainium miss = rack integration; China can rationally subsidize 3x-power chips if it has 4x power.
- **Bull AND bear surfaced:** Sarah Guo pushes back that infrastructure/system-software (orchestration, caching across turns/tool-use, distributed-systems abstractions) is NOT commoditized and is the durable neocloud moat — Dylan partially concedes. Both views captured below.

## Quotes worth keeping

> "It's the first time America's had the best open-source model in six months, nine months, a year... Llama 3.1 405B was the last time." — Dylan

> "It's very clear that people aren't actually using the reasoning models that much in API. Anthropic has eclipsed OpenAI in API revenue, and their API revenue is primarily not thinking — it's Claude, but not in thinking mode, with code being the biggest use case that's skyrocketing." — Dylan (the key `[[inference-economics]]` data point)

> "[The OpenAI open-weight model] is going to just like kneecap, cut everyone off at the hip, and bring margins down again." (on non-frontier API margins) — Dylan

> "It's a three-headed dragon: they're really good at engineering GPUs, really good at networking, and everyone else is just terrible at software... Nvidia can take steps toward what you're going for, and if you didn't execute perfectly or the models changed architecture, you fail." — Dylan, on why Nvidia is hard to beat

> "All of the first-wave AI hardware companies [Cerebras, Groq, SambaNova, Graphcore] made the same bet on memory vs compute — more on-chip memory, lower off-chip bandwidth. Then the models just got way too big... and then went super sparse [MoE]. No one predicted the hardware would go that way." — Dylan

> "There's sort of a rock and a hard place for ~100 of these neoclouds... you either go really really big, or move into the software layer, or you make commercial-real-estate returns, or you go bankrupt." — Dylan

> "[Amazon] blamed their AWS miss on Trainium not coming online fast enough because of rack-integration issues... it's like what Google was doing four or five years ago. Supply chain is hard." — Dylan

> "I'd say AMD GPUs or Amazon's Trainium will probably be the best second choice... more likely to succeed than a chip hardware startup." — Dylan (explicitly "not investment advice")

> "Even if their [China's] chips cost 3x as much, they can subsidize that rationally — they did it with solar and EVs." — Dylan

## Connect-the-dots / investment implications

1. **`[[inference-economics]]` — reasoning is cost/latency-gated, not capability-gated.** The wiki's open-weight-moat debate (Dwarkesh: perishable ~4mo lag; Katti: 6-month lead is enormous) gets a third axis: *the high-margin reasoning tier is barely monetized in API today.* A cheap, self-hostable open-weight reasoner (OpenAI's) could simultaneously (a) **expand** reasoning-token demand (Jevons) — bullish total compute/[[NVDA]] — and (b) **compress** closed-lab reasoning-API margins — bearish pure-API lab revenue quality. **This sharpens the existing "LLM layer commoditizes while hardware/apps capture value" thesis with a concrete margin event.**
2. **NVDA moat re-underwritten at the architecture level.** "Three-headed dragon" + "specialization loses to generality because models evolve unpredictably" is the cleanest first-principles defense of the [[NVDA]] moat on the wiki. Bullish/structural. Best *threats* = **[[AMD]]** (GPU) and **[[AMZN]]** Trainium — but Dylan caveats AMD's software/networking/codesign gaps and Amazon's supply-chain execution (Trainium rack-integration miss). Custom-silicon bear-on-NVDA case is weaker than headlines imply.
3. **Neocloud consolidation = stock-specific dispersion.** [[CRWV]] positioned to survive (sold-out long contracts, rumored buying Fireworks to move up-stack), [[NBIS]] offering inference services (up-stack move). The ~100 sub-scale VC-backed neoclouds face bankruptcy/consolidation → counterparty/oversupply risk for the cheap-GPU-rental trade. CRE money inflow chasing 10-15% ROE = ceiling on neocloud equity returns over time. Double-edged for [[CRWV]]/[[NBIS]] (same "route-to-cheapest" pressure on their own pricing).
4. **Hyperscaler GPU margins ≠ CPU margins.** Dylan: AWS/GCP charge "absurd margins" on CPU/storage out of habit; assuming that translates to GPU is "a fallacy" → why neoclouds + custom silicon are eating in. Read-through: hyperscaler ([[AMZN]], [[GOOGL]], [[MSFT]]) cloud-segment GPU economics may be structurally lower-margin than legacy compute. Watch margin commentary.
5. **AMZN Trainium = supply-chain risk, not silicon risk.** The AWS miss was rack integration, a fixable execution issue — neither a Trainium death-knell nor a clean bull signal. Calibrates the [[AMZN]] custom-silicon thesis: the chip is fine; the systems/rack supply chain is the gating item.
6. **Power = confirmed multi-bottleneck + labor.** GE turbine 4-8yr backlog (corroborates [[bottleneck-roadmap]]); CoWoS/HBM/optical *still* binding; NEW emphasis on **electrician/labor shortage** (wages soaring; Meta tents; imported labor) as a real constraint — read-through to datacenter-construction / electrical-contractor names ([[IESC]], [[PWR]], [[STRL]], [[FIX]], [[EME]]).
7. **Sovereign-AI value-stack logic ([[sovereign-ai]]):** US policy goal = capture highest-margin layer (services > tokens > infra > GPUs), don't export chip-making tools. Most Middle East GPUs operated/rented by US firms (OpenAI, Amazon, Oracle, G42). Bullish framing for [[ORCL]]/[[CRWV]]/hyperscaler sovereign deployments. China can rationally subsidize 3x-power chips (solar/EV playbook) → long-timeline competitive risk (consistent with prior "long timelines China wins").

## Contradictions / tensions to surface (do NOT resolve)
- **Open-weight moat (vs `[[inference-economics]]`):** existing page frames open-weight as *good-enough for 80-90% routed tasks while frontier keeps the 10-20%.* Dylan adds a twist that *tensions both sides*: the high-value reasoning tier is **barely used in API today** (cost/latency), so a cheap open-weight reasoner could shift the mix faster than the "frontier keeps the premium" reconciliation assumes. Surface alongside Dwarkesh (perishable) and Katti (6-mo lead is huge) — Dylan is closer to Dwarkesh's "moat is thin" camp on the *non-frontier API margin*, but agnostic on frontier capability lead.
- **"Power is solvable" (vs 2026-05-09 Dwarkesh):** prior Dylan said "scaling power in the US will not be a problem" (16+ gas vendors, behind-the-meter). Here he's more bottleneck-heavy (GE 4-8yr backlog, grid delays in Ohio, permits/protests, labor). Not a true contradiction — both say *solvable by competent orgs* — but the tone is notably more constraint-aware. Surface as nuance.

## Bias / usage notes
- Sarah Guo (Conviction) is a VC investing at the application/neocloud/infra layer — some questions are book-adjacent (cognition, neocloud software moat); her pushback on "infrastructure isn't commoditized" is a genuine analytical counter, captured above.
- Dylan repeatedly says "not investment advice" / declines to name companies he's invested in (AMD/Trainium pick, the datacenter-automation angel investment) — note the conflict disclosure; weight accordingly.
- The Cognition/poker and Lebanon/geopolitics segments are color, not investable signal (Cognition = private; included only as sentiment).
- **No price targets given. None to cite.**

## Wiki updates suggested (orchestrator to action — NOT done here)
- **[[inference-economics]]** — ADD: reasoning models barely used in API (cost/latency-gated); Anthropic > OpenAI in API rev, non-thinking/code-dominated; OpenAI open-weight + day-1 kernels = margin-kneecap event. Slot into the open-weight-moat debate table as a third data point.
- **[[NVDA]]** — ADD: "three-headed dragon" moat framing; why specialization loses (MoE/sparsity killed Cerebras/Groq/SambaNova/Graphcore memory bets); best alternatives = AMD/Trainium per Dylan.
- **[[AMD]]** — best realistic GPU alternative per Dylan, but software/networking/codesign gaps named.
- **[[AMZN]]** — Trainium miss = rack-integration supply-chain, not silicon; OpenAI/Amazon CPU deal; hyperscaler-GPU-margin-fallacy.
- **[[CRWV]] / [[NBIS]]** — neocloud consolidation taxonomy; CRWV rumored buying Fireworks (move up-stack); CRE money inflow / 10-15% ROE ceiling; survival paths.
- **[[bottleneck-roadmap]]** — multi-bottleneck confirmation (CoWoS/HBM/optical still binding) + NEW labor/electrician constraint; GE turbine 4-8yr backlog.
- **[[sovereign-ai]]** — value-stack framing (services>tokens>infra>GPUs); US-operated Middle East GPUs; China rational-subsidy / long-timeline risk.
- **[[ai-bubble-debate]] / [[ai-capex-cycle]]** — AI buildout as the marginal driver of US GDP growth (Noah Smith framing); labor/wage second-order effects.
- Datacenter-electrical read-through: **[[IESC]], [[PWR]], [[STRL]], [[FIX]], [[EME]]** (electrician-labor scarcity).
