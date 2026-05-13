---
date: 2026-05-09
type: podcast
publisher: Dwarkesh Podcast
guest: Dylan Patel (CEO, SemiAnalysis)
host: Dwarkesh Patel
url: https://www.dwarkesh.com/p/dylan-patel-2
raw_path: raw/podcasts/dwarkesh_dylan_pod.txt
duration_topics:
  - 00:00:00 Why an H100 is worth more today than 3 years ago
  - 00:24:52 Nvidia secured TSMC allocation early; Google is getting squeezed
  - 00:34:34 ASML will be the #1 constraint for AI compute scaling by 2030
  - 00:55:47 Can't we just use TSMC's older fabs?
  - 01:05:37 When will China outscale the West in semis?
  - 01:16:01 The enormous incoming memory crunch
  - 01:42:34 Scaling power in the US will not be a problem
  - 01:54:44 Space GPUs aren't happening this decade
  - 02:14:07 Why aren't more hedge funds making the AGI trade?
  - 02:18:30 Will TSMC kick Apple out from N2?
  - 02:24:16 Robots and Taiwan risk
touches:
  - bottleneck-roadmap
  - ai-capex-cycle
  - ai-bubble-debate
  - nvda-supply-chain
  - semiconductors
  - NVDA
  - TSM
  - ASML
  - MU
  - SNDK
  - WDC
  - AAPL
  - TSLA
  - GOOGL
  - AMZN
  - META
  - VRT
  - ETN
  - KLAC
  - LRCX
  - CRWV
  - NBIS
---

# Dwarkesh × Dylan Patel — The Semiconductor Supply Chain Through 2030

## TL;DR
- **Memory is the binding constraint *now*** (2026); **EUV / ASML tooling is the binding constraint by 2028-2030**. Power will not be the bottleneck — there are 16+ gas/power vendors and behind-the-meter alternatives.
- **An H100 is worth MORE today than 3 years ago** — falsifies the bear "GPUs depreciate fast, capex is overstated" thesis. AI labs signing $2.40/hr 2-3yr deals on H100s vs. $1.40 build TCO.
- **Apple is being structurally pushed out of TSMC's leading edge** as AI customers prepay, NCNR, and outbid. Memory cost crunch will halve smartphone unit volumes (1.4B → 500-600M). **AAPL more bearish than the wiki currently reflects.**
- ASML can make ~70 EUV tools/year now → ~100 by 2030. **3.5 EUV tools = 1 GW** of AI chips. By EOD (~700 cumulative tools): ~200 GW/year of AI chip capacity *if all goes to AI*.

## Key facts (with verbatim numbers)

### Compute scale
- Big 4 (MSFT/AMZN/GOOGL/META) 2026 capex: **~$600B**; whole supply chain: **~$1T**
- 2026 incremental US capacity: **~20 GW** critical IT
- OpenAI + Anthropic each at **2-2.5 GW now**; targeting **5-6 GW by EOY 2026**, **~10 GW by EOY 2027**
- Anthropic adding **$4B → $6B/month** in revenue → ~**$60B run-rate growth over next 10 months** → needs **+4 GW inference capacity** just to grow
- $50B CapEx / $10-13B rental per gigawatt
- Meta is adding more capacity in 2026 alone than its entire 2022 fleet of compute and data centers
- Google Gemini Q4 ARR: **$5B** (post Nano Banana / Gemini 3 inflection)

### H100 economics (the long-life depreciation thesis)
- Hopper TCO over 5 years: **~$1.40/hr** to deploy
- $2.00/hr long-term contracts → ~35% gross margin
- AI labs signing **$2.40/hr** for 2-3 years now (post-OpenAI raise)
- Counter to Michael Burry / 3-yr depreciation bears: **the value-per-token argument** beats the price-of-newer-chips argument when supply is constrained

### Nvidia leverage
- **$90B of long-term contracts secured** with TSMC + memory makers
- Nvidia signed earlier and harder than Google/Amazon — NCNR, deposits
- By 2027: Nvidia will have **>70% of N3 wafer capacity**
- Nvidia *purposely fractures* complementary industries (neoclouds; data-environments) to maintain leverage
- Jensen "is X-1, not X — not as AGI-pilled as Dario / Sam" → even Nvidia is under-supplying vs. lab demand

### TSMC dynamics
- N3 was Apple-dominant in 2025; Apple moving to N2
- TSMC margin advantage on **HPC > mobile**
- TSMC favors CPU > GPU allocation (Graviton, AMD CPUs) because **CPU is "stable growth," GPU is cyclical**
- N2 in 2026: Apple still has the **majority**; year after, Apple "closer to half"; then drops
- **A16 (N2 variant): first customer is AI, not Apple**

### Memory / HBM
- **30% of Big 4's 2026 CapEx going to memory** (a third!)
- HBM4 stack: **2.5 TB/s** vs DDR5: **64-128 GB/s** in same shoreline area (1 order of magnitude)
- HBM consumes **3-4x more wafer area per bit** than commodity DRAM
- Memory prices **already tripled**; could double or triple again
- iPhone BOM impact: $50 → ~$150 just on memory; ~$250 retail price impact
- **Smartphone unit volumes**: 1.4B → 1.1B → projected **800M (2026)** → **500-600M (2027)**
- Xiaomi/Oppo cutting low/mid-end volumes by half
- Demand destruction in consumer is the **mechanism** for AI to get more memory
- NAND going up too but **less than DRAM** (more consumer destruction releases NAND back to AI)
- Memory makers (SK Hynix, Samsung, Micron) signing 3-year deals at higher prices
- **3D DRAM is the late-decade architecture shift** (6F → 4F → 3D); will retool fabs but not until 2028-2030

### ASML / EUV — THE bottleneck for 2028+
- ASML EUV output: **~70 tools/yr now → 80 next year → maybe 100 by 2030 aggressive**
- Tool price: **$300-400M each**
- Each tool: 75 wafers/hour at 90% uptime
- **3.5 EUV tools = 1 GW of AI chips**
- 1 GW = ~55K wafers of 3nm + 6K wafers of 5nm + 170K wafers of DRAM = **~2M EUV passes/GW**
- $50B capex per GW vs. only **$1.2B of EUV tooling per GW**
- 2030 cumulative: ~**700 EUV tools → ~200 GW/year of AI capacity** (if all allocated to AI)
- Sam Altman wants 52 GW/yr by EOD = 25% of theoretical max
- Elon wants 100 GW/yr (in space)
- ASML supply chain: **10,000+ people**; Cymer (San Diego, source), reticle stage (Wilmington CT), wafer stage + optics (Carl Zeiss, Europe — most important)
- 18 multilayer molybdenum/ruthenium mirror lenses per tool
- Wafer stage moves at **9 Gs**, sub-nanometer overlay accuracy
- ASML has **NOT** taken margin like Nvidia / memory players — gross margin discipline atypical for a monopoly
- Tool gets shipped disassembled across multiple plane loads, reassembled at customer site

### Power — "not a problem"
- Currently 20-30 GW critical IT capacity → 200 GW by EOD
- Add 20-30% gross-up for transmission/cooling losses
- US grid is **~1 TW** — data centers 3-4% today → 10% by 2028
- **Could unlock 20% (~200 GW) of US grid** with utility-scale batteries absorbing peaks
- 16+ vendors of gas-power generation tracked by SemiAnalysis; **hundreds of GW of orders**
- Behind-the-meter share of new capacity: **~50% by EOD**
- Alternatives beyond combined-cycle GT: aeroderivatives, reciprocating engines, ship engines (Nebius+MSFT NJ), Bloom Energy fuel cells, solar+battery, wind+battery
- Cost spread: combined-cycle ~$1,500/kW; alternatives up to $3,500/kW (~2.4x). **Hopper TCO impact: only +10c/hr on $1.40/hr** = the trade is worth it

### China
- Today, 100% of China's 7nm/14nm uses **ASML DUV**
- China indigenized DUV: **likely by 2030** (~100 tools/yr possible)
- China indigenized EUV: **working tools by 2030** but not high-volume
- Huawei Ascend 7nm AI chip predated TPU by 2 months and A100 by 4 months — but banned from TSMC since 2019
- "Fast timelines US wins, long timelines China wins"
- "If Huawei had TSMC, they'd already be the #1 customer"

### Space data centers (the Elon thesis)
- Same chip constraint applies
- 6+ months added to deploy vs Earth = **10% of GPU useful life**
- 15% of Blackwell GPUs need RMA on initial deploy
- Networking: per-rack scale-up bandwidth scales 2x per gen — space lasers can't keep up with NVLink
- Verdict: **not this decade**; possibly 2035+ when chips are no longer the bottleneck

### Robots
- Distributed compute model: planning in cloud (high-batch), thin local model on robot
- Elon signed **Samsung Texas deal** for robot chips → Taiwan-risk diversification + escapes the AI-data-center wallet competition
- Nvidia's new LPU (launching at GTC) is built on Samsung — only other AI demand on Samsung

### Taiwan tail risk
- "Snake eating its own tail" — EUV tools use Taiwan-fabbed chips
- If Taiwan goes: capacity drops from 200 GW/yr (EOD) to **10-20 GW/yr** across Intel + Samsung
- Airlifting engineers doesn't fix it — fabs need to be physically rebuilt

## Key claims (and how confident)

| Claim | Confidence | Why it matters |
|---|---|---|
| H100 worth more today than 3 yrs ago | High (priced in long-term deals) | Falsifies short-depreciation bear case for AI capex |
| EUV is THE binding constraint by 2028-2030 | High (single-source SemiAnalysis tracks tools) | Reframes [[ASML]] as the supply-chain linchpin |
| 30% of 2026 capex going to memory | Medium-High (consistent with separate sources) | Validates [[MU]] thesis; quantifies HBM pull |
| Smartphone volumes go to 500-600M by 2027 | Medium (forecast, but supplier data points already showing) | Bear catalyst for [[AAPL]]; bull for [[MU]]/HBM |
| Apple loses majority of N2 within 2 years | Medium-High | Significant negative for [[AAPL]] |
| Power will NOT be binding by EOD | Medium-High (16+ vendor tracking) | Tempers the [[VRT]]/[[ETN]] urgency narrative — they're growing fast but not THE constraint |
| China DUV indigenized by 2030 | Medium (Dylan acknowledges high uncertainty) | Long-timelines tail risk |
| Space data centers don't make sense this decade | High (chip-constrained, deploy-time penalty) | Bearish for any "Tesla space datacenter" narrative |

## Quotes worth keeping

> "An H100 is worth more today than it was three years ago." — Dylan, on long-life depreciation

> "OpenAI has got way more access to compute than Anthropic by the end of the year ... Dario screwed the pooch compared to OpenAI." — Dylan, on commitment timing

> "Jensen doesn't believe software is going to be fully automated ... he's still way more AGI-pilled than Google in Q3 of last year." — Dylan, on Nvidia's relative AGI-pilling

> "OpenAI and Anthropic know they need X. Nvidia is not quite as AGI-pilled. They're building X-1. You go down the supply chain, everyone's doing X-1. In some cases X÷2." — Dylan, on demand under-estimation

> "ASML has never raised the price more than they've increased the capability of the tool ... they've always provided net benefit to their customers." — Dylan, on ASML's atypical monopoly behavior

> "Memory prices ... could double or triple again ... what this does to the market is quite drastic." — Dylan

> "Apple ... will become a smaller and smaller percentage of TSMC's revenue, and therefore be less relevant for TSMC to cater to their demands ... they are just not TSMC's best bud like they have been historically." — Dylan, on AAPL/TSM relationship

> "Fast timelines US wins, long timelines China wins." — Dwarkesh, restating Dylan

> "If Taiwan goes ... incremental ability to add compute goes to almost zero. Instead of hundreds of gigawatts a year by the end of the decade ... maybe 10 gigawatts across Intel and Samsung, or 20 gigawatts. It's nothing." — Dylan

## Wiki updates made (this ingest)

### Created
- New theme page [[bottleneck-roadmap]] — synthesizes the time-sequenced constraints (memory now → cleanrooms → EUV by 2028-2030)
- This source summary

### Pending (surfaced for user review before edit — see log entry)
The following pages have material updates / contradictions to surface:

- **[[AAPL]]** — current page is "neutral / medium conviction." Source argues structural memory-cost squeeze halves smartphone volumes 2026→2027 AND TSMC kicks Apple to back of N2 line. **Proposal: tilt to bearish-medium.**
- **[[SNDK]]** — current page is "bull / medium." Source nuances: NAND pricing rises *less* than DRAM because consumer destruction releases NAND. **Proposal: add nuance, keep stance.**
- **[[VRT]] / [[ETN]] / [[NVTS]]** — current pages frame data center power as a binding constraint. Source explicitly: "scaling power in the US will not be a problem." **Proposal: add tempering note; thesis still works (huge growth) but not THE bottleneck.**
- **[[ASML]]** — current page is "bull / medium" because of 2026 China pull-forward digestion. Source frames ASML as the SINGLE binding constraint of all of AI by 2028-2030. **Proposal: upgrade conviction to high on multi-year horizon; keep medium near-term.**
- **[[MU]]** — current page captures the supercycle but underweights the *demand-destruction mechanism*. **Proposal: add the consumer destruction → AI memory release dynamic.**
- **[[NVDA]]** — add: $90B of long-term contracts secured; >70% of N3 by 2027; "X-1 not AGI-pilled" framing.
- **[[TSM]]** — add: TSMC favors CPU > GPU allocation; A16 first customer is AI not Apple.
- **[[TSLA]]** — add: Samsung Texas robot-chip deal (Taiwan-risk diversification, separate supply chain); space data center thesis dismissed.
- **[[GOOGL]]** — add: Q4 Gemini ARR $5B; sold Ironwood capacity to Anthropic in info-asymmetric error; has woken up massively (energy company, turbines, powered land).
- **[[ai-capex-cycle]]** — add: $1T full supply chain figure; demand under-estimation pattern across stack ("X-1 / X÷2").
- **[[ai-bubble-debate]]** — add: H100 *worth more today* counter-thesis to short-depreciation bears; but also note 30% of capex going to memory (margin stacking).
- **[[nvda-supply-chain]]** — add layer notes from this source (Cymer, Carl Zeiss, Victory Giant PCB, Foxconn).
- **Not-yet-covered watch list updates**: Carl Zeiss (private), Cymer (ASML-owned), GE Vernova (GEV, gas turbines), Bloom Energy (BE, fuel cells), Oracle (ORCL, OpenAI compute partner), CoreWeave already exists.
