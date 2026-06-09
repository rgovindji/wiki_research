#!/usr/bin/env python3
"""Validate the newsletter self-improvement loop data files.

Checks predictions.json (schema, unique ids, falsifiers on every call,
calibration tally matching actual statuses, stale open predictions),
the latest market_state snapshot, playbook.md structure, portfolio.json
arithmetic, and issue frontmatter.

Run after every headless run (daily_claude.sh does this) or manually:

    python3 scripts/validate_loop.py            # validate repo files
    python3 scripts/validate_loop.py --strict   # warnings also exit non-zero

Exit codes: 0 = clean (or warnings without --strict), 1 = errors.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NL = REPO / "newsletter"

VERDICTS = {"right", "wrong", "partial", "timing", "expired"}
STATUSES = {"open"} | VERDICTS
CONFIDENCES = {"high", "medium", "low"}
EDITIONS = {"morning", "close"}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def parse_date(s: str, ctx: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(s)
    except (TypeError, ValueError):
        err(f"{ctx}: bad date {s!r}")
        return None


def check_predictions() -> None:
    path = NL / "predictions.json"
    if not path.exists():
        err("predictions.json missing")
        return
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        err(f"predictions.json: invalid JSON — {e}")
        return

    preds = data.get("predictions")
    if not isinstance(preds, list) or not preds:
        err("predictions.json: 'predictions' must be a non-empty list")
        return

    today = dt.date.today()
    seen_ids: set[str] = set()
    tally: dict[str, int] = {v: 0 for v in VERDICTS}

    required = ["id", "made", "issue", "type", "claim", "confidence",
                "horizon", "falsifier", "status"]
    for p in preds:
        pid = p.get("id", "<no id>")
        ctx = f"prediction {pid}"
        for field in required:
            if not p.get(field):
                err(f"{ctx}: missing or empty '{field}'")
        if pid in seen_ids:
            err(f"{ctx}: duplicate id")
        seen_ids.add(pid)

        status = p.get("status")
        if status not in STATUSES:
            err(f"{ctx}: status {status!r} not in {sorted(STATUSES)}")
        if p.get("confidence") not in CONFIDENCES:
            err(f"{ctx}: confidence {p.get('confidence')!r} not in {sorted(CONFIDENCES)}")

        made = parse_date(p.get("made", ""), ctx)
        horizon = parse_date(p.get("horizon", ""), ctx)
        if made and horizon and horizon < made:
            err(f"{ctx}: horizon {horizon} before made {made}")

        falsifier = p.get("falsifier") or ""
        if len(falsifier.strip()) < 20:
            err(f"{ctx}: falsifier too vague ({falsifier!r}) — no falsifier, no call")

        if status == "open":
            if p.get("resolution_note"):
                err(f"{ctx}: open but has a resolution_note")
            if horizon and horizon < today:
                warn(f"{ctx}: horizon {horizon} has passed but still open — due for resolution")
        elif status in VERDICTS:
            tally[status] += 1
            if not (p.get("resolution_note") or "").strip():
                err(f"{ctx}: resolved as {status} but resolution_note is empty — the WHY is the product")
            if not p.get("resolved"):
                err(f"{ctx}: resolved as {status} but 'resolved' date is empty")

    cal = data.get("calibration", {})
    for verdict in VERDICTS:
        recorded = cal.get(verdict)
        if recorded != tally[verdict]:
            err(f"calibration.{verdict} = {recorded} but actual count is {tally[verdict]} — tally out of sync")

    open_count = sum(1 for p in preds if p.get("status") == "open")
    if open_count > 15:
        warn(f"{open_count} open predictions — too many to track honestly; resolve or expire some")


def check_market_state() -> None:
    d = NL / "market_state"
    if not d.exists():
        err("market_state/ missing")
        return
    snaps = sorted(d.glob("*.json"))
    if not snaps:
        err("market_state/ has no snapshots")
        return
    latest = snaps[-1]
    try:
        data = json.loads(latest.read_text())
    except json.JSONDecodeError as e:
        err(f"{latest.name}: invalid JSON — {e}")
        return

    if data.get("date") != latest.stem:
        err(f"{latest.name}: 'date' field {data.get('date')!r} doesn't match filename")

    for key in ("indexes", "regime", "key_levels", "calendar"):
        if key not in data:
            err(f"{latest.name}: missing '{key}'")

    regime = data.get("regime", {})
    if regime.get("options") and regime.get("call") not in regime["options"]:
        err(f"{latest.name}: regime call {regime.get('call')!r} not in declared options")
    if not (regime.get("what_changes_it") or "").strip():
        warn(f"{latest.name}: regime has no 'what_changes_it' — a regime call without a flip condition is a vibe")

    cal = data.get("calendar", [])
    if not isinstance(cal, list) or not cal:
        warn(f"{latest.name}: calendar empty")

    age = (dt.date.today() - dt.date.fromisoformat(latest.stem)).days
    if age > 4:
        warn(f"latest market_state snapshot is {age} days old ({latest.name})")


YOLO_STATUSES = {"open", "win", "loss", "no-trigger", "expired"}


def check_yolo() -> None:
    path = NL / "yolo.json"
    if not path.exists():
        warn("yolo.json missing (YOLO desk not initialized)")
        return
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        err(f"yolo.json: invalid JSON — {e}")
        return
    trades = data.get("trades", [])
    seen: set[str] = set()
    wins = losses = no_trig = 0
    for t in trades:
        tid = t.get("id", "<no id>")
        ctx = f"yolo trade {tid}"
        if tid in seen:
            err(f"{ctx}: duplicate id")
        seen.add(tid)
        for field in ("date", "structure", "thesis", "trigger", "target", "invalidation", "status"):
            if not t.get(field):
                err(f"{ctx}: missing or empty '{field}'")
        status = t.get("status")
        if status not in YOLO_STATUSES:
            err(f"{ctx}: status {status!r} not in {sorted(YOLO_STATUSES)}")
        if status in ("win", "loss", "no-trigger") and not (t.get("resolution_note") or "").strip():
            err(f"{ctx}: resolved as {status} but resolution_note is empty")
        if status == "open" and t.get("date") and t["date"] < dt.date.today().isoformat():
            warn(f"{ctx}: open trade from {t['date']} — the close run should have resolved it")
        wins += status == "win"
        losses += status == "loss"
        no_trig += status == "no-trigger"
    sc = data.get("scorecard", {})
    for name, actual in (("wins", wins), ("losses", losses), ("no_trigger", no_trig)):
        if sc.get(name) != actual:
            err(f"yolo.json scorecard.{name} = {sc.get(name)} but actual count is {actual}")


def check_playbook() -> None:
    path = NL / "playbook.md"
    if not path.exists():
        err("playbook.md missing")
        return
    text = path.read_text()
    for section in ("## Active lessons", "## Hypotheses under test", "## Retired"):
        if section not in text:
            err(f"playbook.md: missing section '{section}'")
    active = re.findall(r"^\d+\. \*\*", text, re.MULTILINE)
    if len(active) > 20:
        warn(f"playbook.md: {len(active)} active lessons (cap ~20) — due for distillation")


def check_portfolio() -> None:
    path = NL / "portfolio.json"
    if not path.exists():
        err("portfolio.json missing")
        return
    try:
        p = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        err(f"portfolio.json: invalid JSON — {e}")
        return
    total = sum(h.get("allocation_pct", 0) for h in p.get("current_holdings", []))
    total += p.get("cash_pct", 0)
    if abs(total - 100) > 0.01:
        err(f"portfolio.json: allocations + cash = {total}%, not 100%")
    for h in p.get("current_holdings", []):
        t = h.get("ticker", "?")
        if not (h.get("avg_price_usd", 0) > 0 and h.get("current_price_usd", 0) > 0):
            err(f"portfolio.json: {t} has non-positive price")
        if h.get("avg_price_usd") == round(h.get("avg_price_usd", 0)) and h.get("avg_price_usd", 0) >= 50:
            warn(f"portfolio.json: {t} avg cost ${h.get('avg_price_usd'):.2f} is a round number — placeholder?")


FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def check_issues() -> None:
    issues = sorted((NL / "issues").glob("*.md"))
    if not issues:
        warn("no issues found")
        return
    for issue in issues[-6:]:
        m = FM_RE.match(issue.read_text())
        if not m:
            err(f"{issue.name}: no frontmatter")
            continue
        fm = dict(
            (k.strip(), v.strip().strip('"').strip("'"))
            for k, _, v in (line.partition(":") for line in m.group(1).splitlines())
            if k.strip()
        )
        if "title" not in fm:
            err(f"{issue.name}: frontmatter missing title")
        edition = fm.get("edition", "close")
        if edition not in EDITIONS:
            err(f"{issue.name}: edition {edition!r} not in {sorted(EDITIONS)}")
        if edition == "close" and "inception" not in issue.name and "issue_number" not in fm:
            warn(f"{issue.name}: close edition without issue_number")
        body = issue.read_text()[m.end():]
        if "[[" in body:
            err(f"{issue.name}: contains [[wikilink]] — wiki must not leak into reader-facing copy")
        if re.search(r"\bwiki\b", body, re.IGNORECASE):
            err(f"{issue.name}: mentions 'wiki' in the body — rewrite per style guide")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="warnings also fail")
    args = ap.parse_args()

    check_predictions()
    check_market_state()
    check_playbook()
    check_portfolio()
    check_yolo()
    check_issues()

    for e in errors:
        print(f"ERROR   {e}")
    for w in warnings:
        print(f"warning {w}")
    print(f"[validate_loop] {len(errors)} error(s), {len(warnings)} warning(s)")
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
