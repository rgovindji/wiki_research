---
type: theme
tags: [hedging, risk, defensive, volatility, late-cycle]
last_updated: 2026-05-14
last_full_review: 2026-05-14
sources: 0
conviction: high
---

# Hedging & Risk Coverage

## Why this page exists

Until 2026-05-14 the wiki was **100% long-biased.** Every framework page modeled what to buy; none addressed what to do when the bear case played out. With **5 of 6 late-cycle warning indicators firing** (per [[ai-bubble-debate]]) and the **30y Treasury auctioned above 5% with soft demand** (per [[fed-policy]]), that's a contradiction worth fixing before the May 20 NVDA print and June 10 CPI binary.

**Hedging is insurance, not a directional bet.** The wiki's central long thesis (AI capex acceleration, semiconductor bottleneck cascade, structural compounders) is intact. Hedging is what protects realized gains from short-window tail risks while the long thesis plays out over 18-24 months.

## When to hedge — the indicator framework

Cross-reference [[ai-bubble-debate]] late-cycle warning indicators:

| Indicators firing | Hedge sizing | Mode |
|---|---|---|
| 0-2 of 6 | 0% — no hedges needed | Risk-on |
| 3-4 of 6 | 1-3% in event-window hedges only | Watch |
| **5 of 6 (CURRENT — May 2026)** | **5-10% in mixed hedges** | **Defensive caution** |
| 6 of 6 | 10-15% + raise cash to 10% | Defensive aggressive |

**Current state:** 5/6 firing — small-cap AI speculation, IPO oversubscription, retail "undervalued P/E" on memory, "trillion-dollar club" rhetoric, geopolitical tail. **Not firing:** GPU rental softening (rentals still tight, +40% in 5 months). So we're in **Defensive caution** mode.

## Hedge categories (ranked by current applicability)

### Tier 1 — Currently recommended

#### Cash / T-Bills (the underrated hedge)
**Instruments:** BIL (1-3mo T-bills), SHY (1-3yr Treasuries), SGOV (0-3mo T-bills), or direct money-market
**Current yield:** ~4.75-5.00% (matches Fed funds upper bound)
**Cost of carry:** Zero — you're getting paid to hold

**When to use:** Always. The dry powder that lets you deploy on Scenario C (NVDA disappoint) or Scenario 3 (CPI accelerating) is the highest-value hedge in the toolkit because it's the only one with positive carry.

**Recommended sizing (May 2026):** 3-5% of portfolio in BIL/SGOV

#### Put spreads on QQQ (event-window hedge)
**Instruments:** QQQ put spreads expiring May 23 (NVDA event-window) + late June (CPI event-window)
**Current QQQ:** ~$555 (as of May 14)
**Recommended structures:**
- **NVDA event hedge:** QQQ May 23 540/520 put spread — cost ~$3 net debit, max payoff $20 = ~6.7x. Pays if NVDA disappoint + index follow-through.
- **June 10 CPI hedge:** QQQ June 27 530/500 put spread — cost ~$4 net debit, max payoff $30 = ~7.5x. Pays if accelerating CPI cracks the index.

**When to use:** Around binary catalysts with elevated IV. Defined-risk; loses 100% if the event passes uneventfully.

**Recommended sizing:** ~1-2% of portfolio in combined event hedges

#### VIX call spreads (volatility-spike hedge)
**Instruments:** VXX, UVXY (avoid for long holds — daily reset decay), or **VIX option spreads** for cleanest risk
**Current VIX:** ~17 (low-ish given elevated stock price + late-cycle signals)
**Recommended structures:**
- **VIX July 22/30 call spread:** cost ~$1, max payoff $8 = 8x. Pays if VIX spikes to >22 on June 10 CPI or earlier crash.

**When to use:** When VIX is unusually low relative to underlying signals (i.e., now — VIX 17 with 5/6 indicators firing is complacent pricing).

**Recommended sizing:** ~0.5-1% in VIX call spreads

#### Gold (Fed credibility hedge)
**Instruments:** GLD (gold ETF), GDX (gold miners — levered)
**Current gold:** ~$3,400/oz (May 2026 — already elevated)
**Why it's a hedge:** Gold rallies when (a) real rates fall (Fed cuts), (b) dollar weakens (Fed credibility loss), (c) inflation expectations re-anchor higher

**Specific use case:** The "Warsh capitulates → cuts into hot inflation" 20% tail in [[fed-policy]]. If that scenario plays out, gold is the cleanest single hedge.

**Recommended sizing:** 1-3% in GLD as structural late-cycle position

### Tier 2 — Situational

#### NVDA-specific put spreads
**Use case:** Direct hedge on the 7% NVDA structural position around May 20 earnings
**Recommended structure:** NVDA May 23 200/180 put spread — cost ~$2-3, max payoff $20 = 7-10x
**Why over outright puts:** IV crush after earnings would erode outright put value; spreads cap the IV-crush damage

**Recommended sizing:** ~0.5-1% if you want event-specific NVDA hedge

#### Sector rotation (defensives)
**Instruments:** XLU (utilities), XLP (staples), XLV (healthcare)
**When to use:** Multi-month/quarter defensive tilt, not single-event hedge
**Limitation:** This is asset allocation, not hedging — it's opportunity cost vs the AI growth thesis

**Recommended:** Not adding now (wiki growth thesis still favored), but flag as available

### Tier 3 — Currently NOT recommended

#### Long-duration Treasuries (TLT, ZROZ)
**Why not now:** The 30y > 5% with soft auction demand means TLT bleeds while waiting for the rate-cut trade. Wait for a clear signal (June 10 CPI cool scenario, or hard equity break) before adding.

#### Leveraged inverse ETFs (SQQQ, SDS, SPXS)
**Why not:** Daily-reset decay destroys long-hold value. Only useful as 1-3 day tactical positions, which is harder to time than just buying put spreads.

#### Covered calls on high-conviction names
**Why not:** Selling calls on NVDA / TSM / etc. caps the upside on the wiki's highest-conviction names. The wiki's stance is bull/high on these — capping upside contradicts that. Use cash and puts instead.

#### Naked single-stock puts
**Why not:** Concentrated risk. Use spreads instead.

## Recommended hedge stack (current — May 14, 2026)

Total ~6-9% of portfolio in hedges + ~3-5% in cash = ~10% defensive sleeve

| Hedge | Sizing | Purpose | Window |
|---|---|---|---|
| **BIL / SGOV** | 3-5% | Dry powder + positive carry | Always-on |
| **QQQ May 23 540/520 put spread** | 1% | NVDA event hedge | Through May 23 |
| **NVDA May 23 200/180 put spread** | 0.5-1% | Direct NVDA hedge | Through May 23 |
| **QQQ June 27 530/500 put spread** | 1.5% | June 10 CPI event hedge | Through June 27 |
| **VIX July 22/30 call spread** | 0.5-1% | Vol-spike insurance | Through July |
| **GLD** | 1-2% | Fed credibility tail hedge | Structural |

## Smart-money macro hedging signal (NEW 2026-05-17 PM)

Per Q1 2026 13F filings (via [[2026-05-17-robotics-multi-agent-batch]] context):
- **Dan Loeb (Third Point) established large SPY PUT position** — portfolio-level macro hedge
- **Berkshire Hathaway max-defensive**: portfolio $274B → $263B; trimmed Apple; exited Amazon + UnitedHealth + Domino's + heavy Chevron sells; top 5 holdings now 68% of portfolio = **cash hoarding**
- **Point72 (Steve Cohen) rotating defensive**: bought TransDigm (aerospace) + Equinix (defensive data center)

**Which means**: 3+ tier-1 fundamental smart-money funds are positioning **defensively** for Q2 2026. Combined with our [[bank-of-japan]] June 16-17 catalyst + [[ai-bubble-debate]] Damodaran "AI correction worse than dotcom" framework + the NVDA 280x forward PE + insider selling cluster — the **risk-asymmetry tilt is toward more hedging, not less, into June**.

**Add to falsifiable triggers** for hedge sizing-up:
- Q2 2026 13F filings (filed mid-August) show *more* smart-money defensive positioning = raise hedge sizing
- Q2 13Fs show smart money UNWINDING SPY puts = lighten hedges

## BoJ June 16-17, 2026 hedge overlay (NEW 2026-05-17 PM)

Per new [[bank-of-japan]] page + [[2026-05-17-boj-carry-trade-risk]]: **BoJ rate decision June 16-17 is the most-actionable scheduled tail-risk catalyst in 2026**. Carry-trade unwind probability ~65-70% per subagent research; +90% of pre-Aug-2024 yen-carry positions remain (~$500B per MS). USD/JPY at 158.76 (May 17); meeting consensus 25bp hike (priced in via swaps). Path-risk = a faster path (50bp) or hawkish forward guidance.

**Add to hedge stack ahead of June 16-17**:

| Hedge | Sizing | Purpose | Window |
|---|---|---|---|
| **FXY June 27 78/82 call spread** OR **YCS puts** | 0.5-1% | Direct yen-strength catalyst exposure | Through June 27 |
| **VIX July 22/30 call spread expanded to July 30 expiry** | (raise existing 0.5-1% → 1-1.5%) | Multi-week vol risk if unwind extends past flash event | Through July 30 |
| **Trim highest-multiple AI names**: NVDA (+32% off Mar low), MU (+154% YTD), CRWV/NBIS | 1-2% partial trim | Reduce duration-sensitive exposure pre-meeting | Pre June 16 |
| **Long defensive ETF (XLU / XLP)** | 1% | Inverse-correlated rotation hedge | Through July |

**Why this matters for the wiki**: positions are concentrated in high-multiple AI/tech ([[NVDA]] 280x forward, [[MU]] +154% YTD, [[CRWV]] / [[NBIS]] premium-growth, [[SOITEC]] +447% YTD). These are exactly the names that get sold first in a duration shock. The Japanese institutional holders (GPIF $1.8T, life insurers) are a meaningful second-order flow risk — repatriation on yen strength = forced selling of [[NVDA]] / [[MSFT]] / [[AAPL]] / [[GOOGL]] positions.

**Catalyst-specific watch**:
- USD/JPY < 150 ahead of June 16 = yen self-correcting; BoJ pressure releases; can lighten the FXY leg
- USD/JPY > 158 ahead of June 16 = pressure builds; raise hedge sizing
- BoJ Ueda or board member hawkish drift speech post-G7 = leading indicator

**Adjusts to 5-6/6 indicators:** raise put-spread sizing 50%; add SPXS tactical layer; raise cash to 7-10%.
**Adjusts back to 3-4/6 indicators:** close event hedges; reduce VIX to 0.25%.

## Cost of carry — be honest about the bleed

Hedging is not free. Conservative estimates:

| Hedge | Annualized bleed if nothing happens |
|---|---|
| Cash / BIL | -0% (actually +4.75% yield) |
| QQQ put spreads (rolled) | ~3-5% on the notional hedged |
| NVDA put spreads (rolled) | ~5-8% on the notional hedged |
| VIX call spreads (rolled) | ~30-40% if VIX stays calm |
| GLD | ~0-2% (depends on real rates) |

**Total expected cost of a 7% hedge stack in a calm year:** roughly 0.3-0.5% of portfolio drag. Worth it if the bear case has even a 10% probability of a 10%+ drawdown.

## What this page is NOT

- Not a market-timing tool — hedges should be sized to the indicator framework, not to gut feel
- Not a guarantee against losses — even a fully hedged portfolio can lose money on basis risk and tracking error
- Not a substitute for position sizing — concentration is the enemy; hedging is the backup, not the plan
- Not a permanent fixture — when indicators drop back to 3-4/6, most hedges come off

## Position discipline rules

1. **Never hedge more than you've gained.** If portfolio is up 15% YTD, max hedge cost should be 1-2% of gains (cap on insurance premium).
2. **Don't roll hedges past their event.** May 23 QQQ put spread should close by May 23, not get rolled "in case."
3. **Take profits on hedges that work.** If VIX call spread goes +400%, take it — don't let "what if more" greed turn a winning hedge into a round trip.
4. **Don't hedge a position you should just sell.** If conviction on a name is medium → low, the answer is trim, not hedge.

## Related
[[ai-bubble-debate]] · [[fed-policy]] · [[2026-05-20-nvda-earnings]] · [[2026-06-10-cpi-binary]] · [[overview]] · [[valuation-environment]]

## Sources
- OptionCharts (NVDA / QQQ IV + expected move data, May 14, 2026)
- CBOE VIX historical context
- Wiki internal: [[ai-bubble-debate]] late-cycle warning indicators framework
