---
date: 2026-06-24
type: article
publisher: SemiWiki (forum + articles)
url: https://semiwiki.com
raw_path: n/a (scripts/semiwiki_scan.py incremental scan)
touches: [AVGO, INTC, MU, ASML, QCOM, NVDA, semiconductors, bottleneck-roadmap, ai-infrastructure-debt, us-china-relations]
---

# SemiWiki daily sweep — 2026-06-24 (9 new items)

## TL;DR
- **Broadcom × OpenAI unveil "Jalapeño," OpenAI's first custom inference chip** — first in a multi-gen platform, 9-month design-to-tape-out, deploy end-2026, MSFT ~40% of volume. The AVGO custom-silicon leg validated; AVGO +~3% intraday (closed +0.51%).
- **But the same day, two AVGO counterweights surface:** Broadcom reportedly LOST the Google TPU v9 SerDes socket to **MediaTek** (Google fell back from 448G to MediaTek's 336G on signal-integrity/thermal issues; AVGO's 448G slips to a 2nm-DSP / 2028-29 problem), and a SemiWiki teardown details Broadcom's **$29B contingent lease guarantee** backstopping Apollo's purchase of OpenAI racks (an ai-infrastructure-debt vector).
- **Long-tail captured:** xLight $350M EUV-alternative raise (Gelsinger chair); Apple-Intel chips "2-3 years away" (Reuters); Qualcomm buys Modular ~$4B (AI software stack); Chinese CXMT 24Gb DDR5 enters retail kits (memory-independence datapoint); MediaTek 10-20% broad price hikes; GaN-on-SiC foundry slots tightening + NVIDIA Rubin SiC interposer; Nvidia banned chips 2x on China black market.

## Key facts

### 1. Broadcom × OpenAI "Jalapeño" (AVGO — portfolio)
- OpenAI's **first custom Intelligence Processor**, co-developed with Broadcom; first AI accelerator in a **multi-generation** compute platform the two are building together.
- **9 months design → tape-out** — among the fastest high-performance ASIC cycles ever; OpenAI used its own models to speed parts of the design.
- For **inference** (serving ChatGPT etc.); "performance per watt substantially better than current state-of-the-art."
- Initial deployment **end-2026**, large-scale late-2026 into the years ahead; **Microsoft expected to buy ~40%** of the chips.
- Market: AVGO +~3% intraday on the reveal, closed **+0.51% ($382.07)**.

### 2. MediaTek wins Google TPU v9 SerDes — Broadcom loses the socket (AVGO counter)
- MediaTek secured a **pivotal TPU v9** role via a **336G SerDes** solution after Google's original **448G** target hit signal-integrity, power and thermal walls.
- **Broadcom "is said to have lost its leading position for now"** on TPU v9, constrained by 448G maturity/timeline; 448G optical-module DSPs may need **2nm**, with capacity unlikely before **2028-29**.
- MediaTek also raising prices **10-20%** across mobile SoCs + PMICs (component shortages, capacity, lead times); its AI-ASIC revenue est. ~**$2B 2026**, scaling to several billion in 2027.

### 3. Broadcom's $29B lease guarantee (AVGO / ai-infrastructure-debt)
- SemiWiki ("The Wedding of the Year") on Broadcom's 10-Q (qtr ended May 3, filed June 9): **Note 11 discloses a guarantee of up to $29B** in lease obligations on AI racks built around Broadcom's custom chips, with **Apollo Global** (~$700B AUM) as the investor-partner buying the racks and holding the lease; **Broadcom is guarantor if OpenAI defaults.**
- Structure: OpenAI gets compute without upfront capital; Apollo gets a yield asset backstopped by Broadcom; Broadcom gets a committed custom-silicon customer at scale. A **contingent liability subordinating Broadcom's balance sheet to OpenAI's revenue** — the author calls it possibly "the most important structural change in the AI hardware industry this cycle." (Reported: Microsoft was originally to buy ~40% of the packaged silicon; OpenAI's compute head reportedly called that "unworkable" — unconfirmed whether Apollo's entry resolved it.)

### 4. xLight $350M EUV-alternative raise (ASML competitive / lithography)
- US-backed startup **xLight** raising **$350M** (Bain Capital + Boardman Bay leading); **Pat Gelsinger executive chairman** (since March), Playground Global invested 2025. US gov already in **$150M** via CHIPS (one of the largest shareholders); total funding ~$200M.
- Building **free-electron-laser** EUV light sources to cut cost/time of advanced-chip litho; first prototype in **Albany NY**, first working light source targeted **2028**; nonbinding **$4.2B** project-financing agreement.
- Plans to lobby ASML, TSMC, Intel, **Micron** to join the round. **ASML CEO Fouquet confirms ASML is collaborating with xLight on tech demonstrations** (rival X-ray litho effort from "Substrate" also noted). Long-dated, but a named, funded EUV-alternative vector to watch against the ASML monopoly.

### 5. Apple-Intel deal: "2-3 years away" (INTC)
- Reuters: any advanced Intel chip for Apple is **2-3 years out** ("2 years to design an SoC of this complexity + ~4 months to volume"). Penn (Future Horizons) calls it "a shotgun wedding," "huge leap of faith" given no track record.
- Analysts split on node: **14A** (2028-29) vs the safer **18A-P** (initial production this month) or older **Intel 3**. Context: Intel landed **Tesla** in April; the deal pairs Intel's foundry-credibility rebuild with Apple's hunt for capacity as TSMC strains on AI demand (Cook flagged supply constraints holding back iPhone sales in April). No formal announcement from either company.

### 6. Qualcomm buys Modular ~$4B (QCOM)
- Qualcomm acquiring **Modular Inc.** for **~$4B** — an AI-native, **silicon-agnostic** software stack that runs models across CPU/GPU/NPU/ASIC without per-accelerator rewrites. Deepens QCOM's data-center/edge software foundation ("efficiency, not capability, is the constraint; performance-per-watt drives inference cost"). A software-moat / developer-ecosystem play into QCOM's data-center ambitions.

### 7. Chinese CXMT 24Gb DDR5 enters retail kits (MU — China memory independence)
- Chinese vendors **Gloway and KingBank** now shipping **CXMT 24Gb DDR5** modules in 48GB consumer kits (6,000 MT/s) — **ending reliance on Micron/SK hynix/Samsung** for those SKUs. CXMT earlier shipped 16Gb DDR5 at 8,000 MT/s; G4 cells ~20% smaller than G3 (progression from 23nm→18nm nodes). Consumer-tier only for now, but a real domestic-DRAM-substitution datapoint — the long-run bear vector against the memory oligopoly's pricing power at the low end.

### 8. GaN-on-SiC foundry tightening + NVIDIA Rubin SiC interposer (bottleneck-roadmap / NVDA)
- GaN-on-SiC foundry slots harder to book: **Feb 2026 DoD invoked emergency procurement** prioritizing military GaN over commercial 5G/consumer (EW/anti-drone demand), squeezing dual-use/commercial radar programs. Separately, **NVIDIA reportedly planning to replace silicon interposers with silicon carbide in next-gen Rubin** — redirecting SiC substrate capacity toward data centers and compressing RF supply. Pricing pulled two ways: Chinese SiC wafers ($400-500/6") eroding prices ~30%, Western premium substrates $1,000-2,000 + DoD-reserved capacity priced at a premium.

### 9. Nvidia banned chips 2x on China black market (NVDA / us-china, minor)
- Reported (via X): Nvidia's China-banned AI chips trading at **2x price on China's black market** — "Jensen said share goes to zero in China but Nvidia gets paid either way" via smuggled units. Anecdotal, no hard volume; logged as a gray-market demand-intensity tell.

## Key claims (and how confident)
- **Jalapeño is a real AVGO win (high confidence — joint OpenAI/Broadcom release), but its EPS contribution is back-half-2026+ and the same week's TPU v9 SerDes loss to MediaTek shows the custom-ASIC moat is contestable.** Net for AVGO: thesis-positive (OpenAI multi-gen platform) but not unalloyed — one socket won, one lost, and a $29B contingent liability added.
- **The $29B Broadcom lease guarantee is disclosed fact (10-Q Note 11).** It's contingent, not drawn, but it moves AVGO from pure chip-vendor toward deployment-underwriter — an ai-infrastructure-debt exposure the bull case has to carry.
- **CXMT in retail kits = a real, dated China-memory-substitution datapoint** (consumer-tier), not yet a server/HBM threat — long-tail MU bear vector, not a near-term thesis mover.

## Wiki updates made
- Patched [[AVGO]] — Jalapeño reveal + TPU v9 SerDes loss to MediaTek + $29B Apollo lease guarantee.
- Patched [[INTC]] — Apple deal "2-3 years away" / node-split analyst read.
- Patched [[MU]] — CXMT 24Gb DDR5 retail-kit substitution datapoint.
- Patched [[ASML]] — xLight $350M EUV-alternative raise (Gelsinger; ASML collaborating on demos).
- Patched [[QCOM]] — Modular ~$4B acquisition.
- Patched [[semiconductors]] — MediaTek price hikes + TPU v9 SerDes shift; GaN-on-SiC tightening.
- Patched [[bottleneck-roadmap]] — GaN-on-SiC foundry squeeze + NVIDIA Rubin SiC-interposer.
- Logged in [[index]] and `log.md`. No stance/conviction changes.
