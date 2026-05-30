#!/usr/bin/env python3
"""Render the latest daily-update log entry as styled HTML and email it.

Pulls the most recent `## [YYYY-MM-DD] daily|analysis|earnings|note | ...` block
from log.md, converts it to HTML using a small stdlib markdown subset (enough
for the kind of markdown the wiki produces), wraps it in a styled template,
and sends it via Gmail SMTP or AWS SES.

Usage:
    python scripts/daily_email.py                  # send latest daily entry
    python scripts/daily_email.py --dry-run        # print HTML to stdout, don't send
    python scripts/daily_email.py --date 2026-05-27 # send a specific entry
    python scripts/daily_email.py --type all       # include any entry, not just `daily`
    python scripts/daily_email.py --to other@example.com
    python scripts/daily_email.py --backend ses    # force SES (default: env EMAIL_BACKEND, fallback smtp)

Env — pick ONE backend:

  AWS SES (recommended; uses your default boto3 credentials chain):
    EMAIL_BACKEND=ses
    SES_SENDER          # verified SES identity, e.g. "wiki@decideai.xyz"
    AWS_REGION          # optional, defaults to us-east-1
    EMAIL_TO            # default recipient

  Gmail SMTP:
    EMAIL_BACKEND=smtp
    GMAIL_USER          # the sending Gmail address
    GMAIL_APP_PASSWORD  # https://myaccount.google.com/apppasswords
    EMAIL_TO            # default recipient

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
    # 2. [[wikilink]] → italicized chip (class targeted by both CSS and inliner)
    s = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]",
               lambda m: f'<span class="wiki-wikilink">{m.group(2) or m.group(1)}</span>', s)
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


# ----------------- styled email template (light, email-client-safe) -----------------
#
# Design notes:
# - Light background + dark text — readable in both light AND dark mode email
#   clients without inverting the user's expectations.
# - Inlined critical styles on each element (in addition to the <style> block)
#   because Gmail mobile and several other clients strip or limit <style>.
# - No backdrop-filter, no rgba on backgrounds, no flexbox/grid — desktop and
#   mobile webmail render these inconsistently.
# - System font stack so Apple/Google clients use native typefaces.
# - max-width 680px is the Stratechery/Substack convention; comfortable line
#   length on desktop, doesn't break mobile.
# - Code/wikilink chips use solid pastel backgrounds (not rgba) so they
#   survive client-side CSS stripping.

EMAIL_CSS = """
body { margin: 0; padding: 0; background-color: #f6f7f9; color: #1f2933; font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif; line-height: 1.55; }
.wiki-wrap { max-width: 680px; margin: 0 auto; padding: 28px 16px 40px; }
.wiki-card { background-color: #ffffff; border: 1px solid #e2e6ec; border-radius: 8px; padding: 32px 32px 28px; }
.wiki-kicker { color: #2563eb; text-transform: uppercase; letter-spacing: 1.2px; font-size: 11px; font-weight: 700; margin: 0 0 8px; }
.wiki-headline { color: #0f172a; font-size: 24px; line-height: 1.3; margin: 0 0 8px; font-weight: 700; }
.wiki-meta { color: #64748b; font-size: 13px; margin: 0 0 24px; padding-bottom: 16px; border-bottom: 1px solid #e2e6ec; }
.wiki-content h2 { color: #0f172a; font-size: 20px; font-weight: 700; margin: 28px 0 10px; padding-bottom: 6px; border-bottom: 1px solid #e2e6ec; }
.wiki-content h3 { color: #1e293b; font-size: 16.5px; font-weight: 700; margin: 22px 0 8px; }
.wiki-content h4 { color: #334155; font-size: 13px; font-weight: 700; margin: 18px 0 6px; text-transform: uppercase; letter-spacing: 0.5px; }
.wiki-content p, .wiki-content li { color: #1f2933; font-size: 15px; }
.wiki-content p { margin: 0 0 12px; }
.wiki-content ul { padding-left: 22px; margin: 8px 0 14px; }
.wiki-content li { margin: 0 0 6px; }
.wiki-content blockquote { border-left: 3px solid #2563eb; padding: 10px 16px; background-color: #eff4ff; margin: 14px 0; border-radius: 0 4px 4px 0; }
.wiki-content blockquote p { margin: 4px 0; color: #1e3a8a; font-style: italic; }
.wiki-content code { background-color: #f1f5f9; padding: 1px 6px; border-radius: 3px; font-size: 13px; color: #0f172a; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
.wiki-content pre { background-color: #f8fafc; padding: 14px 16px; border-radius: 6px; border: 1px solid #e2e6ec; overflow-x: auto; }
.wiki-content pre code { background: none; padding: 0; font-size: 12.5px; color: #1e293b; }
.wiki-content table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 13.5px; }
.wiki-content th, .wiki-content td { padding: 8px 10px; text-align: left; border: 1px solid #e2e6ec; vertical-align: top; color: #1f2933; }
.wiki-content th { background-color: #f8fafc; color: #0f172a; font-weight: 700; }
.wiki-content tr:nth-child(even) td { background-color: #fbfcfd; }
.wiki-content a { color: #2563eb; text-decoration: underline; }
.wiki-content a:hover { color: #1e40af; }
.wiki-wikilink { color: #b45309; background-color: #fef3c7; padding: 0 5px; border-radius: 3px; font-size: 13px; font-style: italic; font-weight: 500; }
.wiki-content hr { border: 0; height: 1px; background-color: #e2e6ec; margin: 22px 0; }
.wiki-content strong { color: #0f172a; font-weight: 700; }
.wiki-content em { color: #334155; }
.wiki-footer { color: #94a3b8; font-size: 11.5px; text-align: center; margin-top: 18px; padding: 0 16px; }
.wiki-footer a { color: #64748b; }
"""


# Inline-style fallbacks for clients that strip <style>. Applied where they
# matter most (the chip/wikilink/headline elements).
_INLINE = {
    "body":      'margin:0;padding:0;background-color:#f6f7f9;color:#1f2933;font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;line-height:1.55;',
    "wrap":      "max-width:680px;margin:0 auto;padding:28px 16px 40px;",
    "card":      "background-color:#ffffff;border:1px solid #e2e6ec;border-radius:8px;padding:32px 32px 28px;",
    "kicker":    "color:#2563eb;text-transform:uppercase;letter-spacing:1.2px;font-size:11px;font-weight:700;margin:0 0 8px;",
    "headline":  "color:#0f172a;font-size:24px;line-height:1.3;margin:0 0 8px;font-weight:700;",
    "meta":      "color:#64748b;font-size:13px;margin:0 0 24px;padding-bottom:16px;border-bottom:1px solid #e2e6ec;",
    "footer":    "color:#94a3b8;font-size:11.5px;text-align:center;margin-top:18px;padding:0 16px;",
}


def _inline_wikilinks(html: str) -> str:
    """Apply inline style to .wiki-wikilink chips for clients that strip CSS."""
    return html.replace(
        '<span class="wiki-wikilink">',
        '<span class="wiki-wikilink" style="color:#b45309;background-color:#fef3c7;padding:0 5px;border-radius:3px;font-size:13px;font-style:italic;font-weight:500;">'
    ).replace(
        '<code>',
        '<code style="background-color:#f1f5f9;padding:1px 6px;border-radius:3px;font-size:13px;color:#0f172a;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;">'
    ).replace(
        '<strong>',
        '<strong style="color:#0f172a;font-weight:700;">'
    )


def render_html(entry: dict) -> str:
    html_body = _inline_wikilinks(markdown_to_html(entry["body"]))
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<meta name="color-scheme" content="light only"/>
<meta name="supported-color-schemes" content="light"/>
<title>Wiki update — {entry['date']}</title>
<style>{EMAIL_CSS}</style>
</head>
<body style="{_INLINE['body']}">
  <div class="wiki-wrap" style="{_INLINE['wrap']}">
    <div class="wiki-card" style="{_INLINE['card']}">
      <div class="wiki-kicker" style="{_INLINE['kicker']}">Investing Wiki · {entry['type']}</div>
      <h1 class="wiki-headline" style="{_INLINE['headline']}">{_escape(entry['title'])}</h1>
      <div class="wiki-meta" style="{_INLINE['meta']}">{entry['date']} · auto-rendered from <code style="background-color:#f1f5f9;padding:1px 6px;border-radius:3px;font-size:13px;color:#0f172a;">log.md</code></div>
      <div class="wiki-content">{html_body}</div>
    </div>
    <div class="wiki-footer" style="{_INLINE['footer']}">Generated by <code style="background-color:#f1f5f9;padding:1px 6px;border-radius:3px;color:#0f172a;">scripts/daily_email.py</code> · <a href="https://github.com/rgovindji/wiki_research" style="color:#64748b;">repo</a></div>
  </div>
</body></html>"""


def send_email_smtp(html: str, subject: str, recipient: str) -> None:
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
    msg.attach(MIMEText("HTML email — open in an HTML-capable client.", "plain", "utf-8"))
    msg.attach(MIMEText(html, "html", "utf-8"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as s:
        s.login(user, password)
        s.sendmail(user, [recipient], msg.as_string())
    print(f"[email] smtp sent: from={user} to={recipient}")


def send_email_ses(html: str, subject: str, recipient: str) -> None:
    sender = os.environ.get("SES_SENDER")
    if not sender:
        raise SystemExit(
            "[email] SES_SENDER must be set to a verified SES identity. "
            "List your verified identities with: aws ses list-identities"
        )
    try:
        import boto3  # type: ignore
        from botocore.exceptions import ClientError  # type: ignore
    except ImportError:
        raise SystemExit(
            "[email] boto3 not installed. Run: pip install boto3"
        )
    region = os.environ.get("AWS_REGION", "us-east-1")
    client = boto3.client("sesv2", region_name=region)
    try:
        resp = client.send_email(
            FromEmailAddress=sender,
            Destination={"ToAddresses": [recipient]},
            Content={
                "Simple": {
                    "Subject": {"Data": subject, "Charset": "UTF-8"},
                    "Body": {
                        "Html": {"Data": html, "Charset": "UTF-8"},
                        "Text": {"Data": "HTML email — open in an HTML-capable client.", "Charset": "UTF-8"},
                    },
                }
            },
        )
        message_id = resp.get("MessageId", "<unknown>")
        print(f"[email] ses sent: from={sender} to={recipient} message_id={message_id}")
    except ClientError as e:
        code = e.response.get("Error", {}).get("Code", "?")
        msg = e.response.get("Error", {}).get("Message", str(e))
        if code == "MessageRejected" and "not verified" in msg.lower():
            print(f"[email] SES rejected: {msg}", file=sys.stderr)
            print(f"[email] verify the sender first:", file=sys.stderr)
            print(f"  aws ses verify-email-identity --email-address {sender} --region {region}", file=sys.stderr)
            print(f"  (or use sesv2 create-email-identity)", file=sys.stderr)
        else:
            print(f"[email] SES error [{code}]: {msg}", file=sys.stderr)
        raise SystemExit(1)


def send_email(html: str, subject: str, recipient: str, backend: str) -> None:
    if backend == "ses":
        send_email_ses(html, subject, recipient)
    elif backend == "smtp":
        send_email_smtp(html, subject, recipient)
    else:
        raise SystemExit(f"[email] unknown backend: {backend!r} (use 'ses' or 'smtp')")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Render+email the latest daily log entry")
    p.add_argument("--date", help="YYYY-MM-DD — pick a specific entry instead of latest")
    p.add_argument("--type", default="daily,analysis,earnings,ingest,research",
                   help="comma-separated entry types to include; use 'all' to include any")
    p.add_argument("--to", help="recipient email (overrides EMAIL_TO env)")
    p.add_argument("--backend", choices=["ses", "smtp"], help="email backend (overrides EMAIL_BACKEND env; default ses)")
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
    backend = args.backend or os.environ.get("EMAIL_BACKEND", "ses")
    print(f"[email] sending via {backend.upper()}: {subject!r} → {recipient}")
    send_email(html, subject, recipient, backend)
    return 0


if __name__ == "__main__":
    sys.exit(main())
