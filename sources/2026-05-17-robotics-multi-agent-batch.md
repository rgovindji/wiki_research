---
date: 2026-05-17
type: multi-agent-research
publisher: Anthropic Haiku subagents via Claude Code Agent tool
url: composite — see per-agent URLs below
touches: [TSLA, MP, OUST, ALGM, AMBA, VPG, AMBA, robotics, humanoid-oems, bottleneck-roadmap, NVDA, MSFT]
---

# Robotics Deep-Dive Multi-Agent Batch (May 17, 2026)

User requested "best research base for AI robotics" via multi-agent. Six parallel Haiku subagents spawned to research:
- A: Tesla Optimus production state
- B: Figure AI funding + deployments
- C: Apptronik / Agility / Boston Dynamics
- D: Skild / Physical Intelligence / 1X / Sanctuary (foundation-model layer)
- E: Chinese humanoid suppliers + Foxconn manufacturing
- F: NVIDIA GR00T / Isaac / Cosmos ecosystem

## Agent A: Tesla Optimus production state — KEY FINDING

### Production timing finally concrete
- **Gen 3 production begins July-August 2026** at Fremont (slow initial ramp: "dozens or hundreds" not thousands)
- **2026 unit target: 50K-100K** (vs 10K originally targeted for 2025; actual 2025 number unknown, far lower)
- **1M units/year run-rate by late 2026** targeted at Fremont
- **Giga Texas factory (10M/year capacity) announced for 2027**
- **First external commercial customers: late 2026** — Tesla is currently behind Figure (already at BMW production line)
- **B2B early pricing >$100K** per unit; B2C target $20-30K untested

### Chip supply (AI5 timing matters)
- **AI5 chip taped out April 2026**; dual-sourced TSMC + Samsung Texas
- **AI5 ships in Optimus FIRST**, then vehicles (robotaxi lower priority)
- **Samsung Taylor Texas fab full operational by EOY 2026** (risk of slip to early 2027)
- **AI6 tape-out scheduled December 2026**

### Component supplier read-throughs (specific names + dollars)
- **MP Materials**: each Optimus needs **3.5kg NdFeB magnets**; China controls 85% refining
- **🔥 Musk confirmed May 2026: Optimus production HIT BY China rare earth export controls; seeking licenses** — MP Materials direct beneficiary
- **Sanhua: $685M order** for thermal/control systems
- **Harmonic Drive (incl. Suzhou Green Harmonic, 25% share)**: expanding to 500K units/year by 2026
- Actuators: Nidec, Nabtesco, Rockwell Automation; **56% of BOM** from these names
- Custom Tesla designs for 28-40 joint modules

### Reality-check data
- **Prediction markets: ONLY 6% probability of Optimus consumer sales by June 2026** — extreme skepticism
- **Tesla 2026 FCF forecast: -$5.1B** (vs $38.8B 2024)
- **ARK 2029 target $2,600 has ZERO Optimus upside baked in** (Cathie Wood: "may be too conservative on humanoid" — but not yet modeling it)
- **Figure AI is operationally ahead** of Tesla — Figure 02 delivered **30K+ BMW X3 vehicles in 11-month pilot** (Spartanburg Nov 2024-Nov 2025); Tesla's internal Optimus still "primarily for learning" per Q4 2025 call

### Wiki implications
- [[TSLA]] bear stance **reinforced** — Optimus inflates valuation without near-term revenue; Q1 capex surge + negative FCF + zero external customers + 178x 2026 EPS
- [[MP]] thesis **strengthens** with hard 3.5kg/unit number + May 2026 Musk-confirmed China constraint
- [[OUST]] / [[ALGM]] / [[AMBA]]: wait for July 2026 commercial Optimus units for sensor demand validation; Figure BMW win already validates broader humanoid sensor demand

## Agent B: Figure AI — Operationally Ahead

### Funding state May 2026
- **$39B post-money** (Series C Sept 2025, led by Parkway VC; participants NVDA, Intel Capital, Qualcomm, LG Tech)
- **No Series D announced**; runway ample
- **IPO likely 2027-2028 at earliest**

### 🔥 Commercial deployments (real production data)
- **BMW Spartanburg (flagship win)**: Figure 02 in 11-month pilot Nov 2024-Nov 2025; **10-hour daily shifts**; **30,000+ BMW X3 vehicles built**
- **Pilot continues through summer 2026** + **expansion to Leipzig plant planned**
- **Production rate: 240 units/month (April 2026)**, up from 150 total in 2025
- **Target: 100,000 units over next 4 years** via BotQ high-volume facility (12K units/yr initial capacity)
- **Boeing 777X line: NOT CONFIRMED** in May 2026 search — appears speculative
- **Robot-as-a-Service pricing: ~$1,000/month lease**

### Tech stack
- **F.02 (Figure 02)**: 168 cm / 70 kg; 5-hour battery; Helix VLA model running at **200 Hz** control loop
- **F.03 launched Oct 2025**: 9% less mass; **upgraded cameras (2x frame rate, 60% wider FOV)**; 3-gram tactile sensitivity; engineered for high-volume manufacturing
- **Helix 02 (latest)**: full-body autonomy update
- **Severed OpenAI partnership Feb 2025** — "in-house AI breakthrough" claim; all AI now proprietary

### Public-market read-throughs
- **NVIDIA**: direct Series C investor; Figure uses **Isaac platform** for simulation + Helix training; durable compute demand
- **Microsoft Azure**: cloud compute for Figure model development + data pipelines; broader "physical AI infrastructure" push from GTC 2026
- **Qualcomm + LG Tech**: Series C investors with strategic angles (chips + display/component)
- **Intel Capital**: also Series C — slight bull data point for [[INTC]]

### Moat assessment (Agent verdict: moderate-to-fragile)
- BMW exclusivity contractual but **not proprietary** — no disclosed patents/manufacturing secrets that differentiate Figure from Apptronik or Boston Dynamics
- First-mover RaaS revenue real (~$50M ARR estimated, unverified)
- Tesla's sub-$30K target + Boston Dynamics' Hyundai OEM supply chain are structural threats
- **Risk: 18-month Figure lead closes by 2027-2028 as Apptronik/Xiaomi/Tesla deliver competitive VLMs**

### Investability summary
- **Best wiki proxy: [[NVDA]] (direct investor + Isaac platform user)**
- Secondary: [[MSFT]] (Azure compute infra)
- Tertiary: [[INTC]] (Intel Capital co-investor — small stake)
- No direct public exposure beyond IPO 2027-2028+

## Agent C: Apptronik / Agility / Boston Dynamics

### Apptronik (private, Mercedes/NVIDIA partner)
- **$5B valuation** — Series A extension Feb 2026 ($520M), total Series A $935M
- **New backers**: Google, Mercedes-Benz, AT&T Ventures, John Deere, Qatar Investment Authority
- **Apollo runs on NVIDIA Jetson AGX Orin (275+ TOPS)**
- **Customers**: Mercedes-Benz factories + GXO Logistics; **no new OEMs (Honda, BMW, Ford, GM) announced**
- **Manufacturing partner: Jabil (US-listed [[JBL]])** — direct read-through
- 2026 roadmap: commercial-scale deployment; 2027: fine manipulation + multi-step tasks
- **Alpha angle**: Google's repeat investment signals long-term confidence in AGI agent embodiment

### Agility Robotics (private, Amazon-backed)
- **$1.75-2.12B valuation**; Series C $400M (Jun-Sep 2025, tranched reports)
- **Amazon $150M stake**
- **Customers**: Amazon (narrow "tote recycling" R&D pilot only — not broad warehouse deployment), Toyota (Feb 2026 pilot signed), Mercado Libre (Dec 2025), GXO, Schaeffler
- **RoboFab Salem Oregon**: targets 10,000 units/year capacity; **currently <1,000 units shipped**
- CEO Peggy Johnson: Digit "interoperate near humans" by mid-2026
- **Alpha angle**: Amazon's cautious narrow pilot vs hype suggests technical hurdles persist

### Boston Dynamics (Hyundai 005380.KS subsidiary)
- **Atlas Gen 3 unveiled CES 2026**; **entire 2026 production reserved for Hyundai RMAC + Google DeepMind**
- **Hyundai $26B US investment**; 30K units/yr factory by 2028 (Savannah Metaplant); deployment 2028-2030
- **Boston Dynamics revenue: 150.1B won (~$100M USD)**; **loss 528.4B won = 3.5x revenue burn**
- **Internal valuation $20-21B** (24x since 2021 acquisition)
- **Nasdaq IPO expected early 2027** — appears promotional given burn rate
- **🔑 Atlas uses Google DeepMind Gemini Robotics models (NOT GR00T)** — important competitive datapoint for NVDA framework

### US investability
- **Direct**: None (all private/subsidiary); BDX IPO expected early 2027 but appears overhyped at $20B given 3.5x burn
- **Indirect**: Hyundai ADR (HMG) for Boston Dynamics; NVIDIA Jetson Orin supply (Apptronik); [[JBL]] manufacturing partner (Apptronik)
- **Under-covered insight**: Amazon's narrow Digit pilot CONTRADICTS "soon at scale" narrative

## Agent D: Robotics foundation models (Skild / π / 1X / Sanctuary)

### Skild AI (Pittsburgh, commercial leader)
- **$14B valuation** Series C Jan 2026 ($1.4B raised)
- **$30M+ ARR** — first credible commercial revenue at the foundation-model layer
- **Deployed across Foxconn/NVIDIA, ABB Robotics, Universal Robots**
- Closed-model approach (vs π open-source)
- Investors: Lightspeed, Coatue, SoftBank, NVIDIA, Bezos, CMU spinout

### Physical Intelligence (π — Levine + Hausman founders)
- **$600M Series B late 2025**; in talks for **$1B raise at $11B valuation**
- **π0.6 released Feb 2025** using **Google Gemma 3 4B backbone + action expert**
- **Open-source code/weights**; **1000+ citations in 12 months** for OpenVLA/Pi0 family
- No named commercial customers yet — capability scaling + ecosystem seeding

### 1X Technologies (Norwegian, OpenAI portfolio)
- **Neo pre-orders at $20K**; **$499/mo subscription model**
- **🔑 CRITICAL: 2026 units rely on human teleoperators viewing inside homes — NOT autonomous yet**
- Series C $100M+ from OpenAI
- Eve commercial robot also in pipeline

### Sanctuary AI (Vancouver, stalled)
- **Gen-8 Phoenix** designed for production cost reductions
- ~$140M raised total
- **Magna partnership** (strategic equity + contract manufacturing)
- **Candidate for acquisition / consolidation** per agent verdict

### Architecture divergence + "Linux of robotics"
- **Closed/proprietary**: Skild (platform), Tesla Optimus (vertical), 1X (hybrid via OpenAI)
- **Open/ecosystem**: Physical Intelligence (Gemma-based VLA), NVIDIA GR00T N2 (open commercial licensing)
- **π0's open Gemma-based stack is the most likely commoditizer** — could crater Skild $14B valuation thesis
- **11+ commercial VLA deployments by Q1 2026** signals moat narrowing

### Public-market read-through
- **NVDA**: direct investment in Skild; GR00T N2 open release
- **MSFT**: OpenAI's 1X backing
- **Hyundai (HMG)**: Boston Dynamics ownership
- **Magna (MGA)**: Sanctuary AI equity + manufacturing partner

## Agent E: China humanoid suppliers + Foxconn

### Chinese humanoid OEMs (private + listed)
- **Unitree Robotics (Hangzhou)** — world's TOP humanoid seller 2025 — **just filed Shanghai STAR IPO at ~$610M raise**; **5,500 units delivered 2025** (more than Tesla + Figure + Agility); **targeting 20,000 in 2026** at $13,500-$73,900 price range
- **AgiBot (Shanghai)** — unicorn; **Xi Jinping visited factory April 2025** (gov backing signal); **5,000 robots produced by end-2025**; targeting multi-fold 2026 growth
- **UBTECH (9880.HK listed)** — Walker S/S2 mass production; **800M yuan+ orders (2025)** at BYD + Geely; industrial focus
- **🔑 XPENG Motors (XPEV — US-listed)** — committed **¥100B (~$13.7B) to IronMan/IRON humanoid**; targeting **mass production late 2026 with 1,000+ units/month**; former NVIDIA Android manager leads XPENG robotics
- **Fourier Intelligence**: GR-2 (53 DOF) targeting 2026 mass production

### Chinese component supply chain (CRITICAL choke points)
**China controls 70-80% of humanoid joint/actuator supply.**

| Ticker | Listing | Role | Data point |
|---|---|---|---|
| **Leader Drive** | 300695.SZ | Harmonic reducers | **30-40% China share**; net profit DOUBLED 2025 to 124M yuan (+47% rev); founders now billionaires; expanding US JV with Minth |
| **Sanhua Intelligent Controls** | 002050.SZ | Actuators (Tesla supplier) | **30% of HK$1.19B IPO** allocated to humanoid actuators; **~70% Tesla Optimus actuator module share** confirmed; bionic actuator TAM $8.7B by 2029 |
| **Inovance Technology** | 300124.SZ | Servo drives / motion control | 13-15% 2026 revenue growth |
| **Estun Automation** | 002747.SZ | Industrial robot arms | Launched Codroid 02 (31 DOF, 5kg) June 2025 |

### Foxconn (Hon Hai, 2317.TW / HNHPF OTC)
- **Unveiled industrial humanoids at NVIDIA GTC 2026** — confirmed humanoid manufacturing capability
- Expanding Vietnam/Mexico production
- HNHPF ~$11.38/share; 2025 revenue +18%, earnings +24%
- Rumored partnerships with Apple/Nvidia/OpenAI (unconfirmed)

### US investor access
- **Direct A-share access blocked** (requires QFII or Stock Connect)
- **Hong Kong-listed accessible**: UBTECH (9880.HK)
- **Taiwan-listed accessible**: Foxconn (HNHPF OTC)
- **A-share ETF proxies**: **KSTR (KraneShares STAR Market), KOID (KraneShares Humanoid Robotics)** — both give exposure to Leader Drive + Inovance + Estun
- **US market proxies**: [[ON]] (Tesla supplier), [[NVDA]] (chip content)

## Agent F: NVIDIA GR00T / Isaac / Cosmos

### Platform state May 2026
- **GR00T N1.7** in early access with **commercial licensing** (production-ready)
- **GR00T N2 ships end-2026** (world action model based on Dream Zero); **#1 on RoboArena benchmarks**
- **Partners**: ABB, FANUC, KUKA, Universal Robots, Franka Robotics, AGIBOT, Skild AI, YASKAWA, **Figure AI**

### Public company integrations
| Company | Listing | NVDA partnership status |
|---|---|---|
| **XPENG** | XPEV | **Using Isaac Sim/Lab for humanoid training**; 5th-gen robot (Turing AI chip); mass-prod H2 2026 |
| **Boston Dynamics** | Hyundai sub | **NOT GR00T — uses Google DeepMind Gemini Robotics** |
| **Foxconn** | HNHPF | **Confirmed at NVIDIA GTC 2026** for industrial humanoid; not explicitly robotics-named |

### Financial impact on NVDA P&L (today — minimal)
- **Automotive segment (includes robotics) = $2.35B = 1.09% of total NVDA revenue FY26** (+6% YoY in Q4; ~flat growth)
- **Data Center = $197.3B = 91.5% of revenue** (robotics dwarfed)
- **Edge chips**: **Jetson Thor (Blackwell) at $1,999 / 130W**; **2M developers on Jetson; 7K customers on Orin**
- **No GR00T licensing revenue disclosed** — likely embedded in partnerships, not separated

### Cosmos + Dream Dojo
- **Cosmos: 2M+ downloads**, commercially licensable, open-source
- **Cosmos Policy**: 98.5% success on LIBERO sim; 67.1% on RoboCasa; 12.5% improvement bimanual real-world
- **Dream Dojo: open-sourced Feb 2026**; trained on **44,711 hours human video** (15x prior scale); runs 10.81 FPS; **Pearson r=0.995 correlation with real-world success**
- Customers: Lightwheel, Moon Surgical, Skild AI, Uber (AV), Waabi (sim)

### Market sizing
- **Bank of America projects 90K humanoid units shipped 2026 → 1.2M by 2030**
- Unitree alone: 5.5K in 2025; targeting 20K in 2026 — already outpaced Tesla, Figure, Agility combined

### Strategic threat: open vs closed
- **GR00T proprietary** — NVIDIA classic moat strategy
- **Cosmos open-source** — fragments partner loyalty but seeds ecosystem
- **Levine's π0 uses Google Gemma** — open-source threat to GR00T

## Cross-cutting investment implications

### Wiki position updates needed
- **[[NVDA]]**: GR00T N2 catalyst end-2026; Automotive segment still only 1.09% of revenue (don't overweight robotics in valuation); Jetson Thor product detail
- **[[TSLA]]**: Bear stance reinforced — prediction markets at 6% probability Optimus consumer June 2026; Figure operationally ahead
- **[[MP]]**: Direct hard-data validation — 3.5kg NdFeB per Optimus + Musk-confirmed China constraint May 2026
- **[[JBL]]**: Apptronik manufacturing partner — new direct robotics exposure beyond AI servers
- **[[robotics]]** (sector): massive update needed; Unitree IPO accessible only via KSTR/KOID; commercial deployment data
- **[[humanoid-oems]]**: deep update with valuations + production rates for all major OEMs
- **New page candidates**: [[XPEV]] (humanoid pivot at scale, US-listed, ¥100B commitment) — should create

### Most-actionable new public-market plays surfaced
1. **XPEV** (Xpeng Motors) — US-listed; ¥100B humanoid commitment; late 2026 mass production target; underexposed in US market
2. **HNHPF** (Foxconn ADR) — manufacturing layer beneficiary; GTC 2026 humanoid showcase
3. **MGA** (Magna) — Sanctuary AI manufacturing partner + auto-supplier diversification
4. **HMG** (Hyundai ADR) — Boston Dynamics ownership; 30K units/yr factory by 2028
5. **KOID + KSTR** ETFs — diversified China robotics-supply-chain exposure (Leader Drive + Inovance + Estun)

### Wiki updates made (next step)
- [[robotics]] sector page — comprehensive rewrite with valuations, production rates, customer wins, supplier mapping
- [[humanoid-oems]] theme — deepened with private valuations
- Created [[XPEV]] stub
- Patched [[TSLA]], [[MP]], [[JBL]], [[NVDA]], [[OUST]], [[ALGM]], [[AMBA]]
- [[us-china-relations]] — Unitree IPO + Stock Connect access
- [[bottleneck-roadmap]] — rare earth confirmation
