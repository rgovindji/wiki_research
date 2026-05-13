---
type: source
title: The Great GPU Shortage – Rental Capacity – Launching our H100 1-Year Rental Price Index
authors: Daniel Nishball, Jordan Nanos, Cheang Kang Wen, and 2 others (SemiAnalysis)
publication: SemiAnalysis Newsletter
date_published: 2026-04-01
date_read: 2026-05-09
url: https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity
local_file: raw/articles/The Great GPU Shortage – Rental Capacity – Launching our H100 1 Year Rental Price Index.pdf
tags: [ai, semis, gpu-rental, neocloud, market-sentiment]
---

# 2026-04-01 — SemiAnalysis launches H100 1-yr rental price index

## Headline numbers

- **H100 1-yr contract: $1.70/hr (Oct 2025) → $2.35/hr (Mar 2026) — +40%** in 5 months
- Rate is set to rise another **15-20% month-on-month** through end of March
- **All GPU capacity coming online until August-September 2026 has already been booked** — market-wide
- **Anthropic ARR: $9B (end of last year) → over $30B today** — tripled in a single quarter
- Customers paying **$14/hr/GPU for p6-b200 spot instances on AWS**
- Some H100 contracts being renewed at **the exact same rate they were signed at 2-3 years ago** (no decay)
- Blackwell lead times for new deployments now extend into June-July 2026

## Why this matters (refutes prior bear data point)

This index **directly contradicts the Reddit thread** that surfaced 2026-04 (GQG H200 secondary-market discount). The Reddit anecdote was one data point; SemiAnalysis's index is built from 100+ market participant surveys plus transaction data they themselves arrange. **Which means:** the "GPU rental softening = late-cycle warning" thesis is NOT confirmed by broader survey data. If anything, the SemiAnalysis evidence points the opposite direction — pricing is reaccelerating, not decaying.

## Drivers behind the surge

1. **Hopper held firm.** Before late 2025 the consensus was H100/H200 prices would fall as Blackwell ramped. Opposite happened — H100 demand strengthened on inference-heavy open-weight model adoption.
2. **Memory pricing went parabolic (Jan 2026).** LPDDR5 prices tracking ~4x YoY and DDR5 ~5x YoY in 1Q26. **Which means:** OEMs repriced AI servers above the underlying component-cost increase, compressing prospective project IRRs and causing operators to slow-roll/abandon deployments → supply that would have come online was withheld → rental market tightened.
3. **B300 chassis BoM evolution.** CPU DDR5 RAM cost per GB: $4 (Sept 2025) → $8 (Dec) → $14 (current) → $21.7 (4Q28 projected). Total server cost up 8% (Dec) → 14% (4Q28).
4. **Multi-agent workflows + native media generation** (Seedance, Nano Banana) driving parabolic token consumption.
5. **Claude Code growth.** Anthropic ARR tripled in one quarter from $9B → $30B+. Claude Code = 4.0% of public GitHub daily commits (42,886x growth in 13 months) and projected to reach 20%+ by end of 2026. **Which means:** the demand curve has shifted up and is "relatively inelastic for now" — if ROI on AI tools is 5-10x, rental pricing can rise substantially before demand curtails.

## Market structure (3 segments)

1. **Short-term (on-demand, spot, <3m)** — residual capacity; Lambda, Runpod
2. **Mid-term (3m-3y+)** — most economically relevant segment; this is what the new index tracks
3. **Long-term offtakes (4-5y)** — dominated by AI labs locking in 50MW-100MW+ blocks (~24K-48K GB300 NVL72 GPUs); often Hyperscaler-backstopped, structured for teens project IRR

## The market sentiment disconnect (KEY INVESTMENT INSIGHT)

> "What is most striking is the disconnect between these underlying dynamics and broader market sentiment. Despite clear evidence of tightening supply and rising prices... public sentiment has turned increasingly negative on names like CoreWeave, Nebius, IREN, and these companies' share prices are currently at the low end of the 6-12mth trading range."

**Which means:** there's a setup where fundamentals (rising rents, sold-out capacity) are diverging from sentiment (share prices at lows). Beneficiaries with shorter-duration contracts repricing fastest into the new environment:
- Shorter-duration contract books (faster repricing) — [[CRWV]], [[NBIS]], IREN
- Large H100 install bases (now repricing at +40%)
- Near-term capacity additions

The featured guest-post comment on the article was simply: **"Long NBIS"**.

## Three checkpoints for forward direction

1. **GB300 cluster ramp through 2026** — does additional compute capacity ameliorate the shortage, or does token demand outpace it?
2. **Silicon shortage** — TSMC N3 capacity, HBM, DRAM, NAND tightness can always worsen
3. **AI labs ARR growth** — rate at which adoption spreads and token consumption grows

## Conclusion (author)

> "GPU rental pricing is more likely to continue rising than falling... Would we be jinxing it if we said that This Time Might Be Different?"

## Direct wiki implications

- **[[ai-bubble-debate]]** — NUANCE the "late-cycle warning indicators" section. The Reddit B200 anecdote was a localized data point; the authoritative survey-based index shows the OPPOSITE through March 2026. The warning indicators framework is still conceptually correct — but March 2026 data does NOT confirm them yet. Status: monitoring, not triggered.
- **[[ai-capex-cycle]]** — Add 2026-04 data: all capacity through Sep 2026 sold out. Demand inelastic at current price points.
- **[[CRWV]]** — Public sentiment vs fundamentals disconnect. Stock at low end of 6-12mo range while rental prices +40%.
- **[[NBIS]]** — Same disconnect. Featured comment "Long NBIS" reflects this thesis.
- **[[MU]]** — DRAM prices going parabolic (4-5x YoY) confirms the AI memory supercycle.
- **[[SNDK]]** — Same; LPDDR5 +4x YoY confirms tight memory.
- **[[bottleneck-roadmap]]** — Memory bottleneck is biting harder and earlier than expected (Jan 2026 parabolic).
- **[[nvda-supply-chain]]** — B300 chassis BoM data point: component cost +8% to +14% vs September baseline.

## Related

[[NVDA]] · [[CRWV]] · [[NBIS]] · [[MU]] · [[SNDK]] · [[ai-bubble-debate]] · [[ai-capex-cycle]] · [[bottleneck-roadmap]] · [[2026-05-09-dwarkesh-dylan-semianalysis]]
