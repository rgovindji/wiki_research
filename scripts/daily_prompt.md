# After the Bell — Headless Daily Run

You are running the daily close-of-market job for rgovindji's Investing wiki in **headless / non-interactive mode** (invoked by `claude -p` from a launchd job at 5 PM Central, two hours after the close). There is no user in the loop. Two deliverables, in order:

1. **Update the wiki** (the 8-step daily ritual — same as always)
2. **Write the After Hours newsletter issue** from what you learned; the wrapper script renders and emails it

## Context loading (read these first)

1. The full **CLAUDE.md** in the repo root — wiki schema, conventions, ingest workflow
2. **MEMORY.md** index + the linked feedback files for `daily-update-workflow`, `earnings-workflow`, `accountability-log`, `connect-the-dots`, `what-this-means-box`
3. **index.md** — catalog of all wiki pages (so you know what's covered)
4. The last ~80 entries of **log.md** (so you don't re-ingest what's already in)
5. **wiki/watchlist.md** — current stance/conviction table
6. **scripts/newsletter_style.md** — the newsletter voice guide (for part 2)
7. **newsletter/portfolio.json** + the most recent two issues in `newsletter/issues/` — portfolio state and yesterday's letter

## Part 1 — Wiki update

Execute the 8-step daily ritual from `feedback_daily_update_workflow.md`, with these headless-mode adjustments:

### What you DO

1. **Discover** — parallel WebSearch sweeps:
   - Today's full session: index moves, sector rotation, top AI / semi / Mag 7 movers and why
   - Earnings prints from wiki tickers today (especially after-hours prints from the last two hours) and yesterday
   - Long-form sources (Stratechery, SemiAnalysis, Dwarkesh, BG2, ILTB)
   - 8-Ks / filings; sector-specific signals (memory pricing, GPU rental rates, power)
   - Closing prices for every ticker in `newsletter/portfolio.json` (needed for part 2)
2. **Curate** — apply the signal-vs-noise bar:
   - Ingest only net-new substantive info, contradictions, long-form, conviction-relevant data
   - Skip restatements, price-action narratives, opinion pieces
   - A low-signal day for the *wiki* is fine — but the *newsletter* still goes out (part 2 is never skipped)
3. **Save raw material** (optional) — use WebFetch to pull article content, save under `raw/articles/YYYY-MM-DD-slug.md`. `raw/` is gitignored.
4. **Write source summaries** — for each curated source create `sources/YYYY-MM-DD-slug.md` using the CLAUDE.md template
5. **Append to wiki pages** — add bullets to existing `## Recent developments` sections only. Use the connect-the-dots style ("Which means…" implication line).
6. **Update index.md** — add new source ingests + any new pages to the right catalog section
7. **Append to log.md** — prepend a new entry just after the first `---` separator:
   ```
   ## [YYYY-MM-DD] daily | <6-12 word title>

   <body summarizing what was added, with [[wikilinks]] to every page touched>

   ---
   ```

### What you DO NOT do

- **Do NOT flip stances** (bull → bear or vice versa). Flag in the log entry as "needs user sign-off" and leave the wiki page unchanged.
- **Do NOT change conviction levels** unilaterally for high-importance positions. For low/medium tier names, you may upgrade with a clear "flagged for review" annotation in the log entry.
- **Do NOT modify frontmatter** of existing wiki pages other than `last_updated` and `sources` count.
- **Do NOT create new top-level wiki pages** without a clear demand signal.
- **Do NOT commit or push** — the wrapper script does that.
- **Do NOT modify MEMORY.md** or anything under `.claude/`.

## Part 2 — The After Hours letter

This is the product the reader sees. The wiki work above is your research; the letter is the synthesis. **It goes out every market day, even when the wiki update was low-signal** — a quiet tape is itself a story if you tell it honestly.

### Update the portfolio first

In `newsletter/portfolio.json`, update each holding's `current_price_usd` to today's closing price (from your part-1 research; search for any you're missing). Don't touch `avg_price_usd`, allocations, or holdings — position changes are the user's call.

### Write the issue

Create `newsletter/issues/YYYY-MM-DD-afterhours.md`:

```yaml
---
edition: close
issue_number: <previous afterhours issue_number + 1; check the latest issue in newsletter/issues/>
date: YYYY-MM-DD
title: "<headline, not a label>"
subtitle: "<one or two sentences that sell the letter>"
---
```

Shape (≈1,000–1,600 words, in the mold of issue #1):

1. **Cold open** — a few paragraphs on the day's defining story or tension. Not "stocks rose today"; find the thread.
2. **One to three main stories** with story-headline `##` sections. What happened, the mechanics in plain English, what it means, our take. Earnings prints from names we own or track always make the cut.
3. **Portfolio commentary** — a paragraph or two on how the day treated our positions: biggest mover and why, anything that challenges a thesis, what we'd do with the cash reserve and at what level. (The live table, chart, and position values are appended automatically by the renderer — do NOT paste a holdings table into the body.)
4. **Things to watch** — a small markdown table of tomorrow/this week's catalysts (When | What | Why it matters). Only rows that matter.
5. **Optional: One Concept Worth Knowing** — when the day's news used a mechanic worth unpacking (include it most days; skip when forced).
6. **The bottom line** — a short closing section that lands the day's thesis in two or three paragraphs. Sign off "— *After Hours*".

Voice rules from `scripts/newsletter_style.md` apply in full. The two that get violated under deadline pressure:
- **No wiki anywhere in the letter.** No "our wiki", no `[[wikilinks]]`, no "source summary". Wiki-derived knowledge becomes "we've been tracking…".
- **No AI-tell vocabulary or structure.** If a section reads like a press summary, rewrite it around what it means for the reader's money.

## Output format

When you're done writing files, print a brief summary to stdout:

```
DAILY RUN COMPLETE — YYYY-MM-DD
Sources ingested: N
Wiki pages touched: <list>
Stance changes flagged for review: <list or "none">
Newsletter: newsletter/issues/YYYY-MM-DD-afterhours.md — "<title>"
Portfolio prices updated: <N tickers>
```

Keep the summary under 30 lines.

## Hard constraints

- **No interactive prompts.** Make conservative calls and flag them in the log entry.
- **Tool budget.** Up to ~25 WebSearch and ~10 WebFetch calls total across both parts.
- **Time budget.** Under 30 minutes wall-clock total.
- **File-write discipline.** Only write to `raw/`, `sources/`, `wiki/`, `index.md`, `log.md`, `newsletter/issues/`, `newsletter/portfolio.json`. Nothing else.
- **Never invent prices.** If you can't confirm a close for a portfolio ticker, leave its `current_price_usd` unchanged and say so in the stdout summary rather than guessing.
- If today was a US market holiday, skip part 2 (no letter) and write a one-line log entry noting the holiday; the wiki sweep (part 1) still runs if there's news.

## Today's date

`__TODAY__` (the wrapper script substitutes this with the UTC date before invoking you).
