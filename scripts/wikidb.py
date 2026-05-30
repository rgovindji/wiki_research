#!/usr/bin/env python3
"""SQLite FTS5 index over the Investing wiki.

Indexes every .md file under wiki/, sources/, and (optionally) raw/.
Stores frontmatter as JSON, body as FTS5-searchable content. Tracks mtime
for incremental rebuilds.

Usage:
    python scripts/wikidb.py build              # build/refresh the index
    python scripts/wikidb.py search "query"     # FTS5 search
    python scripts/wikidb.py stale              # list pages that need re-indexing
    python scripts/wikidb.py stats              # summary counts
    python scripts/wikidb.py page TICKER        # print one page from the index

The DB is written to wiki.db at the repo root (gitignored).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import time
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = REPO_ROOT / "wiki.db"

# Directories to index. raw/ is gitignored copyrighted material — index it
# locally only if RAW_INDEX=1 is set in the environment.
DEFAULT_DIRS = ["wiki", "sources"]
RAW_DIRS = ["raw"]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


@dataclass
class Doc:
    path: str          # relative path from repo root
    title: str         # H1 or filename stem
    frontmatter: dict  # parsed (best-effort) YAML-ish frontmatter
    body: str          # full body text (no frontmatter)
    wikilinks: list[str]
    mtime: float


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Best-effort YAML-ish frontmatter parser. We avoid PyYAML to stay stdlib."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    raw = m.group(1)
    body = text[m.end():]
    fm: dict = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") and current_key:
            fm[current_key] = (fm[current_key] or "") + " " + line.strip()
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if value.startswith("[") and value.endswith("]"):
                items = [x.strip().strip("'\"") for x in value[1:-1].split(",") if x.strip()]
                fm[key] = items
            else:
                fm[key] = value
            current_key = key
    return fm, body


def extract_title(body: str, fallback: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
        if stripped:
            break
    return fallback


def load_doc(path: Path) -> Doc | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    fm, body = parse_frontmatter(text)
    rel = str(path.relative_to(REPO_ROOT))
    title = extract_title(body, path.stem)
    wikilinks = sorted({m.group(1).strip() for m in WIKILINK_RE.finditer(body)})
    return Doc(
        path=rel,
        title=title,
        frontmatter=fm,
        body=body,
        wikilinks=wikilinks,
        mtime=path.stat().st_mtime,
    )


def iter_markdown(dirs: list[str]):
    for d in dirs:
        base = REPO_ROOT / d
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            yield path


def open_db(create: bool = True) -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    if create:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS documents (
                path        TEXT PRIMARY KEY,
                title       TEXT NOT NULL,
                frontmatter TEXT NOT NULL,
                wikilinks   TEXT NOT NULL,
                mtime       REAL NOT NULL,
                indexed_at  REAL NOT NULL
            );
            CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts
                USING fts5(path UNINDEXED, title, body);
        """)
    return conn


def upsert(conn: sqlite3.Connection, doc: Doc) -> None:
    now = time.time()
    conn.execute(
        "INSERT OR REPLACE INTO documents (path, title, frontmatter, wikilinks, mtime, indexed_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (doc.path, doc.title, json.dumps(doc.frontmatter), json.dumps(doc.wikilinks), doc.mtime, now),
    )
    conn.execute("DELETE FROM documents_fts WHERE path = ?", (doc.path,))
    conn.execute(
        "INSERT INTO documents_fts (path, title, body) VALUES (?, ?, ?)",
        (doc.path, doc.title, doc.body),
    )


def cmd_build(args) -> int:
    include_raw = args.include_raw or os.environ.get("RAW_INDEX") == "1"
    dirs = DEFAULT_DIRS + (RAW_DIRS if include_raw else [])
    conn = open_db()
    existing = {r["path"]: r["mtime"] for r in conn.execute("SELECT path, mtime FROM documents")}
    seen, added, updated, removed, errors = set(), 0, 0, 0, 0
    for path in iter_markdown(dirs):
        rel = str(path.relative_to(REPO_ROOT))
        seen.add(rel)
        try:
            current_mtime = path.stat().st_mtime
        except OSError:
            errors += 1
            continue
        if rel in existing and existing[rel] == current_mtime and not args.force:
            continue
        doc = load_doc(path)
        if doc is None:
            errors += 1
            continue
        upsert(conn, doc)
        if rel in existing:
            updated += 1
        else:
            added += 1
    for rel in list(existing):
        if rel not in seen:
            conn.execute("DELETE FROM documents WHERE path = ?", (rel,))
            conn.execute("DELETE FROM documents_fts WHERE path = ?", (rel,))
            removed += 1
    conn.commit()
    total = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    conn.close()
    print(f"[build] dirs={dirs} added={added} updated={updated} removed={removed} errors={errors} total={total}")
    print(f"[build] db={DB_PATH}")
    return 0


def cmd_search(args) -> int:
    if not DB_PATH.exists():
        print("[search] index does not exist — run: python scripts/wikidb.py build", file=sys.stderr)
        return 1
    conn = open_db(create=False)
    query = " ".join(args.query)
    # FTS5 supports column filters and prefix operators.
    sql = """
        SELECT
            fts.path,
            fts.title,
            snippet(documents_fts, 2, '«', '»', '…', 12) AS snippet,
            bm25(documents_fts, 5.0, 1.0) AS rank
        FROM documents_fts AS fts
        WHERE documents_fts MATCH ?
        ORDER BY rank
        LIMIT ?
    """
    try:
        rows = conn.execute(sql, (query, args.limit)).fetchall()
    except sqlite3.OperationalError as e:
        print(f"[search] FTS5 error: {e}", file=sys.stderr)
        print('[search] tip: quote multi-word phrases like \'"vera rubin"\'', file=sys.stderr)
        return 2
    if not rows:
        print(f"[search] no matches for: {query}")
        return 0
    for r in rows:
        print(f"\n— {r['title']}  ({r['path']})  rank={r['rank']:.3f}")
        print(f"  {r['snippet']}")
    conn.close()
    return 0


def cmd_stale(args) -> int:
    if not DB_PATH.exists():
        print("[stale] no index yet", file=sys.stderr)
        return 1
    conn = open_db(create=False)
    indexed = {r["path"]: r["mtime"] for r in conn.execute("SELECT path, mtime FROM documents")}
    stale = []
    missing_from_disk = []
    new_on_disk = []
    seen = set()
    for path in iter_markdown(DEFAULT_DIRS):
        rel = str(path.relative_to(REPO_ROOT))
        seen.add(rel)
        mtime = path.stat().st_mtime
        if rel not in indexed:
            new_on_disk.append(rel)
        elif indexed[rel] < mtime:
            stale.append(rel)
    for rel in indexed:
        if rel not in seen:
            missing_from_disk.append(rel)
    print(f"[stale] {len(stale)} updated on disk since index was built:")
    for p in stale:
        print(f"  ~ {p}")
    print(f"[stale] {len(new_on_disk)} new on disk (never indexed):")
    for p in new_on_disk:
        print(f"  + {p}")
    print(f"[stale] {len(missing_from_disk)} indexed but deleted from disk:")
    for p in missing_from_disk:
        print(f"  - {p}")
    conn.close()
    return 0


def cmd_stats(args) -> int:
    if not DB_PATH.exists():
        print("[stats] no index yet", file=sys.stderr)
        return 1
    conn = open_db(create=False)
    total = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    by_dir: dict[str, int] = {}
    for r in conn.execute("SELECT path FROM documents"):
        top = r["path"].split("/", 1)[0]
        by_dir[top] = by_dir.get(top, 0) + 1
    print(f"[stats] total indexed: {total}")
    for d, n in sorted(by_dir.items()):
        print(f"  {d}: {n}")
    # Sample a few of the most-linked pages
    print("\n[stats] top wiki-linked targets:")
    counts: dict[str, int] = {}
    for r in conn.execute("SELECT wikilinks FROM documents"):
        for target in json.loads(r["wikilinks"]):
            counts[target] = counts.get(target, 0) + 1
    for target, n in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"  [[{target}]] — {n} references")
    conn.close()
    return 0


def cmd_page(args) -> int:
    if not DB_PATH.exists():
        print("[page] no index yet", file=sys.stderr)
        return 1
    conn = open_db(create=False)
    name = args.name
    # Try multiple resolutions: exact path, basename match, title match.
    rows = conn.execute(
        "SELECT path, title, frontmatter, wikilinks FROM documents WHERE path = ? OR path LIKE ? OR title = ?",
        (name, f"%/{name}.md", name),
    ).fetchall()
    if not rows:
        print(f"[page] not found: {name}", file=sys.stderr)
        return 1
    for r in rows[: args.limit]:
        print(f"\n=== {r['title']} ({r['path']}) ===")
        fm = json.loads(r["frontmatter"])
        if fm:
            print(json.dumps(fm, indent=2, sort_keys=True))
        links = json.loads(r["wikilinks"])
        if links:
            print(f"\nWiki-links ({len(links)}):")
            print(", ".join(f"[[{x}]]" for x in links[:30]))
            if len(links) > 30:
                print(f"… +{len(links) - 30} more")
    conn.close()
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="SQLite FTS5 over the Investing wiki")
    sub = p.add_subparsers(dest="cmd", required=True)

    pb = sub.add_parser("build", help="build or refresh the index")
    pb.add_argument("--force", action="store_true", help="re-index even if mtime unchanged")
    pb.add_argument("--include-raw", action="store_true", help="also index raw/ (copyrighted; local only)")
    pb.set_defaults(func=cmd_build)

    ps = sub.add_parser("search", help="FTS5 search")
    ps.add_argument("query", nargs="+", help="FTS5 query terms (use quotes for phrases)")
    ps.add_argument("--limit", type=int, default=15)
    ps.set_defaults(func=cmd_search)

    sub.add_parser("stale", help="list pages that need re-indexing").set_defaults(func=cmd_stale)
    sub.add_parser("stats", help="show index stats + top wiki-link targets").set_defaults(func=cmd_stats)

    pp = sub.add_parser("page", help="show one page from the index")
    pp.add_argument("name", help="path, basename without extension, or title")
    pp.add_argument("--limit", type=int, default=3)
    pp.set_defaults(func=cmd_page)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
