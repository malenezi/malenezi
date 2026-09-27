"""Query classification and routing — Module 4 (diagnosis) and Module 7 (cost).

Two jobs, one taxonomy:

  * Module 4 uses the classes to REPORT per class. An aggregate nDCG of 0.71
    hides an identifier class sitting at 0.31; the capstone rubric caps a
    submission at 70% for aggregate-only reporting precisely because of this.
  * Module 7 uses the classes to ROUTE. Multi-hop decomposition on a simple
    factoid is 3x the latency for zero gain, and a corrective loop on an
    out-of-scope question is money spent to eventually refuse.

The classifier is rules-first on purpose. It is auditable, free, deterministic
(so evaluation deltas are signal, not judge noise), and on this corpus it
agrees with the human labels on ~90% of the golden set. An LLM classifier is
Lab 7's optional extension, and the honest comparison — accuracy gain vs added
latency and non-determinism — is exactly the trade-off literacy the course is
trying to build.
"""
from __future__ import annotations

import re
from enum import Enum

from ..arabic import contains_identifier, normalise


class QueryClass(str, Enum):
    IDENTIFIER = "identifier"        # names a circular, article, doc code
    FACTOID = "factoid"              # one fact, one document
    TABULAR = "tabular"              # a number that lives in a table
    MULTI_HOP = "multi_hop"          # needs two or more documents composed
    CONDITIONAL = "conditional"      # entitlement under stated conditions
    COMPARATIVE = "comparative"      # difference between two things
    PROCEDURAL = "procedural"        # steps / how do I
    UNANSWERABLE = "unanswerable"    # out of corpus scope -> must refuse
    AMBIGUOUS = "ambiguous"          # under-specified -> multi-query expansion


_MULTI_HOP = [
    r"\band\b.*\b(also|then|as well)\b", r"both\b.*\band\b",
    r"\bcompared with\b", r"\bwhich .* and .* (require|apply)",
    r"\bwhat does .* say .* and .*\b",
    r"وما\b", r"\bوكذلك\b", r"\bمع\s+بيان\b", r"\bوما هي\s+.*\s+ذات العلاقة",
]
_COMPARATIVE = [r"\b(difference|differ|versus|vs\.?|compare|which is (higher|lower))\b",
                r"\b(الفرق|مقارنة|أيهما)\b"]
_CONDITIONAL = [r"\bif\b", r"\bwhen\b.*\b(then|does|is)\b", r"\bunder what (conditions|circumstances)\b",
                r"\bam i (eligible|entitled)\b", r"\b(إذا|في حال|متى)\b", r"\bهل يحق\b"]
_PROCEDURAL = [r"\bhow (do|can) i\b", r"\bwhat( are|'s) the steps\b", r"\bprocedure for\b",
               r"\bكيف\b", r"\bما هي الخطوات\b", r"\bإجراءات\b"]
_TABULAR = [r"\b(how much|what is the (amount|rate|band|ceiling|allowance))\b",
            r"\bgrade\s*\d+\b", r"\bper[- ]diem\b",
            r"\b(كم|مقدار|قيمة|شريحة|سقف)\b", r"\bالمرتبة\s*\d+\b"]
_OUT_OF_SCOPE = [r"\b(weather|football|stock price|recipe|flight)\b",
                 r"\b(الطقس|كرة القدم|وصفة)\b"]


def _any(patterns: list[str], text: str) -> bool:
    return any(re.search(p, text, re.I) for p in patterns)


def classify_query(query: str) -> QueryClass:
    q = normalise(query)
    if _any(_OUT_OF_SCOPE, q):
        return QueryClass.UNANSWERABLE
    if contains_identifier(query):
        return QueryClass.IDENTIFIER
    if _any(_MULTI_HOP, q):
        return QueryClass.MULTI_HOP
    if _any(_COMPARATIVE, q):
        return QueryClass.COMPARATIVE
    if _any(_TABULAR, q):
        return QueryClass.TABULAR
    if _any(_CONDITIONAL, q):
        return QueryClass.CONDITIONAL
    if _any(_PROCEDURAL, q):
        return QueryClass.PROCEDURAL
    if len(q.split()) <= 3:
        return QueryClass.AMBIGUOUS
    return QueryClass.FACTOID


# --------------------------------------------------------------------------
# routing policy: which path does each class deserve to pay for?
# --------------------------------------------------------------------------
ROUTES: dict[QueryClass, dict] = {
    QueryClass.IDENTIFIER:  {"path": "hybrid",     "sparse_weight": "mandatory", "rerank": True},
    QueryClass.TABULAR:     {"path": "hybrid",     "sparse_weight": "high",      "rerank": True},
    QueryClass.FACTOID:     {"path": "hybrid",     "sparse_weight": "normal",    "rerank": True},
    QueryClass.PROCEDURAL:  {"path": "hybrid",     "sparse_weight": "normal",    "rerank": True},
    QueryClass.CONDITIONAL: {"path": "multi_hop",  "sparse_weight": "normal",    "rerank": True},
    QueryClass.COMPARATIVE: {"path": "multi_hop",  "sparse_weight": "normal",    "rerank": True},
    QueryClass.MULTI_HOP:   {"path": "multi_hop",  "sparse_weight": "normal",    "rerank": True},
    QueryClass.AMBIGUOUS:   {"path": "multi_query", "sparse_weight": "normal",   "rerank": True},
    QueryClass.UNANSWERABLE: {"path": "refuse",    "sparse_weight": "none",      "rerank": False},
}


def route(query: str) -> dict:
    cls = classify_query(query)
    return {"query_class": cls.value, **ROUTES[cls]}
