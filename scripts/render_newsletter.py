#!/usr/bin/env python3
"""Render and send an After Hours newsletter issue.

Reads:
  newsletter/issues/YYYY-MM-DD-slug.md  — the issue body (markdown + YAML frontmatter)
  newsletter/portfolio.json             — current holdings + cost basis + history

Renders a styled HTML newsletter (cream / serif / coral editorial aesthetic,
email-client safe with inline styles) and sends via AWS SES.

Usage:
    python scripts/render_newsletter.py <issue.md>            # send
    python scripts/render_newsletter.py <issue.md> --dry-run  # preview, no send
    python scripts/render_newsletter.py <issue.md> --save out.html

Env (same as daily_email.py):
    SES_SENDER       e.g. wiki@decideai.xyz
    EMAIL_TO         recipient
    AWS_REGION       default us-east-1
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_PATH = REPO_ROOT / "newsletter" / "portfolio.json"

# Reuse the markdown engine from daily_email.py so we don't duplicate logic.
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import daily_email as de  # noqa: E402

# Earth-toned palette matching the cream/coral editorial theme.
# Twelve colors for up to 11 holdings + 1 cash slice.
PALETTE = [
    "#cc785c",  # coral (primary)
    "#5577aa",  # dusty blue
    "#8a6433",  # deep amber
    "#5db8a6",  # sage teal
    "#b8956e",  # taupe
    "#c64545",  # brick red
    "#846b58",  # warm brown
    "#6b8f88",  # sage gray
    "#d4a574",  # warm sand
    "#9f6e8a",  # mauve
    "#7d8c5c",  # olive
    "#cfc8b8",  # cream (cash)
]


# ----------------------------- frontmatter -----------------------------

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    body = text[m.end():]
    raw = m.group(1)
    fm: dict = {}
    for line in raw.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


# ----------------------------- portfolio render -----------------------------

def _format_change(avg: float, cur: float) -> tuple[str, str]:
    """Return (display_text, css_color) for the % change column.
    Returns em-dash + muted gray when the change is effectively zero (Day 1)."""
    if avg <= 0:
        return "—", "#9a9690"
    delta = (cur - avg) / avg * 100
    if abs(delta) < 0.05:
        return "—", "#9a9690"
    color = "#0f7c4a" if delta > 0 else "#a8312c"
    sign = "+" if delta > 0 else ""
    return f"{sign}{delta:.2f}%", color


def render_portfolio_section(p: dict) -> str:
    """Wide-format portfolio table. Columns: Ticker | Name | Weight | Avg Cost
    | Current | Change | Position Value. Thesis is rendered separately (after
    the table) so the data row stays compact."""
    capital = float(p["starting_capital_usd"])
    rows: list[str] = []
    for h in p["current_holdings"]:
        ticker = h["ticker"]
        company = h["company"]
        pct = float(h["allocation_pct"])
        avg = float(h.get("avg_price_usd", h.get("cost_basis_usd", 0)))
        cur = float(h.get("current_price_usd", avg))
        position_value = capital * pct / 100.0  # at current price; will diverge from invested when current != avg
        if avg > 0:
            invested = capital * pct / 100.0
            shares = invested / avg
            position_value = shares * cur
        chg_text, chg_color = _format_change(avg, cur)
        rows.append(
            "<tr>"
            f'<td style="font-family:\'JetBrains Mono\',ui-monospace,SFMono-Regular,Menlo,monospace;color:#cc785c;font-weight:700;font-size:14px;white-space:nowrap;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;">{de._escape(ticker)}</td>'
            f'<td style="color:#252523;font-weight:500;font-size:13px;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;">{de._escape(company)}</td>'
            f'<td style="color:#252523;font-weight:600;font-size:13.5px;text-align:right;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;font-variant-numeric:tabular-nums;">{pct:.0f}%</td>'
            f'<td style="color:#6c6a64;font-size:13px;text-align:right;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;font-variant-numeric:tabular-nums;font-family:\'JetBrains Mono\',monospace;">${avg:,.2f}</td>'
            f'<td style="color:#252523;font-weight:600;font-size:13px;text-align:right;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;font-variant-numeric:tabular-nums;font-family:\'JetBrains Mono\',monospace;">${cur:,.2f}</td>'
            f'<td style="color:{chg_color};font-weight:600;font-size:13px;text-align:right;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;font-variant-numeric:tabular-nums;font-family:\'JetBrains Mono\',monospace;">{chg_text}</td>'
            f'<td style="color:#3d3d3a;font-size:13px;text-align:right;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;font-variant-numeric:tabular-nums;font-family:\'JetBrains Mono\',monospace;">${position_value:,.0f}</td>'
            "</tr>"
        )
    # Cash row
    cash_pct = float(p.get("cash_pct", 0))
    cash_value = capital * cash_pct / 100.0
    rows.append(
        "<tr>"
        f'<td style="font-family:\'JetBrains Mono\',ui-monospace,monospace;color:#6c6a64;font-weight:700;font-size:14px;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;">CASH</td>'
        f'<td style="color:#6c6a64;font-style:italic;font-size:13px;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;">Reserve / dry powder</td>'
        f'<td style="color:#252523;font-weight:600;font-size:13.5px;text-align:right;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;font-variant-numeric:tabular-nums;">{cash_pct:.0f}%</td>'
        f'<td style="color:#6c6a64;font-size:13px;text-align:right;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;">—</td>'
        f'<td style="color:#6c6a64;font-size:13px;text-align:right;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;">—</td>'
        f'<td style="color:#9a9690;font-weight:600;font-size:13px;text-align:right;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;">—</td>'
        f'<td style="color:#3d3d3a;font-size:13px;text-align:right;padding:13px 10px;border-bottom:1px solid #ebe6df;vertical-align:middle;font-variant-numeric:tabular-nums;font-family:\'JetBrains Mono\',monospace;">${cash_value:,.0f}</td>'
        "</tr>"
    )

    table_style = "width:100%;border-collapse:collapse;margin:18px 0 14px;font-size:13px;font-family:'Inter',-apple-system,sans-serif;"
    th_style = "text-align:left;padding:9px 10px;font-size:10.5px;text-transform:uppercase;letter-spacing:1px;color:#6c6a64;font-weight:600;border-bottom:1px solid #e6dfd8;"
    th_right = th_style + "text-align:right;"

    table_html = (
        f'<table style="{table_style}">'
        f'<thead><tr>'
        f'<th style="{th_style}">Ticker</th>'
        f'<th style="{th_style}">Name</th>'
        f'<th style="{th_right}">Weight</th>'
        f'<th style="{th_right}">Avg Cost</th>'
        f'<th style="{th_right}">Current</th>'
        f'<th style="{th_right}">Change</th>'
        f'<th style="{th_right}">Value</th>'
        f'</tr></thead><tbody>'
        + "".join(rows)
        + "</tbody></table>"
        + '<div style="font-family:\'Inter\',-apple-system,sans-serif;font-size:11.5px;color:#6c6a64;font-style:italic;margin:0 0 26px;">Day 1 — positions opened at today\'s prices, so Change reads as &mdash;. Tomorrow\'s letter will show real movement.</div>'
    )

    # Append a compact thesis block below the table — one ticker per line.
    thesis_lines: list[str] = []
    for h in p["current_holdings"]:
        thesis = h.get("thesis", "").strip()
        if not thesis:
            continue
        thesis_lines.append(
            f'<div style="margin:0 0 9px;padding-left:14px;border-left:2px solid #e6dfd8;">'
            f'<span style="font-family:\'JetBrains Mono\',monospace;color:#cc785c;font-weight:700;font-size:13px;margin-right:8px;">{de._escape(h["ticker"])}</span>'
            f'<span style="color:#3d3d3a;font-size:13.5px;line-height:1.55;">{de._escape(thesis)}</span>'
            f'</div>'
        )
    thesis_block = (
        '<details style="margin:8px 0 24px;">'
        '<summary style="font-family:\'Inter\',-apple-system,sans-serif;font-size:11.5px;text-transform:uppercase;letter-spacing:1.2px;color:#cc785c;font-weight:600;cursor:pointer;margin-bottom:14px;">'
        'Why we own each position &nbsp;›'
        '</summary>'
        '<div style="margin-top:14px;">' + "".join(thesis_lines) + '</div>'
        '</details>'
    ) if thesis_lines else ""

    return table_html + thesis_block


def render_portfolio_chart(p: dict) -> str:
    """Build a QuickChart.io doughnut PNG embed showing portfolio weights,
    plus a matching HTML legend below it. QuickChart-rendered PNGs render
    reliably in every email client (Gmail, Apple Mail, Outlook)."""
    import urllib.parse

    holdings = list(p["current_holdings"])
    labels = [h["ticker"] for h in holdings] + ["CASH"]
    data = [h["allocation_pct"] for h in holdings] + [p["cash_pct"]]
    colors = (PALETTE * 2)[: len(labels)]

    config = {
        "type": "doughnut",
        "data": {
            "labels": labels,
            "datasets": [{
                "data": data,
                "backgroundColor": colors,
                "borderColor": "#faf9f5",
                "borderWidth": 2,
            }],
        },
        "options": {
            "plugins": {
                "legend": {"display": False},
                "datalabels": {
                    "color": "#fff",
                    "font": {"size": 11, "weight": "bold", "family": "sans-serif"},
                    "formatter": "(value) => value + '%'",
                },
            },
            "cutout": "55%",
        },
    }

    config_json = json.dumps(config, separators=(",", ":"))
    chart_url = (
        "https://quickchart.io/chart?bkg=transparent&w=460&h=460&c="
        + urllib.parse.quote(config_json)
    )

    # Build the legend with matching color swatches in a 3-column grid (for
    # email clients that don't support flex/grid, we fall back to a table).
    legend_cells: list[str] = []
    for i, label in enumerate(labels):
        color = colors[i]
        weight = data[i]
        legend_cells.append(
            f'<td style="padding:5px 14px 5px 0;vertical-align:middle;font-size:12.5px;color:#3d3d3a;font-family:\'Inter\',-apple-system,sans-serif;white-space:nowrap;">'
            f'<span style="display:inline-block;width:11px;height:11px;background-color:{color};border-radius:2px;margin-right:8px;vertical-align:middle;"></span>'
            f'<span style="font-family:\'JetBrains Mono\',monospace;color:#252523;font-weight:600;">{de._escape(label)}</span>'
            f'<span style="color:#6c6a64;margin-left:6px;font-variant-numeric:tabular-nums;">{weight}%</span>'
            f'</td>'
        )

    # Layout: 3 columns. 12 items → 4 rows.
    cols = 3
    rows: list[str] = []
    for i in range(0, len(legend_cells), cols):
        row_cells = legend_cells[i:i + cols]
        while len(row_cells) < cols:
            row_cells.append("<td></td>")
        rows.append("<tr>" + "".join(row_cells) + "</tr>")
    legend_table = (
        '<table style="border-collapse:collapse;margin:14px auto 0;">'
        + "".join(rows)
        + "</table>"
    )

    return (
        '<div style="text-align:center;margin:28px 0 8px;">'
        f'<img src="{chart_url}" width="320" height="320" alt="Portfolio allocation chart" style="display:block;margin:0 auto;max-width:100%;height:auto;border:0;"/>'
        + legend_table
        + '</div>'
    )


def render_portfolio_summary_card(p: dict) -> str:
    """Small at-a-glance card showing capital + inception + cash policy.
    Renders ABOVE the portfolio table in the email."""
    inception = p["inception_date"]
    today = dt.date.today().isoformat()
    days_running = (dt.date.fromisoformat(today) - dt.date.fromisoformat(inception)).days
    capital = p["starting_capital_usd"]
    return (
        '<div style="background-color:#f5f0e8;border-left:3px solid #cc785c;padding:18px 22px;margin:22px 0;border-radius:0 4px 4px 0;">'
        '<div style="font-family:\'Inter\',-apple-system,sans-serif;font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:#cc785c;font-weight:600;margin-bottom:8px;">Portfolio at a glance</div>'
        '<table style="width:100%;font-family:\'Inter\',-apple-system,sans-serif;font-size:13.5px;color:#252523;border-collapse:collapse;">'
        f'<tr><td style="padding:3px 0;width:55%;">Starting capital</td><td style="padding:3px 0;font-family:\'JetBrains Mono\',monospace;font-weight:600;font-variant-numeric:tabular-nums;">${capital:,.0f}</td></tr>'
        f'<tr><td style="padding:3px 0;">Inception</td><td style="padding:3px 0;font-family:\'JetBrains Mono\',monospace;font-variant-numeric:tabular-nums;">{inception} (day {days_running + 1})</td></tr>'
        f'<tr><td style="padding:3px 0;">Holdings</td><td style="padding:3px 0;font-family:\'JetBrains Mono\',monospace;font-variant-numeric:tabular-nums;">{len(p["current_holdings"])} positions + cash</td></tr>'
        f'<tr><td style="padding:3px 0;">Cash reserve</td><td style="padding:3px 0;font-family:\'JetBrains Mono\',monospace;font-weight:600;font-variant-numeric:tabular-nums;">{p["cash_pct"]}%</td></tr>'
        '</table>'
        '</div>'
    )


# ----------------------------- HTML shell -----------------------------

NEWSLETTER_CSS = """
body { margin: 0; padding: 0; background-color: #faf9f5; color: #3d3d3a; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 16px; line-height: 1.7; -webkit-font-smoothing: antialiased; }
.wrap { max-width: 680px; margin: 0 auto; padding: 56px 28px 64px; }
.brandbar { display: block; margin-bottom: 40px; font-family: 'Inter', -apple-system, sans-serif; font-size: 13px; font-weight: 500; color: #141413; letter-spacing: 0.2px; }
.brandbar .right { color: #6c6a64; font-weight: 400; font-size: 12.5px; float: right; }
.eyebrow { color: #cc785c; text-transform: uppercase; letter-spacing: 1.5px; font-size: 11.5px; font-weight: 600; margin: 0 0 14px; }
h1.title { font-family: 'Cormorant Garamond', 'Garamond', 'Times New Roman', Georgia, serif; color: #141413; font-size: 40px; line-height: 1.1; margin: 0 0 14px; font-weight: 500; letter-spacing: -0.7px; }
.subtitle { font-size: 18px; line-height: 1.55; color: #252523; font-weight: 400; margin: 0 0 36px; max-width: 60ch; font-style: italic; }
h2 { font-family: 'Cormorant Garamond', Georgia, serif; color: #141413; font-size: 28px; font-weight: 500; margin: 44px 0 14px; letter-spacing: -0.3px; }
h3 { font-family: 'Cormorant Garamond', Georgia, serif; color: #141413; font-size: 22px; font-weight: 500; margin: 28px 0 10px; letter-spacing: -0.2px; }
p, li { color: #3d3d3a; font-size: 16.5px; line-height: 1.7; }
p { margin: 0 0 18px; max-width: 64ch; }
ul { padding: 0; list-style: none; margin: 14px 0 18px; }
li { position: relative; padding-left: 20px; margin-bottom: 10px; max-width: 64ch; }
li:before { content: ""; position: absolute; left: 0; top: 13px; width: 10px; height: 1px; background-color: #cc785c; }
blockquote { border-left: 3px solid #cc785c; padding: 6px 0 6px 22px; margin: 24px 0; background: transparent; }
blockquote p { font-family: 'Cormorant Garamond', Georgia, serif; margin: 4px 0; color: #141413; font-style: normal; font-size: 19px; line-height: 1.5; font-weight: 500; max-width: 58ch; }
code { background-color: #f5f0e8; padding: 1px 7px; border-radius: 3px; font-size: 14px; color: #252523; font-family: 'JetBrains Mono', ui-monospace, monospace; font-weight: 500; }
table { width: 100%; border-collapse: collapse; margin: 22px 0 26px; font-size: 13.5px; font-family: 'Inter', -apple-system, sans-serif; }
th { text-align: left; padding: 11px 12px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #6c6a64; font-weight: 600; border-bottom: 1px solid #e6dfd8; }
td { padding: 13px 12px; border-bottom: 1px solid #ebe6df; vertical-align: top; color: #3d3d3a; line-height: 1.55; }
td:first-child { color: #252523; font-weight: 500; }
a { color: #cc785c; text-decoration: none; border-bottom: 1px solid #cc785c; font-weight: 500; }
strong { color: #141413; font-weight: 600; }
em { color: #252523; font-style: italic; }
hr { border: 0; height: 0; text-align: center; margin: 40px 0; color: #8e8b82; line-height: 1; }
hr:before { content: "✻ ✻ ✻"; letter-spacing: 14px; font-size: 12px; }
.signoff { font-family: 'Cormorant Garamond', Georgia, serif; font-size: 22px; color: #cc785c; font-style: italic; margin-top: 8px; }
.footer { color: #6c6a64; font-size: 12.5px; line-height: 1.6; margin-top: 56px; padding-top: 28px; border-top: 1px solid #e6dfd8; font-style: italic; max-width: 60ch; }
"""

GOOGLE_FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'
)

# Inline-style fallbacks for clients that strip <style>
INLINE = {
    "body":      "margin:0;padding:0;background-color:#faf9f5;color:#3d3d3a;font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;font-size:16px;line-height:1.7;-webkit-font-smoothing:antialiased;",
    "wrap":      "max-width:680px;margin:0 auto;padding:56px 28px 64px;",
    "brandbar":  "display:block;margin-bottom:40px;font-family:'Inter',-apple-system,sans-serif;font-size:13px;font-weight:500;color:#141413;letter-spacing:0.2px;",
    "eyebrow":   "color:#cc785c;text-transform:uppercase;letter-spacing:1.5px;font-size:11.5px;font-weight:600;margin:0 0 14px;",
    "title":     "font-family:'Cormorant Garamond','Garamond','Times New Roman',Georgia,serif;color:#141413;font-size:40px;line-height:1.1;margin:0 0 14px;font-weight:500;letter-spacing:-0.7px;",
    "subtitle":  "font-size:18px;line-height:1.55;color:#252523;font-weight:400;margin:0 0 36px;max-width:60ch;font-style:italic;",
    "footer":    "color:#6c6a64;font-size:12.5px;line-height:1.6;margin-top:56px;padding-top:28px;border-top:1px solid #e6dfd8;font-style:italic;max-width:60ch;",
}

CHIP_STYLES = {
    "wikilink": "font-family:'JetBrains Mono',monospace;color:#cc785c;background-color:transparent;padding:0;font-size:14px;font-style:normal;font-weight:600;",
    "code":     "background-color:#f5f0e8;padding:1px 7px;border-radius:3px;font-size:14px;color:#252523;font-family:'JetBrains Mono',ui-monospace,monospace;font-weight:500;",
    "strong":   "color:#141413;font-weight:600;",
}


def render_html(fm: dict, body_md: str, portfolio: dict) -> str:
    title = fm.get("title", "Untitled")
    subtitle = fm.get("subtitle", "")
    issue_date = fm.get("date", dt.date.today().isoformat())
    issue_num = fm.get("issue_number", "1")

    # Inject the portfolio AT THE PLACEHOLDER if present in markdown; otherwise
    # the markdown table that exists in the issue body is the source of truth.
    # Today's inception issue includes a markdown table; we also render the JSON
    # version below the body so the live portfolio renders even when the issue
    # is older.
    body_html = de.markdown_to_html(body_md)
    body_html = de._apply_chip_styles(body_html, CHIP_STYLES)

    # Live portfolio block: summary card + pie chart + wide table + theses dropdown
    summary_card = render_portfolio_summary_card(portfolio)
    chart_block = render_portfolio_chart(portfolio)
    portfolio_table = render_portfolio_section(portfolio)
    live_portfolio_section = (
        '<hr/>'
        '<div style="font-family:\'Inter\',-apple-system,sans-serif;font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:#cc785c;font-weight:600;margin:32px 0 12px;">The After Hours portfolio</div>'
        + summary_card
        + chart_block
        + portfolio_table
    )

    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<meta name="color-scheme" content="light only"/>
<meta name="supported-color-schemes" content="light"/>
<title>After Hours — {de._escape(title)}</title>
{GOOGLE_FONTS}
<style>{NEWSLETTER_CSS}</style>
</head>
<body style="{INLINE['body']}">
  <div class="wrap" style="{INLINE['wrap']}">
    <div class="brandbar" style="{INLINE['brandbar']}">
      <span>✻ &nbsp;After Hours &nbsp;·&nbsp; Issue #{issue_num}</span>
      <span style="color:#6c6a64;font-weight:400;font-size:12.5px;float:right;">{issue_date}</span>
    </div>
    <div class="eyebrow" style="{INLINE['eyebrow']}">Today's letter</div>
    <h1 class="title" style="{INLINE['title']}">{de._escape(title)}</h1>
    <p class="subtitle" style="{INLINE['subtitle']}">{de._escape(subtitle)}</p>
    <div>{body_html}</div>
    {live_portfolio_section}
    <div class="footer" style="{INLINE['footer']}">
      After Hours is a daily market letter. The portfolio shown is a model portfolio for educational purposes — track it with us, but it is not personal financial advice. Every position, price, and trade is disclosed in real time so you can audit the work. Reply to this email to subscribe a friend.
    </div>
  </div>
</body></html>"""


# ----------------------------- send -----------------------------

def send_via_ses(html: str, subject: str, recipients: list[str]) -> None:
    import boto3  # type: ignore
    from botocore.exceptions import ClientError  # type: ignore
    sender = os.environ.get("SES_SENDER", "wiki@decideai.xyz")
    region = os.environ.get("AWS_REGION", "us-east-1")
    client = boto3.client("sesv2", region_name=region)
    try:
        resp = client.send_email(
            FromEmailAddress=sender,
            Destination={"ToAddresses": recipients},
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
        print(f"[newsletter] ses sent: from={sender} to={','.join(recipients)} message_id={resp.get('MessageId', '?')}")
    except ClientError as e:
        print(f"[newsletter] SES error: {e}", file=sys.stderr)
        raise SystemExit(1)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Render and send an After Hours newsletter issue")
    p.add_argument("issue", help="path to the issue markdown file")
    p.add_argument("--to", help="recipient email(s); comma-separated for multiple; overrides EMAIL_TO env")
    p.add_argument("--dry-run", action="store_true", help="render but don't send; print html length")
    p.add_argument("--save", help="also save the HTML to this path")
    args = p.parse_args(argv)

    de.load_dotenv(REPO_ROOT / ".env")

    issue_path = Path(args.issue)
    if not issue_path.is_absolute():
        issue_path = REPO_ROOT / issue_path
    if not issue_path.exists():
        print(f"[newsletter] not found: {issue_path}", file=sys.stderr)
        return 1

    if not PORTFOLIO_PATH.exists():
        print(f"[newsletter] portfolio.json missing at {PORTFOLIO_PATH}", file=sys.stderr)
        return 1

    fm, body = parse_frontmatter(issue_path.read_text(encoding="utf-8"))
    portfolio = json.loads(PORTFOLIO_PATH.read_text(encoding="utf-8"))

    html = render_html(fm, body, portfolio)
    subject = f"After Hours · {fm.get('date', dt.date.today().isoformat())} · {fm.get('title', 'Today')}"

    if args.save:
        Path(args.save).write_text(html, encoding="utf-8")
        print(f"[newsletter] HTML saved to {args.save}")

    if args.dry_run:
        print(f"[newsletter] dry-run: subject={subject!r} html_length={len(html)}")
        return 0

    recipient_raw = args.to or os.environ.get("EMAIL_TO")
    if not recipient_raw:
        print("[newsletter] no recipient (set EMAIL_TO or pass --to)", file=sys.stderr)
        return 1
    recipients = [r.strip() for r in recipient_raw.split(",") if r.strip()]

    print(f"[newsletter] sending {subject!r} to {len(recipients)} recipient(s): {', '.join(recipients)}")
    send_via_ses(html, subject, recipients)
    return 0


if __name__ == "__main__":
    sys.exit(main())
