---
type: analysis
tags: [playbook, boj, japan, carry-trade, fx, macro, june-2026, pre-mortem]
last_updated: 2026-05-17
last_full_review: 2026-05-17
sources: 1
event_date: 2026-06-16
status: active-pre-event
---

# Playbook: BoJ June 16-17, 2026 Decision + Carry Trade Tail

> **Purpose of this page**: pre-commit hedge AND profit-seeking decisions BEFORE the BoJ meeting. June 16-17 is the **highest-leverage scheduled macro catalyst of 2026** because of the rebuilt yen carry trade (~$500B per MS estimates) and the wiki's concentration in high-multiple US AI/tech. Don't make decisions on June 16; execute what's written here.

> See [[bank-of-japan]] for the full framework, [[2026-05-17-boj-carry-trade-risk]] for the source synthesis.

## ⚠️ 2026-05-18 ACCELERATION NOTE — market is front-running this trade by 30 days

**The playbook's deploy-by-June-10 timeline is already late.** Today's cross-asset data:

- **JGB 10Y jumped +9bps to 2.793%** — highest in years; that's the BoJ-anticipation move arriving 30 days early
- **30Y UST at 1-year high** — global duration is repricing
- **USD/JPY still ~158** — the playbook's "full Tier 2 sizing" trigger is already active
- **Memory cohort selloff**: MU -6%, SEAG -7%, WDC -4.8%, SNDK -5.3% on Seagate CEO "factories take too long" comment at JPM conference
  - **The crowd is misreading this as bear**; the wiki's [[bottleneck-roadmap]] framework reads "capacity can't keep up" as **bull for HBM pricing**, not bear for demand
  - **This is exactly the cross-asset rates-driven selloff pre-positioning the BoJ trade would predict** — memory is duration-sensitive and high-multiple
- **NVDA -4.4% to $225** on the same rates move + pre-earnings de-risking

**Revised scenario probabilities after today's data:**
- Scenario A (vanilla + dovish): 30% (was 35%) — less likely as market keeps pricing hawkish path
- **Scenario B (vanilla + hawkish path): 35-40% (was 30%)** — biggest probability shift; market is pricing this now
- Scenario C (50bp or aggressive path): 15-20% (was 15%) — slightly higher given JGB momentum
- Scenarios D + E (hold): 10% combined (was 20%) — getting harder to argue BoJ holds at this JGB level

**Calendar acceleration — pull Tier 1 deployment forward**:
- Original playbook timing: "Establish all Tier 1 positions by June 5"
- **Updated timing: deploy Tier 1 this week (May 19-23)** — premium is cheaper now than after another 5-10bps of JGB drift
- Tier 2 sizing was conditional on USD/JPY > 158 — that condition is met TODAY

**2026-05-19 EOD update — 30Y UST yield at 2-decade high**:
- The duration repricing has spread beyond JGBs to the global long-end
- Russell 2000 + Nasdaq -1%; MAGS -1.40%; NVDA -1.3% to ~$222
- **Iran 14-point MOU is the cross-current variable**: if signed (45% probability), oil drops to $80-85, BoJ has less cover to hike hard, Scenario A probability rises and Tier 1 hedge stops paying. If rejected + escalated (25%), oil $130-150, BoJ Scenario C activates. **The Iran outcome may invalidate or amplify this whole playbook within 7-14 days.**
- Action: keep Tier 1 deployed but be ready to take FXY profits early on Iran-deal signing news (lock in 1-2x gain before reversal)

**New trigger watches (added 2026-05-18)**:
| Trigger | What it means | Action |
|---|---|---|
| JGB 10Y crosses 3.0% | Scenario C front-running confirmed | Activate Tier 3 (full aggressive); cap NVDA structural at current size |
| USD/JPY breaks 155 before June 16 | Yen strengthening ahead of meeting | Take half profits on FXY positions; let runner go |
| MU bounces +5% in next 5 days | Memory misread reverses | Add to MU on the read-through; reinforces bottleneck thesis |
| Trump-Xi summit explicit H200 framework | Removes one BoJ-compounding risk | Slightly reduce Tier 3 sizing |

**The connection between NVDA earnings (May 20) and BoJ (June 16)**:
NVDA's reaction Wednesday will be filtered through rates positioning regardless of print quality. If JGB 10Y keeps climbing through earnings, even a beat-and-raise NVDA print may only deliver +5% (not the +5-15% [[2026-05-20-nvda-earnings]] Scenario A modeled). **The two events are no longer independent — they're being traded as one rates story.**

---

## Pre-event setup

| Variable | Value | As of |
|---|---|---|
| Event | BoJ rate decision + Ueda press conference | June 16-17, 2026 |
| Current rate | 0.75% | April 28, 2026 |
| Vote at last meeting | **6-3** (3 dissenters for immediate 1.0%) | April 28 |
| Consensus expectation | **25bp hike to 1.00%** priced into swaps | May 17 |
| USD/JPY spot | **¥158.76** | May 17 |
| **JGB 10Y yield** | **2.793% (+9bps in one day; highest in years)** | **May 18** |
| **30Y UST yield** | **1-year high** | **May 18** |
| MS estimate of live yen-carry positions | **~$500B** (~90% of pre-Aug 2024 still on) | post-Aug 2024 |
| Subagent unwind-event probability | **65-70%** in June-July 2026 | this playbook source |
| **Front-run signal** | **Market pricing Scenario B already** | **May 18** |

## Scenario matrix — what to do in each case

The market has priced a vanilla 25bp hike. **The trade is in the *path*, not the *decision*.**

### Scenario A — Vanilla 25bp + dovish forward guidance (35% probability)
*"Hike, but emphasize gradual."*
- USD/JPY: **strengthens 2-3 yen** to ~155-156 then stabilizes
- Tech: **brief 1-3% intraday dip then recovers** within 24-48 hrs
- VIX: spikes briefly then bleeds back
- Carry trade: minor stress, no forced unwind
- **Wiki position action**: close FXY call spreads at small gain; let VIX position decay; **redeploy proceeds to add risk back** (cheap dip in our high-conviction names)

### Scenario B — Vanilla 25bp + hawkish path signal (30% probability)
*"Hike + 'we will continue to raise rates if data warrants' + dot plot shifts."*
- USD/JPY: **strengthens 5-7 yen** to ~152-153
- Tech: **5-8% correction** over 5-10 trading days
- VIX: sustained elevation 20-30 zone
- Carry trade: partial unwind, similar magnitude to Aug 2024 (~10-15% of positions clear)
- **Wiki position action**: **Capture profits on FXY calls** (≥3x return likely); roll VIX spreads further out; **trim 1-2% more from highest-multiple names** ([[NVDA]], [[MU]]); use proceeds for **high-conviction adds at -10%** ([[NBIS]], [[CRWV]] specifically)

### Scenario C — 50bp surprise hike OR aggressive forward path (15% probability)
*"BoJ accelerates timeline; Ueda invokes inflation persistence."*
- USD/JPY: **collapses 8-12 yen** to ~146-150
- Tech: **10-15% correction** over 2-4 weeks; multiple compression real
- VIX: spike to 30-45 zone; sustained
- Carry trade: substantial unwind (30-50% of positions clear); similar to or exceeding Aug 2024 violence
- **Wiki position action**: **Major hedge realization** — FXY calls 5-10x; VIX spreads 3-5x; trim defensive positions and use proceeds + hedge profits to BUY high-conviction names ([[NVDA]], [[TSM]], [[ASML]]) at distressed levels. **This is the "buy the dip with hedge profits" scenario the playbook is designed for.**

### Scenario D — Hold + dovish guidance (15% probability)
*"BoJ blinks; yen weakens further to 162+."*
- USD/JPY: weakens 2-4 yen to ~161-163
- Tech: rallies 2-4%
- VIX: drops
- Carry trade: re-loaded; tail risk pushed to July or September
- **Wiki position action**: close FXY position at loss (-50 to -80%); roll VIX spreads to September meeting; **add to FXY positions at lower prices for next BoJ meeting** (July 30-31 or September 18-19); BoJ retreat just compounds 2027 risk

### Scenario E — Hold + hawkish guidance (5% probability)
*"BoJ delays the hike but doubles down on path signaling."*
- USD/JPY: modest yen strengthening (~157)
- Tech: muted reaction
- VIX: slight elevation
- **Wiki position action**: hold hedge stack; June was a feint, the real catalyst is the next meeting

> **Pricing the contracts**: see [[hedging-risk]] "Options pricing + education tools" section for the free calculators (OIC, OptionStrat, OptionsProfitCalculator) to price specific strikes/expiries at deploy time. IV changes daily — re-price before executing.

## Pre-event positioning (deploy BY June 10, 2026)

### Tier 1 — Pure Hedge (defensive, ~2% portfolio cost, all-or-nothing payoff)

| Instrument | Sizing | Strike/expiry | Rationale | Cost |
|---|---|---|---|---|
| **FXY July 31 80/84 call spread** | 0.5-1% | Strikes ~3-5% OTM | Direct yen-strength exposure; 5-8x payoff in Scenario B; 8-15x in Scenario C | ~0.5% portfolio |
| **VIX July 30 22/30 call spread** | 0.5-1% | Through July expiry | Multi-week vol risk if unwind extends | ~0.5% portfolio |
| **QQQ July 18 530/500 put spread** | 0.5% | Through July expiry | Tech-specific Δ hedge | ~0.5% portfolio |

**Trigger to add**: USD/JPY remains above 158 going into June 10
**Trigger to lighten**: USD/JPY breaks below 150 ahead of meeting

### NEW 2026-05-17 PM — Japanese-exporter robotics cohort exposure

Per [[2026-05-17-robotics-multi-agent-batch]] Agent I: BoJ rate hike to 1.0% expected June 16-17 will strengthen yen by 2-5% → **2-5% gross margin compression for Japanese exporters absent price pass-through**.

**Most exposed Japanese robotics exporters**:
- **Harmonic Drive Systems (6324.T)** — +99.7% YoY May 2026; Tesla Optimus V3 in 14/28 actuators; 70%+ precision reducer share — **highest beta to yen strength + valuation re-rating risk**
- **Nabtesco (6268.T)** — RV reducer specialist; 60% global share
- **RNECY (Renesas ADR)** — most US-accessible Japanese robotics name
- **FANUC (FANUY ADR)** — industrial robot leader; already in post-correction recovery
- **NJDCY (Nidec OTC)** — motor leader

**Tactical add to Tier 2/3 playbook**: short selected Japanese robotics exporters via ADR puts (RNECY, FANUY) or trim long positions if held; **the BoJ rate decision is structurally bearish for these names** even if the broader carry-trade unwind is signaled (not shock).

### Tier 2 — Asymmetric Profit (moderate cost, larger upside, ~3-4% portfolio cost)

Building on Tier 1, ADD:

| Instrument | Sizing | Strike/expiry | Rationale |
|---|---|---|---|
| **Long [[MUFG]] / [[SMFG]] / [[MFG]] common (Japan bank ADRs)** | 1-2% combined | Underlying common | Japanese banks BENEFIT from BoJ hikes (NIM expansion); inverse-of-carry-unwind exposure |
| **Add longer-dated FXY Sept 18 78/86 call spread** | 0.5% | Through Sept | Captures September BoJ meeting as backup catalyst if June is non-event |
| **Trim [[NVDA]] / [[MU]] (highest multiples)** | 1-2% partial trim | Underlying | Reduce duration-sensitive exposure pre-meeting |
| **Add [[XLU]] or [[CEG]] / [[VST]]** | 1% | Underlying | Inverse-correlated defensive long; AI-power exposure as fallback |

### Tier 3 — Aggressive Profit (higher cost, leveraged to Scenarios B+C, ~5-6% portfolio cost)

Building on Tiers 1-2, ADD:

| Instrument | Sizing | Strike/expiry | Rationale |
|---|---|---|---|
| **Long-dated FXY Dec 19 80/90 call spread** | 0.5-1% | Through Dec | Captures full 2H 2026 BoJ path (June + July + Sept meetings) |
| **Short USD/JPY via FUTURE (futures account required)** | 0.5-1% | Sept contract | Direct, leveraged yen exposure (margin call risk; sizing tight) |
| **NVDA July 18 200/170 put spread** | 0.5% | Through July | Position-specific tail; NVDA at 280x forward = max duration |
| **Long [[NEM]] / [[GLD]]** | 1-2% | Underlying | Real-asset hedge if both BoJ AND Fed surprise |

## Entry/exit rules

### Pre-event entry (June 1-10)
1. Establish all Tier 1 positions by **June 5** to avoid event premium spikes
2. Add Tier 2/3 incrementally based on USD/JPY level:
   - USD/JPY > 158: full Tier 2 sizing
   - USD/JPY 153-158: 50% Tier 2 sizing
   - USD/JPY < 150: Tier 1 only; close FXY positions
3. Watch Ueda speeches between now and June 10 for hawkish drift — leading indicator

### Event execution (June 16-17)
- **Don't trade during the press conference** unless USD/JPY moves >3% in 5 minutes. Initial moves often reverse.
- Wait for **2-hour-post-meeting close** before adjusting positions
- Use overnight Asian session as the real signal — that's when domestic Japanese flows hit

### Exit triggers

| Trigger | Action |
|---|---|
| Scenario A confirmed (vanilla hike, dovish guidance) | Close FXY at small gain (~1-2x); let VIX/QQQ decay; redeploy to risk-on adds |
| Scenario B confirmed (vanilla + hawkish path) | Take FXY profits at 3-5x; roll VIX further out; partial puts close at gain; **add to NBIS/CRWV at -10% from current** |
| Scenario C confirmed (50bp or aggressive path) | **Capture all hedge profits at 5-10x**; convert to high-conviction LONG positions at distressed levels (NVDA, TSM, ASML target -15%) |
| Scenario D (hold + dovish) | Close FXY at loss (-50 to -80%); roll VIX to Sept; **add FXY for next meeting** at cheaper prices |

## What invalidates this playbook

- **BoJ emergency action before June 16** (unscheduled hike) — flip immediately to Scenario C playbook
- **USD/JPY breaks below 145** independent of BoJ (US weakness) — yen correcting on its own; BoJ pressure releases; close most hedges
- **Fed surprise cut before June 16** — differential narrows; carry trade tail risk amplifies separately; hold hedges
- **Iran war ceasefire + oil collapse** — removes April's BoJ inflation-upgrade rationale; hike probability declines
- **Major NIKKEI flash-crash before June 16** — front-running; possibly reduce hedge sizing as event-premium drops

## Cost-of-carry honesty

This is not free. Conservative bleed estimates:
- **Tier 1 (pure hedge)**: ~0.4-0.6% portfolio decay over 6 weeks if BoJ holds
- **Tier 2 (asymmetric)**: ~1-1.5% portfolio decay over 6 weeks if BoJ holds + JPN banks under-perform
- **Tier 3 (aggressive)**: ~2-2.5% portfolio decay over 6 weeks if BoJ holds + JPN banks under-perform

**Break-even math**: Tier 1 needs Scenario A or better to be even; Tier 2 needs Scenario B; Tier 3 needs Scenario C.

## Position-sizing discipline rule

Match tier to confidence:
- If you genuinely expect Scenario A (35%): only Tier 1 hedging makes sense
- If you genuinely expect Scenario B (30%): Tier 2 is the rational choice
- If you genuinely expect Scenario C (15%): Tier 3 is the rational choice
- Don't size Tier 3 if you only believe Scenario A is likely — you're paying for insurance you don't think you'll need

## Specific BoJ-hike-beneficiary tickers (for the asymmetric profit leg)

Japanese banks benefit from BoJ rate hikes via NIM expansion (their domestic loan book reprices faster than deposits):

| Ticker | Listing | Description | BoJ-hike exposure |
|---|---|---|---|
| MUFG | NYSE ADR | Mitsubishi UFJ — Japan's largest bank by assets | Direct |
| SMFG | NYSE ADR | Sumitomo Mitsui Financial Group | Direct |
| MFG | NYSE ADR | Mizuho Financial Group | Direct |
| BCS | NYSE | Barclays (cross-asset; not Japan but vol-positive) | Indirect |

**Caveat**: Japan bank ADR liquidity is modest; size positions accordingly. Underlying Tokyo-listed names (8306, 8316, 8411) require international broker access.

## Falsifiable watch triggers (between now and June 16)

| Date / event | What to watch | Implication |
|---|---|---|
| **2026-05-21+ Ueda G7 meetings** | Hawkish drift in his comments | Tier sizing up |
| **2026-05-30 BoJ Outlook Report** | Inflation forecast revision | If raised again, Scenario B/C probability up |
| **2026-06-01-10 USD/JPY level** | Above 158 = pressure; below 150 = release | Adjust tier sizing |
| **2026-06-05 Japan May CPI** | If hot (>2.5%), gives BoJ more cover | Hike probability up |
| **2026-06-10 US CPI** ([[2026-06-10-cpi-binary]]) | Hot US CPI → Fed pause → diff opens against yen | Compound risk; raise hedge sizing |
| **2026-06-12 BoJ blackout begins** | No more communication | What you have at this point is what you act on |

## Related
[[bank-of-japan]] · [[hedging-risk]] · [[fed-policy]] · [[2026-06-10-cpi-binary]] · [[2026-05-20-nvda-earnings]] · [[valuation-environment]] · [[NVDA]] · [[MU]] · [[CRWV]] · [[NBIS]] · [[SOITEC]] · [[AAPL]] · [[overview]]

## Sources
1. [[2026-05-17-boj-carry-trade-risk]] — primary subagent research (BCA, BIS, SocGen, Goldman, MS sources); current BoJ state; carry-trade size; Aug 2024 reference event
