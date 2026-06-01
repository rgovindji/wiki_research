---
date: 2026-06-01
type: keynote
publisher: NVIDIA / GTC Taipei + Computex 2026 keynote
url: https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark
raw_path: n/a (public keynote + NVIDIA newsroom press releases)
touches: [NVDA, ARM, MEDIATEK, INTC, AMD, QCOM, AAPL, TSM, DELL, HPE, MSFT, ORCL, CRWV, robotics, humanoid-oems, nvda-supply-chain, ai-capex-cycle, bottleneck-roadmap, overview]
---

# NVIDIA Computex Keynote — RTX Spark PC Superchip + Vera CPU "In Full Production" + Isaac GR00T Humanoid Reference

On **2026-06-01 in Taipei**, Jensen Huang delivered the NVIDIA GTC Taipei keynote (running concurrently with Computex 2026). Three structural product announcements stacked in a single session — **(1) RTX Spark** (NVIDIA's first ground-up consumer PC superchip targeting the premium Windows laptop market), **(2) Vera CPU** ramping into full production with Anthropic, OpenAI, SpaceX (xAI), Oracle, CoreWeave, and Dell named as initial customers, and **(3) Isaac GR00T H2+** (the open humanoid-robot reference design built on Unitree's H2 chassis with Sharpa Wave hands and Jetson Thor compute). Plus the surprise-to-the-upside reveal that the **Vera Rubin supply chain has now doubled relative to Grace Blackwell**, spans **350+ factories in 30 countries** (150 in Taiwan), and rack assembly time has compressed from **~2 hours to ~5 minutes** via cable-free modular trays. Jensen called Vera Rubin **"the largest product launch, probably in the history of Taiwan."**

This is a **tier-1 platform-expansion event** for the wiki. Stance impact: bull case sharpens at NVDA / ARM / TSM / DELL / MEDIATEK; one bull leg compressed at INTC / AMD / QCOM / AAPL.

## TL;DR

- **NVIDIA entered the PC chip market**: **RTX Spark superchip** (formerly codenamed N1X) — Arm-based **20-core Grace CPU** (10× Cortex-X925 perf + 10× Cortex-A725 eff, up to 4.1 GHz) co-designed with **MediaTek (2454.TW / MDTKF)** + **Blackwell RTX GPU with 6,144 CUDA cores + 5th-gen Tensor Cores (FP4)** + NPU + **up to 128 GB unified LPDDR5X**, linked via **NVLink-C2C**, on a single **TSMC N3 (3nm) package**. **Up to 1 petaflop AI compute.** Ships **October 2026** (fall 2026); **starting at $1,499**; OEMs: **Microsoft Surface, Dell, HP, ASUS, Lenovo, MSI**.
- **Vera CPU now "in full production"** — Jensen called it **"our new major growth driver."** Initial customers named: **Anthropic, OpenAI, SpaceX (xAI), Oracle, CoreWeave, Dell**. NVIDIA claims **Vera completes tasks ~80% faster than x86 equivalents** (Intel/AMD comparison) on agentic AI workloads. Converts the **$200B Vera CPU TAM** announced at the May 20 Q1 FY27 print from roadmap to revenue.
- **Vera Rubin platform full production** — supply chain **doubled vs. Grace Blackwell**; **350+ factories across 30 countries; 150 in Taiwan**. Rack assembly time compressed **~2 hr → ~5 min (~95% reduction)** via cable-free modular trays. Jensen: *"the largest product launch, probably in the history of Taiwan."*
- **Isaac GR00T H2+ humanoid reference design** — **Unitree H2+ chassis** (~6 ft, 150 lb, **31 DOF** body) + **Sharpa Wave five-fingered tactile hands** (22 DOF/hand → **75 DOF total**) + **Jetson Thor onboard compute** ($1,999/130W Blackwell-architecture edge SoC). Available from Unitree **late 2026**. First customers: **Ai2, ETH Zurich, Stanford Robotics Center, UC San Diego ARC Lab**.
- **Also unveiled**: **Nemotron 3 Ultra** (500B-param open-weights agentic AI model — NVIDIA's largest open release ever); **Cosmos 3** (first open Physical AI omnimodel; #1 on 7+ robotics benchmarks); **DLSS 4.5 Ray Reconstruction** (August timeframe); **DGX Station for Windows** ($3,999 → $4,699 subsequently raised on memory constraints).
- **Stock reaction:** **NVDA +5% intraday → near $222** (closed near **$220.67** vs $211.14 Friday); **DELL +10%; HP Inc +8%; QCOM −7%; INTC −3%+; AMD −3%+**. Three index records: **S&P 500 +0.26% → 7,599.96 · Nasdaq +0.42% → 27,086.81 · Dow +0.09% → 51,078.88**. **10th consecutive S&P weekly gain in progress**.
- **The "supply-side rallies, demand-funding mechanism sells off" framework expression of the year:** RTX Spark + Vera CPU + Vera Rubin + GR00T = picks-and-shovels supply side rallying while [[GOOGL]] (the AM $80B equity raise) sold off −2.51% to $380.34. **Cleanest single-day expression of the wiki's "supply discipline vs. demand-funding mechanism" framework all cycle.**

## RTX Spark superchip (the headline product)

### Technical specs

| Spec | Value |
|---|---|
| Codename / brand | **N1X** (silicon) → **RTX Spark** (consumer brand) |
| CPU | **20-core Grace** — Arm v9.2-A; **10× Cortex-X925 performance + 10× Cortex-A725 efficiency** cores |
| CPU clock | up to **4.1 GHz** |
| CPU co-design partner | **MediaTek (2454.TW / MDTKF)** |
| GPU | **Blackwell RTX** — **6,144 CUDA cores** + **5th-gen Tensor Cores (FP4)** |
| Interconnect | **NVLink-C2C** chip-to-chip |
| Memory | **up to 128 GB unified LPDDR5X** (CPU + GPU shared) |
| AI compute | **up to 1 petaflop** |
| Process | **TSMC N3** (3nm) |
| Ship date | **October 2026** (fall 2026) |
| Starting price | **$1,499** |
| OEM partners | **Microsoft Surface, Dell, HP, ASUS, Lenovo, MSI** (6 OEMs — entire premium-Windows OEM stack minus Acer) |
| Gaming claim | **100 FPS at 1440p in AAA games** (with DLSS) |

### Microsoft co-launch

Satya Nadella joined Jensen on stage (rare joint keynote). NVIDIA + Microsoft confirmed jointly that **"the first Windows on Arm PCs with native CUDA acceleration will arrive in October 2026."** The framing was **Microsoft-led**: "personal AI" / "agentic AI OS." Microsoft Surface is one of the six OEM brands shipping at launch.

### Competitive context

- **Qualcomm**'s exclusive Windows-on-Arm partnership with Microsoft **expired in late 2025 / early 2026**. RTX Spark drops into the socket Qualcomm just vacated. **QCOM −7% intraday** is the market verdict.
- **Apple M-series** (M5 Pro/Max/Ultra) was the *only* shipping architecture with unified CPU+GPU memory at this scale. That architectural lead is **no longer uniquely Apple's.**
- **Intel Lunar Lake / Panther Lake (x86 AI-PC)** — premium-AI-PC ASP power leg compressed; foundry-binary part of the bull case intact.
- **AMD Ryzen AI Max+ / Strix Halo** — directly competes; Ryzen AI leg compressed; Helios MI400/MI450 data-center thesis intact.

**Which means**: RTX Spark is NVIDIA charging the gate on the one major compute market it doesn't own — the $100B+ Windows premium-laptop market. By fall 2026, the canonical AI-PC will run a Blackwell GPU. NVDA's bull case adds a **third revenue line** (CPU + GPU + DPU + PC + automotive + robotics, all on the same Blackwell→Rubin→Feynman compute roadmap). Intel, AMD, Qualcomm, and Apple each lose a piece of their differentiated story.

## Vera CPU in production

### Production status + customers

- **Status:** "in full production" (Jensen verbatim).
- **Initial customers named** (six): **Anthropic, OpenAI, SpaceX (xAI), Oracle, CoreWeave, Dell.**
- **Architecture:** 88-core "Olympus" Arm v9.2-A custom core (ARM-licensed).
- **Pairing:** Rubin GPU in the Vera Rubin Superchip.
- **Performance claim:** **~80% faster than x86 equivalents** on agentic AI workloads (NVIDIA-supplied benchmark; verify with independent third-party testing before any decision).
- **TAM framing:** **$200B new CPU TAM** (set at Q1 FY27 print May 20).

### Why the customer roster matters

The six initial customers are the **single most striking data point of the keynote beyond what the user already had**:

- **Anthropic + OpenAI + xAI** — three of the four most-capitalized AI labs in the world. At Anthropic's $900B+ valuation (per [[2026-05-27-anthropic-900B-surpasses-openai]]) and OpenAI's $852B, these are the canonical compute buyers of the cycle. **They are buying NVIDIA *CPUs*, not just GPUs.**
- **Oracle** — the canonical debt-funded AI infrastructure name ([[ai-infrastructure-debt]] thesis). OCI on Vera doubles down on NVIDIA full-stack vs. AMD MI450 / GOOGL TPU alternatives.
- **CoreWeave** — already NVDA-equity-backed (~7% NVDA stake). Vera adds CPU to the existing GPU dependency.
- **Dell** — closes the loop with the **DELL +10% on the day** reaction (PowerEdge XE-series with Vera Rubin = the AI-server channel pull-through).

### Implications for ARM royalty stream

The 88-core "Olympus" custom core is built on **Arm v9.2-A**. Every Vera CPU shipped from H2 FY27 forward pays ARM royalty at the highest-tier v9 rate. **Which means** for [[ARM]]: this is the cleanest royalty-stream pull-through of the cycle. The two bull bullets the ARM page tracks — "Data center penetration accelerating" + "Vera Rubin volume ramps in 2H 2026" — just moved from forecast to commercially-shipping reality. Conviction-upgrade triggers now have cleaner empirical tests: (1) RTX Spark unit ship-rate disclosure 1H 2027; (2) ARM Holdings v9 mix % disclosure in 2027 earnings; (3) MediaTek royalty-rate confirmation.

### Jensen's framing

> *"AI agents will be the largest users of computing. Vera is the first CPU designed for that future — built to run agentic AI at hyperscale with extraordinary performance, efficiency and programmability."*

> Vera CPU is *"our new major growth driver"* — language tier upgrade from "additive" to "primary growth."

## Vera Rubin platform — full production + Taiwan supply-chain doubling

### The under-covered detail of the keynote

Buried under the consumer-product fireworks (RTX Spark / Isaac GR00T) was the single most important data-center signal:

| Metric | Value |
|---|---|
| Status | **Full production**; shipments H2 FY27 |
| Supply chain scale | **2× Grace Blackwell** |
| Factory footprint | **350+ factories across 30 countries** |
| Taiwan factories | **150** (verified by Digitimes) |
| Rack assembly time | **~2 hr (Grace Blackwell) → ~5 min (Vera Rubin)** = **~95% reduction** |
| Mechanism | **Cable-free modular tray design** (snap-together) |
| Platform components | Vera CPU + Rubin GPU + ConnectX-9 SuperNIC + BlueField-4 DPU + networking + storage + software |

### Three implications

1. **H2 FY27 volume capacity is materially larger than the wiki's prior models implied.** If the supply chain has doubled and rack-assembly throughput has compressed ~24×, the binding constraint shifts from "NVDA can't make enough racks" toward **TSMC N3 + HBM + substrates** ([[bottleneck-roadmap]] layers).
2. **Taiwan concentration is now structural.** **150 of 350+ factories in Taiwan = ~43% concentration.** The geopolitical risk vector at the Taiwan strait densifies, not lightens. The TSM bull case validates but the tail-risk overlay sharpens proportionally.
3. **Jensen's framing — *"the largest product launch, probably in the history of Taiwan"*** — maps Vera Rubin to a **decade-scale event for Taiwan's economy**, not just an NVIDIA product cycle. Read-through to TSM / MediaTek / UNIMICRON / all Taiwan suppliers.

## Isaac GR00T H2+ humanoid reference design

### Specs

| Spec | Value |
|---|---|
| Chassis partner | **Unitree** (Shanghai STAR-IPO candidate) — **H2 Plus** model |
| Height / weight | **~6 ft / 150 lb (68 kg)** |
| Body DOF | **31 degrees of freedom** |
| Hands | **Sharpa Wave** tactile five-finger hands — **22 DOF each** |
| Total DOF (body + hands) | **75 DOF** |
| Compute brain | **NVIDIA Jetson Thor** (Blackwell edge SoC, $1,999 / 130W) |
| Availability | **Late 2026** from Unitree |
| First research customers | **Ai2, ETH Zurich, Stanford Robotics Center, UC San Diego ARC Lab** |
| Demonstrated capability | Hands dexterous enough to **deal a pack of cards** |

### Implications for the humanoid OEM stack

- **Unitree** (Hangzhou; Shanghai STAR-IPO candidate) is now confirmed as **NVIDIA's reference chassis-design partner.** This is the structural validation of the Chinese humanoid OEM layer the wiki has been tracking under [[robotics]] / [[humanoid-oems]].
- **Sharpa Wave** — first NVIDIA-blessed end-effector reference design. Not currently in wiki; flag for watchlist.
- **Research-customer roster** is the canonical academic robotics circuit. Reference designs at this footprint compound into the broader humanoid developer ecosystem (~2M Jetson developers per [[2026-05-17-robotics-multi-agent-batch]]).
- **Reference design ≠ product sale.** This is plumbing for the humanoid economy, not 2026 P&L impact. Robotics remains ~1.09% of NVDA revenue per [[2026-05-17-robotics-multi-agent-batch]].

**Which means** for [[NVDA]]: this is the **physical-robot capstone** on the chip + sim + dataset + model stack. NVDA's robotics moat layers now compound to **five**: chips (Jetson Thor) + simulator (Dream Dojo) + dataset (Cosmos 3) + model (GR00T N1.7/N2) + reference humanoid (H2+). Long-duration call option on a $2-12B robotics TAM in 2030 (per BofA in NVDA wiki) is structurally more credible.

## Market reaction

### Three index records on the day

| Index | Move | Close | Status |
|---|---|---|---|
| **S&P 500** | +0.26% | **7,599.96** | Record close |
| **Nasdaq** | +0.42% | **27,086.81** | Record close |
| **Dow** | +0.09% | **51,078.88** | Record close |

**10th consecutive S&P weekly gain in progress** — the streak that started early April 2026 continues; now the longest weekly winning streak since 2020.

### Ticker moves

| Ticker | Move | Read |
|---|---|---|
| **NVDA** | **+5% intraday → near $222** (closed near **$220.67**) | Bull thesis adds three structural moats |
| **DELL** | **+10%** | AI-server channel thesis extends into consumer/SMB AI-PC + Vera Rubin server volume |
| **HP Inc** | **+8%** | RTX Spark OEM partner |
| **QCOM** | **−7%** | Windows-on-Arm socket lost to NVDA; biggest single-name loser |
| **INTC** | **−3%+** | Premium-AI-PC ASP power leg compressed |
| **AMD** | **−3%+** | Ryzen AI Max+ leg compressed; data-center Helios intact |
| **GOOGL** | **−2.51% → $380.34** | AM equity-raise dilution (separate event, not Computex-driven) |
| **MEDIATEK** (2454.TW / MDTKF) | not in wiki | Silent winner; Grace CPU co-design partner; flag for coverage |

### The framework expression of the year

On a single day, the **picks-and-shovels supply side (NVDA + DELL + HP + TSM upstream) rallied** while **the platform funding the buildout (GOOGL via $80B equity raise) sold off**. This is the cleanest single-day expression of the wiki's "supply discipline vs. demand-funding mechanism" framework all cycle. **Which means**: the bull case at the supply side is now **empirically separable** from the funding-mechanism question. The market can simultaneously reward NVDA's structural moats and punish the equity dilution of the customer funding the orders — without the two cancelling out.

## Key claims (and confidence)

| Claim | Confidence | Notes |
|---|---|---|
| RTX Spark is NVIDIA's first ground-up consumer PC superchip | **High** | NVIDIA newsroom + 8+ independent sources confirm |
| 6 OEM partners committed for fall 2026 (Microsoft Surface + Dell + HP + ASUS + Lenovo + MSI) | **High** | All 6 named in NVIDIA + Microsoft joint press release |
| Starting price $1,499 | **High** | Joint NVIDIA + Microsoft Oct 2026 statement |
| TSMC N3 process node | **Medium-high** | Implied by Grace + Blackwell pairing; verify before any decision on TSM pricing model |
| Vera CPU in full production | **High** | Jensen verbatim from keynote |
| Six Vera CPU initial customers (Anthropic, OpenAI, xAI, Oracle, CoreWeave, Dell) | **High** | NVIDIA newsroom + CrnAsia + StorageReview corroborate |
| Vera CPU ~80% faster than x86 on agentic AI | **Medium** | NVIDIA-supplied benchmark; verify with independent third-party |
| Vera Rubin supply chain doubled vs Grace Blackwell; 350+ factories / 30 countries / 150 in Taiwan | **High** | Digitimes + multiple independent confirmations |
| Rack assembly time 2hr → ~5min (~95% reduction) | **High** | NVIDIA-disclosed + cable-free modular tray design verified |
| Isaac GR00T H2+ uses Unitree H2 + Sharpa Wave + Jetson Thor | **High** | NVIDIA newsroom + 6 independent sources |
| 31 DOF body + 22 DOF/hand → 75 DOF total | **High** | TechRadar + Unitree PR confirms |
| Unitree H2+ available late 2026 | **High** | PRNewswire confirms |
| RTX Spark + Vera + GR00T are 3 distinct new revenue lines for NVDA | **High** | Direct read from product roadmap |
| AAPL M-series architectural lead is no longer uniquely Apple's | **Medium-high** | Defensible by 128 GB unified memory at $1,499 price point |
| QCOM lost the Windows-on-Arm socket NVDA is now filling | **High** | QCOM −7% intraday + RTX Spark OEM mix |
| MediaTek is the silent winner not in the wiki | **High** | Grace CPU co-design partner named in NVIDIA press release |
| Vera CPU $200B TAM moves from roadmap to revenue | **High** | Six named customers + "full production" = revenue, not forecast |
| Jensen's "largest product launch in Taiwan history" framing | **High** | Direct quote from keynote |

## Quotes worth keeping

> *"Microsoft and Nvidia are going to reinvent the PC."* — Jensen Huang

> *"This is going to be the new PC. This is the first across the lineup of PC reinvention for 40 years."* — Jensen Huang

> *"This reinvention of the computer is as big of a deal as the reinvention of the phone into what we now know as the smartphone."* — Jensen Huang

> *"AI agents will be the largest users of computing. Vera is the first CPU designed for that future — built to run agentic AI at hyperscale with extraordinary performance, efficiency and programmability."* — Jensen Huang on Vera CPU

> *"[Vera Rubin is] the largest product launch, probably in the history of Taiwan."* — Jensen Huang

> Vera CPU as *"our new major growth driver"* — repeated across multiple Computex sessions

> *"Demand has gone parabolic. Agentic AI has arrived."* — Jensen Huang (carry-over from Q1 FY27 print May 20, re-emphasized at Computex)

> Industry framing (per FourWeekMBA): *"He's building the operating system of the AI era, from the silicon to the software to the robots that run on it."*

## Wiki updates that should be made

- **[[NVDA]]** — Recent developments entry (already drafted on NVDA page). Three structural moats added simultaneously: PC TAM (RTX Spark fall 2026), Vera CPU revenue (full production, 6 named customers), Isaac GR00T physical-robot capstone. Conviction held at **bull/high** (already at ceiling). Stance unchanged.
- **[[ARM]]** — Recent developments entry (already drafted). Cleanest royalty-stream pull-through of the year — both v9 PC SKUs (RTX Spark) and v9 server SKUs (Vera CPU) shipping commercially in H2 2026. Conviction-upgrade triggers now have cleaner empirical tests.
- **[[MEDIATEK]]** *(new page being created in parallel)* — Grace CPU co-design partner for RTX Spark; silent winner of the keynote; promote from "not covered" to full page.
- **[[DELL]]** — Recent developments: +10% close confirms AI-server channel thesis extends into consumer/SMB AI-PC; also named as Vera CPU initial customer (full-stack PowerEdge XE-series read).
- **[[INTC]]** — Recent developments: premium AI-PC ASP power leg compressed (RTX Spark starts at $1,499 with 128 GB unified memory — INTC Lunar Lake/Panther Lake can't match the spec). Foundry-binary part of the bull case intact (Intel 18A unaffected). Stance unchanged at neutral/low.
- **[[AMD]]** — Recent developments: Ryzen AI Max+ leg compressed; Helios MI400/MI450 data-center thesis intact. Stance unchanged at bull/high.
- **[[AAPL]]** — Recent developments: M-series architectural lead is no longer uniquely Apple's — Windows side now has system equivalent at $1,499 with 128 GB unified memory. Bear thesis sharpens marginally.
- **[[TSM]]** — Recent developments: N3 leadership validated across three NVDA product families (data-center Vera Rubin GPU + Vera CPU + RTX Spark PC superchip). Stance unchanged at bull/high. Taiwan concentration risk densifies (150 of 350+ Vera Rubin factories in Taiwan).
- **[[QCOM]]** — Not currently in wiki; −7% on the day on losing the Windows-on-Arm socket. Flag for coverage opening if user wants to track the loser side.
- **[[robotics]] / [[humanoid-oems]]** — Unitree H2+ confirmed as NVDA's reference chassis-design partner; structural validation for the Chinese humanoid OEM layer (Shanghai STAR IPO). Sharpa Wave hands debut — flag for watchlist.
- **[[ai-capex-cycle]]** — Vera Rubin supply chain doubling → H2 FY27 volume capacity materially larger than prior models implied. Anthropic + OpenAI + SpaceX as Vera CPU customers crystallizes demand-pull thesis at the lab tier.
- **[[bottleneck-roadmap]]** — Taiwan concentration at 43% of Vera Rubin factories; rack assembly bottleneck resolved (~95% reduction in assembly time). Binding constraints shift back upstream to TSMC N3 + HBM + substrates.
- **[[nvda-supply-chain]]** — Add MediaTek (Grace CPU co-design), Unitree H2 (humanoid reference), Sharpa (hands), 6 RTX Spark OEMs (Microsoft Surface + Dell + HP + ASUS + Lenovo + MSI).
- **[[overview]]** — June 1 PM section already includes this event (drafted by user).
- **[[index]]** — Add this source summary entry + new MediaTek page entry.
- **[[log]]** — Keynote ingest entry.

## Cross-references

- **[[2026-06-01-googl-80B-equity-raise-berkshire]]** — The AM event of the same day; opposite implication (supply-side rallies / platform sells off). **Cleanest single-day expression of the "supply discipline vs demand-funding mechanism" framework all cycle.**
- **[[2026-05-20-NVDA-Q1-FY27-earnings]]** — Vera CPU $200B TAM was first announced at this print; June 1 Computex confirms full production + six initial customers.
- **[[2026-05-28-DELL-Q1-FY27-earnings]]** — DELL's $51.3B AI backlog now extends into AI-PC + Vera Rubin server volume; +10% on the day validates the channel-extension thesis.
- **[[2026-05-16-jim-fan-nvda-robotics]]** — VLA→WAM paradigm + Dream Dojo simulator context; Isaac GR00T H2+ is the physical-robot reference that completes the stack (chip + sim + dataset + model + reference humanoid).
- **[[2026-05-17-robotics-multi-agent-batch]]** — Robotics is ~1.09% of NVDA revenue; GR00T N2 ships end-2026; this June 1 reveal is a precursor catalyst.
- **[[2026-05-09-dwarkesh-dylan-semianalysis]]** — $90B NVDA-TSMC long-term contract context; >70% of N3 by 2027 reinforced by 3 product families (Vera Rubin + Vera CPU + RTX Spark) all on N3.
- **[[2026-05-27-anthropic-900B-surpasses-openai]]** — Anthropic is named as Vera CPU initial customer; the $900B-valuation lab is buying NVIDIA CPUs not just GPUs.
- **[[2026-05-29-record-week-dell-friday]]** — 9-week streak context; the June 1 + 10th-week-in-progress extends the late-cycle blow-off-top pattern firing alongside structural bull wins.
- **[[2026-05-17-multi-agent-research-batch]]** — TSMC #1-customer status (NVDA 19% of TSMC 2025 revenue); RTX Spark on N3 reinforces this.

## Other June 1 market signals (not separate source summaries — surfaced for context)

- **Marvell (MRVL)** hit a new ATH post Q1 FY27 print last week: rev $2.4B (+28% YoY), Q2 guide $2.7B (+35% YoY), trading ~70x trailing earnings, +130% YTD. Wiki has MRVL on the "not yet covered" list; this is the **second consecutive material print** that argues for promotion. Custom-silicon companion to [[AVGO]] + optical-DSP layer (AWS Trainium 2). *(MRVL coverage in-flight per parallel task queue.)*
- **ServiceNow (NOW)** +8.6% to ~$91.49 on BofA reinstated Buy / $130 PT and an analyst-narrative shift framing NOW as a *beneficiary*, not victim, of agentic AI. Record 40% rally in four sessions. Not in the wiki; AI-software bellwether worth tracking but lower priority than picks-and-shovels.
- **IBM** +9% on bullish analyst initiation. Not in wiki; mainframe + consulting + watsonx + quantum optionality. Surfaced for awareness only.
- **WTI** +5% to $92 on US-Iran peace-talk uncertainty (tentative 60-day ceasefire extension awaiting Trump approval). [[hedging-risk]] / [[commodity-producers]] unchanged.

## Process note

**Was this a tier-1 event or supplementary to the AM GOOGL event?** Honest read: **tier-1, parallel to GOOGL — neither subsumes the other.** The two events together form the cleanest single-day expression of the wiki's "supply discipline vs. demand-funding mechanism" framework all cycle. GOOGL's $80B raise validates the demand side; NVDA's RTX Spark + Vera production + Isaac GR00T validates the supply side.

**Most striking data point beyond what the user already had**: the **Vera Rubin supply chain has doubled relative to Grace Blackwell** — 350+ factories across 30 countries with **150 in Taiwan**, and rack assembly time has compressed from ~2 hours to ~5 minutes (~95% reduction) via cable-free modular trays. This is the under-covered detail because the consumer-product fireworks (RTX Spark + GR00T) dominated press coverage. **Implication**: the H2 FY27 volume capacity is materially larger than the wiki's prior models implied; binding constraint shifts back to TSMC N3 + HBM + substrates ([[bottleneck-roadmap]] layers).

**Contradictions with the user's overview section?** None. The user's framing — three index records + NVDA +2-4% + DELL +10% + INTC/AMD −3%+ + GOOGL −2.51% on AM dilution + "10th consecutive S&P weekly gain in progress" — matches independent press coverage. NVDA close near $220.67 is consistent with the +5% intraday print (24/7 Wall St + Yahoo cite "near $222" midday). **One refinement worth surfacing**: the **QCOM −7%** data point should be added to the overview (largest single-name loser); **MediaTek** (silent winner) is the other addition.

**Recommended stance / conviction changes for user review (flag, don't apply):**

- **[[NVDA]]** — held at bull/high (already at ceiling). Bull case sharpens but conviction already maxed.
- **[[ARM]]** — flag for **conviction upgrade medium → high** *if* RTX Spark unit ship-rate in 1H 2027 confirms the v9 mix-shift narrative. **Don't upgrade today** — wait for empirical test (first reported royalty quarter post-RTX-Spark launch, ~Q4 FY27 ARM earnings).
- **[[MEDIATEK]]** — open new wiki page (in-flight); initial stance bull/medium-high. **Promote from "not covered" to active coverage.**
- **[[INTC]]** — held at neutral/low. Premium-AI-PC bear leg now has clean empirical evidence; foundry-binary intact.
- **[[AMD]]** — held at bull/high (Helios remains structural thesis). Don't downgrade on Ryzen-AI compression alone.
- **[[AAPL]]** — held at bear/neutral. Architectural-lead-compression is marginal; M-series still leads on power efficiency at chip level. Track AAPL Q3 FY26 (July 2026) Mac unit volume for empirical impact.
- **[[QCOM]]** — flag for opening a wiki page if user wants to track the loser side.
- **[[TSM]]** — held at bull/high. Taiwan concentration densifies but doesn't change supply-side monopoly thesis.
- **[[robotics]] / [[humanoid-oems]]** — Unitree H2+ reference design adds canonical Chinese OEM data point. **Don't change conviction** — robotics remains a long-duration call option, not a 2026 revenue line at NVDA scale.

## Sources

- [NVIDIA newsroom: NVIDIA and Microsoft Reinvent Windows PCs for the Age of Personal AI](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark)
- [NVIDIA newsroom: Isaac GR00T Reference Humanoid Robot](https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design)
- [NVIDIA GeForce Computex 2026 announcements (DLSS 4.5, RTX updates)](https://www.nvidia.com/en-us/geforce/news/computex-2026-nvidia-geforce-rtx-announcements/)
- [Tom's Hardware: RTX Spark Superchip](https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory)
- [Tom's Hardware: Spark vs Qualcomm WoA expiration](https://www.tomshardware.com/laptops/nvidia-enters-the-windows-pc-market-with-rtx-spark)
- [HotHardware: RTX Spark Computex 2026](https://hothardware.com/news/nvidia-announces-rtx-spark-at-computex-2026)
- [ServeTheHome: Computex 2026 keynote live coverage](https://www.servethehome.com/nvidia-computex-2026-keynote-live-coverage/)
- [ServeTheHome: Vera Rubin production + DGX Station Windows](https://www.servethehome.com/nvidia-computex-2026-news-bytes-vera-rubin-now-in-production-dgx-station-gets-windows/)
- [StorageReview: NVIDIA Computex 2026 Keynote Recap](https://www.storagereview.com/news/nvidia-computex-2026-keynote-the-rtx-spark-pc-family-dgx-station-and-physical-ai)
- [CNBC: NVIDIA jumps into PCs with Arm-based chip](https://www.cnbc.com/2026/05/31/nvidias-new-chip-to-power-fresh-line-of-windows-laptops-by-dell-hp.html)
- [CNBC: NVIDIA picks Unitree for humanoid robot platform](https://www.cnbc.com/2026/06/01/nvidia-unitree-humanoid-robotics-system-researchers.html)
- [Fortune: Jensen Huang reinventing the PC](https://fortune.com/2026/06/01/jensen-huang-nvidia-pc-reinvention-ai-chips/)
- [Benzinga: NVIDIA "infrastructure company"](https://www.benzinga.com/markets/tech/26/06/52895858/nvidia-infrastructure-company-jensen-huang-computex-2026-ai-factory)
- [TechRadar: NVIDIA-Unitree-Sharpa humanoid](https://www.techradar.com/ai-platforms-assistants/robots-that-can-perform-real-work-nvidia-unitree-and-sharpa-are-forming-a-super-group-to-make-the-most-capable-humanoid-robots-yet-with-jensen-huang-promising-a-meaningful-step-towards-frighteningly-capable-robots)
- [Unitree H2+ PRNewswire](https://www.prnewswire.com/news-releases/unitree-announces-h2-plus-an-nvidia-isaac-gr00t-reference-humanoid-robot-for-academic-research-302786748.html)
- [Cryptobriefing: Vera Rubin full production + 95% assembly speed](https://cryptobriefing.com/nvidia-vera-rubin-full-production/)
- [SiliconANGLE: NVIDIA ramps Vera Rubin production](https://siliconangle.com/2026/06/01/nvidia-ramps-production-vera-rubin-foundation-next-generation-ai-factories/)
- [Digitimes: 150 Taiwan suppliers powering Vera Rubin ramp](https://www.digitimes.com/news/a20260601VL216/nvidia-rubin-taiwan-production-ceo.html)
- [Yahoo Finance: NVIDIA Rallies 5% on RTX Spark](https://finance.yahoo.com/markets/stocks/articles/nvidia-rallies-4-rtx-spark-155423133.html)
- [24/7 Wall St: NVDA +5%, QCOM −7%](https://247wallst.com/investing/2026/06/01/nvidia-rallies-4-on-rtx-spark-launch-as-qualcomm-falls-7-on-ai-pc-competition-fears/)
- [Invezz: Intel, AMD, Qualcomm slide on RTX Spark](https://invezz.com/en-ae/news/2026/06/01/intel-amd-and-qualcomm-slide-as-nvidia-targets-ai-pc-market-with-rtx-spark-chip/)
- [Crnasia: Three key takeaways from NVIDIA Computex 2026](https://www.crnasia.com/news/2026/components-and-peripherals/three-key-takeaways-from-nvidia-at-computex-2026)
- [ExplainX: Computex 2026 complete recap (Nemotron 3 Ultra, Cosmos 3, RTX Spark)](https://www.explainx.ai/blog/nvidia-computex-2026-nemotron-3-ultra-complete-recap)
- [FourWeekMBA: 6 chips, PC, Robot — End of an Era](https://fourweekmba.com/nvidia-computex-2026-five-layer-strategy/)
- [TechFinitive: 3 things businesses need to know](https://www.techfinitive.com/3-things-businesses-need-to-know-from-nvidias-computex-2026-keynote/)
- [The Register: Grace Blackwell to PC](https://www.theregister.com/systems/2026/06/01/nvidia-recasts-gb10-superchip-in-bid-for-high-end-pc-market/5249068)
