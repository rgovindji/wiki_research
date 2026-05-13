---
type: source
title: How Much Do GPU Clusters Really Cost? (Calculating Cluster TCO, The Real Impact of Downtime, The Grand Unifying Theory of Goodput, ClusterMAX 2.1 Update)
authors: Jordan Nanos, Bryan Shan, Cheang Kang Wen, and 2 others (SemiAnalysis)
publication: SemiAnalysis Newsletter
date_published: 2026-04-20
date_read: 2026-05-09
url: https://newsletter.semianalysis.com/p/how-much-do-gpu-clusters-really-cost
local_file: raw/articles/How Much Do GPU Clusters Really Cost_.pdf
tags: [ai, semis, gpu, cluster-tco, goodput, neocloud]
---

# 2026-04-20 — Rethinking the Total Cost of a GPU Cluster

44-page deep dive on GPU cluster TCO methodology. Most page content is paywalled in the PDF rendering, but the introduction and structure establish the framework.

## Framework

> "Modern GPUs are unbelievably expensive. A single Blackwell GPU costs more than the average car, and uses more energy than a single family home... Many foundation model companies now spend an order of magnitude more money on GPUs than they do on employees. We know multiple companies spending over 80% of their initial funding on GPUs."

Startup founders building financial plans have **four cost categories**:
1. GPU clusters
2. Tokens
3. Employees
4. Everything else

The article reframes the TCO conversation: "two cloud offerings with **identical pricing per GPU-hour** can have very different TCO" once you account for:
- Downtime
- Setup time
- Debugging time
- Networking / storage performance tuning
- CPU compute
- Networking, storage, software costs (the hidden line items)

## "Grand Unifying Theory of Goodput"

The article introduces (per the subtitle) a unified framework for measuring effective compute output ("goodput") rather than raw GPU-hours. Specific methodology was not legible in the PDF extract.

## ClusterMAX 2.1 Update

Updated rankings of Neocloud providers on cluster reliability/performance. Full rankings not visible in the extract. SemiAnalysis maintains [ClusterMAX](https://clustermax.semianalysis.com) as their tracked dataset.

## Investment implications (inferred from framework)

- **[[CRWV]] / [[NBIS]]:** Differentiation on goodput (uptime, performance) vs. raw $/hr matters. The "all clouds are equal" commoditization bear case is structurally wrong. **Which means:** providers that can demonstrate measurably better goodput command premiums and longer-tenor contracts.
- **[[NVDA]]:** Reinforces that the Blackwell value proposition is not just FLOPS but the ecosystem (networking, software) that delivers them.
- **AI startups (off-watchlist):** Spending 80%+ of initial funding on GPUs is the new normal — explains why AI-native ARR ramps fast but burn rates are extreme.

## Direct wiki implications

- **[[ai-capex-cycle]]:** Reference the "80% of initial funding on GPUs" data point as evidence of how AI capex has restructured startup financial models.
- **[[CRWV]] / [[NBIS]]:** Note ClusterMAX 2.1 framework as the authoritative third-party benchmark on Neocloud quality.

## Related

[[NVDA]] · [[CRWV]] · [[NBIS]] · [[ai-capex-cycle]] · [[2026-04-01-semianalysis-gpu-rental-index]]
