# Mistral AI — Investment Decision Dossier
**Status: PARKED / open — revisit later.** · Compiled 2026-06-17–18 · The offer: **€19.8B post-money, €45.76/share.**

> Self-contained summary of everything we worked through. Full live page: `wiki/companies/MISTRAL.md`. Source summaries: `sources/2026-06-08-google-intel-3m-tpu-2028.md` (context), `sources/2026-03-26-latentspace-mistral-voxtral-gtm.md` (GTM). Built from a 4-agent research sweep (fundamentals · competitive/moat · ruthless bear · valuation) plus follow-up diligence.

---

## One-paragraph verdict
Impressive company; the **entry at €19.8B is not clearly a good risk/reward**. You'd be paying **~50x trailing revenue (the richest multiple in the frontier cohort) for the weakest compute position**, in the most commoditized layer, late in the cycle, into an illiquid structure where — unless it's primary preferred — you hold maximum downside with minimal protection and no liquidity for years. Honest expected value is positive but **right-tail-dependent (~2.3x illustrative EV, wide error bars), with a material (~20%+) chance of permanent loss.** Treat as a **small speculative/venture-sleeve position sized like money you can lose entirely**, and only if the deal terms check out. If it's secondary common via a fee-heavy SPV with no information rights → **pass.**

## The numbers
- **Valuation history:** Seed ~€240M (2023) → A ~€2B → B €5.8B (Jun'24) → **C €11.7B (Sep'25, ASML led €1.3B, ~11%, largest holder)** → rumored ~€3B raise at **~€20B (Jun'26, not confirmed closed)**. €19.8B = ~1.7x step-up vs Series C; essentially flat vs the rumored primary.
- **Revenue:** ~$400M ARR (Jan'26), up ~20x YoY from ~$16-20M. **$1B is a self-set 2026 target, not achieved.** Gross margin / burn **undisclosed**.
- **Implied multiple:** ~**50x trailing ARR** (vs Anthropic ~21x on ~$47B, OpenAI ~34x on ~$25B); ~20x only on the unproven $1B forward target.
- **Share count:** €19.8B ÷ €45.76 ≈ **432.7M shares**.
- **Cap table:** founders >50% voting via dual-class (~39% economics); ASML ~11%; a16z, General Catalyst, Lightspeed, DST, Nvidia, Mubadala, Bpifrance (French state), Microsoft <1%; ESOP ~10%.
- **Compute:** Mistral Compute = ~13,800 Nvidia GB300s, 44MW, Bruyères-le-Châtel (Essonne), $830M debt (7-bank syndicate), live ~end-Q2'26. Target ~200MW by end-2027.

## ⚠️ The pivotal unknown — resolve FIRST
**€19.8B / €45.76 appear in no public source** (press says "~€20B"). Two readings invert your risk:
- **PRIMARY (new preferred):** you fund the company, likely get **preferred + ~1x liquidation preference** = downside protection. (Cleaner per-share price + reported ~€3B raise support this.)
- **SECONDARY / SPV (existing common):** no preference, no info rights, fee-heavy (double-promote), subordinate to ASML's senior pref = **worst seat.**
You cannot tell which from public data. **Get it in writing.**

## Bull case
- **Sovereignty moat** (EU data-residency, on-prem/air-gapped, no US-Cloud-Act exposure) — a regulatory/political moat US labs can't easily copy. Anchors French MoD framework, Germany public-admin, Helsing, CMA CGM (~80k seats), Stellantis.
- **Genuine growth** (~20x ARR in 12 months) and **elite, candid management** (Mensch ex-DeepMind, Lample/Lacroix ex-Meta FAIR; real research depth).
- **ASML + French-state anchoring**; efficiency-first specialized-small-model strategy may give **healthier inference margins** than a frontier-API burner.
- **Sticky GTM (data gravity):** the pitch — "you're wasting the trillions of proprietary tokens you've collected; fine-tune your own data on-prem, 10x cheaper" — plus forward-deployed engineers = real switching-cost lock-in that blunts the commoditization fear.

## Bear case (where the weight is)
- **🔴 Compute gap is existential.** Anthropic pays **~$1.25B/month** for one 220k-GPU cluster; Mistral has raised ~$3-4B equity *total* and runs ~13,800 GPUs. 15-50x deficit. Efficiency narrows ~2-3x, not 50x. Falling off the frontier → re-rate to "European inference vendor" = **80-90% impairment.**
- **🔴 Commoditization.** Open-weight + DeepSeek/Qwen (97% price cuts) collapse the segment. Mistral is *not frontier enough* to charge premium, *not cheap enough* to beat the Chinese.
- **🟠 Multiple-quality fulcrum.** The GTM is **services-led (forward-deployed engineers, bespoke fine-tunes)** = **Palantir/Accenture-FDE economics (~5-15x rev), not OpenAI-platform economics (~50x)**. The 50x is only defensible if self-serve platform (La Plateforme/Studio/Forge) is the engine and FDEs are land-and-expand — *not* if the FDEs ARE the business. **Decisive, and undisclosed.**
- **🟠 Dilution.** ~9-month mega-round cadence; ~3 more rounds at ~18% → you keep ~55% of your stake. **Flat exit = ~0.55x loss before any preference.**
- **🟠 Sovereignty caps the ceiling.** France treats Mistral as a strategic asset → high-premium foreign (US-megacap) M&A is near-politically-foreclosed; IPO ~2028-2030. The moat that protects the floor caps the exit.
- **🟠 Liquidity.** No real secondary market (inconsistent marks: Notice $11.63 / Hiive $37.55); years to any exit; information asymmetry vs the lead funds.
- **🟡 Myth-bust:** the "$14B French defense deal" is a **misreport of the valuation**, not a contract — don't underwrite on it.

## Return math
| Exit valuation | Gross | Net of ~45% dilution |
|---|---|---|
| €19.8B flat | 1.0x | ~0.55x (loss) |
| €40B | 2.0x | ~1.1x |
| €80B | 4.0x | ~2.2x |
| €150B | 7.6x | ~4.2x |
| €300B | 15.2x | ~8.4x |

Illustrative probability-weighted **EV ≈ 2.3x net** (right-tail-driven; ~50% of mass break-even-or-worse net of dilution). You need a **~€40B+ exit just to break even net**; real money needs €80B+.

## The €200B question (from the 2026-06-18 discussion)
**Not "no way" — but a low-probability right tail (~10-15% over 5-10 years).** €200B ≈ 10x the entry; needs ~$5-10B revenue (10-25x from today). The realistic path is **"entrenched European sovereign-AI infrastructure riding the agentic-token wave," not "beat OpenAI."** Stacked conditions: agentic inflection arrives (CTO says ~a year+ out) + becomes the EU/regulated default + AI multiples don't fully compress + stays frontier-relevant. **Key nuance for you:** a €200B *company* outcome is only **~5-5.5x net of dilution for your €45.76** — a true personal 10x needs the company **~€350-400B** (deeper tail, ~5%).

## Questions you MUST ask the seller
1. **Primary or secondary?** (Decides everything below.)
2. **Liquidation preference & seniority** — 1x non-participating preferred, or common/junior? Where vs ASML's pref?
3. **Share class & voting** (founders' >50% dual-class).
4. **Information rights** — do you get financials (the undisclosed gross margin, burn, runway, NDR, customer concentration, gov vs commercial mix)?
5. **Pro-rata / anti-dilution** protection against the ~9-month round cadence?
6. **SPV fees** — management fee + carry (double-promote)? Can eat 20-30% of returns.
7. **Transfer restrictions / ROFR / lockup** and any realistic pre-IPO liquidity.
8. **Is the ~€20B primary actually closed, who led, exact price** — is €45.76 real or a benchmarked mark?
9. **Platform vs services revenue split + gross margin** — the multiple-quality fulcrum. Services revenue deserves ~5-15x, not ~50x.

## Conviction log (what moved my view, what didn't)
- 4-agent sweep → **lean cautious** (high-risk, illiquid, right-tail).
- Your business-model bullets → verified; one correction (Medium 3.5 is open-weight/revenue-capped, not closed/API-only — prior Medium 3 was the closed one); **verdict held** (components moved, netted out).
- Latent Space transcript → **confirmed** services-led GTM; strengthened moat, hardened valuation concern; **verdict held**.
- "No way to €200B?" → corrected to **low-probability tail, not impossible**.
- **Net, unchanged throughout: lean cautious on the entry; the decision hinges on deal terms + revenue mix, not on the (genuine) quality of the company.**
