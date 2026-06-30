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
import datetime
import hashlib
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
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
BULLET_RE = re.compile(r"^\s*[-*]\s+")

# Administrative / meta sections with near-zero retrieval value — excluded from chunking
# so they don't pollute results (e.g. a "Citations" section matching an off-topic query).
BOILERPLATE_HEADINGS = {
    "citations", "sources", "related", "see also", "references",
    "wiki updates", "wiki updates made", "wiki updates suggested",
}


def _is_boilerplate(crumb: str) -> bool:
    return crumb.split(">")[-1].strip().lower() in BOILERPLATE_HEADINGS

# Embedding backend. Auto-detects provider from .env: Voyage (VOYAGE_API_KEY,
# default model voyage-3.5) is preferred over OpenAI (OPENAI_API_KEY/OPEN_AI_KEY,
# text-embedding-3-small). Override with WIKI_EMBED_PROVIDER / WIKI_EMBED_MODEL.
EMBED_BATCH = 96
RRF_K = 60  # reciprocal-rank-fusion constant
LOWCONF_SIM = 0.45  # below this best cosine sim (and no strong lexical hit) -> low-confidence warning
LEX_STRONG = 2      # a shown result with lexical rank <= this counts as a strong lexical anchor


def load_env() -> None:
    """Tiny .env loader (mirrors daily_email.py) so OPEN_AI_KEY is available headless."""
    env_path = REPO_ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def openai_key() -> str | None:
    return os.environ.get("OPENAI_API_KEY") or os.environ.get("OPEN_AI_KEY")


def embed_provider() -> str:
    """Which embedding backend to use, auto-detected from the environment."""
    override = os.environ.get("WIKI_EMBED_PROVIDER")
    if override:
        return override.lower()
    if os.environ.get("VOYAGE_API_KEY"):
        return "voyage"
    if openai_key():
        return "openai"
    return "none"


def embed_model() -> str:
    if os.environ.get("WIKI_EMBED_MODEL"):
        return os.environ["WIKI_EMBED_MODEL"]
    return {"voyage": "voyage-3.5", "openai": "text-embedding-3-small"}.get(embed_provider(), "")


def has_embed_key() -> bool:
    return embed_provider() != "none"


@dataclass
class Chunk:
    path: str
    heading: str
    ord: int
    text: str
    date_hint: str | None
    tags: list[str]
    embed_input: str
    content_hash: str
    mtime: float


def _doc_defaults(doc: "Doc") -> tuple[str | None, list[str]]:
    fm = doc.frontmatter
    default_date = None
    for k in ("last_updated", "date", "last_full_review"):
        v = fm.get(k)
        if isinstance(v, str):
            m = DATE_RE.search(v)
            if m:
                default_date = m.group(1)
                break
    tags: list[str] = []
    t = fm.get("ticker")
    if isinstance(t, str) and t.strip():
        tags.append(t.strip())
    tg = fm.get("tags")
    if isinstance(tg, list):
        tags.extend(str(x) for x in tg)
    elif isinstance(tg, str):
        tags.extend(x.strip() for x in tg.replace(",", " ").split() if x.strip())
    return default_date, tags


def _split_size(text: str, max_chars: int) -> list[str]:
    """Split overlong text on blank-line paragraph boundaries."""
    if len(text) <= max_chars:
        return [text]
    parts: list[str] = []
    cur: list[str] = []
    size = 0
    for para in re.split(r"\n\s*\n", text):
        if size + len(para) > max_chars and cur:
            parts.append("\n\n".join(cur))
            cur, size = [], 0
        cur.append(para)
        size += len(para) + 2
    if cur:
        parts.append("\n\n".join(cur))
    return parts


def chunk_doc(doc: "Doc", max_chars: int = 1200) -> list[Chunk]:
    """Split a doc into retrieval units: one per markdown section, with dated
    bullets (Recent developments / Contradicting evidence) exploded individually."""
    default_date, base_tags = _doc_defaults(doc)
    stack: list[tuple[int, str]] = []
    sections: list[tuple[str, list[str]]] = []
    cur: list[str] = []

    def crumb() -> str:
        names = [h for lvl, h in stack if lvl >= 2]
        return " > ".join(names) if names else (doc.title or doc.path)

    def flush():
        nonlocal cur
        if any(l.strip() for l in cur):
            sections.append((crumb(), cur))
        cur = []

    for line in doc.body.splitlines():
        m = HEADING_RE.match(line)
        if m:
            flush()
            level = len(m.group(1))
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, m.group(2).strip()))
        else:
            cur.append(line)
    flush()

    raw: list[tuple[str, str]] = []  # (heading, text)
    for heading, body_lines in sections:
        if _is_boilerplate(heading):
            continue
        bullets = [l for l in body_lines if BULLET_RE.match(l)]
        dated = [l for l in bullets if DATE_RE.search(l)]
        if len(dated) >= 2 and len(dated) >= len(bullets) / 2:
            # dated bullet list -> one chunk per top-level bullet (+ its continuation lines)
            buf: list[str] = []
            for l in body_lines:
                if BULLET_RE.match(l):
                    if buf:
                        raw.append((heading, "\n".join(buf).strip()))
                    buf = [l]
                elif buf:
                    buf.append(l)
            if buf:
                raw.append((heading, "\n".join(buf).strip()))
        else:
            text = "\n".join(body_lines).strip()
            for piece in _split_size(text, max_chars):
                if piece.strip():
                    raw.append((heading, piece.strip()))

    chunks: list[Chunk] = []
    for i, (heading, text) in enumerate(raw):
        if not text.strip():
            continue
        m = DATE_RE.search(text)
        date_hint = m.group(1) if m else default_date
        wl = sorted({mm.group(1).strip() for mm in WIKILINK_RE.finditer(text)})
        tags = sorted(set(base_tags) | set(wl))
        embed_input = f"{doc.title} — {heading}\n{text}"
        chash = hashlib.sha1(embed_input.encode("utf-8")).hexdigest()
        chunks.append(Chunk(doc.path, heading, i, text, date_hint, tags, embed_input, chash, doc.mtime))
    return chunks


def embed_texts(texts: list[str], input_type: str = "document") -> list[list[float]] | None:
    """Embed via the detected provider. input_type is 'document' (indexing) or
    'query' (search) — Voyage uses it for asymmetric retrieval. Returns None
    (caller falls back to lexical) on any failure."""
    if not texts:
        return None
    provider = embed_provider()
    if provider == "voyage":
        return _embed_voyage(texts, input_type)
    if provider == "openai":
        return _embed_openai(texts)
    return None


def _embed_voyage(texts: list[str], input_type: str) -> list[list[float]] | None:
    key = os.environ.get("VOYAGE_API_KEY")
    if not key:
        return None
    import requests
    model = embed_model()
    out: list[list[float]] = []
    try:
        for i in range(0, len(texts), 128):
            resp = requests.post(
                "https://api.voyageai.com/v1/embeddings",
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                json={"input": texts[i:i + 128], "model": model, "input_type": input_type},
                timeout=60,
            )
            resp.raise_for_status()
            data = sorted(resp.json()["data"], key=lambda x: x["index"])
            out.extend(d["embedding"] for d in data)
    except Exception as e:
        detail = ""
        if isinstance(e, requests.HTTPError) and e.response is not None:
            detail = f" — {e.response.text[:200]}"
        print(f"[embed] voyage failed ({e}){detail}; falling back to lexical-only", file=sys.stderr)
        return None
    return out


def _embed_openai(texts: list[str]) -> list[list[float]] | None:
    key = openai_key()
    if not key:
        return None
    try:
        from openai import OpenAI
    except Exception as e:
        print(f"[embed] openai package unavailable: {e}", file=sys.stderr)
        return None
    client = OpenAI(api_key=key)
    out: list[list[float]] = []
    try:
        for i in range(0, len(texts), EMBED_BATCH):
            resp = client.embeddings.create(model=embed_model(), input=texts[i:i + EMBED_BATCH])
            out.extend(d.embedding for d in resp.data)
    except Exception as e:
        print(f"[embed] openai call failed ({e}); falling back to lexical-only", file=sys.stderr)
        return None
    return out


STOPWORDS = {
    "is", "are", "was", "were", "be", "been", "being", "the", "a", "an", "of", "to",
    "in", "on", "for", "and", "or", "with", "by", "at", "as", "from", "into", "vs",
    "what", "how", "who", "why", "when", "which", "where", "does", "do", "did", "will",
    "would", "should", "could", "can", "about", "this", "that", "these", "those", "it",
    "its", "i", "my", "me", "we", "our", "you", "your", "more", "most", "than", "then",
    "there", "their", "they", "any", "some", "if", "so", "vs.",
}


def _fts_query(q: str) -> str:
    """Turn a natural-language question into a safe FTS5 OR-query of quoted, content-bearing
    terms (function words dropped so filler doesn't generate spurious lexical matches)."""
    words = [w for w in re.findall(r"[A-Za-z0-9$%.+-]+", q.lower())
             if len(w) > 1 and w not in STOPWORDS]
    return " OR ".join(f'"{w}"' for w in words)


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

            CREATE TABLE IF NOT EXISTS chunks (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                path         TEXT NOT NULL,
                heading      TEXT,
                ord          INTEGER,
                text         TEXT NOT NULL,
                date_hint    TEXT,
                tags         TEXT,
                content_hash TEXT NOT NULL,
                mtime        REAL NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_chunks_path ON chunks(path);
            CREATE INDEX IF NOT EXISTS idx_chunks_hash ON chunks(content_hash);
            CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts
                USING fts5(chunk_id UNINDEXED, heading, text);
            CREATE TABLE IF NOT EXISTS embeddings (
                content_hash TEXT PRIMARY KEY,
                model        TEXT NOT NULL,
                dim          INTEGER NOT NULL,
                vec          BLOB NOT NULL
            );
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


def reindex_chunks(conn: sqlite3.Connection, doc: Doc) -> None:
    """Drop and rebuild a document's chunks (+ their FTS rows)."""
    for r in conn.execute("SELECT id FROM chunks WHERE path = ?", (doc.path,)).fetchall():
        conn.execute("DELETE FROM chunks_fts WHERE chunk_id = ?", (r["id"],))
    conn.execute("DELETE FROM chunks WHERE path = ?", (doc.path,))
    for ch in chunk_doc(doc):
        cur = conn.execute(
            "INSERT INTO chunks (path, heading, ord, text, date_hint, tags, content_hash, mtime) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (ch.path, ch.heading, ch.ord, ch.text, ch.date_hint, json.dumps(ch.tags), ch.content_hash, ch.mtime),
        )
        conn.execute(
            "INSERT INTO chunks_fts (chunk_id, heading, text) VALUES (?, ?, ?)",
            (cur.lastrowid, ch.heading, ch.text),
        )


def embed_pending(conn: sqlite3.Connection) -> int:
    """Embed any chunk lacking a cached vector for the current model. Returns count embedded."""
    if not has_embed_key():
        return 0
    model = embed_model()
    rows = conn.execute(
        "SELECT DISTINCT c.content_hash AS h, d.title AS title, c.heading AS heading, c.text AS text "
        "FROM chunks c "
        "LEFT JOIN embeddings e ON c.content_hash = e.content_hash AND e.model = ? "
        "LEFT JOIN documents d ON c.path = d.path "
        "WHERE e.content_hash IS NULL",
        (model,),
    ).fetchall()
    if not rows:
        return 0
    inputs = [f"{r['title']} — {r['heading']}\n{r['text']}" for r in rows]
    vecs = embed_texts(inputs, input_type="document")
    if not vecs:
        return 0
    import numpy as np
    n = 0
    for r, v in zip(rows, vecs):
        arr = np.asarray(v, dtype=np.float32)
        conn.execute(
            "INSERT OR REPLACE INTO embeddings (content_hash, model, dim, vec) VALUES (?, ?, ?, ?)",
            (r["h"], model, int(arr.shape[0]), arr.tobytes()),
        )
        n += 1
    conn.commit()
    return n


def do_build(include_raw: bool = False, force: bool = False, embed: bool = True) -> dict:
    load_env()
    include_raw = include_raw or os.environ.get("RAW_INDEX") == "1"
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
        if rel in existing and existing[rel] == current_mtime and not force:
            continue
        doc = load_doc(path)
        if doc is None:
            errors += 1
            continue
        upsert(conn, doc)
        reindex_chunks(conn, doc)
        if rel in existing:
            updated += 1
        else:
            added += 1
    for rel in list(existing):
        if rel not in seen:
            for r in conn.execute("SELECT id FROM chunks WHERE path = ?", (rel,)).fetchall():
                conn.execute("DELETE FROM chunks_fts WHERE chunk_id = ?", (r["id"],))
            conn.execute("DELETE FROM chunks WHERE path = ?", (rel,))
            conn.execute("DELETE FROM documents WHERE path = ?", (rel,))
            conn.execute("DELETE FROM documents_fts WHERE path = ?", (rel,))
            removed += 1
    conn.commit()
    embedded = embed_pending(conn) if embed else 0
    total = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    nchunks = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    nvecs = conn.execute("SELECT COUNT(*) FROM embeddings").fetchone()[0]
    conn.close()
    return {
        "dirs": dirs, "added": added, "updated": updated, "removed": removed,
        "errors": errors, "total": total, "chunks": nchunks,
        "embedded": embedded, "vectors": nvecs,
    }


def cmd_build(args) -> int:
    s = do_build(include_raw=args.include_raw, force=args.force, embed=not args.no_embed)
    print(f"[build] dirs={s['dirs']} added={s['added']} updated={s['updated']} "
          f"removed={s['removed']} errors={s['errors']} docs={s['total']} "
          f"chunks={s['chunks']} embedded_now={s['embedded']} vectors={s['vectors']}")
    if not has_embed_key() and not args.no_embed:
        print("[build] note: no VOYAGE_API_KEY / OpenAI key found — semantic vectors skipped (lexical-only).")
    elif s["embedded"] or s["vectors"]:
        print(f"[build] embeddings: provider={embed_provider()} model={embed_model()}")
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


def cmd_ask(args) -> int:
    """Hybrid retrieval: lexical (FTS5) + semantic (OpenAI), RRF-fused,
    re-ranked by recency and frontmatter conviction. Returns cited chunks."""
    load_env()
    if not args.no_build:
        do_build(embed=not args.no_embed)
    if not DB_PATH.exists():
        print("[ask] no index — run: python scripts/wikidb.py build", file=sys.stderr)
        return 1
    conn = open_db(create=False)
    q = " ".join(args.query)

    fm_map: dict[str, dict] = {}
    for r in conn.execute("SELECT path, frontmatter FROM documents"):
        try:
            fm_map[r["path"]] = json.loads(r["frontmatter"])
        except Exception:
            fm_map[r["path"]] = {}

    # --- lexical half ---
    lex_rank: dict[int, int] = {}
    fts_q = _fts_query(q)
    if fts_q:
        try:
            for i, r in enumerate(conn.execute(
                "SELECT chunk_id FROM chunks_fts WHERE chunks_fts MATCH ? ORDER BY rank LIMIT 50",
                (fts_q,),
            )):
                lex_rank[r["chunk_id"]] = i
        except sqlite3.OperationalError as e:
            print(f"[ask] fts error: {e}", file=sys.stderr)

    # --- semantic half ---
    sem_rank: dict[int, int] = {}
    sem_sim: dict[int, float] = {}
    qv = embed_texts([q], input_type="query") if (not args.no_embed and has_embed_key()) else None
    if qv:
        import numpy as np
        rows = conn.execute(
            "SELECT c.id AS id, e.vec AS vec, e.dim AS dim "
            "FROM chunks c JOIN embeddings e ON c.content_hash = e.content_hash "
            "WHERE e.model = ?",
            (embed_model(),),
        ).fetchall()
        if rows:
            dim = rows[0]["dim"]
            mat = np.frombuffer(b"".join(r["vec"] for r in rows), dtype=np.float32).reshape(len(rows), dim)
            ids = [r["id"] for r in rows]
            qvec = np.asarray(qv[0], dtype=np.float32)
            matn = mat / (np.linalg.norm(mat, axis=1, keepdims=True) + 1e-8)
            qn = qvec / (np.linalg.norm(qvec) + 1e-8)
            sims = matn @ qn
            for rank, idx in enumerate(np.argsort(-sims)[:50]):
                cid = ids[int(idx)]
                sem_rank[cid] = rank
                sem_sim[cid] = float(sims[int(idx)])

    # --- reciprocal-rank fusion ---
    scores: dict[int, float] = {}
    for cid, rnk in lex_rank.items():
        scores[cid] = scores.get(cid, 0.0) + 1.0 / (RRF_K + rnk)
    for cid, rnk in sem_rank.items():
        scores[cid] = scores.get(cid, 0.0) + 1.0 / (RRF_K + rnk)
    if not scores:
        print(f"[ask] no matches for: {q}")
        return 0

    # --- recency + conviction re-rank ---
    today = datetime.date.today()

    def recency(d: str | None) -> float:
        # Gentle decay: 1.0 (today) -> 0.6 (old). A tie-breaker, not a dominator —
        # foundational/undated content must not be buried under fresh daily bullets.
        if not d:
            return 0.85
        try:
            dt = datetime.date.fromisoformat(d)
        except Exception:
            return 0.85
        days = max(0, (today - dt).days)
        return 0.6 + 0.4 * (0.5 ** (days / 365.0))

    conv_factor = {"high": 1.15, "medium": 1.0, "low": 0.85}
    ids = list(scores)
    qmarks = ",".join("?" * len(ids))
    rowmap = {
        r["id"]: r for r in conn.execute(
            f"SELECT id, path, heading, text, date_hint FROM chunks WHERE id IN ({qmarks})", ids
        )
    }
    ranked = []
    for cid, base in scores.items():
        r = rowmap.get(cid)
        if not r:
            continue
        fm = fm_map.get(r["path"], {})
        conv = conv_factor.get(str(fm.get("conviction", "")).lower(), 1.0)
        rec = recency(r["date_hint"])
        comp = {"rrf": base, "rec": rec, "conv": conv,
                "lex": lex_rank.get(cid), "sem": sem_rank.get(cid),
                "sim": sem_sim.get(cid)}
        ranked.append((base * rec * conv, r, fm, comp))
    ranked.sort(key=lambda x: -x[0])
    conn.close()

    # Per-page diversity cap: at most `per_page` chunks from any one page in the
    # displayed set, then backfill if the cap left us short.
    show, page_counts = [], {}
    for item in ranked:
        path = item[1]["path"]
        if page_counts.get(path, 0) >= args.per_page:
            continue
        show.append(item)
        page_counts[path] = page_counts.get(path, 0) + 1
        if len(show) >= args.limit:
            break
    if len(show) < args.limit:
        picked = {id(x) for x in show}
        for item in ranked:
            if id(item) in picked:
                continue
            show.append(item)
            if len(show) >= args.limit:
                break

    # Confidence signal: low only when semantics are weak AND there's no strong lexical
    # anchor — this spares short exact-token queries (e.g. "Vera Rubin") whose sim is low
    # but whose lexical match is exact, while still flagging genuinely-absent topics.
    best_sim = max((c["sim"] for *_, c in show if c.get("sim") is not None), default=None)
    # A real anchor needs a strong lexical hit that is ALSO semantically corroborated
    # (present in the semantic top-K) — a keyword match on a generic word alone won't do.
    has_lex_anchor = any(
        c.get("lex") is not None and c["lex"] <= LEX_STRONG and c.get("sim") is not None
        for *_, c in show
    )
    low_conf = best_sim is not None and best_sim < LOWCONF_SIM and not has_lex_anchor
    print(f'## Retrieved context for: "{q}"\n')
    if low_conf:
        print(f"> ⚠ **Low confidence** (best semantic match {best_sim:.2f} < {LOWCONF_SIM}, "
              f"no strong lexical hit). The wiki likely doesn't cover this — treat results "
              f"as weak, and prefer a fresh WebSearch.\n")
    for n, (score, r, fm, comp) in enumerate(show, 1):
        meta = []
        if r["date_hint"]:
            meta.append(r["date_hint"])
        if fm.get("conviction"):
            meta.append(f"conviction: {fm['conviction']}")
        if fm.get("stance"):
            meta.append(f"stance: {fm['stance']}")
        tail = ("  ·  " + "  ·  ".join(meta)) if meta else ""
        print(f"### {n}. {r['heading']}  ·  `{r['path']}`{tail}")
        if args.scores:
            lex = f"L{comp['lex']}" if comp["lex"] is not None else "L-"
            sem = f"S{comp['sem']}" if comp["sem"] is not None else "S-"
            sim = f"sim={comp['sim']:.2f}" if comp.get("sim") is not None else "sim=-"
            print(f"_[score={score:.4f} rrf={comp['rrf']:.4f} rec={comp['rec']:.2f} "
                  f"conv={comp['conv']:.2f} {sim} {lex} {sem}]_")
        print(r["text"].strip())
        print()
    mode = "hybrid (lexical+semantic)" if sem_rank else (
        "lexical-only (no embeddings cached)" if has_embed_key() else "lexical-only (no API key)")
    distinct = len({r["path"] for _, r, _, _ in show})
    simtxt = f" · best_sim={best_sim:.2f}" if best_sim is not None else ""
    print(f"_retrieval: {mode} · {len(ranked)} candidates · top {len(show)} shown "
          f"across {distinct} page(s){simtxt}_")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="SQLite FTS5 over the Investing wiki")
    sub = p.add_subparsers(dest="cmd", required=True)

    pb = sub.add_parser("build", help="build or refresh the index (docs + chunks + embeddings)")
    pb.add_argument("--force", action="store_true", help="re-index even if mtime unchanged")
    pb.add_argument("--include-raw", action="store_true", help="also index raw/ (copyrighted; local only)")
    pb.add_argument("--no-embed", action="store_true", help="skip OpenAI embeddings (lexical-only)")
    pb.set_defaults(func=cmd_build)

    ps = sub.add_parser("search", help="FTS5 full-document search (legacy)")
    ps.add_argument("query", nargs="+", help="FTS5 query terms (use quotes for phrases)")
    ps.add_argument("--limit", type=int, default=15)
    ps.set_defaults(func=cmd_search)

    pa = sub.add_parser("ask", help="hybrid retrieval (lexical+semantic) returning cited chunks")
    pa.add_argument("query", nargs="+", help="natural-language question")
    pa.add_argument("--limit", type=int, default=8, help="how many chunks to return")
    pa.add_argument("--per-page", type=int, default=3, help="max chunks from any one page")
    pa.add_argument("--no-build", action="store_true", help="skip the incremental rebuild first")
    pa.add_argument("--no-embed", action="store_true", help="lexical-only; skip OpenAI embeddings")
    pa.add_argument("--scores", action="store_true", help="show score breakdown per result (debug)")
    pa.set_defaults(func=cmd_ask)

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
