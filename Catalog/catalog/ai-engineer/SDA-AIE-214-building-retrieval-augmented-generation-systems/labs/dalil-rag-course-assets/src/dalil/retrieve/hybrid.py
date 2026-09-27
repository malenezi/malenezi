"""Dense + sparse, fused with Reciprocal Rank Fusion. Module 4, Lab 4.

Why RRF and not a weighted sum of scores: cosine similarity lives in [-1, 1]
and BM25 scores are unbounded and corpus-dependent. Normalising them onto a
common scale requires per-corpus tuning that silently rots the day the corpus
grows. RRF throws the scores away and fuses RANKS:

        score(d) = Σ over rankers  1 / (k + rank_r(d))

with k=60 by convention. It has no tunable per-corpus parameter, it is stable,
and it degrades gracefully when one leg returns nothing — which matters here,
because the sparse leg is legitimately empty for a purely conceptual Arabic
question and the dense leg is legitimately weak for "Circular 44/2025".
"""
from __future__ import annotations

from collections import defaultdict

from ..config import settings
from .backends import Backend, Hit, AccessContext


def rrf_fuse(rankings: list[list[Hit]], k: int | None = None,
             weights: list[float] | None = None) -> list[Hit]:
    k = k or settings.rrf_k
    weights = weights or [1.0] * len(rankings)
    scores: dict[str, float] = defaultdict(float)
    best: dict[str, Hit] = {}
    for w, ranking in zip(weights, rankings):
        for rank, hit in enumerate(ranking, start=1):
            scores[hit.chunk_id] += w / (k + rank)
            if hit.chunk_id not in best:
                best[hit.chunk_id] = hit
    out = []
    for cid, s in sorted(scores.items(), key=lambda kv: -kv[1]):
        h = best[cid]
        out.append(Hit(h.chunk_id, h.doc_id, h.text, s, h.payload))
    return out


def hybrid_search(backend: Backend, query: str, *, fetch_k: int | None = None,
                  ctx: AccessContext | None = None,
                  sparse_weight: float = 1.0, dense_weight: float = 1.0) -> list[Hit]:
    """Stage 1 of the two-stage budget: fetch wide and cheap.

    fetch_k is deliberately generous (40 by default). Retrieval is milliseconds
    and fractions of a halala; generation tokens are the expensive part. Being
    stingy here to 'save cost' saves nothing and costs recall.
    """
    fetch_k = fetch_k or settings.fetch_k
    ctx = ctx or AccessContext()
    dense = backend.search_dense(query, fetch_k, ctx)
    sparse = backend.search_sparse(query, fetch_k, ctx)
    rankings, weights = [], []
    if dense:
        rankings.append(dense)
        weights.append(dense_weight)
    if sparse:
        rankings.append(sparse)
        weights.append(sparse_weight)
    if not rankings:
        return []
    return rrf_fuse(rankings, weights=weights)[:fetch_k]
