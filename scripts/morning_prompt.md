# Before the Bell — Headless Morning Run

You are writing the **Before the Bell** morning brief for __TODAY__, invoked by `claude -p` from a launchd job at ~6:45 AM Central, before the 8:30 AM CT market open. There is no user in the loop. Write the issue file, then exit — the wrapper script renders and emails it.

This is a **newsletter run, not a wiki-update run.** Do not ingest sources, do not create source summaries, do not modify wiki pages. The evening run owns the wiki.

## Context loading (read these first)

1. `scripts/newsletter_style.md` — the voice guide. Non-negotiable; reread it.
2. `newsletter/issues/2026-06-01-inception.md` — the canonical voice example.
3. The most recent `newsletter/issues/*-afterhours.md` (if any) — last night's letter; don't repeat it, build on it.
4. The most recent `newsletter/market_state/*.json` — last night's dashboard: regime call, key levels, gamma if collected, calendar. Your futures read this morning is measured AGAINST these levels.
5. `newsletter/predictions.json` — open calls. Note any prediction that **resolves today** (data print, event date); the brief should tell the reader exactly what we said and what number proves us right or wrong.
6. `newsletter/playbook.md` — accumulated lessons; apply them to today's framing.
7. `wiki/watchlist.md` and `wiki/overview.md` — what we cover and our current stances. Background knowledge, never cited.
8. The last ~20 entries of `log.md` — what we've been tracking lately.

## Research (parallel WebSearch, ~8-12 calls)

- US stock futures right now (S&P, Nasdaq) and the 10-year yield
- Overnight Asia/Europe sessions — especially TSMC, ASML, SK Hynix, Samsung, and anything that moves our names
- Pre-market movers and why; any overnight or pre-market earnings from names we cover
- Today's calendar: earnings due (before open / after close), economic data (CPI, jobs, Fed speakers), and known catalysts
- Any big overnight AI / semiconductor / mega-cap tech news

Budget: ~12 WebSearch and ~4 WebFetch calls, under 12 minutes wall-clock. This is a brief, not a deep dive.

## Write the issue

Create `newsletter/issues/__TODAY__-morning.md`:

```yaml
---
edition: morning
date: __TODAY__
title: "<headline, not a label>"
subtitle: "<one or two sentences that sell the brief>"
---
```

Shape (≈600-950 words — shorter than the evening letter; the reader has ten minutes before work):

1. **The setup** — two or three paragraphs: where futures point relative to last night's regime call and key levels, what happened overnight, and the one thing that matters most before the open. Lead with the most interesting thing, not with "futures are up".
2. **On the line today** — when one of our logged calls resolves today (a data print, an event), one tight paragraph: what we said, the specific number or level that proves us right or wrong, and what we'll do in either branch. Skip the section entirely when nothing resolves.
3. **One to three overnight stories** with story-headline `##` sections. Each: what happened, the mechanics in plain English, what it means for names we own or track, and our take.
4. **Today's calendar** — a small markdown table (When | What | Why it matters) covering earnings and data due today. Only rows that matter; three rows beat eight.
5. **The game plan** — the closing section: the one or two levels that matter today and why, in mechanism terms a smart non-professional can use ("if the S&P loses ~X, the selling tends to feed itself; above ~Y the dip was noise"), drawn from last night's market_state. End with a forward sentence and sign off "— *Before the Bell*".

The morning run does NOT update `predictions.json`, `playbook.md`, or `market_state/` — those belong to the evening run. The brief consumes them.

Voice rules from `scripts/newsletter_style.md` apply in full. Especially: no wiki mentions, no `[[wikilinks]]`, no AI-tell vocabulary, takes over hedges.

## Housekeeping

- Append one short entry to `log.md` just after the first `---` separator:
  ```
  ## [__TODAY__] note | Morning brief: <title>

  Before the Bell sent. Covered: <one line>. No wiki changes (morning runs don't ingest).

  ---
  ```
- Write ONLY to `newsletter/issues/` and `log.md`. Nothing else.
- Do NOT commit or push — the wrapper handles it.

## Output

When done, print:

```
MORNING BRIEF COMPLETE — __TODAY__
Issue: newsletter/issues/__TODAY__-morning.md
Title: <title>
```

## Hard constraints

- No interactive prompts; make conservative calls and move on.
- If markets are closed today (US holiday / weekend), still check: if there is genuinely nothing (no futures session, no calendar), write a two-paragraph holiday note in the same voice instead of forcing a full brief.
- Never invent prices or futures levels. If a search result is stale or ambiguous, give the range and time-stamp it ("as of early this morning").
