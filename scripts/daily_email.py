#!/usr/bin/env python3
"""Render the latest daily-update log entry as styled HTML and email it.

Pulls the most recent `## [YYYY-MM-DD] daily|analysis|earnings|note | ...` block
from log.md, converts it to HTML using a small stdlib markdown subset (enough
for the kind of markdown the wiki produces), wraps it in a styled template,
and sends it via Gmail SMTP using an App Password.

Usage:
    python scripts/daily_email.py                  # send latest daily entry
    python scripts/daily_email.py --dry-run        # print HTML to stdout, don't send
    python scripts/daily_email.py --date 2026-05-27 # send a specific entry
    python scripts/daily_email.py --type all       # include any entry, not just `daily`
    python scripts/daily_email.py --to other@example.com

Env (required for send):
    GMAIL_USER             # the sending Gmail address
    GMAIL_APP_PASSWORD     # https://myaccount.google.com/apppasswords
    EMAIL_TO               # default recipient (overridden by --to)

The script never logs the password and never writes secrets to disk.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = REPO_ROOT / "log.md"

ENTRY_RE = re.compile(
    r"^## \[(?P<date>\d{4}-\d{2}-\d{2})\] (?P<type>[\w\-]+) \| (?P<title>.+?)$",
    re.MULTILINE,
)


def load_dotenv(path: Path) -> None:
    """Tiny .env loader so we don't add python-dotenv as a hard dep."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def extract_entries(text: str) -> list[dict]:
    """Return list of {date, type, title, body} for every log entry."""
    matches = list(ENTRY_RE.finditer(text))
    entries: list[dict] = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        # Strip the trailing "---" separator if present
        body = re.sub(r"\n\s*---\s*$", "", body).strip()
        entries.append({
            "date": m.group("date"),
            "type": m.group("type"),
            "title": m.group("title").strip(),
            "body": body,
        })
    return entries


def pick_entry(entries: list[dict], target_date: str | None, allowed_types: set[str]) -> dict | None:
    pool = [e for e in entries if e["type"] in allowed_types or "all" in allowed_types]
    if target_date:
        for e in pool:
            if e["date"] == target_date:
                return e
        return None
    # Otherwise pick most recent
    pool.sort(key=lambda e: e["date"], reverse=True)
    return pool[0] if pool else None


# ----------------- minimal markdown → HTML (no external deps) -----------------

def _escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _render_inline(s: str) -> str:
    # 1. Escape first so we never inject raw HTML from the markdown.
    s = _escape(s)
    # 2. [[wikilink]] → italicized chip
    s = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]",
               lambda m: f'<span class="wikilink">{m.group(2) or m.group(1)}</span>', s)
    # 3. [text](url) link
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)",
               r'<a href="\2">\1</a>', s)
    # 4. **bold**
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    # 5. *italic*
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    # 6. `code`
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def markdown_to_html(md: str) -> str:
    """Just enough markdown to render wiki log entries cleanly.

    Supports: paragraphs, headings (## ### ####), unordered lists (- or *),
    fenced code blocks, blockquotes (>), GitHub-flavored tables, horizontal
    rules. Other constructs degrade to escaped text.
    """
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    in_list = False
    in_blockquote = False

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    def close_blockquote():
        nonlocal in_blockquote
        if in_blockquote:
            out.append("</blockquote>")
            in_blockquote = False

    while i < len(lines):
        line = lines[i]
        # Fenced code
        if line.strip().startswith("```"):
            close_list(); close_blockquote()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            out.append(f"<pre><code>{_escape(chr(10).join(buf))}</code></pre>")
            i += 1
            continue
        # Tables (header | --- | header pattern)
        if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|?[\s\-|:]+\|[\s\-|:]+\|?\s*$", lines[i + 1]):
            close_list(); close_blockquote()
            header_cells = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            html = ["<table>", "<thead><tr>"]
            html.extend(f"<th>{_render_inline(h)}</th>" for h in header_cells)
            html.append("</tr></thead><tbody>")
            for r in rows:
                html.append("<tr>")
                html.extend(f"<td>{_render_inline(c)}</td>" for c in r)
                html.append("</tr>")
            html.append("</tbody></table>")
            out.append("".join(html))
            continue
        # Horizontal rule
        if re.match(r"^\s*---+\s*$", line):
            close_list(); close_blockquote()
            out.append("<hr/>")
            i += 1
            continue
        # Heading
        m = re.match(r"^(#{2,6})\s+(.*)$", line)
        if m:
            close_list(); close_blockquote()
            level = len(m.group(1))
            out.append(f"<h{level}>{_render_inline(m.group(2).strip())}</h{level}>")
            i += 1
            continue
        # Blockquote
        if line.startswith("> "):
            close_list()
            if not in_blockquote:
                out.append("<blockquote>")
                in_blockquote = True
            out.append(f"<p>{_render_inline(line[2:])}</p>")
            i += 1
            continue
        # List item
        lm = re.match(r"^\s*[-*]\s+(.*)$", line)
        if lm:
            close_blockquote()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{_render_inline(lm.group(1))}</li>")
            i += 1
            continue
        # Empty line: close blocks, no <p/>
        if not line.strip():
            close_list(); close_blockquote()
            i += 1
            continue
        # Default paragraph
        close_list(); close_blockquote()
        out.append(f"<p>{_render_inline(line.strip())}</p>")
        i += 1

    close_list(); close_blockquote()
    return "\n".join(out)


# ----------------- styled email template (dark glass aesthetic) -----------------

EMAIL_CSS = """
body { margin: 0; padding: 0; background: #0a1a2f; font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif; color: #e8eef7; line-height: 1.55; }
.wrap { max-width: 760px; margin: 0 auto; padding: 32px 20px 60px; }
.card { background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.10); border-radius: 14px; padding: 28px 28px 24px; backdrop-filter: blur(8px); }
.kicker { color: #6da9ff; text-transform: uppercase; letter-spacing: 1.4px; font-size: 11px; font-weight: 600; margin-bottom: 8px; }
.headline { color: #ffffff; font-size: 26px; line-height: 1.25; margin: 0 0 6px; font-weight: 700; }
.meta { color: #8aa0c1; font-size: 13px; margin-bottom: 22px; }
.content h2 { color: #ffffff; font-size: 22px; margin-top: 28px; margin-bottom: 10px; border-bottom: 1px solid rgba(255, 255, 255, 0.10); padding-bottom: 6px; }
.content h3 { color: #f0f4fa; font-size: 18px; margin-top: 24px; margin-bottom: 8px; }
.content h4 { color: #cad7ec; font-size: 15px; margin-top: 18px; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.6px; }
.content p, .content li { color: #dde6f3; font-size: 14.5px; }
.content ul { padding-left: 22px; }
.content blockquote { border-left: 3px solid #6da9ff; padding: 6px 14px; background: rgba(109, 169, 255, 0.06); margin: 14px 0; border-radius: 4px; }
.content blockquote p { margin: 4px 0; color: #c9d6ea; font-style: italic; }
.content code { background: rgba(255, 255, 255, 0.08); padding: 1px 6px; border-radius: 3px; font-size: 13px; color: #aed6ff; }
.content pre { background: rgba(0, 0, 0, 0.35); padding: 12px 14px; border-radius: 6px; overflow-x: auto; }
.content pre code { background: none; padding: 0; color: #c8d8ef; font-size: 12.5px; }
.content table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 13.5px; }
.content th, .content td { padding: 8px 10px; text-align: left; border-bottom: 1px solid rgba(255, 255, 255, 0.10); vertical-align: top; }
.content th { color: #aed6ff; font-weight: 600; }
.content a { color: #6da9ff; text-decoration: none; border-bottom: 1px dotted rgba(109, 169, 255, 0.5); }
.content a:hover { border-bottom-style: solid; }
.wikilink { color: #ffd596; font-style: italic; background: rgba(255, 213, 150, 0.08); padding: 0 4px; border-radius: 3px; font-size: 13px; }
.content hr { border: 0; height: 1px; background: rgba(255, 255, 255, 0.08); margin: 22px 0; }
.footer { color: #6981a3; font-size: 11.5px; text-align: center; margin-top: 22px; }
.footer a { color: #6da9ff; }
"""


def render_html(entry: dict) -> str:
    html_body = markdown_to_html(entry["body"])
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"/><title>Wiki update — {entry['date']}</title>
<style>{EMAIL_CSS}</style></head>
<body>
  <div class="wrap">
    <div class="card">
      <div class="kicker">Investing Wiki · {entry['type']}</div>
      <h1 class="headline">{_escape(entry['title'])}</h1>
      <div class="meta">{entry['date']} · auto-rendered from <code>log.md</code></div>
      <div class="content">{html_body}</div>
    </div>
    <div class="footer">Generated by <code>scripts/daily_email.py</code> · <a href="https://github.com/rgovindji/wiki_research">repo</a></div>
  </div>
</body></html>"""


def send_email(html: str, subject: str, recipient: str) -> None:
    user = os.environ.get("GMAIL_USER")
    password = os.environ.get("GMAIL_APP_PASSWORD")
    if not user or not password:
        raise SystemExit(
            "[email] GMAIL_USER and GMAIL_APP_PASSWORD must be set (see scripts/.env.example)"
        )
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = recipient
    # Plaintext fallback: just send the markdown
    plain = MIMEText("HTML email — open in an HTML-capable client.", "plain", "utf-8")
    msg.attach(plain)
    msg.attach(MIMEText(html, "html", "utf-8"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as s:
        s.login(user, password)
        s.sendmail(user, [recipient], msg.as_string())


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Render+email the latest daily log entry")
    p.add_argument("--date", help="YYYY-MM-DD — pick a specific entry instead of latest")
    p.add_argument("--type", default="daily,analysis,earnings,ingest,research",
                   help="comma-separated entry types to include; use 'all' to include any")
    p.add_argument("--to", help="recipient email (overrides EMAIL_TO env)")
    p.add_argument("--dry-run", action="store_true", help="print HTML to stdout instead of sending")
    p.add_argument("--save", help="also save the HTML to this path")
    args = p.parse_args(argv)

    load_dotenv(REPO_ROOT / ".env")
    load_dotenv(REPO_ROOT / "scripts" / ".env")

    if not LOG_PATH.exists():
        print(f"[email] log.md not found at {LOG_PATH}", file=sys.stderr)
        return 1
    entries = extract_entries(LOG_PATH.read_text(encoding="utf-8"))
    if not entries:
        print("[email] no entries found in log.md", file=sys.stderr)
        return 1
    allowed = set(t.strip() for t in args.type.split(","))
    entry = pick_entry(entries, args.date, allowed)
    if entry is None:
        print(f"[email] no matching entry (date={args.date} types={allowed})", file=sys.stderr)
        return 1

    html = render_html(entry)
    subject = f"[Wiki] {entry['date']} {entry['type']}: {entry['title'][:80]}"

    if args.save:
        Path(args.save).write_text(html, encoding="utf-8")
        print(f"[email] HTML saved to {args.save}")

    if args.dry_run:
        sys.stdout.write(html)
        return 0

    recipient = args.to or os.environ.get("EMAIL_TO")
    if not recipient:
        print("[email] no recipient (set EMAIL_TO or pass --to)", file=sys.stderr)
        return 1
    print(f"[email] sending {subject!r} to {recipient}")
    send_email(html, subject, recipient)
    print("[email] sent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
