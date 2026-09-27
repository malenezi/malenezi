"""Parser registry — format dispatch with explicit, *loud* failure handling.

Module 2, failure class F1 (parsing loss).

The design rule of this file: a document may fail to parse, but it may never
fail SILENTLY. Every extractor returns structured blocks with a `kind`, and
every document carries a `parse_quality` score and a `quarantined` flag. A
pipeline that reports "300/300 parsed" while 28 of them produced empty strings
is the most expensive bug in RAG, because it is invisible until a citizen asks
the question whose answer was dropped.

Blocks, not strings
-------------------
Every loader emits `Block(kind, text, meta)` where kind is one of:

    heading | paragraph | table | list | caption

Tables are emitted as ONE block containing a markdown-serialised table, never
as loose cells. `" ".join(cells)` turns "Grade 11 | 9,900 | SAR/month" into
"Grade 11 9,900 SAR month" — a string that no longer answers "what is the
Grade 11 housing allowance?". That single line of lazy code is the case study
in Module 2, and it is why `_serialise_table` exists.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from ..arabic import normalise, has_arabic


class ParseError(RuntimeError):
    """Raised when a document cannot be parsed at all."""


@dataclass
class Block:
    kind: str                      # heading|paragraph|table|list|caption
    text: str
    meta: dict = field(default_factory=dict)


@dataclass
class ParsedDocument:
    doc_id: str
    path: str
    fmt: str
    blocks: list[Block]
    needs_ocr: bool = False
    parse_quality: float = 1.0     # 0..1 — chars of usable text / expected
    quarantined: bool = False
    warnings: list[str] = field(default_factory=list)
    meta: dict = field(default_factory=dict)

    @property
    def text(self) -> str:
        return "\n\n".join(b.text for b in self.blocks)

    @property
    def n_chars(self) -> int:
        return sum(len(b.text) for b in self.blocks)

    @property
    def language(self) -> str:
        return "ar" if has_arabic(self.text[:4000]) else "en"


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def _serialise_table(rows: list[list[str]]) -> str:
    """Markdown-serialise a table so the header travels with every cell.

    Why markdown and not JSON or CSV: the embedding model and the LLM both read
    markdown tables natively, header row included, so 'Grade 11' stays adjacent
    to '9,900' in the token stream. This is the difference between a retrievable
    allowance figure and an F1.
    """
    rows = [[(c if c is not None else "").strip().replace("\n", " ") for c in r] for r in rows]
    rows = [r for r in rows if any(r)]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    head, body = rows[0], rows[1:]
    out = ["| " + " | ".join(head) + " |",
           "| " + " | ".join(["---"] * width) + " |"]
    out += ["| " + " | ".join(r) + " |" for r in body]
    return "\n".join(out)


_HEADING_RE = re.compile(r"^\s*(?:\d+(?:\.\d+)*[.)]?\s+|[أ-ي]+\s*[:ً]?\s*)?[A-Z؀-ۿ][^\n]{0,90}$")


def _looks_like_heading(line: str) -> bool:
    s = line.strip()
    if not s or len(s) > 95:
        return False
    if s.endswith((".", "،", ";")):
        return False
    if re.match(r"^\s*\d+(\.\d+)*[.)]\s+\S", s):
        return True
    if re.match(r"^(أولا|ثانيا|ثالثا|رابعا|خامسا|سادسا)\b", normalise(s)):
        return True
    words = s.split()
    return 1 <= len(words) <= 9 and (s[0].isupper() or has_arabic(s))


# --------------------------------------------------------------------------
# format loaders
# --------------------------------------------------------------------------
def load_pdf(path: Path, doc_id: str) -> ParsedDocument:
    try:
        import pymupdf
    except ImportError as exc:                     # pragma: no cover
        raise ParseError("pymupdf is required for PDF parsing: pip install pymupdf") from exc

    blocks: list[Block] = []
    warnings: list[str] = []
    text_chars = 0
    with pymupdf.open(path) as doc:
        n_pages = doc.page_count
        for pno, page in enumerate(doc, start=1):
            # 1) real tables first — they must not be re-extracted as prose
            table_rects = []
            try:
                finder = page.find_tables()
                for t in finder.tables:
                    rows = t.extract()
                    md = _serialise_table(rows)
                    if md:
                        blocks.append(Block("table", normalise(md),
                                            {"page": pno, "rows": len(rows)}))
                        text_chars += len(md)
                        table_rects.append(t.bbox)
            except Exception as exc:               # table finder is best-effort
                warnings.append(f"table detection failed on p{pno}: {type(exc).__name__}")

            # 2) prose outside the table rectangles.
            #    Line-by-line, because heading detection is a per-LINE decision:
            #    normalising the whole page first collapses newlines and every
            #    heading disappears into the paragraph that follows it. That
            #    single ordering mistake costs ~15 points of section-title
            #    coverage downstream, which the chunker needs to prefix chunks.
            raw = page.get_text("text") or ""
            # cell-level suppression: a table cell re-emitted as a prose line
            # is a duplicated fact that will compete with its own table chunk
            # at retrieval time and split the ranking signal.
            table_text = {
                cell.strip()
                for b in blocks
                if b.kind == "table" and b.meta.get("page") == pno
                for ln in b.text.split("\n")
                for cell in ln.strip().strip("|").split("|")
                if cell.strip() and cell.strip() != "---"
            }
            para: list[str] = []
            for line in raw.split("\n"):
                stripped = line.strip()
                if not stripped:
                    if para:
                        s = normalise(" ".join(para))
                        if s:
                            text_chars += len(s)
                            blocks.append(Block("paragraph", s, {"page": pno}))
                        para = []
                    continue
                if normalise(stripped) in table_text:      # already captured as a table
                    continue
                if _looks_like_heading(stripped):
                    if para:
                        s = normalise(" ".join(para))
                        if s:
                            text_chars += len(s)
                            blocks.append(Block("paragraph", s, {"page": pno}))
                        para = []
                    s = normalise(stripped)
                    text_chars += len(s)
                    blocks.append(Block("heading", s, {"page": pno}))
                else:
                    para.append(stripped)
            if para:
                s = normalise(" ".join(para))
                if s:
                    text_chars += len(s)
                    blocks.append(Block("paragraph", s, {"page": pno}))

    expected = max(n_pages * 400, 1)               # ~400 usable chars/page floor
    quality = min(1.0, text_chars / expected)
    needs_ocr = text_chars < 40 * n_pages          # essentially no text layer
    if needs_ocr:
        warnings.append("no usable text layer — routed to OCR")
    return ParsedDocument(doc_id, str(path), "pdf", blocks, needs_ocr=needs_ocr,
                          parse_quality=quality, warnings=warnings,
                          meta={"pages": n_pages})


def load_docx(path: Path, doc_id: str) -> ParsedDocument:
    try:
        from docx import Document
    except ImportError as exc:                     # pragma: no cover
        raise ParseError("python-docx is required: pip install python-docx") from exc

    d = Document(str(path))
    blocks: list[Block] = []
    for p in d.paragraphs:
        s = normalise(p.text)
        if not s:
            continue
        style = (p.style.name or "").lower()
        kind = "heading" if style.startswith("heading") else (
            "list" if "list" in style else "paragraph")
        blocks.append(Block(kind, s, {"style": p.style.name}))
    for t in d.tables:
        rows = [[c.text for c in r.cells] for r in t.rows]
        md = _serialise_table(rows)
        if md:
            blocks.append(Block("table", normalise(md), {"rows": len(rows)}))
    quality = 1.0 if blocks else 0.0
    return ParsedDocument(doc_id, str(path), "docx", blocks, parse_quality=quality,
                          quarantined=not blocks,
                          warnings=[] if blocks else ["docx produced no text"])


def load_xlsx(path: Path, doc_id: str) -> ParsedDocument:
    try:
        from openpyxl import load_workbook
    except ImportError as exc:                     # pragma: no cover
        raise ParseError("openpyxl is required: pip install openpyxl") from exc

    wb = load_workbook(str(path), data_only=True, read_only=True)
    blocks: list[Block] = []
    for ws in wb.worksheets:
        rows = [[("" if c is None else str(c)) for c in row]
                for row in ws.iter_rows(values_only=True)]
        rows = [r for r in rows if any(x.strip() for x in r)]
        if not rows:
            continue
        blocks.append(Block("heading", normalise(f"{path.stem} — {ws.title}"),
                            {"sheet": ws.title}))
        # split trailing note rows (single populated cell) away from the grid
        grid = [r for r in rows if sum(1 for x in r if x.strip()) > 1]
        notes = [r for r in rows if sum(1 for x in r if x.strip()) == 1]
        md = _serialise_table(grid)
        if md:
            blocks.append(Block("table", normalise(md),
                                {"sheet": ws.title, "rows": len(grid)}))
        for n in notes:
            s = normalise(" ".join(x for x in n if x.strip()))
            if s:
                blocks.append(Block("caption", s, {"sheet": ws.title}))
    wb.close()
    return ParsedDocument(doc_id, str(path), "xlsx", blocks,
                          parse_quality=1.0 if blocks else 0.0,
                          quarantined=not blocks)


_TAG = re.compile(r"<[^>]+>")
_DROP = re.compile(r"<(script|style|nav|footer|header|form)\b.*?</\1>", re.I | re.S)


def load_html(path: Path, doc_id: str) -> ParsedDocument:
    raw = path.read_text(encoding="utf-8", errors="replace")
    warnings: list[str] = []
    body = raw
    try:
        import trafilatura                          # best extractor when present
        extracted = trafilatura.extract(raw, include_tables=True, favor_recall=True)
        if extracted:
            body = extracted
        else:
            warnings.append("trafilatura returned nothing — fell back to tag stripping")
            body = _TAG.sub("\n", _DROP.sub(" ", raw))
    except ImportError:
        warnings.append("trafilatura not installed — boilerplate stripping is approximate")
        body = _TAG.sub("\n", _DROP.sub(" ", raw))

    blocks = []
    for para in re.split(r"\n\s*\n|\n(?=\S)", body):
        s = normalise(para)
        if len(s) < 3:
            continue
        blocks.append(Block("heading" if _looks_like_heading(s) else "paragraph", s, {}))
    return ParsedDocument(doc_id, str(path), "html", blocks,
                          parse_quality=1.0 if blocks else 0.0,
                          quarantined=not blocks, warnings=warnings)


def load_txt(path: Path, doc_id: str) -> ParsedDocument:
    body = path.read_text(encoding="utf-8", errors="replace")
    blocks = [Block("paragraph", normalise(p), {})
              for p in re.split(r"\n\s*\n", body) if normalise(p)]
    return ParsedDocument(doc_id, str(path), "txt", blocks,
                          parse_quality=1.0 if blocks else 0.0)


REGISTRY: dict[str, Callable[[Path, str], ParsedDocument]] = {
    ".pdf": load_pdf,
    ".docx": load_docx,
    ".xlsx": load_xlsx,
    ".xlsm": load_xlsx,
    ".html": load_html,
    ".htm": load_html,
    ".txt": load_txt,
    ".md": load_txt,
}


def load(path: str | Path, doc_id: str | None = None) -> ParsedDocument:
    """Dispatch on extension. Unsupported formats raise — they are never skipped.

    The lab's step 1 asks participants to read the parse report and count
    `unsupported format` errors. If this function returned an empty document
    instead of raising, that count would always be zero and the corpus would
    lose documents in silence.
    """
    p = Path(path)
    doc_id = doc_id or p.stem
    fn = REGISTRY.get(p.suffix.lower())
    if fn is None:
        raise ParseError(f"unsupported format {p.suffix!r} for {p.name} "
                         f"(known: {', '.join(sorted(REGISTRY))})")
    doc = fn(p, doc_id)
    if doc.parse_quality < 0.15 and not doc.needs_ocr:
        doc.quarantined = True
        doc.warnings.append(f"parse quality {doc.parse_quality:.2f} below threshold — quarantined")
    return doc
