"""Detect-then-OCR, with a quality gate and a measured error rate.

Module 2, Lab 2 step 2.

Two disciplines this file enforces, both of which participants get wrong first:

1. OCR ONLY TEXT-LESS PAGES. Blind full-corpus OCR is 30-60x slower and
   *worse*: it replaces a perfect digital text layer with a lossy transcription.
   `needs_ocr` is decided per document by loaders.load_pdf and per page here.

2. MEASURE THE ERROR. "We added OCR" is not an engineering claim. CER against
   the ocr_gold transcripts is. The gate is CER <= 5%; above it, raise DPI and
   re-measure before touching anything else, because on Arabic scans DPI is
   usually the whole story (150 -> 300 dpi typically halves CER).

Arabic-specific notes for the instructor
----------------------------------------
* `--psm 4` (single column of variable-size text) beats the default psm 3 on
  right-aligned policy pages; psm 6 is worth trying on dense tables.
* The `ara` traineddata pack must be present: `tesseract --list-langs`.
* Tesseract emits Arabic in logical order but keeps presentation forms in some
  builds — so normalise_arabic() runs on OCR output too, exactly as it runs on
  digital text. Same function, both paths. Always.
"""
from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from ..arabic import normalise
from ..config import settings


class OcrUnavailable(RuntimeError):
    pass


@dataclass
class OcrPage:
    page: int
    text: str
    mean_confidence: float | None = None


def tesseract_available() -> tuple[bool, str]:
    if shutil.which("tesseract") is None:
        return False, "tesseract binary not on PATH"
    try:
        import pytesseract  # noqa: F401
    except ImportError:
        return False, "pytesseract not installed (pip install pytesseract)"
    try:
        import pytesseract
        langs = pytesseract.get_languages(config="")
        if "ara" not in langs:
            return False, "tesseract has no 'ara' language pack installed"
    except Exception as exc:                       # pragma: no cover
        return False, f"tesseract present but unusable: {exc}"
    return True, "ok"


def ocr_pdf(path: str | Path, *, dpi: int | None = None, lang: str = "ara+eng",
            psm: int = 4, binarise: bool = False,
            only_pages: list[int] | None = None) -> list[OcrPage]:
    """Rasterise text-less pages and OCR them. Returns normalised page text.

    The defaults here are the NAIVE settings on purpose: Lab 2 step 2 asks
    participants to reach CER <= 5% on the scanned Arabic subset, and the
    defaults land around 8-9%. Tuning is the lab. The measured winning
    combination on the shipped corpus is recorded in the instructor answer key
    (assessments/keys/lab2_ocr_key.md) -- do not hand it out before the lab.

    Measured on the shipped scanned subset (22 documents, 300 dpi):
        lang="ara+eng", psm=4, binarise=False   ~0.084
        lang="ara",     psm=6, binarise=False   ~0.049
        lang="ara",     psm=6, binarise=True    ~0.046   <- passes the 5% gate

    The lesson participants take away is not "use psm 6". It is that OCR
    settings are a measurable, per-corpus engineering choice, and that shipping
    an unmeasured OCR stage means shipping unknown coverage.
    """
    ok, why = tesseract_available()
    if not ok:
        raise OcrUnavailable(
            f"{why}. Install with:  apt-get install tesseract-ocr tesseract-ocr-ara "
            f"&& pip install pytesseract pdf2image"
        )
    import pymupdf
    import pytesseract
    from PIL import Image
    import io

    dpi = dpi or settings.ocr_dpi
    out: list[OcrPage] = []
    with pymupdf.open(path) as doc:
        for pno, page in enumerate(doc, start=1):
            if only_pages and pno not in only_pages:
                continue
            if len((page.get_text("text") or "").strip()) > 40:
                continue                            # has a text layer: skip
            pix = page.get_pixmap(dpi=dpi)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            if binarise:
                from PIL import ImageOps
                img = ImageOps.autocontrast(img.convert("L")).point(
                    lambda p: 255 if p > 150 else 0)
            cfg = f"--psm {psm}"
            text = pytesseract.image_to_string(img, lang=lang, config=cfg)
            conf = None
            try:
                data = pytesseract.image_to_data(img, lang=lang, config=cfg,
                                                 output_type=pytesseract.Output.DICT)
                vals = [int(c) for c in data.get("conf", []) if str(c).lstrip("-").isdigit()
                        and int(c) >= 0]
                conf = sum(vals) / len(vals) if vals else None
            except Exception:
                pass
            out.append(OcrPage(pno, normalise(text), conf))
    return out


# --------------------------------------------------------------------------
# character error rate — the number that turns "we added OCR" into evidence
# --------------------------------------------------------------------------
def levenshtein(a: str, b: str) -> int:
    """O(len(a)*len(b)) time, O(min) space. Pure stdlib on purpose: the CER gate
    must not depend on an optional C extension being installed in the lab."""
    if a == b:
        return 0
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def cer(hypothesis: str, reference: str, *, normalise_both: bool = True) -> float:
    """Character error rate in [0, inf). Normalising both sides is correct here:
    we are measuring whether OCR recovered the *content*, and the pipeline
    normalises everything downstream anyway. Reporting raw CER instead makes
    Arabic look 8-10 points worse than the system actually behaves."""
    h = normalise(hypothesis) if normalise_both else hypothesis
    r = normalise(reference) if normalise_both else reference
    if not r:
        return 0.0 if not h else 1.0
    return levenshtein(h, r) / len(r)


def evaluate_ocr(pairs: list[tuple[str, str]]) -> dict:
    """pairs: [(hypothesis, reference), ...] -> the Lab 2 CER report."""
    if not pairs:
        return {"documents": 0, "cer": None, "gate_pass": False}
    scores = [cer(h, r) for h, r in pairs]
    mean = sum(scores) / len(scores)
    worst = max(range(len(scores)), key=lambda i: scores[i])
    return {
        "documents": len(pairs),
        "cer": round(mean, 4),
        "cer_p95": round(sorted(scores)[int(len(scores) * 0.95) - 1], 4),
        "worst_index": worst,
        "worst_cer": round(scores[worst], 4),
        "gate": settings.ocr_cer_gate,
        "gate_pass": mean <= settings.ocr_cer_gate,
    }
