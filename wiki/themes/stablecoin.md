---
type: theme
tags: [stablecoin, crypto, fintech, payments]
last_updated: 2026-06-30
last_full_review: 2026-06-30
sources: 2
conviction: medium
---

# Stablecoins

## What this is
Dollar-pegged tokens (USDC, USDT, and now the consortium **Open USD**) that move value on public blockchains. The investable questions for this wiki are narrow: **who captures the reserve float**, **which distribution wins**, **how regulation treats the yield**, and **which public equities (or chains) benefit** — not the tokens themselves (crypto is outside the equity core; tracked as adjacency).

## Why it matters now (2026)
The economic model is under simultaneous attack from two sides, which is why [[CRCL]] (USDC issuer) is ~52% off its high:
1. **A 140-firm consortium ("Open Standard") launching Open USD (OUSD)** — Visa, Mastercard, Stripe, BlackRock, BNY, Standard Chartered, **Coinbase**, Ripple, Google, Shopify, Klarna ([[2026-06-30-open-usd-consortium-vs-circle]]). It **shares reserve yield with adopting businesses** and brings the **payment-rail distribution** incumbents lack.
2. **Regulation on the yield** — GENIUS Act framework + CLARITY-Act drafts threatening to ban interest/rewards on stablecoins (drove an −18% CRCL day in March 2026). Reserve yield *is* the issuers' revenue.

## Key drivers
- **Reserve float = the prize.** Issuer revenue is the interest earned on the T-bill reserves backing the coin. Rate-sensitive; whoever holds the float (and keeps vs. shares the yield) wins the economics.
- **Distribution, not the token, is the moat.** Stablecoins are commoditized at the token level (all $1-pegged, fiat-backed); the durable edge is *where they're accepted and minted* — exchanges (Coinbase), card networks (Visa/Mastercard), checkout (Stripe/Shopify).
- **Regulatory posture** — GENIUS Act legitimizes compliant issuers (favors Circle vs. Tether) but a yield ban compresses the whole model; the consortium's "share yield with *businesses* not *users*" design may route around a user-yield ban.
- **Throughput** — per the BG2 framing ([[2026-06-20-bg2-ai-bubble-stablecoin]]): card networks do ~50k TPS vs. base-layer chains <4k TPS — a scaling gap that favors high-throughput L1s/L2s for real payment volume.

## The competitive map
| Player | Public equity | Model | Status |
|---|---|---|---|
| **USDC** | [[CRCL]] (Circle) | Compliant first-mover; *keeps* reserve yield (shares ~half with Coinbase) | #2 by volume; under attack |
| **USDT** | (Tether, private) | Offshore, opaque reserves; dominant volume | #1; not in the consortium |
| **Open USD (OUSD)** | (Open Standard, partner-governed) | **Shares yield with adopters**; multi-chain; 140-firm distribution | Announced 2026-06-30; no firm launch date |
| **PYUSD** | [[PayPal]]* | PayPal-distributed | minor |

\*not a wiki page.

## Who captures the value (the economics)
- **Float yield → the issuer / its partners.** Circle keeps it (minus the Coinbase split); Open USD pushes nearly all of it to adopters — which is precisely why the consortium can out-distribute Circle.
- **Distribution rents → the rails** (Visa/Mastercard/Stripe/Coinbase). The Open USD thesis is that these firms would rather *own a share of the float economics* than pay Circle to use USDC.
- **NOT the chains directly** — see below.

## Chain-settlement implications — and the Solana question
Open USD launches **natively on Solana day one**, then Base / Polygon / Stellar. Does that pump the L1 token (e.g., **SOL**)?
- **Narrative tailwind: yes, modest.** Being the chosen day-one chain for a Visa/Mastercard/BlackRock/Coinbase stablecoin is a real credibility stamp for *Solana-as-settlement-rail* — it strengthens the "Solana wins payments" bull case and pulls builders/issuers toward it.
- **Direct token-price linkage: weak.** Stablecoin transfers pay trivial fees; the SOL fee-burn/demand from OUSD volume is tiny vs. SOL's market cap, and **the float yield accrues to the issuer, not to SOL holders.** Multi-chain deployment also means Solana isn't exclusive.
- **The durable version:** *if* OUSD scales AND Solana keeps the dominant share of its settlement, the second-order ecosystem growth (more DeFi, more issuers, more activity) is the real, slower tailwind — that's the thing to track, not the launch headline. SOL price is still driven more by crypto-beta / ETF flows / reliability than by one stablecoin.

## Beneficiaries / public-market expressions
- [[CRCL]] — the *most exposed* (negatively) — its core economics are the target.
- [[COIN]] — ambiguous: in the consortium (upside) *and* earns ~half of USDC's reserve yield (downside if USDC shrinks). A hedge that's bad for Circle either way.
- No clean *equity* for "Solana wins settlement" — crypto-native (SOL, SOL ETFs, SOL-treasury cos) sit outside the wiki's equity focus.

## Risks / counter-thesis
- **Network effects are sticky** — USDC/USDT liquidity, integrations, and trust don't transfer overnight; Open USD is unproven (no date, undisclosed reserves/custodian/regulated entity).
- **Consortium coordination** — 140 partner-governed firms is a herding-cats risk.
- **Regulatory whipsaw** — a hard yield ban could compress *all* issuers, consortium included.

## Open questions
- Does Open USD actually ship with disclosed reserves + a regulated entity, and on what timeline?
- Does Coinbase meaningfully shift volume off USDC (the [[CRCL]] kill-switch)?
- Does the yield-ban regulation land — and does the "share-with-businesses" design survive it?

## Related
[[CRCL]] · [[COIN]] · [[overview]] · [[ai-bubble-debate]]

## Sources
- [[2026-06-30-open-usd-consortium-vs-circle]] — the Open USD consortium launch
- [[2026-06-20-bg2-ai-bubble-stablecoin]] — BG2: rewards-as-interest, GENIUS Act, throughput gap, hyperscaler re-entry
