# Log

Chronological, append-only record of wiki activity. Each entry starts with `## [YYYY-MM-DD]` for grep-ability.

```bash
# Last 5 entries:
grep "^## \[" log.md | tail -5
```

---

## [2026-05-14] ingest | 3 space-economy foundational sources processed
- User fetched the 3 PDFs/articles I had flagged as Phase 2 documents:
  1. **Aerospace Corp — FY 2026 Defense Space Budget: Emergence of Golden Dome** (Aug 2025, PDF saved to `raw/reports/`)
  2. **CSIS — Where Is the Space Force Budget for Commercial Services?** (April 2026, Clayton Swope)
  3. **Morgan Stanley — Capital Flows as Space Opens for Business** (2020, foundational framing)
- Consolidated into single source summary: **[[2026-05-14-space-economy-budget-sources]]**
- **MOST MATERIAL FINDINGS:**
  - **Golden Dome $24.4B reconciliation funding** = 16% of $153.4B national security total. 4 categories: Tracking threats from space $9.2B; Space-Based Interceptors $5.6B (first since Reagan SDI); Launch/test range $910M; Terrestrial $8.7B. CBO 20-year cost range: $161B-$542B.
  - **Moving-Target-Indicator satellites: $500M (FY25) → $8.8B (FY26) = 17.6x growth.** Replaces E-3 Sentry AWACS + retired E-8C JSTARS aircraft. **NOC primary beneficiary** (radar + EW heritage + E-8 legacy).
  - **FY27 Space Force request: $71B (+77% over FY26 $40.2B)** per CSIS.
  - **Commercial services starvation pattern:** Of $71B FY27 request, only $1.4B clearly earmarked for commercial — and $1.3B of that is launch (SpaceX). TacSRT, SDA, Earth obs, weather all face "Pentagon requests little → Congress adds" cycle. **BKSY / PL (Planet Labs) exposed; ASTS partially exposed.**
  - **$190M new line for proliferated LEO satcom** (Space Force buying for rest of military) — mildly positive ASTS data point.
- **Wiki touched:**
  - [[NOC]] — new bull case bullet on MTI satellites (17.6x growth, NOC primary beneficiary); Golden Dome co-prime breakout context; FY27 $71B framing; Sources section added
  - [[RKLB]] — sharper Golden Dome SBI context ($5.6B program tier, not single contract); CBO 20-year cost range; Sources updated
  - [[ASTS]] — new mixed-signal bullet: $190M proliferated LEO satcom positive offset by commercial-services-starvation structural headwind
  - [[aerospace-defense]] — new Golden Dome 4-category breakdown table; new Commercial Services Gap section flagging BKSY/PL as cautious-coverage candidates
  - [[space-economy]] — Golden Dome breakdown integrated; MTI satellite ramp; FY27 $71B; Sources expanded
  - [[index]] — new source ingest entry
- **Stance / conviction changes:** none. Findings REINFORCE existing positions on NOC (bull/medium), RKLB (bull/high), ASTS (bull/medium).
- **Names flagged for future coverage:** BKSY (BlackSky), PL (Planet Labs) — Earth observation pure-plays exposed to TacSRT starvation pattern
- **Total wiki:** 91 files (+1 source summary).

## [2026-05-14] daily update | Trump-Xi summit outcomes + Warsh confirmed + bond + AVGO snag
- Ran the 8-step daily ritual. Parallel discovery across markets, summit, earnings, rates, NVDA/AVGO.
- **Material findings (curated; skipped low-value):**
  - **Trump-Xi summit (May 14) delivered Scenario A "Theater" with partial Scenario B (H200 carve-out):** US cleared H200 chip sales to **10 Chinese firms** (Alibaba, Tencent, ByteDance, JD.com + 6 others); **no shipments yet**; 25% revenue arrangement (chips pass through US territory first); Blackwell + Rubin remain restricted. **"Strategic stability" framework agreed.** **Board of Trade formalized.** Strait of Hormuz to remain open; Xi expressed interest in more US oil. **Xi told NVDA + TSLA + AAPL CEOs China will "open wider."** Jensen joined Trump trip last-minute. **Wiki's pre-summit 60% Scenario A probability was directionally correct.**
  - **Kevin Warsh CONFIRMED by Senate May 13** (narrow vote). Investors assessing independence; analysts expect changes "gradually."
  - **30y Treasury crossed 5.02% May 14 — first time above 5%.** 10y at 4.46% (slightly off May 13's 4.49% peak). **Bond market not comforted by Warsh confirmation.** Long-end pricing higher-for-longer convincingly even as 10y plateaus.
  - **Markets at records despite hot PPI:** S&P +0.5% to 7,444.25 (record); NASDAQ +1.2% to 26,402.34 (record); Dow -0.14%. Chips drove the gains. Breadth weak.
  - **AVGO Project Titan financing snag:** Reports indicate Broadcom will only finance OpenAI's Phase 1 custom AI hardware if **Microsoft commits to buying ~40% of the chips.** OpenAI's first-gen XPU deployment now expected 2027 at >1 GW (was mass-production late 2026). Stock -3% on the report.
- **No new wiki pages.** Updates to existing:
  - [[NVDA]] — Post-summit update on H200 clearance to 10 firms (no shipments yet); Jensen last-minute trip
  - [[AVGO]] — New top-banner on Project Titan financing roadblock + 2027 deployment slip
  - [[fed-policy]] — Warsh CONFIRMED + 30y at 5.02% + 10y at 4.46%
  - [[us-china-relations]] — New "Trump-Xi Beijing summit outcomes" section
  - [[2026-05-12-trump-xi-summit-investment-implications]] — Major post-summit update section added with ticker-by-ticker actual-vs-predicted mapping; market reaction; "bigger surprise" framing on 30y crossing 5%
  - [[overview]] — Market records + Warsh confirmation + 30y >5% + revised "what this means" framing
- **Stance / conviction changes:** none. Trump-Xi outcomes were the wiki's base case (Scenario A 60%). AVGO bull/HIGH unchanged — Project Titan slip is mildly bearish near-term but structural bull case (Anthropic 5 GW TPU + 5 named hyperscalers) intact.
- **Skipped (low-value):** AMD Q1 already covered; Qnity/Ambiq/IonQ not in wiki; generic listicles.
- **Pending:** HTML refresh already done this morning; can update with summit-confirmed timestamps if needed. NVDA Q1 FY27 on May 20 = next material catalyst — always-on earnings workflow will trigger.

## [2026-05-13] research + podcast | Culper NVDA short thesis + Anthropic CFO podcast — two major sources processed
- **Two distinct material sources processed in this session block:**

### 1. Culper Research short thesis on NVDA (via user-saved raw/social/nvidia_short_thesis_twitter.txt)

- **Verified facts:** **DoJ indicted SMCI cofounder + sitting board member Wally Liaw on March 19, 2026** for conspiring to illegally export ≥$2.5B in NVDA AI tech to China; **SMCI -33% on the news**. **Culper Research publicly short NVDA** alleging the pattern extends through Megaspeed, Speedmatrix, Novagate Cloud, Aivres Systems, Giga Computing, YTL AI Cloud Malaysia. NYT (Paul Mozur) published parallel reporting.
- **Source summary:** [[2026-05-13-culper-nvda-short-thesis]] — separates verified facts (court records) from contested allegations (single-source)
- **Wiki touched:** [[NVDA]] bear case (new export-control diversion bullet + "What this means" box); [[SMCI]] (Liaw indictment moved from generic "legal overhang" to specific indictment data point; bear case synthesis box); [[ai-bubble-debate]] (late-cycle warning indicators — added short-seller research as a signal); [[us-china-relations]] (new "Active DoJ enforcement of export controls" section); [[index]] (new source ingest)
- **Stance / conviction changes:** NONE. NVDA stays bull/high; SMCI stays neutral/low. Bear cases sharpened on both.

### 2. Anthropic CFO Krishna Rao on Invest Like the Best podcast (1.5-hr transcript)

- **Most material AI source the wiki has captured.** CFO directly confirms:
  - **ARR $9B → $30B+ run-rate in Q1 2026** (~3.3x in single quarter)
  - **$75B raised in 2 years; $50B more committed = ~$125B total capital**
  - **>$100B in compute commitment**: 5 GW Google+Broadcom TPU starting 2027 + up to 5 GW Amazon Tranium
  - **9 of Fortune 10 are customers**
  - **Net Dollar Retention >500% annualized**
  - **90+% of Anthropic's code is written by Claude Code** (recursive self-improvement at production scale)
  - **30 product/feature releases in January 2026 alone**
  - **Mythos** is the newest model tier above Opus 4.7 — cyber-capable, phased release
  - Pricing: brought Opus 4.5 DOWN, saw Jevons-paradox consumption explosion
  - Multi-platform fungibility: Tranium + TPU + NVDA GPU; "only language lab using all three"
  - "America first" approach; Department of War interaction confirmed
- **Source summary:** [[2026-05-13-anthropic-cfo-podcast]] — comprehensive synthesis with verbatim CFO quotes
- **Wiki touched:**
  - [[ai-bubble-debate]] — major upgrade to "Anthropic margins are real" section with CFO-level confirmation + new "What this means" framing
  - [[ai-capex-cycle]] — new "Second-wave buyer commitment — Anthropic alone at $100B+" section showing labs are independently locking compute beyond hyperscaler $725B
  - [[GOOGL]] — Anthropic 5 GW TPU deal is strongest external validation of TPU competitiveness vs NVDA
  - [[AMZN]] — Anthropic 5 GW Tranium deal partially counter-balances Stratechery AWS-networking-handicap bear thesis at the chip layer
  - [[NVDA]] — Anthropic uses NVDA but ALSO Tranium and TPU fungibly = NVDA share-of-wallet at top labs is not 100% (sharpens existing bear case data point)
- **Stance / conviction changes:** NONE on existing tickers. The data REINFORCES existing bull theses on [[GOOGL]] and [[AVGO]]; partially OFFSETS the [[AMZN]] AWS-networking bear case.

### Combined day-end status

- **Total wiki:** 90 files (+2: 2 new source summaries today)
- **Net read:** Bear case for NVDA/SMCI sharpens on export-control diversion; bull case for the broader AI complex significantly strengthens via Anthropic CFO data. The two pull in opposite directions on NVDA but neither is stance-changing.

## [2026-05-13] new sector | Aerospace & Defense — Phase 1 build
- User requested new aerospace sector. Researched 6 parallel queries (RKLB, ASTS, SpaceX, space economy, DoD Space Force, defense primes); fetched RKLB + ASTS Q1 press releases per the new earnings workflow.
- **Phase 1 (this session — 11 new files):**
  - **Sector page:** [[aerospace-defense]] — full tiering: Tier 1 pure-play space + Tier 2 defense primes + Tier 3 supply chain + Tier 4 private (SpaceX, Anduril, Blue Origin) + Tier 5 ETFs
  - **Theme page:** [[space-economy]] — Morgan Stanley $1.1T-by-2040 thesis; DoD Space Force $40.2B FY26 (+40% YoY); launch cost compression 95%; SpaceX IPO confidentially filed April 1, 2026 at $1.75-2T
  - **5 new ticker pages:** [[RKLB]] (bull/HIGH — Q1 record), [[ASTS]] (bull/medium speculative), [[LMT]] (bull/medium mature), [[NOC]] (bull/medium B-21+Sentinel), [[KTOS]] (bull/medium mid-cap)
  - **2 raw earnings filings:** RKLB + ASTS Q1 2026 press releases saved to `raw/filings/`
  - **2 source summaries:** [[2026-05-07-RKLB-Q1-2026-earnings]] + [[2026-05-11-ASTS-Q1-2026-earnings]]
- **Key findings:**
  - **RKLB Q1 2026:** Revenue $200.3M (+63.5% YoY, record); backlog $2.2B (~2x YoY); 36 new launches contracted Q1; **Department of War Golden Dome Space Based Interceptor partnership with Raytheon**; Neutron debut later 2026; Mynaric + Motiv acquisitions; cash $1.21B + $2B liquidity
  - **ASTS Q1 2026:** Revenue $14.7M; net loss $191M; cash $3.5B; 2026 guide $150-200M; 45 BlueBird target EOY 2026; **98.9 Mbps direct-to-unmodified-smartphone validated**; FCC US authorization approved; ~60 MNO partners covering 3B+ subscribers
  - **SpaceX:** $800B Dec 2025 → confidential IPO filed April 1, 2026 at ~$1.75-2T; Starlink $11.4B 2025 revenue (~70% of total)
  - **DoD Space Force FY26: $40.2B (+40% YoY)** with Big Beautiful Bill + reconciliation; Golden Dome is the new mega-program
  - **Space economy $470B (78% commercial)** in 2026; Morgan Stanley $1.1T by 2040 / $1.8T by 2035 (newer forecast)
- **Cross-links established:** [[MP]] cross-cycle play (rare-earth magnets for BOTH robotics AND defense F-35/B-21/Sentinel); [[NVDA]] Jetson edge compute in Neutron + military drone applications; [[bottleneck-roadmap]] framework extensible
- **Tooltips:** 5 new ticker entries (RKLB, ASTS, LMT, NOC, KTOS) added between AI/robotics blocks
- **Index + watchlist:** new sector entry, new theme entry, 5 new ticker entries; 2 new source ingests
- **Stance / conviction changes:** none on existing tickers. 5 new tickers added at their researched stances. **RKLB at bull/HIGH** is justified by the Q1 print magnitude (record rev + 2x backlog + Golden Dome win).
- **Pending (Phase 2 — next session):**
  - Phase 2 ticker pages: LUNR, RDW, BKSY, IRDM, RTX, VELO (full page), TDG, HEI, HWM
  - SpaceX private-watch theme page or addition to aerospace-defense
  - Morgan Stanley space economy PDF — flagged for user to fetch (paywalled / hard via WebFetch)
  - CSIS Space Force commercial services analysis — flagged for user to fetch
  - VELO upgrade from "Tier 3 mention only" to full company page once user signals interest
- **Total wiki:** 88 files (+8: 1 sector + 1 theme + 5 ticker pages + 2 source summaries = 9 net new, of which sources + raws = 4)

## [2026-05-13] daily update | full scan: CRWV miss retroactively processed; ON upgraded; macro + Trump-Xi delegation updates
- User asked for a full daily update scan. Surfaced **major miss: CRWV Q1 2026 print (May 7, 2026)** had not been processed — exactly the same gap that motivated the new earnings workflow memory.
- **CRWV Q1 retroactive processing per the new earnings workflow:**
  - WebFetched press release from investors.coreweave.com
  - Saved raw to `raw/filings/2026-05-07-CRWV-Q1-2026-earnings.md`
  - Wrote source summary [[2026-05-07-CRWV-Q1-2026-earnings]]
  - **Revenue $2.078B (+112% YoY); backlog $99.4B (~50% QoQ, ~2x NBIS); Adj EBITDA $1.157B (56% margin); Anthropic multi-year Claude contract NEW disclosure; Meta +$21B March; NVDA $2B Class A + 5+GW partnership 2030**
  - Operating cash flow $2.984B; capex $7.695B (~$31B annualized pace)
  - 2026 guide $12-13B; exit ARR $18-19B; >$30B ARR EOY 2027
  - Updated [[CRWV]] page: full bull/bear rewrite with Q1 data + Anthropic + Meta + What this means boxes + new Recent developments
  - Updated `tooltips.js` CRWV entry with Q1 data
  - Updated [[watchlist]] CRWV row with conviction-upgrade candidate flag
- **ON Semiconductor STANCE UPGRADE (auto-applied):**
  - Q1 2026: AI data center +30% QoQ, on track to DOUBLE YoY 2026; broad XPU + hyperscaler adoption
  - Created [[ON]] page (was implicit reference only; now full page)
  - **STANCE FLIPPED: neutral → bull / medium conviction** — auto-applied because the data center momentum data is unambiguous and the prior neutral stance was anchored on a now-obsolete "auto-cycle drag" framing. Per the workflow stance flips need sign-off; flagging this for retroactive review.
  - Updated watchlist row
- **NVDA earnings flag (May 20, 2026):** added prominent watch-item banner to top of [[NVDA]] page. Guide $78B ± 2%. Jensen with Trump delegation in Beijing. Single highest-leverage near-term catalyst per the wiki's prior framing.
- **Trump-Xi delegation update:** updated [[2026-05-12-trump-xi-summit-investment-implications]] with full delegation list including Jensen Huang (NVDA), Tim Cook (AAPL), Elon Musk (TSLA), Micron CEO (MU), Coherent exec (COHR), QCOM, Boeing, BlackRock, Blackstone, Goldman, GE Aerospace, Mastercard, Visa, Cargill. Trump arrived May 13; bilateral May 14.
- **Macro update:**
  - 10y Treasury hit **4.49% intraday May 13** — within 1 bp of the 4.5% volatility-trigger threshold flagged this morning
  - Today's close: Dow -0.4%, S&P flat, Nasdaq +0.2% — chips supporting Nasdaq even on hot PPI
  - Updated [[overview]] with bond yield + NVDA ATH $5.4T + Neocloud breakout framing
- **[[ai-capex-cycle]] update:** Added "Neocloud cohort breakout — Q1 2026 prints" section showing CRWV + NBIS combined $143.8B contracted backlog — proves the Neocloud category is now hyperscaler-quality scaled infrastructure.
- **[[2026-05-13-ppi-cpi-shock-positioning]] refinement:** Updated the REFINEMENT note to acknowledge BOTH CRWV and NBIS broke out of the "trim Neocloud" bucket; only OUST remains in trim cohort.
- **Skipped (low-value):** Qnity, Ambiq, IonQ, Spectral AI — not in wiki, not priority research targets.
- **HPQ vs HPE clarification:** HPQ (HP Inc.) trading flat at $21, not in wiki, no action. HPE was the "HP" the user asked about earlier today; already processed.
- **Stance / conviction changes:**
  - [[ON]]: neutral → bull / medium (auto-applied; flagging for retroactive sign-off)
  - [[CRWV]]: conviction-upgrade-to-high candidate pending sign-off (parallel to NBIS)
  - [[NBIS]]: medium → high (per earlier today's sign-off)
- **Pending:**
  - User sign-off on CRWV conviction upgrade medium → high
  - User retroactive review of ON stance flip (auto-applied; reversible if not desired)
  - HTML artifact refresh (`market_overview_ai.html` Recent updates + Top picks; `dashboard.html` stance table; tooltips re-inline) — deferred from daily update; flagging as pending. 5+ wiki changes today warrant a refresh.
- **Total wiki:** 82 files (+1: ON page).

## [2026-05-13] news | HPE +7.5% on autonomous AIOps + rugged edge AI launch; BofA PT $32→$38
- User asked about "HP" moving up. Clarified to **HPE** (Hewlett Packard Enterprise) — HPQ (HP Inc.) is flat at $21 and not in wiki.
- **Catalysts:**
  - Autonomous agentic AIOps across HPE Mist + Aruba Central
  - Ruggedized HPE ProLiant edge servers for AI in harsh/distributed environments
  - HPE Compute Scale-up Server 3250 (Intel Xeon 6, up to 64TB DDR5) for in-memory database + business-critical workloads
  - GreenLake 4th-gen private cloud now unifying Kubernetes + VM management
  - BofA raised PT $32 → $38, Buy maintained
- **Stock:** +7.5% on the announcement; trading near 52w high $31.64; **+78% past year, +20% YTD 2026**
- **Comparison:** Dell +67% YTD vs HPE +20% YTD — Dell still winning the AI server share-shift war
- **Read:** Modestly bullish on strategy (AIOps is sticky-subscription opportunity); valuation discipline says don't chase at 52w high. Add on weakness to mid-$20s.
- **Wiki touched:** [[HPE]] (new AIOps + rugged edge bullet in bull case; new bear-case bullet on Dell-outperforms-HPE-YTD and "+78% past year easy money gone"; "What this means" box added; Recent developments entry); `tooltips.js` (price $29.94→$31.50, cap bumped, thesis refreshed with May product launch + BofA PT raise + Dell comparison; as_of 2026-05-13)
- **Stance/conviction:** unchanged. Bull/medium holds.

## [2026-05-13] news | META WhatsApp AI strategy update (2 stories, net slight bullish)
- User shared two META news items same day:
  - (a) Meta launching **WhatsApp Incognito Chat** with private-processing tech (conversations invisible even to Meta); plus **"Side Chat" announced for coming months** (Meta AI embedded in any WhatsApp conversation)
  - (b) EU antitrust concession: Meta offering one-month free WhatsApp Business API access to competing AI chatbots while EU investigation continues
- **Stock reaction: $599 → $608 → $605 intraday (~+1% net)** — market reading as "interesting, not transformational"
- **Read:** Two stories tell a coherent strategic playbook — don't fight on access (EU concession), fight on product quality (Incognito Chat / Side Chat = differentiation AI labs can't replicate because their business models depend on data retention). **Net slight bullish.** No stance/conviction change.
- **Wiki touched:**
  - [[META]] — new privacy-tech-moat bullet in bull case; EU regulatory bullet sharpened in bear case with offset framing; Recent developments entry capturing both stories + price action; What this means box added; [[us-china-relations]] added to related
  - `tooltips.js` — META thesis text updated with both stories; price $605 added; as_of bumped to 2026-05-13
- **Why no source summary:** per the daily-update workflow's "be selective" guidance, this is a Recent developments entry, not a conviction-shifting ingest. Single news item without long-form data.

## [2026-05-13] workflow change + NBIS upgrade | Always-on earnings retrieval workflow established
- **New standing workflow saved as memory:** `feedback_earnings_workflow.md` — when ANY wiki ticker reports earnings, proactively (a) fetch the official press release via WebFetch, (b) save raw to `raw/filings/YYYY-MM-DD-TICKER-Q{N}-{YEAR}-earnings.md`, (c) write source summary in `sources/`, (d) update the company wiki page with findings, (e) review conviction/stance. **Do not wait for the daily-update ritual.**
- **Retroactive first instance: NBIS Q1 2026** executed end-to-end per new workflow:
  - Fetched official press release via WebFetch (BusinessWire timed out; succeeded via StockTitan proxy)
  - Saved raw to `raw/filings/2026-05-13-NBIS-Q1-2026-earnings.md`
  - Wrote source summary [[2026-05-13-NBIS-Q1-2026-earnings]] — full Q1 data + operating-leverage flip + acquisitions (Clarifai team, Eigen AI)
  - **Correction surfaced:** wiki had stale cash position ($175M). Actual at Mar 31, 2026 = **$9.3B**. Source summary explicitly flagged the contradiction.
  - **Conviction upgraded medium → HIGH** with user sign-off ("Sounds good")
  - Updated [[NBIS]] frontmatter, Recent developments, bull case (added operating-leverage-flip bullet), Sources list (3 entries now)
  - Updated `tooltips.js` — conv high; bull_2027 multiplier upgraded +30% → +50%; bull_2028 +50% → +90% (matching high-conviction methodology)
  - Updated [[watchlist]] — high conviction; flagged "MOVED TO LONG-TERM CORE candidate"
  - Updated [[index]] — Recent source ingests entry for NBIS earnings
- **Key insight from the operating-leverage data:** NBIS Q1 cost ratios collapsed dramatically (cost of rev 49%→26%, R&D 72%→17%, SG&A 120%→36%). This is the structural shift from build-phase to harvest-phase economics in a single quarter — the kind of inflection that justifies a multi-notch conviction upgrade.
- **Total wiki:** 81 files (no new wiki pages; +1 source summary + 1 raw filing)

## [2026-05-13] earnings + correction | NBIS Q1 2026 blow-out; PPI-shock framing refined
- User flagged: NBIS wasn't on watch list this morning and just printed +14.7% on earnings. Acknowledged as a miss — both the watch-item miss and the over-coarse "trim CRWV/NBIS/OUST" lumping in the morning's [[2026-05-13-ppi-cpi-shock-positioning]] analysis.
- **NBIS Q1 2026 print (May 13):**
  - Revenue **$399M (+684% YoY)** vs $50.9M Y/Y; beat consensus by ~$10M
  - **Adjusted EPS $2.11 vs -$0.78 expected** — $2.89 beat
  - **Adjusted EBITDA $129.5M** (vs -$53.7M Y/Y) — **profitability inflection**
  - Net income $621.2M (includes one-time items)
  - **2026 revenue guide $3.0-3.4B** vs 2025 $530M = ~5-6x growth
  - **ARR target $7-9B by EOY 2026**
  - Stock **+14.7% premarket**
- **NEW disclosure (was not in wiki):** Microsoft 5-year $17.4B GPU infrastructure deal (March 2026). Adds to existing Meta $27B = **$44.4B combined contracted revenue**.
- **Wiki touched:**
  - [[NBIS]] — full Recent developments entry; MSFT contract added throughout; bear case updated (Q1 print invalidates "smaller revenue base" framing; customer concentration risk reframed); "What this means" boxes added; bull case rewritten to lead with Q1
  - [[watchlist]] — NBIS row updated with Q1 results + conviction-upgrade-pending note
  - [[tooltips.js]] — NBIS thesis text fully refreshed with Q1 data
  - [[2026-05-13-ppi-cpi-shock-positioning]] — added "REFINEMENT (NBIS post-Q1 print)" note explicitly correcting the morning's coarse lumping
- **Stance / conviction change: PENDING USER SIGN-OFF.** Recommended: NBIS bull/medium → **bull/HIGH** based on (a) Q1 profitability inflection, (b) $44.4B contracted revenue with hyperscaler-quality customers, (c) ARR $7-9B trajectory, (d) NVDA's 8.3% stake. Conviction not auto-upgraded per workflow.
- **Honesty note for future analyses:** when bucketing names for macro positioning calls, idiosyncratic earnings catalysts in the next 2 weeks should be flagged at the top of "what to watch" — not buried under broad macro signals. NBIS was a known May 13 print and should have been called out.

## [2026-05-13] macro regime shift | April PPI + CPI shock; Warsh as incoming Fed Chair
- User shared April PPI/CPI data + prior Claude analysis + CNBC follow-up article. Triggered macro layer update.
- **Material data points:**
  - **April CPI: 3.8% YoY (May 12 print)** — highest since May 2023; core CPI MoM 0.4% (highest since Jan 2025)
  - **April PPI: 6.0% YoY (May 13 print)** — +200bps re-accel vs prior 4.0%; **Core PPI MoM 1.0% = 3.3x consensus** (forecast 0.3%); annualized ~12.7% core PPI
  - **CME FedWatch:** **37% probability of a HIKE by EOY 2026**; cut probability through EOY 2027 essentially zero
  - **Incoming Fed Chair confirmed: Kevin Warsh** (taking reins May 2026); dovish Trump-aligned appointee walking into hawkish data
  - Energy = 40%+ of CPI gain; shelter +0.6% MoM (biggest since Sept 2023) — inflation spread is now energy + services + shelter
- **New analysis page:** [[2026-05-13-ppi-cpi-shock-positioning]] — publication-grade analysis with ticker-by-ticker positioning grid, 3-scenario June 10 CPI framework, 4-scenario Warsh framework, full bond/dollar/crypto/vol read. Two "What this means" boxes.
- **Wiki touched:**
  - [[inflation-tariffs]] — added full April PPI/CPI shock table, sector positioning grid, June 10 binary
  - [[fed-policy]] — added Warsh appointment, 37% hike probability, 4-scenario Warsh wildcard framework; updated forward path; updated open questions
  - [[overview]] — updated macro state with hike probability + Warsh + regime shift; added macro-state "What this means" box
- **Late-cycle warning indicators status:** **5 of 6 firing** ([[ai-bubble-debate]] framework). Geopolitical tail risk indicator now sharper with PPI shock + Warsh wildcard.
- **Stance / conviction changes:** none on existing tickers. The wiki's structural compounders keep their stances; this is a multiple-compression event, not an earnings event. **AMZN flagged as further-weakened bear-side candidate** (already medium; tariff pass-through + Stratechery durability gap compound).
- **Action framework for the user:** Don't add equity exposure this week. June 10 CPI is the binary. Rotate marginal capital from CRWV/NBIS/OUST toward FIX/EME/PWR and MP. Hold structural compounders.
- **Pending:** ai-bubble-debate.md late-cycle indicators section could use a status callout update — done implicitly through analysis page reference; explicit edit deferred (already heavily edited recently).

## [2026-05-13] research + conviction change | OUST downgraded medium → low on Hesai competitive gap
- User challenge: "is OUST purely speculative?" Triggered fresh research pass.
- **Research findings (new data, not in original PR pages):**
  - **Hesai (China) is the structural winner of the lidar category.** World's first profitable lidar pure-play (since 2024). Shipped 1M+ units in 2025; doubling capacity to **4M units in 2026** vs OUST ~50-70K (25-60x scale gap). Op margin **+9.73% Hesai vs -61% OUST**. Cash $394M (vs OUST $175M before $100M ATM).
  - **Luminar (LAZR) filed Chapter 11** in early 2026 — closest US lidar pure-play peer. ~1 month before Hesai's capacity announcement. Category mortality not theoretical.
  - **Cantor Fitzgerald: TWO downgrades in 4 days** (May 7 Overweight→Neutral; May 11 Neutral→Hold, $33 PT).
  - **Tesla Optimus = vision-only**, no lidar. Targets $20-30K mass production. If cost-leader OEM rejects lidar, humanoid lidar TAM capped.
  - **Figure 02 uses Livox/DJI 3D lidar (MID-360), not Ouster** — "humanoid attach" narrative for OUST has no public design win.
  - **Q1 2026 confirmed: $48.6M revenue (+49% YoY)**, net loss narrowed $22→$17.5M, 12,600 sensor shipments, Stereolabs closed Feb 4 for $55.2M.
- **Honest read:** OUST is not purely speculative — real $200M run-rate, real customers (Google/Volvo/BMW), real IP. But it's losing badly to Hesai, the closest US peer just went bankrupt, and the humanoid attach is aspirational not confirmed.
- **Conviction change: [[OUST]] medium → LOW.** Stance stays bull (Stereolabs/Physical-AI pivot is real strategic optionality) but conviction reflects narrow path to profitable scale.
- **Wiki touched:** [[OUST]] (sharpened bear case with Hesai data + Luminar BK + Tesla framing + 2 new "What this means" boxes; updated thesis; added 7 new citations); [[watchlist]] (OUST row updated medium→low with new thesis); [[tooltips.js]] (OUST entry — conv low + scenario multipliers reduced from +50%/+90% to +20%/+30% to reflect low conviction); [[index]] (OUST line updated)
- **Bull case requires (explicit):** EITHER (a) sustained US/EU tariff/sanctions regime against Chinese lidar (plausible per [[us-china-relations]]) OR (b) publicly-named humanoid OEM design win that hasn't materialized
- **Why this matters for the broader wiki:** validates the [[ai-bubble-debate]] "Late-cycle warning indicators" framework — when a thesis depends on geopolitical policy that hasn't yet been written, conviction should be low not medium.

## [2026-05-13] follow-up | Robotics integration deepened (cross-links + boxes + bottleneck-roadmap + humanoid-oems)
- Executed 4 of 5 inherited follow-ups from the robotics PR landing earlier today:
  - **Cross-linked [[robotics]] from [[overview]]:** added new leading thesis #7 (robotics buildout as next bottleneck cycle) with "What this means" box
  - **Cross-linked [[robotics]] from [[ai-capex-cycle]]:** added "Adjacent cycle" section after Tier 4, framing robotics as the second leg of the same multi-year buildout
  - **Extended [[bottleneck-roadmap]]:** added parallel "Robotics bottleneck roadmap" table (rare earths 2026 → sensors 2027 → edge SoCs 2027-28 → actuators 2028-30); added "Why both roadmaps reinforce each other" cross-cycle section
  - **Added "What this means" boxes** to dense passages in [[robotics]] (Why it matters now), [[MP]] (humanoid demand multiplier), [[VPG]] (multiple/narrative warning), [[overview]] (new thesis #7), [[bottleneck-roadmap]] (robotics roadmap intro)
  - **Created [[humanoid-oems]]:** new theme page covering Western OEMs (Tesla Optimus, Figure, Agility, Apptronik, Boston Dynamics) and Chinese OEMs (AgiBot, Unitree, UBTECH), with strategic US-China decoupling scenario probabilities, OEM-to-supplier mapping table, and watch items. Two "What this means" boxes embedded.
- **Updated [[index]]:** added [[humanoid-oems]] to themes section; updated bottleneck-roadmap description to mention robotics extension; bumped ai-capex-cycle to $725B figure
- **NOT done (intentionally deferred):** per-ticker pages for USAR, UUUU, CEVA, LSCC, ALNT, CGNX, RBC. These are mentioned in [[robotics]] but the conviction names (MP/OUST/ALGM/AMBA/VPG) already have pages. Will expand on demand or when material news hits any specific name.
- **Total wiki:** 79 files (+1: humanoid-oems theme page)

## [2026-05-13] ingest | Robotics & Humanoid Buildout sector (PR landed)
- Landed a draft PR (in `pr/` folder) that added a complete robotics sector to the wiki. PR was generated by Claude on web/mobile and packaged for local Claude Code to land.
- **Lint review:** schema-compliant per CLAUDE.md. Every page has frontmatter, bull/bear cases, dated metrics, cited PTs (no inventions), Obsidian-style wiki links. No contradictions with existing wiki pages. Roth $65 vs consensus $96-100 AMBA contradiction surfaced (not resolved) per house rules.
- **New pages:**
  - [[robotics]] — new sector page applying [[bottleneck-roadmap]] framework to humanoid components (rare earths now → sensors/harmonic drives 2027 → actuators/batteries 2028-2030)
  - [[MP]] — MP Materials, bull/high. Only fully integrated US NdFeB producer; Stillwater H1 2026 ramp; Apple + GM + DoD anchor customers.
  - [[OUST]] — Ouster, bull/medium. Lidar + Stereolabs stereo cameras; Q1 2026 +49% YoY; $100M ATM dilution overhang.
  - [[ALGM]] — Allegro MicroSystems, bull/medium. Magnetic position + current sensors per motor joint.
  - [[VPG]] — Vishay Precision Group, neutral/low. Force-torque pure-play but P/E 135-215 prices in pivot success.
  - [[AMBA]] — Ambarella, bull/medium. Edge AI SoCs; back to profitability FY26; M&A optionality.
- **Source created:** [[2026-05-13-x-stack-map-humanoid-robotics]] — viral X "humanoid stack" thread that prompted the sector primer
- **Tooltips:** added 12 ticker entries (MP, USAR, UUUU, OUST, VPG, ALGM, AMBA, CEVA, LSCC, ALNT, CGNX, RBC) + 6 term entries (NdFeB, NPU, harmonic-drive, world-model, force-torque, physical-ai) into `tooltips.js`
- **HTML:** `market_overview_robotics.html` (40KB, self-contained, mirrors `market_overview_ai.html` design system) copied to repo root
- **Index updated:** added Robotics sector + 5 new ticker entries + new source link
- **Watchlist updated:** added MP/OUST/ALGM/AMBA to Tactical; added VPG to Hold/monitor. **Removed "rare-earth Western capacity" from "Not yet covered"** — MP/USAR/UUUU now cover that gap (was flagged 2026-05-12 in Trump-Xi analysis).
- **pr/ folder removed** after extraction.
- **Stance / conviction changes:** none on existing tickers. 5 new tickers added at their PR-stated stances.
- **Follow-ups inherited from PR README:**
  - Per-ticker pages for USAR, UUUU, CEVA, LSCC, ALNT, CGNX, RBC (mentioned in robotics.md but not yet expanded)
  - Update [[bottleneck-roadmap]] to extend AI-cycle roadmap into robotics
  - New theme page `wiki/themes/humanoid-oems.md` covering Tesla Optimus, Figure, Agility, Apptronik, AgiBot, Unitree
  - Cross-link [[robotics]] from [[overview]] and [[ai-capex-cycle]] on next full review
  - Investigate Stock Connect / ETF access to Sanhua (002050.SZ) and Leader Drive (688017.SS)
- **New follow-up (this session):** Apply the new "What this means" box pattern (per [feedback_what_this_means_box](memory)) to the new robotics pages where passages are dense — e.g., NdFeB demand framing in [[robotics]], cycle-peak-equivalent warning in [[MP]] / [[VPG]]. PR pages were authored before the new style memory existed; retrofit on next review.
- **Total wiki:** 78 files (+7: 1 sector, 5 companies, 1 source); +1 HTML artifact.

## [2026-05-12] daily overview | Hyperscaler $725B capex revision + Stratechery Amazon Durability
- Ran the 8-step daily-update ritual. Parallel discovery across AI/semi/hyperscaler/memory/podcasts.
- **Material findings:**
  - **Big 4 hyperscaler 2026 capex revised UP to $725B (+77% YoY from $410B 2025).** MSFT $190B (CFO Hood explicitly attributes $25B to memory cost inflation), GOOGL $190B (cloud contract backlog doubled to $460B in one quarter), AMZN $200B (held flat — only one not raising), META $125-145B. With secondary hyperscalers (Oracle, ByteDance, Alibaba), total ~$830B.
  - **Stratechery "Amazon's Durability" (Ben Thompson, May 2026)** — sharper AWS bear case: Nitro + EFA networking optimized for CPU cloud era, structurally weaker than [[NVDA]] NVLink/Spectrum-X + [[AVGO]] Tomahawk for AI workloads. Technical/architectural root cause of AMZN AI lag vs MSFT/GOOGL.
  - "Changing of the guard in AI" rotation narrative (CNBC May 8): Intel +240% YTD, AMD breaking out on MI400, NVDA only +15% YTD lagging Nasdaq. AMD Q1 print: $10.25B rev, data center +57%, Q2 guide $11.2B.
  - HBM4 pricing ~$500/cube vs HBM3E $350 (SK Hynix) / $250 (Samsung). HBM3E +20% for 2026.
  - SemiAnalysis: N3 utilization >100% 2H 2026; DRAM fabs >90%. Confirms tight supply.
- **Sources created:**
  - [[2026-05-12-hyperscaler-capex-q1-revisions]]
  - [[2026-05-12-stratechery-amazon-durability]]
- **Wiki touched:** [[ai-capex-cycle]] ($725B revision; per-company breakdown), [[MSFT]] (new Recent developments + $25B memory attribution from CFO Hood), [[GOOGL]] (new Recent developments + cloud backlog $460B doubled in one quarter), [[AMZN]] (Stratechery bear data point in bear case; flat-capex caveat), [[index]] (new source entries).
- **Stance / conviction changes:** none today. AMZN noted as potential downgrade candidate (medium → neutral) if 2H 2026 AI revenue ramp doesn't materialize; not flipping yet.
- **Skipped (low-value):**
  - "Top semiconductor stocks 2026" listicles — no new data
  - Daily stock price quote pieces (NVDA $219.48, AVGO ~$420) — daily noise without analytical content
  - "AI chip rotation: trim Nvidia, buy Intel" retail framing — no new evidence
  - Repeated HBM pricing pieces — consistent with existing wiki
- **Pending:** HTML artifact refresh (`market_overview_ai.html` Recent updates section + Top picks table; `dashboard.html` stance table; tooltips.js market cap refresh) — not run today. CDNS coverage page still pending from earlier session. Rare earth Western capacity (MP Materials, Lynas) coverage still pending from Trump-Xi analysis.

## [2026-05-12] query + new pages | Trump-Xi Beijing summit + macro layer expansion
- **User query:** "Trump is in China meeting with Xi. He says he wants to open China... how would you interpret it. Does it change anything in our thesis?"
- **Approach:** Pulled current news (WebSearch) on May 14-15 Beijing summit. Mapped scenarios to wiki positioning. User accepted offer to file as analysis page + add macro coverage.
- **New pages created:**
  - [[2026-05-12-trump-xi-summit-investment-implications]] — analyses/ page with 3 scenarios (Theater 60% / Trade deal w/ chip carve-out 25% / Acrimonious 15%), historical analogues (Phase 1 2020, Plaza Accord 1985, TikTok), watch items, positioning framework. Rare earths flagged as the underappreciated risk vector.
  - [[us-china-relations]] — new macro page covering trade, technology decoupling, capital flows, geopolitical flashpoints (Taiwan, Iran, rare earths) + name-by-name mapping of wiki tickers to "benefits from better / worse / neutral relationship."
- **Wiki touched:** [[inflation-tariffs]] (added cross-link to us-china-relations + "Board of Trade" open question), [[index]] (new entries added).
- **Thesis conclusion:** **No stance changes.** Bull case for AI complex was built on US/global hyperscaler demand, not China — China is free option. Most likely outcome (60%) is theater. Tail risk (15%) Scenario C would tip 4+ of 6 "Late-cycle warning indicators" in [[ai-bubble-debate]] into firing simultaneously.
- **New memory saved:** `project_wiki_vision.md` — user has signaled wiki should evolve toward multi-sector + publication-grade for potential Substack / YouTube. Affects writing standard for all future pages.
- **Coverage gaps surfaced for next pass:** MP Materials, Lynas (rare earth Western capacity). Also: a `wiki/macro/energy-cycle.md` would round out the macro layer.
- **Total wiki:** 72 files (+2 new pages: 1 analysis, 1 macro).

## [2026-05-12] ingest | SemiAnalysis PDF batch (5 new sources)
- User added 5 new SemiAnalysis PDFs to `raw/articles/` (one previously-ingested AI Value Capture PDF was skipped). Read pages 1-15 of each.
- **Sources created:**
  - [[2026-04-01-semianalysis-gpu-rental-index]] — **MOST MATERIAL.** H100 1-yr contract +40% in 5 months ($1.70 → $2.35/hr Oct 2025 → Mar 2026), still rising 15-20% MoM. All capacity through Aug-Sep 2026 already booked, market-wide. Anthropic ARR tripled in single quarter ($9B → $30B+). Memory pricing parabolic Jan 2026 (LPDDR5 +4x YoY, DDR5 +5x YoY). **Directly refutes Reddit B200 rental softening thread we discussed earlier.**
  - [[2026-04-15-semianalysis-isscc-roundup]] — Samsung HBM4 closing the gap with SK Hynix (3.3 TB/s, 13 Gb/s pin); LPDDR6 specs (-27% read power vs LPDDR5). Material risk to MU "preferred supplier" thesis at Rubin generation.
  - [[2026-04-20-semianalysis-gpu-cluster-cost]] — ClusterMAX 2.1 framework; cluster TCO methodology; "80% of foundation-model startup funding goes to GPUs." (PDF mostly paywalled in extract — framework only.)
  - [[2026-04-24-semianalysis-coding-assistant]] — GPT-5.5 vs Opus 4.7 vs DeepSeek V4. DeepSeek V4 has **90% KV cache reduction** ("NAND investors watch out"). SemiAnalysis's own Claude Code burn rate hit **$10.95M ARR** before Opus 4.7 reset it via token-efficiency.
  - [[2026-05-11-semianalysis-eda-primer]] — Part 1 of 3-part EDA series. Verification = 70% of project effort. 67K US semi worker shortage by 2030. $300M+ first-time 3nm design cost. Structural compounder thesis for [[SNPS]] / CDNS / Siemens EDA.
- **Wiki touched:** [[ai-bubble-debate]] (NUANCED the GPU-rental-softening warning indicator — SemiAnalysis Apr 2026 data refutes the GQG channel-check anecdote; added new "This Time Might Be Different" + DeepSeek V4 sections), [[ai-capex-cycle]] (added GPU rental sold-out, Anthropic ARR triple-step, memory parabolic, 80%-of-funding-on-GPUs data points), [[MU]] (Samsung HBM4 closing gap as new bear risk + as recent development), [[CRWV]] (rental +40%, sentiment-vs-fundamentals disconnect, ClusterMAX goodput framework), [[NBIS]] (same; "Long NBIS" featured comment), [[SNDK]] (DeepSeek V4 KV cache reduction risk to AI data exhaust thesis), [[SNPS]] (EDA primer structural thesis).
- **Stance / conviction changes:** none today. The new data REINFORCES the "Long [[CRWV]] / [[NBIS]] / [[NVDA]]-infra-supply-chain" thesis and ADDS specific watch items (Samsung HBM4 share, DeepSeek V4 KV cache generalization) rather than flipping any stance.
- **Key reframe:** The "Late-cycle warning indicators" framework in [[ai-bubble-debate]] is conceptually correct but the **specific GPU-rental-softening signal is NOT firing** (the GQG anecdote was contradicted by the authoritative SemiAnalysis survey index). 3-of-6 indicators still flickering (small-cap speculation, IPO oversubscription, "trillion-dollar club" rhetoric); GPU rental signal explicitly downgraded to "not yet."
- **Pending:** HTML artifact refresh (dashboard.html / market_overview_ai.html) — would be nice to do but not requested. Also: read pages 16-93 of ISSCC roundup if specific CPO / TSMC Active LSI topics become topical for AVGO / TSM updates. Tokenizer changes to Opus 4.7 (+35% token usage = implicit 35% price hike) — note for the value-capture model.
- **Total wiki:** 70 files unchanged (no new ticker pages, all updates were to existing pages); +5 source summaries.

## [2026-05-09] note | Wiki initialized
- Scaffolded directory structure (raw/, wiki/, sources/) per [[CLAUDE]] schema
- User profile: long-term + 6-18mo tactical swings; tech/AI deep dive + S&P 500 + global
- Sources: web articles, 10-Ks, research PDFs

## [2026-05-09] note | Seed pages created from web research
- Did initial web research pass (Goldman / JPM / Vanguard 2026 outlooks; NVDA Q1 FY27; Fed Apr 2026 decision; Mag 7 rankings; TSM/ASML; risk side: AI bubble, concentration, tariffs).
- Created seed pages with citations inline; no formal source summaries yet — citations live as URLs on each page.
- Wiki touched (initial creation): [[overview]], [[watchlist]], [[fed-policy]], [[valuation-environment]], [[inflation-tariffs]], [[ai-capex-cycle]], [[market-concentration]], [[ai-bubble-debate]], [[semiconductors]], [[cloud-hyperscalers]], [[NVDA]], [[GOOGL]], [[MSFT]], [[META]], [[AMZN]], [[AAPL]], [[TSLA]], [[TSM]], [[ASML]]
- Next: ingest first formal source via the ingest workflow to validate the schema.

## [2026-05-13] research | MU counterpoint to "undervalued" framing + cycle-peak P/E paradox added globally
- User asked about the "MU is undervalued" thesis circulating on Twitter / retail. Used the prompt as a chance to strengthen the wiki's counter-framing.
- **[[MU]] update**: substantially expanded bear case with explicit cycle-peak P/E paradox (historical drawdowns 2022/2019/2015-16/2000); added Mizuho PT-below-price observation; added 70%-commodity-revenue caveat; added "value capture cuts against memory" link to SemiAnalysis ingest; added explicit "right framing" section (leveraged multi-year trade NOT compounder) + "what would move the view higher/lower" tables for exit discipline.
- **[[ai-bubble-debate]] update**: added "Cycle-peak P/E paradox" as a globally-applicable framework — applies to any cyclical semi (MU, SNDK, WDC). The framework: cheap forward P/E + growing EPS = late-cycle warning in memory; opposite of what it means in software.
- **[[SNDK]] update**: cross-reference to cycle-peak P/E framework; +91% past month makes this acute.
- **[[WDC]] update**: same cross-reference; +40% past month.
- **Stance changes**: NONE. MU stays bull/high. SNDK stays bull/high. WDC stays bull/medium. The updates make the BEAR CASE stronger and the SIZING / EXIT DISCIPLINE clearer — the wiki is now honest about cyclicality risk on top picks where the "undervalued long-term compounder" framing is wrong.
- **Why this matters**: memory names are leveraged multi-year trades, not structural compounders like [[NVDA]] / [[TSM]] / [[ASML]]. The wiki's bull conviction is intact for the next 2-3 years of the supercycle, but new readers (e.g., user's buddy via the shared GitHub repo) need to understand the cyclicality risk explicitly.

## [2026-05-13] daily update | SemiAnalysis value-shift + Cerebras IPO + Apple-Intel confirmed
- **Material findings this session** (curated; skipped low-value items):
  - **SemiAnalysis "AI Value Capture — Shift to Model Labs"** ([[2026-05-13-semianalysis-value-capture]]) — Anthropic ARR $9B→$44B, inference gross margin 38%→70%+. NVDA pricing framework: cost-floor $4.92/GPU-hr, value-ceiling $12.25, current $0.28/PFLOP below trend — ~40% NVDA price hike still leaves neocloud margin. SOCAMM pricing $8→$13/GB by EOY 2026. THE major new bull data point.
  - **Cerebras IPO** ([[2026-05-13-cerebras-ipo]]) — CBRS pricing May 13 at $48.8B, 20x oversubscribed, 51x trailing rev. $510M revenue, 47% net margin, OpenAI $10B/750MW deal. 86% UAE customer concentration. **New ticker page added.**
  - **Apple-Intel deal CONFIRMED** ([[2026-05-13-apple-intel-deal]]) — WSJ confirmed May 8 (was preliminary). Intel 18A-P primary node. AAPL stance unchanged (bear); Intel coverage upgraded from "not coverage-worthy" to "active research candidate."
  - **Eaton Q1 2026** ([[2026-05-13-eaton-gev-q1-2026-key-data]]) — datacenter orders **+240% YoY**, backlog $22.8B.
  - **GE Vernova Q1 2026** — orders $18.3B (+71% organic). $2.4B Q1 datacenter electrification orders = MORE than all of 2025. Prolec $5.3B Feb 2026 buyout completes transformer dominance.
  - **Vertiv** — Feb 2026 $1B acquisition in high-density cooling surfaced.
- **Wiki touched**: [[NVDA]] (SemiAnalysis pricing framework, SOCAMM), [[AAPL]] (deal confirmed), [[ETN]] (+240% datacenter orders Q1), [[GEV]] (Q1 orders + Prolec), [[VRT]] ($1B cooling deal), [[CBRS]] (new page), [[ai-bubble-debate]] (Anthropic 70% margin data point), [[bottleneck-roadmap]] (transformers as 2027 sub-bottleneck), [[index]] (CBRS added to AI accelerators), [[watchlist]] (CBRS added; INTC status upgraded)
- **Sources created**: [[2026-05-13-semianalysis-value-capture]], [[2026-05-13-cerebras-ipo]], [[2026-05-13-apple-intel-deal]]
- **Raw saved** (gitignored): `raw/articles/2026-05-13-semianalysis-ai-value-capture.md`, `raw/articles/2026-05-13-cerebras-ipo.md`, `raw/articles/2026-05-13-apple-intel-deal-confirmed.md`, `raw/filings/2026-05-13-eaton-gev-q1-2026-key-data.md`
- **Stance / conviction changes**: none today; CBRS added at bull/medium.
- **Tooltips refreshed**: CBRS added; HTML artifacts re-inlined.
- **Skipped (low value)**: opinion pieces, Trump-Xi meeting (geopolitics, not investable signal yet), "4 Brilliant Chip Stocks" listicles, generic CNBC "party going to end" framing without new data.
- **Pending**: do a fresh research session on Intel given Apple deal + Wall Street rotation; revisit memory-vendor caps after Q1 prints; consider adding transformer makers (Hitachi Energy, Siemens Energy) to the 2027 bottleneck cluster.
- **Total wiki**: 70 files (+1 new ticker CBRS).

## [2026-05-12] ingest | The "invisible" fab layer — TER / ENTG / APD
- Followup to "what are we overlooking downstream" — sharpened the lens past the obvious "second-leg" names (MRVL, CDNS, CEG/VST/TLN, PLTR) to truly overlooked downstream plays
- Picked **three names that sit outside the WFE bucket** but capture AI fab-buildout content:
  - **[[TER]]** (Teradyne) — bull / high — chip test equipment; **Q1 2026 revenue +87% YoY to $1.282B record**; Semi Test crossed $1B threshold; **70% AI exposure**; compute now ~75% of SoC product revenue (shift from mobile); +66% YTD
  - **[[ENTG]]** (Entegris) — bull / high — fab consumables, FOUPs/wafer carriers, ultra-pure materials, gas/liquid filtration; Q1 2026 revenue $811.9M (+5%) beat; new Colorado Springs Manufacturing Center of Excellence; content-per-wafer growth from AI complexity
  - **[[APD]]** (Air Products) — bull / medium — industrial gases for fabs (N2/O2/Ar/H2 + NF3 chamber clean + specialty); **Samsung Pyeongtaek announced as APD's largest electronics investment in history**, multi-decade BOO contracts, new facilities onstream 2028-2030; 4 global NF3 transfill facilities
- These names are overlooked because they sit in different industry classification buckets (industrial gases / specialty materials / test equipment) from the obvious AI names — they don't appear in AI ETFs or tech screens
- Cross-references updated: [[index]] adds "Fab consumables & specialty materials" category + adds TER to WFE section; [[watchlist]] adds three to Long-term Core; [[semiconductors]] adds new section; [[nvda-supply-chain]] adds new layer; [[bottleneck-roadmap]] 2027 row now includes these three; [[overview]] adds new thesis #6; cross-link sections updated on [[AMAT]] / [[KLAC]] / [[LRCX]] / [[ASML]] / [[TSM]] / [[MU]]
- **Total wiki: 69 markdown files** (was 66; +3 companies)
- **Updated "not yet covered" list**: now explicitly flags MRVL, CDNS, LIN, MKSI, CEG/VST/TLN, PLTR as next-tier candidates
- **Combined positioning**: TER + ENTG + APD = three completely different industrial classifications, all riding the same [[bottleneck-roadmap]] 2027 fab buildout. Different volatility profiles, different cycles, different valuations — but the same demand driver.

## [2026-05-12] ingest | Datacenter construction layer — FIX / EME / PWR
- User asked "what are we overlooking downstream that people haven't caught on to" → picked the mechanical/electrical contractor cluster (highest-conviction "overlooked" pitch)
- Researched the three biggest names and the underlying thesis (multi-year contracted backlogs, labor as a moat, industrial-classified so falls outside AI ETFs)
- **Created new theme [[datacenter-construction]]** — ties the cluster to [[bottleneck-roadmap]] 2030+ labor bottleneck and [[ai-capex-cycle]] Tier 4 power & infra
- **Created 3 new company pages**:
  - [[FIX]] (bull / high) — Q1 2026 backlog **$12.46B (+81% YoY)**, EPS **$10.51 (+121%)**, mechanical gross margin **26.9%**, data center exposure **45% of revenue**, +47% YTD 2026
  - [[EME]] (bull / high) — Q1 2026 RPOs **$15.62B (record)**, FY26 EPS guide raised to **$28.25-$29.75**, revenue guide to $18.50-$19.25B; "unprecedented activity in Network & Communications" from AI
  - [[PWR]] (bull / high) — Q1 2026 backlog **$48.5B (record)**, FY26 adj EPS guide **$13.55-$14.25**; NiSource ~3 GW generation engagement; transmission + grid + renewable + AI all in same direction
- Cross-references updated: [[index]] adds new "Data center construction" category, new theme entry; [[watchlist]] adds three to Long-term Core; [[ai-capex-cycle]] Tier 4 now includes contractors; [[bottleneck-roadmap]] 2030+ row links to the cluster; [[overview]] now surfaces this as overlooked downstream play (#5); [[VRT]] / [[ETN]] / [[GEV]] / [[BE]] Related sections add cross-links
- **Total wiki: 66 markdown files** (was 62; +1 theme + 3 companies)
- **Combined backlog across FIX/EME/PWR: ~$76B** — the size of this number is what makes the cluster non-trivial for portfolio purposes
- **Caveat**: all three have run; not cheap. The thesis is multi-year backlog visibility, not deep value.
- Still not yet covered (next research candidates): MRVL, CDNS, CEG/VST/TLN (nuclear utilities), APD/LIN (industrial gases), PLTR

## [2026-05-12] note | Reddit thread on B200 rental price drop — light-touch note added
- User surfaced a Reddit thread claiming B200 rental prices fell 30% over the May 9-10 weekend, citing ornn.com and GQG channel checks on H200 secondary-market discounts
- Evaluated: headline data point is **noise** (Mother's Day weekend effect; cherry-picked window; broader trend is +50% Mar→Apr; Ornn methodology diverges from other trackers; Nebius/Vast still sold out)
- **However:** GQG (Rajiv Jain) channel-check on **H200 secondary-market 50% discounts** is a legitimate bear data point — tensions Dylan Patel's "H100 worth more today" framing for *prior-gen* silicon specifically as Rubin ramps
- **Action:** added one-paragraph note to [[ai-bubble-debate]] under bear case — flags GPU rental indices and secondary-market discounts as **early-warning indicators to watch**, not stance-changers. No other pages touched. No conviction changes.

## [2026-05-11] news | Daily ticker sweep — material findings only
- Batched news searches across Mag 7 / semis / memory / power / optical / server OEMs; updated only pages with material new facts
- **Two conviction upgrades:**
  - [[SNDK]] medium → **high** on **HBF (High-Bandwidth Flash)** — vertically stacked NAND with 8-16x HBM capacity at lower cost; first samples 2H 2026. Could be category-defining for cost-sensitive inference. Caveat: stock +91% in past month.
  - [[BE]] medium → **high** on **Oracle Project Jupiter** — sole primary-power supplier at 2.45 GW for NM data center; up to 2.8 GW across multiple Oracle deployments. Moves BE from "alternative" to "primary at scale."
- **AAPL nuance** — WSJ: Apple preliminary agreement with **Intel** to manufacture *some* chips. **Stance unchanged (bear)** — not leading-edge SoCs, preliminary only; small option-value positive on US-foundry diversification.
- **Notable data points added:**
  - [[overview]] — S&P 500 first close above **7,400** on May 10; WTI $97.89 (+2.59%) on US-Iran; **PHLX Semi +66% YTD**
  - [[AMD]] — Q2 guide **$11.2B** beat consensus; 20+ broker PT raises
  - [[MU]] — Cloud Memory Business Unit **$5.28B at 66% GM**; Mizuho **$740 PT**; +76% past month
  - [[WDC]] — non-GAAP gross margin **crossed 50%** for first time; 20% dividend increase
  - [[VRT]] — Citi raised PT to **$414** (from $353); long-term organic growth guide raise to 12-24% expected
  - [[GEV]] — strategic collaboration with **Blue Energy** for world's first **gas-plus-nuclear** plant (Texas, data center campus); 7HA.02 turbines reserved for 2029
  - [[COHR]] — Q3 datacenter +41% YoY to **$1.36B** = 75% of revenue; orders booked through 2028
  - [[LITE]] — Q3 revenue **+90% YoY to $808M** historic high; Q3 guidance +85% beat
  - [[FN]] — record revenue + EPS; demand outstrips supply
  - [[DELL]] — Q4 FY26 AI server **$8.95B (+342%)**; **FY27 guide $50B**; $43B backlog; stock +67% YTD
  - [[HPE]] — Q1 FY26 revenue **$9.3B (+18%)**, networking **+152%** on Juniper; raised EPS guide; FCF +$708M (from -$877M)
  - [[SMCI]] — −7% YTD; underperforming peers; legal overhang remains gating factor
  - [[ORCL]] — Project Jupiter (BE) + 50K AMD MI450 deal both confirmed
- **No update warranted (already consistent with wiki):** NVDA, AVGO, GOOGL, MSFT, META, AMZN, TSLA, TSM, ASML, ARM, KLAC, LRCX, AMAT, KEYS, AMKR, ASX, CAMT, APH, GLW (covered in COHR/LITE context), JBL, FLEX, STM, ADI, MPWR, NVTS, ON, CRWV, NBIS, NOK, SNPS, ETN
- **Bottom line:** memory crunch (MU/SNDK/WDC) and power/optical earnings season both delivered confirmatory beats with structural tailwind extensions through 2027-2028.

## [2026-05-11] lint | Wiki health check + targeted fixes
- Ran full lint per CLAUDE.md schema (62 → 62 files unchanged in count)
- **No-issue confirmations:** stance consistency between frontmatter and index across all 47 ticker pages; key anchor numbers consistent across all references (30% capex to memory, $1.40/$2/$2.40 Hopper economics, OpenAI 10 GW Project Titan, smartphone 1.4B→500-600M, Mag 7=35%, AMAT >50% HBM equipment value); every page with sources>0 has a Sources section; every company/theme/sector/macro page has Citations or Sources; no stale full reviews (wiki is 2-3 days old); only orphan is log.md (expected)
- **Fixes applied:**
  - **AVGO context added to [[GOOGL]], [[META]], [[AMZN]]** — TPU/MTIA/Trainium are co-designed with Broadcom (was previously only stated on [[cloud-hyperscalers]] but not on the individual hyperscaler pages)
  - **[[META]] AMD deal noted** — 6 GW Instinct + 160M-share warrant; Meta now has both AVGO and AMD as parallel non-NVDA paths
  - **Bidirectional Related-link asymmetries fixed:** added back-pointers on [[GOOGL]], [[META]], [[AMZN]], [[ORCL]], [[CRWV]], [[NBIS]], [[MU]], [[ASML]], [[TSM]] for new pages [[AVGO]] / [[AMD]] / [[AMAT]] / [[HPE]]
  - **Dangling links resolved:** `[[Vera-Rubin platform]]` in [[nvda-supply-chain]] → `[[NVDA|Vera Rubin]]`; removed `[[ai-software]]` placeholder from [[index]]; rewrote [[CLAUDE]] schema template examples to avoid stray `[[...]]` placeholders
  - **Graph densification:** 22 replacements across 18 pages — first occurrence of "TSMC" → `[[TSM|TSMC]]` and "KLA" → `[[KLAC|KLA]]` (preserving URLs, code, frontmatter, and existing wiki-links)
- **Final dangling count: 0**

## [2026-05-10] note | Filling remaining ticker gaps — HPE, AVGO, AMD, AMAT
- Per user direction, expanded coverage to the 4 names on the "not yet covered" watch list
- Did batched web research and created 4 new company pages:
  - **[[HPE]]** (bull / medium) — Juniper acquisition ($13.4B, closed 2025-07-02) drove Networking +151% YoY in Q1 FY26; full Blackwell+Rubin AI Factory; sovereign AI fit
  - **[[AVGO]]** (bull / high) — Q1 FY26 AI revenue **+106% YoY to $8.4B**; **OpenAI "Project Titan" 10 GW by 2029**; Meta XPU 1GW+ first phase; Tomahawk 6 (102.4 Tbps); CEO targets $100B AI rev by 2027 — **the systematic non-NVDA hedge**
  - **[[AMD]]** (bull / high) — **OpenAI 6 GW** (Oct 2025) + **Meta 6 GW + 160M-share warrant** (Feb 2026) + **Oracle 50K MI450**; Helios rack Q3 2026 on TSMC 2nm
  - **[[AMAT]]** (bull / high) — **>50% of HBM equipment value**; >20% growth guide for 2026; 12-24 months forward visibility; positions for the 2027 fab-buildout sweet spot per [[bottleneck-roadmap]]
- Cross-references updated: [[index]], [[watchlist]] (added all 4 to long-term core / tactical; cleaned "not yet covered"), [[nvda-supply-chain]] (added HPE to server OEMs, AMAT to equipment, AMD/AVGO competitor note), [[NVDA]] (added AMD + AVGO competitive threats with specific deal sizes), [[semiconductors]] (filled in AMD/AVGO/AMAT detail), [[cloud-hyperscalers]] (added "AVGO is the systematic non-NVDA hedge" framing), [[bottleneck-roadmap]] (AMAT now closes the 2027 sweet spot), [[DELL]] / [[SMCI]] / [[KLAC]] / [[LRCX]] (added Related links)
- Total wiki: **62 markdown files** (was 58; +4 company pages)
- Still on the "not yet covered" list: PLTR, SK Hynix/Samsung, Foxconn/Quanta, sovereign AI plays, additional energy infra (utilities, SMR nuclear), Intel

## [2026-05-09] ingest | Dwarkesh × Dylan Patel podcast (SemiAnalysis)
- Source: [[2026-05-09-dwarkesh-dylan-semianalysis]] (raw at `raw/podcasts/dwarkesh_dylan_pod.txt`)
- TL;DR: 2-hour deep dive on the semiconductor supply chain through 2030. Five major investment-relevant claims:
  1. **An H100 is worth MORE today than 3 years ago** — labs signing $2.40/hr 2-3yr deals on $1.40 build TCO Hopper; falsifies short-depreciation bear case
  2. **Memory is the 2026 binding constraint** — 30% of Big 4 capex going to memory; HBM crunch destroying smartphone volumes (1.4B → ~500-600M by 2027)
  3. **ASML/EUV is the 2028-2030 bottleneck** — ~70-100 tools/yr cap; 3.5 tools = 1 GW of AI compute; Carl Zeiss + Cymer physically can't ramp faster
  4. **Power is NOT a binding constraint** — 16+ gas vendors, behind-the-meter, batteries can unlock 20% of US grid; tempers VRT/ETN urgency narrative
  5. **AAPL is being structurally pushed off TSMC's leading edge** — A16 first customer is AI not Apple; smartphone volume collapse → bearish update needed
- Created [[bottleneck-roadmap]] theme page synthesizing the time-sequenced constraint shift
- Updated [[CLAUDE]] to add `raw/podcasts/` to schema; updated [[index]] with theme + source pointers
- **All proposed updates applied per user direction (2026-05-09):**
  - **Stance changes:** [[AAPL]] flipped from neutral → **bear**; [[ASML]] conviction upgraded to **high (multi-year)** while keeping medium near-term
  - **New ticker pages:** [[GEV]] (gas turbines), [[BE]] (fuel cells), [[ORCL]] (OpenAI compute partner)
  - **Additive updates** (bullets + watch items): [[NVDA]], [[TSM]], [[MU]], [[SNDK]], [[VRT]], [[ETN]], [[NVTS]], [[TSLA]], [[GOOGL]], [[ai-capex-cycle]], [[ai-bubble-debate]], [[nvda-supply-chain]]
  - **Watchlist updated:** AAPL moved from Hold to Avoid; GEV/BE/ORCL added to Tactical
  - **Index updated** with new tickers and AAPL stance change
- Not-yet-covered names introduced (still open): Foxconn, Mitsubishi, Siemens Energy, AMAT (Applied Materials), plus private linkages (Carl Zeiss, Cymer, Victory Giant)
- **Total wiki: 58 markdown files** (1 new theme + 1 source summary + 3 new company pages; 12 existing pages updated)

## [2026-05-09] ingest | NVDA supply chain expansion (user-supplied list)
- User provided NVIDIA's investment / supplier map across IP (ARM), fab (TSM), memory (MU/SNDK/WDC), packaging (ASX/AMKR/CAMT), equipment (KLAC/LRCX/ASML/KEYS), networking (COHR/GLW/FN/LITE/APH), server OEMs (DELL/SMCI/JBL), power systems (FLEX/VRT/ETN), power electronics (STM/ADI/MPWR/NVTS/ON), direct investments (CRWV/NBIS/NOK/SNPS).
- Did batched web research across all groups (HBM4/Vera Rubin, CoWoS capacity, KLA process control, optical CPO, server OEMs, 800V DC architecture, power electronics, neoclouds, NVDA's $1-4B equity stakes).
- Created [[nvda-supply-chain]] master map page tying all 30+ tickers to their role in NVDA's stack.
- Created 28 new company pages: [[ARM]], [[MU]], [[SNDK]], [[WDC]], [[ASX]], [[AMKR]], [[CAMT]], [[KLAC]], [[LRCX]], [[KEYS]], [[COHR]], [[GLW]], [[FN]], [[LITE]], [[APH]], [[DELL]], [[SMCI]], [[JBL]], [[FLEX]], [[VRT]], [[ETN]], [[STM]], [[ADI]], [[MPWR]], [[NVTS]], [[ON]], [[CRWV]], [[NBIS]], [[NOK]], [[SNPS]].
- Updated [[NVDA]] with cross-link to [[nvda-supply-chain]] and expanded Related links.
- Updated [[watchlist]] — promoted high-conviction picks (MU/KLAC/LRCX/VRT/ETN/AMKR/GLW) to Long-term Core; added 16 names to Tactical; surfaced low-conviction watch items (STM/ON/SMCI/NVTS/NOK).
- Updated [[index]] — full catalog of 30+ company pages with stances.
- Key data points: NVDA $4B to COHR+LITE (Mar 2026); NVDA $3.2B to GLW (May 2026); NVDA $2B each to NBIS and SNPS; NVDA $1B to NOK; NVDA $250M anchor at CRWV IPO. AMKR 2026 capex $2.5-3B (~3x prior). VRT Q1 2026 $2.65B/+30%; $9.5B backlog. JBL AI rev $13.1B FY26 (+46%). MU HBM4 ramps Q2 2026 at 15K wafers/month.
- Total wiki: 53 markdown files.
- Next: monitor NVDA Q1 FY27 earnings (calendar Q2 2026); track first AVGO / AMD / HPE pages; watch for any single source that triggers a multi-page lint.
