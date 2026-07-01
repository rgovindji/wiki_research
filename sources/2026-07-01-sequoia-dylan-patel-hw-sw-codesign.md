---
date: 2026-07-01
type: podcast
publisher: Sequoia Capital (Training Data)
url: https://www.youtube.com/watch?v=f6D_aiy8qyU
raw_path: raw/podcasts/2026-07-01-sequoia-dylan-patel-hw-sw-codesign.txt
touches: [inference-economics, bottleneck-roadmap, ai-capex-cycle, ai-bubble-debate, NVDA, AVGO, CRWV, NBIS, CRUSOE, SPCX, MU, GOOGL]
---

# Dylan Patel (SemiAnalysis) on Sequoia's Training Data — hardware-software co-design, per-GW economics, the compute crunch

## TL;DR
- **Hardware-software co-design is the real 100x.** Isolated gains at the hardware, systems, and model layers are ~2x each (multiplicative to ~8x); *co-optimizing all three* is where a 100x shows up. "Silicon alone gets you 8x." Model cost for equivalent quality falls ~60x/yr; intelligence-per-watt ~40x/yr; Hopper→Blackwell was ~30x on an optimized DeepSeek deployment over 3 years.
- **Hard per-gigawatt rental numbers** (the cleanest public dataset on neocloud economics yet): Trainium <$10B/GW to Anthropic/OpenAI; GPUs ~$12–13B/GW (neocloud *and* Amazon; Amazon subsidizes so the gap is wider); the SpaceX→Google deal ~$25B/GW ($25M/MW/yr) — a "crazy divergence" justified by SpaceX delivering *running* compute now vs paper signed 6 months early. Colo power-only: $/kW/month went $60 → $120–160 (some $200 bad-credit, $80 India).
- **Compute crunch is demand *and* supply.** 20 GW deployed in 2026, >30 GW in 2027 (after delays). Persists as long as model progress keeps expanding the TAM of useful tasks faster than compute grows — which it has over the last 6 months.

## Key facts
- **Co-design > single-layer wins.** DeepSeek's efficiency came from co-optimizing model shape (expert sizes, attention, arithmetic intensity, collectives) to the *specific* chip (V3→Hopper, V4→Blackwell/Huawei). "TPUs suck at running DeepSeek" but are great at other model families; NVLink connects 72 GPUs, Google's ICI connects ~8,000 chips (no switch, but you hop through chips). You *cannot* rank TPU vs NVIDIA in isolation because the comparison extends up into the model layer.
- **CUDA moat "partially disentangled."** Models now write their own kernels (Claude/Codex do the optimization work), and there are only *tens* of frontier model companies, not thousands — so the "everyone needs CUDA compatibility" thesis is weakening. The *real* lock-in is that downstream open models (DeepSeek, Kimi, Qwen, Xiaomi, Nemotron) are co-designed for GPUs → ecosystem gravity. Google's counter = ship its own good open models (Gemma) so an OSS ecosystem optimizes for TPUs.
- **Everyone gets an ASIC program, but keeps general-purpose compute too.** Google runs *three different* TPU design programs (Broadcom, MediaTek, and an undisclosed third — *different architectures*, not just different vendors). Everyone will deploy tens of $B (Google hundreds of $B/yr) of custom silicon — but also keep NVIDIA because labs "don't even know what architecture they'll run in a year." Local-minima risk: an ASIC optimized perfectly for today's architecture can be *wrong* after a model-architecture breakthrough. NVIDIA stays the general-purpose hedge. (Datapoint: Google paying xAI ~$11/GPU-hr despite owning TPUs.)
- **Anthropic economics (hard numbers).** Q2 net-income profitable ex-SBC; possibly profitable *incl.* SBC by Q3. Opus 4.8 API per-token gross margin >80% (corporate GM clawed down by Bedrock/Vertex deals). Because margins are so high, Anthropic can pay *above market* for every GPU/TPU/Trainium and still expand NOI ("every GPU I rent I immediately sell tokens on at positive margin") — restates the "monetization-per-GW rising" bull leg with a real P&L.
- **Gigawatts are heterogeneous.** "A gigawatt given to Anthropic is worth more revenue than a gigawatt given to OpenAI." Google puts ~1.5 GW of hardware in a 1 GW site (power-sloshing) and cuts utility deals (2 GW except ~3 days/yr → curtail) to *sell more gigawatts* — ties directly to Pebble's ~100 GW "flexible power" thesis (6/26). Best operators (SpaceX networking from Starlink, power mgmt from Tesla) likely extract more per watt.
- **Why neoclouds exist.** AI GPU rental mechanics (whole-rack, long-term contracts; no time-splicing) stripped away the hyperscalers' CPU-cloud moats — Nitro NICs *hurt* AI performance; security/isolation irrelevant. Microsoft's own DC teams "fell on their face" when they had to double the forecast → had to buy neocloud capacity. CoreWeave GPU compute tested *better* on perf/reliability than hyperscalers; CoreWeave/Crusoe = hyperlevered equity owners (crypto + hedge-fund roots) who deliver faster.
- **Jensen's chess.** He funds neoclouds *and* Chinese labs to force a *multipolar* world — because a world where only OpenAI/Anthropic/Google models exist, or only hyperscalers build compute, is one where NVIDIA is "screwed." Every GPU is the same price today, but 5 years out, thriving neoclouds = weaker TPU/Trainium = better for NVIDIA.
- **Memory (technology angle).** No memory *cell* breakthrough in decades (NAND ~25 yr, DRAM ~40 yr); HBM has only added stacks/speed. Next: stacking memory *directly on* the compute die (vs beside it) → bandwidth "explodes." Power density stuck at ~1 W/mm² for two decades (Rubin ~2,000 W, Rubin Ultra ~4,000 W); pushing past 1 W/mm² lets you use *less* silicon at higher power.
- **Space compute:** sub-1% of inference by 2030, but majority of *incremental* compute by ~2040. OpenAI+Anthropic combined >100 GW by 2030; terawatts by 2040.
- **Cerebras:** great at fast inference, but SRAM chips struggle to hold very large models (10T+ params) at long context (1M) — risk is that the models worth paying "fast mode" for are exactly the big ones that don't fit.
- **Live tape color:** references "Fable 5 / Mythos 5 dropped today," huge step-function, heavy switching *despite* higher price → "volume-by-dollars, not volume-by-tokens" is what matters. Thinking Machines' Tinker doing "a few hundred million ARR" <6 months out.

## Key claims (and how confident)
- Per-GW rental figures (Trainium <$10B, GPU $12–13B, SpaceX $25B) — **medium-high** (Patel's proprietary DC model; directionally corroborated by prior GPU-rent-inversion sources, but exact figures unverifiable).
- Anthropic Q2 profitable ex-SBC / >80% Opus-token margin — **medium** (specific, insider-sourced, not disclosed by Anthropic; talks-book adjacent).
- Co-design 100x / 60x-cost / 40x-intelligence-per-watt framing — **medium-high** (consistent with SemiAnalysis's published InferenceX work).
- Google running 3 distinct TPU architectures — **medium** (single-source; specific and plausible).

## Bias flags
- **Sequoia hosts (Sean, Sonia Huang) are large SpaceX investors** and disclosed investments in Crusoe and in "Navian/Deveen's" co-design startup — so the SpaceX-per-GW-premium and neocloud-quality framing is *talk-their-book*.
- **Dylan Patel sells SemiAnalysis research + the InferenceX benchmark** and openly "loves SpaceX, would buy the IPO." Every directional call (neocloud quality, SpaceX efficiency, Anthropic margins) carries promotional tint.

## Contradictions / tensions with the wiki
- The >80% Opus-token margin + "pay above market for every GPU and NOI still rises" is the strongest *bull* rebuttal yet to the Chanos/Damodaran "neocloud = 4–8% ROIC finance company" bear — but it describes the *model lab's* economics, not the *landlord's*. Surfaced, not resolved.
- Reinforces (does not resolve) the ai-bubble-debate: crunch is real *because* model progress keeps expanding TAM; "it's very possible model progress stops" is the stated falsifier.

## Wiki updates made
- [[inference-economics]] — co-design 100x, 60x/40x curves, per-GW rental table, Anthropic >80% margin / above-market-GPU logic.
- [[bottleneck-roadmap]] — memory-on-chip stacking, 1 W/mm² power-density wall (Rubin 2kW/Rubin-Ultra 4kW), CUDA-moat partial disentangle, Google 3 TPU programs.
- [[ai-capex-cycle]] — 20 GW (2026) → >30 GW (2027) deployment; every-quarter-more crunch.
- [[ai-bubble-debate]] — heterogeneous-gigawatt bull leg + "model progress stops" falsifier; Anthropic profitability.
- [[NVDA]] — Jensen multipolar-chess rationale; general-purpose hedge vs local-minima ASIC risk.
- [[CRWV]] / [[NBIS]] / [[CRUSOE]] — why neocloud exists (hyperscaler moats stripped); Crusoe halt-construction tweet; hyperlevered-equity model.
- [[SPCX]] — $25B/GW rental to Google; "running compute now" premium; Anthropic bought SpaceX GPUs below Google rate.
- [[MU]] — no memory-cell breakthrough; memory-on-chip as next bandwidth lever.
- [[AVGO]] / [[GOOGL]] — Google TPU-with-Broadcom program (one of three).
