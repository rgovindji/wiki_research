# Daily Update — Headless Run

You are running the daily wiki update for rgovindji's Investing wiki in **headless / non-interactive mode** (invoked by `claude -p` from a launchd job). There is no user in the loop. Execute the full workflow autonomously, then exit.

## Context loading (read these first)

1. The full **CLAUDE.md** in the repo root — wiki schema, conventions, ingest workflow
2. **MEMORY.md** index + the linked feedback files for `daily-update-workflow`, `earnings-workflow`, `accountability-log`, `connect-the-dots`, `what-this-means-box`
3. **index.md** — catalog of all wiki pages (so you know what's covered)
4. The last ~80 entries of **log.md** (so you don't re-ingest what's already in)
5. **wiki/watchlist.md** — current stance/conviction table

## The job

Execute the 8-step daily ritual from `feedback_daily_update_workflow.md`, with these headless-mode adjustments:

### What you DO

1. **Discover** — parallel WebSearch sweeps:
   - Top AI / semi / Mag 7 news today and yesterday
   - Earnings prints from wiki tickers in the last 48h
   - Long-form sources (Stratechery, SemiAnalysis, Dwarkesh, BG2, ILTB)
   - 8-Ks / filings; sector-specific signals
2. **Curate** — apply the signal-vs-noise bar:
   - Ingest only net-new substantive info, contradictions, long-form, conviction-relevant data
   - Skip restatements, price-action narratives, opinion pieces
   - If nothing material happened, write a "low-signal day" log entry and exit cleanly
3. **Save raw material** (optional) — use WebFetch to pull article content, save under `raw/articles/YYYY-MM-DD-slug.md`. `raw/` is gitignored.
4. **Write source summaries** — for each curated source create `sources/YYYY-MM-DD-slug.md` using the CLAUDE.md template (frontmatter + TL;DR + Key facts + Key claims + Quotes worth keeping + Wiki updates that should be made + Cross-references)
5. **Append to wiki pages** — add bullets to existing `## Recent developments` sections only. Use the connect-the-dots style ("Which means…" implication line).
6. **Update index.md** — add new source ingests + any new pages to the right catalog section
7. **Append to log.md** — prepend a new entry just after the first `---` separator:
   ```
   ## [YYYY-MM-DD] daily | <6-12 word title>
   
   <body summarizing what was added, with [[wikilinks]] to every page touched>
   
   ---
   ```

### What you DO NOT do

- **Do NOT flip stances** (bull → bear or vice versa). If a print warrants a stance change, flag it in the log entry as "needs user sign-off" and leave the wiki page unchanged.
- **Do NOT change conviction levels** unilaterally for high-importance positions. For low/medium tier names, you may upgrade with a clear "flagged for review" annotation in the log entry.
- **Do NOT modify frontmatter** of existing wiki pages other than the `last_updated` and `sources` count fields.
- **Do NOT create new top-level wiki pages** (companies, sectors, themes) without a clear demand signal. Stick to appending to existing pages and creating source summaries.
- **Do NOT commit or push** — the wrapper script does that. Just write files to disk.
- **Do NOT modify MEMORY.md** or anything under `.claude/`.

### Output format

When you're done writing files, print a brief summary to stdout:

```
DAILY UPDATE COMPLETE — YYYY-MM-DD
Sources ingested: N
Wiki pages touched: <list>
Stance changes flagged for review: <list or "none">
Skipped (low-value): <one-line summary>
```

The wrapper script reads stdout for logging. Keep the summary under 30 lines.

### Hard constraints

- **No interactive prompts.** If you're uncertain, make a conservative call and flag it in the log entry. Don't pause for input — there's no user listening.
- **Tool budget.** Use up to ~20 WebSearch calls and ~10 WebFetch calls. If you need more, you're probably ingesting too much; reduce.
- **Time budget.** Aim for under 20 minutes total wall-clock.
- **File-write discipline.** Only write to `raw/`, `sources/`, `wiki/`, `index.md`, `log.md`. Nothing else.
- **No new abstractions / refactors.** This is a content update, not a code change.

### Today's date

`__TODAY__` (the wrapper script substitutes this with the UTC date before invoking you).

### If nothing material happened

Write a single log entry:

```
## [YYYY-MM-DD] daily | Low-signal day — no material ingests

Reviewed: <one-line summary of what was checked>. Nothing rose above the signal bar today. Next session priorities: <1-2 items from the previous log entry's "Next session priorities" list>.

---
```

Then print:
```
DAILY UPDATE COMPLETE — YYYY-MM-DD
Sources ingested: 0
Wiki pages touched: log.md
Stance changes flagged for review: none
Skipped (low-value): nothing crossed the bar
```

…and exit. The wrapper will detect the lack of net-new sources and skip the email step if you prefer (it's controlled by a flag in the script).
