---
date: 2026-06-20
type: podcast
publisher: Simon Willison — High Leverage (Heavybit), host Joe Ruscio
url: https://www.youtube.com/watch?v=D76X-96tpTY
raw_path: raw/podcasts/2026-06-20-t6-simon-willison-coding.txt
touches: [inference-economics, ai-bubble-debate, ai-capex-cycle, MISTRAL, NVDA]
---

# Simon Willison — The AI Coding Paradigm Shift (~Jun 2026)

## TL;DR
- **November 2025 was the tipping point: coding agents became "reliable partners."** Claude Opus 4.5 + GPT-5.1 shipped near-simultaneously; "working code 9 out of 10 times." Peers now report **70–80% of their code is agent-written.** Cause: Anthropic + OpenAI spent *all of 2025's compute budget* on RL against simulated software. — **Hard developer ground-truth on adoption + unit-economics inflection.**
- **The pricing honeymoon is ending — Q1 2026 finance reviews triggered it.** Two big price hikes "this week": Opus 4.7 = same nominal price but ~1.4× tokens (an invisible ~40% bump); **GPT-5.5 = 2× the price of GPT-5.4.** Heavy coding-agent users burn ~100× the tokens of 2024 chat users. → enterprises must shift from token-maxing to **cost-per-outcome**. Directly confirms the wiki's CIO-cost-backlash thesis.
- **Open-weight is a real pricing anchor:** DeepSeek ~20× cheaper than Claude Opus on API, "not 20× worse on benchmarks"; runs on your own hardware. Qwen 3.6 (~627B-class, runs in ~20GB) feels like a frontier model from ~6–12 months ago and **runs on a MacBook Pro.** — **The single most concrete open-weight-moat datapoint in the cluster.**

## Key facts / claims (with confidence)
- **Coding has unusually clean RL reward signals** ("did the code work? yes/no") — the perfect RL fit; law/writing have 6-month feedback loops. *High confidence — the structural reason coding led.*
- **Why XAI / Gemini fell behind: they didn't spend 2025 on coding-RL loops** (firing up ~10,000 VMs with Python interpreters to grade generated code; acknowledged in a Qwen paper). Both now "doubling down" but ~12 months behind. Willison expects **Gemini to close the coding gap by end-2026.** *His read; dated, falsifiable catalyst.*
- **Chinese open labs: ≥5 competitive, ~3–6 months behind frontier closed models.** *High confidence — his explicit beat for 18 months.* — Brackets the moat-debate lag (vs Dwarkesh ~4mo, Ross ~6mo, Katti "6mo enormous").
- **The labs leapfrog each other constantly → committing to one vendor is shortsighted;** Willison runs an abstraction layer (his `llm` tool). Multi-model / model-routing is the rational enterprise posture. *His practice — confirms wiki's routing thesis.*
- **Human review was the hidden rate-limiter between dev and prod; removing it breaks the whole SDLC** (design, PM, spec processes were all built around code being expensive). *Sharp structural observation.*
- **Software-is-dead is wrong; public software multiples are over-punished.** Custom software for a butcher shop was never economically viable; enterprises still buy cohesive, *proven* (battle-tested) data layers + security. → bearish the "SaaS goes to zero" narrative; the right design is a hardened core schema/API with vibe-coded UI on top. *His thesis — bull-case nuance for software equities.*
- **AI's public approval is cratering** (sub-20% in some polls, "less popular than ICE," worst among heavy-using Gen Z); data-center backlash is the physical lightning rod. *Reported; a real reputational/regulatory-risk signal for the buildout.*
- **Per-token pricing is now universal** (GitHub Copilot + Windsurf abandoned flat per-request pricing because one prompt can run 10 min). *High confidence.*

## Quotes worth keeping
> "Both of those companies are doubling down on the coding side … but they're 12 months behind."
> "DeepSeek is what, 20 times cheaper than Claude Opus, and on benchmarks it's not 20 times worse."
> "I thought I needed $50,000 worth of server GPUs to run a model as good as the best ones a year ago, and now it's fitting on my MacBook Pro."
> "The entire software development life cycle was designed around the idea that it takes a day to produce a few hundred lines of code. And now it doesn't."
> "There's no world in which [a token-maxing leaderboard] ends well."

## Bias flags
- **Independent practitioner/journalist** (Django co-creator; blog simonwillison.net). Self-styled "middle of the road" beat = "what can it actually do today." **Lowest-bias source in the cluster.** No frontier-lab employment, no disclosed equity book. One foot in the VC world via the host (Heavybit; mentions portfolio co exe.dev) — note the soft promotional moments but they don't color the model claims.
- Currently *critical* of Anthropic's Claude Code pricing changes and migrated to OpenAI Codex — a usage preference, flag it as a real-time pricing-power signal (heavy user churning on price) rather than neutral product review.

## Wiki updates suggested
- Patch [[inference-economics]]: (1) **Nov-2025 reliability tipping point + dated price hikes (Opus 4.7 ~+40% effective, GPT-5.5 2×)** = the clearest evidence yet that the cost-backlash phase has *arrived*; (2) DeepSeek ~20×-cheaper and Qwen-on-a-laptop are the hardest open-weight-moat datapoints — add to "open-weight gap-closing" and "who captures margin"; (3) multi-model abstraction-layer practice confirms model-routing as standard.
- Patch [[ai-bubble-debate]]: Willison's "software-is-dead is wrong / multiples over-punished" is a *bullish-for-software* counter to the derate; pair with the AI-approval-cratering / data-center-backlash reputational risk.
- Patch [[ai-capex-cycle]]: 2025 = "all compute went to coding-RL" explains the coding lead and the XAI/Gemini lag; **Gemini-closes-coding-gap-by-end-2026** is a dated, falsifiable catalyst to track.
- Touch [[MISTRAL]] / open-weight: ≥5 Chinese labs at 3–6 months behind = the open-weight catch-up evidence base.
