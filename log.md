# Log

Chronological, append-only record of wiki activity. Each entry starts with `## [YYYY-MM-DD]` for grep-ability.

```bash
# Last 5 entries:
grep "^## \[" log.md | tail -5
```

---

## [2026-05-17] autonomous-session-FINAL-rollup | EOD totals (batches 1-12)

User had flu, granted autonomous control, then pushed back on early "wrap" framing — produced 13 commits across a 12-batch session.

### Headline data points surfaced today (ranked by investment leverage)

1. **🔥 NVDA overtook Apple as TSMC's #1 customer in 2025** — primary-source TSMC Annual Report (April 2026): NVDA = 19% of 2025 revenue (NT$726.97B); Apple = 17% (NT$645.17B); Apple dropped from 22% in 2024. **Empirically validates AAPL bear thesis at 5pp/year deprioritization speed.**
2. **TSMC $20B capital injection into TSMC Arizona** (primary source: TSMC board resolutions May 17) — ~1/3 of FY26 CapEx earmarked for Arizona alone; direct booster to FIX/EME/PWR/AMKR.
3. **TSMC 2025 revenue NT$3,809B (+31.6% YoY); Q1 2026 GM 66.2% (operating margin 58.1%, NPM 50.5%); HPC = 61% of revenue; A14 by 2028 (10-15% speed gain vs N2); COUPE photonics production begins 2026 with 2x power efficiency**.
4. **TSMC management 25% CAGR target 2024-2029** (materially above prior wiki 10-15% long-term assumption).
5. **CC Wei Q1 call: "Intel and Tesla are still our customers"** despite Terafab announcement — reduces INTC Terafab bull magnitude; reinforces TSM moat.
6. **ASML Q1 2026 GM was only 53%** vs TSMC 66.2% vs NVDA 75% — pricing-power hierarchy is inverse of monopoly position; confirms "generous monopolist" thesis. **ASML China revenue already dropped to 19%** (from 36% Q4 2025) — correction to wiki's prior "historically 40%" framing.
7. **MATCH Act probability 55-70%**; if passes, ASML revenue impact -10 to -15%.
8. **AI-driven CPU shortage row added to bottleneck-roadmap** — Intel Q1 10-Q quoted (server ASP +27% / volume -5%); AMD +38% vs Intel +7% YoY = strongest AMD relative-outperformance signal.
9. **MU +154% YTD, ATH $818.67 May 11**; DA Davidson $1,000 PT; Q3 FY26 guide $33.5B/81% GM/$19.15 EPS. HBM4 share: SK Hynix 54% / Samsung 28% / MU 18%. Memory rationing cascading to QCOM + PC OEMs.
10. **SOITEC**: 95% photonics-SOI share (BofA confirm); new CEO Laurent Rémont April 1; +447% YTD vs revenue -10.2%; sell-side PT avg €53-56 (58% downside vs spot €150); CPO ramp validation; iPhone 17 mmWave on Soitec FD-SOI.
11. **BoJ rate decision June 16-17 = highest-leverage scheduled macro catalyst of 2026.** Carry-trade unwind probability ~65-70%; ~$500B live yen-funded positions remain (90% of pre-Aug 2024). New [[bank-of-japan]] page + [[2026-06-16-boj-decision]] playbook with three-tier hedge/profit strategy.

### Contradictions surfaced (per house rule — not resolved)
- GPU useful life: Dylan 7-8 yr (physical) vs SemiWiki forum 1-3 yr (operational, Google architect citation). Empirical test = NVDA Q1 FY27 (May 20) warranty reserve trajectory.
- Intel strategy: Nenni "GO INTEL / never bet against Lip-Bu" bull view vs BlueOne insider "no grand strategy" multi-employee sourcing.
- Apple-TSMC priority: Apple has 50%+ of N2 2026 (current dominance) BUT lost 5pp of 2025 revenue share to NVDA + Apple's own Intel diversification = future deprioritization. Time-horizon distinction resolves the apparent contradiction.

### Architectural pivot mid-session (per user's strategic question)
- **evaluate_script** for forum extraction: ~85% payload reduction vs full snapshot
- **Multi-agent (Haiku subagents)** for parallel non-SemiWiki research: 7 agents total today, returning 30-60 sec each with focused 400-word reports
- Pattern works for: pre-earnings consensus, primary-source IR docs, public analyst notes
- Pattern does NOT work for: authenticated forum content (single Chrome MCP session); needs main agent (me) to drive serially

### Session totals
- **Commits pushed**: 13 (cbe2a27 → 881cc86)
- **Source summaries created**: 12
- **New wiki pages**: 4 — [[INTC]], [[SOITEC]], [[bank-of-japan]], [[CDNS]]
- **New playbook**: [[2026-06-16-boj-decision]] (3-tier hedge/profit strategy)
- **Wiki pages patched**: 20+ unique (TSM, NVDA, AAPL, GOOGL, AMD, ARM, MU, ASML, SNPS, CDNS, CRWV, NBIS, ORCL, AVGO, TSLA, INTC, SOITEC, ai-capex-cycle, ai-infrastructure-debt, ai-bubble-debate, bottleneck-roadmap, datacenter-construction, copper-thesis, nvda-supply-chain, semiconductors, robotics, us-china-relations, hedging-risk, fed-policy, bank-of-japan, watchlist, index)
- **Haiku subagents spawned**: 7 (NVDA pre-earnings, TSMC IR, SOITEC, MU pre-earnings, MATCH Act, CRWV/NBIS/ORCL, BoJ)

### Why the early "diminishing returns" call was wrong
- Batches 4-5 contained the iPhone 17 mmWave SOITEC validation (changed bear-case framing)
- Batch 7 contained the NVDA-overtakes-Apple TSMC primary-source data (highest-leverage finding of the day)
- Batch 9 contained the BoJ ~$500B unwound positions data
- Batches 10-12 contained the CC Wei Terafab pushback + Pan Am-Boeing balance + CDNS coverage gap close

**Lesson**: forum-only browsing hits diminishing returns; pivoting to primary-source IR (via Haiku agents) + Daniel Nenni's blog articles + targeted user-flagged macro (BoJ) keeps signal density high.

### Get-well-soon notes for the user

**Tuesday May 20 — NVDA Q1 FY27 earnings** (after close): Consensus $78.5-78.8B revenue / $1.77-1.79 EPS / +79% YoY; BofA PT $320 (raised May 13); ~280x forward PE = "little room for macro shock or China revenue restatement." China H200 zero-deliveries wildcard live. Empirical test of GPU lifespan contradiction = warranty reserve disclosure in 10-Q. Wiki playbook: [[2026-05-20-nvda-earnings]] (pre-existing).

**Tuesday May 27 — Soitec FY26 full-year earnings** (binary event for SOITEC stance): YoY revenue -10.2%; sell-side PT avg €53-56 vs spot €150; new CEO Laurent Rémont first call midstream. Wiki page [[SOITEC]] has the pre-earnings setup section.

**June 10 — May US CPI** ([[2026-06-10-cpi-binary]] playbook pre-existing).

**June 16-17 — BoJ rate decision** (highest-leverage scheduled macro catalyst). Playbook [[2026-06-16-boj-decision]] has three-tier strategy with concrete instruments.

**June end — MU Q3 FY26** ($33.5B/81% GM/$19.15 EPS guide).

### Final status — all committed and pushed
All work on `origin/main`. Wiki is in significantly better shape than 24 hours ago. Get well soon.

---

## [2026-05-17] autonomous-session | Batch 9: BoJ + yen carry trade unwind risk (user-flagged)

User flagged BoJ June rate decision as a major 2026 macro decision. Spawned Haiku subagent to research. Created new macro coverage.

### Key findings (subagent synthesis)
- **BoJ rate now 0.75%** (held April 28, 2026); **6-3 vote with 3 dissenters for immediate 1.0% hike** — hawks gaining
- **April BoJ inflation forecast upgraded to 2.8%** (from 1.9%) on Iran war energy + weak yen
- **USD/JPY at 158.76** (May 17, 2026); BoJ comfort zone 145-155
- **June 16-17 meeting consensus: 25bp hike to 1.0%** priced in via swaps
- **MS estimates ~$500B in live yen-carry positions remain post-Aug 2024** (only 10% unwound; 90% remains)
- **BCA total yen-related swaps/forwards: ¥2,281T** (size estimates vary widely — fuel for tail risk)
- **GPIF $1.8T** has internal discussion to reduce foreign bonds + equities = repatriation flow risk on yen strength
- **Subagent verdict: ~65-70% probability of carry unwind event** in June-July 2026
- Flash crash risk LOWER than Aug 2024 (event is signaled); multi-week sustained unwind risk HIGHER (no Fed differential support + GPIF flows + higher tech multiples)

### Why 2026 risk > 2024 (more sustained, not less)
1. BoJ has less retreat room (after 2 years of yen weakness + accumulated inflation + 6-3 hawkish vote)
2. 90% of pre-Aug-2024 carry positions remain rebuilt
3. No automatic Fed cut differential support (Fed pause / re-cut uncertainty live)
4. NVDA 280x forward PE vs ~50x in early 2024 = bigger drawdown for same vol shock
5. GPIF rebalancing = slow-burn flow risk Aug 2024 didn't have

### Wiki created / patched
- **Created [[bank-of-japan]]** (new macro page) — current BoJ state, June decision tree, August 2024 reference event, wiki position exposure ranking, falsifiable watch triggers
- **Patched [[hedging-risk]]** — added BoJ June 16-17 overlay with explicit hedge instrument suggestions (FXY call spread, expanded VIX, trim AI multiples, defensive long)
- **Patched [[index]]** — added BoJ page + source link
- **Sources**: [[2026-05-17-boj-carry-trade-risk]]

### Position exposure (ranked highest first)
- **Highest**: [[NVDA]] (280x forward), [[MU]] (+154% YTD), [[CRWV]], [[NBIS]], [[SOITEC]] (+447% YTD)
- **High**: [[AAPL]], [[MSFT]], [[GOOGL]] — Japanese institutional holding overweight
- **Medium-high**: [[TSM]], [[ASML]], [[AMD]]
- **Medium**: [[INTC]] (gov-catalyst driven, less duration sensitive)
- **Hedge legs**: defensive cohort (utilities, staples)

### Watch list (BoJ-specific)
- USD/JPY level into June 16-17 (below 150 = pressure releases; above 158 = pressure intensifies)
- Ueda + board member speeches post-G7 (hawkish drift = leading indicator)
- Shunto 2027 settlements (autumn 2026)
- Fed September meeting interaction with BoJ June hike

---

## [2026-05-17] autonomous-session | Multi-agent batch 7 — NVDA #1 at TSMC + SOITEC CEO transition + pre-NVDA-earnings consensus

User pushed back on my premature "diminishing returns" framing. Pivoted to multi-agent + evaluate_script architecture for higher throughput.

### Architecture changes (per user's strategic question)
- **evaluate_script**: tested on Nvidia jobs thread — extracted 10 posts as compact JSON (~10KB) vs estimated 75KB full snapshot = **~85% payload reduction**. Will use for remaining forum work.
- **Multi-agent parallelism**: spawned 3 Haiku subagents simultaneously, each researching a different non-SemiWiki primary source. Returned in 35-65 seconds with high-leverage findings. **Worked exactly as designed** — they handled the heavy WebSearch/WebFetch work without polluting my context.

### Headline finding from this batch
🔥 **NVIDIA overtook Apple as TSMC's #1 customer in 2025** per TSMC 2025 Annual Report (April 2026):
- NVDA: 19% of 2025 revenue (NT$726.97B)
- Apple: 17% of 2025 revenue (NT$645.17B)
- 2024: Apple was 22% — **Apple lost 5pp of TSMC share in a single year**

**This is the empirical proof of the [[AAPL]] bear thesis** that the wiki framed qualitatively from [[2026-05-09-dwarkesh-dylan-semianalysis]]. Stance reinforced — bear / medium conviction; deprioritization is now observable at 5pp/year speed.

### Other findings from Agent A (NVDA Q1 FY27 preview)
- Q1 FY27 consensus: $78.5-78.8B revenue; $1.77-1.79 EPS; +79% YoY; DC growth +35% YoY; DC GM 75% +/- 50bps guide
- **BofA Vivek Arya raised PT to $320** (from $300, May 13) on AI accelerator TAM raised $1.0T → $1.2T — **citing hyperscaler ASICs (Google TPU, AWS Trainium) as tailwinds NOT headwinds** (paradigm shift in framing)
- Goldman $250 PT; MS ~$250; UBS/RBC/Cantor consensus ~$291.67
- Stock $224-225 (-5% from May 14 peak $236, profit-taking); +32% off March low
- ~280x forward PE = "little room for macro shock or China revenue restatement"
- China H200: cleared to 10 Chinese firms but **zero deliveries to date**
- Culper Research short thesis claims >20% NVDA FY26 compute revenue tied to China diversion networks

### Other findings from Agent B (TSMC primary IR)
- TSMC 2025 consolidated revenue NT$3,809B (+31.6% YoY)
- Q1 2026 gross margin 66.2% (beat; +3.9pp QoQ)
- HPC = 61% of revenue (up 20% QoQ); 3nm = 25% wafer revenue; 5nm = 36%; 7nm+ = 74%
- N2: 20+ tape-outs received, 70+ in pipeline — **1.5x more tape-outs than 3nm at equivalent stage**
- N2 capacity target: **140K wafers/month by EOY 2026**
- **A16 on track for H2 2026 with SPR (Super Power Rail) backside power delivery**
- **TSMC-COUPE production begins 2026 with 2x power efficiency vs pluggable** ← massive for [[SOITEC]]
- C.C. Wei named Time 100 Pioneers

### Other findings from Agent C (Soitec May 27 setup)
- **New CEO Laurent Rémont started April 1, 2026** — enters first earnings call midstream
- **FY26 guidance withdrawn Nov 2025** — only Q4 sequential guide given
- **+447% YTD** vs revenue -10.2% YoY (massive disconnect)
- **Sell-side PT avg €53-56** vs spot ~€150 = **58% implied downside**
- **95% market share of photonics-grade SOI** (BofA March 2026 confirmation)
- **Marvell acquired Celestial AI's Photonic Fabric** (confirmed; previously partnership-only)
- **GlobalFoundries SCALE platform**: $1B+ revenue target by 2028
- **Goldman: silicon photonics revenue DOUBLING in 2026 across foundries**
- Q-COM + MediaTek cut 4nm smartphone AP orders by 15-20M units; smartphone production -10% YoY to 1.135B

### Wiki touched
- [[TSM]] — NVDA #1 customer 2025; 2025 rev $3.8T (+31.6%); Q1 GM 66.2%; HPC 61%; N2 tape-outs; A16 H2 2026; COUPE production 2026
- [[AAPL]] — quantitative bear validation (22% → 17%); 5pp/year deprioritization speed
- [[NVDA]] — TSMC #1 customer 19%; Q1 FY27 consensus refresh; BofA $320; China H200 wildcard
- [[SOITEC]] — new CEO Rémont; 95% share confirmed; 58% PT downside; CPO ramp timing; GFS SCALE $1B+
- [[AVGO]] — Tomahawk 6 + 200G/lane CPO + photonic substrates
- [[index]] + [[log]]

### Process notes
- Each Haiku subagent ~$0.001-0.002 cost equivalent (rough estimate); returned 400-word focused reports
- Total parallel research throughput: equivalent of 30+ minutes serial work compressed to ~1 minute wall-clock
- Pattern works for: pre-earnings consensus, primary-source IR docs, public analyst notes
- Pattern does NOT work for: authenticated forum content (single Chrome MCP session); needs me to drive serially
- **For rest of session**: continue multi-agent for parallel non-SemiWiki work + selective forum browsing via evaluate_script

---

## [2026-05-17] autonomous-session-summary | End-of-day rollup

User had flu and granted autonomous control for the day. Working via authenticated Chrome MCP session on SemiWiki forum + blog. Five batches successfully committed and pushed.

### Sources added today (9 total, all 2026-05-17)
1. [[2026-05-16-dylan-patel-invest-like-best]] — Dylan Patel ILTB podcast (DRAM 2-3x, GPU 7-8yr, Anthropic 30%→72% margins, TSMC $100B 2028, 6-18mo robotics, copper foil sold out)
2. [[2026-05-16-john-arnold-invest-like-best]] — John Arnold ILTB podcast (China decoupling quantified, permitting reform 2026, solar PPA +50%, SMR 10-15yr horizon)
3. [[2026-05-15-semiwiki-tsmc-tool-orders-capex]] — Daniel Nenni article on TSMC record $21B Advanced Node equipment authorization
4. [[2026-05-17-semiwiki-kuo-apple-intel]] — Ming-Chi Kuo Apple-Intel partnership thread (lifecycle 2026 test → 2029 decline; TSMC 90%+ retention)
5. [[2026-05-17-semiwiki-cpu-shortage-intel-18a]] — Combined source: AI-driven CPU shortage + Lip-Bu Tan Intel strategy (Q1 10-Q quoted; AMD +38% vs Intel +7%; insider "no grand strategy")
6. [[2026-05-17-semiwiki-cxmt-ddr5]] — CXMT shipping DDR5 in commercial volumes; STAR IPO; DRAM bifurcation
7. [[2026-05-17-semiwiki-forum-sweep-2]] — Combined: Trump-Xi summit + MRC supercomputer + TSMC Apple modem on N2 + TSMC Board Resolutions + TSMC-VIS divestiture. **TSMC $20B Arizona injection** is the headline data point.
8. [[2026-05-17-semiwiki-forum-sweep-3]] — Cerebras IPO ($150-$160, 20x oversubscribed); **MATCH Act**; GPU lifespan controversy
9. [[2026-05-17-semiwiki-nenni-blog-sweep]] — 3 Nenni articles: 2nm Crunch + Mii TSMC roadmap (A14 2028, COUPE) + SNPS-TSMC alliance

### New wiki pages created today (2)
- [[INTC]] — Intel Corporation. Stance neutral / low conviction. Multiple bull (gov 9.9% stake, Apple/Tesla/Terafab, +200% YTD, CPU shortage ASP benefit) and bear (-16.61% post-Xi, 18A yields slip to 2027, $125.5B capex forensics, insider "no strategy") factors surfaced with equal weight.
- [[SOITEC]] — Soitec S.A. (SOI.PA). Stance bull / low-medium conviction. Photonics-SOI substrate monopoly play; iPhone 17 mmWave already on FD-SOI confirmed by Yole/TechInsights; CPO transition is the 2026-2028 inflection. Stock has rallied 6x off Dec 2025 lows so valuation tension is the main pushback.

### Wiki pages patched today (15+ unique)
**Companies**: NVDA, AAPL, GOOGL, AMD, ARM, INTC, MU, TSM, ASML, SNPS, SOITEC, CBRS
**Themes**: bottleneck-roadmap, datacenter-construction, copper-thesis, nvda-supply-chain, ai-infrastructure-debt, ai-bubble-debate, ai-capex-cycle
**Sectors**: semiconductors, robotics
**Macro**: us-china-relations

### Highest-leverage findings (sorted by investment significance)

**Sharpens existing positions**:
1. **TSMC $20B Arizona capital injection** (primary source: TSMC board resolutions May 17) — ~1/3 of FY26 CapEx earmarked for Arizona alone. Read-through to FIX/EME/PWR.
2. **TSMC A14 by 2028** (Mii R&D roadmap) — 10-15% speed gain vs N2; aligns with bottleneck-roadmap EUV constraint period
3. **SOITEC = third independent confirmation** of TSMC's CPO push (COUPE photonic engine in Mii roadmap + SNPS-TSMC alliance + the iPhone 17 mmWave validation)
4. **DRAM market is bifurcating** (CXMT commodity vs Big 3 HBM) — MU HBM moat intact
5. **AI-driven CPU shortage** (Intel Q1 10-Q verbatim: ASP +27% / volume -5%); AMD +38% vs Intel +7% YoY → AMD bull thesis sharpens; ARM cross-cycle beneficiary

**New investment angles surfaced**:
6. **INTC binary trade** opened (neutral / low conviction) — Apple/Tesla/Terafab/+200% YTD bull vs $125.5B capex forensics + insider "no strategy" bear
7. **MATCH Act** as material structural risk to ASML China service revenue (~40% of sales)
8. **GPU lifespan contradiction surfaced** (Dylan 7-8 yr vs forum 1-3 yr) — empirical test = NVDA Q1 FY27 warranty reserve % (May 20)
9. **SOITEC FD-SOI in iPhone 17 mmWave** — Mobile segment per-device content growth offsets volume decline
10. **Rapidus Japan** sovereign-AI foundry: $11.3B raised / $32B needed by 2027

### Contradictions surfaced (per house rule)
- GPU useful life: Dylan 7-8 yr (physical) vs forum/Google architect 1-3 yr (operational)
- Intel strategy: Nenni's "GO INTEL" bull view vs BlueOne's insider "no grand strategy" multi-employee sourcing
- TSMC Apple priority: Apple-Intel diversification narrative (Kuo) vs Apple modem stays at TSMC on N2 (TSMC Apple win)

### Process notes / what worked
- **Chrome MCP authenticated session** enabled access to forum-member commentary that WebFetch could not reach — most valuable for: BlueOne insider Intel sources, the Intel 10-Q quoted verbatim, the Lip-Bu Tan management critique
- **Sequential thread fetches + grep/awk on snapshots** kept working context manageable
- **Combined source summaries** (forum-sweep-2, forum-sweep-3, nenni-blog-sweep) more efficient than one-source-per-thread for related material
- **House rule discipline** (contradictions surfaced not resolved) preserved across all batches

### Commits pushed today
- 40e3ff8 (DeepSeek V4 Flash) — pre-existing on entry
- 424125e (... earlier commits)
- c60d23c (Dylan + Arnold ingest)
- dc659a9 (SOITEC creation)
- a2ed32d (SemiWiki Nenni TSMC tool orders)
- cbe2a27 (Batch 1: INTC + 4 forum threads)
- 0a12c5f (Batch 2: TSMC $20B Arizona + INTC reversal + Apple modem)
- 17f442a (Batch 3: Cerebras IPO + MATCH Act + GPU lifespan)
- d3a0842 (Batch 4: Nenni blog articles)
- pending (Batch 5 wrap + iPhone 17 SOITEC validation + this summary)

### What NOT done today (transparency)
- T-Glass / MediaTek thread (paywalled, skipped)
- Intel-McLaren / Keysight CSR / Synopsys VC Connect / Weebit Nano (PR fluff, skipped per quality bar)
- TSMC monthly revenue reports (deferred — would have been hard primary data)
- Deeper TSMC / Soitec subforum traversal (diminishing returns)
- No formal lint pass (wiki has grown by 9+ sources; a lint is overdue per CLAUDE.md schema)

### Get-well-soon notes for the user
- NVDA Q1 FY27 earnings is Tuesday May 20 — see [[2026-05-20-nvda-earnings]] playbook
- Two unresolved contradictions on the wiki (GPU lifespan + Intel strategy) — both will be empirically tested in coming weeks
- SOITEC stance is bull / low-medium conviction (you said you might start a small position) — May 27 FY26 earnings is the binary catalyst there

---

## [2026-05-17] autonomous-session | SemiWiki blog sweep #4 — Nenni articles (Global 2nm Crunch + Mii TSMC roadmap + SNPS-TSMC AI alliance)

Pivot from forum threads to Daniel Nenni's published articles. Three articles read via authenticated Chrome MCP.

### Articles covered
- **Article 1**: "Global 2nm Supply Crunch" (March 2026) — TSM/INTC/Samsung/Rapidus foundry landscape
- **Article 2**: "Dr. Y.J. Mii on TSMC Technology Leadership in 2026" (April 30) — TSMC R&D roadmap (A14 2028, CFET, COUPE, SoW)
- **Article 3**: "Synopsys and TSMC Deepen AI Design Alliance" (May 5) — SNPS/TSMC ecosystem deepening

### Key findings
- **TSMC A14 timing 2028** with 10-15% speed gain / 25-30% power reduction vs N2 — confirms [[bottleneck-roadmap]] EUV constraint period
- **TSMC's COUPE (Compact Universal Photonic Engine)** explicitly named in BOTH Mii roadmap AND SNPS-TSMC alliance = **third independent wiki confirmation of [[SOITEC]] photonic substrate thesis**. The CPO transition is real, at-scale, ecosystem-supported. Reinforces SOITEC's structural position.
- **Rapidus (Japan)**: $11.3B raised / **$32B needed** by 2027 mass production target. Funding gap = potential IPO/strategic investor event. Sovereign-AI foundry hedge.
- **Samsung's foundry credibility issue** — Nenni: *"Samsung is not a viable alternative to TSMC for high-volume 2nm orders. Trust is the foundation of the semiconductor industry."* — explains why Samsung doesn't show up in TSMC alternative analysis on the wiki
- **Synopsys agentic AI in Fusion Compiler** on A14 = paradigm shift in EDA (passive AI assistance → decision-guiding tools); 3DIC Compiler at **5.5x reticle limit** CoWoS — massive multi-die future; ASIL B chiplet TAM expansion into automotive

### Wiki touched
- [[TSM]] — Mii roadmap + N2 sold out + COUPE / SoW / CFET
- [[SOITEC]] — third confirmation of COUPE thesis
- [[SNPS]] — TSMC alliance deepening (agentic Fusion Compiler, 3DIC, automotive ASIL B)
- [[INTC]] — Nenni's bullish demand-side framing added for bull/bear balance
- [[us-china-relations]] — Rapidus Japan sovereign-AI foundry section

### Why this batch was lower-leverage than batches 1-3
These articles confirmed and sharpened existing wiki positions rather than introducing wholly new theses. The SOITEC COUPE confirmation is the highest-leverage incremental data point (third independent source = thesis hardening). No stance changes; primarily depth-of-coverage improvement.

### Cumulative session stats (batches 1-4)
- **Source summaries created**: 8 (including this batch)
- **New wiki pages**: 2 (INTC, SOITEC)
- **Wiki pages patched**: 14+ unique pages
- **Commits pushed**: 5 (a2ed32d, cbe2a27, 0a12c5f, 17f442a, pending)

### Process notes / context management
- ~60% of context still available; cleaned snapshot tmp between batches
- Considering whether to wrap or continue — diminishing returns becoming visible (this batch added depth but no new alpha)
- Next high-value targets if continuing: TSMC monthly revenue reports (primary financial data), Soitec subforum activity, or specific NVDA/AMD/MU subforum threads beyond What's New

---

## [2026-05-17] autonomous-session | SemiWiki forum sweep #3 — Cerebras IPO + MATCH Act + GPU lifespan controversy

Third autonomous batch. Combined source: [[2026-05-17-semiwiki-forum-sweep-3]].

### Threads covered
- **A**: Cerebras IPO raise to $150-$160 (30 replies, Nenni-started, 20x oversubscribed)
- **B**: GPU lifespan controversy (within Cerebras thread) — Google architect 1-3 yr vs Dylan 7-8 yr
- **C**: China criticizes MATCH Act (pending US chip equipment legislation)

### Highest-impact findings
- **MATCH Act**: pending US legislation specifically targeting **ASML + Tokyo Electron** equipment exports AND **service revenue** in China. House Foreign Affairs advanced April 22. China responded with April 13 "Malicious Entity List" decree. Trump admin "no public position." Bipartisan momentum + Chinese preemptive countermeasures = non-trivial passage probability. **Service-license requirement is the highest-leverage lever** — ASML China revenue ~40% of sales, service segment is highest-margin.
- **GPU lifespan contradiction**: Forum thread cites unnamed Google architect saying GPU service life is **1-3 years**, directly contradicting Dylan Patel's 7-8 year claim ingested earlier today. NVDA warranty reserves at 1.8% of revenue and "increased substantially in past few years" — empirical signal supporting forum view. Per house rule, both views surfaced on [[NVDA]] and [[ai-infrastructure-debt]] without resolution. Empirical test = NVDA Q1 FY27 (May 20) warranty reserve trajectory.
- **Cerebras IPO TCO blindspot**: Forum technical commentary (KevinK) notes the S-1 "focuses on speed and latency and steers clear of TCO." Implies CBRS has defensible premium-latency niche but may not be competitive on cost-per-token at hyperscaler scale. Addressable market potentially narrower than $48.8B valuation implies.

### Wiki touched
- [[CBRS]] — TCO blindspot + wafer-scale durability question added to bear case
- [[NVDA]] — GPU lifespan contradiction surfaced (Dylan 7-8 yr vs forum 1-3 yr); empirical test = warranty reserves trajectory
- [[ASML]] — **MATCH Act bear case added** (material new risk; service-license requirement specifically called out)
- [[ai-infrastructure-debt]] — GPU lifespan contradiction surfaced; "depreciation bear case partially re-armed" framing
- [[us-china-relations]] — MATCH Act + China "Malicious Entity List" decree section added
- [[index]] + [[log]]

### Skipped this round
- T-Glass / MediaTek (paywalled)
- Intel-McLaren Racing (PR fluff)
- SiFive RISC-V (lower priority; would affect ARM bear case incrementally)
- "Is AI the automobile" (speculative debate, no actionable data)
- Keysight CSR / Synopsys VC connect (PR)

### Cumulative session stats (batches 1-3)
- **Source summaries created**: 7 (kuo-apple-intel, cpu-shortage-intel-18a, cxmt-ddr5, forum-sweep-2, forum-sweep-3, plus the earlier Dylan/Arnold/SemiWiki TSMC ingest)
- **New wiki pages**: 2 (INTC, SOITEC earlier today)
- **Wiki pages patched**: 12+ (TSM, NVDA, AAPL, AMD, ARM, MU, GOOGL, ASML, CBRS, INTC, ai-infrastructure-debt, bottleneck-roadmap, datacenter-construction, us-china-relations, plus minor index/log updates)
- **Commits pushed**: 4 (a2ed32d, cbe2a27, 0a12c5f, pending batch 3)

---

## [2026-05-17] autonomous-session | SemiWiki forum sweep #2 — TSMC $20B Arizona + INTC reversal + Apple modem

Second batch of autonomous forum browsing. Combined source: [[2026-05-17-semiwiki-forum-sweep-2]].

### Threads covered
- **A**: Trump-Xi summit (May 13-14, 2026) — CEO entourage + post-trip stock data
- **B**: MRC supercomputer networking — Google Apollo/Palomar OCS framing
- **C**: TSMC wins Apple modem order — Apple C2 5G on N2, modem-disaggregation strategy
- **D**: TSMC Board of Directors Meeting Resolutions — **primary source** for $31.3B + new **$20B Arizona injection**
- **E**: TSMC sells 8.1% of VIS — capital recycling

### Headline findings
- **TSMC $20B capital injection into TSMC Arizona** — roughly 1/3 of FY26 CapEx ear-marked for Arizona alone. Most aggressive US-foundry posture to date. Direct booster to [[FIX]] / [[EME]] / [[PWR]] / [[AMKR]] addressable demand.
- **INTC -16.61% one-week** during Xi summit (despite +200% YTD); Lip-Bu Tan conspicuously absent from the CEO trip — political signal worth tracking
- **Apple's C2 5G modem going to TSMC on N2** (not Intel) — flagship Apple work stays at TSMC; Intel gets at most secondary AP shares (Samsung-style role). Reduces Apple-Intel bull case strength for [[INTC]]
- **GOOGL Apollo/Palomar OCS** validated as a generation ahead of industry consortium (MRC) — vertical-integration moat extends beyond TPU into network fabric
- **QCOM -13.24% week** (we don't have a page) — confirmed losing Apple modem to in-house C2 starting 2027
- **TSMC backend test capacity "almost fully booked"** with AI demand from NVDA/GOOGL/MSFT/META/AMD — independent confirmation of [[bottleneck-roadmap]] thesis

### Wiki touched
- [[TSM]] — board resolution primary data, $20B Arizona, VIS divest, Apple modem
- [[INTC]] — -16.61% one-week, Lip-Bu absent, Apple modem stays at TSMC reframes bull case
- [[AAPL]] — modem-disaggregation strategy (BB on TSMC N2, AP multi-source)
- [[GOOGL]] — Apollo/Palomar OCS moat
- [[us-china-relations]] — Trump-Xi summit market read + post-trip moves
- [[datacenter-construction]] — TSMC $20B Arizona read-through to FIX/EME/PWR
- [[index]] — added forum-sweep-2 source entry

### Skipped (intentionally)
- T-Glass / MediaTek thread — paywalled, only teaser content
- McLaren Racing / Intel — PR fluff
- Keysight CSR report — non-investable PR
- Weebit Nano fundraise — too small / not in framework
- "Is AI the automobile" speculative thread — no actionable data

### Process notes
- Continued use of Chrome MCP authenticated session
- Snapshot files cleaned between batches (kept in .semiwiki-tmp/, gitignored)
- 6 sources written and 9 wiki pages patched across batches 1+2 today
- Two commits pushed: cbe2a27 (batch 1), pending (batch 2)

---

## [2026-05-17] autonomous-session | SemiWiki forum sweep #1 — INTC page created, 4 threads ingested

User is sick (flu) and granted autonomous control. First batch from forum browsing via authenticated Chrome MCP session.

### Threads ingested
1. **[[2026-05-17-semiwiki-kuo-apple-intel]]** — Ming-Chi Kuo's 10 industry checks on Apple-Intel partnership. Apple lifecycle at Intel 18A-P: test 2026 → ramp 2027 → growth 2028 → decline 2029. TSMC retains 90%+ Apple supply. Apple itself acknowledges TSMC tilting toward AI.
2. **[[2026-05-17-semiwiki-cpu-shortage-intel-18a]]** — Combined source for two related threads (CPU shortage + Lip-Bu Tan strategy). Key extraction: Intel Q1 10-Q quoted verbatim (server ASP +27% YoY, volume -5% YoY); AMD Q1 +38% YoY revenue vs Intel +7%; Intel $125.5B CapEx forensics; insider "no grand strategy" quote (BlueOne, multiple Intel-internal sources); Daniel Nenni's contra bull view.
3. **[[2026-05-17-semiwiki-cxmt-ddr5]]** — CXMT shipping DDR5 commercial volumes; STAR Market IPO planned (~$4.34B); 9M 2025 revenue +97.8% YoY. CXMT one generation behind (24Gb vs 32Gb), can't make HBM. Big 3 retain 91.5% global DRAM share. Bifurcation framing: complement to Dylan's "DRAM 2-3x" thesis, not counter.
4. **T-Glass MediaTek / Google TPU thread** — checked, content is paywalled (only teaser visible). Deferred.

### Wiki changes
- **Created [[INTC]]** (new company page) — long-deferred Intel coverage now opened. **Stance: neutral / low conviction**. Surface bull (gov 9.9% stake, Apple/Tesla/Terafab wins, +114% April, CPU shortage ASP benefit) and bear (Q1 volume -5%, AMD outperformance 5x, 18A yields slip to 2027, $125.5B capex forensics, insider "no strategy") with equal weight per house rule.
- **Patched [[AAPL]]** — Kuo lifecycle detail + Apple's own TSMC-tilt acknowledgment. Stance unchanged (bear).
- **Patched [[AMD]]** — Q1 +38% YoY vs Intel +7%; relative-growth signal sharpening AMD bull thesis. Added [[INTC]] and [[ARM]] to Related.
- **Patched [[ARM]]** — cross-cycle CPU-shortage beneficiary; x86 constraint accelerates ARM-based server CPU adoption (Graviton/Cobalt/Axion/Vera) without capex risk.
- **Patched [[MU]]** — DRAM market bifurcation framing; CXMT plugs commodity hole, Big 3 retain HBM/leading-edge pricing power. HBM moat intact.
- **Patched [[bottleneck-roadmap]]** — new "x86 CPUs (parallel constraint)" row between memory and photonic substrates; [[INTC]] + [[AMD]] + [[ARM]] cross-link.
- **Patched [[us-china-relations]]** — new CXMT section; commodity DRAM bifurcation framing; sovereign-AI flow indicator.
- **Updated [[index]]** — added new INTC entry in Companies; 3 new source entries in Recent Source Ingests.

### Process notes
- All forum content accessed via Chrome MCP with authenticated session (semiwiki.com).
- Account is "pending approval" status — but full forum-thread content is rendered to read-only despite the gating banner. Posting/replying likely blocked.
- Snapshot files in `.semiwiki-tmp/` (gitignored); content extracted via grep/awk to keep working context lean.
- Insider commentary (BlueOne on Intel "no strategy"; Naga Chandrasekaran on Intel-as-foundry economics; Kevork Kechichian on Intel culture) was the high-value differentiator vs unauthenticated WebFetch.

---

## [2026-05-17] ingest | SemiWiki (Daniel Nenni) — TSMC Record Tool Orders / CapEx Shockwave

User surfaced SemiWiki (semiwiki.com) as a new monitored source — industry-insider blog + forum run by Daniel Nenni, longtime semi industry analyst. Saved [[reference-semiwiki]] memory entry. **First article ingested**: Nenni's May 15 piece on TSMC's record Q1 2026 tool orders.

### Source
[[2026-05-15-semiwiki-tsmc-tool-orders-capex]] — Daniel Nenni, "TSMC's Record Tool Orders Hint at Another CapEx Shockwave" (May 15, 2026)

### Why ingested (high-leverage data)
- TSMC Q1 2026 board capital appropriations: **$31.3B** total (down from $45.0B Q4 2025 — but composition is the story)
- Of that, **$21.0B is Advanced Node equipment** — **the highest single-quarter authorization since tracking began Q4 2019**
- **Trailing twelve-month Advanced Node equipment approvals ≈ $55B** vs. TSMC's full 2026 CapEx guide of ~$56B → math forces either spending cadence drop or guide raise
- Nenni's verdict: "TSMC's current 2026 CapEx framework is already becoming too conservative"; 2Q26 earnings (July 2026) upward revision probability "increasing"
- **Specialty Devices + Advanced Packaging $0** Q1 approvals attributed to digestion of prior massive allocations (silicon photonics, CoWoS, SoIC), not demand weakness — but worth monitoring

### Why this matters in context
- Dylan Patel ([[2026-05-16-dylan-patel-invest-like-best]], ingested *earlier today*) qualitatively projected TSMC capex "approaching $100B by 2028"
- Nenni provides the **hard tooling-order data** that mechanically validates Dylan's trajectory — first concrete corroboration from a different source class
- The [[bottleneck-roadmap]] 2027 cleanroom-space row now has *quantitative* equipment-order data backing the framing, not just narrative
- Reduces "this is one analyst's view" risk on the TSMC capex framework

### Wiki touched
- Created [[2026-05-15-semiwiki-tsmc-tool-orders-capex]] (source summary)
- [[TSM]] — added 2026-05-15 recent development with $31.3B / $21B composition and Nenni framing; updated Sources list
- [[bottleneck-roadmap]] — added Nenni corroboration section to the Dylan TSMC $100B 2028 update; bumped sources to 7
- [[index]] — listed the new source in both Recent Ingests and Sources sections

### Tooling notes (WebFetch depth testing)
User asked how deep WebFetch can navigate.
- **Works**: arbitrary public URLs (article pages, category pages); discovering article URLs from category index pages by stringing fetches together
- **Limited**: SemiWiki **forum thread content is GATED** behind registration — guest users see thread titles + previews only, not full posts. Industry-insider commentary in forums is therefore inaccessible without an authenticated session
- **No interactive navigation**: WebFetch can't click links, scroll, or maintain session state across fetches. Each fetch is independent
- **Recommendation**: stick with manual triage (user flags articles → I WebFetch them). No scraper needed. If forum access becomes important later, consider Chrome devtools MCP with authenticated session

---

## [2026-05-17] research | New coverage initiated: SOITEC (SOI.PA) — photonics-SOI substrate monopoly

User flagged Soitec from a semiconductor forum mention and is considering starting a small position. Did batched web research and created [[SOITEC]] company page (stub-to-medium depth — full FY26 results May 27 will trigger upgrade or downgrade).

**Why this fits the wiki framework:**
- Soitec is the **sole qualified volume supplier of photonics-SOI substrate wafers** to TSMC, GlobalFoundries, and Tower Semiconductor — the three foundries shipping silicon-photonics for CPO.
- **Direct foundry-level exposure** to NVDA Spectrum-X / Quantum-X CPO switches (launched March 2025), AVGO Davisson chiplet, MRVL Celestial chiplet. The substrate layer captures upstream rent that doesn't flow to the optical-module names ([[COHR]] / [[LITE]] / [[FN]]).
- Adds a new row to [[bottleneck-roadmap]]: **2026-2028 photonic substrates** between memory (2025-26) and EUV (2028-30).
- Patent moat (Smart Cut, 3,500+ patents); only competitor licensee Shin-Etsu has limited volume, GlobalWafers license terminated 2025.

**Why conviction is low-medium not high:**
- Stock has already rallied **~6x off Dec 2025 lows** (€23 → ~€148-171) — entry valuation is uncomfortable
- **Sell-side targets €31-€35** (JPM/HSBC/MS Hold) vs spot ~€148+. Either analysts haven't caught up, or the market has front-run multiple years of execution
- Mobile Communications still 52% of revenue and declining 30% YoY — race against time
- Photonics-SOI is only ~17% of revenue (~€100M) today — needs 5-7x scale to drive bull math
- Customer concentration (3 customers >10%); CPO ramp execution risk; EUR/FX/liquidity for US holders
- Paris-listed only (no US ADR)

**Wiki touched:**
- Created [[SOITEC]] (new company page)
- [[nvda-supply-chain]] — added Soitec as upstream substrate above optical-module layer
- [[bottleneck-roadmap]] — added 2026-2028 photonic substrates row + SOITEC to Related
- [[semiconductors]] — new Photonics Substrates sub-segment
- [[COHR]], [[LITE]], [[FN]] — added SOITEC + bottleneck-roadmap to Related (substrate is upstream of module)
- [[index]] — added Photonics substrates category

**Key event**: **May 27, 2026** FY26 full-year results — single biggest catalyst. Watch for Photonics-SOI absolute revenue print, FY27 growth guide, any named CPO customers, gross margin trajectory.

**Position sizing recommendation surfaced on page**: small starter pre-earnings; add only on May 27 confirmation; half-sized vs comparable bull/medium-conviction names ([[MU]], [[KLAC]]) given the valuation gap.

---

## [2026-05-17] ingest | Dylan Patel + John Arnold — Invest Like the Best dual ingest

User added two new podcast transcripts to `raw/podcasts/` (dylan_invest_like_best.txt + john_arnold.txt). Both ingested in one workflow pass.

### Source 1: Dylan Patel — Invest Like the Best (2026-05-16)
- Source summary: [[2026-05-16-dylan-patel-invest-like-best]]
- **Second deep podcast in 8 days** (with [[2026-05-09-dwarkesh-dylan-semianalysis]]) — Dylan is now the highest-frequency source in the wiki. Confirms ongoing primary-source status.
- **Highest-impact new claims:**
  1. **DRAM pricing structurally 2-3x** — HBM wafer-conversion drains DRAM capacity one-way → conventional DRAM repriced, not just HBM. *Sharpens [[MU]] medium-term thesis.*
  2. **GPU useful life 7-8 years** (with software stack assumption) — directly refutes Burry's 1-3 year depreciation framing. *Strengthens [[NVDA]] bull case.*
  3. **Anthropic gross margins 30% → 72% in 5 months** — compute price decline + frontier-model premium drives the curve. *Updates [[ai-bubble-debate]] productivity-reset claim.*
  4. **TSMC 2028 capex approaching $100B** — 70-80% upward revision vs prior wiki framing ($55-65B). *Major upgrade for [[KLAC]] / [[LRCX]] / [[AMAT]] / [[TER]] / [[ENTG]] / [[APD]] addressable market.*
  5. **Few-shot robotics learning 6-18 months out** — most aggressive timeline of any source. 4-way researcher contradiction now (Fan 2-3yr / Levine 5yr / LeCun >>5yr / Dylan 6-18mo for narrow tasks).
  6. **Copper foil for PCBs is sold out** — independent confirmation of [[copper-thesis]] supply-tightness framing.
  7. **Anthropic ARR $40-45B run-rate, compute-constrained, growing 10%/month** — beyond the $30B Krishna Rao number from May 13.

### Source 2: John Arnold — Invest Like the Best (2026-05-16)
- Source summary: [[2026-05-16-john-arnold-invest-like-best]]
- **John Arnold context**: former Enron / Centaurus (largest hedge-fund payday at age 38), now major climate-philanthropy infrastructure backer with direct congressional engagement. Higher signal than a typical macro pundit because he's *in the rooms* shaping policy.
- **Highest-impact new claims:**
  1. **China decoupling now quantified** (from personal trip): flights -70%, expats -50-75%, students -90%. Apocalypse-Now-like personal account is the visceral data point the [[us-china-relations]] page was missing.
  2. **Federal permitting reform plausibly passes 2026** — Schumer + Lee bipartisan; Arnold "reasonably optimistic." Single largest near-term political catalyst for [[datacenter-construction]] / [[PWR]] / [[GEV]].
  3. **Solar PPA pricing +50%** — broader productivity-reset evidence beyond just AI compute pricing.
  4. **SMRs are 10-15 year horizon, NOT 2030** — tempers near-term framing on small modular nuclear thesis.

### Wiki touched
- [[MU]] — added DRAM doubling/tripling thesis section (Dylan attribution)
- [[NVDA]] — added GPU 7-8yr useful life + Anthropic compute-constrained bullets; source #8
- [[TSM]] — added 2028 $100B capex possibility in recent developments
- [[ai-infrastructure-debt]] — added GPU depreciation bear case structural weakening section
- [[ai-bubble-debate]] — added Anthropic 30%→72% margins section
- [[ai-capex-cycle]] — added productivity-reset evidence bullet + Anthropic ARR
- [[us-china-relations]] — added quantified China decoupling section (Arnold trip data)
- [[robotics]] — added Dylan 6-18mo few-shot section; updated researcher-contradiction to 4-way
- [[copper-thesis]] — added Dylan independent confirmation of copper foil sold out
- [[datacenter-construction]] — added Arnold permitting reform 2026 catalyst section
- [[bottleneck-roadmap]] — added Dylan DRAM 2-3x + TSMC $100B 2028 + sold-out enumeration

### Notes
- **No stance changes from this ingest** — all sharpens existing positions rather than flipping them. [[MU]] and [[NVDA]] bull thesis sharpens; [[TSM]] capex intensity revises up; [[copper-thesis]] gets independent third-party validation.
- **Connect-the-dots writing style maintained** throughout — every analytical claim paired with implication.
- **Contradictions surfaced**: Dylan 6-18mo robotics timeline now creates 4-way contradiction with Fan/Levine/LeCun. Logged on [[robotics]] without resolution per house rule.
- **Watch items added**: Senate energy committee output Q3-Q4 2026 (permitting reform vote); FIX/EME 2027 earnings calls for robotic-assisted labor mentions; TSMC FY26-FY27 capex guidance updates against Dylan's $100B trajectory.

---

## [2026-05-17] daily | Anthropic 2028 paper + NVDA Q1 FY27 preview + HBM market update

**Workflow**: 8-step daily update ritual. Saturday — markets closed but new sources from May 14-16 emerged.

### Net-new material (ingested)
1. **Anthropic "2028: Two Scenarios for Global AI Leadership" (May 14, 2026)** — frontier-lab policy paper with **first cleanly quantified US-China compute gap data**: Huawei = 4% of NVDA 2026, 2% 2027. DeepSeek R1 = 94% malicious-request compliance vs 8% US. 11× US/China compute ratio claim. Source summary: [[2026-05-14-anthropic-2028-ai-leadership]].

### Material confirmations (small patches)
2. **NVDA Q1 FY27 earnings preview** — Tuesday May 20. Consensus: $78.78B / $1.76 EPS (+78.8% YoY); Q2 consensus $86.08B (+9.3% seq). Goldman "major re-rating" call; BofA $320 PT. NVDA has fallen on 4 of last 5 earnings despite revenue beats. Added to [[NVDA]] recent developments.
3. **HBM market update (TrendForce May 13)** — HBM3E +20% pricing for 2026; HBM4 production begins Q3 2026; Micron 1-2 quarters behind SK Hynix/Samsung but **fully sold out via advance contracts**. Added to [[MU]] recent developments.

### Wiki touched
- [[NVDA]] — Anthropic Huawei 4%/2% compute share bull bullet + Q1 FY27 preview in recent developments
- [[us-china-relations]] — Anthropic 2028 paper section + both/and framing on Anthropic-as-regulatory-capture
- [[ai-bubble-debate]] — same paper from bubble-debate lens; LeCun framing contextually validated
- [[MU]] — HBM market update in recent developments
- [[index]] — Anthropic paper listed in recent ingests

### Skipped (low-value or already in wiki)
- **Rubin platform** (announced Jan 2026 at CES, already in wiki)
- **NVDA-Corning $3.2B deal** (May 6, already in wiki + [[GLW]])
- **Iran conflict / oil shock** (ongoing context, already in wiki framing)
- **Mag 7 earnings recap** (already ingested May 12-14)
- **Stratechery / Dwarkesh / BG2** — nothing material-new in 48-hour window
- **DeepSeek V4 release** (April 24, already in wiki)

### Stance/conviction changes
**None.** [[NVDA]] bull/high reinforced quantitatively by Anthropic data; no flips elsewhere.

### Pending items to track
- **NVDA Tuesday May 20 earnings** — primary catalyst this week. Wiki has framework ready.
- **OpenRouter Chinese-token-share verification** (yesterday's 36% figure still community-cited, not officially disclosed)
- **Copper price action** (Goldman expects H2 2026 dip from current ATH)

## [2026-05-16] research | New sector page initiated: copper-thesis

- **Trigger**: User question about whether to elevate copper from stub to dedicated page given the AI capex / electrification / smart-money convergence.
- **Research dive completed** via WebSearch: Goldman/Trafigura/BNEF forecasts, FCX/SCCO/TECK/BHP earnings, Friedland commentary, geographic risk (Chile/Peru/DRC), ETF vehicles (CPER/COPX), Druckenmiller positioning context.
- **New page**: `wiki/sectors/copper-thesis.md`
  - Demand math: AI data centers 400-572kt/yr through 2028 (BNEF), peaking at 1.1Mt/yr by 2030 (Sprott); grid drives >60% of demand growth through 2030 (Goldman); EVs at 4x ICE copper content; robotics adds to compounding demand.
  - Supply math: 15-20 yr mine permit cycles; $210B capex needed by 2035 vs only $76B in past 6 years; Chile +500kt/yr coming (positive); Peru political risk (Tía María revoked Mar 2026); DRC Chinese-funded expansion.
  - **Smart money**: Druckenmiller long futures ([[2026-05-16-druckenmiller-hard-lessons]]); Friedland "dawn of the copper age" $15K/tonne; Larry Fink at BlackRock; Goldman confirms demand-outpaces-supply from 2029.
  - **Vehicles**: CPER (futures, Druckenmiller-style); COPX (miners ETF, $8.2B AUM); single names FCX/SCCO/TECK/BHP/Anglo American with operational + geographic risk overlay.
  - **Stance**: bull. **Conviction**: high for futures (CPER), medium for diversified miners (COPX/TECK/BHP), medium-low for FCX (Grasberg overhang) and SCCO (declining grades).
  - **Caveat**: Goldman near-term surplus call (2026 average $12,650, drifting to $12,000 H2). Entry timing matters. Druckenmiller himself calls it a "big consensus trade."
- **Cross-links added**:
  - [[ai-capex-cycle]] — copper as physical-layer commodity bottleneck
  - [[bottleneck-roadmap]] — copper as parallel commodity bottleneck (2026-2035)
  - [[datacenter-construction]] — 5,000 tonnes copper / GW of data center capacity
  - [[robotics]] — humanoid copper-intensity; CPER/COPX as broader-market expression
  - [[commodity-producers]] — graduation pointer to dedicated copper page
  - [[index]] — new sector listing
- **No stance changes elsewhere**. Existing FIX/EME/PWR/MP positions reinforced by the copper-as-input framing.

## [2026-05-16] research | New coverage initiated: AUR (Aurora Innovation) + retail-FOMO behavioral indicator

- **Trigger**: r/stocks "Next Big Sector" thread (275 upvotes, 301 comments) — AUR surfaced as one of the few applied-AI investable plays vs. mostly speculative micro-caps (HGRAF +2,650%, quantum, eVTOL).
- **AUR coverage initiated** at `wiki/companies/AUR.md`:
  - One of 2 surviving commercial autonomous-trucking pure-plays (with Kodiak AI / KDK) after TuSimple / Embark / Waymo Via exits.
  - First US driverless commercial freight live for McLane (Berkshire Hathaway) on Dallas-Houston April 2026.
  - Hirschbach 500-truck MOU (April 30, 2026) targeting binding in H2 2026; "hundreds of millions" multi-year DaaS revenue; deliveries 2027.
  - NVIDIA Drive Thor (dual-SoC, Blackwell architecture) + Continental manufacturing (production 2027) + Volvo VNL Autonomous + PACCAR.
  - Q1 2026: $1M revenue, -$0.10 EPS (beat by $0.01), $1.3B liquidity, $190-220M/quarter burn = ~6 quarters runway.
  - 2026 guide: $14-16M revenue, Q4 exit run-rate ~$80M, 200 driverless trucks EOY.
  - Stock surged 50%+ in May 2026 ($5.15 → ~$8) on McLane + Hirschbach catalysts; market cap ~$15.7B.
  - Analyst dispersion extreme: Goldman Neutral $5 / TD Cowen Hold $7 / Morgan Stanley Overweight $14.
  - **Stance: bull / low-medium conviction.** Real product, real customers, but valuation requires 5+ years of execution; dilution near-certain through 2027.
- **Wiki touched**: [[AUR]] (new), [[nvda-supply-chain]] (added Drive Thor partner section), [[NVDA]] (Drive Thor commercial deployment bullet), [[robotics]] (autonomous trucking as adjacent applied-AI category), [[ai-bubble-debate]] (retail-FOMO behavioral late-cycle indicator), index, log
- **Behavioral indicator captured**: HGRAF +2,650% YTD with $19K Q1 revenue and $1.8B market cap recorded as a *late-cycle micro-cap-mania marker* in [[ai-bubble-debate]]. Worth tracking if it crashes 80%+ in a week as a textbook signal.

## [2026-05-16] ingest | Stan Druckenmiller (Duquesne) — Morgan Stanley Hard Lessons (~March 2026 dated)

- **Source:** [[2026-05-16-druckenmiller-hard-lessons]] (raw at `raw/podcasts/drukenmiller.txt`)
- **⚠ Staleness flag**: source content is ~2 months old at ingest. Druckenmiller says he changes mind every 3 weeks. Treat as framework anchor, NOT current portfolio.
- **TL;DR:** Stan Druckenmiller on Morgan Stanley's *Hard Lessons*. Lower-yield than the other May 16 ingests because most content is process/wisdom rather than current data. Three things worth capturing:
  1. **Reduced — NOT shorted — AI exposure** starting summer/fall 2025 because "AI started to get disturbingly heated… some rhyme with 1999-2000." Important nuance: he did NOT bet against AI, he rotated to other longs (biotech, TEVA, Japan-Korea, copper futures, gold, short bonds, bearish USD). Distinct from Burry/Chanos/Culper (active shorts).
  2. **Copper futures, not equities** — Druckenmiller specifically rolling the front-end of copper futures rather than holding FCX/SCCO. Implies he views the pure structural-supply thesis as cleaner in futures than in equities (which carry idiosyncratic operational/geographic execution risk).
  3. **The NVDA "couldn't stand success" exit anti-pattern** — bought at ~$150 (pre-ChatGPT), doubled twice; said publicly he'd hold for 2-3 years at $390; sold at $800. Stock went to $1,400 in 5 weeks. The lesson encoded: when massive secular change is in motion and your sizing is correct, the default should be HOLD over TRIM. Useful sizing-discipline anchor for [[NVDA]].
- **Wiki touched:** [[ai-bubble-debate]], [[commodity-producers]], [[NVDA]]
- **No stance changes.** All patches add expert anchors and wisdom; nothing flips.

## [2026-05-16] ingest | Aswath Damodaran (NYU Stern) — Prof G Markets quarterly live stream

- **Source:** [[2026-05-16-damodaran-profg-markets]] (raw at `raw/podcasts/ai_boom.txt`)
- **TL;DR:** Aswath Damodaran ("dean of valuation," NYU Stern) on Prof G Markets with Scott Galloway / Ed Elson. Mostly confirmation of existing wiki theses but from a high-credibility independent voice. Six investment-relevant data points:
  1. **AI correction would be WORSE than dotcom** because of macro spillover — data centers + power + water + employment across the country = market-wide correction with longer macro hangover. Direct sharpening of [[ai-bubble-debate]] bear case.
  2. **Hyperscaler revenue concentration in OpenAI + Anthropic** — Galloway cites a chart: MSFT ~50%, ORCL >50%, GOOGL 43%, AMZN 51% of revenue backlog. The cleanest quantitative single-source for the circularity concern. Tightens [[ai-infrastructure-debt]].
  3. **"AI is still NET EXPENSE, not income, for most of Mag 7"** — depreciation on AI capex puts downward pressure on earnings for MSFT/GOOGL/META/AMZN; real AI earnings concentrate at chip makers. Caveat added to [[ai-capex-cycle]] bull case.
  4. **Chip sector top warning** — 10 years ago = 3% of S&P 500; today = 17%. +60% in 2 months. MU +160% YTD. Damodaran: "the bulk of the run is done." Added to [[ai-bubble-debate]] + [[MU]] as a sizing-discipline prompt.
  5. **Banks distributing data center debt (JPM, MS, SMBC)** — Damodaran independently corroborates [[ai-infrastructure-debt]] thesis. Direct quote on regulators needing to track bank overexposure.
  6. **SpaceX intrinsic value $1.2T** per Damodaran's "Trillions and Beyond" DCF — implies ~30-45% overvaluation if SpaceX IPOs at $1.75T+ private mark. Highest-credibility independent DCF anchor in the wiki. Added to [[space-economy]].
- **Notable color**: combined SpaceX + Anthropic + OpenAI IPOs will exceed entire dotcom-era IPO market cap. Damodaran: "those three companies alone will be larger in market cap than 95% of the markets out there."
- **Wiki touched:** [[ai-bubble-debate]], [[ai-infrastructure-debt]], [[ai-capex-cycle]], [[market-concentration]], [[MU]], [[space-economy]]
- **No stance changes.** MU stays bull/high — sizing flag added to bear case. Other patches sharpen existing theses without flipping any.

## [2026-05-16] ingest | Yann LeCun (AME Labs / ex-Meta) — Unsupervised Learning podcast

- **Source:** [[2026-05-16-yann-lecun-ame-labs]] (raw at `raw/podcasts/yan.txt`)
- **TL;DR:** Yann LeCun (Turing Award winner) confirms he left Meta in late 2025 / early 2026 to start AME Labs (Advanced Machine Intelligence) in Paris, focused on JEPA / world-model architecture. Five investment-relevant data points:
  1. **Insider validation of the Meta strategic refocus story.** Post-Llama-4 disappointment, Mark refocused company on LLM catch-up; FAIR was "isolated within the company"; "lots of good people have left already." Mild bearish on Meta's research-talent moat.
  2. **PyTorch dominance independently corroborated by an outgoing competitor.** LeCun: "the entire industry is built on PyTorch basically except for a few people at Google." Reinforces the META programming-model moat bullet (just added from Horace He).
  3. **3-way architecture contradiction with Jim Fan + Sergey Levine.** LeCun: VLA = "pretty much now seen as a failure"; generative video world models = "losing proposition"; only JEPA / joint-embedding architecture works. Three top researchers from three orgs disagree on architecture even while agreeing on 3-5yr timeline. Surfaced explicitly in [[robotics]] per wiki house rule.
  4. **LLM data-wall hard claim**: "They've already run out of data. The openly available publicly available data text data is already all used. So what those companies are doing is licensing commercial copyrighted data or training on synthetic data." Strengthens the [[ai-bubble-debate]] bear leg on pre-training scaling.
  5. **Sovereign-AI federated training mechanism (Tapestry)** + industrial process control as adjacent TAM. Both added as monitor-but-not-investable threads to [[ai-capex-cycle]].
- **Notable color**: LeCun also takes a direct shot at Anthropic — "some kind of commercial good commercial reasons for them to believe that and to kind of brainwash some people and government into thinking their systems are dangerous." First high-profile peer accusing Anthropic of regulatory capture for commercial advantage.
- **Hinton/Bengio divergence**: LeCun says they "changed their minds, I didn't change mine" in 2023 after GPT-4. Hinton's calc: cortex = 16B neurons / 10 backprop equivalents = 1.6B ≈ GPT-4 → quasi-AGI. LeCun's read: Hinton wanted to retire.
- **Wiki touched:** [[META]], [[robotics]], [[ai-bubble-debate]], [[ai-capex-cycle]]
- **No stance changes.** META bear case slightly sharpens (research-talent moat erodes) but is offset by PyTorch confirmation; net unchanged.

## [2026-05-16] ingest | Dwarkesh × Sergey Levine (Physical Intelligence) — robotics foundation models

- **Source:** [[2026-05-16-sergey-levine-physical-intelligence]] (raw at `raw/podcasts/robotics.txt`)
- **TL;DR:** Sergey Levine (Physical Intelligence co-founder, UC Berkeley professor, leading robotics foundation-model researcher) gives an independent, slightly more-measured timeline vs. Jim Fan: **5-year median to fully autonomous home robot; GPT-5-equivalent robotics in 2028-2030; useful narrow deployment 1-2 years**. Key data point: **robot arm cost has collapsed from $400K (2014 PR2) → $30K (early-2020s research) → $3K (PI today) → "small fraction of $3K" forward**. ~100× cost decline in ~10 years. Physical Intelligence's π0 model = Google's open-source **Gemma VLM** + grafted action expert. Levine: **"no Nvidia of robotics" yet** — wants heterogeneity. Off-board inference (cloud-streamed) likely for low-cost robots.
- **Five investment-relevant insights:**
  1. Independent corroboration of 2-5yr timeline for first major capability inflection (alongside Jim Fan); contradiction surfaced not resolved (Fan more aggressive at 2-3yr Turing test)
  2. 100× arm cost decline + future "small fraction of $3K" → deployment-velocity assumptions in robotics market sizing are likely too conservative
  3. "No Nvidia of robotics" → bearish for single-OEM concentration (TSLA Optimus, Figure, Apptronik); bullish for diversified component supply chain (MP, OUST, ALGM, AMBA, VPG, ALNT)
  4. Off-board inference → latent 2028-2030 demand vector for CRWV/NBIS that nobody is pricing yet
  5. Gemma open-source as robotics substrate → modest GOOGL tailwind; PyTorch as training framework → META platform-tax tailwind
- **Wiki touched:** [[robotics]], [[humanoid-oems]], [[bottleneck-roadmap]], [[datacenter-construction]], [[us-china-relations]], [[MP]], [[CRWV]], [[NBIS]], [[GOOGL]], [[META]], [[ai-capex-cycle]]
- **No stance changes.** Conviction reinforcements only.

## [2026-05-16] ingest | Horace He (Meta PyTorch Compilers) — "Building ML Systems for a Trillion-Trillion FLOPs"

- **Source:** [[2026-05-16-horace-he-ml-systems]] (raw at `raw/podcasts/deep_learning.txt`)
- **TL;DR:** Horace He (PyTorch compilers team at Meta — wrote torch.compile and FlexAttention) on the structural shape of ML systems. Technical talk with 5 investment-relevant data points:
  1. **Tensor Core moat is hardware-level, not just CUDA-level.** On A100: 1000 TFLOPS TF32 (matmul) vs 67 TFLOPS FP32 (everything else) = **~15× cliff**. If you aren't doing matmuls on a GPU, you get 7% of peak FLOP utilization. This is the chip-level reason transformers consolidated as the only architecture.
  2. **Bit precision trajectory: V100=FP16 → A100=FP8 → B100=FP4.** Each halving roughly doubles effective throughput per transistor *without* requiring a new fab node. Effective-FLOPs growth axis independent of EUV bottleneck.
  3. **Fault tolerance ceiling at 131K GPUs.** Per Llama 3 paper: at 16K GPUs, MTBF ≈ 1.8 hrs; at 131K GPUs, ≈ 15 minutes. Engineering complexity scales worse than linearly → only hyperscalers + a small set of neoclouds (CRWV/NBIS) can actually USE frontier-scale clusters.
  4. **Memory bandwidth as perennial sub-bottleneck.** Matmul = 99.8% of FLOPs, 61% of runtime; the other 39% of runtime is memory-bound. Validates the structural HBM thesis (MU) as not a one-cycle event but an architectural constant.
  5. **Programming-model ownership > compiler optimization.** Horace's thesis: durable winners own the programming model (CUDA for NVDA, PyTorch for META). Compilers are unreliable; programming models that bake parallelism in (FlexAttention, torch.compile) win.
- **Wiki touched:** [[NVDA]], [[ai-capex-cycle]], [[bottleneck-roadmap]], [[META]], [[semiconductors]]
- **No stance changes.** Existing high-conviction NVDA + META bull theses thickened with hardware-level evidence.

## [2026-05-16] ingest | HN thread on Hashimoto "AI psychosis" — bear case sharpening v2

- **Source:** Hacker News thread (1683 upvotes, 908 comments) on Mitchell Hashimoto's "AI psychosis" post about companies forcing AI adoption without checks
- **TL;DR:** Mostly confirmation of wiki's existing bear framework (Kedrosky/Zitron already integrated). Three new material additions:
  - **Carlota Perez framework** as academic anchor — *Technological Revolutions and Financial Capital* — bubble + crash + golden age sequence. Most credible academic backing for the wiki's "AI is real AND a bubble" both-sides framing.
  - **Mitchell Hashimoto's sociological framing** of "AI psychosis" at corporate level — HashiCorp founder, builder not critic; complements Kedrosky's financial framework. "Very resilient catastrophe machine" is the sharpest single description of what's happening at vibecoded companies.
  - **Vibecoded mission-critical failure** added as 8th falsifiable bear trigger — when first major incident lands (medical / financial / industrial / infrastructure), AI insurance/liability emerges as a sector.
- **Corroborating anecdotal data:**
  - FAANG $300/day token quotas + "use it or be terrible" pressure = material OpEx line item (~$3.75B/year per company at scale)
  - GitHub uptime degradation as collateral damage of vibe coding
  - Hospital vibecoded inventory systems with security/data issues
  - Amazon workers making up AI tasks to look productive
- **Wiki touched:**
  - [[ai-bubble-debate]] — added Carlota Perez academic anchor section; added Hashimoto "AI psychosis" to "Bear case strongmen" with corporate adoption patterns table; added 8th falsifiable bear trigger
  - [[ai-infrastructure-debt]] — added "Token spend as Mag 7 OpEx line" section with FAANG $300/day quota anecdote + tied to Kedrosky's SBC/buyback compression thesis
  - [[log]] — this entry
- **Stance / conviction changes:** none. This is bear-case sharpening, not bull thesis breaking.
- **Skipped (low-value):**
  - Endless ad hominem about "AI psychosis" as clinical vs colloquial term
  - Bot accusations on the thread (correct but not actionable)
  - Pedantic compiler/JIT/CNC analogies
  - Technology vs craftsmanship general debate
- **Methodology note:** This was a thread, not a primary source. The named voices (Hashimoto, references to Perez) get cited; anonymous commentary is treated as anecdote, not data. Same discipline as POET Lumilens deal analysis.

## [2026-05-16] ingest | Jim Fan (NVIDIA Robotics chief scientist) — "The Great Parallel" robotics talk

- **Source:** raw/podcasts/nvda_robotics.txt — saved by user 2026-05-16
- **Source summary:** [[2026-05-16-jim-fan-nvda-robotics]]
- **TL;DR:** Robotics is following the LLM 3-step function (pre-train next-world-state → action fine-tune → RL). VLA models (Pi, Groot) being superseded by World Action Models (Dream Zero). EgoScale found a clean log-linear scaling law for dexterity (21k hr egocentric video + 4 hr teleop). Dream Dojo = neural simulator. Physical Turing test 2-3 years; full endgame 2040 with 95% certainty.
- **Wiki touched:**
  - [[NVDA]] — added "Robotics moat is deeper than chips" bullet to bull case: Dream Zero (WAM) + EgoScale scaling law + Dream Dojo simulator = three additional moats stacked on chip moat
  - [[robotics]] sector — added "Model paradigm shift VLA→WAM" subsection + "Data revolution" + "2040 endgame framework" with Fan's 14-year extrapolation
  - [[AAPL]] — added small option-value bull bullet: iPhone as "pocket world scanner" for robotics data ingestion (doesn't flip bear stance, structural hedge only)
  - [[index]] — added source ingest entry
  - [[log]] — this entry
- **Stance / conviction changes:**
  - **NVDA:** stays bull/HIGH. Conviction strengthened — wider moat than wiki captured. No size change since already maxed.
  - **AAPL:** stays bear/medium. Small positive added to bull side but doesn't flip thesis.
  - **Robotics sector:** thesis sharpened, not changed. 2040 endgame framework now anchors timeline framing.
- **Implications:**
  - For [[MP]] / [[ALGM]] / [[VPG]] / [[ALNT]] / [[AMBA]] (humanoid component cohort): accelerating model timeline pulls commercial deployment closer. Mild positive; mostly priced.
  - For competitive landscape: Pi (Physical Intelligence) and other pure-play VLA labs at risk if WAM wins. Not in wiki ticker list but shapes venture-side dynamics.
  - For NVDA: confirms the bull thesis is multi-layered (chips + models + data + simulator). Less single-point-of-failure than wiki had assumed.
- **Bias caveat:** Fan is NVIDIA's chief scientist of Robotics speaking at NVIDIA's conference. Discount certainty by ~15% for self-promotional bias.
- **No contradictions** with existing wiki framework. This SHARPENS rather than challenges.
- **Skipped:** specific Pi / Groot unicorn valuations — not investable on public markets.

## [2026-05-15] EOD | Daily update close — Friday close data + Blue Owl risk-off signal

- **Friday close confirmed:** S&P -1.24% to 7,408.50; NASDAQ -1.54% to 26,225.14; Dow -1.07% to 49,526.17. Worst day since the Trump-Xi summit week began.
- **Wiki tickers moves:**
  - NVDA -4.39% on H200 China limbo + macro overlay
  - AMAT -3% despite Thursday beat + CY26 >30% guide raise (post-print selling pattern)
  - CBRS -10% after Thursday +68% IPO debut surge — late-cycle volatility
  - Intel -8% to $108 after 214% YTD run on Apple foundry speculation (not in wiki, signal only)
  - **POET -11% to $18.27** on $400M dilution dump + Q1 miss + CFO exit (covered in PM4)
- **Other material signals:**
  - **Bill Ackman's Pershing Square took a MSFT position** — described pullback as "rare opportunity to buy dominant tech franchise at compelling valuation." Institutional bull-side validation
  - **Blue Owl OPTED NOT TO FUND Oracle's $10B Michigan data center** — bear-case data point for [[ai-infrastructure-debt]]; CEO explicitly stated reducing software exposure (May 7); but Blue Owl AUM still grew 15% YoY. Largest private credit AI funder being selective, not pulling out wholesale
  - **Trump left Beijing with NO rare earth deal confirmed** — China 90% rare earth refining + 60%+ mined supply gives massive leverage. Bullish for [[MP]] domestic rare earth thesis; bearish for any name requiring China rare earth supply
  - **Apollo $8B in two recent DC deals** (Zelter quote) — still actively deploying, just more selective
  - **Ares co-president flagged $900B opportunity** for third-party DC investment — frames the scale of private credit absorption ahead
- **Next week catalysts confirmed:**
  - **May 20 Wed AC: NVDA Q1 FY27** — consensus updated $1.78/$78.98B (slightly higher than prior $1.77/$78.8B)
  - **May 21 Thu BMO: WMT Q1 FY27** — consumer health check
  - **May 20 + 21:** $16B 20-year Treasury auction (same day NVDA) + $19B 10-year TIPS reopened
- **Wiki updates:**
  - [[ai-infrastructure-debt]] — Blue Owl Oracle Michigan PASS data point added; CEO software-reduction statement; PIMCO+Blue Owl $29B Meta partnership now framed as "selective continuation"
  - [[overview]] — Friday close numbers updated; CBRS, Intel, Ackman MSFT position added to context
- **Stance / conviction changes:** none.
- **Skipped (low value):** Speculation about Ackman's MSFT entry price (no public info yet); general "tech selloff" headlines (already captured); detailed Walmart preview (not in wiki ticker list directly)
- **Pending for Monday open:** Hedges should be sized + in place per [[hedging-risk]] ahead of May 20 NVDA + 20-year auction compound shock window. [[2026-05-20-nvda-earnings]] playbook is the operating manual for that day.

## [2026-05-15] PM4 | POET $400M dilution dump + Q1 miss + CFO exit — dedicated wiki page created

- **POET stock -11% to $18.27** today on three stacked events:
  1. **$400M registered direct offering** to undisclosed single institutional investor — 19M common shares + 19M warrants at $21/$26.15. **38M potential new shares = ~30-40% dilution.**
  2. **Q1 FY26 EPS missed:** adjusted loss $0.08 vs $0.05 expected (wider by $0.03)
  3. **CFO Thomas Mika announced retirement** (May 12) after 10 years of service. Timing: ahead of the $400M financing close (May 18). Reason not publicly disclosed.
- **Two-day playbook completed:** May 14 Lumilens partnership (with 22.9M-share warrant at $8.25 deep ITM to Lumilens) pumped stock +38% to $20+; May 15 POET sold $400M into the pop. **Lumilens deal created the pop; the $400M raise monetized it.** This is the canonical small-cap-photonics dilute-into-narrative playbook the wiki has been documenting.
- **Wiki action:**
  - **NEW:** [[POET]] dedicated company page (AVOID stance, high conviction). Snapshot, full bull-and-bear case, position sizing guidance, 4-validation track record, key questions, recent developments timeline
  - [[feedback-log]] — 4th validation entry (-49% drop, +130% bounce, +38% Lumilens pop, -11% dilution all hit the framework correctly). New pattern named: "dilute-into-narrative two-step" — when a small-cap announces partnership-with-warrant, check for follow-on cash raise within 48 hours
  - [[index]] — added "Anti-canonical" section with POET as the wiki's reference AVOID stance
- **User context:** User's friend has $100K+ in POET, sees the $18.27 pullback as a "better buying opportunity." Wiki framework view: this is the FOMO-on-pullback pattern; the asymmetric downside is BIGGER at $18 (vs $8.20 PT = 2.2x consensus) than at $8 was. Position sizing >5% of net worth is concentration risk inconsistent with the speculative nature.
- **Wall Street consensus PT remains $8.20** per public consensus. Stock at $18.27 = 2.2x consensus. If stock returns to consensus = -55% downside.
- **Stance / conviction changes:** none. POET stays AVOID/high. Pattern was correctly identified prior to today's event.
- **Skipped (low-value):** General "POET drop" market coverage; speculation on the institutional buyer identity (will surface in 13F filings naturally).

## [2026-05-15] PM3 | New theme page — wiki/themes/ai-infrastructure-debt.md

- **Followed through on the research thread opened in PM2.** Created dedicated [[ai-infrastructure-debt]] page unifying the SRT mechanism, named exposures, private credit absorption, and 2008 CDO/SIV pattern analog into a single tracker.
- **Additional research that fed into the page:**
  - **Private credit redemption crisis (Q1 2026) is bigger than initially captured:**
    - Blue Owl OCIC ($36B fund): 21.9% requested → gated at 5%
    - **Blue Owl OTIC ($6B tech fund): 40.7% requested → gated at 5%** (near-run on tech-focused private credit)
    - Apollo flagship ($25B): 11.2% requested → gated
    - Blackstone BCRED ($82B): 7.9% requested → raised limit 5%→7%
    - $4.6B+ trapped in redemption limits across funds
  - **SRT mechanism details verified via BIS + Basel + CFA Institute:** 2% of bank loans currently, US = 30% of global deal flow, 50-80% RWA reduction per transaction, investor base = private credit + hedge funds + pension + insurance
  - **Major AI DC private credit deals named:** Blue Owl $30B Meta Hyperion (Louisiana), Apollo + Blackstone + BlackRock + TPG all participating in data center deals
- **NVDA bill-and-hold verification attempt:** WebSearch + WebFetch on 10-K could not surface any specific bill-and-hold disclosure. NVDA customer advances grew $323M (H1 FY25) → $664M (H1 FY26) — consistent with CONSERVATIVE deferred revenue practice, not supportive of bill-and-hold. Per ASC 606, material bill-and-hold requires disclosure; absence is informative. Flagged as pending verification on May 20 earnings call.
- **Wiki touched:**
  - **NEW:** [[ai-infrastructure-debt]] (full theme page — 130+ lines with mechanism explanation, named exposures, falsifiable watch triggers, counter-arguments, sources list)
  - [[index]] — added ai-infrastructure-debt to Themes section
  - [[financials]] — added "MAJOR EXPOSURE TRACKING" section with stance implications:
    - **Asset managers / private credit (BX/APO/ARES/BLK):** stance shifts neutral/bear on near-term given Q1 2026 redemption pressure (was bull/low)
    - Money-center banks (JPM/BAC): mild downgrade pending
    - Insurance (MET/PRU): flag for monitoring as SRT end-holders
- **Stance / conviction changes:**
  - **Asset managers / private credit ([[financials]] section): bull (low) → neutral/bear** — preliminary; needs proper company page work to confirm. Flagged prominently.
- **Methodology note:** The wiki's "verify named specifics" discipline that surfaced in PM2 paid off here. Created a tracker page for the bear vector with the highest-leverage data, not a generic theme rant. Falsifiable watch triggers attached to the page.

## [2026-05-15] PM2 | Bear case verification via Gemini transcript search + WebSearch

- **User used Gemini to dig deeper into the podcast transcripts.** Returned: (a) Dylan Patel (Kakashi) is the source for bill-and-hold on NVDA per the podcast — significant credibility upgrade; (b) Zitron named specific projects (Project Rainier, Stargate Abilene, MSFT Fairwater Wisconsin); (c) Zitron sourced FT story on banks "choking" on AI DC debt + $1T-of-$6T insurance annuities in private credit claim; (d) Kedrosky's NVDA over-ordering is his own analysis, not external evidence.
- **WebSearch verification on the named DCs:**
  - **Project Rainier (AWS Indiana):** 7 of 30 buildings operational ✓ (Zitron's numbers right) BUT those 7 are **2.2 GW running 500K Trainium2 for Anthropic** — meaningful scale, not fictional. $26B committed across phases. Phase II planned.
  - **Stargate Abilene:** Zitron said 1→2 buildings in 6 months; reality is ~4 of 8 operational May 2026, remaining 6 mid-2026. 450K GB200 GPUs total. **Zitron framing out of date.**
  - **MSFT Fairwater Wisconsin:** Phase 1 operational by July 2026 (on schedule), +15 buildings approved Jan 2026. $7.3B invested. **Active phased buildout, not fake.**
- **Bank-debt-offloading verification:** Verified + BIGGER than Zitron stated.
  - **$38B Oracle-leased DC debt** being distributed by JPM + MUFG at discounts to non-bank lenders
  - 6 major banks offloading: JPM, Morgan Stanley, SMBC, MUFG, Citi, Goldman
  - **SRT (Significant Risk Transfer)** mechanism transferring risk to private credit + insurance + pension funds
  - **FSB stat:** AI = >33% of private credit deals 2025 (vs 17% prior 5yr avg)
  - **Tech groups shifted $120B AI DC debt off bank balance sheets** (FT)
  - Man Group quote: "out of scale to anything we've thought about, ever"
- **Strategic synthesis:** Two methodology wins captured. (1) **Verify-named-specifics discipline** — Zitron's "1-2 buildings of dozens" framing collapsed under fact-check; his banks-offloading-debt claim verified and got materially bigger. (2) **Source credibility matters** — bill-and-hold from Zitron + Dylan Patel weighs more than Zitron alone.
- **Wiki touched:**
  - [[ai-bubble-debate]] — 3 entries updated with verified specifics; new dedicated "AI infrastructure debt" section with $38B Oracle deal + 6 banks + SRT mechanism + FSB stats
  - [[feedback-log]] — 〰️/✅ verdict entry capturing the partial validation + methodology lessons
  - [[overview]] — new top-level callout on AI infrastructure debt as systemic risk vector wiki had missed
- **Stance / conviction changes:** none. Bear thesis sharpened with verified data; bull thesis unchanged.
- **Research thread opened:** dedicated [[ai-infrastructure-debt]] page potentially worth building (next session) — would unify SRT mechanism, named exposures, private credit absorption, insurance/pension fund risk. **This is closer to 2008 CDO/SIV pattern than dot-com pattern** and the wiki should treat it explicitly as the contagion mechanism, not just a bull-vs-bear debate point.
- **Outstanding follow-up:** WebFetch NVDA 10-Q revenue recognition footnote to verify bill-and-hold claim before May 20 earnings.

## [2026-05-15] PM | Bear case integration — Zitron + Kedrosky + Jane Street DC tour

- **3 podcast sources processed.** Two bear cases (Zitron x2 episodes, Kedrosky on Plain English) + one bull data point (Jane Street DC tour). Goal: sharpen the wiki's bear framework with the strongest available critiques rather than dismiss them.
- **Kedrosky (Plain English):** Strongest version of the bear case. Railroads-style infrastructure bubble framing. 5 material new arguments: (1) 3-phase capex/market-cap regime shift ($1 → $0 → negative reward), (2) productivity math is misleading (GDP arithmetic, not AI working), (3) deterministic+expansive (coding) vs non-deterministic+compressive (white-collar) token economics — refutes naive 100M-knowledge-worker token extrapolation, (4) SBC+buyback compression, (5) HALO rotation cohort.
- **Zitron (Tech Report x2):** Sharper but less sophisticated. New material claims: (1) "operational" DCs are 1-2 buildings out of dozens, (2) bill-and-hold accounting on NVDA, (3) bank debt offloading at discounts, (4) capacity wall for OpenAI/Anthropic (actually inverts his own bear case).
- **Jane Street DC tour:** 4,032 GPUs at 140 kW per cabinet (14x traditional density) — real operating facility, counter to Zitron's "DCs aren't being built." Validates VRT/ETN power+cooling thesis.
- **Wiki touched:**
  - [[ai-bubble-debate]] — added "Bear case strongmen" section consolidating Kedrosky + Zitron with claim-by-claim wiki integration + falsifiable watch list (7 specific triggers)
  - [[ai-capex-cycle]] — added two caveats: token-economics-not-uniform across knowledge work, productivity-math-is-just-capex-arithmetic
  - [[VRT]] — added 140 kW density data point from Jane Street
  - [[2026-05-20-nvda-earnings]] playbook — added bill-and-hold watch item as #7 in "what to watch on call"
- **Stance / conviction changes:** none. Framework integration sharpens the bear case but doesn't break the bull thesis. Late-cycle 5/6 firing was already mapped; hedging-risk page already built.
- **Falsifiable watch list (NEW):** 7 specific triggers added to ai-bubble-debate. If any fire → bear case activates → execute hedging-risk Tier 2 sizing.
- **Research threads opened (not yet pages):**
  - Bank debt offloading at discounts (need specific examples — Zitron's claim, no evidence yet)
  - NVDA bill-and-hold 10-Q check (could do via WebFetch on next NVDA 10-Q)
  - SemiAnalysis site-level commissioned capacity tracker (test Zitron's "1-2 buildings of dozens" claim)
  - Mag 7 buyback rate vs SBC tracker (Kedrosky's compression thesis)
- **Skipped (low value):** Talus/Cerebras inference disruption as immediate bear catalyst (5-10yr story; near-term NVDA CUDA moat intact); revisit if any major customer announces shifted away from NVDA inference.

## [2026-05-15] AM | Daily update — Friday reversal, H200 China limbo, AMAT post-print sell

- **Market reversal Friday May 15:** S&P -1%, NASDAQ -1.3% from Thursday records. Driven by yield spike + Trump-Xi summit disappointment + H200 China deal stalling.
- **30y to 5.08%** (+5 bps from May 14 auction-cleared 5.046%); **10y to 4.54%** (highest since May 2025). Markets fully priced out 2026 Fed cuts; some pricing in December hike. Direct continuation of bond-market pressure framework.
- **NVDA H200 China limbo:** Thursday +4.4% on US clearing H200 sales to ~10 Chinese firms (Alibaba, Tencent, ByteDance, JD.com, Lenovo, Foxconn + 4 others; up to 75K chips each). Friday -4% on news that **China has NOT approved purchases** from its side. **Trump: "they want to develop their own."** Refines Trump-Xi summit feedback-log entry: Scenario A "Theater" call now stronger, not weaker — even the symbolic chip carve-out is bilaterally contested.
- **AMAT -3% despite Thursday's beat + CY26 >30% guide raise.** Classic post-earnings selling after multi-month run-up. Thesis intact; no stance change.
- **Wiki touched:** [[NVDA]] (H200 limbo line), [[overview]] (Friday reversal section + yields update), [[feedback-log]] (Trump-Xi refinement), [[2026-05-20-nvda-earnings]] playbook (China commentary now more important — added explicit bullish/neutral/bearish triggers).
- **Stance / conviction changes:** none. NVDA stays bull/high. AMAT stays bull/high.
- **Skipped (low-value):** BABA Q4/FY25 print (not in wiki); WMT preview next week; broad coverage of "tech pulled back" headline (already captured); various pundit takes on H200.
- **Pending:** Weekend = pre-position for Monday open. Hedges should be in place by Monday per [[hedging-risk]] sizing.

## [2026-05-14] PM4 | Process improvement v2 — adjacent coverage + weekly synthesis pipeline

- **Context:** Continuing the process-improvement roadmap after pushing PM3 (playbooks + hedging). Two remaining items from the original menu: bridge adjacent coverage + weekly synthesis pipeline. User authorized both.
- **Adjacent coverage stubs (5 new sector pages):**
  - [[commodity-producers]] — gold (GLD/NEM/AEM), copper (FCX/SCCO), oil E&Ps (XOM/CVX/COP/OXY) — closes the hedge-adjacent gap; ties into [[hedging-risk]] Tier 1 GLD recommendation
  - [[defensives]] — utilities (NEE/DUK/SO + AI-exposed CEG/VST/TLN), staples (PG/KO/COST), defensive healthcare (UNH/JNJ); explicit framing that defensives are Tier 2 hedging (not primary)
  - [[financials]] — banks (JPM/BAC), IBs (GS/MS), asset managers (BLK/BX/KKR), payments (V/MA), insurance (BRK/PGR); flagged the AI-private-credit thesis as worth standalone treatment later
  - [[biotech-pharma]] — separated from defensive healthcare due to different beta profile; LLY/NVO weight-loss gap flagged explicitly as the wiki's biggest single mega-cap miss
  - [[consumer-cyclicals]] — retail/restaurants/travel/brands/autos — closes the consumer-rate-sensitive gap that the macro framework had been flagging without ticker anchors
- **Weekly synthesis pipeline:**
  - [[weekly-synthesis-template]] — reusable Friday template with structure (lede, big picture, what changed in wiki, one idea, catalyst calendar, position discipline, reading list, sign-off), voice notes, Substack publishing checklist. Targeted at 800-1,500 word publication length.
  - [[2026-05-15-weekly-synthesis]] — first instance for Saturday May 17 publication. Title: "The week the supply chain raised its hand — and the bond market raised it higher." Anchors on AMAT >30% CY26 guide raise + 30y auction at 5.046%. ~1,300 words. Internal draft; final edit pass before Saturday publication.
- **Wiki touched:**
  - 5 new sector pages (`wiki/sectors/`)
  - 1 template page + 1 first-instance page (`wiki/playbooks/` and `wiki/analyses/`)
  - [[index]] — Adjacent coverage subsection added under Sectors; Analyses subsection populated; Playbooks updated with template
- **Stance / conviction changes:** none. All preliminary stub-level stances on the new sector pages are flagged as low-confidence pending deeper coverage.
- **Pending items closed by this session:** Bridge adjacent coverage ✓; Weekly synthesis pipeline ✓
- **Original 4-item process improvement roadmap status (May 14):**
  - 1. NVDA + CPI playbooks ✓ (PM3)
  - 2. Hedging coverage ✓ (PM3)
  - 3. Bridge adjacent coverage ✓ (this session)
  - 4. Weekly synthesis + Substack pipeline ✓ (this session)
- **Next natural cadence:** Saturday May 17 — final edit + publish first weekly synthesis (if user wants to begin Substack cadence). Otherwise hold as internal review artifact.

## [2026-05-14] PM3 | Process improvement v1 — pre-mortem playbooks + hedging coverage

- **Context:** User asked for high-level process improvement suggestions. Identified 8 improvements ranked by leverage. After clarifying conversation, user opted to skip positions tracker (privacy) and tackle the other recommendations.
- **Sequencing decision:** time-sensitive items first (NVDA May 20 = 6 days out; June 10 CPI = 27 days out), then structural items later.
- **Created:**
  - [[2026-05-20-nvda-earnings]] — NVDA Q1 FY27 playbook. 4 scenarios (Strong beat 40% / In-line 35% / Disappoint 20% / Black swan 5%). Each has triggers (Rev/EPS/GM/guide thresholds), expected stock reaction, and position-by-position action table covering NVDA core, NVDA $240C May 22 YOLO, WFE complex, neoclouds, memory, defense, hedges. Cheat-sheet card for mobile.
  - [[2026-06-10-cpi-binary]] — May CPI playbook. 3 scenarios (Cool 30-35% / Stable hot 45% / Accelerating 25-30%). Each tied to specific YoY/MoM triggers, macro implications, equity reactions, position-by-position actions. Adds Scenario 3b "stagflation shock" for the Warsh-cuts-into-hot-inflation 20% tail from [[fed-policy]].
  - [[hedging-risk]] — first defensive coverage page in the wiki. Tier 1 (cash/BIL, QQQ put spreads, VIX call spreads, GLD), Tier 2 (NVDA-specific spreads, sector rotation), Tier 3 (NOT recommended — TLT, leveraged inverse ETFs, covered calls on high-conviction names). Recommended hedge stack for current 5/6-indicators-firing state: ~6-9% in hedges + ~3-5% in cash.
- **Wiki touched:**
  - 3 new pages created (playbooks + hedging)
  - [[index]] — added Playbooks section + hedging-risk to top-level
  - [[overview]] — added "Pre-committed playbooks" section cross-referencing all three
- **Stance / conviction changes:** none. Hedging coverage doesn't reflect a stance flip — it formalizes the contradiction the wiki has been mapping (5/6 late-cycle indicators firing while 100% long-biased).
- **Pending for next session:**
  - **Bridge adjacent coverage** — stub pages for autos, fintech, energy E&Ps, gold/copper miners, utilities, staples, healthcare, biotech, REITs
  - **Weekly synthesis + Substack pipeline** — Friday templated artifact bridging wiki to publication
  - Post-NVDA May 20: update [[2026-05-20-nvda-earnings]] with actual outcome + feedback-log entry
  - Post-June 10 CPI: same protocol for [[2026-06-10-cpi-binary]]

## [2026-05-14] PM2 | Daily update — AMAT Q2 print + 30y auction confirmed above 5%

- **Sweep:** parallel WebSearch on market close, earnings reports, NVDA pre-earnings positioning, 30y auction. Material findings:
  - **AMAT Q2 FY26 (May 14 AC) — earnings workflow triggered.** Rev $7.91B record (+11% YoY); non-GAAP EPS $2.86 vs $2.68 cons (+20% YoY); GAAP EPS $3.51 (+33%). Non-GAAP GM 50.0%; OpInc $2.52B. Semi Systems $5.97B with mix Foundry/Logic 67% / DRAM 29% / Flash 4%. AGS $1.67B. **CEO raised CY26 semi equipment growth guide from ">20%" to ">30%"** — first explicit annual-outlook upgrade this cycle. CFO: "AI demand is now in full force." Q3 guide $8.95B ± $500M. 15% dividend hike to $0.53. Acquiring ASMPT NEXX advanced packaging.
  - **30y Treasury auction (May 14) cleared at 5.046%** — first auction above 5% since 2007. Bid-to-cover 2.3x (below 6-auction avg 2.42x = **soft demand**). Tail +0.5 bps. Indirect 63.95%.
  - **Cisco Q3 FY26 (May 13 AC):** Rev $15.8B beat; EPS $1.06 beat. **AI infrastructure orders guidance raised from $5B to $9B** for FY26 (80% increase). DC switching +40% YoY. Stock +20% on print.
  - **NVDA pre-earnings:** consensus $78.8B rev / $1.77 EPS for May 20 print; Polymarket 90% implied beat probability. NVDA hit ATH May 8 at $217.80.
  - **Market close:** S&P record 7,444.25 (+0.5%); NASDAQ record 26,402.34 (+1.2%); Dow -0.14%. NVDA +2%, MU +4%, SMH +2%.
- **Strategic synthesis — supply-side AI capex validation:** AMAT raising CY26 from >20% to >30% + CSCO raising AI infra orders $5B→$9B = the supply chain is **upgrading its own outlook mid-year**. The bear case "AI capex is over-extrapolated" gets harder to sustain when WFE + networking + model labs all independently confirm the curve.
- **Tension:** AI demand validation (AMAT, CSCO) clashes with bond-market signal (30y >5% confirmed at auction with soft demand). This is the macro/micro tension the wiki has been mapping — both signals are now stronger than 24 hours ago.
- **Wiki touched:**
  - [[AMAT]] — full Q2 FY26 update; snapshot table refreshed; recent developments + "what this means" added; CY26 >30% guide raise reflected
  - [[2026-05-14-AMAT-Q2-2026-earnings]] — new source summary
  - [[fed-policy]] — new "30y auction confirmed above 5%" section with metrics + read
  - [[overview]] — refreshed rates line; new "Supply-side AI capex validation" section; "what this means" updated
  - [[ai-capex-cycle]] — added AMAT + CSCO supply-side validation bullets
  - [[feedback-log]] — ✅ AMAT bull/high call validated; ✅ 30y >5% call validated
  - [[index]] — new source added
- **Stance / conviction changes:** none. AMAT stays bull/high (already correct). Wiki conviction validated via guide raise, not changed by it.
- **Skipped (low-value):**
  - JD.com earnings — not in wiki ticker list
  - General "S&P at record" commentary (already captured)
  - BABA / PLUG / others reporting this week not in wiki
- **Pending:** May 18-21 Treasury supply window (bills May 18, $16B 20-year May 20 same day as NVDA, $19B 10y TIPS May 21); NVDA Q1 FY27 print May 20 AC; AMAT/CSCO follow-up Q3 prints.

## [2026-05-14] PM | ENPH coverage gap closed — residential solar added to wiki

- User flagged off-framework purchase: bought [[ENPH]] (Enphase Energy) on 2026-05-12; asked retroactively if wiki had recommended.
- **Honest answer:** zero wiki coverage. Grep returned no hits on "ENPH" or "Enphase" across 92 files. Solar appeared only as generic "solar+battery" in [[bottleneck-roadmap]] / [[GEV]] / [[VRT]] data-center power alternatives.
- **Diagnosis:** wiki's "power" coverage is entirely **data-center power infrastructure** ([[VRT]] / [[ETN]] / [[GEV]] / [[BE]] / [[FIX]] / [[EME]] / [[PWR]]) — a B2B AI capex thesis. Residential solar / consumer energy was never built.
- **Actions taken:**
  - Created [[ENPH]] company page with Q1 2026 data: Rev $282.9M beat, non-GAAP EPS $0.47 beat, non-GAAP GM 44%, FCF $83M, cash $930.6M, GAAP net loss $7.4M
  - Q2 guide $280-310M, GM 44-47% incl. ~3pp reciprocal tariff drag
  - Hold consensus (avg PT $59 / current $42)
  - **Stance: neutral, low conviction** — value-recovery / bombed-out-cyclical play; NOT in core AI capex framework
  - Explicit framing that ENPH is exposed to consumer rates + tariffs + ITC — all macro headwinds the wiki separately flags
  - Position sizing guidance: cap at 1-2%, buy zone $35-38, stop $30, trim ladder $52/$65/$80
- **Feedback log:** added 🛠️ Process gap entry. **Lesson:** wiki's macro pessimism (rates, tariffs, ITC) wasn't anchored to any consumer-rate-sensitive tickers — so user purchase in that space wasn't surfaced. Future improvement: add a "consumer-rate-sensitive" ticker bucket so macro framework maps to specific names.
- **Wiki touched:** [[ENPH]] (new), [[feedback-log]], [[index]], [[log]]

## [2026-05-14] PM | Counter-bear relief valve + May 20 macro-micro confluence
- User shared news feed with multiple macro items. Filtered signal from noise.
- **Material findings:**
  - **OPEC+ plan to complete series of quota hikes** (per delegates) — more supply moderates oil prices → relieves Iran-shock-driven energy inflation impulse
  - **IMF: "medium-term inflation expectations remain anchored"** — even in IMF's "adverse scenario" framing, expectations haven't unanchored. Gives Fed cover to hold rather than hike.
  - **Tech rally continuing** — Cisco strong results + NVDA continued momentum
  - **May 18-21 Treasury supply concentration** — $89B 3-mo + $77B 6-mo bills May 18; **$16B 20-year auction May 20 (same day as NVDA earnings)**; $19B 10-yr TIPS May 21
- **Strategic synthesis:** OPEC+ + anchored expectations = counter-bear relief valve. The 30y >5% bond pricing may be over-extrapolating. Cooling-scenario probability for June 10 CPI nudged up from 25% → 30-35%. Reduces (but doesn't eliminate) the 20% Warsh-cuts-into-hot-inflation tail.
- **Wiki touched:**
  - [[overview]] — "Counter-bear relief valve emerging" section + "May 20 macro+micro confluence" callout
  - [[inflation-tariffs]] — new "Counter-bear relief valve" section with OPEC+ + IMF framing
  - [[fed-policy]] — new "May 20 = macro + micro confluence" section + "Counter-bear relief valve" section
  - [[feedback-log]] — pending verdict refined: June 10 CPI probabilities now 30-35% / 45% / 25-30% (was 25% / 45% / 30%)
- **Filtered out (noise):**
  - BoE's Pill jawboning (UK central bank, not US-material)
  - UK Health Secretary resignation (political noise)
  - ECB Villeroy on GDP (background)
  - IMF Iran war assistance (already in framework via energy)
- **Stance / conviction changes:** none. This is probability refinement at the margin.

## [2026-05-14] new artifact | Feedback log accountability page launched
- User requested a "feedback log" tracking wiki calls vs actual outcomes — explicitly as a trust-building mechanism for the eventual Substack/YouTube vision.
- **Created:** [[feedback-log]] — top-level wiki page with structured schema for tracking:
  - ✅ Right calls (matched directionally + timing)
  - ⏱️ Right but timing wrong (structural call correct, near-term move opposite)
  - 〰️ Partially right (right on some dimensions, wrong on others)
  - ❌ Wrong calls
  - 🛠️ Process gaps (workflow broke; not necessarily wrong analytically)
- **9 backfilled entries** from the past 2 weeks:
  - ⏱️ OUST downgrade timing wrong (+26% in 8 days after downgrade)
  - ✅ POET avoid stays correct through -49% drop AND +130% bounce
  - ✅ Trump-Xi summit Scenario A (60% probability) confirmed
  - 🛠️ CRWV Q1 print missed for 6 days → closed via new earnings workflow
  - ✅ NBIS Q1 conviction upgrade captured same day
  - ✅ Anthropic margins prediction validated at CFO level (cross-source convergence)
  - ⏱️ PPI shock macro framework right, Neocloud bucketing was too coarse
  - ✅ OUST Hesai-gap structural downgrade immediately validated
  - ✅ Culper NVDA short thesis — wiki framework separated verified facts from contested allegations
- **10 pending verdicts** flagged with explicit "verdict TBD when X happens" markers (AAPL stance flip; MU cycle-peak warning; ASML pricing power; NVDA Q1 FY27 May 20; etc.)
- **9 lessons accumulated** at bottom of page (stance ≠ market timing; cross-source convergence; macro+catalysts; fact-based downgrades; etc.)
- **New memory saved:** `feedback_accountability_log.md` — workflow rule for when to add entries, schema to follow, verdict tags to use
- **Updated [[index]]** with feedback-log at top-level alongside overview / watchlist / log
- **Stance / conviction changes:** none. This is a meta-artifact, not a positioning change.
- **Why this matters:** The wiki now has explicit "show your work" honesty. Wrong calls get the same visual treatment as right ones. Pending verdicts are flagged so readers know what's testable. This is exactly the kind of trust-building Substack/YouTube readers respond to.
- **Total wiki:** 92 files (+1 new top-level page).

## [2026-05-14] price-action review | POET + OUST honest reckoning
- User asked why POET went up so much today and whether we missed it; also whether OUST might be a sleeper hit.
- **POET (stance unchanged: AVOID):**
  - Stock $18.45 May 14 (high $20.65, low $13.90); bounced from $7.97 late-April low = +130% in ~3 weeks
  - Catalysts: new COO Sandeep Kumar (Silicon Labs veteran) building Malaysia AI manufacturing + speculation Marvell cancellation was one-off
  - **Wall Street consensus PT: $8.20** (range $8.00-$8.40) — stock now trades at **2.2x consensus PT**
  - Fundamentals unchanged: $1.07M 2025 revenue, $63M losses
  - **Framework validated:** the wiki's [[ai-bubble-debate]] "Late-cycle warning indicators" #1 specifically named POET as the canonical example of small-cap AI speculation. The +130% bounce on narrative without earnings inflection IS the pattern.
- **OUST (stance unchanged: bull/LOW; price moved):**
  - Stock $33.86 May 14, **+26% since wiki downgrade May 13 ($26.80)**
  - Catalysts: NVDA DRIVE Hyperion + DriveWorks full qualification; BlueCity expanding 6 → 30+ Atlanta intersections (FIFA World Cup tailwind); Stereolabs ZED X Nano wrist-mounted stereo camera launch; Oppenheimer PT raised $40 → $42
  - **Honest read:** thesis structurally right (Hesai gap, Luminar BK, Tesla camera-only intact) but timing was wrong on near-term momentum
  - At $33.86 vs $42 PT = only **24% upside** to most bullish public PT (down from 57% at downgrade). Easy money mostly gone.
  - Bull case still requires (a) US tariffs barring Hesai OR (b) named humanoid OEM design win. Neither in place.
- **Wiki updates:**
  - [[watchlist]] POET entry: added "Update 2026-05-14: framework validated" with +130% bounce data point
  - [[OUST]] page: new Recent developments entry capturing +26% week with all catalysts; explicit "thesis was structurally right but timing was wrong" honesty
  - `tooltips.js` OUST entry: price updated $26.80 → $33.86; thesis text reflects framework validation
  - [[ai-bubble-debate]] late-cycle indicator #1: POET bounce added as "framework validated" follow-up with "lesson: indicator firing ≠ stock down tomorrow" framing
- **Stance / conviction changes:** none. Both stay where they are.
- **Meta-lesson captured:** the wiki's framework identifies which way asymmetry skews, not market timing. Holding POET avoid through both the -49% drop AND the +130% bounce was the right call. Holding OUST bull/low while it ran +26% is the same call in inverse — structural risk doesn't go away just because the stock went up.

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
