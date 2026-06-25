---
date: 2026-06-25
type: podcast
publisher: Latent Space (swyx)
url: https://www.youtube.com/watch?v=h5dlIPM0X18
raw_path: raw/podcasts/2026-06-25-latentspace-midha-amp-gpu-labs.txt
touches: [inference-economics, bottleneck-roadmap, ai-capex-cycle, ai-bubble-debate, market-concentration]
---

# Latent Space — Anjney Midha (Amp / a16z): "Why AI Labs With Unlimited GPUs Still Fail"

Published 2026-06-18 (Latent Space). Anjney Midha is an **a16z general partner AND founder/CEO of "Amp"**, the compute-grid company he describes — heavy talk-his-book throughout. Investor in Anthropic, Periodic Labs, Mistral, Black Forest Labs.

## TL;DR
- **Compute is not the binding constraint — culture/alignment is.** Many labs have all the cash + compute they need and still cannot ship; well-funded labs fail on execution, not hardware.
- **Endemic utilization waste:** best-in-class MFU (model FLOP utilization) is only ~60-70%, and node allocation often sits below the ~96% that Google treats as the floor (<95% = an outage). A large share of nominal compute spend is effectively wasted.
- **Amp is positioning as the "independent system operator" (ISO) for compute** — a multi-cloud, multi-silicon scheduling "grid" (PJM-for-electricity analogy), anchored ~1.3 GW base-load demand, targeting ~6 GW of spike capacity over 4 years. "Excess capacity we expected to free up by year-end is all gone. It's exploding."

## Key facts / claims
- **Utilization:** two regimes — node allocation (% cards in use; ~96% standard, <95% = outage at Google) and MFU (best-in-class ~60-70%). Most single-tenant clusters miss both; fix = iterative bring-ups, not big-bang scaling.
- **Demand (timely):** in the ~6 weeks prior, expected excess capacity vanished; founders who raised billions are texting for "15 nodes in the next few weeks." Midha: **"Nvidia's not able to meet the demand of production. We just need more chips."**
- **Amp grid economics:** ~1.3 GW base-load ≈ "$40B of cloud spend" target over 4 yrs (not all secured); ~6 GW spike capacity needed. Model borrowed from Google Borg/Brain-Marketplace scheduler + a16z internal "Oxygen." Explicitly NOT a neo-cloud ("marketing speak") and NOT vertically integrated (opposite of xAI/OpenAI). Donated ~2,000 H100s to nonprofit/university labs.
- **Matrox** (founder Reiner Pope, ex-Google): tapes out 2027; differentiates on logic-die systems co-design; deliberately adopts **Nvidia's reference architecture** so chips drop into any Nvidia bring-up site. Structural risk for challenger silicon = trust-boundary: ~2-yr tape-out needs early visibility into the *next* model architecture.
- **Lisa Su (AMD)** flagged as upcoming guest — alt-architecture demand is live.
- **Anthropic:** a16z put "a few hundred million" in earlier this year; Midha claims Anthropic "achieved takeoff in October of last year," far more capital-efficient than OpenAI, with coding as P0 path to AGI.
- **Power/permitting:** marginal compute ~$4/hr (Scott Nolan framing); self-flagged-as-overstated claim that "up to 20% of US data centers this year are at risk" of failing on community/permitting support; predicts coming regulatory audits/investigations of fast-moving data-center builders.

## Key claims (and how confident)
- *Demand re-accelerated mid-2026, Nvidia supply-constrained* — directional, self-interested but corroborated by [[MU]] supercycle + Korea export reads. **Medium-high.**
- *60-70% MFU / sub-96% node util = wasted capex* — expert assertion, not audited; plausible. **Medium.**
- *Well-funded labs fail on culture, not compute* — execution-side bubble warning; credible but unfalsifiable. **Medium.**
- *20% of US data centers at community/permitting risk* — self-flagged as possibly overstated. **Low.**

## Quotes worth keeping
> "There are so many AI labs today that have all the cash they need. They have all the compute they need and they're still not able to ship anything [solid]… my diagnosis is it's the culture."

> "We thought we'd have a bunch of excess capacity by the end of this year. It's all gone. It's exploding."

## Bias flag
Heavy talk-his-book: nearly every favorable claim maps to a Midha/a16z position (Amp, Anthropic, Periodic, Matrox, Mistral). Utilization stats = directional expert assertion, not audited; "demand exploding" is self-interested; "20% at risk" self-flagged as overstated. Ad-free/subscriber-funded show.

## Wiki updates made
- [[inference-economics]] — added MFU 60-70% / node <96% effective-vs-gross-compute waste bullet.
- [[bottleneck-roadmap]] — added culture/trust-boundary (≈2-yr tape-out) + power/permitting as binding bottlenecks.
- [[ai-capex-cycle]] — added mid-2026 demand re-acceleration ("excess gone, Nvidia can't meet production") vs 20%-at-risk brake.
- [[ai-bubble-debate]] — added execution-side warning: unlimited GPUs ≠ shippable output.
- [[market-concentration]] — added Nvidia reference-architecture gravity (challengers build *into* it).
