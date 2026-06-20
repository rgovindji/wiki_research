---
date: 2026-06-20
type: podcast
publisher: Daytona Compute Conference ("The Datacenter in 2026: CPUs, RL Environments & Agent-Driven Workloads")
guest: Dylan Patel (founder / chief analyst, SemiAnalysis)
host: Daytona (Ivan / team) — sandbox-infra company
url: (unknown — Daytona Compute Conference recording)
raw_path: raw/podcasts/2026-06-20-dylan-patel-datacenter-2026-cpus-rl.txt
recording_estimate: ~late May 2026 (Dylan: "Nvidia is launching Rubin next week" → Rubin samples shipped 2026-05-20, Computex 2026-06-01; this likely recorded ~end of May 2026)
touches:
  - bottleneck-roadmap
  - ai-capex-cycle
  - inference-economics
  - INTC
  - AMD
  - NVDA
  - ARM
  - AMZN
  - TSM
  - AAPL
  - MEDIATEK
  - CBRS
  - MU
  - SNDK
  - WDC
  - GOOGL
  - MSFT
---

# Dylan Patel × Daytona — CPUs Are the New Bottleneck (RL Environments & Agentic Inference)

## TL;DR
- **NEW BOTTLENECK: CPUs.** After GPUs (2023-24) and DRAM/HBM (2025-26), the *third* binding constraint of the agentic era is **server CPUs (vCPUs)**. "Over the last 6 months we've seen the entire cloud market run out of CPUs." Driven by (1) RL-environment verifier loops getting tighter and (2) long-horizon agents (Codex working 6-7hr) hammering CPU for tool calls, sandboxes, scraping, DB calls. This is genuinely new vs. prior Dylan content (Dwarkesh/ILTB focused on GPU/memory/EUV).
- **Intel + AMD both "fully sold out," have sent price-increase notices, "not even competing with each other anymore."** Server-CPU margins, historically thin, are now "creeping up." Amazon installing **3x YoY** CPU servers.
- **The GPU↔CPU ratio is collapsing.** Used to be ~100 MW of GPUs served by ≤1 MW of CPUs; now "much, much closer" for both RL training and agentic inference. "Warm-pool" CPUs kept hot so $-expensive GPUs never sit idle waiting on a verifier = structurally more CPU per GPU.
- **CPU silicon is fragmenting** (the "gold rush → even broken pickaxes sell" dynamic): Intel/AMD x86, Amazon Graviton (5-6 gens), **Nvidia Vera** (Grace successor — deploying late-2026/early-2027; standalone Grace never sold in volume), Microsoft + Google in-house CPUs ramping, and **ARM launching its own standalone CPU "in a few weeks" that Meta + Cloudflare will adopt** (ARM moving from IP-licensing to selling silicon directly).
- **AI is squeezing everyone off leading-edge nodes.** TSMC is telling **Apple, Qualcomm, MediaTek to "get off 3nm, move to 2nm faster"** because all AI accelerators (MI350, Trainium3, TPUv7, Rubin) are on N3. This pushes mobile/PC vendors toward **Intel** as a non-AI-competing foundry alternative. **Nvidia's Groq acquisition = partly because Groq is on Samsung** (no TSMC N3 capacity available). "Just make any decent chip and it'll sell."
- **Memory cross-read corroborated + extended:** DRAM "4x in price over the last year and going to keep going up"; **SSD/NAND also up 3-4x, "another ~60% to go" (less than DRAM but a lot)**. RAM and storage are "very fungible" between PCs and datacenters → consumer PC/Mac/laptop prices spiking (Apple "sold out of Mac minis").

## Key facts & quantitative claims (with confidence)

| Claim | Value | Confidence |
|---|---|---|
| Entire cloud market "ran out of CPUs" over last 6 months | qualitative | High (Dylan's own infra tracking) |
| Amazon CPU-server installs | **3x YoY** (this year vs last) | High |
| Code-agent revenue | "a couple billion → north of **$10B**" in a very short time | Medium-High (consistent w/ his ILTB $-figures) |
| Codex agent run length | **6-7 hours** continuous | High |
| Old GPU:CPU power ratio | ~100 MW GPU : ≤1 MW CPU | Medium (illustrative) |
| New GPU:CPU ratio | "much much closer" | Medium |
| DRAM price | **+4x last year, still rising** | High (matches MU/Micron supercycle thesis) |
| SSD / NAND price | **+3-4x, another ~60% to come** | Medium-High |
| Intel + AMD server CPUs | both "fully sold out," price-increase notices issued | High |
| ARM standalone CPU launch | "in a few weeks," **Meta + Cloudflare** adopting | Medium-High |
| Nvidia Vera CPU deploy timing | late-2026 / early-2027 | High (matches NVDA Q1 FY27 "Q3 2026 production") |
| TSMC pushing Apple/Qualcomm/MediaTek off N3 → N2 | qualitative | Medium-High |
| Single Daytona customer ran **1M vCPU workloads in 6 hours** | 1 customer, 1 day | High (host's own data) |
| GitHub instability attributed to MSFT selling spare CPUs to OpenAI/Anthropic | qualitative | Medium (Dylan's inference) |

## Why this is NEW vs. already-ingested Dylan content
- Prior Dylan sources (`2026-05-09-dwarkesh`, `2026-05-16-invest-like-best`): bottleneck stack = **memory now → cleanroom → EUV/ASML by 2028-30**, plus GPU 7-8yr life, DRAM 2-3x, TSMC $100B 2028 capex, copper foil sold out.
- **This adds a NEW near-term layer to `[[bottleneck-roadmap]]`: server CPUs (2026), driven by RL-environment verifier loops + long-horizon agents.** Not in any prior source. Plus a *named, dated* ARM standalone-CPU launch (Meta + Cloudflare) and the Groq/Samsung rationale for Nvidia's acquisition.

## Key claims & how confident

- **High (own infra data):** CPU shortage is real and acute; Amazon +3x YoY; Intel/AMD sold out w/ price hikes; warm-pool dynamic.
- **High (corroborates prior sources):** DRAM +4x and rising; NAND/SSD +3-4x; AI eating N3/N2 capacity; Vera CPU timing.
- **Medium (Dylan opinion / inference):** GitHub instability ← MSFT CPU reallocation; ARM-standalone adoption list; Groq-on-Samsung as Nvidia acquisition rationale.
- **Bear-side honesty:** Dylan explicitly tempers the **Intel** bull read — "they'll do better but it's not like the company's saved... others (AMD, Amazon) will catch up on capacity." CPU-shortage tailwind to INTC is real but **short-term / cyclical**, not a structural turnaround. The durable INTC angle is foundry-of-last-resort for vendors kicked off TSMC N3.

## Quotes worth keeping

> "Over the last 6 months we've seen the entire cloud market run out of CPUs." — Dylan

> "Microsoft sold all their CPUs that they had spare to other people... they signed deals with Anthropic and OpenAI and so they just have like no CPUs left." (on GitHub instability) — Dylan

> "[Intel and AMD] have said they're fully sold out. They've sent price-increase notices to their customers. They're not even competing with each other anymore. They're just like 'how many can I make and sell?'" — Dylan

> "ARM is going to launch a CPU in like a few weeks that Meta is going to adopt and a few others... like Cloudflare. So there's going to be a lot more proliferation — ARM standalone rather than ARM licensing the IP." — Dylan

> "All the AI chips are on 3 nanometer now... they're telling Apple to get off, telling Qualcomm and MediaTek to get off, and all three are like 'maybe we should use Intel because they can't manufacture AI chips.'" — Dylan

> "People make up all these nonsense reasons why Nvidia acquired Groq... part of it is that Groq is manufactured on Samsung. Because there's no 3-nanometer capacity for them at TSMC." — Dylan

> "RAM and storage are very fungible [between PCs and data centers]... you have to buy a Mac mini now otherwise you'll never escape the permanent underclass." — Dylan (echoing his recurring tagline)

## Connect-the-dots / investment implications

1. **CPU shortage is a NEW investable bottleneck layer.** Beneficiaries: **[[AMD]]** (EPYC sold out, pricing power, server share gains), **[[INTC]]** (Xeon sold out + foundry-of-last-resort for kicked-off-N3 mobile/PC vendors — but Dylan caps the bull: short-term not structural), **[[ARM]]** (standalone-CPU launch + Meta/Cloudflare design wins = business-model shift from royalties to silicon), **[[AMZN]]** (Graviton +3x install, ARM port of OpenAI stack), **[[NVDA]]** (Vera CPU $200B TAM now demand-confirmed). Catalyst to watch: **ARM standalone-CPU launch (~early-mid June 2026 per "few weeks") + Meta/Cloudflare confirmation.**
2. **Reinforces the memory supercycle ([[MU]], [[SNDK]], [[WDC]]).** DRAM +4x/yr and *NAND/SSD now +3-4x with ~60% more to come* — NAND inflation is sharper here than in the 2026-05-09 Dwarkesh read (which had NAND rising *less* than DRAM). Surface as an **update, not contradiction**: NAND lagged DRAM but is now catching up. Bullish [[SNDK]]/[[WDC]] near-term.
3. **TSMC node-allocation squeeze ([[TSM]], [[AAPL]], [[MEDIATEK]], [[CBRS]]):** AI accelerators monopolize N3 → Apple/Qualcomm/MediaTek pushed to N2 faster or toward Intel. Reinforces the **AAPL-structurally-deprioritized** thesis already flagged in `2026-05-09-dwarkesh`. Possible Intel design-win optionality for mobile/PC SoCs.
4. **Agentic-inference = CPU-heavy, not just GPU-heavy.** The unit-economics of agents now include a meaningful vCPU line (sandboxes, verifiers, warm pools). Read-through to `[[inference-economics]]`: cost-per-agent-task has a rising CPU component; warm-pool CPUs deliberately burn money to avoid idle-GPU cost. Private/under-radar: **Daytona** (sandbox infra), managed-Ray / RL-environment providers.
5. **RL-environment compute is exploding** (1M vCPU/6hr from a single small-cloud customer; physics/biology-sim verifiers ahead). Validates the RL-environment / data-labeling decabillion theme tracked in `[[inference-economics]]` and `2026-06-20-dwarkesh-sample-efficiency`. Robotics world-model verifiers ("tensile strength of a shoelace" checked against a physics sim on CPU) = next CPU-demand step-function.

## Bias / usage notes
- Dylan is generally high-credibility on supply chain; SemiAnalysis tracks CPU/cloud capacity directly (own data) so the shortage claim is well-grounded.
- **Host (Daytona) is a CPU-sandbox vendor** — talking their book on "CPUs are the new bottleneck." Dylan's independent corroboration (Amazon +3x, Intel/AMD sold out) is the load-bearing evidence; discount the host's framing, weight Dylan's numbers.
- Dylan explicitly says "not financial advice" on Intel and *de-hypes* the Intel turnaround — note the conviction discipline; do not over-read INTC.
- No price targets given. None to cite.

## Wiki updates suggested (orchestrator to action — NOT done here)
- **[[bottleneck-roadmap]]** — ADD new near-term layer: **server CPUs (2026)** driven by RL-environment verifiers + long-horizon agents; warm-pool dynamic; GPU:CPU ratio collapsing. Sequence becomes: GPU (23-24) → memory/HBM (25-26) → **CPU (26)** → EUV/ASML (28-30).
- **[[AMD]]** — EPYC sold out, price-increase notices, server-share tailwind from CPU shortage.
- **[[INTC]]** — Xeon sold out + foundry-of-last-resort for vendors kicked off TSMC N3; BUT add Dylan's temper ("not saved," cyclical not structural).
- **[[ARM]]** — standalone-CPU launch (~June 2026) + Meta/Cloudflare design wins; royalty→silicon business-model shift.
- **[[AMZN]]** — Graviton +3x install YoY; OpenAI ported x86→ARM for Amazon capacity (the recent Amazon/OpenAI deal was partly a CPU grab).
- **[[NVDA]]** — Vera CPU demand-confirmed (no standalone Grace volume historically); Groq acquisition partly = Groq-on-Samsung (no TSMC N3 left).
- **[[MU]] / [[SNDK]] / [[WDC]]** — NAND/SSD now +3-4x with ~60% more to come (NAND catching up to DRAM — update vs 2026-05-09).
- **[[TSM]] / [[AAPL]] / [[MEDIATEK]] / [[CBRS]]** — N3 monopolized by AI; mobile vendors pushed to N2 or toward Intel.
- **[[inference-economics]]** — agentic-task unit cost now has a rising vCPU component (warm pools, verifiers, sandboxes).
- Watch-list (no page yet): **Daytona** (private, sandbox infra); managed-Ray / RL-environment infra providers.
