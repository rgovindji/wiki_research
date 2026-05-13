/**
 * Investing Wiki — Tooltip data + interactive system
 * As of 2026-05-12. Mobile-supported (tap to open / tap to dismiss).
 *
 * Forward estimates ("Bull 2027" / "Bull 2028") are SCENARIO PROJECTIONS,
 * not analyst price targets. Methodology:
 *   bull/high:        +50% (2027) / +90% (2028)
 *   bull/high(multi): +45% / +80%
 *   bull/medium:      +30% / +50%
 *   bull/low:         +20% / +30%
 *   neutral/medium:   +10% / +20%
 *   neutral/low:      +5% / +10%
 *   bear (upside):    +5-8% / +10-15%
 * Multipliers represent "if the wiki's bull thesis plays out." Real outcomes
 * will vary wildly. Use for sizing intuition only, not as targets.
 */

const TOOLTIPS = {
  // ====================== TICKERS ======================
    NVDA: { kind: "ticker", name: "NVIDIA", cap: "$5.37T", bull_2027: "$8.05T", bull_2027_pct: "+50%", bull_2028: "$10.20T", bull_2028_pct: "+90%", price: "$216", bull_2027_px: "$324", bull_2028_px: "$411", stance: "bull", conv: "high", thesis: "AI chip leader. $1T confirmed demand through 2027; $90B long-term supply contracts; >70% of N3 wafer capacity by 2027.", as_of: "2026-05-12" },
  GOOGL: { kind: "ticker", name: "Alphabet", cap: "$4.80T", bull_2027: "$7.20T", bull_2027_pct: "+50%", bull_2028: "$9.12T", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Cheapest Mag 7 (fwd P/E ~29.7). TPU is the only credible NVDA alternative; co-designed with AVGO.", as_of: "2026-05-12" },
  AAPL: { kind: "ticker", name: "Apple", cap: "$4.30T", bull_2027: "$4.64T", bull_2027_pct: "+8%", bull_2028: "$4.95T", bull_2028_pct: "+15%", stance: "bear", conv: "medium", thesis: "STANCE FLIPPED 2026-05-09. TSMC deprioritization at A16; memory crunch projected to halve smartphone units (1.4B→550M by 2027).", as_of: "2026-05-12" },
  MSFT: { kind: "ticker", name: "Microsoft", cap: "$3.10T", bull_2027: "$4.65T", bull_2027_pct: "+50%", bull_2028: "$5.89T", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Azure + Copilot. AI capex leader. Tightly coupled with OpenAI on AI distribution.", as_of: "2026-05-12" },
  AMZN: { kind: "ticker", name: "Amazon", cap: "$2.89T", bull_2027: "$3.76T", bull_2027_pct: "+30%", bull_2028: "$4.33T", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "AWS reaccelerating + retail margin recovery. Trainium custom silicon co-designed with AVGO.", as_of: "2026-05-12" },
  TSLA: { kind: "ticker", name: "Tesla", cap: "$1.61T", bull_2027: "$1.74T", bull_2027_pct: "+8%", bull_2028: "$1.85T", bull_2028_pct: "+15%", stance: "bear", conv: "medium", thesis: "178x 2026 EPS. Valuation depends on unproven robotaxi/Optimus. Samsung Texas robot-chip deal is a small option-value positive.", as_of: "2026-05-12" },
  META: { kind: "ticker", name: "Meta Platforms", cap: "$1.52T", bull_2027: "$1.98T", bull_2027_pct: "+30%", bull_2028: "$2.28T", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "Ad biz funds AI. Dual non-NVDA paths: AVGO MTIA partnership + 6 GW AMD Instinct deal (with 160M-share warrant).", as_of: "2026-05-12" },
  TSM: { kind: "ticker", name: "Taiwan Semiconductor", cap: "$2.10T", bull_2027: "$3.15T", bull_2027_pct: "+50%", bull_2028: "$3.99T", bull_2028_pct: "+90%", price: "$405", bull_2027_px: "$607", bull_2028_px: "$769", stance: "bull", conv: "high", thesis: "Sole leading-edge foundry. 2026 capex $52-56B; rev growth ~30%. A16 first customer is AI, not Apple.", as_of: "2026-05-12" },
  AVGO: { kind: "ticker", name: "Broadcom", cap: "$1.99T", bull_2027: "$2.98T", bull_2027_pct: "+50%", bull_2028: "$3.78T", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Custom XPU for 6 hyperscalers. OpenAI Project Titan = 10 GW by 2029. Q1 AI rev +106% YoY to $8.4B. $100B AI rev target by 2027.", as_of: "2026-05-12" },
  ASML: { kind: "ticker", name: "ASML Holding", cap: "$614B", bull_2027: "$890B", bull_2027_pct: "+45%", bull_2028: "$1.11T", bull_2028_pct: "+80%", stance: "bull", conv: "high (multi-yr)", thesis: "EUV monopoly — THE binding constraint of all AI by 2028-2030. Risk: historically the 'generous monopolist' that hasn't taken margin.", as_of: "2026-05-12" },
  ARM: { kind: "ticker", name: "Arm Holdings", cap: "$252B", bull_2027: "$328B", bull_2027_pct: "+30%", bull_2028: "$378B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "Royalty stream scales with Vera Rubin volumes ramping 2H 2026. Vera CPU = 88-core Arm v9.2-A.", as_of: "2026-05-12" },
  AMD: { kind: "ticker", name: "Advanced Micro Devices", cap: "$743B", bull_2027: "$1.11T", bull_2027_pct: "+50%", bull_2028: "$1.41T", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Credible #2 GPU. OpenAI 6 GW + Meta 6 GW + Oracle 50K MI450. Helios rack ships Q3 2026 on TSMC 2nm.", as_of: "2026-05-12" },
  MU: { kind: "ticker", name: "Micron Technology", cap: "$847B", bull_2027: "$1.27T", bull_2027_pct: "+50%", bull_2028: "$1.61T", bull_2028_pct: "+90%", price: "$747", bull_2027_px: "$1,120", bull_2028_px: "$1,419", stance: "bull", conv: "high", thesis: "Preferred HBM supplier (12-high HBM3E). HBM4 ramp Q2 2026; +76% past month. Mizuho $740 PT.", as_of: "2026-05-12" },
  SNDK: { kind: "ticker", name: "SanDisk", cap: "$207B", bull_2027: "$310B", bull_2027_pct: "+50%", bull_2028: "$393B", bull_2028_pct: "+90%", price: "$1,399", bull_2027_px: "$2,098", bull_2028_px: "$2,657", stance: "bull", conv: "high", thesis: "NAND pure-play. HBF (High-Bandwidth Flash) = 8-16x HBM capacity at lower cost; first samples 2H 2026. +91% past month.", as_of: "2026-05-12" },
  WDC: { kind: "ticker", name: "Western Digital", cap: "$60B", bull_2027: "~$78.0B", bull_2027_pct: "+30%", bull_2028: "~$90.0B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "Nearline HDD oligopoly. Non-GAAP gross margin crossed 50%; 20% dividend increase; +40% past month.", as_of: "2026-05-12" },
  AMAT: { kind: "ticker", name: "Applied Materials", cap: "$346B", bull_2027: "$519B", bull_2027_pct: "+50%", bull_2028: "$657B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: ">50% of HBM equipment value (15 of 19 HBM stacking steps). >20% growth guide 2026; 12-24 month forward visibility.", as_of: "2026-05-12" },
  KLAC: { kind: "ticker", name: "KLA Corporation", cap: "$235B", bull_2027: "$352B", bull_2027_pct: "+50%", bull_2028: "$446B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Process control monopoly. Jefferies $1,500 PT (Dec 2025). Highest gross margin among WFE peers.", as_of: "2026-05-12" },
  LRCX: { kind: "ticker", name: "Lam Research", cap: "$370B", bull_2027: "$555B", bull_2027_pct: "+50%", bull_2028: "$703B", bull_2028_pct: "+90%", price: "$296", bull_2027_px: "$443", bull_2028_px: "$562", stance: "bull", conv: "high", thesis: "Deposition + etch. HBM is wafer-intensive (3x DDR5/GB) = Lam content. Systems revenue +26% FY26.", as_of: "2026-05-12" },
  TER: { kind: "ticker", name: "Teradyne", cap: "$57.6B", bull_2027: "$86.4B", bull_2027_pct: "+50%", bull_2028: "$109B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Chip test equipment. Q1 2026 revenue +87% YoY to $1.282B record. 70% AI exposure. +66% YTD.", as_of: "2026-05-12" },
  ENTG: { kind: "ticker", name: "Entegris", cap: "$17.4B", bull_2027: "$26.1B", bull_2027_pct: "+50%", bull_2028: "$33.1B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Fab consumables: FOUPs, ultra-pure materials, gas/liquid filtration. Content-per-wafer grows with AI complexity.", as_of: "2026-05-12" },
  KEYS: { kind: "ticker", name: "Keysight Technologies", cap: "$30B", bull_2027: "~$39.0B", bull_2027_pct: "+30%", bull_2028: "~$45.0B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "T&M for AI silicon design verification. Adjacent to WFE.", as_of: "2026-05-12" },
  AMKR: { kind: "ticker", name: "Amkor Technology", cap: "$10B", bull_2027: "~$15.0B", bull_2027_pct: "+50%", bull_2028: "~$19.0B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "OSAT for TSMC CoWoS overflow. 2026 capex $2.5-3B (~3x prior). Peoria AZ campus = US end-to-end advanced packaging.", as_of: "2026-05-12" },
  ASX: { kind: "ticker", name: "ASE Technology", cap: "$30B", bull_2027: "~$39.0B", bull_2027_pct: "+30%", bull_2028: "~$45.0B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "Largest OSAT globally. Advanced packaging sales doubling in 2026. Owns SPIL.", as_of: "2026-05-12" },
  CAMT: { kind: "ticker", name: "Camtek", cap: "$5B", bull_2027: "~$6.5B", bull_2027_pct: "+30%", bull_2028: "~$7.5B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "AOI inspection for advanced packaging (CoWoS, HBM stacks).", as_of: "2026-05-12" },
  COHR: { kind: "ticker", name: "Coherent Corp", cap: "$61.8B", bull_2027: "$92.7B", bull_2027_pct: "+50%", bull_2028: "$117B", bull_2028_pct: "+90%", price: "$344", bull_2027_px: "$516", bull_2028_px: "$654", stance: "bull", conv: "high", thesis: "NVDA $2B direct investment (with LITE). Q3 datacenter +41% YoY to $1.36B. Orders booked through 2028.", as_of: "2026-05-12" },
  LITE: { kind: "ticker", name: "Lumentum", cap: "$70.3B", bull_2027: "$105B", bull_2027_pct: "+50%", bull_2028: "$134B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "NVDA $2B (paired with COHR). Q3 revenue +90% YoY to $808M historic high. EML supplier.", as_of: "2026-05-12" },
  GLW: { kind: "ticker", name: "Corning", cap: "$80B", bull_2027: "~$120B", bull_2027_pct: "+50%", bull_2028: "~$152B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "NVDA $3.2B for 3 new US optical fiber factories (10x capacity expansion).", as_of: "2026-05-12" },
  FN: { kind: "ticker", name: "Fabrinet", cap: "$22B", bull_2027: "~$28.6B", bull_2027_pct: "+30%", bull_2028: "~$33.0B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "Contract mfg for optical transceivers. Customers: NVDA, Cisco, AWS, Lumentum. Demand outstrips supply.", as_of: "2026-05-12" },
  APH: { kind: "ticker", name: "Amphenol", cap: "$130B", bull_2027: "~$169B", bull_2027_pct: "+30%", bull_2028: "~$195B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "Diversified interconnect. AI rack content growing.", as_of: "2026-05-12" },
  DELL: { kind: "ticker", name: "Dell Technologies", cap: "$169B", bull_2027: "$254B", bull_2027_pct: "+50%", bull_2028: "$321B", bull_2028_pct: "+90%", price: "$238", bull_2027_px: "$357", bull_2028_px: "$452", stance: "bull", conv: "high", thesis: "Q4 FY26 AI server $8.95B (+342% YoY). FY27 guide $50B AI server revenue. $43B backlog. +67% YTD.", as_of: "2026-05-12" },
  HPE: { kind: "ticker", name: "Hewlett Packard Enterprise", cap: "$38.1B", bull_2027: "$49.5B", bull_2027_pct: "+30%", bull_2028: "$57.2B", bull_2028_pct: "+50%", price: "$29.94", bull_2027_px: "$38.92", bull_2028_px: "$44.91", stance: "bull", conv: "medium", thesis: "Q1 FY26 networking +152% YoY post-Juniper. FCF swung +$708M (from -$877M). Full Blackwell+Rubin portfolio.", as_of: "2026-05-12" },
  SMCI: { kind: "ticker", name: "Super Micro Computer", cap: "$21.2B", bull_2027: "$22.3B", bull_2027_pct: "+5%", bull_2028: "$23.3B", bull_2028_pct: "+10%", price: "$32.81", bull_2027_px: "$34.45", bull_2028_px: "$36.09", stance: "neutral", conv: "low", thesis: "Strong Blackwell support but accounting/legal overhang. -7% YTD vs DELL +67% / HPE +20%.", as_of: "2026-05-12" },
  JBL: { kind: "ticker", name: "Jabil", cap: "$25B", bull_2027: "~$32.5B", bull_2027_pct: "+30%", bull_2028: "~$37.5B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "Intelligent Infrastructure +52% YoY. AI rev $13.1B FY26 (+46%). $500M NC facility mid-2026.", as_of: "2026-05-12" },
  FLEX: { kind: "ticker", name: "Flex Ltd", cap: "$20B", bull_2027: "~$26.0B", bull_2027_pct: "+30%", bull_2028: "~$30.0B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "Diversified contract mfg with AI infra exposure.", as_of: "2026-05-12" },
  VRT: { kind: "ticker", name: "Vertiv Holdings", cap: "$141B", bull_2027: "$212B", bull_2027_pct: "+50%", bull_2028: "$268B", bull_2028_pct: "+90%", price: "$368", bull_2027_px: "$552", bull_2028_px: "$700", stance: "bull", conv: "high", thesis: "Only large player covering power AND cooling. Q1 2026 rev $2.65B (+30%); $9.5B backlog. Citi $414 PT.", as_of: "2026-05-12" },
  ETN: { kind: "ticker", name: "Eaton Corporation", cap: "$164B", bull_2027: "$246B", bull_2027_pct: "+50%", bull_2028: "$312B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Beam Rubin DSX with NVDA. 800V DC architecture. Q4 2025 data center orders +200%.", as_of: "2026-05-12" },
  GEV: { kind: "ticker", name: "GE Vernova", cap: "$290B", bull_2027: "$435B", bull_2027_pct: "+50%", bull_2028: "$551B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Combined-cycle gas turbines. Lead times beyond 2030 on specific blades. Blue Energy gas-plus-nuclear Texas deal.", as_of: "2026-05-12" },
  BE: { kind: "ticker", name: "Bloom Energy", cap: "$82.1B", bull_2027: "$123B", bull_2027_pct: "+50%", bull_2028: "$156B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Fuel cells. Oracle Project Jupiter 2.45 GW primary power; up to 2.8 GW across multiple Oracle deployments.", as_of: "2026-05-12" },
  STM: { kind: "ticker", name: "STMicroelectronics", cap: "$25B", bull_2027: "~$27.5B", bull_2027_pct: "+10%", bull_2028: "~$30.0B", bull_2028_pct: "+20%", stance: "neutral", conv: "medium", thesis: "Auto downturn caps near-term torque despite 800V DC partner status.", as_of: "2026-05-12" },
  ADI: { kind: "ticker", name: "Analog Devices", cap: "$120B", bull_2027: "~$156B", bull_2027_pct: "+30%", bull_2028: "~$180B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "800V DC partner. Quality compounder. Industrial recovery + AI dual tailwind.", as_of: "2026-05-12" },
  MPWR: { kind: "ticker", name: "Monolithic Power Systems", cap: "$35B", bull_2027: "~$45.5B", bull_2027_pct: "+30%", bull_2028: "~$52.5B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "PMIC for AI server power delivery. Specialty fabless model.", as_of: "2026-05-12" },
  NVTS: { kind: "ticker", name: "Navitas Semiconductor", cap: "$5.3B", bull_2027: "$6.4B", bull_2027_pct: "+20%", bull_2028: "$6.9B", bull_2028_pct: "+30%", stance: "bull", conv: "low", thesis: "GaN/SiC. NVDA 800V partner but ~74x sales — extreme valuation. Inflection 2027.", as_of: "2026-05-12" },
  ON: { kind: "ticker", name: "onsemi", cap: "$25B", bull_2027: "~$27.5B", bull_2027_pct: "+10%", bull_2028: "~$30.0B", bull_2028_pct: "+20%", stance: "neutral", conv: "medium", thesis: "SiC leader but auto cycle weighs.", as_of: "2026-05-12" },
  FIX: { kind: "ticker", name: "Comfort Systems USA", cap: "$71.0B", bull_2027: "$106B", bull_2027_pct: "+50%", bull_2028: "$135B", bull_2028_pct: "+90%", price: "$2,009", bull_2027_px: "$3,014", bull_2028_px: "$3,818", stance: "bull", conv: "high", thesis: "Pure mech/HVAC contractor. Q1 2026 backlog $12.46B (+81% YoY). 45% data center mix. Mech gross margin 26.9%. Joining S&P 500.", as_of: "2026-05-12" },
  EME: { kind: "ticker", name: "EMCOR Group", cap: "$41.2B", bull_2027: "$61.8B", bull_2027_pct: "+50%", bull_2028: "$78.3B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Largest US MEP contractor. Q1 2026 RPOs $15.62B record. FY26 EPS guide raised to $28.25-$29.75.", as_of: "2026-05-12" },
  PWR: { kind: "ticker", name: "Quanta Services", cap: "$117B", bull_2027: "$176B", bull_2027_pct: "+50%", bull_2028: "$222B", bull_2028_pct: "+90%", stance: "bull", conv: "high", thesis: "Transmission/substation/grid. Q1 2026 backlog $48.5B record. NiSource ~3 GW generation engagement. +25% in 5-day streak May 2026.", as_of: "2026-05-12" },
  APD: { kind: "ticker", name: "Air Products & Chemicals", cap: "$67.8B", bull_2027: "$88.1B", bull_2027_pct: "+30%", bull_2028: "$102B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "Industrial gases for fabs (N2/O2/Ar/H2 + NF3). Samsung Pyeongtaek = APD's largest semi investment in history. Multi-decade BOO contracts.", as_of: "2026-05-12" },
  CRWV: { kind: "ticker", name: "CoreWeave", cap: "$42.7B", bull_2027: "$55.5B", bull_2027_pct: "+30%", bull_2028: "$64.1B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "Largest neocloud. NVDA $250M IPO anchor. Meta deal ~$35B total through 2032.", as_of: "2026-05-12" },
  NBIS: { kind: "ticker", name: "Nebius Group", cap: "$45.0B", bull_2027: "$58.5B", bull_2027_pct: "+30%", bull_2028: "$67.5B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "NVDA $2B direct investment. Meta $27B contract. 2 GW power contracted; 800MW-1GW connected by EOY 2026.", as_of: "2026-05-12" },
  NOK: { kind: "ticker", name: "Nokia", cap: "$25B", bull_2027: "~$30.0B", bull_2027_pct: "+20%", bull_2028: "~$32.5B", bull_2028_pct: "+30%", stance: "bull", conv: "low", thesis: "NVDA $1B for AI-RAN/6G. T-Mobile US trials 2026. Long lead time to revenue.", as_of: "2026-05-12" },
  SNPS: { kind: "ticker", name: "Synopsys", cap: "$90B", bull_2027: "~$117B", bull_2027_pct: "+30%", bull_2028: "~$135B", bull_2028_pct: "+50%", stance: "bull", conv: "medium", thesis: "EDA duopoly with Cadence. NVDA $2B minority stake for AI/GPU-accelerated chip design tools.", as_of: "2026-05-12" },
  ORCL: { kind: "ticker", name: "Oracle", cap: "$554B", bull_2027: "$720B", bull_2027_pct: "+30%", bull_2028: "$831B", bull_2028_pct: "+50%", price: "$186", bull_2027_px: "$242", bull_2028_px: "$279", stance: "bull", conv: "medium", thesis: "OpenAI compute partner. Multi-year capacity deals. Project Jupiter (BE 2.45 GW) + AMD 50K MI450.", as_of: "2026-05-12" },
  CBRS: { kind: "ticker", name: "Cerebras Systems", cap: "$48.8B", bull_2027: "$63.4B", bull_2027_pct: "+30%", bull_2028: "$73.2B", bull_2028_pct: "+50%", price: "$155", bull_2027_px: "$202", bull_2028_px: "$233", stance: "bull", conv: "medium", thesis: "Wafer-scale AI chip. IPO May 13 2026 ($48.8B, 20x oversubscribed, 51x trailing rev). $510M 2025 revenue / 47% net margin. OpenAI $10B/750MW commitment. RISK: 86% UAE customer concentration (MBZUAI 62%, G42 24%).", as_of: "2026-05-13" },

  // ====================== TERMS ======================
  HBM: { kind: "term", name: "HBM (High-Bandwidth Memory)", def: "Vertically-stacked DRAM with massively higher bandwidth than DDR5 (2.5 TB/s vs 64-128 GB/s per shoreline). The memory technology used in AI GPUs/accelerators. Consumes 3-4x wafer area per bit vs commodity DRAM." },
  HBF: { kind: "term", name: "HBF (High-Bandwidth Flash)", def: "SanDisk's vertically-stacked NAND product — same architecture as HBM but using NAND instead of DRAM. Promises 8-16x the capacity of HBM in the same footprint at lower cost. First samples expected 2H 2026." },
  EUV: { kind: "term", name: "EUV (Extreme Ultraviolet Lithography)", def: "ASML's lithography machines required for patterning chips at advanced nodes (≤7nm). ~70 tools/yr current output → ~100 by 2030 aggressive case. 3.5 tools = 1 GW of AI compute capacity." },
  DUV: { kind: "term", name: "DUV (Deep Ultraviolet Lithography)", def: "Older-generation lithography (193nm wavelength) used for less-advanced nodes (≥7nm via multi-patterning). ASML dominates here too. China's chip industry currently relies on imported DUV." },
  CoWoS: { kind: "term", name: "CoWoS (Chip-on-Wafer-on-Substrate)", def: "TSMC's advanced packaging technology that integrates multiple chips (GPU + HBM stacks) onto a single interposer. The major capacity bottleneck of 2023 AI chip rollouts; now oversubscribed through 2026." },
  FOUP: { kind: "term", name: "FOUP (Front-Opening Unified Pod)", def: "The standardized 300mm wafer-carrier pod that protects wafers from contamination as they move between fab process steps. Entegris is the dominant supplier." },
  WFE: { kind: "term", name: "WFE (Wafer Fab Equipment)", def: "Capital equipment used to manufacture semiconductors. Includes lithography (ASML), deposition/etch (LRCX, AMAT), and process control (KLAC). 2026 industry forecast: $145B." },
  NF3: { kind: "term", name: "NF3 (Nitrogen Trifluoride)", def: "The leading specialty gas for chamber cleaning in semiconductor fabs. Air Products is one of the few large Western suppliers; operates a 4-site global transfill network." },
  TPU: { kind: "term", name: "TPU (Tensor Processing Unit)", def: "Google's custom AI accelerator, co-designed with Broadcom (AVGO). The only credible non-NVIDIA accelerator at hyperscaler scale. Multi-generation; Ironwood is v7." },
  XPU: { kind: "term", name: "XPU (any custom AI accelerator)", def: "Generic term for custom AI accelerators designed for a specific workload — typically by Broadcom for hyperscalers (Google TPU, Meta MTIA, Amazon Trainium, etc.)." },
  ASIC: { kind: "term", name: "ASIC (Application-Specific Integrated Circuit)", def: "A chip designed for a specific use case rather than general purpose. AI accelerators (TPU, MTIA, Trainium) are ASICs; CPUs and GPUs are not." },
  DPU: { kind: "term", name: "DPU (Data Processing Unit)", def: "A specialized processor that offloads networking, storage, and security tasks from the CPU. Marvell (Pensando) and NVIDIA (BlueField) are major DPU vendors." },
  SoC: { kind: "term", name: "SoC (System-on-Chip)", def: "An integrated circuit combining CPU, GPU, memory controllers, and other components onto a single chip. Apple's M-series and A-series are SoCs." },
  PMIC: { kind: "term", name: "PMIC (Power Management Integrated Circuit)", def: "A chip that handles voltage regulation, power sequencing, and power delivery on a board. Monolithic Power Systems (MPWR) and Analog Devices (ADI) are major suppliers." },
  GaN: { kind: "term", name: "GaN (Gallium Nitride)", def: "A wide-bandgap semiconductor material used in power electronics for higher efficiency at high voltages. Navitas (NVTS) is a pure-play GaN company." },
  SiC: { kind: "term", name: "SiC (Silicon Carbide)", def: "A wide-bandgap material used in power electronics, especially for EVs and data center power. ST, ON, Wolfspeed, and Infineon are major suppliers." },
  EML: { kind: "term", name: "EML (Electro-absorption Modulated Laser)", def: "A high-speed laser used in optical transceivers for data center fabric. Currently a supply bottleneck for optical-component manufacturing (Coherent and Lumentum are major suppliers)." },
  CPO: { kind: "term", name: "CPO (Co-Packaged Optics)", def: "Silicon photonics integrated directly with the switch ASIC rather than as a pluggable transceiver. Higher bandwidth and lower power. NVDA's Spectrum-X/Quantum-X switches use CPO." },
  OSAT: { kind: "term", name: "OSAT (Outsourced Semiconductor Assembly & Test)", def: "Companies that handle the back-end assembly, packaging, and testing of chips for fabless designers and IDMs. ASE Technology and Amkor are the two largest." },
  ODM: { kind: "term", name: "ODM (Original Design Manufacturer)", def: "A contract manufacturer that designs and builds products for other brands. Foxconn, Quanta, and Wistron are the major Asian ODMs for hyperscaler-direct AI server programs." },
  BOO: { kind: "term", name: "BOO (Build-Own-Operate)", def: "A contract model where a supplier builds, owns, and operates infrastructure on the customer's site under a long-term off-take agreement. Air Products uses BOO for industrial gas plants at fabs (typically 15-20 year contracts)." },
  MEP: { kind: "term", name: "MEP (Mechanical / Electrical / Plumbing)", def: "The combined trades of mechanical (HVAC), electrical, and plumbing contracting required to build out a data center. EMCOR (EME) is the largest US MEP contractor." },
  RPO: { kind: "term", name: "RPO (Remaining Performance Obligations)", def: "Contracted but not-yet-recognized revenue under existing customer agreements. A more conservative backlog metric than total backlog. EMCOR's Q1 2026 RPOs hit $15.62B." },
  PPA: { kind: "term", name: "PPA (Power Purchase Agreement)", def: "A long-term contract between a power producer and a buyer (utility or hyperscaler) for electricity at agreed prices. The mechanism by which hyperscalers lock in dedicated power for data centers." },
  CAPE: { kind: "term", name: "CAPE / Shiller P/E", def: "Cyclically-Adjusted Price-to-Earnings ratio — uses a 10-year average of inflation-adjusted earnings rather than trailing or forward. Currently 39.8, highest reading since the 2000 dot-com peak (44.2). Long-run average ~17." },
  FOMC: { kind: "term", name: "FOMC (Federal Open Market Committee)", def: "The Federal Reserve committee that sets US interest rate policy. Held the federal funds rate at 3.50-3.75% in April 2026 with an 8-4 dissent — the largest split since October 1992." },
  FCF: { kind: "term", name: "FCF (Free Cash Flow)", def: "Operating cash flow minus capital expenditures. The cash a company actually has available after maintaining/expanding its asset base. Most hyperscaler AI capex is currently funded out of FCF, not debt." },
  TCO: { kind: "term", name: "TCO (Total Cost of Ownership)", def: "The full cost of operating a piece of equipment over its useful life, including capex, power, cooling, maintenance, and depreciation. For an H100, ~$1.40/hour over 5 years." },
  NCNR: { kind: "term", name: "NCNR (Non-Cancelable, Non-Returnable)", def: "Contract terms binding the buyer to take delivery and pay regardless of demand changes. NVIDIA secured massive NCNR contracts with TSMC and memory suppliers." },
  ARR: { kind: "term", name: "ARR (Annual Recurring Revenue)", def: "A SaaS-style metric: subscription revenue annualized. Most AI labs (OpenAI, Anthropic) report ARR. Anthropic added $4-6B/month in revenue in early 2026." },
  BOM: { kind: "term", name: "BOM (Bill of Materials)", def: "The total cost of physical components going into a product. Memory price triples have added ~$150 to iPhone BOM, translating to ~$250 retail price impact at Apple's typical margin." },
  HVDC: { kind: "term", name: "HVDC (High-Voltage Direct Current)", def: "Power transmission/distribution at high voltage in DC form. NVIDIA's 800V HVDC architecture is the next-gen power scheme for AI data centers, partnered with Eaton, Schneider, Vertiv, Navitas, STM." },
  AI_RAN: { kind: "term", name: "AI-RAN (AI Radio Access Network)", def: "Cellular infrastructure where the radio access network's signal processing runs on AI accelerators rather than dedicated baseband chips. The 5G→6G transition NVDA-Nokia is targeting." },
  RAN: { kind: "term", name: "RAN (Radio Access Network)", def: "The portion of cellular networks handling radio communications — base stations, antennas, signal processing. The $1B NVDA-Nokia partnership focuses on AI-native RAN for 6G." },
  KV_cache: { kind: "term", name: "KV Cache", def: "Cached attention key-value tensors stored in GPU memory during LLM inference. Grows with context length — the reason long-context AI dramatically increases memory demand. Half the cost of accelerators is memory." },
  MoE: { kind: "term", name: "MoE (Mixture of Experts)", def: "A neural network architecture where multiple 'expert' sub-networks are sparsely activated per token. Used by GPT-5.4 and DeepSeek." },
  CMP: { kind: "term", name: "CMP (Chemical Mechanical Planarization)", def: "A wafer-processing step that polishes the wafer surface flat between deposition steps. Critical for advanced nodes. Entegris (via CMC Materials acquisition) is a major slurry supplier." },

  // ====================== PRODUCTS ======================
  Blackwell: { kind: "product", name: "Blackwell (NVIDIA)", def: "NVIDIA's current-generation AI GPU platform (B100/B200/GB200/GB300). Sold out through mid-2026; the backlog cascades into Vera Rubin. ~$78B Q1 FY27 revenue guide." },
  Hopper: { kind: "product", name: "Hopper / H100 / H200 (NVIDIA)", def: "NVIDIA's prior-gen AI GPU (H100, H200). Still widely deployed; ~$1.40/hr 5-year TCO. Per Dylan Patel: 'an H100 is worth more today than 3 years ago' — labs signing $2.40/hr long-term deals." },
  Vera_Rubin: { kind: "product", name: "Vera Rubin (NVIDIA)", def: "NVIDIA's next-generation AI compute platform launching at GTC 2026. Vera CPU (88-core Arm v9.2-A 'Olympus' custom design) paired with Rubin GPU. Available 2H 2026." },
  GB200: { kind: "product", name: "GB200 (NVIDIA)", def: "Grace Blackwell Superchip — pairs an Arm-based Grace CPU with two Blackwell GPUs. The building block of the NVL72 rack-scale system." },
  GB300: { kind: "product", name: "GB300 (NVIDIA)", def: "Grace Blackwell Ultra Desktop Superchip. Dell was the first OEM to ship a desktop with the GB300." },
  NVL72: { kind: "product", name: "NVL72 (NVIDIA)", def: "Rack-scale AI system with 72 Blackwell GPUs interconnected at terabytes/second via NVLink. Pushed scale-up domain from 8 GPUs (H100 server) to 72 GPUs (rack scale)." },
  Helios: { kind: "product", name: "Helios (AMD)", def: "AMD's rack-scale AI platform launching Q3 2026. 72 MI455X accelerators + 31 TB HBM4 = 3 AI exaflops per rack. AMD's first credible answer to NVIDIA's NVL72." },
  MI450: { kind: "product", name: "MI450 (AMD)", def: "AMD's Instinct MI450 AI GPU. Subject of major commitments: OpenAI 6 GW deal (Oct 2025), Meta 6 GW deal (Feb 2026), Oracle 50,000 units. Sampling to lead customers; production H2 2026." },
  MI500: { kind: "product", name: "MI500 (AMD)", def: "AMD's next-gen AI accelerator beyond MI400/MI450. Built on TSMC 2nm. AMD claims 1000x AI performance increase from the architecture." },
  Tomahawk6: { kind: "product", name: "Tomahawk 6 (Broadcom)", def: "Broadcom's networking silicon — the world's first 102.4 Tbps switch ASIC. Doubles the bandwidth of the prior generation. Volume deployment early 2026." },
  Project_Titan: { kind: "product", name: "Project Titan (OpenAI × Broadcom)", def: "OpenAI's custom AI inference engine, co-developed with Broadcom. Targeting 10 GW of deployed compute by 2029. Mass production begins late 2026." },
  Project_Jupiter: { kind: "product", name: "Project Jupiter (Oracle × Bloom Energy)", def: "Oracle's New Mexico data center campus, powered entirely by Bloom Energy fuel cells. 2.45 GW capacity; Oracle contracted up to 2.8 GW from BE across multiple deployments." },
  Trainium: { kind: "product", name: "Trainium (Amazon × Broadcom)", def: "Amazon's custom AI training accelerator, co-designed with Broadcom. Part of AWS's strategy to reduce dependence on NVIDIA. Trainium 2 is the current generation." },
  MTIA: { kind: "product", name: "MTIA (Meta × Broadcom)", def: "Meta's Training and Inference Accelerator, co-designed with Broadcom. >1 GW first-phase commitment with multi-gigawatt rollout planned." },
  CUDA: { kind: "product", name: "CUDA (NVIDIA)", def: "NVIDIA's parallel computing platform and programming model. The software moat that anchors NVIDIA's GPU monopoly — switching away requires re-platforming AI workloads to ROCm (AMD) or other alternatives." },
  ROCm: { kind: "product", name: "ROCm (AMD)", def: "AMD's open-source software stack for GPU compute — the direct competitor to NVIDIA's CUDA. Still significantly behind CUDA in maturity but improving rapidly with each AMD MI generation." },
  NVLink: { kind: "product", name: "NVLink (NVIDIA)", def: "NVIDIA's high-bandwidth chip-to-chip interconnect for multi-GPU systems. Terabytes-per-second bandwidth within a server or rack. The basis for NVL72 rack-scale scale-up domains." },
  Spectrum_X: { kind: "product", name: "Spectrum-X (NVIDIA)", def: "NVIDIA's Ethernet-based AI networking platform — includes Spectrum-X switches and BlueField DPUs. Co-developed with Coherent and Lumentum for co-packaged optics versions." },
  Gemini: { kind: "product", name: "Gemini (Google)", def: "Google's family of frontier AI models. Gemini Pro is the largest production model of any major lab (larger than GPT-5.4 or Opus). Q4 2025 ARR hit $5B." },
  Opus: { kind: "product", name: "Claude Opus (Anthropic)", def: "Anthropic's most capable Claude model tier. Current generation is Opus 4.6. Sonnet is the mid-tier; Haiku is the small/fast tier." },
  Llama: { kind: "product", name: "Llama (Meta)", def: "Meta's family of open-source frontier AI models. Strategic role in commoditizing competitors' moat and positioning Meta as the default platform for open-model AI development." },
  Beam_Rubin_DSX: { kind: "product", name: "Beam Rubin DSX (Eaton × NVIDIA)", def: "Eaton's grid-to-chip power infrastructure platform, integrated with NVIDIA's Vera Rubin DSX AI Factory reference design. Targets the 'nearly $7 trillion' data center buildout market." },
  HGX: { kind: "product", name: "HGX (NVIDIA)", def: "NVIDIA's reference design platform for building 4-GPU and 8-GPU servers. HGX B100/B200 are the Blackwell-based versions that OEMs (Dell, HPE, SMCI) integrate into their server SKUs." },
  DGX: { kind: "product", name: "DGX (NVIDIA)", def: "NVIDIA's first-party AI supercomputer product line. Sold directly by NVIDIA as turnkey AI infrastructure, parallel to the OEM HGX channel." }
};

// =============================================================================
// TOOLTIP RUNTIME — handles desktop hover + mobile tap-to-show
// =============================================================================

(function() {
  function init() {
    const isTouch = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);

    const style = document.createElement("style");
    style.textContent = `
      [data-tip] {
        border-bottom: 1px dashed currentColor;
        cursor: help;
        transition: opacity 0.15s ease;
        -webkit-tap-highlight-color: transparent;
      }
      [data-tip]:hover { opacity: 0.85; }
      [data-tip].active { opacity: 0.6; }

      #wiki-tooltip {
        position: fixed;
        z-index: 10000;
        background: rgba(20, 20, 19, 0.97);
        color: #faf9f5;
        padding: 14px 16px;
        border-radius: 10px;
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.32), 0 0 0 1px rgba(255, 255, 255, 0.06);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, sans-serif;
        font-size: 13px;
        line-height: 1.5;
        max-width: 340px;
        opacity: 0;
        transform: translateY(-4px);
        transition: opacity 0.14s ease, transform 0.14s ease;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        pointer-events: none;
      }
      #wiki-tooltip.show { opacity: 1; transform: translateY(0); }
      #wiki-tooltip.pinned { pointer-events: auto; }

      /* Mobile / touch: full-width bottom sheet */
      @media (max-width: 640px), (pointer: coarse) {
        #wiki-tooltip {
          left: 12px !important;
          right: 12px !important;
          bottom: 12px !important;
          top: auto !important;
          max-width: none;
          width: auto;
          padding: 18px 18px 20px;
          font-size: 14px;
          border-radius: 14px;
          transform: translateY(20px);
          box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.06);
        }
        #wiki-tooltip.show { transform: translateY(0); }
        #wiki-tooltip .close-btn { display: flex; }
      }

      #wiki-tooltip .close-btn {
        display: none;
        position: absolute;
        top: 10px;
        right: 10px;
        width: 28px;
        height: 28px;
        background: rgba(255, 255, 255, 0.08);
        border: none;
        color: #faf9f5;
        font-size: 16px;
        font-weight: 700;
        cursor: pointer;
        border-radius: 50%;
        align-items: center;
        justify-content: center;
        padding: 0;
        line-height: 1;
      }
      #wiki-tooltip .close-btn:hover { background: rgba(255, 255, 255, 0.15); }

      #wiki-tooltip .ttl {
        font-weight: 600;
        font-size: 13px;
        color: #faf9f5;
        display: flex;
        align-items: baseline;
        gap: 8px;
        margin-bottom: 10px;
        padding-right: 32px;
      }
      #wiki-tooltip .ttl .sym {
        font-family: ui-monospace, "SF Mono", Menlo, monospace;
        color: #cc785c;
        font-weight: 700;
        font-size: 14px;
      }
      #wiki-tooltip .ttl .nm {
        color: #a09d96;
        font-weight: 400;
        font-size: 12px;
        flex: 1;
      }
      #wiki-tooltip .ttl .kind {
        background: rgba(255, 255, 255, 0.08);
        color: #a09d96;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 9px;
        padding: 2px 6px;
        border-radius: 3px;
        font-weight: 600;
      }
      #wiki-tooltip .row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        font-size: 12px;
      }
      #wiki-tooltip .row:last-of-type { border-bottom: 0; }
      #wiki-tooltip .row .lbl {
        color: #a09d96;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        font-size: 10px;
        font-weight: 600;
      }
      #wiki-tooltip .row .val {
        color: #faf9f5;
        font-variant-numeric: tabular-nums;
        font-weight: 600;
      }
      #wiki-tooltip .scenario {
        margin-top: 8px;
        background: rgba(204, 120, 92, 0.08);
        border-left: 2px solid rgba(204, 120, 92, 0.6);
        border-radius: 0 6px 6px 0;
        padding: 8px 10px;
      }
      #wiki-tooltip .scenario-ttl {
        font-size: 9px;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: #cc785c;
        font-weight: 700;
        margin-bottom: 4px;
      }
      #wiki-tooltip .scenario-row {
        display: flex;
        justify-content: space-between;
        font-size: 11.5px;
        padding: 1px 0;
      }
      #wiki-tooltip .scenario-row .y { color: #a09d96; font-weight: 600; }
      #wiki-tooltip .scenario-row .pct {
        color: #7adf90;
        font-weight: 700;
        font-size: 11px;
        margin-left: 4px;
      }
      #wiki-tooltip .scenario-row .px {
        color: #d4d1c9;
        font-weight: 500;
        font-size: 11.5px;
      }
      #wiki-tooltip .scenario-row .v {
        color: #f5e9d8;
        font-weight: 600;
        font-variant-numeric: tabular-nums;
      }
      #wiki-tooltip .scenario-note {
        font-size: 10px;
        color: #7a7770;
        margin-top: 4px;
        font-style: italic;
      }
      #wiki-tooltip .pill {
        display: inline-block;
        padding: 1px 7px;
        border-radius: 10px;
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
      }
      #wiki-tooltip .pill.bull { background: rgba(93, 184, 114, 0.18); color: #7adf90; }
      #wiki-tooltip .pill.bear { background: rgba(198, 69, 69, 0.18); color: #ff8a8a; }
      #wiki-tooltip .pill.neutral { background: rgba(255, 255, 255, 0.10); color: #cfccc4; }
      #wiki-tooltip .thesis {
        margin-top: 9px;
        font-size: 12px;
        color: #d4d1c9;
        line-height: 1.5;
      }
      #wiki-tooltip .def {
        font-size: 12.5px;
        color: #d4d1c9;
        line-height: 1.55;
      }
      #wiki-tooltip .as-of {
        margin-top: 8px;
        padding-top: 6px;
        border-top: 1px solid rgba(255, 255, 255, 0.06);
        color: #7a7770;
        font-size: 10px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
      }
    `;
    document.head.appendChild(style);

    const tip = document.createElement("div");
    tip.id = "wiki-tooltip";
    tip.setAttribute("role", "tooltip");
    tip.innerHTML = '<button class="close-btn" aria-label="Close">×</button><div class="content"></div>';
    document.body.appendChild(tip);
    const tipContent = tip.querySelector(".content");
    const closeBtn = tip.querySelector(".close-btn");

    function render(d, key) {
      if (!d) return "";
      if (d.kind === "ticker") {
        const pillClass = d.stance || "neutral";
        let scenario = "";
        if (d.bull_2027 || d.bull_2028) {
          const px27 = d.bull_2027_px ? ` &middot; <span class="px">${d.bull_2027_px}</span>` : "";
          const px28 = d.bull_2028_px ? ` &middot; <span class="px">${d.bull_2028_px}</span>` : "";
          scenario = `
            <div class="scenario">
              <div class="scenario-ttl">Bull scenario (cap &amp; price)</div>
              ${d.bull_2027 ? `<div class="scenario-row"><span class="y">If 2027 goes well</span><span class="v">${d.bull_2027} <span class="pct">${d.bull_2027_pct}</span>${px27}</span></div>` : ""}
              ${d.bull_2028 ? `<div class="scenario-row"><span class="y">If 2028 goes well</span><span class="v">${d.bull_2028} <span class="pct">${d.bull_2028_pct}</span>${px28}</span></div>` : ""}
              <div class="scenario-note">Scenario assumes conviction-tier multiplier &mdash; not an analyst target. Implied $/share at constant share count where price available.</div>
            </div>
          `;
        }
        return `
          <div class="ttl">
            <span class="sym">${key}</span>
            <span class="nm">${d.name}</span>
          </div>
          <div class="row"><span class="lbl">Market cap</span><span class="val">${d.cap}</span></div>
          ${d.price ? `<div class="row"><span class="lbl">Price (current)</span><span class="val">${d.price}</span></div>` : ""}
          <div class="row"><span class="lbl">Stance</span><span class="val"><span class="pill ${pillClass}">${d.stance} · ${d.conv}</span></span></div>
          ${scenario}
          <div class="thesis">${d.thesis}</div>
          <div class="as-of">Data as of ${d.as_of}</div>
        `;
      }
      return `
        <div class="ttl"><span class="nm" style="flex:none;color:#faf9f5;text-align:left;margin:0;font-weight:600">${d.name}</span><span class="kind">${d.kind}</span></div>
        <div class="def">${d.def}</div>
      `;
    }

    function position(e) {
      // Only used on desktop hover. Mobile uses fixed bottom-sheet via CSS.
      if (isTouch) return;
      const padding = 14;
      const vw = window.innerWidth;
      const vh = window.innerHeight;
      let x = e.clientX + padding;
      let y = e.clientY + padding;
      const r = tip.getBoundingClientRect();
      if (x + r.width + 8 > vw) x = e.clientX - r.width - padding;
      if (y + r.height + 8 > vh) y = e.clientY - r.height - padding;
      x = Math.max(8, Math.min(x, vw - r.width - 8));
      y = Math.max(8, Math.min(y, vh - r.height - 8));
      tip.style.left = x + "px";
      tip.style.top = y + "px";
    }

    let activeKey = null;
    let activeEl = null;
    let pinned = false;

    function show(key, el, e) {
      const data = TOOLTIPS[key];
      if (!data) return;
      if (key !== activeKey) {
        tipContent.innerHTML = render(data, key);
        activeKey = key;
      }
      if (activeEl && activeEl !== el) activeEl.classList.remove("active");
      activeEl = el;
      el.classList.add("active");
      tip.classList.add("show");
      if (e) position(e);
    }

    function hide() {
      tip.classList.remove("show", "pinned");
      if (activeEl) activeEl.classList.remove("active");
      activeEl = null;
      activeKey = null;
      pinned = false;
    }

    closeBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      hide();
    });

    if (!isTouch) {
      // DESKTOP: hover behavior
      document.addEventListener("mouseover", (e) => {
        const t = e.target.closest("[data-tip]");
        if (!t) return;
        show(t.getAttribute("data-tip"), t, e);
      });
      document.addEventListener("mousemove", (e) => {
        if (tip.classList.contains("show")) position(e);
      });
      document.addEventListener("mouseout", (e) => {
        const t = e.target.closest("[data-tip]");
        if (!t) return;
        const related = e.relatedTarget && e.relatedTarget.closest && e.relatedTarget.closest("[data-tip]");
        if (related === t) return;
        hide();
      });
    } else {
      // MOBILE / TOUCH: tap to show, tap outside or close button to dismiss
      document.addEventListener("click", (e) => {
        const t = e.target.closest("[data-tip]");
        if (t) {
          e.preventDefault();
          e.stopPropagation();
          show(t.getAttribute("data-tip"), t);
          pinned = true;
          tip.classList.add("pinned");
          return;
        }
        if (tip.classList.contains("show") && !e.target.closest("#wiki-tooltip")) {
          hide();
        }
      });
    }

    // Convert external links to open in new tabs
    document.querySelectorAll('a[href]').forEach(a => {
      const href = a.getAttribute("href");
      if (!href || href.startsWith("#")) return;
      if (href.startsWith("/") && !href.startsWith("//")) return;
      if (a.hasAttribute("target")) return;
      try {
        const u = new URL(href, window.location.href);
        if (u.origin !== window.location.origin) {
          a.setAttribute("target", "_blank");
          a.setAttribute("rel", "noopener noreferrer");
        }
      } catch (_) {}
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
