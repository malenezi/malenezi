"""Arabic text normalisation — the single highest-leverage 40 lines in the course.

WHY THIS MODULE EXISTS (Module 2 / Module 3, failure class F3)
--------------------------------------------------------------
A bilingual corpus fails retrieval in ways an English-only corpus never does,
and almost all of them are *string* problems, not model problems:

  1. PRESENTATION FORMS. PDFs produced without a bidi engine store Arabic as
     Unicode presentation forms (U+FB50–U+FEFF) instead of base letters. The
     text looks perfect on screen and is invisible to every lexical matcher and
     badly embedded by every tokenizer. NFKC folding fixes it. Real SDAIA and
     real ministry PDFs both exhibit this; so does the course's Layer B corpus,
     deliberately.
  2. ORTHOGRAPHIC VARIANTS. أ إ آ ا all appear for the same word; ى/ي and ة/ه
     alternate by author. "اجراءات" and "إجراءات" must match.
  3. DIACRITICS AND TATWEEL. Decorative, semantically empty, and they split
     tokens.
  4. DIGIT SETS. ٤٤/٢٠٢٥ and 44/2025 are the same circular. An identifier query
     that misses because of digit set is the most infuriating F4 there is.

THE RULE THE COURSE REPEATS UNTIL IT STICKS
    Normalise at INDEX time and at QUERY time with the SAME function.
    Normalising on one side only is worse than not normalising at all: it
    guarantees divergence between the indexed text and the query.

Deliberately NOT done here: stemming and stopword removal. Both help BM25 a
little and hurt dense embeddings a lot, and neither is needed once folding and
digit unification are in place. Measure before you add them — that is Lab 3's
mini-exercise, not a default.
"""
from __future__ import annotations

import re
import unicodedata

# Arabic-Indic and Extended Arabic-Indic digits -> ASCII
_DIGITS = {ord(c): str(i) for i, c in enumerate("٠١٢٣٤٥٦٧٨٩")}
_DIGITS.update({ord(c): str(i) for i, c in enumerate("۰۱۲۳۴۵۶۷۸۹")})

# Harakat, tanween, shadda, sukun, superscript alef, and tatweel
_DIACRITICS = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")

_ALEF = re.compile(r"[إأآٱ]")
_YA = re.compile(r"ى")
_TA_MARBUTA = re.compile(r"ة")
_WS = re.compile(r"\s+")

# Punctuation unification: Arabic comma/semicolon/question mark -> ASCII
_PUNCT = {ord("،"): ",", ord("؛"): ";", ord("؟"): "?", ord("٪"): "%", ord("ـ"): ""}

ARABIC_BLOCK = re.compile(r"[؀-ۿﭐ-﻿]")


def has_arabic(text: str) -> bool:
    return bool(ARABIC_BLOCK.search(text or ""))


def fold_presentation_forms(text: str) -> str:
    """Map Arabic presentation forms back to base letters (pathology #1)."""
    return unicodedata.normalize("NFKC", text)


def normalise_arabic(text: str, *, fold_orthography: bool = True,
                     unify_digits: bool = True) -> str:
    """The one function that must run at BOTH index and query time.

    Parameters are exposed only so Lab 3's ablation exercise can turn each
    behaviour off and measure the recall cost. Production uses the defaults.
    """
    if not text:
        return ""
    t = fold_presentation_forms(text)
    t = t.translate(_PUNCT)
    t = _DIACRITICS.sub("", t)
    if unify_digits:
        t = t.translate(_DIGITS)
    if fold_orthography:
        t = _ALEF.sub("ا", t)
        t = _YA.sub("ي", t)
        t = _TA_MARBUTA.sub("ه", t)
    return _WS.sub(" ", t).strip()


def normalise(text: str) -> str:
    """Language-agnostic entry point used by the ingest and query paths.

    Latin text passes through NFKC + whitespace collapse only; Arabic gets the
    full treatment. Calling this on every string is cheap and removes the class
    of bug where someone forgets to check the language first.
    """
    if not text:
        return ""
    if has_arabic(text):
        return normalise_arabic(text)
    return _WS.sub(" ", unicodedata.normalize("NFKC", text)).strip()


def normalise_identifier(text: str) -> str:
    """Aggressive form for identifier matching: '٤٤ / ٢٠٢٥' -> '44/2025'.

    Used by the sparse/lexical path and by the identifier query-class detector.
    Separators are collapsed so 'Circular 44-2025', 'circular 44/2025' and
    'التعميم ٤٤/٢٠٢٥' all reduce to the same key.
    """
    t = normalise(text)
    # Collapse separators ONLY between digits: "44 - 2025" and "44/2025" are the
    # same circular, but "NDSA-HR-101" is one token and must stay one token.
    t = re.sub(r"(?<=\d)\s*[/\-–—]\s*(?=\d)", "/", t)
    return t.lower()


IDENTIFIER_PATTERNS = [
    re.compile(r"\b\d{1,4}\s*/\s*\d{2,4}\b"),          # 44/2025
    re.compile(r"\b(?:NDSA|SDA)-[A-Z]{2,6}-\d{1,4}\b", re.I),
    re.compile(r"\barticle\s+\d+\b", re.I),
    re.compile(r"\bالمادة\s+\S+"),
    re.compile(r"\bتعميم\s*\S*\d"),
    re.compile(r"\bcircular\s+\d", re.I),
]


def contains_identifier(text: str) -> bool:
    """True when a query is carrying an exact token dense retrieval will blur.

    This is the gate that decides whether the sparse leg of hybrid retrieval is
    mandatory for a query — see retrieve/router.py and Module 4.
    """
    t = normalise_identifier(text)
    return any(p.search(t) for p in IDENTIFIER_PATTERNS)
