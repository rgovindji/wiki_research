---
date: 2026-06-22
type: article
publisher: SemiWiki (forum + articles; aggregating WSJ, Nikkei, Newswitch)
url: https://semiwiki.com/forum/
raw_path: null
touches: [MU, ASML, TSM, ai-bubble-debate, bottleneck-roadmap, semiconductors]
---

# SemiWiki daily sweep — memory crunch (WSJ), China-without-ASML, TSMC, 800V racks

Incremental SemiWiki scan returned 7 new items. Curated five; captured the long tail per the standing curator instruction.

## TL;DR
- **WSJ "Why the Memory Crunch Is Almost Impossible to Solve"** (June 19): the shortage behind Apple's price hikes is structural and slow to fix — new US fabs don't help for years (Micron Boise opens ~mid-2027; Clay, NY not until 2030). The three titans (Samsung, SK Hynix, Micron — all now >$1T valued) are running capacity for AI and staying conservative on new plants despite record margins (Micron's GM 80%). "AI companies have the deepest pockets and they're outbidding everyone else for memory."
- **"Can China build a self-sufficient equipment supply chain without ASML?"**: SMEE reportedly validating 28nm ArF immersion litho; NAURA mass-producing 28nm gear; AMEC validating 14nm tools at SMIC; Huawei supporting domestic equipment dev. Consensus in-thread: China can get self-sufficient at 28nm-and-above and selectively into 14/7/5nm with compromises, but replacing ASML for economical 5/3nm HVM is a 2030s problem.
- **"Why TSMC doesn't even need to win the AI race"**: TSM Q1 FY26 revenue +41% YoY to $35.9B, EPS +58%, HPC = 61% of revenue; 2026 capex guide $52-56B; $106B cash; 5nm+3nm dominant (7nm now just 13% of wafer revenue). The more the titans compete, the more wafers they all buy from TSMC.

## Key facts
- Micron US fab timeline: Boise first facility ~mid-2027; Clay, NY ~2030 — confirms the structural-shortage runway the MU bull case rests on.
- China equipment progress is at MATURE nodes (28/14nm); advanced-node EUV substitution remains a 2030s question — so the [[ASML]] EUV chokepoint is intact near/medium-term, but the China DUV/service revenue erosion (the MATCH-Act bear leg) gets a fresh datapoint.
- **800V DC rack architecture (diamond-in-the-rough):** at 1,000 kW rack power, moving from 54V to 800V DC cuts current ~15x (18,518A → 1,250A) — less copper, lower I²R loss, smaller busbars. But 800V is a system-realization challenge: clearance/creepage, arc risk, connector safety, hot-swap, fault isolation. Supports the [[ETN]]/[[VRT]] 800V-DC transition thesis.

## Key claims (and how confident)
- **Memory shortage is supply-physics-bound, not a pricing blip (high).** WSJ corroborates the wiki's structural-shortage-through-2028 thesis from a mainstream desk, days before MU's June 24 print.
- **China-without-ASML is a 2030s story at the leading edge (medium).** Near-term: ASML's chokepoint holds; the erosion is in mature-node share + China service revenue.
- **Bear voice captured for balance:** an FT-style op-ed ("AI is the greatest money-wasting scheme") argues 35% of the S&P sits in 7 firms, six unprofitable on AI; $1.4T cumulative capex against <$60B annual AI turnover; Stein's Law. Pure bear-narrative, no new fact, but the framing belongs in [[ai-bubble-debate]].

## Quotes worth keeping
> "The AI companies have the deepest pockets in the economy and they're outbidding everyone else for memory. The rest of us just have to pay for it." — Jim Secreto (ex-Commerce), WSJ, 2026-06-19.

## Wiki updates made
- [[MU]] — WSJ memory-crunch bullet (US-fab timeline, 80% GM, titans >$1T) ahead of the June 24 print.
- [[ASML]] — China self-sufficiency thread (SMEE/NAURA/AMEC progress at mature nodes; EUV substitution a 2030s problem).
- [[TSM]] — fresh Q1 FY26 figures + the "every titan's competition is TSMC's tailwind" framing.
- [[bottleneck-roadmap]] — 800V DC rack physics (15x current reduction) supporting the power-transition thesis.
- [[ai-bubble-debate]] — the $1.4T-capex-vs-<$60B-turnover bear op-ed added to the bear column.
- Skipped: two SemiWiki vendor/thought-leadership pieces (AION Silicon RISC-V SoC white paper; "Available Is Not In Control" fab-ops essay) — no new investable fact.
