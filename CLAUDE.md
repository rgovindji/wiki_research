# Investing Wiki — Schema

This file is the operating manual for the LLM agent maintaining this wiki. The user (rgovindji) is the curator and reader; the LLM (Claude) writes and maintains every page in `wiki/`.

## Purpose

A persistent, compounding knowledge base for **long-term equity investing with tactical 6-18 month swings**. The user is researching what to **buy, hold, or sell** with a primary focus on:

1. **Tech & AI sector deep dive** — semis, hyperscalers, AI software, infrastructure
2. **US large-cap (S&P 500)** — Magnificent Seven and adjacent leaders
3. **Global / international** — TSMC, ASML, and other non-US AI/tech beneficiaries

The wiki is not a recommendation system. It is a synthesis of evidence and debate. The user makes decisions; the wiki keeps them informed.

## Architecture

Three layers:

- **`raw/`** — immutable source documents. Articles, filings, PDFs, images. Never edited.
- **`wiki/`** — LLM-written markdown. Owned by the LLM. The compiled, cross-linked synthesis.
- **`sources/`** — one short summary page per ingested raw source. Bridges raw and wiki.

Plus two index files at the repo root:

- **`index.md`** — content catalog. Updated on every ingest.
- **`log.md`** — append-only chronological log of ingests, queries, lints.

## Directory layout

```
raw/
  articles/      # web articles (markdown via Obsidian Web Clipper or .txt paste)
  filings/       # 10-K, 10-Q, 8-K, S-1
  reports/       # analyst PDFs, broker research, whitepapers
  podcasts/      # transcripts (.txt or .md)
  assets/        # images, charts, screenshots referenced from articles
sources/         # one .md per raw source — short summary + key takeaways + links to wiki pages it touched
wiki/
  overview.md            # top-level synthesis: current macro stance + leading theses
  watchlist.md           # active buy/sell candidates with thesis + trigger
  companies/             # one page per ticker (UPPERCASE filename, e.g. NVDA.md)
  sectors/               # semiconductors, cloud-hyperscalers, ai-software, etc.
  themes/                # cross-cutting drivers (ai-capex-cycle, market-concentration)
  macro/                 # fed-policy, inflation-tariffs, valuation-environment
  concepts/              # generic concepts (forward-pe, free-cash-flow, moats)
  analyses/              # comparison tables, screens, ad-hoc deep dives
```

## File naming

- **Tickers**: uppercase, no exchange prefix. `NVDA.md`, `GOOGL.md`, `TSM.md` (Taiwan Semi ADR), `ASML.md`.
- **Sectors / themes / concepts / macro**: kebab-case. `ai-capex-cycle.md`, `fed-policy.md`.
- **Source summaries**: `YYYY-MM-DD-slug.md`. Example: `2026-05-09-dwarkesh-dylan-semianalysis.md`.

## Cross-linking

Use **Obsidian-style wiki links**: `[[NVDA]]`, `[[ai-capex-cycle]]`, `[[fed-policy|Fed]]`. Obsidian resolves these by basename across the vault, so no relative paths needed. Use `|` for display aliases.

Every page should link to:
- Pages it depends on (e.g. NVDA links to `[[ai-capex-cycle]]`, `[[semiconductors]]`)
- Pages that reference it (back-links happen automatically in Obsidian)

## Frontmatter

Every wiki page starts with YAML frontmatter:

```yaml
---
type: company | sector | theme | macro | concept | analysis | overview | watchlist
ticker: NVDA            # only on company pages
tags: [ai, semis, mag7]
last_updated: 2026-05-09
last_full_review: 2026-05-09   # last time the page was rewritten end-to-end (not just patched)
sources: 3              # count of source summaries that have touched this page
conviction: high | medium | low | n/a   # only on company / theme pages
stance: bull | bear | neutral | n/a     # only on company pages
---
```

`last_full_review` matters: small patches drift. When a page hasn't had a full review in >90 days or after >5 patches, schedule one in lint.

## Page templates

### Company page (`wiki/companies/TICKER.md`)

```markdown
# {Company} ({TICKER})

**Stance:** bull / bear / neutral · **Conviction:** high / medium / low · **Time horizon:** long-term / 6-18mo / both

## One-line thesis
{One sentence. The reason to own this or avoid it.}

## Snapshot
| Metric            | Value         | As of     |
| Market cap        | $X.XT         | YYYY-MM-DD |
| Forward P/E       | XX.X          | YYYY-MM-DD |
| Revenue (TTM)     | $XX.XB        | YYYY-MM-DD |
| Rev growth (YoY)  | XX%           | YYYY-MM-DD |
| Gross margin      | XX%           | YYYY-MM-DD |
| FCF (TTM)         | $XX.XB        | YYYY-MM-DD |

## Bull case
- ...

## Bear case / risks
- ...

## Key questions / what to watch
- ...

## Recent developments
- {YYYY-MM-DD} — {event}. From `<source-summary-slug>`.

## Related
{ai-capex-cycle} · {semiconductors} · {market-concentration}   ← use real Obsidian-style double-bracket wiki-links in actual pages

## Sources
1. `<source-summary-slug>`
2. [URL] — title
```

### Theme / sector / macro page

```markdown
# {Title}

## What this is
{1-2 sentences.}

## Why it matters now
{Why this is investable / live, as of {date}.}

## Key drivers
- ...

## Beneficiaries
- [[NVDA]] — ...

## Risks / counter-thesis
- ...

## Open questions
- ...

## Related
{related-page} · {another-page}   ← use real Obsidian-style double-bracket wiki-links in actual pages

## Sources
- ...
```

### Source summary (`sources/YYYY-MM-DD-slug.md`)

```markdown
---
date: 2026-05-09
type: article | filing | report
publisher: Goldman Sachs
url: https://...
raw_path: raw/articles/goldman-2026-outlook.md   # if saved locally
touches: [overview, valuation-environment, NVDA]
---

# {Title}

## TL;DR
{3 bullets.}

## Key facts
- ...

## Key claims (and how confident)
- ...

## Quotes worth keeping
> "..."

## Wiki updates made
- Updated [[overview]] target prices
- Added bull-case bullet to [[NVDA]]
- Created [[market-concentration]]
```

## Workflows

### Ingest a new source

1. **Read** the raw source thoroughly (or fetch via WebFetch if it's a URL).
2. **Discuss** key takeaways with the user before writing — confirm what's important.
3. **Write `sources/YYYY-MM-DD-slug.md`** — the canonical summary.
4. **Update wiki pages** the source touches. Update existing pages rather than creating new ones, unless a genuinely new entity / theme / concept appears. A single source typically touches 5-15 pages.
5. **Flag contradictions** explicitly. If a new source disagrees with an existing claim, do not silently overwrite. Add a "Contradicting evidence" subsection with both views and a date — the user decides.
6. **Update `index.md`** — add new pages, bump source counts.
7. **Append to `log.md`** — see format below.

### Answer a query

**Retrieval is mandatory before reasoning. Never answer from general knowledge or from
whatever happens to be in context — the wiki holds 300+ pages no single session can hold.**

1. **Recall first — always run `python3 scripts/wikidb.py ask "<the question>"`.** This is hybrid
   (lexical + semantic) retrieval over every wiki page and source summary; it auto-refreshes the
   index first and returns the most relevant dated, cited passages with conviction/stance. Run it
   *before* forming any view. Rephrase and re-run for distinct sub-questions.
2. **State what the wiki already knows** — briefly list the relevant prior claims the recall
   surfaced (with their dates/sources) before adding anything new. If recall returns a position
   the wiki already holds, build on it; do not silently re-derive a fresh "general" take.
3. **Read the full pages** behind the top passages (and the sources they cite) when depth is needed.
   Use `index.md` only as a secondary map when recall is thin.
4. **Synthesize** an answer with citations to wiki pages and source summaries. Only then layer in
   fresh WebSearch for anything dated within the last 30 days.
5. **Ask the user** if the answer should be filed back as a new page in `wiki/analyses/`. Good queries become permanent assets.
6. **Append to `log.md`**.

### Lint pass

Run when asked, or proactively when the wiki has grown by ~10 sources since the last lint.

Check for:
- **Contradictions** between pages (two pages making opposite claims about the same fact)
- **Stale claims** — pages whose `last_updated` is >60 days old AND that reference live metrics (price, multiple, growth rate) that have likely moved
- **Stale full reviews** — pages with `last_full_review` >90 days old or with >5 patches since the last full review
- **Orphan pages** — pages with no inbound wiki links
- **Implicit entities** — a ticker mentioned in 3+ pages that doesn't have its own page yet
- **Missing cross-references** — pages that should link but don't (e.g. NVDA not linking to `[[ai-capex-cycle]]`)
- **Source gaps** — claims with no citation, or themes covered by <2 sources

Output a lint report. Do not auto-fix; let the user decide what to act on.

## `log.md` format

Append-only. Each entry starts with this exact prefix so `grep "^## \[" log.md` works:

```
## [YYYY-MM-DD] {ingest|query|lint|note} | {short title}
```

Example:
```
## [2026-05-09] ingest | <Title of source>
- Source: sources/<slug>.md
- Wiki touched: overview, valuation-environment, NVDA, GOOGL
- Notes: <key takeaway and how it changed the wiki>
```

## Conventions and house rules

- **Always cite.** Every non-obvious claim links to a source summary or external URL.
- **Date everything.** Metrics, prices, claims — include the as-of date inline. Markets move; undated facts rot.
- **Bull and bear, always.** Every company page must have a real bear case. If you can't write one, you don't understand the position.
- **No price targets without source.** Do not invent or estimate price targets. Cite analyst targets verbatim with attribution and date.
- **Conviction is honest.** Mark `conviction: low` when the evidence is thin. Do not inflate.
- **Contradictions are surfaced, not resolved.** When sources disagree, show both. The user resolves.
- **Update don't append.** When new info supersedes old, edit the claim and add a note in "Recent developments" — don't pile up stale bullets.
- **No financial advice language.** This is a research wiki, not a recommendation. Phrasing: "the bull case argues...", not "you should buy...".

## What this wiki does NOT do

- It does not execute trades or interface with a broker.
- It does not track the user's actual positions unless the user explicitly populates a `wiki/portfolio/` directory (intentionally absent by default).
- It does not produce real-time prices. Always note "as of {date}" and prefer ranges over precise numbers when the data is older than a week.

## Tools the LLM can use

- **`python3 scripts/wikidb.py ask "<question>"`** — **the primary recall tool. Use it first on
  every query.** Hybrid lexical + semantic retrieval over all wiki pages and source summaries,
  returning dated, cited passages re-ranked by recency and conviction. Auto-refreshes the index
  before searching (build-before-read), so results are never stale. Backed by Voyage embeddings
  (`VOYAGE_API_KEY` in `.env`); degrades gracefully to lexical-only if the API is unreachable.
  - `wikidb.py build` — refresh the index manually (also runs automatically in the daily/sweep jobs).
  - `wikidb.py search "<terms>"` — legacy whole-document FTS5 (use `ask` instead for questions).
  - `wikidb.py page TICKER` / `stats` / `stale` — inspect the index.
- **WebSearch** — for current prices, recent news, and finding sources.
- **WebFetch** — for ingesting articles by URL.
- **Bash / Read / Write / Edit** — to maintain the wiki files.
- **Grep over `log.md`** — to recall recent activity.

When the user asks "what's the latest on X", default to: **`wikidb ask "X"` first**, then read the
surfaced page(s), then run a fresh WebSearch for anything dated within the last 30 days, then update
the page if you find something new.
