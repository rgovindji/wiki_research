---
type: source
title: "Amazon's Durability"
authors: Ben Thompson (Stratechery)
publication: Stratechery
date_published: 2026-05-11
date_read: 2026-05-12
url: https://stratechery.com/2026/amazons-durability/
tags: [AMZN, AWS, cloud-hyperscalers, ai, networking, nvda, avgo]
---

# 2026-05-11 — Stratechery: AWS's structural AI networking handicap

Ben Thompson's piece on Amazon argues that AWS's long-standing optimization choices — specifically the in-house **Nitro** card and **Elastic Fabric Adapter (EFA)** networking stack — left it structurally less-prepared for AI workloads than competitors using Nvidia/Broadcom networking from the start. The piece picks up on SemiAnalysis reporting that AWS infrastructure suffers an AI-era networking penalty relative to GCP/Azure.

## The core argument

AWS built Nitro + EFA over a decade to win the **CPU cloud era** — they're elegant for distributing millions of small workloads at scale. But AI training and inference are **fundamentally different topology problems**: they need ultra-low-latency, high-bandwidth, lossless networking between very small numbers of very-high-power GPUs.

**Which means:** Nvidia's NVLink / NVSwitch / Spectrum-X and Broadcom's Tomahawk are the substrate the entire AI industry is building on. AWS Nitro/EFA wasn't designed for that workload shape, and now AWS faces a choice: (a) graft Nvidia/Broadcom networking into its stack and lose Nitro differentiation, or (b) ship AI on Nitro and underdeliver on goodput vs competitors.

## Why this matters now

This explains the AWS-specific signals that have surfaced across multiple sources:

- **Stalled AWS AI revenue mix disclosure** — AWS is the most opaque among hyperscalers about AI revenue specifically
- **AMZN held 2026 capex flat at $200B** while [[MSFT]] / [[GOOGL]] / [[META]] all raised (see [[2026-05-12-hyperscaler-capex-q1-revisions]])
- **AWS Trainium 2 + Trainium 3 strategy** is partially compensating but still nascent
- The Anthropic compute deal with AWS got significant fanfare but AWS still buys substantial Nvidia GPUs

**Which means:** the AWS AI ramp narrative is structurally more fragile than [[MSFT]] Azure or [[GOOGL]] Cloud — not because of demand, but because of the **stack-level constraint** that Ben Thompson identifies. This is a sharper bear thesis than anything currently in the wiki's [[AMZN]] page.

## Investment implications

### For [[AMZN]] (current wiki stance: bull / medium)

**Bear data point to add:** AWS's Nitro/EFA stack was optimized for the prior cloud era and creates structural AI networking penalty vs Azure (Nvidia networking) and GCP (TPU + Nvidia). Trainium is the hedge but unproven at frontier-model scale. **Which means:** AMZN's AI revenue lag vs MSFT/GOOGL has a technical/architectural root cause, not just a go-to-market gap. This is the kind of multi-year handicap that doesn't resolve in one capex cycle.

**Counter:** Retail business margin expansion is the other half of the AMZN bull case — that thesis is unchanged.

**Net:** Conviction stays medium. Bull stance holds but the AWS leg of the thesis weakens. If AMZN can't show AI-attached revenue growth in line with peers by 2H 2026, consider downgrading to neutral.

### For [[NVDA]] (current wiki stance: bull / high)

**Bull data point confirmation:** Even AWS, the largest hyperscaler with the most sophisticated in-house silicon program, can't fully escape Nvidia networking dependence. **Which means:** Nvidia's networking moat (NVLink + Spectrum-X) is even more durable than the GPU moat — the GPU is replaceable, the networking is not.

### For [[AVGO]] (current wiki stance: bull / high)

**Bull data point confirmation:** Broadcom Tomahawk + Jericho switching is the alternative substrate to Nvidia networking. **Which means:** AVGO is the only credible non-Nvidia networking play at hyperscale, which matters because Google (Broadcom's largest custom silicon customer) explicitly chose this stack. AVGO Q1 AI rev +106% YoY is supported by this networking-moat logic.

## Caveat — Anthropic / AWS partnership

The wiki has previously noted Anthropic uses AWS for substantial compute (alongside GCP). The Stratechery framing doesn't dismiss this — it argues that **even Anthropic uses AWS despite the networking handicap**, because compute is so scarce that even a sub-optimal cluster is better than no cluster. **Which means:** AWS will still generate AI revenue; the question is whether the unit economics (goodput per $) can match GCP/Azure. The SemiAnalysis ClusterMAX framework (see [[2026-04-20-semianalysis-gpu-cluster-cost]]) is precisely the methodology that exposes this gap.

## Related

[[AMZN]] · [[NVDA]] · [[AVGO]] · [[GOOGL]] · [[MSFT]] · [[cloud-hyperscalers]] · [[ai-capex-cycle]] · [[2026-05-12-hyperscaler-capex-q1-revisions]] · [[2026-04-20-semianalysis-gpu-cluster-cost]]

## Citations

- [Amazon's Durability — Stratechery (Ben Thompson)](https://stratechery.com/2026/amazons-durability/)
