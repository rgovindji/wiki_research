"""AWS Lambda handler — daily wiki update + overview email.

Runs end-to-end without git: fetches repo content via the GitHub Contents API,
calls Anthropic for the daily research sweep, writes back via the same API,
then renders + sends the overview email via SES.

Invoked on a schedule by EventBridge. Manual invocations via:
    aws lambda invoke --function-name wiki-daily-update \\
        --payload '{"skip_update":false,"send_email":true}' /tmp/out.json

Event payload (all optional):
    skip_update: bool   — skip the Claude research call (just email latest log entry)
    send_email:  bool   — skip the SES send (write to repo only)
    email_to:    str    — override recipient (default: from env)
    dry_run:     bool   — return the JSON plan, don't write or send

Required env vars (set by CloudFormation):
    GITHUB_REPO            e.g. "rgovindji/wiki_research"
    GITHUB_BRANCH          e.g. "main"
    SES_SENDER             e.g. "wiki@decideai.xyz"
    EMAIL_TO_DEFAULT       e.g. "rgovindji@gmail.com"
    SECRET_ANTHROPIC_ID    Secrets Manager secret id (JSON {"api_key":"..."})
    SECRET_GITHUB_ID       Secrets Manager secret id (JSON {"token":"..."})
    ANTHROPIC_MODEL        optional, default claude-opus-4-7
"""
from __future__ import annotations

import base64
import datetime as dt
import json
import logging
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import boto3

# Bundled scripts/ — packaged alongside handler.py in the Lambda zip.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scripts"))
import daily_email as de  # noqa: E402

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

logger = logging.getLogger()
logger.setLevel(logging.INFO)

GITHUB_REPO = os.environ.get("GITHUB_REPO", "rgovindji/wiki_research")
GITHUB_BRANCH = os.environ.get("GITHUB_BRANCH", "main")
GITHUB_API = "https://api.github.com"
GITHUB_RAW = "https://raw.githubusercontent.com"

SES_SENDER = os.environ.get("SES_SENDER", "wiki@decideai.xyz")
EMAIL_TO_DEFAULT = os.environ.get("EMAIL_TO_DEFAULT", "rgovindji@gmail.com")
AWS_REGION = os.environ.get("AWS_REGION_OVERRIDE", "us-east-1")

SECRET_ANTHROPIC_ID = os.environ.get("SECRET_ANTHROPIC_ID", "wiki/anthropic")
SECRET_GITHUB_ID = os.environ.get("SECRET_GITHUB_ID", "wiki/github")

ANTHROPIC_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-7")
ANTHROPIC_MAX_TOKENS = 16000
ANTHROPIC_WEB_SEARCH_MAX_USES = 12

LOG_PATH_IN_REPO = "log.md"
INDEX_PATH = "index.md"
WATCHLIST_PATH = "wiki/watchlist.md"

# Lambda committer identity for GitHub writes
COMMITTER = {"name": "wiki-bot", "email": "wiki-bot@decideai.xyz"}


# ---------------------------------------------------------------------------
# Secret + GitHub helpers
# ---------------------------------------------------------------------------

_sm_client = boto3.client("secretsmanager", region_name=AWS_REGION)
_ses_client = boto3.client("sesv2", region_name=AWS_REGION)


def get_secret(secret_id: str, json_key: str) -> str:
    resp = _sm_client.get_secret_value(SecretId=secret_id)
    payload = json.loads(resp["SecretString"])
    value = payload.get(json_key)
    if not value:
        raise RuntimeError(f"secret {secret_id} missing key {json_key!r}")
    return value


def _gh_request(method: str, path: str, token: str, body: dict | None = None,
                params: dict | None = None) -> dict:
    url = f"{GITHUB_API}{path}"
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "wiki-daily-lambda/1.0")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        logger.error("github api %s %s failed: %s — %s", method, path, e.code, body_text[:500])
        raise


def gh_get_file(path: str, token: str, ref: str = GITHUB_BRANCH) -> tuple[str, str | None]:
    """Return (content_text, sha). sha is None if file doesn't exist (404)."""
    try:
        data = _gh_request("GET", f"/repos/{GITHUB_REPO}/contents/{urllib.parse.quote(path)}",
                           token, params={"ref": ref})
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "", None
        raise
    content = base64.b64decode(data["content"]).decode("utf-8")
    return content, data["sha"]


def gh_put_file(path: str, content: str, message: str, token: str,
                sha: str | None = None, branch: str = GITHUB_BRANCH) -> dict:
    """Create or update a file. Pass sha for updates, None for creates."""
    body = {
        "message": message,
        "branch": branch,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        "committer": COMMITTER,
    }
    if sha:
        body["sha"] = sha
    return _gh_request("PUT", f"/repos/{GITHUB_REPO}/contents/{urllib.parse.quote(path)}",
                       token, body=body)


def gh_list_dir(path: str, token: str, ref: str = GITHUB_BRANCH,
                silent_404: bool = True) -> list[dict]:
    """List directory contents (returns list of {name, path, type, sha, ...}).
    Silently returns [] for missing directories when silent_404=True so optional
    paths don't pollute CloudWatch with ERROR-level noise."""
    try:
        if silent_404:
            url = f"{GITHUB_API}/repos/{GITHUB_REPO}/contents/{urllib.parse.quote(path)}?{urllib.parse.urlencode({'ref': ref})}"
            req = urllib.request.Request(url, method="GET")
            req.add_header("Authorization", f"Bearer {token}")
            req.add_header("Accept", "application/vnd.github+json")
            req.add_header("X-GitHub-Api-Version", "2022-11-28")
            req.add_header("User-Agent", "wiki-daily-lambda/1.0")
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    return []
                raise
        else:
            data = _gh_request("GET", f"/repos/{GITHUB_REPO}/contents/{urllib.parse.quote(path)}",
                               token, params={"ref": ref})
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return []
        raise
    return data if isinstance(data, list) else []


# ---------------------------------------------------------------------------
# Claude orchestration
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are the editorial AI maintaining rgovindji's Investing wiki,
running inside an AWS Lambda daily-update job. The user is a long-term equity
investor focused on AI / semis / Mag 7 with tactical 6-18mo swings.

You will be given today's date, the current index.md, the last ~80 log entries
from log.md, and the watchlist.md table. Your job is to:

1. DISCOVER. Use web_search to do parallel sweeps of:
   - Top AI / semi / Mag 7 news today and yesterday
   - Earnings prints from wiki tickers in the last 48h
   - Long-form sources (Stratechery, SemiAnalysis, Dwarkesh, BG2)
   - 8-K filings; sector-specific tightening signals

2. CURATE. Apply the wiki's signal-vs-noise bar: ingest only net-new
   substantive info, contradictions to existing wiki claims, long-form
   deep dives, or conviction-changing data. Skip restatements, pure
   price-action narratives, opinion pieces, click-bait.

3. PROPOSE. Return a single JSON object (no prose, no markdown wrapper):

   {
     "summary_one_liner": "<6-12 word title for the log entry>",
     "log_entry_body":    "<markdown body for log.md — no heading; the script adds it>",
     "source_summaries":  [{"path": "sources/YYYY-MM-DD-slug.md", "content": "<full markdown>"}],
     "wiki_appends":      [{"path": "wiki/companies/TICKER.md", "after_heading": "Recent developments", "content": "- **YYYY-MM-DD** — ..."}]
   }

HARD RULES:
- Output ONLY the JSON object. No prose, no code fences.
- Use [[wikilinks]] for every wiki page reference.
- Cite the date of every metric inline.
- "Which means..." implication line for every analytical statement.
- DO NOT propose stance/conviction changes — flag in log_entry_body
  as "needs user sign-off" but never edit those.
- DO NOT modify frontmatter of existing wiki pages — only append to
  body sections via wiki_appends.
- If nothing material happened today: empty source_summaries +
  empty wiki_appends + a log_entry_body that says "Low-signal day."
- Source summaries use the standard schema (frontmatter + TL;DR +
  Key facts + Key claims + Quotes worth keeping + Wiki updates).

The Lambda will deterministically write your JSON via the GitHub API."""


def tail_log_entries(log_text: str, n: int = 80) -> str:
    lines = log_text.splitlines()
    boundaries = [i for i, ln in enumerate(lines) if ln.startswith("## [")]
    if not boundaries:
        return "\n".join(lines[-400:])
    start = boundaries[-n] if len(boundaries) >= n else boundaries[0]
    return "\n".join(lines[start:])


def list_wiki_pages_from_github(token: str) -> list[str]:
    """One-level scan of wiki/ subdirectories to enumerate page basenames."""
    pages: list[str] = []
    subdirs = ["wiki/companies", "wiki/sectors", "wiki/themes", "wiki/macro",
               "wiki/concepts", "wiki/analyses", "wiki/playbooks"]
    for d in subdirs:
        for item in gh_list_dir(d, token):
            if item.get("type") == "file" and item.get("name", "").endswith(".md"):
                pages.append(item["name"][:-3])
    # Also top-level wiki/*.md
    for item in gh_list_dir("wiki", token):
        if item.get("type") == "file" and item.get("name", "").endswith(".md"):
            pages.append(item["name"][:-3])
    return sorted(set(pages))


def call_claude(api_key: str, log_md: str, index_md: str, watchlist_md: str,
                wiki_pages: list[str], skip_search: bool = False) -> dict:
    try:
        from anthropic import Anthropic  # type: ignore
    except ImportError:
        raise RuntimeError("anthropic SDK missing from Lambda package")
    client = Anthropic(api_key=api_key)
    today_iso = dt.datetime.utcnow().date().isoformat()
    tools = []
    if not skip_search:
        tools = [{"type": "web_search_20250305", "name": "web_search",
                  "max_uses": ANTHROPIC_WEB_SEARCH_MAX_USES}]
    user_msg = (
        f"Today (UTC): {today_iso}\n\n"
        f"=== CURRENT index.md ===\n{index_md}\n\n"
        f"=== RECENT log.md (last entries) ===\n{tail_log_entries(log_md)}\n\n"
        f"=== watchlist.md ===\n{watchlist_md[:8000]}\n\n"
        f"=== WIKI PAGE BASENAMES (use these in [[wikilinks]]) ===\n"
        f"{', '.join(wiki_pages)}\n\n"
        f"Run the daily update workflow and return the JSON object."
    )
    logger.info("calling anthropic model=%s tokens_input~%d", ANTHROPIC_MODEL, len(user_msg))
    resp = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=ANTHROPIC_MAX_TOKENS,
        system=SYSTEM_PROMPT,
        tools=tools,
        messages=[{"role": "user", "content": user_msg}],
    )
    text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text").strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```\s*$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        logger.error("model JSON parse failed: %s; raw=%s", e, text[:1000])
        raise


# ---------------------------------------------------------------------------
# Plan application (GitHub writes)
# ---------------------------------------------------------------------------

def apply_plan(plan: dict, token: str, current_log: str, current_log_sha: str | None) -> str:
    """Apply the Claude plan to the repo. Returns the new log.md content."""
    today_iso = dt.datetime.utcnow().date().isoformat()
    write_count = 0

    # 1. Source summaries (creates only; skip if file exists)
    for s in plan.get("source_summaries", []):
        path = s.get("path", "").strip()
        content = s.get("content", "")
        if not path.startswith("sources/") or not content:
            continue
        existing, sha = gh_get_file(path, token)
        if sha is not None:
            logger.info("source summary already exists, skipping: %s", path)
            continue
        if not content.endswith("\n"):
            content += "\n"
        gh_put_file(path, content, f"Daily auto-update: source summary {today_iso}",
                    token, sha=None)
        logger.info("wrote source summary: %s", path)
        write_count += 1

    # 2. Wiki appends (insert immediately after named heading)
    for a in plan.get("wiki_appends", []):
        path = a.get("path", "").strip()
        heading = a.get("after_heading", "").strip()
        content = a.get("content", "").strip()
        if not path.startswith("wiki/") or not heading or not content:
            continue
        existing, sha = gh_get_file(path, token)
        if sha is None:
            logger.warning("wiki page not found: %s", path)
            continue
        pattern = re.compile(rf"^(##+ {re.escape(heading)}\s*\n)", re.MULTILINE)
        if not pattern.search(existing):
            logger.warning("heading %r not found in %s", heading, path)
            continue
        new_content = pattern.sub(rf"\1\n{content}\n", existing, count=1)
        gh_put_file(path, new_content, f"Daily auto-update: append to {path} {today_iso}",
                    token, sha=sha)
        logger.info("appended to wiki page: %s", path)
        write_count += 1

    # 3. Log entry (prepend after the first --- separator)
    log_body = plan.get("log_entry_body", "").strip()
    if log_body:
        title = (plan.get("summary_one_liner") or "auto-update").strip() or "auto-update"
        entry = f"## [{today_iso}] daily | {title}\n\n{log_body}\n\n---\n\n"
        m = re.search(r"^---\s*$", current_log, re.MULTILINE)
        if m:
            insertion_point = m.end() + 1
            new_log = current_log[:insertion_point] + "\n" + entry + current_log[insertion_point:]
        else:
            new_log = current_log + "\n" + entry
        gh_put_file(LOG_PATH_IN_REPO, new_log,
                    f"Daily auto-update: log entry {today_iso}",
                    token, sha=current_log_sha)
        logger.info("wrote log entry: [%s] %s", today_iso, title)
        write_count += 1
        return new_log

    return current_log


# ---------------------------------------------------------------------------
# Pull-quote scan (recent sources/, GitHub-API edition)
# ---------------------------------------------------------------------------

def fetch_recent_pull_quote(token: str, days_back: int = 14) -> dict | None:
    cutoff = dt.date.today() - dt.timedelta(days=days_back)
    items = gh_list_dir("sources", token)
    candidates: list[tuple[dt.date, dict]] = []
    for item in items:
        name = item.get("name", "")
        m = re.match(r"^(\d{4}-\d{2}-\d{2})-", name)
        if not m:
            continue
        try:
            file_date = dt.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if file_date < cutoff:
            continue
        # Fetch via raw endpoint to avoid base64 round-trip
        text, _ = gh_get_file(f"sources/{name}", token)
        result = de.extract_pull_quote_from_text(name, text)
        if result is not None:
            candidates.append((file_date, result))
    if not candidates:
        return None
    candidates.sort(key=lambda c: c[0], reverse=True)
    return candidates[0][1]


# ---------------------------------------------------------------------------
# Email rendering + send
# ---------------------------------------------------------------------------

def render_and_send_email(new_log: str, watchlist_md: str, recipient: str,
                          token: str, dry_run: bool = False) -> dict:
    entries = de.extract_entries(new_log)
    if not entries:
        raise RuntimeError("no log entries to render")
    entry = max(entries, key=lambda e: e["date"])
    tiers = de.parse_watchlist_text(watchlist_md)
    picks = de.select_top_picks(tiers, n=7, log_text=new_log)
    pull_quote = fetch_recent_pull_quote(token)
    html = de.render_overview_html(entry, picks, pull_quote, "editorial")
    subject = f"[Investing Wiki] {entry['date']} — {entry['title'][:90]}"

    if dry_run:
        logger.info("dry-run: would send subject=%r to=%s (html len=%d)",
                    subject, recipient, len(html))
        return {"sent": False, "subject": subject, "html_length": len(html)}

    resp = _ses_client.send_email(
        FromEmailAddress=SES_SENDER,
        Destination={"ToAddresses": [recipient]},
        Content={
            "Simple": {
                "Subject": {"Data": subject, "Charset": "UTF-8"},
                "Body": {
                    "Html": {"Data": html, "Charset": "UTF-8"},
                    "Text": {"Data": "HTML email — open in an HTML-capable client.",
                             "Charset": "UTF-8"},
                },
            }
        },
    )
    message_id = resp.get("MessageId", "<unknown>")
    logger.info("ses sent: from=%s to=%s message_id=%s",
                SES_SENDER, recipient, message_id)
    return {"sent": True, "subject": subject, "message_id": message_id}


# ---------------------------------------------------------------------------
# Lambda entry point
# ---------------------------------------------------------------------------

def handler(event, context):
    started = time.time()
    event = event or {}
    skip_update = bool(event.get("skip_update", False))
    send_email = bool(event.get("send_email", True))
    dry_run = bool(event.get("dry_run", False))
    recipient = event.get("email_to") or EMAIL_TO_DEFAULT

    logger.info("invocation start: skip_update=%s send_email=%s dry_run=%s recipient=%s",
                skip_update, send_email, dry_run, recipient)

    github_token = get_secret(SECRET_GITHUB_ID, "token")

    # 1. Read repo state
    log_md, log_sha = gh_get_file(LOG_PATH_IN_REPO, github_token)
    index_md, _ = gh_get_file(INDEX_PATH, github_token)
    watchlist_md, _ = gh_get_file(WATCHLIST_PATH, github_token)

    # 2. (Optional) Daily research via Claude
    if not skip_update:
        anthropic_key = get_secret(SECRET_ANTHROPIC_ID, "api_key")
        wiki_pages = list_wiki_pages_from_github(github_token)
        plan = call_claude(anthropic_key, log_md, index_md, watchlist_md, wiki_pages)
        if dry_run:
            return {
                "status": "dry_run_plan",
                "plan_summary": plan.get("summary_one_liner"),
                "source_count": len(plan.get("source_summaries", [])),
                "append_count": len(plan.get("wiki_appends", [])),
                "elapsed_seconds": round(time.time() - started, 2),
            }
        log_md = apply_plan(plan, github_token, log_md, log_sha)

    # 3. Email (uses possibly-updated log_md from step 2)
    email_result = {"sent": False, "skipped": True}
    if send_email:
        email_result = render_and_send_email(log_md, watchlist_md, recipient,
                                             github_token, dry_run=dry_run)

    elapsed = round(time.time() - started, 2)
    logger.info("invocation done in %ss; email=%s", elapsed, email_result)
    return {
        "status": "ok",
        "skip_update": skip_update,
        "email": email_result,
        "elapsed_seconds": elapsed,
    }
