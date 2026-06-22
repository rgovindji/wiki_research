---
date: 2026-06-22
type: podcast
publisher: Tasty Live (tastytrade)
url: https://www.youtube.com/watch?v=bUiIEOvQCTI
raw_path: raw/podcasts/2026-06-22-yt-bUiIEOvQCTI.txt
touches: [hedging-risk, market-concentration]
---

# Tasty Live — "Not all AI stocks are created equal" (correlation/beta study)

## TL;DR
- **AI stocks have decoupled from *each other* but become *more sensitive to the market*** — avg pairwise correlation fell ~52% (2020-22) → ~42% (2024-26), while beta to the market rose to ~75%. Low correlation + high beta is the unusual, important combination.
- **Two camps with different hedges:** market-coupled lower-beta (MSFT/GOOGL/AMZN, >70% corr → S&P puts work) vs **narrative-driven high-beta (NVDA/AMD/META/PLTR/SMCI → S&P puts do NOT hedge them)**.
- **In a crash, all AI names snap to >90% correlation** — "diversification disappears when the market gets stressed." Size by **beta-weighted risk, not dollars.**

## Key facts / claims (with confidence)
- Avg pairwise AI-stock correlation: **~52% (pre-AI 2020-22) → ~42% (2024-26)**, ~23% relative drop. *Their study; directional.*
- Market beta of AI names rose to **~75%** (2024-26). *Their study.*
- 90-day rolling correlation-to-market: **MSFT/GOOGL/AMZN stay >70%** (index-coupled); **NVDA/PLTR move on their own AI narrative** — NVDA's correlation drifted the *furthest* from the market. *Sound, matches general market behavior.*
- Correlation threshold they use for these high-vol names = **65%** (vs the usual 50%): below 65% = "not following the market."
- **Hedging implication:** for index-coupled names, **S&P puts** hedge effectively; for narrative-driven high-beta names, **S&P puts can't bail you out** — need name/sector-specific hedges. *High-value, sound.*
- **Crash behavior:** "correlation spikes during crashes… all AI stocks move together above 90%" → diversification vanishes exactly when needed. *The key risk takeaway.*
- Return dispersion since Jan-2024 confirms "these are not the same trade anymore" — treat each AI name individually.
- Portfolio note: adding AI names raises portfolio volatility *significantly* even at low correlation, because beta/vol is high — "the vol premium per dollar of allocation is the real cost"; size by beta-weighted risk.

## Quotes worth keeping
> "Less correlations and high sensitivity to the market."
> "When it's not correlated to the market, S&P puts can't bail out, can't be used to hedge your positions."
> "Diversification can disappear when the market gets stressed or in the sell-offs."

## Bias / usage notes
- Retail options-education show (tastytrade) — descriptive quant, *not* a stock call; the exact %s are their internal study (directional, not gospel). Nothing here changes a stock pick — it's a hedging/sizing insight.
- **Directly validates our hedge construction:** the $200K moonshot uses a **SOXX (semis-specific) tail hedge, not SPX**, precisely because its high-beta narrative names (NVDA/AMD) can't be hedged with index puts — this study independently confirms that. And it quantifies the core book's real tail: AI concentration looks "decoupled" in calm tape but snaps to >90% correlation in a crash, so cash + the de-rated/power tilt are the only diversification that survives a drawdown.

## Wiki updates made
- Patched [[hedging-risk]] (the SPX-can't-hedge-narrative-names point + crash-correlation + beta-weighted sizing).
- Touches [[market-concentration]] (AI-name decoupling vs crash-convergence).
