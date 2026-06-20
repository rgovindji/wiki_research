---
date: 2026-06-20
type: podcast
publisher: BG2 Pod (Brad Gerstner / Altimeter + Bill Gurley) — episode w/ Satya Nadella (MSFT CEO) + Sam Altman (OpenAI CEO)
url: unknown (BG2 Pod, recorded ~late Oct 2025 based on internal references; ingested 2026-06-20)
raw_path: raw/podcasts/2026-06-20-bg2-satya-sam-3trillion-buildout.txt
touches: [ai-capex-cycle, inference-economics, MSFT, OpenAI, NVDA, AMD, AVGO, ORCL, GOOGL, AMZN, ai-software, valuation-environment]
---

# BG2 — Satya Nadella + Sam Altman on the ~$3T AI buildout

> **Bias flag (heavy):** Gerstner (Altimeter) is a large OpenAI/NVDA/MSFT/META bull and says outright "we're certainly a buyer, not a seller." Nadella and Altman are the two most talk-their-book people alive on this topic — both are *selling* the durability of the OpenAI–MSFT partnership and the no-glut thesis directly into a market that is questioning AI capex. Treat every "non-existent chance of a glut" and "demand is infinite" line as a promotional claim from interested parties, not neutral analysis. Discount the AGI/science-discovery hype. The durable signal is in the *deal mechanics* and the *self-reported compute-constraint / RPO numbers*, which are checkable against MSFT filings.

## TL;DR
- **MSFT–OpenAI deal terms clarified (announced "Tuesday" of recording week):** MSFT holds ~27% of OpenAI on a fully-diluted basis for ~$13.5B cash invested ($134B figure cited loosely; Satya later anchors the actual at-risk cash at ~$13.5B). OpenAI nonprofit (OpenAI Foundation) capitalized with ~$130B of stock; first $25B directed to health + AI resilience. **Azure exclusivity on "stateless APIs" runs through 2030; rev-share (~15% assumed for illustration) + royalty-free IP access run through 2032 — both terminate early if AGI is independently verified by an expert panel.**
- **Compute scarcity is the whole story, and it's now a *power/shell* problem, not a chip problem.** Satya: "the biggest issue we are now having is not a compute glut, but it's power... I don't have warm shells to plug into. In fact, that is my problem today." Both MSFT and OpenAI say revenue/Azure growth would have been *higher* with more compute.
- **OpenAI capex commitments ~$1.4T over 4-5 yrs vs ~$13B+ 2025 revenue** — the central bubble question. Altman's defense: revenue growing steeply, would buy back OpenAI shares from skeptics, but also volunteers the real falsifier (cheap energy / 40x-per-year cost decline could strand contracts).

## Key facts / claims (with confidence)
- **MSFT ownership ~27% of OpenAI; ~$13.5B cash at risk; equity stake ~$135B today** (high confidence — stated by Satya directly). Q most-recent quarter: MSFT consolidated ~$4B of OpenAI losses; reporting non-GAAP EPS for transparency. *Verify against the actual MSFT 10-Q for the relevant quarter before using as fact.*
- **Azure grew 39% in the quarter on a ~$93B run rate** (Gerstner's framing, Satya agrees); cited vs GCP ~32% and AWS ~20%. Satya: Azure could have grown **41-42% with more compute** ("Absolutely. Absolutely... no question"). (Medium — Gerstner-supplied comparatives; check exact Azure growth/run-rate in MSFT filing.)
- **MSFT RPO ~$400B, ~2-year average duration**, described as diversified across 1P and 3P; framed as high-certainty backlog driving capex. Plus the separate $250B OpenAI/Azure commitment (longer duration). (Medium-high — Satya's own number.)
- **OpenAI compute commitments ~$1.4T / 4-5 yrs:** ~$500B NVIDIA, ~$300B each AMD + Oracle, ~$250B Azure (Gerstner's recitation; note the "$500 million / $300 million" in transcript are transcription errors for billion). 2025 OpenAI revenue "reported $13B," Altman says "well more than that." (Medium — directional; the per-vendor splits are widely reported frameworks, not contracts.)
- **OpenAI now >1B searches/day; reached ~400B annual searches ~8 yrs faster than Google** (Gerstner, cross-referenced in the China episode). (Low-medium — Altimeter's own analysis.)
- **OpenAI IPO:** Altman explicitly walks back the Reuters "late-26/27 IPO" report — "we don't have anything that specific... no date in mind." Gerstner pushes the trillion-$ / 10x-$100B-revenue framing; Altman prefers to fund with revenue growth. (High that there is no committed timeline; the trillion-$ math is Gerstner's, not a target.)
- **Inference software optimization is outpacing Moore's Law** (Satya): the per-GPU inference-stack gains at OpenAI are "much more exponential" than hardware. Reinforces [[inference-economics]] tokens-per-dollar-per-watt framing. (High as a directional claim.)
- **SaaS / "agent factory" thesis:** Satya repeats his "business apps are CRUD DB + business logic, and the logic collapses into the agent tier" call. Public software trades ~5.2x forward revenue vs ~7x 10-yr avg despite ATH market. Key nuance: "**agents are the new seats**"; enterprise monetization clear, consumer monetization "murky"; chat unit economics structurally worse than search (no amortized fixed index — every query burns GPU). (High as MSFT's stated view; surfaces a bear flag for incumbent SaaS.)
- **"Golden age of margin expansion"** (Satya) — Mag7 flat headcount + AI productivity; he expects headcount to grow but "with max leverage," top line outgrowing employees. (Bias: this is the bull case for operating leverage; stated by an interested party.)
- **Circular-revenue / vendor-financing question:** Satya claims MSFT has done *none* of the exotic vendor financing (AMD-equity-for-compute, NVIDIA deals, Meta debt backstops) — its OpenAI exposure is equity-for-compute or discounted compute pricing only. "Circularity ultimately will be tested by demand." (Self-interested distinction; surfaces the contradiction without resolving — see other episode.)

## Quotes worth keeping
> "The biggest issue we are now having is not a compute glut, but it's power... I don't have warm shells to plug into. In fact, that is my problem today." — Nadella
> "If the price of compute per unit of intelligence fell by a factor of 100 tomorrow, you would see usage go up by much more than 100." — Altman (Jevons framing)
> "There will come a glut for sure... if a very cheap form of energy comes online soon at mass scale then a lot of people are going to be extremely burned with existing contracts they've signed." — Altman (the falsifier, in his own words)
> "Agents are the new seats." — Nadella
> "It's kind of like having a frontier model for free if you're an MSFT shareholder." — Nadella (on royalty-free IP access through 2032)
> "There's not been a single business plan that I've seen from OpenAI that they have put in and not beaten." — Nadella

## How this is used / bias flags
- Feeds [[ai-capex-cycle]] (the $3T/60GW framing, power-not-chips bottleneck, RPO durability), [[inference-economics]] (software optimization > Moore's law; chat vs search unit economics), and the MSFT/[[ai-software]] pages (agent-factory thesis, SaaS multiple compression).
- **Do not treat the "non-existent chance of a glut over 2-3 years" as wiki fact** — it is the unanimous view of NVDA's largest customers + Jensen, all long. Altman himself contradicts it on the 5-yr horizon. Surface as a dated bull consensus with a named counter (the 40x cost-decline / cheap-energy stranding risk) — don't resolve.
- The MSFT financial specifics (27% stake, $13.5B at risk, $400B RPO, Azure 39%/$93B) should be verified against the actual MSFT 10-Q before being stated as fact on any company page.

## Wiki updates suggested (for orchestrator — not done here)
- [[ai-capex-cycle]]: add "power/warm-shell bottleneck > chip bottleneck (Satya, Jun 2026 ingest)" and the OpenAI ~$1.4T vendor-split framework with bubble caveat.
- [[inference-economics]]: add "inference software optimization outpacing Moore's law" + "chat unit economics structurally worse than search (no amortized index)."
- MSFT page (if/when created or patched): deal terms (Azure exclusivity 2030, rev-share/IP 2032, AGI early-termination clause), $400B RPO, $4B consolidated OpenAI losses, agent-factory SaaS thesis.
- [[valuation-environment]] / [[ai-software]]: software at ~5.2x fwd rev vs ~7x 10-yr avg; "agents are the new seats" disruption flag.
