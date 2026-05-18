---
type: analysis
tags: [playbook, nvda, earnings, may-2026, pre-mortem]
last_updated: 2026-05-14
last_full_review: 2026-05-14
sources: 0
event_date: 2026-05-20
status: active-pre-event
---

# Playbook: NVDA Q1 FY27 Earnings — May 20, 2026 (AC)

> **Purpose of this page:** pre-commit decisions BEFORE the event so reaction is mechanical, not emotional. Read this Wed May 20 morning. Don't make decisions during the AC release window — execute what's written here.

## Pre-event setup

| Variable | Value | Source |
|---|---|---|
| Earnings release | **2026-05-20 after close** | NVDA IR |
| Conference call | 2026-05-20 5:00pm ET | NVDA IR |
| Consensus revenue | **$78.8B** | Street consensus (May 14) |
| Consensus EPS (non-GAAP) | **$1.77** | Street consensus (May 14) |
| Implied YoY revenue growth | ~78% | vs Q1 FY26 $44.1B |
| Options expected move | **±12.9%** (≈±$28) | OptionCharts (May 14) |
| IV rank | 61 (elevated) | OptionCharts (May 14) |
| Put/call ratio | 0.84 (slight bull) | MarketBeat (May 14) |
| Polymarket implied beat prob | 90% | (May 14) |
| Stock as of May 14 close | ~$216–220 (ATH $217.80 May 8) | Market |
| **Macro confluence** | **$16B 20-year Treasury auction same day** | Treasury |

## Critical context

- AMAT just raised CY26 semi equipment growth from >20% → >30% (May 14) — **supply-side validation that NVDA's downstream demand is real**
- Cisco Q3 FY26 raised AI infra orders $5B → $9B (May 13) — networking-side confirmation
- 30y Treasury auctioned at 5.046% with soft demand (May 14) — bond market is the offsetting bear signal
- Anthropic ARR $9B → $30B in one quarter (May 13 CFO disclosure) — model-lab demand is accelerating
- Trump-Xi summit cleared H200 sales to 10 Chinese firms (May 14) — China commentary on call is critical

## ⚠️ 2026-05-18 MACRO-OVERLAY UPDATE — rates are now the dominant variable

**Today's cross-asset move materially changes the expected NVDA reaction**:
- **JGB 10Y +9bps to 2.793%** (highest in years) — BoJ trade is front-running by 30 days
- **30Y UST at 1-year high** — global duration repricing
- **Memory cohort -5 to -7%** on capacity-tightness comment misread as bear
- **NVDA -4.4% to $225** on rates + pre-earnings de-risking, not on fundamentals
- See [[2026-06-16-boj-decision]] acceleration note dated 2026-05-18

**Implication: Scenario A becomes harder to realize even on a strong beat.**

| Original probability | Revised 2026-05-18 | Driver |
|---|---|---|
| Scenario A: 40% | **25-30%** | Strong beat may only get +5% (not +5-15%) if rates climb through the print |
| Scenario B: 35% | **45-50%** | Most likely outcome; chop dominated by macro |
| Scenario C: 20% | 20-25% | Downside dampened by pre-positioning (crowd already short) |
| Scenario D: 5% | 5% | Unchanged |

**What this changes about the playbook**:
- **NVDA $240C May 22 (YOLO position)**: expected value materially negative now. Don't add. If holding, set -50% hard stop and forget.
- **MU at -6% today is a contrarian add** (consistent with [[bottleneck-roadmap]]) — Seagate "factories can't keep up" comment is structurally bull for HBM, not bear.
- **Hedge selection shift**: FXY July call spread (from BoJ playbook) is now structurally cheaper than NVDA puts for the same expected dollar payoff. Use BoJ hedge stack, not NVDA-specific event hedge.
- **The Scenario A → B probability shift is rates-driven, not fundamentals-driven.** If Jensen confirms Vera Rubin demand strong + Q2 guide $87B+, the *fundamentals* are still Scenario A even if the *stock reaction* is muted by macro.

## What to watch on the call

1. **Gross margin trajectory.** Q4 FY26 GAAP GM was 73.0%. Any guide below 72.5% = bearish; >74% = bullish.
2. **Vera Rubin demand commentary.** Specific 5GW+ customer commits = bullish; vague language = neutral.
3. **China H200 shipment update (UPDATED 2026-05-15 — now more important).** Setup: US approved H200 to ~10 China firms (75K chips each); China NOT YET approved purchases (Trump: "they want to develop their own"). **Bullish:** Jensen confirms shipments imminent OR Q2 guide assumes ~$5-10B China contribution. **Neutral:** "evaluating" / "discussions continuing" language. **Bearish:** explicit acknowledgment China revenue is off the table for FY27.
4. **Q2 FY27 guide.** Consensus implies ~$85B. Guide < $82B = bearish; > $88B = strong bullish. **Sub-question:** does the guide include or exclude China H200 contribution? Ask in Q&A.
5. **Capex commentary about customer commitments.** Any "customers asked us to pull forward" = bullish; any softening = bearish.
6. **Q&A: pricing power.** If analysts press on Blackwell pricing vs Hopper and answers are evasive = bearish setup for Q2.
7. **Bill-and-hold / revenue recognition (NEW 2026-05-15 per Zitron Tech Report).** Zitron alleges NVDA may be counting revenue on GPUs sitting in warehouses awaiting DC commissioning. SEC ASC 606 has specific rules on bill-and-hold (customer must request delay; title transferred; no obligation to repurchase). **Watch the call for:** (a) any analyst question about deferred-delivery / un-deployed shipped inventory; (b) any change in language around "delivered but not deployed"; (c) deferred revenue line item in the 10-Q. Material if true — could mean revenue is overstated. **Bullish signal:** clear language that all shipped revenue is deployed and operational. **Bearish signal:** evasive or technical language about delivery vs deployment.

## Pre-committed scenarios

### Scenario A — Strong beat + raised guide (probability ~40%)

**Triggers (need 3+ to qualify):**
- Revenue > $80B
- Non-GAAP EPS > $1.85
- Q2 guide > $85B
- Gross margin > 73% (stable or expanding)
- Vera Rubin commentary names specific customer commits
- China H200 shipments confirmed with revenue contribution

**Expected stock reaction:** +5–15% next day (toward $230–$245)

**Pre-committed actions:**
- **NVDA structural (7% position):** HOLD. Do not trim — bull thesis intact.
- **NVDA $240C May 22 (YOLO 3.5%):** trim 1/2 at +100% (premium $20–22). Let runner go for +200% target.
- **Downstream beneficiaries — confirm bull/high:** [[AMAT]], [[KLAC]], [[LRCX]], [[TSM]], [[CRWV]], [[NBIS]] all stay structural.
- **China-exposed names:** [[AVGO]], [[TSM]] get positive read-through; consider modest adds if pullback.
- **Memory ([[MU]], [[SNDK]]):** positive read-through but DO NOT add at peak P/E — cycle-peak warning intact.
- **Hedges:** close out any QQQ/NVDA put spreads at next-day open if profitable; let cheap VIX hedges expire.
- **20-year auction same day:** if auction clean too, market melts up — let it. If auction tails, equity probably ignores; watch 30y level.

### Scenario B — In-line / mixed (probability ~35%)

**Triggers:**
- Revenue $77–80B
- EPS $1.75–1.85
- Guide $82–85B
- Gross margin 72.5–73%
- Mixed Vera Rubin / China commentary

**Expected stock reaction:** -3% to +5% (chop)

**Pre-committed actions:**
- **NVDA structural:** HOLD.
- **NVDA $240C May 22:** likely stops out at -50% (premium $4-5) over the following 24-48hr as IV crushes. **Hard exit by May 22 close regardless.**
- **Downstream:** no changes; conviction unchanged.
- **Hedges:** keep event hedges through May 21 IV crush, then assess.
- **GM commentary is the tell.** If GM guided down materially in this scenario, **treat as Scenario C** for action mapping.

### Scenario C — Disappointment / soft guide (probability ~20%)

**Triggers (any of):**
- Revenue < $77B
- EPS < $1.70
- Q2 guide < $80B
- Gross margin guide < 72%
- Vague/cautious Vera Rubin commentary
- China H200 revenue "delayed" or "uncertain"

**Expected stock reaction:** -5% to -15% next day (toward $185–$205)

**Pre-committed actions:**
- **NVDA structural:** trim 20% **if and only if stock breaks $200** in the next 2 sessions. If stock holds $200, hold — thesis durations are 18-24 months; one print doesn't break it.
- **NVDA $240C May 22:** HARD EXIT at -50% loss the morning after. **Do not "hold and hope."**
- **Downstream — selective trim:**
  - Memory ([[MU]], [[SNDK]]): trim 25% — cycle-peak P/E means downside is amplified
  - Neoclouds ([[CRWV]], [[NBIS]]): trim 25% if no idiosyncratic catalyst; keep 75%
  - WFE ([[AMAT]], [[KLAC]], [[LRCX]]): HOLD — their guide already validated separately (AMAT >30% CY26)
  - [[ASML]]: HOLD — 2028+ thesis independent of one NVDA quarter
- **Hedges:** keep VIX/put spreads open; let them run.
- **20-year auction same day:** if also tails = **compound shock scenario.** Trim YOLO bucket to 10% (from 19%); raise cash buffer to 5%.

### Scenario D — Black swan / extreme reaction (probability ~5%)

**Triggers:**
- Either side >20% move (e.g., +25% gap up on massive Vera Rubin commits, or -25% on shock)

**Pre-committed actions:**
- **DO NOT TRADE in the first 60 minutes.** Liquidity is fake during opening auctions on event days.
- After 10:30 AM ET, assess: is the move structural (thesis change) or technical (positioning unwind)?
- Structural change in thesis: follow Scenario A or C actions, sized up
- Technical/positioning: let the dust settle; consider fading the extreme

## Position-by-position cheat sheet

Copy this card to your phone before May 20:

| Position | Scenario A | Scenario B | Scenario C |
|---|---|---|---|
| NVDA core (7%) | Hold | Hold | Trim 20% if breaks $200 |
| NVDA $240C May 22 | Trim 50% at +100% | Stop out at -50% by May 22 | Hard exit at -50% next AM |
| AMAT / KLAC / LRCX | Hold | Hold | Hold |
| ASML | Hold | Hold | Hold |
| MU / SNDK | Hold (don't add) | Hold | Trim 25% |
| CRWV / NBIS | Hold | Hold | Trim 25% |
| TSM | Hold | Hold | Hold |
| AVGO | Hold; consider adding on pullback | Hold | Hold (Q2 print June 3) |
| Construction (FIX/EME/PWR) | Hold | Hold | Hold (defensive) |
| Hedges (see [[hedging-risk]]) | Close out next AM | Hold through May 22 IV crush | Hold and add |
| Dry powder | Deploy in pullbacks | Hold | Hold (raise to 5%) |

## Three questions to answer NOW (before the print)

1. **What's my hard stop on the NVDA $240C calls?** → **-50% premium loss = exit no matter what.** No "wait one more day."
2. **What's my trim trigger on NVDA structural?** → **Stock breaks $200 in any of the 2 sessions after print = trim 20%.** Above $200, hold.
3. **If NVDA beats but the 20-year auction tails badly, what do I do first?** → **Close NVDA $240C at open the next morning** (lock in IV-crush-resistant gain). Then assess equity-side response.

## What this playbook is NOT

- Not a stance change — NVDA stays bull/high regardless of Q1 outcome unless the print structurally invalidates the 18-24mo thesis (only Scenario C extremes do that).
- Not a market-timing tool — it's an event-response framework.
- Not a substitute for thinking — if commentary surprises in a direction not captured here, re-evaluate before acting.

## Related
[[NVDA]] · [[hedging-risk]] · [[fed-policy]] · [[2026-06-10-cpi-binary]] · [[overview]] · [[feedback-log]]

## Post-event update protocol

After May 20 close + May 21 morning:
1. Update this page with **what actually happened** vs each scenario
2. Mark which scenario hit + which actions were executed
3. Append outcome to [[feedback-log]] as ⏱️ / ✅ / ❌ / 〰️
4. Roll the lessons forward into the June 10 CPI playbook
