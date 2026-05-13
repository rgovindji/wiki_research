# Investing Wiki

A personal LLM-maintained knowledge base for **long-term equity research**, focused on AI / semiconductor / data-center infrastructure.

The pattern is from [the LLM Wiki idea](https://chrlschn.dev/blog/2025/01/llm-wiki/): an LLM agent maintains a persistent, interlinked collection of markdown files instead of re-discovering knowledge on every query. The wiki compounds as new sources arrive; cross-references stay current; contradictions are flagged rather than silently overwritten.

> **Not investment advice.** This is a research artifact, not a recommendation system. Stances are research stances. Numbers are dated and should be verified before any decision. See [DISCLAIMER.md](./DISCLAIMER.md).

## Quick start

1. **Read [`wiki/overview.md`](./wiki/overview.md)** — top-level synthesis (current macro stance + leading theses).
2. **Browse [`wiki/watchlist.md`](./wiki/watchlist.md)** — active buy / hold / avoid candidates.
3. **Drill into [`wiki/companies/`](./wiki/companies/)** — one page per ticker.
4. **Open `market_overview_ai.html` or `dashboard.html`** in any browser — self-contained HTML artifacts with hover/tap tooltips, market caps, and bull-case scenarios for 2027/2028.

## Repository structure

```
CLAUDE.md          — schema / operating manual for the LLM maintainer
index.md           — catalog of every wiki page
log.md             — chronological log of ingests, queries, lints

wiki/
  overview.md            — top-level synthesis
  watchlist.md           — active candidates
  companies/             — one page per ticker
  sectors/               — semiconductors, cloud-hyperscalers, etc.
  themes/                — ai-capex-cycle, bottleneck-roadmap, etc.
  macro/                 — fed-policy, valuation-environment, inflation-tariffs
  concepts/              — generic concepts (mostly empty; populated on demand)
  analyses/              — ad-hoc deep dives

sources/
  YYYY-MM-DD-slug.md     — one summary per ingested external source

raw/                     — (gitignored) source material; not redistributed

market_overview_ai.html  — research memo (Claude design)
dashboard.html           — scan-mode dashboard (Linear design)
tooltips.js              — shared tooltip data + runtime (inlined into both HTML files)
```

## How it works

The LLM ingests new sources (articles, podcast transcripts, filings), summarizes them under `sources/`, and updates the relevant wiki pages — flagging contradictions and adding cross-links. The schema in [`CLAUDE.md`](./CLAUDE.md) tells the LLM how to do this consistently.

Designed for use with [Claude Code](https://docs.claude.com/en/docs/claude-code/) or any LLM coding agent. Could also be browsed in [Obsidian](https://obsidian.md/) (the wiki uses Obsidian-style `[[wiki-links]]`).

## License

MIT — see [LICENSE](./LICENSE).
