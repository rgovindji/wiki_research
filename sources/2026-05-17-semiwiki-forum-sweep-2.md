---
date: 2026-05-17
type: forum-sweep
publisher: SemiWiki Forum (multiple threads)
url: https://semiwiki.com/forum/whats-new/posts/
touches: [TSM, AAPL, INTC, NVDA, GOOGL, MU, us-china-relations, ai-capex-cycle, bottleneck-roadmap, datacenter-construction]
---

# SemiWiki Forum Sweep #2 (May 17 2026) — Trump-Xi-Jensen, MRC Supercomputer, TSMC-Apple Modem, TSMC Board Resolutions

Four threads from SemiWiki forum sweep #2, combined into one source. Each thread referenced individually below.

## Thread A: Trump lands in China for Xi summit with Nvidia CEO in tow
**URL**: https://semiwiki.com/forum/threads/trump-lands-in-china-for-xi-summit-with-nvidia-ceo-in-tow.25098/
**Started**: May 13 2026 by Daniel Nenni (5 posts). Participants: Xebec, TonyGet, SiliconBruh, KevinK, BlueOne, Barnsley.

### Key facts
- Trump's two-day Beijing summit started May 13, 2026 — first US president visit to China in nearly a decade
- **CEO entourage** (officially): Elon Musk, **Jensen Huang (NVDA)**, **Tim Cook (AAPL)**, Larry Fink (BLK), Stephen Schwarzman (BX), Kelly Ortberg (BA), Brian Sikes (Cargill), Jane Fraser (Citi), Larry Culp (GE), David Solomon (GS), **Sanjay Mehrotra (MU)**, Cristiano Amon (QCOM)
- **Conspicuously absent: Lip-Bu Tan (INTC)** — flagged on forum as notable given Intel just got 9.9% gov stake and Apple diversification rumor
- Bessent had **3 hours of preparatory talks** with Chinese officials in South Korea; Xinhua called "candid, in-depth and constructive"
- Agenda beyond trade: **Iran war, US arms sales to Taiwan, China-Iran intermediation**
- Nvidia angle: still seeking regulatory permission to sell H200 chips to China; Trump asked Huang "at the last minute" to join (boarded Air Force One during Alaska refueling)

### Stock moves (per forum member tabulating ~week ending around May 16)
| Ticker | 1-week | Other |
|---|---|---|
| **INTC** | **-16.61%** | but +200% YTD |
| **QCOM** | **-13.24%** | |
| **MU** | **-8.48%** | |
| **BA** | -7.91% | |
| **BX** | -4.35% | |
| **C** | -1.48% | |

Forum verdict (siliconbruh999): *"Doesn't seem like the visit did much .. ?"*

### Investment implications
- **Negative summit read**: market voted *against* the trip being a positive catalyst for the named CEOs' companies
- **INTC**: -16.61% one-week drawdown is meaningful for our brand-new [[INTC]] page; the "+114% April" is being partially given back. **+200% YTD** is the longer-frame number — much bigger than the +114% April we cited
- **MU**: -8.48% post-trip despite CEO attendance — China DRAM regulatory or supply-chain concerns?
- **QCOM**: -13.24% is steep — likely reflects market pricing in Apple's confirmed C2 modem swap-out (see Thread C below). QCOM losing Apple modem business is a major revenue headwind
- **Lip-Bu Tan's INTC absence**: politically curious given INTC's strategic moment. Could signal Tan's focus is elsewhere (domestic / Lazo / Terafab execution) — or that Treasury didn't want the 9.9%-owned company at the table

## Thread B: MRC supercomputer networking, announced by OpenAI and others
**URL**: https://semiwiki.com/forum/threads/mrc-supercomputer-networking-annonced-by-openai-and-others.25100/
**Started**: by NY_Sam2. Small thread (~7 posts).

### Key facts
- New AI networking standard "MRC" announced by OpenAI + others
- **Google notably absent** from MRC consortium — already deep into proprietary optical circuit switching (OCS) with **Apollo/Palomar hardware** generations
- BlueOne forum quote: *"Google might be missing because they are all in on optical switching (OCS) already with their Apollo/Palomar hardware and beyond"*
- KevinK forum quote: *"By investing in a proprietary architecture Google is far ahead of anything the industry groups can kludge together, for functionality and efficiency. Datacenter networking has become a deep morass of inefficient legacy layers built on top of industry standards which won't evolve to meet the needs of commercial interests. MRC is a classic example."*
- Technical context: *"AI workloads, especially on GPUs, are really allergic to congestion of any kind (it causes expensive stalls in SIMD processing), and data transfer sizes have become huge, so 'spraying' packets across links (like Ultra Ethernet) and multipath connections (like MRC) are all the rage."*

### Investment implications
- **[[GOOGL]] networking moat validated**: Apollo/Palomar OCS is one generation ahead of industry consortium efforts (MRC, Ultra Ethernet). This is a network-effect / efficiency moat that compounds with each AI training generation
- **[[AVGO]]**: MRC participation as a switch/silicon supplier; sells "kludge" infrastructure that Google has obsoleted internally — but the *non-Google* hyperscaler base still buys it
- **Optical interconnect cohort ([[COHR]] / [[LITE]] / [[FN]])**: indirect read — every AI network standard pushes more optical content per rack; immune to which standard wins

## Thread C: TSMC wins major modem chip order from Apple
**URL**: https://semiwiki.com/forum/threads/tsmc-wins-major-modem-chip-order-from-apple.25102/
**Started**: by Daniel Nenni. Participants: Nenni (5), rinoali (2), others.

### Key facts
- **Apple outsourcing all major 5G modem chip orders to TSMC on N2 (2nm)**
- Apple's self-developed modem (next-gen successor of "C1", presumably **C2**) replaces Qualcomm modems starting next year (2027)
- **C2 features**: full millimeter wave support (improvement over Sub-6 only); satellite communication
- **Hundreds of millions of units** anticipated across iPhone, iPad, Apple Watch
- Backend wafer testing: TSMC's subsidiary **Jingcai (3374, Taiwan-listed)** **urgently purchased 600 testing machines** to handle the Apple modem volume
- **TSMC's back-end wafer testing capacity is "almost fully booked"** with AI demand from NVDA, GOOGL, MSFT, META, AMD — Apple modem stretch requires capacity expansion
- Industry insiders on Apple-Intel rumor: *"Even if Apple does transfer some chip orders to Intel, it does not mean that it will abandon TSMC."*

### Daniel Nenni's verdict (verbatim)
> "Who is the media kidding here. What foundry at 2nm has the capacity and yield to support Apple's iPhone orders? I can only think of one...... TSMC!!!!! Not to mention trust with that important of a chip."

### Forum technical nuance (rinoali)
> "I think this news just mention Baseband designed by Apple, not A21. Intel maybe will get some shares of A21 just like TSMC+Samsung for iphone AP. Apple will select BB+AP design instead of integrated in one SoC."

**Interpretation**: Apple is doing **modem-disaggregation strategy** — own Baseband (BB, on TSMC N2) + Application Processor (AP, possibly multi-foundry sourced). Intel could get *some* A21 share at best, not the marquee modem work.

### Investment implications
- **[[TSM]] bull case strengthens**: even with Apple-Intel diversification narrative, marquee Apple work (5G modem on N2) stays at TSMC. **Which means** Apple deprioritization at TSMC is *real* (Apple loses share to AI customers) but TSMC's wallet share *of remaining Apple workloads* stays high
- **[[AAPL]] strategy clarified**: own-modem + AP-multi-source = disaggregated design. Doesn't change the bear thesis (smartphone volumes, TSMC priority) but adds execution complexity
- **[[INTC]] downside reframe**: even if Apple-Intel diversification is real, Intel gets *secondary* AP shares (Samsung-like role), not flagship modem. The Kuo lifecycle from [[2026-05-17-semiwiki-kuo-apple-intel]] may overstate Intel's eventual Apple wallet share — patches [[INTC]] page bear case
- **[[QCOM]]**: confirmed losing Apple modem business in 2027. Likely explains the -13.24% week move from Thread A above
- **TSMC backend testing capacity "fully booked" with AI**: independent confirmation of [[bottleneck-roadmap]] cleanroom-space thesis. Apple modem stretch requires capacity expansion — read-through to [[TER]] (chip-final test) and adjacent test equipment

## Thread D: TSMC Board of Directors Meeting Resolutions
**URL**: https://semiwiki.com/forum/threads/tsmc-board-of-directors-meeting-resolutions.25111/
This is the **primary-source TSMC press release** that Daniel Nenni's earlier article ([[2026-05-15-semiwiki-tsmc-tool-orders-capex]]) was based on.

### Key facts (verbatim from TSMC release)
- **Q1 2026 consolidated revenue: NT$1,134.10 billion**
- **Q1 2026 net income: NT$572.48 billion**
- **Q1 2026 diluted EPS: NT$22.08**
- **Q1 2026 cash dividend: NT$7.0 per share** (record date Sep 22, 2026; payment Oct 8)
- **Capital appropriations: approximately US$31,284.30 million** ("$31.3B") for advanced technology capacity + fab construction + facility systems
- **🔥 Capital injection into TSMC Arizona: not more than US$20 billion** ← MAJOR NEW DATA POINT
- Promotions: Jonathan Lee → SVP Corp Planning; Y.H. Wu → VP Quality & Reliability; Y.C. Ku → VP R&D Nano Patterning Technology; Span Lu → VP Operations / Intelligent Manufacturing Center

### Implications of the $20B Arizona injection
- **Roughly 1/3 of TSMC's full-year 2026 CapEx ($56-60B) earmarked for Arizona alone** — much more aggressive than prior public posture
- **Direct read-through to [[datacenter-construction]] cohort**: [[FIX]] / [[EME]] / [[PWR]] all have material Arizona / SW exposure (also [[AMKR]] Peoria campus)
- **Equipment vendors** ([[AMAT]] / [[KLAC]] / [[LRCX]] / [[ASML]]) — Arizona installation = US-located equipment installs, higher-margin service revenue
- **US-foundry / "Made in America" semis narrative**: TSMC physically moving leading-edge capex into US matters politically and reduces Taiwan-strait tail risk for [[NVDA]] etc.
- **Y.C. Ku VP promotion (Nano Patterning Technology)**: signals continued R&D escalation around EUV-adjacent areas (relevant to [[ASML]] thesis)

## Thread E: TSMC to Sell 8.1% of Vanguard International Semiconductor (companion)
**URL**: https://semiwiki.com/forum/threads/tsmc-to-sell-8-1-of-vanguard-international-semiconductor.25112/
Brief — primary source release; no forum discussion of note.

### Key facts
- TSMC selling **up to 152.0 million common shares (~8.1%) of VIS** via block trade to financial institutions
- TSMC current stake: ~27.1% → post-sale ~19%
- "Strategic relations" with VIS preserved (interposer production outsourcing + GaN tech licensing)
- TSMC ceased VIS board representation June 2024
- Stated rationale: *"focus its resources on core business activities"*

### Investment implications
- **Capital recycling**: TSMC monetizing legacy mature-node stakes to fund Arizona $20B + advanced-node CapEx
- VIS = mature-node foundry (not AI-relevant); divestiture confirms TSMC's narrowing focus on leading-edge
- Watch for additional legacy-stake divestitures as TSMC funds the 2027 cleanroom-space expansion per [[bottleneck-roadmap]]

## Wiki updates made
- Patched [[TSM]] — board resolution primary data + $20B Arizona + VIS divest
- Patched [[INTC]] — -16.61% week post-Xi summit; Lip-Bu Tan absent; modem stayed at TSMC (Apple diversification gets reduced)
- Patched [[AAPL]] — modem-disaggregation clarification (BB on TSMC N2, AP multi-source)
- Patched [[GOOGL]] — Apollo/Palomar OCS validated as one generation ahead of MRC consortium
- Patched [[us-china-relations]] — Xi summit market read + INTC/QCOM/MU post-trip moves
- Patched [[datacenter-construction]] — TSMC Arizona $20B injection read-through to FIX/EME/PWR
