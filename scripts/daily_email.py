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


# ----------------- email themes (all email-client-safe) -----------------
#
# Three themes. Each is a complete (css, inline_attrs, chip_styles, meta) bundle.
# Pick via --theme CLI or EMAIL_THEME env var.
#
# Email-client constraints (apply to all themes):
#   - No backdrop-filter, no flexbox/grid, no @supports.
#   - Inline-style fallbacks for every chip + structural element, because
#     Gmail mobile and some other clients strip or limit <style>.
#   - Solid colors (not rgba) for backgrounds.
#   - Use scheme meta to prevent Gmail dark-mode from inverting colors.
#   - System font stacks only (no Google Fonts; outlook strips <link>).

# fmt: off
THEMES: dict[str, dict] = {
    # -------------------------------------------------------------------------
    # LIGHT — Newspaper / NYT print mode. White bg, TRUE BLACK body text,
    # heavy bold weights, saturated newspaper accents (deep red kicker,
    # rich navy links, deep amber wikilink chips). Designed for high contrast
    # and readability — no washed-out grays.
    # -------------------------------------------------------------------------
    "light": {
        "label":         "Newspaper (black + bold + saturated accents)",
        "color_scheme":  "light only",
        "css": """
body { margin: 0; padding: 0; background-color: #ffffff; color: #0a0a0a; font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif; line-height: 1.55; }
.wiki-wrap { max-width: 680px; margin: 0 auto; padding: 32px 16px 40px; }
.wiki-card { background-color: #ffffff; border: 1px solid #d4d4d4; padding: 36px 36px 30px; border-radius: 0; }
.wiki-kicker { color: #b91c1c; text-transform: uppercase; letter-spacing: 1.6px; font-size: 11px; font-weight: 700; margin: 0 0 10px; }
.wiki-headline { color: #000000; font-size: 28px; line-height: 1.25; margin: 0 0 10px; font-weight: 800; letter-spacing: -0.01em; }
.wiki-meta { color: #4b5563; font-size: 13px; margin: 0 0 26px; padding-bottom: 18px; border-bottom: 2px solid #000000; font-weight: 500; }
.wiki-content h2 { color: #000000; font-size: 22px; font-weight: 800; margin: 30px 0 12px; padding-bottom: 8px; border-bottom: 2px solid #000000; letter-spacing: -0.01em; }
.wiki-content h3 { color: #000000; font-size: 17px; font-weight: 700; margin: 22px 0 8px; }
.wiki-content h4 { color: #000000; font-size: 12.5px; font-weight: 800; margin: 18px 0 6px; text-transform: uppercase; letter-spacing: 0.8px; }
.wiki-content p, .wiki-content li { color: #0a0a0a; font-size: 15px; }
.wiki-content p { margin: 0 0 12px; }
.wiki-content ul { padding-left: 22px; margin: 8px 0 14px; }
.wiki-content li { margin: 0 0 7px; }
.wiki-content blockquote { border-left: 4px solid #b91c1c; padding: 10px 16px; background-color: #fafafa; margin: 14px 0; border-radius: 0; }
.wiki-content blockquote p { margin: 4px 0; color: #000000; font-style: italic; font-weight: 500; }
.wiki-content code { background-color: #f3f4f6; padding: 1px 6px; border-radius: 2px; font-size: 13px; color: #000000; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-weight: 600; }
.wiki-content pre { background-color: #f9fafb; padding: 14px 16px; border-radius: 2px; border: 1px solid #d4d4d4; overflow-x: auto; }
.wiki-content pre code { background: none; padding: 0; font-size: 12.5px; color: #000000; font-weight: 500; }
.wiki-content table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 13.5px; }
.wiki-content th, .wiki-content td { padding: 8px 10px; text-align: left; border: 1px solid #000000; vertical-align: top; color: #0a0a0a; }
.wiki-content th { background-color: #000000; color: #ffffff; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; font-size: 11.5px; }
.wiki-content tr:nth-child(even) td { background-color: #f9fafb; }
.wiki-content a { color: #1e3a8a; text-decoration: underline; font-weight: 600; }
.wiki-content a:hover { color: #1e40af; }
.wiki-wikilink { color: #78350f; background-color: #fde68a; padding: 1px 6px; border-radius: 2px; font-size: 13px; font-style: normal; font-weight: 700; }
.wiki-content hr { border: 0; height: 2px; background-color: #000000; margin: 24px 0; }
.wiki-content strong { color: #000000; font-weight: 800; }
.wiki-content em { color: #0a0a0a; font-style: italic; }
.wiki-footer { color: #4b5563; font-size: 11.5px; text-align: center; margin-top: 22px; padding: 0 16px; font-weight: 500; }
.wiki-footer a { color: #1e3a8a; font-weight: 600; }
""",
        "inline": {
            "body":      'margin:0;padding:0;background-color:#ffffff;color:#0a0a0a;font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;line-height:1.55;',
            "wrap":      "max-width:680px;margin:0 auto;padding:32px 16px 40px;",
            "card":      "background-color:#ffffff;border:1px solid #d4d4d4;padding:36px 36px 30px;border-radius:0;",
            "kicker":    "color:#b91c1c;text-transform:uppercase;letter-spacing:1.6px;font-size:11px;font-weight:700;margin:0 0 10px;",
            "headline":  "color:#000000;font-size:28px;line-height:1.25;margin:0 0 10px;font-weight:800;letter-spacing:-0.01em;",
            "meta":      "color:#4b5563;font-size:13px;margin:0 0 26px;padding-bottom:18px;border-bottom:2px solid #000000;font-weight:500;",
            "footer":    "color:#4b5563;font-size:11.5px;text-align:center;margin-top:22px;padding:0 16px;font-weight:500;",
            "footer_link": "color:#1e3a8a;font-weight:600;",
            "meta_code": "background-color:#f3f4f6;padding:1px 6px;border-radius:2px;font-size:13px;color:#000000;font-weight:600;",
        },
        "chip_styles": {
            "wikilink": "color:#78350f;background-color:#fde68a;padding:1px 6px;border-radius:2px;font-size:13px;font-style:normal;font-weight:700;",
            "code":     "background-color:#f3f4f6;padding:1px 6px;border-radius:2px;font-size:13px;color:#000000;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-weight:600;",
            "strong":   "color:#000000;font-weight:800;",
        },
    },

    # -------------------------------------------------------------------------
    # MUTED-DARK — Cursor / Linear / GitHub-dark.
    # Low-contrast dark for long reads. Bg #0d1117, card visible at #161b22.
    # -------------------------------------------------------------------------
    "muted-dark": {
        "label":         "Muted dark (Cursor/Linear/GitHub-dark)",
        "color_scheme":  "dark only",
        "css": """
body { margin: 0; padding: 0; background-color: #0d1117; color: #c9d1d9; font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif; line-height: 1.55; }
.wiki-wrap { max-width: 680px; margin: 0 auto; padding: 28px 16px 40px; }
.wiki-card { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 32px 32px 28px; }
.wiki-kicker { color: #79c0ff; text-transform: uppercase; letter-spacing: 1.2px; font-size: 11px; font-weight: 700; margin: 0 0 8px; }
.wiki-headline { color: #f0f6fc; font-size: 24px; line-height: 1.3; margin: 0 0 8px; font-weight: 700; }
.wiki-meta { color: #8b949e; font-size: 13px; margin: 0 0 24px; padding-bottom: 16px; border-bottom: 1px solid #30363d; }
.wiki-content h2 { color: #f0f6fc; font-size: 20px; font-weight: 700; margin: 28px 0 10px; padding-bottom: 6px; border-bottom: 1px solid #30363d; }
.wiki-content h3 { color: #e6edf3; font-size: 16.5px; font-weight: 700; margin: 22px 0 8px; }
.wiki-content h4 { color: #b1bac4; font-size: 13px; font-weight: 700; margin: 18px 0 6px; text-transform: uppercase; letter-spacing: 0.5px; }
.wiki-content p, .wiki-content li { color: #c9d1d9; font-size: 15px; }
.wiki-content p { margin: 0 0 12px; }
.wiki-content ul { padding-left: 22px; margin: 8px 0 14px; }
.wiki-content li { margin: 0 0 6px; }
.wiki-content blockquote { border-left: 3px solid #79c0ff; padding: 10px 16px; background-color: #1c2128; margin: 14px 0; border-radius: 0 4px 4px 0; }
.wiki-content blockquote p { margin: 4px 0; color: #c9d1d9; font-style: italic; }
.wiki-content code { background-color: #1f2937; padding: 1px 6px; border-radius: 3px; font-size: 13px; color: #a5b4fc; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
.wiki-content pre { background-color: #0a0e14; padding: 14px 16px; border-radius: 6px; border: 1px solid #30363d; overflow-x: auto; }
.wiki-content pre code { background: none; padding: 0; font-size: 12.5px; color: #c9d1d9; }
.wiki-content table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 13.5px; }
.wiki-content th, .wiki-content td { padding: 8px 10px; text-align: left; border: 1px solid #30363d; vertical-align: top; color: #c9d1d9; }
.wiki-content th { background-color: #1c2128; color: #f0f6fc; font-weight: 700; }
.wiki-content tr:nth-child(even) td { background-color: #141a23; }
.wiki-content a { color: #79c0ff; text-decoration: underline; }
.wiki-content a:hover { color: #a8d2ff; }
.wiki-wikilink { color: #d2a8ff; background-color: #2d2046; padding: 0 5px; border-radius: 3px; font-size: 13px; font-style: italic; font-weight: 500; }
.wiki-content hr { border: 0; height: 1px; background-color: #30363d; margin: 22px 0; }
.wiki-content strong { color: #f0f6fc; font-weight: 700; }
.wiki-content em { color: #b1bac4; }
.wiki-footer { color: #6e7681; font-size: 11.5px; text-align: center; margin-top: 18px; padding: 0 16px; }
.wiki-footer a { color: #8b949e; }
""",
        "inline": {
            "body":      'margin:0;padding:0;background-color:#0d1117;color:#c9d1d9;font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;line-height:1.55;',
            "wrap":      "max-width:680px;margin:0 auto;padding:28px 16px 40px;",
            "card":      "background-color:#161b22;border:1px solid #30363d;border-radius:8px;padding:32px 32px 28px;",
            "kicker":    "color:#79c0ff;text-transform:uppercase;letter-spacing:1.2px;font-size:11px;font-weight:700;margin:0 0 8px;",
            "headline":  "color:#f0f6fc;font-size:24px;line-height:1.3;margin:0 0 8px;font-weight:700;",
            "meta":      "color:#8b949e;font-size:13px;margin:0 0 24px;padding-bottom:16px;border-bottom:1px solid #30363d;",
            "footer":    "color:#6e7681;font-size:11.5px;text-align:center;margin-top:18px;padding:0 16px;",
            "footer_link": "color:#8b949e;",
            "meta_code": "background-color:#1f2937;padding:1px 6px;border-radius:3px;font-size:13px;color:#a5b4fc;",
        },
        "chip_styles": {
            "wikilink": "color:#d2a8ff;background-color:#2d2046;padding:0 5px;border-radius:3px;font-size:13px;font-style:italic;font-weight:500;",
            "code":     "background-color:#1f2937;padding:1px 6px;border-radius:3px;font-size:13px;color:#a5b4fc;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;",
            "strong":   "color:#f0f6fc;font-weight:700;",
        },
    },

    # -------------------------------------------------------------------------
    # TERMINAL — Bloomberg/Reuters high-density mono.
    # Narrow column, full monospace, terminal-style orange/green/blue accents.
    # -------------------------------------------------------------------------
    "terminal": {
        "label":         "Terminal (Bloomberg high-density)",
        "color_scheme":  "dark only",
        "css": """
body { margin: 0; padding: 0; background-color: #0a0e14; color: #9ca3af; font-family: ui-monospace, "SF Mono", SFMono-Regular, "Menlo", "Consolas", monospace; line-height: 1.45; font-size: 13.5px; }
.wiki-wrap { max-width: 600px; margin: 0 auto; padding: 24px 16px 36px; }
.wiki-card { background-color: #0a0e14; border: 1px solid #1f2937; border-radius: 0; padding: 24px 24px 20px; }
.wiki-kicker { color: #fb923c; text-transform: uppercase; letter-spacing: 2px; font-size: 10px; font-weight: 700; margin: 0 0 6px; }
.wiki-headline { color: #fb923c; font-size: 18px; line-height: 1.35; margin: 0 0 8px; font-weight: 700; }
.wiki-meta { color: #6b7280; font-size: 11.5px; margin: 0 0 22px; padding-bottom: 14px; border-bottom: 1px dashed #374151; }
.wiki-content h2 { color: #fb923c; font-size: 14px; font-weight: 700; margin: 24px 0 8px; padding-bottom: 4px; border-bottom: 1px solid #374151; text-transform: uppercase; letter-spacing: 0.8px; }
.wiki-content h3 { color: #fbbf24; font-size: 13.5px; font-weight: 700; margin: 18px 0 6px; }
.wiki-content h4 { color: #34d399; font-size: 11.5px; font-weight: 700; margin: 16px 0 4px; text-transform: uppercase; letter-spacing: 0.8px; }
.wiki-content p, .wiki-content li { color: #d1d5db; font-size: 13.5px; }
.wiki-content p { margin: 0 0 10px; }
.wiki-content ul { padding-left: 18px; margin: 6px 0 12px; }
.wiki-content li { margin: 0 0 4px; }
.wiki-content blockquote { border-left: 2px solid #fb923c; padding: 8px 12px; background-color: #111827; margin: 12px 0; border-radius: 0; }
.wiki-content blockquote p { margin: 3px 0; color: #d1d5db; font-style: normal; }
.wiki-content code { background-color: #111827; padding: 1px 5px; border-radius: 0; font-size: 12.5px; color: #fbbf24; }
.wiki-content pre { background-color: #050810; padding: 12px 14px; border: 1px solid #1f2937; border-radius: 0; overflow-x: auto; }
.wiki-content pre code { background: none; padding: 0; font-size: 11.5px; color: #d1d5db; }
.wiki-content table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 12px; }
.wiki-content th, .wiki-content td { padding: 5px 8px; text-align: left; border: 1px solid #1f2937; vertical-align: top; color: #d1d5db; }
.wiki-content th { background-color: #111827; color: #fb923c; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; font-size: 10.5px; }
.wiki-content tr:nth-child(even) td { background-color: #0d131e; }
.wiki-content a { color: #60a5fa; text-decoration: underline; }
.wiki-content a:hover { color: #93c5fd; }
.wiki-wikilink { color: #34d399; background-color: #052e1c; padding: 0 4px; border-radius: 0; font-size: 12px; font-style: normal; font-weight: 600; }
.wiki-content hr { border: 0; height: 1px; background-color: #1f2937; margin: 18px 0; }
.wiki-content strong { color: #f3f4f6; font-weight: 700; }
.wiki-content em { color: #9ca3af; }
.wiki-footer { color: #4b5563; font-size: 10.5px; text-align: center; margin-top: 16px; padding: 0 16px; }
.wiki-footer a { color: #6b7280; }
""",
        "inline": {
            "body":      'margin:0;padding:0;background-color:#0a0e14;color:#9ca3af;font-family:ui-monospace,"SF Mono",SFMono-Regular,"Menlo","Consolas",monospace;line-height:1.45;font-size:13.5px;',
            "wrap":      "max-width:600px;margin:0 auto;padding:24px 16px 36px;",
            "card":      "background-color:#0a0e14;border:1px solid #1f2937;border-radius:0;padding:24px 24px 20px;",
            "kicker":    "color:#fb923c;text-transform:uppercase;letter-spacing:2px;font-size:10px;font-weight:700;margin:0 0 6px;",
            "headline":  "color:#fb923c;font-size:18px;line-height:1.35;margin:0 0 8px;font-weight:700;",
            "meta":      "color:#6b7280;font-size:11.5px;margin:0 0 22px;padding-bottom:14px;border-bottom:1px dashed #374151;",
            "footer":    "color:#4b5563;font-size:10.5px;text-align:center;margin-top:16px;padding:0 16px;",
            "footer_link": "color:#6b7280;",
            "meta_code": "background-color:#111827;padding:1px 5px;border-radius:0;font-size:12.5px;color:#fbbf24;",
        },
        "chip_styles": {
            "wikilink": "color:#34d399;background-color:#052e1c;padding:0 4px;border-radius:0;font-size:12px;font-style:normal;font-weight:600;",
            "code":     "background-color:#111827;padding:1px 5px;border-radius:0;font-size:12.5px;color:#fbbf24;",
            "strong":   "color:#f3f4f6;font-weight:700;",
        },
    },
}
# fmt: on


def get_theme(name: str | None) -> dict:
    name = (name or os.environ.get("EMAIL_THEME") or "light").lower()
    if name not in THEMES:
        raise SystemExit(
            f"[email] unknown theme {name!r}. Available: {', '.join(THEMES)}"
        )
    return THEMES[name]


def _apply_chip_styles(html: str, chips: dict) -> str:
    """Apply inline styles to .wiki-wikilink + <code> + <strong> for clients
    that strip <style>."""
    return (
        html
        .replace(
            '<span class="wiki-wikilink">',
            f'<span class="wiki-wikilink" style="{chips["wikilink"]}">',
        )
        .replace("<code>", f'<code style="{chips["code"]}">')
        .replace("<strong>", f'<strong style="{chips["strong"]}">')
    )


def render_html(entry: dict, theme_name: str | None = None) -> str:
    theme = get_theme(theme_name)
    inline = theme["inline"]
    html_body = _apply_chip_styles(markdown_to_html(entry["body"]), theme["chip_styles"])
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<meta name="color-scheme" content="{theme['color_scheme']}"/>
<meta name="supported-color-schemes" content="{theme['color_scheme'].split()[0]}"/>
<title>Wiki update — {entry['date']}</title>
<style>{theme['css']}</style>
</head>
<body style="{inline['body']}">
  <div class="wiki-wrap" style="{inline['wrap']}">
    <div class="wiki-card" style="{inline['card']}">
      <div class="wiki-kicker" style="{inline['kicker']}">Investing Wiki · {entry['type']} · {theme['label']}</div>
      <h1 class="wiki-headline" style="{inline['headline']}">{_escape(entry['title'])}</h1>
      <div class="wiki-meta" style="{inline['meta']}">{entry['date']} · auto-rendered from <code style="{inline['meta_code']}">log.md</code></div>
      <div class="wiki-content">{html_body}</div>
    </div>
    <div class="wiki-footer" style="{inline['footer']}">Generated by <code style="{inline['meta_code']}">scripts/daily_email.py</code> · <a href="https://github.com/rgovindji/wiki_research" style="{inline['footer_link']}">repo</a></div>
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
    p.add_argument("--theme", choices=list(THEMES.keys()),
                   help=f"visual theme (overrides EMAIL_THEME env; default light). Options: {', '.join(THEMES)}")
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

    theme_name = args.theme or os.environ.get("EMAIL_THEME") or "light"
    html = render_html(entry, theme_name)
    subject = f"[Wiki] [{theme_name}] {entry['date']} {entry['type']}: {entry['title'][:80]}"

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
