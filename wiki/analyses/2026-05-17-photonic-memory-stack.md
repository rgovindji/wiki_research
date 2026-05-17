---
type: analysis
tags: [photonics, memory, cxl, soitec, avgo, marvell, micron, infrastructure]
last_updated: 2026-05-17
last_full_review: 2026-05-17
sources: 3
status: substack-publish-ready
target_audience: tech-curious investor, semi/AI Twitter
estimated_words: 2100
---

# Photonic Memory: What's Actually Shipping in 2026 — and Who Gets Paid

*A layer-by-layer map of the AI memory + photonics stack, written for people tired of seeing "photonic memory" tickers thrown around with zero technical grounding.*

---

## The thing nobody admits

"Photonic memory" is one of the most-pitched, least-defined terms in AI infrastructure investing. The reason it gets pitched is that anyone who can credibly explain it sounds smart. The reason it stays vague is that **photonic memory, as a discrete commercial product, does not yet exist.**

What does exist — and what makes the term half-useful — is a stack of distinct technologies that are often jammed together when retail-facing accounts write tweets. Each layer of that stack has very different companies, very different unit economics, and very different time horizons. If you confuse the layers, you can buy a ticker that has nothing to do with the thesis you think you're playing.

This post is the layer-by-layer map. By the end you should be able to (a) tell a friend what each piece actually is, (b) name the public ticker at each layer, and (c) recognize when someone on Twitter is conflating things.

I am not an analyst at a firm and I do not issue ratings. The views below are research synthesis from a personal wiki I maintain. Not investment advice. I'll disclose my positions at the bottom.

---

## What the stack actually looks like

Let me start with the punchline and then walk through the layers.

**There are three separate problems people lump under "photonic memory":**

1. **Moving data between chips fast enough** (the interconnect problem). Solved with optical interconnects: pluggable transceivers today, co-packaged optics tomorrow. Not memory.
2. **Bridging compute to memory at the package level** (the memory-wall problem). This is where photonic interposers come in. Frontier territory; the most interesting "photonic-adjacent" memory architecture; barely commercial yet.
3. **Pooling memory across servers** (the inference-cost problem, especially for KV cache in LLMs). Solved electrically with CXL, not photonically. People confuse this with photonics constantly.

Below is the stack mapped layer by layer, with the public ticker that captures each piece. I'll explain each.

| Layer | What it does | Public ticker(s) | What it isn't |
|---|---|---|---|
| **Substrate** | Specialty wafer needed to fab silicon photonics chips | **SOITEC** (SOI.PA) | Not a memory company |
| **Foundry / process** | Manufactures silicon photonics ICs | **TSM** (COUPE), **TSEM** (Tower), GlobalFoundries (private) | Not chip designers |
| **EDA / design IP** | Software + IP to design photonic + electrical co-integration | **SNPS**, **CDNS** | Not hardware |
| **Pluggable optical modules** | Today's optical interconnect product (800G, 1.6T transceivers) | **COHR**, **LITE**, **FN** | Not memory; replaced eventually by CPO |
| **Co-packaged optics (CPO)** | Optics integrated into switch/compute package | **AVGO** (Tomahawk 6 + Davisson), **NVDA** (Spectrum-X / Quantum-X), **MRVL** (Teralynx) | Still interconnect, not memory |
| **Photonic fabric / interposer** | Optical bridge between compute and HBM at package level | **MRVL** (acquired Celestial AI May 2026), Lightmatter (private) | Not standalone product yet |
| **HBM (the actual memory)** | High-bandwidth electrical memory stacked next to GPU | **MU**, SK Hynix (Korea), Samsung (Korea) | Not photonic |
| **CXL memory pooling** | Shared DRAM pool across servers (electrical) | **ALAB** (retimers), **MRVL** (controllers), Samsung/Micron CZ120-class modules | Not photonic |
| **Photonic memory storage** | Storing bits as light (phase-change materials, etc.) | None public. IBM, Oxford research stage. | Doesn't exist commercially |

---

## Layer 1: The substrate — Soitec

Every silicon photonics chip starts with a specialty wafer called **photonics-grade silicon-on-insulator (photonics-SOI)**. It's not the same as regular SOI used for RF chips or FD-SOI used for low-power processors. The photonic version has a precisely-engineered thin buried-oxide layer that lets light propagate without leaking.

There is essentially one company in the world qualified to supply this wafer at volume to all three major foundries (TSMC, GlobalFoundries, Tower Semiconductor): **Soitec**, a French company listed on Euronext Paris as **SOI.PA**. BofA estimates Soitec holds ~95% market share of photonics-grade SOI as of March 2026. Shin-Etsu has a license but minimal volume. GlobalWafers' license was terminated.

If you want to play the photonics-substrate layer, this is the only public name. Note: SOI.PA is Paris-listed only — no US ADR. The stock has rallied ~6x off its December 2025 low, so you're not buying it cheap. Their FY26 earnings May 27 are binary — that's the visibility event.

---

## Layer 2: The foundry — TSMC COUPE, Tower, GlobalFoundries

Once you have the substrate, you need a foundry to turn it into chips. Three players matter:

**TSMC's COUPE** — Compact Universal Photonic Engine. This is TSMC's silicon-photonics platform for co-packaged optics. Per TSMC SVP Y.J. Mii's April 30 Technology Symposium presentation, **COUPE enters production in 2026 with approximately 2x power efficiency vs. pluggable optical modules**. That's a real, public, technical claim. COUPE is part of why every NVDA, AVGO, and MRVL roadmap converges on co-packaged optics for 2026-2028.

**Tower Semiconductor (TSEM)** — Israeli specialty foundry, listed on NASDAQ. Long-time photonics fab. Intel attempted to acquire Tower in 2022; the deal collapsed on China regulatory delay in mid-2023. Tower fabs photonic ICs for a wide customer base — they're foundry to other people's designs, not a design house themselves.

**GlobalFoundries (GFS)** — runs their **SCALE platform** targeting $1B+ silicon photonics revenue by 2028. Less marketed than TSMC but real.

All three buy substrate from Soitec. All three are foundries — they don't sell consumer-facing products; they sell wafer space to other companies.

---

## Layer 3: The design layer — Synopsys + Cadence

You can't design a co-packaged optical chip without specialized EDA software. The two majors that matter are:

**Synopsys (SNPS)** — has silicon-proven IP validated on TSMC N2P (M-PHY v6.0); 64G UCIe IP and 224G high-speed interconnect IP. SNPS Fusion Compiler integrates with TSMC's A14 + COUPE design flow.

**Cadence (CDNS)** — Virtuoso Studio + Celsius Thermal Solver + Sigrity for signal/power integrity at the photonic-electrical interface. Cadence supports the same TSMC COUPE design flow.

Neither is a "photonics pure-play." They're EDA duopoly names that capture rent at every node + every photonic design done at TSMC/GF/Tower. They're cleaner exposure than retail-pitched "photonic memory" tickers because they get paid regardless of which CPO architecture wins.

---

## Layer 4: Today's optical interconnect — pluggables (COHR, LITE, FN)

For the last decade, optical communication between racks (and increasingly within racks) has used pluggable optical modules. They look like little cassettes that plug into a switch. The big public names:

- **Coherent (COHR)** — NVDA made a $2B direct equity investment (alongside Lumentum) in March 2026.
- **Lumentum (LITE)** — paired with Coherent in the same NVDA investment.
- **Fabrinet (FN)** — contract manufacturer for transceivers across the industry.

These are real businesses with real revenue and real growth. But the technology trajectory is replacing them with co-packaged optics over the next 3-5 years. Owning COHR/LITE/FN today is buying the late-cycle of the pluggable era. The thesis is roughly: pluggables expand into 1.6T and 3.2T data rates before being displaced; revenue compounds at attractive rates through 2027-2028; new growth post-2028 depends on whether they can pivot into CPO components.

---

## Layer 5: Co-packaged optics (the actual present-tense innovation)

Co-packaged optics (CPO) is the architecture that replaces pluggables. Instead of plugging optical cassettes into a switch, the optical engine is integrated into the same package as the switch ASIC. Lower latency, lower power, higher density.

The three companies that matter:

- **NVIDIA** — Spectrum-X (Ethernet CPO) launched mid-2025; Quantum-X (InfiniBand CPO) earlier 2026. Both are in production.
- **Broadcom (AVGO)** — Tomahawk 6 (102.4 Tbps) shipping with 200G/lane CPO. Counterpoint projects AVGO captures 60% of custom hyperscaler ASIC by 2027.
- **Marvell (MRVL)** — Teralynx switching silicon plus the May 2026 acquisition of Celestial AI's Photonic Fabric (more on that below).

All three buy photonic ICs fabbed on Soitec substrates at TSMC COUPE / Tower / GlobalFoundries. AVGO is the cleanest pure-AVGO-share exposure to non-NVDA AI silicon as well — owning AVGO is partially a CPO play and partially a custom-ASIC play.

---

## Layer 6: The thing most retail-pitched "photonic memory" stocks are confused about

Here's where the term gets earned, or doesn't. **Celestial AI** is a private company (now Marvell, after the May 2026 acquisition) that built something called **Photonic Fabric**. It's an optical interposer that bridges compute (a GPU or AI accelerator) to memory (HBM) at the package level using light instead of copper traces.

This is the closest commercial architecture to what people mean when they say "photonic memory." It's not photonic memory in the literal sense of "storing bits as photons." It's a photonic *interconnect to memory* at the package level. The reason it matters is the memory wall — modern AI inference is bottlenecked on how fast you can move data between compute and memory, and optical interposers do this faster and with lower energy than electrical interconnect at the same scale.

**Marvell acquired Celestial AI in May 2026.** That's a real, recent, fundamental change to the public market exposure for this layer. If you want to be long the photonic-memory-adjacency, MRVL is the ticker. Not some random ticker someone pitched you. The market hasn't fully priced this acquisition into MRVL's narrative yet — most analysts cover MRVL as "custom ASIC + DPU + storage" and treat the photonic fabric as optionality. That's where the alpha is.

Lightmatter is the other private name. They focus more on optical compute than optical interconnect to memory, but the lines blur.

---

## Layer 7: The actual memory (which is electrical)

In every AI system shipping in 2026, the actual memory is electrical. The two technologies that matter:

**HBM (High-Bandwidth Memory)** — stacked DRAM placed next to the GPU/accelerator on the same package. Three suppliers:
- **Micron (MU)** — preferred supplier on NVDA Vera Rubin; shipping 12-high 36GB HBM4 in volume Q1 2026.
- **SK Hynix** (Korean, accessible via Korea Stock Exchange or 000660.KS)
- **Samsung** (Korean, 005930.KS) — closing the HBM4 gap fast per ISSCC 2026.

HBM is sold-out for 2026; the market is pricing per generation, not per quarter. HBM4 specifically is the cycle most relevant for Vera Rubin and AMD Helios deployments through 2027.

**CXL memory pooling** — the parallel track most "photonic memory" confusion stems from. CXL (Compute Express Link) is an open standard that lets servers share a pool of DRAM. Critical for inference workloads, especially KV cache.

For the un-initiated: **KV cache** is the memory store for attention computations in transformer inference. As context windows grow (10K → 100K → 1M tokens), the KV cache grows in proportion. At million-token contexts, you can't keep the KV cache in HBM — you need to offload to a larger but slower memory pool. CXL pools DDR5 across multiple servers; latency is higher than HBM but cost-per-GB is 3-5x lower.

The public CXL plays:
- **Astera Labs (ALAB)** — pure-play CXL retimers and switches. Pre-IPO darling, now public.
- **Marvell (MRVL)** — CXL controllers (in addition to the photonic fabric piece).
- **Samsung / Micron / SK Hynix** — CXL-class memory modules (Samsung's CZ120, Micron's CZ12x-line).

CXL memory pooling is not photonic. Anyone pitching "photonic memory pooling" or similar buzzword constructs is confusing layers.

---

## What about actual photonic memory storage?

There are research groups working on **storing bits as light** using phase-change materials with optical read/write — IBM, Oxford University, several startups. The technology is called photonic phase-change memory (P-PCM) or similar variants. It has theoretical bandwidth advantages but is not commercial. No public ticker. If someone pitches you a stock based on photonic memory storage, ask them whether the company has a shipping product. The answer in 2026 is no.

This is the layer that gives the term "photonic memory" its mystique — the future where bits are stored as light — but it's a 2030+ commercial horizon, if ever.

---

## So who actually gets paid in 2026-2028?

Three tiers, ranked by visibility of revenue:

**Tier 1 — already getting paid (cleanest 2026 plays)**:
- HBM cycle: **MU** (preferred) and SK Hynix/Samsung (Korean exposure)
- CXL ramp: **ALAB** (pure-play retimer leader)
- EDA backbone: **SNPS** + **CDNS** (every node, every design, photonic and electrical)
- Pluggable optics late cycle: **COHR**, **LITE** (NVDA-invested, but losing share to CPO over time)

**Tier 2 — 2026-2027 production inflection**:
- Substrate: **SOITEC** (95% photonics-SOI share; TSMC COUPE production starts 2026)
- CPO platform owners: **AVGO** (Tomahawk 6 + Davisson), **NVDA** (Spectrum-X/Quantum-X)
- Foundry exposure: **TSM** (the COUPE itself), **TSEM** (specialty foundry)

**Tier 3 — frontier / under-priced (2027-2030 horizon)**:
- Photonic interposer (the closest thing to "photonic memory"): **MRVL** (post-Celestial AI acquisition May 2026)
- True photonic memory storage: no public name

The single most under-priced position on this list is **MRVL post-Celestial acquisition**. Most sell-side coverage treats MRVL as "custom silicon + DPU + storage" and either ignores or applies modest optionality value to Photonic Fabric. If photonic interposers become the standard memory-bridge architecture for AI clusters by 2028 — which is what AVGO, NVDA, and TSMC's roadmaps all imply — Marvell's acquisition begins to look like a bargain. Risk: the integration takes longer, or AVGO/NVDA build internal photonic-interposer capability and bypass MRVL's IP.

---

## How to spot bad pitches

A few patterns to recognize:

- **"$PENG is a photonic memory play"** — Penguin Solutions (PENG) is a systems integrator and advanced memory module supplier. They sell AI factory systems and memory modules including CXL-capable products. They are not a photonic memory IP holder. Conflating systems integration with substrate or fabric IP is the most common confusion.

- **"$SMCI is photonics-adjacent"** — Super Micro is an NVDA server integrator. They put GPUs in racks. They have nothing to do with photonics IP. Owning SMCI is owning the integrator margin on NVDA's growth, not photonic memory.

- **"$TSEM is the photonic memory play"** — Tower is a foundry for photonic ICs. They fab other people's designs. They do not hold photonic memory IP. Owning TSEM is owning capacity rent on the foundry side, not the technology rent on the IP side.

- **"$RKLB is photonic memory"** — Rocket Lab is a launch company. There is no photonic memory thesis on a launch company. Anyone making this claim is throwing buzzwords.

The pattern: if a ticker doesn't fit into one of the boxes in the table above, that's because there's no actual thesis. Photonic memory does not run through random AI-adjacent tickers; it runs through specific layers with specific companies.

---

## What I'd do with this

I'm not telling you what to buy. But here's how I'd think about it if I were positioning around the photonics + memory thesis:

1. **HBM cycle** is the highest-conviction near-term play. Own **MU** as the US-listed leverage to it.
2. **Substrate-layer rent** is captured by **SOITEC** (Paris-listed; valuation tight after 6x rally; May 27 earnings is the binary).
3. **CPO leaders** are **AVGO** (60% custom ASIC share + Tomahawk 6 CPO) and **NVDA** (vertical control via Spectrum-X).
4. **Photonic fabric optionality** is at **MRVL** post-Celestial acquisition — under-discussed on the sell side.
5. **CXL memory pooling** is at **ALAB**; cleanest pure-play.
6. **Skip the buzzword tickers** (PENG, SMCI, RKLB-as-photonics, etc.) — they don't capture the rent layer the marketing implies.

---

## Disclosures and disclaimers

I maintain a personal investing research wiki covering AI, semis, robotics, space, defense, and adjacent themes. I hold positions in some of the names mentioned above; I am considering a position in Soitec but have not yet bought it. I have no relationship with any of the companies covered. This post is research synthesis, not investment advice. Markets are dynamic; numbers move; theses break. Verify everything before any decision.

Sources for specific data points:
- Soitec photonics-SOI market share: BofA equity research (March 2026)
- TSMC COUPE production timing + 2x power efficiency: TSMC SVP Y.J. Mii Technology Symposium 2026, April 30
- Marvell-Celestial AI acquisition: multiple trade press confirmations May 2026
- AVGO Tomahawk 6 CPO: AVGO Q1 FY26 earnings commentary
- HBM4 Q1 2026 shipment to NVDA Vera Rubin: Micron disclosures + TrendForce
- ALAB role in CXL: Astera Labs S-1 + recent quarterly earnings

If you want the wiki entries on any of these, message me and I'll share the relevant page.

---

*Posted Sunday May 17, 2026.*
