---
date: 2026-06-01
type: event
publisher: NVIDIA / Computex 2026 keynote (Taipei)
url: https://fortune.com/2026/06/01/jensen-huang-nvidia-pc-reinvention-ai-chips/
raw_path: (no raw mirror — keynote coverage)
touches: [NVDA, DELL, INTC, AMD, ARM, AAPL, TSM, MSFT, robotics, humanoid-oems, nvda-supply-chain, ai-capex-cycle, overview]
---

# NVIDIA Computex 2026 keynote — RTX Spark PC superchip + Vera CPU "in full production" + Isaac GR00T humanoid reference design

## TL;DR

- **NVIDIA entered the PC chip market**: RTX Spark superchip (formerly codenamed N1X), Arm-based, **20-core Grace CPU + Blackwell RTX GPU (6,144 CUDA cores) + NPU + 128GB unified LPDDR5X**, all on a single **TSMC 3nm package**. Co-designed with **MediaTek** for the Grace CPU core. Ship fall 2026 in Windows laptops from **Microsoft, Dell, HP, ASUS, Lenovo, MSI**.
- **Vera CPU "in full production"** for data centers, named "our new major growth driver." Early customers: **Anthropic, OpenAI, SpaceX AI**. This is the structural pull-through of the May 20 NVDA Q1 FY27 earnings sovereign-AI thesis — the data-center CPU TAM is now revenue-bearing, not roadmap.
- **Isaac GR00T humanoid reference design** unveiled — ~6ft humanoid combining a **Unitree H2 chassis + Sharpa five-fingered dexterous hands**. NVIDIA is shipping a reference physical robot, not just the software/chip stack.
- **Market reaction**: NVDA **+2 to +4% intraday** (closed near $220.67, range $215.10-$222.17); **DELL +10%, HP Inc +8%** on PC partnership; **INTC and AMD both −3%+** on structural PC headwind. All three US indexes set fresh **record closes**: S&P 500 +0.26% to **7,599.96**; Nasdaq +0.42% to **27,086.81**; Dow +0.09% to **51,078.88**. 10th consecutive S&P weekly gain in progress.

## Key facts

### RTX Spark (N1X) PC superchip

| Spec | Value |
|---|---|
| Architecture | Arm-based superchip (CPU + GPU + NPU on single package) |
| CPU | **20-core Grace** (designed in partnership with MediaTek) |
| GPU | **Blackwell RTX with 6,144 CUDA cores** |
| Memory | **Up to 128GB unified LPDDR5X** |
| Foundry / node | **TSMC 3nm** |
| AI performance | ~1 petaflop |
| Launch | Fall 2026 |
| OEM partners | Microsoft Surface, Dell, HP Inc, ASUS, Lenovo, MSI |
| Target | Premium Windows laptops + desktops |

- Replaces (rather than complements) x86 in the OEM PC stack — RTX Spark is the system processor, not an AI accelerator riding on Intel/AMD.
- Picks up the Windows-on-Arm baton from **Qualcomm** (whose Microsoft Snapdragon exclusivity expired). MediaTek is now the Arm-core IP partner, not Qualcomm.
- First time NVIDIA ships a system-CPU SKU for the consumer PC market in its history.

### Vera CPU (data center) status

- **"In full production."** Jensen quote: "going to be our new major growth driver."
- Early-deployment customers: **Anthropic, OpenAI, SpaceX AI** (xAI). Validates the May 20 Q1 FY27 sovereign-AI commentary that Vera CPU is the new $200B TAM with production in H2 FY27.
- Vera Rubin sampling continues per May 20 plan; CPU side now ahead of the GPU-side cadence.

### Isaac GR00T humanoid reference design

- ~6ft humanoid robot reference architecture.
- **Unitree H2 chassis** (the same Chinese humanoid OEM whose Shanghai STAR IPO the wiki flagged on May 17).
- **Sharpa five-fingered dexterous hands** (third-party robotic hand vendor).
- Reference design — partners can build/ship.
- Reinforces the "NVIDIA = Android of robotics" framing: the chip + simulator + dataset + reference robot stack is now publicly visible end-to-end.

### Jensen Huang direct quotes

> "Microsoft and Nvidia are going to reinvent the PC."

> "This is going to be the new PC. This is the first across the lineup of PC reinvention for 40 years."

> "This reinvention of the computer is as big of a deal as the reinvention of the phone into what we now know as the smartphone."

## Key claims (and confidence)

- **Arm replaces x86 in premium Windows OEM lineups (high confidence directionally; uncertain magnitude).** Six OEM partners is a real commercial commitment, not a CES demo. The premium / AI-PC SKU is now Arm-led; mainstream / value SKUs remain x86. The Apple M-series proved Arm-on-laptop can dominate; the question is share-of-mix, not viability.
- **Vera CPU is a structural revenue line, not pilot (high confidence).** "In full production" + three of the largest AI labs as early customers is a different language tier than "sampling." Pulls forward the $200B Vera CPU TAM that the May 20 Q1 FY27 print introduced.
- **PC TAM is upside for NVDA, not material to 2026 P&L (high confidence).** Fall 2026 launch means meaningful revenue lands in FY28 and FY29. The bull case is structural: NVDA now has CPU + GPU + DPU + PC + automotive + robotics revenue lines, all underwritten by the same Blackwell→Rubin→Feynman compute roadmap.
- **Direct structural negative for Intel and AMD on the PC side (high confidence directionally).** Both stocks down 3%+ on the day is the cleanest market verdict. INTC was already running on event-driven binary (gov stake, Apple/Tesla foundry wins); this announcement compresses one of the bull legs (CPU ASP cycle).
- **Microsoft's commitment to Arm-Windows is now committed via OEM partner ecosystem, not Qualcomm-exclusive (high confidence).** This is the structural validation that Windows-on-Arm can work without Qualcomm being the only IP partner.
- **MediaTek (2454.TW / MDTKF) is the unsung beneficiary (medium confidence).** Co-designed the Grace CPU core. Wiki does not currently cover MediaTek; this announcement is the explicit reason to add it.

## Wiki updates made

- **New source summary** — this file.
- **[[NVDA]]** — added Recent developments entry; reinforces bull thesis with three additional structural moats (PC TAM, Vera CPU in production, Isaac GR00T reference design). Conviction held at **bull/high** (already at ceiling, no upgrade needed).
- **[[DELL]]** — added Recent developments entry; +10% close confirms the wiki's "first-mover AI server channel" thesis extending into the consumer/SMB AI-PC lane.
- **[[INTC]]** — added Recent developments entry flagging the −3% close and PC-TAM structural compression of one of the bull legs; **stance unchanged at neutral/low** but the binary event-driven trade premise weakened today.
- **[[AMD]]** — added Recent developments entry; PC-segment headwind acknowledged. Data-center MI400/Helios thesis intact; conviction held at **bull/high**.
- **[[ARM]]** — added Recent developments entry; Vera CPU full-production + RTX Spark Arm-based premium PC lineup = the cleanest royalty-stream pull-through the wiki has captured this year. Conviction held at **bull/medium** with note that bull-case "Vera Rubin volumes 2H 2026" is now empirically validated.
- **[[AAPL]]** — added Recent developments entry; Apple M-series Mac competitive landscape now has six Windows-side Arm OEMs with NVIDIA RTX GPU integrated. Bear thesis sharpens at margin (M-series premium hardware moat narrows over 18-24 months).
- **[[TSM]]** — added Recent developments entry; N3 leadership validated (RTX Spark on TSMC 3nm). Conviction held at **bull/high**.
- **[[robotics]]** — added Isaac GR00T reference design note; Unitree H2 chassis + Sharpa hands surfaces a new component-supplier read-through layer.
- **[[humanoid-oems]]** — Unitree H2 confirmed as the chassis-design reference partner for NVIDIA's first publicly shipped humanoid; commercial implication: Unitree's STAR IPO valuation backstop just strengthened.
- **[[overview]]** — June 1 PM section appended above the June 1 AM (GOOGL) section: Computex announcement + record-close numbers + intraday cross-currents (GOOGL down on raise vs. NVDA/DELL/HP up on chip).
- **[[ai-capex-cycle]]** — note that Anthropic/OpenAI/SpaceX AI named as Vera CPU early customers further crystallizes the demand-pull thesis at the lab tier.
- **[[index]]** — new entry in Recent source ingests.

## Cross-references

- Vera CPU $200B TAM was introduced in [[2026-05-20-NVDA-Q1-FY27-earnings]] — today's "in full production" announcement converts that from roadmap to revenue-bearing.
- Windows-on-Arm history: [[2026-05-09-dwarkesh-dylan-semianalysis]] discussed Qualcomm's Windows-on-Arm exclusivity expiry; today's six-OEM RTX Spark roster is the structural follow-through.
- Isaac GR00T N1.7 / N2 roadmap: [[2026-05-17-robotics-multi-agent-batch]] (Agent F) — today's GR00T reference design is the physical-robot equivalent of those software/chip building blocks.
- Vera Rubin roadmap: [[2026-05-20-NVDA-Q1-FY27-earnings]] (samples shipped + production H2 FY27 + 10x inference cost reduction).
- TSMC #1-customer status: [[2026-05-17-multi-agent-research-batch]] (Agent B) — RTX Spark on TSMC 3nm reinforces this.

## Other June 1 market signals (not separate source summaries — surfaced for context)

- **Marvell (MRVL) hit a new ATH** post Q1 FY27 print last week: rev $2.4B (+28% YoY), Q2 guide $2.7B (+35% YoY), trading ~70x trailing earnings, +130% YTD. Wiki has MRVL on the "not yet covered" list; this is the second consecutive material print that argues MRVL coverage should be promoted. Custom-silicon companion to [[AVGO]] + optical-DSP layer (AWS Trainium 2).
- **ServiceNow (NOW) +8.6% to ~$91.49** on BofA reinstated Buy / $130 PT and an analyst-narrative shift framing NOW as a *beneficiary*, not victim, of agentic AI. Record 40% rally in four sessions. Not in the wiki; surfaced for awareness — AI-software bellwether worth tracking but lower priority than the picks-and-shovels stack.
- **IBM +9%** on bullish analyst initiation. Not in the wiki; mainframe + consulting + watsonx + quantum optionality. Surfaced for awareness only.
- **WTI +5% to $92** on US-Iran peace-talk uncertainty (tentative 60-day ceasefire extension awaiting Trump approval). [[hedging-risk]] / [[commodity-producers]] unchanged.
