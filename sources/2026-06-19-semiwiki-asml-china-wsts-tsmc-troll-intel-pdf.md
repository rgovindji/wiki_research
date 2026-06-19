---
date: 2026-06-19
type: article
publisher: SemiWiki (forum + Nenni blog) — incremental scan
url: https://semiwiki.com
raw_path: n/a (scan extracts)
touches: [ASML, TSM, INTC, MU, semiconductors, ai-bubble-debate, us-china-relations, bottleneck-roadmap, overview]
---

# SemiWiki daily sweep (Juneteenth holiday) — ASML-EUV-in-China allegation, WSTS $1.5T memory blowout, TSMC patent-troll ITC case, Intel-PDF yield pact

US markets closed for Juneteenth (no tape, no letter). SemiWiki scan returned 6 net-new items; this is a genuinely substantive long-tail day, so all are captured.

## TL;DR
- **US Commerce Secretary Lutnick privately told ASML leaders he believes one of their EUV machines may have reached China in breach of export controls; ASML flatly denies it has ever shipped an EUV tool to China.** A new, unproven national-security overhang on Europe's most valuable company.
- **WSTS Spring-2026 forecast: global semis +90% to $1.51T in 2026, with Memory surging ~+250% y/y to >$800B (Logic +37%); 2027 +27% to ~$1.9T.** The single hardest-sourced confirmation yet that the cycle is overwhelmingly a memory-ASP event.
- **TSMC under USITC investigation on a patent complaint from two Irish IPValue/Vector-Capital shells (Longitude Licensing, Marlin Semiconductor) that Taiwan's own IP office publicly calls "patent trolls."** ALJ preliminary ruling expected this month; USITC final decision possibly October.
- **Intel + PDF Solutions (PDFS) yield partnership detailed** — the #1 yield-analytics house helping Intel close 18A/18A-P yield, the leg of the foundry turnaround that actually gates external revenue.

## Key facts
- **ASML / EUV-in-China (Bloomberg via SemiWiki):** Lutnick raised the concern in recent private meetings with ASML senior leaders. US officials say they have evidence ASML is "not acting in good faith" — e.g. exports to China of gear specifically related to EUV tools — but declined Bloomberg's requests for that evidence and would not say whether they had seen an actual EUV system in China. ASML's pushback: EUV tools are "the size of a school bus," made in tiny quantities, and require constant on-site ASML upkeep, so one could not quietly operate in China; the company "has never shipped an EUV machine to China" and "enforces controls strictly." The Dutch foreign ministry says it enforces EUV restrictions "very strictly." Context: China's lack of EUV is "the single toughest constraint" on Huawei.
- **WSTS Spring 2026:** 2026 market $1.51T (+90% y/y). **Memory ~+250% y/y to >$800B** — "overwhelmingly" the driver. Logic +37%. Micro +20%, Analog +10%, Discretes +8%, Sensors/Opto +3%. Regions: Americas +112% (more than doubles), Asia-Pac +87%, Europe +58%, Japan +28%. **2027: +27% to ~$1.9T**, memory again leading (+32%), logic +27%.
- **TSMC ITC case (Taipei Times via SemiWiki):** Longitude Licensing + Marlin Semiconductor (Irish subsidiaries of IPValue Management, owned by San Francisco PE firm Vector Capital) filed a USITC complaint accusing TSMC of infringing their patents; Marlin acquired part of the patents from UMC in 2021. TIPO Director-General Liao Cheng-wei publicly calls them patent trolls/NPEs seeking license fees or settlement. TSMC has petitioned the USPTO PTAB arguing the patents are invalid (published → lack novelty). Four Republican lawmakers urged the ITC (May 22 letter) to block imports of infringing foreign-made chips. ALJ preliminary ruling expected this month; ITC final decision possibly October.
- **Intel + PDF Solutions (Nenni/SemiWiki):** PDF Solutions (NASDAQ: PDFS, Santa Clara) is the #1 yield-analytics house — 18 of the top 20 semiconductor companies have worked with it; its Exensio platform fuses equipment/metrology/inspection/test/design data for root-cause yield work. Intel and PDF announced a collaboration July 2025; Lip-Bu Tan and PDF CEO John Kibarian are reportedly managing the projects directly. RibbonFET (GAA) + PowerVia (backside power) on **18A/18A-P** create new integration challenges that overwhelm traditional SPC — yield learning is the gating item for Intel Foundry external production.

## Long-tail / diamonds-in-the-rough
- **Tensordyne taped out an LNS (logarithmic-number-system) data-center inference chip**, claiming **17× tokens/sec/W vs an Nvidia GB300 system** (13× per rack) — but on **simulated benchmarks only**. Yet another well-funded inference challenger making order-of-magnitude power claims pre-silicon; file under "AI-inference-challenger claims" with heavy skepticism until real rack-level (InferenceX / AA-AgentPerf) numbers exist. Relevant to the long-run NVDA-inference-moat debate, moves nothing today.
- **"Warpage-to-Impedance Causality Matrix" (Dr. Moh Kolbehdari):** technical argument that in large AI packages (chiplets, HBM, glass substrates, bridges, interposers, CoWoS/CoPoS, 2.5D/3D), substrate warpage of 50–100µm is no longer a purely mechanical pass/fail item — it perturbs impedance, SI/PI margin, PDN resonance and thermal-current behavior, so signoff must couple mechanical + electrical + thermal + reliability. **Which means**: advanced-packaging signoff is getting materially harder as packages get bigger — a quiet moat-deepener for the incumbents (TSMC CoWoS, Amkor, the EDA/test layer) and a barrier for would-be second sources.

## Wiki updates made
- [[ASML]] — Recent developments: Lutnick EUV-in-China allegation + ASML denial; bear/headline-risk note. (sources 1→2)
- [[us-china-relations]] — Technology export controls: the EUV-in-China allegation under the existing "ASML EUV to China: RESTRICTED" line. (sources 2→3)
- [[MU]] — Recent developments: WSTS memory +250% to >$800B as the macro counterpart to the single-name PT math. (sources 11→12)
- [[semiconductors]] — State of the sector: WSTS $1.51T 2026 / $1.9T 2027 added alongside the UBS high-side anchor. (sources 3→4)
- [[ai-bubble-debate]] — new dated section: WSTS = the hardest confirmation that memory ASPs are >half the cycle's growth; Tensordyne logged as an inference-challenger flag. (sources 22→23)
- [[TSM]] — Recent developments: USITC patent-troll investigation (litigation overhang, minor). (sources 13→14)
- [[INTC]] — Recent developments: PDF Solutions yield partnership (foundry-execution leg). (sources 8→9)
- [[bottleneck-roadmap]] — packaging-signoff-difficulty note (warpage→electrical coupling) as a packaging-moat deepener.
- [[overview]] — June 19 holiday note (no tape; SemiWiki ingest highlights).
