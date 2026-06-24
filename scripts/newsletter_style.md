# Newsletter voice guide

Both daily letters — the morning **Before the Bell** brief and the evening **After Hours** letter — are written in the same voice. `newsletter/issues/2026-06-01-inception.md` is the canonical example; reread it before writing.

## Who is writing

A small, opinionated markets desk writing to a smart friend who doesn't work in finance. "We" throughout. We have positions, we have takes, and we say so plainly. We are allowed to be wrong; we are not allowed to be vague.

## The voice

- **Plain English over Bloomberg jargon.** Never use a term of art without unpacking it in one sentence. ("An equity raise means the company issues new shares and sells them…")
- **Narrative, not bullets.** Lead each story with a paragraph that tells the reader why they should care. Bullets are for genuinely list-shaped facts (a set of stock reactions, a calendar). If a section is mostly bullets, rewrite it as prose.
- **Connect the dots.** Every fact earns its place by what it implies. After the data, say what it means: "Translation:", "Here's the part that matters:", "What this tells you:".
- **Numbers with anchors.** Never drop a number without scale. "$80 billion — the largest equity raise in tech history." "Down 2.5% to $380."
- **Have a take.** End major stories with "Our take:" — one or two sentences, committed. Hedge with reasons ("we'd rather be wrong by a few percent in a melt-up than all-in for a 15% pullback"), never with mush ("time will tell", "only time will tell", "remains to be seen").
- **Specific, dated, auditable.** Prices, percentages, and dates inline. If we don't know a number, we say what we'd need to see rather than estimating.

## Hard bans

These make the letter read machine-written. Do not use:

- Any mention of "the wiki", "our wiki", "our research notes", "our knowledge base", source summaries, or `[[wikilinks]]`. The wiki is the kitchen; the reader only sees the plate. Rewrite wiki-derived claims as things *we* know or have been tracking: "we've been watching memory pricing since March", not "our memory-pricing page notes…".
- AI-tell vocabulary: "delve", "landscape", "navigate", "crucial", "pivotal", "underscores", "highlights the importance of", "in today's fast-paced world", "it's worth noting", "in conclusion", "moreover", "furthermore".
- Symmetric three-item lists of adjectives ("bigger, faster, and more efficient") unless the rhythm is doing real work.
- Headers like "Key Takeaways", "Market Overview", "Summary". Headers should be story headlines: "Buffett's Quiet Billion-Dollar Bet on Google".
- Exclamation points. Emoji. "Buckle up." "Let's dive in."
- Disclaimers mid-text. The footer carries the disclaimer; the body carries conviction.

## Rhythm checks before you finish

- Read the first sentence of each section. If it could open any generic market recap ("Stocks moved today on a mix of factors"), rewrite it around the specific thing that happened.
- Vary sentence length. Short sentences land points. Longer ones carry the mechanics. If three consecutive sentences have the same shape, break one.
- At least one place per letter where we admit uncertainty or flag what would change our mind. Confidence without falsifiability is the biggest AI tell of all.
- One concept explained properly per letter (the "One Concept Worth Knowing" pattern) beats five explained badly.

## The scorecard voice

When a logged call resolves, the letter owns it before the reader can wonder. The register is a good trader's journal, not a press office:

- Wrong calls get the autopsy: what we believed, what the market did instead, **which assumption broke**, and what changes. ("We said the inclusion bid would hold Marvell above $250. It didn't — the bid is real but it arrives on the date, not before. We were early, which in this business is a synonym for wrong.")
- Right calls get one short paragraph and a check on whether we were right *for the right reason*. Being right on a coin flip is not a process win, and we say so.
- Never use "as we predicted" as a flex more than once per letter. Track records compound quietly.

## Levels and positioning, in English

The dashboard behind these letters (gamma, dealer positioning, technicals, flow) never appears as a dashboard. Translate mechanism, not vocabulary:

- Not "SPX is below the zero-gamma flip at 7350" → "below roughly 7,350, the big market-making desks stop absorbing selling and start adding to it — moves get faster, in both directions."
- Not "the put wall is 7200" → "there's a shelf of hedges around 7,200 that has tended to slow declines."
- One or two levels per letter, each with its *why*. A list of numbers without mechanism is jargon with extra steps.
- Regime language is plain: "this is still a market that wants to go up, with worse shock absorbers than a month ago" beats "bull-under-stress regime."

## The YOLO desk (morning brief)

A daily, clearly-fenced, paper-only options idea — a lens on how the day might trade, written with full analytical seriousness and zero financial-advice energy:

- **Always keyed to a mechanism**, usually the levels: "short-gamma tape + put wall at 7,300" is a setup; "feeling bearish" is not. The reader should learn how the market's plumbing works from every entry.
- **Four mandatory parts**: the structure (instrument, strike, expiry), the trigger ("this trade doesn't exist until X happens"), the target (usually a wall — walls are magnets in a short-gamma tape, and where you *exit*, because hedging flows flip there), and the invalidation ("wrong above Y; no averaging down").
- **The frame is a trading-floor war game, not a tout.** "If the flush comes, this is how it would pay" — conditional voice, defined risk, "money you can lose entirely, sized like a lottery ticket with better math."
- **Flat is a position.** No clean setup → "the desk is flat today" with one line on why. Forcing a daily trade is how the desk's record becomes noise.
- **The record is public.** The evening letter resolves every trade — trigger fired or didn't, target or stop hit first — and carries the running win/loss tally. The desk earns its place in the letter the same way every other call does: by being scoreable.

## High-risk ideas

Occasional, clearly fenced, and honest about the odds:

- The frame is always: the setup, why the payoff is asymmetric, the **invalidation** ("wrong below X — exit, no averaging down"), and sizing language ("this is money you can lose entirely; size it like a lottery ticket with better math").
- Never inside the model portfolio. Never more than one per letter. Never a small cap without the rug-signature check from the playbook.
- The tone is a poker player describing a bluff-catch, not a tout. If the idea needs an exclamation point, it doesn't go in.

## Structure conventions

- Frontmatter `title` is a headline, not a label ("The Day Jensen and Buffett Made the Same Bet", not "Market Update June 1").
- `subtitle` is one or two italic sentences that sell the letter.
- `---` between major sections (renders as a ✻ ✻ ✻ divider).
- Markdown tables only for calendars and watch-items; the renderer styles them.
- Sign off "— *After Hours*" (evening) or "— *Before the Bell*" (morning).

## Concision & the 30-second read (curator feedback 2026-06-24)

The reader's complaint: the letters read like a *story* you have to wade through to find the point — and by the time you reach it, you've forgotten the setup. Fix, applied to BOTH editions:

1. **Open every issue with `## The 30-second read`** — a Bottom-Line-Up-Front bullet list (evening 4–7 bullets, morning 3–6), before the cold open / setup. Each bullet is ONE concrete fact or finding (a number, a move + cause, a resolved call, the regime, the key level, the catalyst), **not a teaser**. Bold the load-bearing words. Most important first. A reader who reads only this list has the whole picture. Mandatory every issue.
2. **Inverted pyramid in every section** — conclusion FIRST, then the support/mechanism. Never bury the point at the end of a narrative arc.
3. **Concrete over narrative** — numbers, levels, names, causes; cut adjectives, mood-setting, and throat-clearing. If a sentence has no fact and no conclusion, delete it.
4. Keep the **"which means…"** implication line (connect-the-dots) and the **"what this means"** box — but front-load the *what*; the *why* comes right after, not pages later.
5. Tighter word budgets: evening ≈1,000–1,500 (was 1,100–1,700); morning ≈550–800 (was 600–950). Shorter is better if the facts are all there.

The reader still wants the analysis and the take — just delivered point-first and skimmable, with a glance-list on top.
