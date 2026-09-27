"""Structure-aware chunking with lifecycle metadata.

Module 2, failure classes F1 (parsing loss) and F2 (chunk-boundary damage).

The naive baseline splits on a fixed character count. On this corpus that
produces ~41% of chunks starting mid-sentence, and — worse — it slices tables
in half, so "Grade 11" ends up in one chunk and "9,900" in another. Neither
chunk answers the question, and no reranker or bigger model recovers a fact
that was destroyed at ingest.

The strategy here:

  * tables are ATOMIC. One table = one chunk, header row included, never split,
    never merged with prose. If a table exceeds the budget it is split by ROWS
    with the header repeated — never mid-row.
  * prose accumulates under its nearest preceding heading, and the heading text
    is PREPENDED to every chunk it owns. This is the cheapest possible fix for
    the orphaned-clause problem: "…shall not exceed 25%" becomes
    "Housing Allowance Policy › 3. Provisions ¶ …shall not exceed 25%".
  * overlap applies to PROSE ONLY. Overlapping tables duplicates numeric facts
    and inflates the index for nothing (the Lab 2 troubleshooting row where
    chunk count explodes to 30k).
  * every chunk carries lifecycle metadata (effective_date, lifecycle,
    supersedes/superseded_by) because Module 6's staleness gate filters on it.
    Metadata attached later never covers the whole corpus.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field, asdict

from .loaders import ParsedDocument, Block
from ..config import settings

_SENT_END = re.compile(r"(?<=[.!?؟،؛])\s+|(?<=\.)\n")


@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    text: str
    kind: str                       # prose|table
    section_title: str = ""
    ordinal: int = 0
    n_chars: int = 0
    starts_mid_sentence: bool = False
    meta: dict = field(default_factory=dict)

    def to_payload(self) -> dict:
        d = asdict(self)
        meta = d.pop("meta")
        d.update(meta)
        return d


def _stable_id(doc_id: str, ordinal: int) -> str:
    """Deterministic point ids so re-running ingest is idempotent.

    Lab 3 step 2 checks exactly this: upserting twice must not double the point
    count. Using `enumerate()` as the id is the bug that makes it double."""
    return hashlib.sha1(f"{doc_id}:{ordinal}".encode()).hexdigest()


def _split_prose(text: str, target: int, overlap: int) -> list[str]:
    """Sentence-boundary packing. Never splits inside a sentence unless a single
    sentence exceeds the budget (then it is split on the nearest space)."""
    sentences = [s for s in _SENT_END.split(text) if s and s.strip()]
    out: list[str] = []
    buf = ""
    for s in sentences:
        s = s.strip()
        if len(s) > target * 1.6:                     # pathological single sentence
            if buf:
                out.append(buf.strip())
                buf = ""
            words, cur = s.split(), ""
            for w in words:
                if len(cur) + len(w) + 1 > target:
                    out.append(cur.strip())
                    cur = w
                else:
                    cur = f"{cur} {w}".strip()
            if cur:
                out.append(cur.strip())
            continue
        if len(buf) + len(s) + 1 > target and buf:
            out.append(buf.strip())
            # Overlap carries whole trailing SENTENCES, not a character slice.
            # A character slice is how a "fix" for orphaned clauses creates
            # orphaned clauses: every overlapped chunk then starts mid-sentence,
            # and the mid-sentence statistic the lab measures never improves.
            tail = ""
            if overlap:
                carried = []
                for prev in reversed(_SENT_END.split(buf)):
                    prev = prev.strip()
                    if not prev:
                        continue
                    if len(tail) + len(prev) + 1 > overlap:
                        break
                    carried.insert(0, prev)
                    tail = " ".join(carried)
            buf = f"{tail} {s}".strip()
        else:
            buf = f"{buf} {s}".strip()
    if buf.strip():
        out.append(buf.strip())
    return out


def _split_table(md: str, target: int) -> list[str]:
    """Split an over-long markdown table by rows, repeating the header."""
    lines = md.split("\n")
    if len(lines) < 3 or len(md) <= target:
        return [md]
    header, sep, body = lines[0], lines[1], lines[2:]
    out, cur = [], []
    base = len(header) + len(sep) + 2
    size = base
    for row in body:
        if size + len(row) + 1 > target and cur:
            out.append("\n".join([header, sep, *cur]))
            cur, size = [], base
        cur.append(row)
        size += len(row) + 1
    if cur:
        out.append("\n".join([header, sep, *cur]))
    return out


def chunk_document(doc: ParsedDocument, *, doc_meta: dict | None = None,
                   target: int | None = None, overlap: int | None = None) -> list[Chunk]:
    target = target or settings.chunk_target_chars
    overlap = overlap if overlap is not None else settings.chunk_overlap_chars
    doc_meta = dict(doc_meta or {})

    chunks: list[Chunk] = []
    section = ""
    pending: list[Block] = []
    ordinal = 0

    def flush_prose():
        nonlocal pending, ordinal
        if not pending:
            return
        joined = "\n".join(b.text for b in pending)
        prefix = f"{doc_meta.get('title', doc.doc_id)} › {section} ¶ " if section else ""
        for piece in _split_prose(joined, target - len(prefix), overlap):
            body = prefix + piece
            chunks.append(Chunk(
                chunk_id=_stable_id(doc.doc_id, ordinal), doc_id=doc.doc_id,
                text=body, kind="prose", section_title=section, ordinal=ordinal,
                n_chars=len(body),
                starts_mid_sentence=bool(piece) and piece[0].islower(),
                meta={**doc_meta, "format": doc.fmt, "language": doc.language,
                      "page": pending[0].meta.get("page")},
            ))
            ordinal += 1
        pending = []

    for b in doc.blocks:
        if b.kind == "heading":
            flush_prose()
            section = b.text[:120]
        elif b.kind == "table":
            flush_prose()
            caption = f"{doc_meta.get('title', doc.doc_id)} › {section} · table" if section else "table"
            for piece in _split_table(b.text, target):
                body = f"{caption}\n{piece}"
                chunks.append(Chunk(
                    chunk_id=_stable_id(doc.doc_id, ordinal), doc_id=doc.doc_id,
                    text=body, kind="table", section_title=section, ordinal=ordinal,
                    n_chars=len(body), starts_mid_sentence=False,
                    meta={**doc_meta, "format": doc.fmt, "language": doc.language,
                          "page": b.meta.get("page"), "table_rows": b.meta.get("rows")},
                ))
                ordinal += 1
        else:
            pending.append(b)
    flush_prose()
    return chunks


def chunk_quality_stats(chunks: list[Chunk]) -> dict:
    """The numbers Lab 2 step 3 reports and the capstone rubric grades."""
    if not chunks:
        return {"chunks": 0}
    n = len(chunks)
    mid = sum(c.starts_mid_sentence for c in chunks)
    tables = sum(c.kind == "table" for c in chunks)
    docs = len({c.doc_id for c in chunks})
    sizes = sorted(c.n_chars for c in chunks)
    return {
        "chunks": n,
        "documents": docs,
        "chunks_per_doc": round(n / max(docs, 1), 2),
        "table_chunks": tables,
        "mid_sentence_pct": round(100 * mid / n, 1),
        "median_chars": sizes[n // 2],
        "p95_chars": sizes[int(n * 0.95) - 1],
        "empty_chunks": sum(1 for c in chunks if not c.text.strip()),
    }
