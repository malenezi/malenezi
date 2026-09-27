"""Corrective RAG: grade the retrieval, retry once, then answer or refuse.

Module 7, Lab 7.

The loop:

    retrieve -> grade evidence -> {sufficient: answer}
                               -> {partial:    rewrite query, retry ONCE}
                               -> {none:       refuse}

Two safeguards without which this pattern is worse than no pattern at all:

  1. AN ITERATION CAP. `settings.corrective_max_retries` defaults to 1. An
     uncapped self-check loop on a hard question retries until the latency and
     cost budget is gone, and then still refuses. Everyone builds this bug once.

  2. A GRADER THAT CAN SAY "NONE". The Module 7 knowledge check asks exactly
     this: a corrective loop given an unanswerable question, whose grader
     always returns "partial", loops to the cap and then answers from
     irrelevant context — converting an honest refusal into a confident
     hallucination. The grader must have a floor, and the loop must refuse when
     it hits the floor.

The offline grader is lexical (query-term coverage in the retrieved text). It
is deterministic, which is a feature: the corrective path's contribution to the
evaluation delta stays measurable instead of drifting with judge temperature.
"""
from __future__ import annotations

from dataclasses import dataclass

from ..arabic import normalise
from ..config import settings
from ..retrieve.backends import AccessContext, Hit
from ..retrieve.hybrid import hybrid_search
from ..retrieve.rerank import rerank
from ..generate.llm import chat_json

GRADE_PROMPT = """You are grading whether retrieved passages contain enough evidence to \
answer the question. Be strict: "partially relevant" means the passages mention the topic \
but do not state the fact asked for.

Return JSON: {{"grade": "sufficient"|"partial"|"none", "missing": "what is absent"}}

Question: {question}

Passages:
{passages}"""

REWRITE_PROMPT = """The first retrieval missed. Rewrite the search query to find what is \
missing. Keep identifiers exact. Return JSON: {{"query": "..."}}

Question: {question}
What was missing: {missing}"""


@dataclass
class Grade:
    grade: str          # sufficient | partial | none
    missing: str = ""
    method: str = "offline"


def grade_retrieval(question: str, hits: list[Hit], *, allow_stub: bool = True) -> Grade:
    if not hits:
        return Grade("none", "no passages retrieved", "trivial")

    data = chat_json([{"role": "user", "content": GRADE_PROMPT.format(
        question=question,
        passages="\n\n".join(f"[{i}] {h.text[:600]}" for i, h in enumerate(hits[:6], 1)))}],
        default=None, allow_stub=allow_stub)
    if isinstance(data, dict) and data.get("grade") in {"sufficient", "partial", "none"}:
        return Grade(data["grade"], str(data.get("missing", "")), "llm")

    # deterministic fallback: content-word coverage
    q = {t for t in normalise(question).split() if len(t) > 3}
    if not q:
        return Grade("partial", "query has no content words", "offline")
    text = normalise(" ".join(h.text for h in hits[:6])).split()
    cover = len(q & set(text)) / len(q)
    if cover >= 0.6:
        return Grade("sufficient", "", "offline")
    if cover >= 0.25:
        return Grade("partial", f"only {cover:.0%} of query terms present", "offline")
    return Grade("none", f"only {cover:.0%} of query terms present", "offline")


def corrective_answer(backend, question: str, *, ctx: AccessContext | None = None,
                      fetch_k: int | None = None, top_k: int | None = None,
                      max_retries: int | None = None) -> tuple[list[Hit], dict]:
    ctx = ctx or AccessContext()
    max_retries = settings.corrective_max_retries if max_retries is None else max_retries

    query = question
    attempts = []
    hits: list[Hit] = []
    for attempt in range(max_retries + 1):
        cands = hybrid_search(backend, query, fetch_k=fetch_k, ctx=ctx)
        hits, _ = rerank(query, cands, top_k=top_k)
        g = grade_retrieval(question, hits)
        attempts.append({"attempt": attempt + 1, "query": query, "grade": g.grade,
                        "missing": g.missing, "grader": g.method,
                         "doc_ids": sorted({h.doc_id for h in hits})})
        if g.grade == "sufficient":
            return hits, {"path": "corrective", "attempts": attempts,
                          "outcome": "answered", "retries_used": attempt,
                          "retrieved_chunk_ids": [h.chunk_id for h in hits],
                          "retrieved_doc_ids": sorted({h.doc_id for h in hits})}
        if g.grade == "none":
            # Refuse now. Retrying on 'none' is how an unanswerable question
            # burns the whole budget and then gets answered from noise.
            return [], {"path": "corrective", "attempts": attempts,
                        "outcome": "refused_no_evidence", "retries_used": attempt,
                        "retrieved_chunk_ids": [], "retrieved_doc_ids": []}
        if attempt < max_retries:
            data = chat_json([{"role": "user", "content": REWRITE_PROMPT.format(
                question=question, missing=g.missing)}], default=None)
            query = (data or {}).get("query") or f"{question} {g.missing}".strip()

    return hits, {"path": "corrective", "attempts": attempts,
                  "outcome": "answered_after_cap", "retries_used": max_retries,
                  "retrieved_chunk_ids": [h.chunk_id for h in hits],
                  "retrieved_doc_ids": sorted({h.doc_id for h in hits})}
