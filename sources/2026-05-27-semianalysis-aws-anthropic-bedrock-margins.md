---
date: 2026-05-27
type: report
publisher: SemiAnalysis
url: https://newsletter.semianalysis.com/p/anthropic-growth-and-bedrock-mix
raw_path: n/a
touches: [AMZN, MSFT, GOOGL, cloud-hyperscalers, inference-economics, ai-capex-cycle, ORCL, CRWV]
---

# Anthropic Growth and Bedrock Mix Drive AWS Margins Higher While Peers Lag

**Authors:** Jeremie Eliahou Ontiveros, Joey Brookhart, Crystal Huang, Dylan Patel. Published 2026-05-27.

## TL;DR
- AWS operating margins inflected up (+213 bps Q/Q) while Azure and GCP margins stayed flat-to-down. The driver is mix: AWS's token-as-a-service (TaaS) business via Bedrock — overwhelmingly Anthropic/Claude — carries much higher margins than the IaaS rental that still dominates Azure/GCP.
- Bedrock is now ~$5.5B run-rate (37% of AWS AI revenue, up from 9% a year ago), grew ~170% Q/Q in 1Q26, and 80-90%+ of its usage is Anthropic models. Trainium powers 50%+ of Bedrock tokens — vertical integration that competitors lack.
- Counter-nuance on GCP: its "record margins" are partly an accounting illusion — ~$5.4B of DeepMind/Gemini training cost is bucketed outside GCP, flattering reported cloud margins.

## Key facts (with confidence)
- **AWS EBIT margin +213 bps Q/Q** (most recent quarter); Azure/GCP margins flat-to-declining over several quarters. (Medium-high — SemiAnalysis estimate built off reported segment data.)
- **Bedrock ~$5.5B run-rate, 37% of AWS AI revenue (vs 9% in 1Q25); grew 170% Q/Q in 1Q26, 60% Q/Q in 4Q25.** (Medium — SemiAnalysis estimate; Amazon does not break out Bedrock.)
- **AI revenue mix:** AWS AI = ~10% of total revenue (up from 2% in 1Q24) vs Azure 27%, GCP 36% — yet AWS's LOWER AI mix outperforms on margin because of TaaS vs IaaS economics. (Medium.)
- **Anthropic:** total ARR $30B, +$21B net-new in 1Q26; API revenue up ~13x y/y on coding demand; inference gross margins mid-60s% (up from 38% in 2025, -94% in 2024). (Medium — ARR/margin are estimates; the coding-driven ~13x is consistent with prior SemiAnalysis value-capture work.)
- **Bedrock unit economics:** ~$26M Bedrock revenue per MW (Anthropic) in 1Q26 → implied ~55% EBIT margin; projected ~$42M/MW in 2Q26. (Low-medium — modeled, sensitive to assumptions.)
- **Bedrock = ~30% of AWS Y/Y gross-profit step-up despite only ~4% of AWS revenue.** (Medium — the punchline stat; an estimate.)
- **Trainium powers 50%+ of Bedrock token usage** (Matt Garman, Nov 2025). (High — direct exec quote.)
- **Azure drag:** datacenter "freeze" cost ~12 months of growth; OpenAI backlog = ~2.5x Azure annual revenue (capacity-bound). (Medium.)
- **GCP accounting illusion:** ~$5.4B "Alphabet-Level Activities" / DeepMind+Gemini training cost in 1Q26 (up from $3.0B in 1Q25) sits OUTSIDE GCP, inflating GCP margins; GCP revenue still >60% YoY. (Medium-high — sourced to Alphabet segment structure.)
- **Anthropic expected operating-income profitable in 2Q26** after adjusting for SBC (WSJ, 2026-05-20). (High — attributed to WSJ.)

## Quotes worth keeping
> "Our AWS Trainium chips, designed in-house for AI workloads, now power more than 50% of Amazon Bedrock token usage." — Matt Garman, AWS CEO (Nov 2025)
> "Anthropic is expected to be Operating Income profitable in 2Q after adjusting for stock-based compensation." — Wall Street Journal (2026-05-20)

## Bias & paywall notes
- **PAYWALLED / TRUNCATED:** ~three-quarters in, "This post is for paid subscribers." Sections "Implications for Hyperscalers and Labs" onward are NOT captured. The core margin/Bedrock data is in the free portion.
- **Bias flag:** AI-bull house view; the piece is structurally favorable to AWS/Amazon and Anthropic (SemiAnalysis has covered Anthropic positively and sells AI-economics models). Most headline figures (Bedrock $/MW, run-rate, EBIT %) are SemiAnalysis ESTIMATES, not company-disclosed — treat as directional. The GCP "accounting illusion" point is a genuinely useful, falsifiable check on the GCP-margin bull case. NO analyst price targets in the piece.

## Wiki updates suggested (NOT yet applied)
- **[[AMZN]]** — add bull-case bullet: AWS margin inflection (+213 bps Q/Q) driven by Bedrock/Anthropic TaaS mix + Trainium vertical integration; Bedrock ~$5.5B run-rate, ~30% of AWS GP step-up on ~4% of revenue. Add bear caveat: figures are third-party estimates, concentration risk on a single lab (Anthropic = 80-90%+ of Bedrock).
- **[[cloud-hyperscalers]]** — add a "Margin divergence: TaaS vs IaaS" section comparing AWS vs Azure vs GCP mix (10% / 27% / 36% AI revenue) and the GCP accounting-illusion ($5.4B training cost outside GCP). Flag MSFT Azure freeze / OpenAI-backlog-vs-capacity (2.5x) as drag.
- **[[GOOGL]]** — add bear/caveat note: reported GCP margins flattered by ~$5.4B DeepMind/Gemini training cost bucketed at Alphabet level, not in GCP segment.
- **[[MSFT]]** — note Azure datacenter freeze (~12mo growth) and OpenAI-backlog-vs-capacity mismatch as relative-margin drag vs AWS.
- **[[inference-economics]]** — Anthropic inference gross margin path (-94% 2024 → 38% 2025 → mid-60s% now) is strong evidence inference is becoming structurally profitable at the frontier; Trainium offtake (50%+ of Bedrock) lowers cost.
- **Contradiction to watch:** none direct, but cross-check the Anthropic mid-60s% inference margin claim against [[inference-economics]] and the broader "AI doesn't have ROI" (Zitron) bear before treating as settled.
