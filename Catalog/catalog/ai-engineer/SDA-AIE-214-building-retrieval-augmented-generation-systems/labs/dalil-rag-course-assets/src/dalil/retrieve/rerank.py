"""Cross-encoder reranking — stage 2 of the two-stage budget. Module 4, Lab 4.

A bi-encoder (the embedding model) encodes query and document SEPARATELY, so
document vectors can be precomputed and searched in milliseconds — and so the
model never sees the two texts together. A cross-encoder reads the pair jointly
and scores relevance directly. It is far more accurate and cannot be
precomputed, which is the whole reason for fetch-40-keep-6: pay the cheap stage
for recall, pay the expensive stage on 40 candidates only, and send 6 to the
LLM.

If the reranker is unavailable, this module returns the input order UNCHANGED
and sets `reranked=False` on every hit. It never pretends. A silent no-op
reranker is how a team ships a "two-stage retriever" that is really one stage.
"""
from __future__ import annotations

from ..config import settings
from .backends import Hit

_RERANKER = None


def get_reranker(model_name: str | None = None):
    global _RERANKER
    if _RERANKER is not None:
        return _RERANKER
    name = model_name or settings.reranker_model
    try:
        from FlagEmbedding import FlagReranker
        _RERANKER = ("flag", FlagReranker(name, use_fp16=True))
    except Exception:
        try:
            from sentence_transformers import CrossEncoder
            _RERANKER = ("ce", CrossEncoder(name))
        except Exception:
            _RERANKER = ("none", None)
    return _RERANKER


def rerank(query: str, hits: list[Hit], *, top_k: int | None = None,
           model_name: str | None = None) -> tuple[list[Hit], bool]:
    """Returns (hits, reranked_flag). Truncates to top_k either way."""
    top_k = top_k or settings.top_k
    if not hits:
        return [], False
    kind, model = get_reranker(model_name)
    if kind == "none" or model is None:
        for h in hits:
            h.payload["reranked"] = False
        return hits[:top_k], False

    pairs = [(query, h.text) for h in hits]
    scores = (model.compute_score(pairs, normalize=True) if kind == "flag"
              else model.predict(pairs))
    if not isinstance(scores, (list, tuple)):
        scores = [scores]
    scored = sorted(zip(hits, scores), key=lambda hs: -float(hs[1]))
    out = []
    for h, s in scored[:top_k]:
        h.payload["reranked"] = True
        h.payload["rerank_score"] = float(s)
        out.append(Hit(h.chunk_id, h.doc_id, h.text, float(s), h.payload))
    return out, True


def two_stage(backend, query: str, *, fetch_k: int | None = None,
              top_k: int | None = None, ctx=None) -> tuple[list[Hit], dict]:
    """The full Module 4 retriever with its own telemetry.

    The telemetry dict is not decoration: `EVALUATION.md` in the capstone must
    report fetch_k, top_k and whether reranking actually ran, and PA-1 asks
    participants to diagnose a retriever from exactly these fields.
    """
    from .hybrid import hybrid_search
    from .backends import AccessContext
    from .router import route

    ctx = ctx or AccessContext()
    plan = route(query)
    sw = {"mandatory": 2.0, "high": 1.5, "normal": 1.0, "none": 0.0}[plan["sparse_weight"]]
    candidates = hybrid_search(backend, query, fetch_k=fetch_k, ctx=ctx, sparse_weight=sw)
    hits, did_rerank = rerank(query, candidates, top_k=top_k) if plan["rerank"] \
        else (candidates[:top_k or settings.top_k], False)
    telemetry = {
        "query_class": plan["query_class"], "path": plan["path"],
        "fetch_k": fetch_k or settings.fetch_k, "top_k": top_k or settings.top_k,
        "candidates": len(candidates), "reranked": did_rerank,
        "sparse_weight": sw,
        "retrieved_chunk_ids": [h.chunk_id for h in hits],
        "retrieved_doc_ids": sorted({h.doc_id for h in hits}),
    }
    return hits, telemetry
