---
date: 2026-05-17
type: blog-sweep
publisher: SemiWiki (Daniel Nenni)
url: multiple — see articles below
touches: [TSM, INTC, SNPS, SOITEC, ASML, bottleneck-roadmap, semiconductors, us-china-relations]
---

# Nenni Blog Sweep — Global 2nm Crunch + Mii TSMC Roadmap + Synopsys-TSMC Alliance

Three Daniel Nenni articles read via authenticated Chrome MCP session. All confirm and sharpen existing wiki framing rather than introducing wholly new theses — but anchor the wiki's foundry-side stance with primary technical detail.

## Article 1: "Global 2nm Supply Crunch: TSMC Leads as Intel 18A, Samsung, and Rapidus Race to Compete" (March 6, 2026)
**URL**: https://semiwiki.com/semiconductor-manufacturers/tsmc/367081-global-2nm-supply-crunch-tsmc-leads-as-intel-18a-samsung-and-rapidus-race-to-compete/

### Key data points
- **TSMC N2 entered volume production late 2025**; "effectively sold out through 2026"
- Anchor customers: **Apple, Nvidia, Qualcomm, AMD** all locking in large shares
- TSMC monthly wafer starts targeted to "well into six figures by 2026-2028"
- TSMC CapEx trajectory: 2024 $29.8B → 2025 $40.9B (+37%) → 2026 **$52-56B** (matches our [[TSM]] page)
- N2 PPA: up to **15% performance gains OR substantial power reductions** vs prior nodes

### Nenni's verdicts (verbatim quotes worth keeping)
- On TSMC: *"TSMC will again dominate 2nm as it did 3nm without question."*
- On Intel: *"Intel was first to production quality GAA and first to BSPD, semiconductor innovation at its finest."* — gives technical credit to Intel
- Bullish Intel framing: *"With Lip-Bu Tan as CEO that has changed of course. The semiconductor Made in America brand has never been stronger, Intel will sign wafer agreements for 18A and 14A from the top semiconductor companies, without a doubt."*
- On Samsung: *"Samsung is not a viable alternative to TSMC for high-volume 2nm orders. Trust is the foundation of the semiconductor industry and without predictable yield there can be no trust."*

### Rapidus (Japan, government-backed) — new wiki coverage candidate
- 2nm-class chip production target: **around 2027**
- Just raised **$1.7B more → $11.3B total** in government subsidies + private investment
- This is **40% of the $32B Rapidus estimates needed** for full-scale mass production
- Strategy: short turnaround + custom small-lot services, NOT volume competition
- Nenni's view: *"From what I have learned about Rapidus over the last year, there is little doubt in my mind that they will succeed."*

**Why Rapidus matters for the wiki**:
- Sovereign-AI / Japan supply-chain hedge — relevant to [[us-china-relations]] sovereign-supply theme
- Funding gap ($32B needed vs $11.3B raised) = needs more capital; potential IPO or strategic investor event
- Private/sovereign-backed; not investable directly but tracks supply-chain alternatives to TSMC

## Article 2: "Dr. Y.J. Mii on TSMC Technology Leadership in 2026" (April 30, 2026)
**URL**: https://semiwiki.com/semiconductor-manufacturers/tsmc/368876-dr-y-j-mii-on-tsmc-technology-leadership-in-2026/

Dr. Y.J. Mii: TSMC SVP R&D since Nov 2016; 30+ year veteran; led 90nm/40nm/28nm node development.

### TSMC roadmap announcements
- **A14** (2nd-gen nanosheet, NanoFlex Pro): **10-15% speed improvement OR 25-30% power reduction** vs N2; production **expected by 2028**
- **A13** (post-A14): 6% die size reduction via optical shrink; backward compatible with A14
- **A12** mentioned (further out)
- **N2 family**: N2, N2P, N2X, N2U — all in customer use; strong adoption
- **CFET** (Complementary FET — vertical nFET/pFET stacking): TSMC has demonstrated early CFET implementations; future scaling beyond GAA
- **2D-material transistors**: research showing significant performance improvements

### Packaging + photonics roadmap
- **CoWoS**: increasing reticle sizes + HBM integration through 2030
- **SoW** (System on Wafer): entire systems integrated on a wafer for massive AI workloads — *NEW concept not on wiki*
- **SoIC 3D stacking**: continued evolution
- **COUPE** (Compact Universal Photonic Engine): TSMC's photonic integration tech for high-speed, low-power optical interconnects — **direct read-through to [[SOITEC]] thesis** (Soitec substrates underpin COUPE)

### Specialty
- **N3A**: fully automotive-qualified
- **N2A**: in development
- **RRAM/MRAM**: replacing embedded flash
- **High-voltage platforms**: for smartphone + smart-glasses displays

### Implications
- **[[TSM]]**: A14 by 2028 timing aligns with [[bottleneck-roadmap]] EUV constraint period
- **[[ASML]]**: A14 nanosheet + CFET both need EUV; A14 specifically benefits from High-NA EUV — bull data point
- **[[SOITEC]]**: COUPE explicit confirmation = TSMC's photonic integration is at-scale program, not speculative — Soitec substrate demand is real
- **SoW** as a new TSMC platform = read-through to advanced packaging cohort ([[AMKR]], [[ASX]], [[CAMT]])

## Article 3: "Synopsys and TSMC Deepen AI Design Alliance: What It Means" (May 5, 2026)
**URL**: https://semiwiki.com/eda/synopsys/368839-synopsys-and-tsmc-deepen-ai-design-alliance-what-it-means/

### Key partnership data points
- **Synopsys IP silicon-proven** on TSMC 3nm + emerging 2nm-class processes
- **M-PHY v6.0**: silicon bring-up on **N2P** (first in industry)
- **64G UCIe IP** + **224G high-speed interconnect IP** tapeouts complete
- **Fusion Compiler with agentic AI** on TSMC A14 + NanoFlex Pro — "decision-guiding" AI design tools (paradigm shift from passive AI assistance)
- **3DIC Compiler**: enables CoWoS at interposer sizes **up to 5.5x reticle limit** — massive multi-die designs
- **Multiphysics simulation**: thermal/electrical/optical interactions for tightly-integrated systems
- **Automotive: UCIe IP compliant with ASIL B** on N5A — chiplet-based safety-critical designs
- **Co-packaged optics + 224G IP**: integrated with TSMC's COUPE design flow
- Support for emerging interconnect standards: optical Ethernet, **UALink**

### Strategic framing (Nenni)
> "Strategic lock-in that benefits tightly aligned partners while raising barriers for competitors."

> "Progress is no longer driven solely by transistor scaling but by the ability to coordinate across multiple layers of the technology stack, from design software and reusable IP to packaging and system integration."

### Implications
- **[[SNPS]]**: bull case reinforced — Synopsys is the design-tool gravity well for TSMC's advanced nodes; agentic AI in EDA = compounding competitive moat (especially with [[CDNS]])
- **[[TSM]]**: A14 ecosystem readiness validated; CoWoS scaling to 5.5x reticle = massive multi-die future
- **[[SOITEC]]**: COUPE design flow + 224G IP integration = third independent wiki confirmation of TSMC's CPO push (after the SOITEC company page itself and the Mii roadmap above)
- **EDA moats**: SNPS automotive TAM expansion (ASIL B chiplets) = new growth vector beyond data center

## Net wiki updates
- Patched [[TSM]] — Mii roadmap + A14/A13/A12/CFET trajectory + COUPE photonic platform
- Patched [[SOITEC]] — multiple TSMC roadmap confirmations of COUPE (the integration platform Soitec substrates serve)
- Patched [[SNPS]] — agentic AI design flow on A14; 3DIC scaling; automotive chiplet TAM
- Patched [[INTC]] — Nenni's bullish framing (March pre-Lip-Bu surge) — adds to the bull case balance on the page
- Added Rapidus mention to [[us-china-relations]] sovereign-supply theme
- No new pages — would have created Rapidus stub but it's private/sovereign-backed and not investable from public markets
