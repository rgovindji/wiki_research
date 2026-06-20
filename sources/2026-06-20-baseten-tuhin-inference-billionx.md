---
date: 2026-06-20
type: podcast
publisher: Stanford ("Economics of AI" class talk/interview)
url: https://www.youtube.com/watch?v=Qh7Oxvo5sJI
raw_path: raw/podcasts/2026-06-20-baseten-tuhin-inference-billionx.txt
touches: [inference-economics, ai-capex-cycle]
---

# Tuhin Srivastava (Baseten founder/CEO) — "Inference is about to go up a billion x" (Stanford)

> **Bias flag — heavy.** Baseten is a **private** AI-inference-infrastructure company (~7 yrs old). Tuhin is talking his book end to end: his entire thesis *requires* (a) inference demand exploding, (b) an independent application layer existing, and (c) open-weight models staying good enough to post-train. He is also a *buyer* of GPUs, so his "supply is 10× worse than people say / prices doubling" framing both reflects real operator pain **and** serves his pitch (and his coming move into owning compute). He explicitly named these as Baseten's three existential risks — treat them as the falsifiers. No price targets given; none invented here.

## TL;DR
- **Baseten claims it already serves ~30 trillion tokens/day** — bigger than the OpenAI *API* product (not ChatGPT) and bigger than the Gemini API, per its last read. Projects needing **~150k B200-equivalents in ~2 years ≈ ~$7B of compute spend.** (Self-reported, unverifiable, private — but a striking demand data point if even directionally true.)
- **The custom/open-weight wedge:** today ~90-95% of inference spend goes to frontier models, ~5% to open-source / post-trained models. Baseten's bet is that share inverts as apps chase gross margins — the bigger/more-scaled the customer, the *more existential* moving off frontier tokens becomes.
- **Compute scarcity is worse than advertised and "never going to normalize."** A B200 cluster repriced **$263/hr → $510/hr (≈2×) at renewal**; new 1,000-GPU orders quote **~Q2 next year (12-15 months out)**; Google Cloud cited with a "~10× backlog." This is why Baseten is shifting from pure-rent toward **own** (≈30% cheaper, "Oracle-like 30% gross margins").
- **NVIDIA dominance is near-total for now** — majority of fleet on NVIDIA; CUDA + TRT-LLM/vLLM/SGLang ecosystem = "the ability to move fast." Heterogeneous (disaggregated prefill/decode) is the *future* state, not the present.

## Key facts / claims (with confidence)
- **~30T tokens/day; "bigger than the OpenAI API and Gemini API."** *Low-medium confidence — self-reported, private, "at least in last report."* If true, a large independent inference operator hidden from public comps.
- **~$7B compute spend / ~150k B200-equivalents in ~2 yrs.** *Medium — his own projection, directionally useful for [[ai-capex-cycle]] demand scale.*
- **Frontier vs open/post-trained spend mix ~90-95% / ~5%, expected to invert.** *Medium — directional; the whole thesis rides on this drift, which is the same number [[inference-economics]] flags as undecided.*
- **Open-weight lag ~90 days behind frontier; 70-90% cheaper to run.** *Medium.* Slightly wider than Dwarkesh/Epoch's ~4 months but same order; the 70-90% cheaper figure matches the Nebius routing demo in [[inference-economics]].
- **GPU repricing: B200 cluster $263→$510/hr at renewal; new orders ~Q2 next year; GCP ~10× backlog.** *Medium-high — concrete operator anecdotes, dated (renewal in October, quote received May).* Strongest data point: a hard, recent, doubling of rental compute price.
- **Own vs rent ≈ 30% cheaper; moving to owning compute + buying direct from chip vendors to *guarantee* access.** *High confidence (stated strategy).* Note: a private inference firm following the [[CRWV]]/Crusoe capex-and-own path — adds to the demand bid for NVIDIA + power + data centers.
- **Best open-weight models today come from China (Moonshot/Kimi, Alibaba/Qwen, MiniMax, DeepSeek); US open-weight was *decreasing* until ~a year ago, now upticking** (Google Gemma, NVIDIA Nemotron, Reflection AI). *Medium — opinion, but a real strategic-risk framing; calls it a national-security issue if "cost of intelligence is 70-90% cheaper in the East."*
- **Multi-cloud as moat:** Baseten stitches compute across **18-20 clouds / 87 clusters**, making GPU fungible. *High (operator detail).* Implies neocloud commoditization at the raw-compute layer — value is in the software/orchestration stack on top.
- **Inference is sticky, not a commodity** — "like buying databases: choose once and grow there"; if inference is down, the customer's product is down. *Opinion; self-serving but plausible.*
- **Heterogeneous compute is coming via prefill/decode disaggregation** (memory-bound decode vs compute-bound prefill on different chips); cites NVIDIA's Grok-chip acquisition; Etched/Positron/d-Matrix/SambaNova/Cerebras/Groq as the long tail. *Medium — directional, matches Katti's heterogeneous-compute point in [[inference-economics]].*

## The contradiction / tension to surface (not resolve)
- **On the open-weight moat, Tuhin sits with Dwarkesh, against Katti.** His ~90-day lag + "the larger you are, the more existential it is to move off frontier tokens" is the *thin/perishable-moat, share-inverts* view. But note his self-stated antithesis: "there are only two players who can get compute, and they own everything" + "not enough good open-source models" — i.e. he concedes the bear case to his own thesis is exactly Katti's bull case. Filed as a live both-sides in [[inference-economics]].
- **"Reasoning tier barely monetized" tension:** Tuhin's frame is the *opposite* angle — frontier labs' incentive is to push the capability gap and keep pricing the most expensive model, so they *won't* seriously invest in post-training/open-weighting their lagging models ("every dollar should go to pre-training if you believe AGI"). Supports the [[inference-economics]] read that the lab layer's pricing power is a *strategic choice*, not a moat fact.

## Quotes worth keeping
> "We do around 30 trillion tokens a day… the Baseten inference service is bigger than the OpenAI API, bigger than Gemini."
> "No matter how much people tell you there's a supply problem, it is 10 times worse."
> "They came to us already in May and said $510 is the new price — double." (B200 cluster renewal, was $263/hr.)
> "I don't think it's ever going to normalize… there's no reset period. It just keeps compounding." (on compute scarcity)
> "We're the West India Company. We are the rebellion." (on whether labs are the "East India Company" extracting customers' workflow data)
> "If you truly believe the AGI thesis and play it out, we all have nothing to do — but then inference is the only market left."
> "The best open source models today are coming from China."

## Wiki updates suggested (NOT made — per instruction, source summary only)
- Patch [[inference-economics]]: add Tuhin as a **fourth source** corroborating (a) open-weight ~90-day lag + 70-90% cheaper, (b) model-routing/share-inversion thesis, (c) the harness/software-as-sticky-layer vs raw-compute-commoditizes split, (d) heterogeneous prefill/decode disaggregation. Add to the moat-debate table on the *perishable-moat* side. Add the "labs won't post-train their laggards because it concedes the AGI thesis" point under "reasoning tier / lab pricing is a strategic choice."
- Patch [[ai-capex-cycle]]: the **2× B200 rental repricing, ~12-15mo GPU lead times, GCP ~10× backlog, $7B/150k-B200 self-projection**, and a private inference firm moving rent→own — all reinforce supply-constraint + demand-scale.
- Consider a future page on **modular/standardized data centers** ("API for compute," container analogy) — Tuhin's pick for the next big buildout business; also flags **data-center project finance** as a hot area.
- Watch-only entity: **Baseten** (private) — possible IPO candidate / private comp for inference demand; do not create a company page (no public ticker).
