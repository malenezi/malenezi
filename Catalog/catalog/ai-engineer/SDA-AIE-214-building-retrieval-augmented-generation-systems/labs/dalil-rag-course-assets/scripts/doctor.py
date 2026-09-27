#!/usr/bin/env python3
"""
doctor.py -- verify the lab environment BEFORE the lab, not during it.

The T-minus-2-days email tells participants to run this. Every check below
corresponds to a real, repeatedly observed classroom failure, and each one
prints the fix rather than the symptom.

    python scripts/doctor.py
    make doctor
"""
from __future__ import annotations

import importlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

OK, WARN, FAIL = "  ok ", " warn", " FAIL"
rows: list[tuple[str, str, str]] = []


def check(name: str, ok: bool, detail: str = "", warn_only: bool = False):
    rows.append((WARN if (not ok and warn_only) else (OK if ok else FAIL), name, detail))
    return ok


def module(name: str, hint: str, required: bool = True):
    try:
        importlib.import_module(name)
        return check(f"python: {name}", True)
    except ImportError:
        return check(f"python: {name}", False, hint, warn_only=not required)


def main() -> int:
    check("python >= 3.11", sys.version_info >= (3, 11), sys.version.split()[0])

    for m, hint, req in [
        ("yaml", "pip install pyyaml", True),
        ("pymupdf", "pip install pymupdf", True),
        ("docx", "pip install python-docx", True),
        ("openpyxl", "pip install openpyxl", True),
        ("PIL", "pip install pillow", True),
        ("sentence_transformers", "pip install sentence-transformers  [Lab 3+]", False),
        ("qdrant_client", "pip install qdrant-client  [Lab 3+]", False),
        ("fastembed", "pip install fastembed  [Lab 4 sparse vectors]", False),
        ("FlagEmbedding", "pip install FlagEmbedding  [Lab 4 reranker]", False),
        ("openai", "pip install openai  [Lab 5+ gateway]", False),
        ("ragas", "pip install ragas datasets  [Lab 6]", False),
        ("pytesseract", "pip install pytesseract  [Lab 2 OCR]", False),
        ("arabic_reshaper", "pip install arabic-reshaper python-bidi  [corpus build]", False),
    ]:
        module(m, hint, req)

    # ---- OCR toolchain ---------------------------------------------------
    tess = shutil.which("tesseract")
    check("tesseract binary", bool(tess),
          tess or "apt-get install tesseract-ocr tesseract-ocr-ara")
    if tess:
        try:
            langs = subprocess.run([tess, "--list-langs"], capture_output=True,
                                   text=True, timeout=20).stdout
            check("tesseract 'ara' language pack", "ara" in langs,
                  "apt-get install tesseract-ocr-ara")
        except Exception as exc:
            check("tesseract 'ara' language pack", False, str(exc))

    # ---- Arabic font for corpus generation --------------------------------
    fonts = [p for p in ("/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf",
                         "/usr/share/fonts/opentype/fonts-hosny-amiri/Amiri-Regular.ttf")
             if Path(p).exists()]
    check("Arabic font (Noto Naskh / Amiri)", bool(fonts),
          fonts[0] if fonts else "apt-get install fonts-noto-core  "
                                 "[only needed to REGENERATE the corpus]", warn_only=True)
    try:
        from PIL import features
        check("Pillow Raqm text layout", features.check("raqm"),
              "needed only to regenerate scanned Arabic pages", warn_only=True)
    except Exception:
        pass

    # ---- Qdrant -----------------------------------------------------------
    try:
        from dalil.config import settings
        import requests
        r = requests.get(f"{settings.qdrant_url}/collections", timeout=4)
        check("Qdrant reachable", r.status_code == 200, settings.qdrant_url, warn_only=True)
    except Exception as exc:
        check("Qdrant reachable", False,
              f"docker compose up -d qdrant  ({type(exc).__name__})", warn_only=True)

    # ---- gateway ----------------------------------------------------------
    from dalil.config import settings
    check("LLM gateway key set", bool(settings.llm_api_key),
          "export DALIL_LLM_API_KEY=...  (per-participant key from the instructor)",
          warn_only=True)

    # ---- model cache ------------------------------------------------------
    import os
    hf = os.getenv("HF_HOME")
    check("HF_HOME points at the course bundle", bool(hf),
          hf or "export HF_HOME=/course/models  — otherwise bge-m3 downloads mid-lab",
          warn_only=True)

    # ---- data -------------------------------------------------------------
    check("corpus generated", (ROOT / "data/corpus/layer_b_index.json").exists(),
          "make corpus")
    check("evaluation sets built", (ROOT / "data/golden/golden_qa_v1.jsonl").exists(),
          "make eval-sets")
    lock = ROOT / "corpus/LOCK.json"
    if lock.exists():
        data = json.loads(lock.read_text(encoding="utf-8"))
        got = sum(1 for d in data["documents"] if d["status"] == "OK")
        check("Layer A (real SDAIA documents) fetched", got >= 10,
              f"{got} resolved — run `make corpus-fetch` on a networked machine",
              warn_only=True)
    else:
        check("Layer A (real SDAIA documents) fetched", False,
              "make corpus-fetch  — labs run on Layer B alone, but the corpus is "
              "much weaker without the real regulation", warn_only=True)

    width = max(len(n) for _, n, _ in rows) + 2
    print()
    for status, name, detail in rows:
        # the fix is only useful when something is wrong
        print(f"[{status}] {name:<{width}} {detail if status != OK else ''}")
    fails = sum(1 for s, _, _ in rows if s == FAIL)
    warns = sum(1 for s, _, _ in rows if s == WARN)
    print(f"\n{len(rows)} checks · {fails} failed · {warns} warnings")
    if fails:
        print("Fix the FAILs before the lab. WARNs are fine on Day 1 and must be "
              "cleared by the day the relevant lab runs.")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
