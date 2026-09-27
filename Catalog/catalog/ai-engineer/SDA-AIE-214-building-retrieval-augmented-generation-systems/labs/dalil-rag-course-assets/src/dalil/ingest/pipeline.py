"""The whole offline path, end to end, with a report you can put on a slide.

    corpus dir -> load() -> [OCR if text-less] -> normalise -> chunk
               -> lifecycle metadata -> chunks.jsonl + ingest_report.json

Run:
    python -m dalil.ingest.pipeline --corpus data/corpus/corpus_v1 --out data/index
    python -m dalil.ingest.pipeline --naive        # Lab 1's deliberately bad baseline
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from .loaders import load, ParseError
from .chunker import chunk_document, chunk_quality_stats, Chunk, _stable_id
from .ocr import ocr_pdf, OcrUnavailable, evaluate_ocr
from ..arabic import normalise
from ..config import settings

SUPPORTED = {".pdf", ".docx", ".xlsx", ".html", ".htm", ".txt", ".md"}


def load_layer_b_index(corpus_root: Path) -> dict[str, dict]:
    """Ground-truth metadata for synthetic documents (tier, lifecycle, dates).

    Layer A documents are not in this index; their metadata comes from the
    manifest. Anything in neither gets conservative defaults: access_tier
    'restricted' and lifecycle 'unknown'. Defaulting to restricted is the safe
    direction — an unclassified document that leaks is an incident; an
    unclassified document that is over-protected is a support ticket.
    """
    idx_path = corpus_root.parent / "layer_b_index.json"
    if not idx_path.exists():
        idx_path = corpus_root / "layer_b_index.json"
    if not idx_path.exists():
        return {}
    data = json.loads(idx_path.read_text(encoding="utf-8"))
    return {d["doc_id"]: d for d in data.get("documents", [])}


def load_layer_a_meta(root: Path) -> dict[str, dict]:
    lock = root / "corpus" / "LOCK.json"
    manifest = root / "corpus" / "manifest" / "sdaia_layer_a.yaml"
    out: dict[str, dict] = {}
    if manifest.exists():
        try:
            import yaml
            man = yaml.safe_load(manifest.read_text(encoding="utf-8"))
            for d in man.get("documents", []):
                out[d["id"]] = {
                    "doc_id": d["id"], "title_en": d.get("title_en"),
                    "title_ar": d.get("title_ar"), "department": d.get("department", "legal"),
                    "access_tier": d.get("access_tier", "public"),
                    "lifecycle": d.get("lifecycle", "current"),
                    "authority": d.get("authority", "SDAIA"), "layer": "A",
                    "doc_class": d.get("doc_class"),
                }
        except Exception:
            pass
    return out


def naive_chunks(text: str, doc_id: str, size: int = 500) -> list[Chunk]:
    """Lab 1's baseline: fixed-size character splits, no structure, no metadata.
    Kept in the codebase on purpose — participants diff it against the real
    chunker in Lab 2 and watch mid-sentence starts fall from ~41% to <8%."""
    out = []
    for i in range(0, len(text), size):
        piece = text[i:i + size]
        out.append(Chunk(chunk_id=_stable_id(doc_id, i // size), doc_id=doc_id,
                         text=piece, kind="prose", ordinal=i // size,
                         n_chars=len(piece),
                         starts_mid_sentence=bool(piece) and piece[0].islower(),
                         meta={"naive": True}))
    return out


def run(corpus: Path, out_dir: Path, *, naive: bool = False, do_ocr: bool = True,
        limit: int | None = None, ocr_gold: Path | None = None,
        ocr_lang: str = "ara+eng", ocr_psm: int = 4, ocr_binarise: bool = False,
        corpus_version: str | None = None, overlay: Path | None = None) -> dict:
    root = Path(__file__).resolve().parents[3]
    meta_b = load_layer_b_index(corpus)
    meta_a = load_layer_a_meta(root)

    corpus_version = corpus_version or ("v2" if corpus.name.endswith("v2") or overlay
                                       else "v1")
    roots = [corpus] + ([overlay] if overlay else [])
    files = sorted(p for root in roots for p in root.rglob("*")
                   if p.is_file() and p.suffix.lower() in SUPPORTED)
    unsupported = sorted(p for root in roots for p in root.rglob("*")
                         if p.is_file() and p.suffix.lower() not in SUPPORTED
                         and p.suffix.lower() not in {".json", ".ini"})
    if limit:
        files = files[:limit]

    chunks: list[Chunk] = []
    report = {
        "corpus": [str(r) for r in roots], "corpus_version": corpus_version,
        "mode": "naive" if naive else "structure-aware",
        "documents_seen": len(files), "by_format": Counter(), "parsed": 0,
        "needs_ocr": 0, "ocr_done": 0, "ocr_skipped_reason": None,
        "quarantined": [], "errors": [], "unsupported": [str(p) for p in unsupported],
        "warnings": Counter(),
    }
    ocr_pairs: list[tuple[str, str]] = []

    for f in files:
        doc_id = f.stem
        try:
            doc = load(f, doc_id)
        except ParseError as exc:
            report["errors"].append({"file": str(f), "error": str(exc)})
            continue
        report["parsed"] += 1
        report["by_format"][doc.fmt] += 1
        for w in doc.warnings:
            report["warnings"][w.split("—")[0].strip()] += 1

        if doc.needs_ocr:
            report["needs_ocr"] += 1
            if do_ocr:
                try:
                    pages = ocr_pdf(f, lang=ocr_lang, psm=ocr_psm,
                                   binarise=ocr_binarise)
                    from .loaders import Block
                    doc.blocks = [Block("paragraph", p.text, {"page": p.page, "ocr": True})
                                  for p in pages if p.text]
                    doc.needs_ocr = False
                    report["ocr_done"] += 1
                    if ocr_gold:
                        gold = ocr_gold / f"{doc_id}.txt"
                        if gold.exists():
                            ocr_pairs.append((doc.text, gold.read_text(encoding="utf-8")))
                except OcrUnavailable as exc:
                    report["ocr_skipped_reason"] = str(exc)

        if doc.quarantined or not doc.blocks:
            report["quarantined"].append(doc_id)
            continue

        dm = dict(meta_b.get(doc_id) or meta_a.get(doc_id) or {})
        # Lifecycle is a function of WHICH corpus version you are indexing.
        # In corpus_v1 a circular that will later be superseded is still the
        # current instrument; it only becomes stale on Day 4 when its v2
        # lands. Baking "superseded" into the document itself would make the
        # staleness drill unfalsifiable — the system would look correct on
        # Day 1 for the wrong reason.
        by_corpus = dm.pop("lifecycle_by_corpus", None)
        if by_corpus:
            dm["lifecycle"] = by_corpus.get(corpus_version, dm.get("lifecycle", "current"))
        dm.setdefault("layer", "B" if doc_id in meta_b else "unknown")
        dm.setdefault("access_tier", "restricted")
        dm.setdefault("lifecycle", "unknown")
        dm.setdefault("department", "general")
        dm["title"] = dm.get("title_en") or dm.get("title_ar") or doc_id
        dm.pop("facts", None)
        dm.pop("path", None)

        chunks += (naive_chunks(doc.text, doc_id) if naive
                   else chunk_document(doc, doc_meta=dm))

    stats = chunk_quality_stats(chunks)
    report["chunk_stats"] = stats
    report["by_format"] = dict(report["by_format"])
    report["warnings"] = dict(report["warnings"])
    if ocr_pairs:
        report["ocr_eval"] = evaluate_ocr(ocr_pairs)

    out_dir.mkdir(parents=True, exist_ok=True)
    suffix = "" if corpus_version == "v1" else f"_{corpus_version}"
    name = f"chunks_naive{suffix}.jsonl" if naive else f"chunks{suffix}.jsonl"
    with (out_dir / name).open("w", encoding="utf-8") as fh:
        for c in chunks:
            fh.write(json.dumps(c.to_payload(), ensure_ascii=False) + "\n")
    (out_dir / (f"ingest_report_naive{suffix}.json" if naive
                else f"ingest_report{suffix}.json")).write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", type=Path, default=Path(settings.corpus_dir))
    ap.add_argument("--out", type=Path, default=Path("data/index"))
    ap.add_argument("--naive", action="store_true", help="Lab 1 baseline chunking")
    ap.add_argument("--no-ocr", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--ocr-gold", type=Path, default=Path("data/corpus/ocr_gold"))
    ap.add_argument("--ocr-lang", default="ara+eng")
    ap.add_argument("--ocr-psm", type=int, default=4)
    ap.add_argument("--ocr-binarise", action="store_true")
    ap.add_argument("--overlay", type=Path,
                    help="second corpus root layered on top (Day 4: corpus_v2)")
    ap.add_argument("--corpus-version", choices=["v1", "v2"],
                    help="which lifecycle view to stamp on chunks")
    a = ap.parse_args()

    rep = run(a.corpus, a.out, naive=a.naive, do_ocr=not a.no_ocr, limit=a.limit,
              ocr_gold=a.ocr_gold if a.ocr_gold.exists() else None,
              ocr_lang=a.ocr_lang, ocr_psm=a.ocr_psm, ocr_binarise=a.ocr_binarise,
              corpus_version=a.corpus_version, overlay=a.overlay)
    s = rep["chunk_stats"]
    print(f"Parsed {rep['parsed']}/{rep['documents_seen']} docs "
          f"({', '.join(f'{v} {k}' for k, v in rep['by_format'].items())})")
    print(f"  needs_ocr {rep['needs_ocr']}, ocr_done {rep['ocr_done']}"
          + (f"  [{rep['ocr_skipped_reason']}]" if rep["ocr_skipped_reason"] else ""))
    print(f"  unsupported {len(rep['unsupported'])}, quarantined {len(rep['quarantined'])}, "
          f"errors {len(rep['errors'])}")
    print(f"Chunks: {s.get('chunks')} (avg {s.get('chunks_per_doc')}/doc)  "
          f"tables kept whole: {s.get('table_chunks')}")
    print(f"Mid-sentence starts: {s.get('mid_sentence_pct')}%")
    if "ocr_eval" in rep:
        e = rep["ocr_eval"]
        print(f"OCR CER: {e['cer']:.3f} (gate {e['gate']}) "
              f"{'PASS' if e['gate_pass'] else 'FAIL'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
