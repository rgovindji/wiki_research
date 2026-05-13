# Log

Chronological, append-only record of wiki activity. Each entry starts with `## [YYYY-MM-DD]` for grep-ability.

```bash
# Last 5 entries:
grep "^## \[" log.md | tail -5
```

---

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
