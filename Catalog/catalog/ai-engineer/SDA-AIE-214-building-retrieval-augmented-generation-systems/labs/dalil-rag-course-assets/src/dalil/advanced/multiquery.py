"""Multi-query expansion with RRF fusion. Module 7, Lab 7.

The failure it addresses: an under-specified question ("remote work rules?")
produces one embedding, which lands in one neighbourhood, which surfaces one
document family. Three paraphrases produce three neighbourhoods and their union
covers what the user meant.

What it does NOT address, and participants must measure rather than assume:
  * identifier queries — three paraphrases of "Circular 44/2025" are still
    three dense queries that blur the same token. Sparse retrieval fixes this,
    not expansion. Running expansion here is pure cost.
  * multi-hop questions — expansion widens ONE hop; it cannot compose two
    documents. That is multihop.py.

The router sends only AMBIGUOUS-class queries down this path, which is why the
measured cost of Lab 7 stays flat on the single-hop subset. An expansion
applied to every query is the classic "loops everywhere" anti-pattern.

Deterministic fallback: when no LLM is reachable, `expand_queries` returns
rule-based variants (bilingual mirror + a keyword-stripped form). They are
weaker than model paraphrases but they keep the lab runnable and the ablation
honest — the report records which generator produced them.
"""
from __future__ import annotations

from ..arabic import has_arabic, normalise
from ..config import settings
from ..retrieve.backends import AccessContext, Hit
from ..retrieve.hybrid import hybrid_search
from ..retrieve.rerank import rerank
from ..generate.llm import chat_json

EXPANSION_PROMPT = """Rewrite the user's question as {n} alternative search queries that \
would retrieve the same answer from a corpus of Saudi data-protection and AI regulations \
and an organisation's internal HR/IT policies.

Rules:
- Keep every identifier, number and date exactly as written.
- Vary vocabulary and specificity, not meaning.
- If the question is Arabic, include at least one English query, and vice versa \
(the corpus is bilingual and the answer may live in either language).
- Return JSON: {{"queries": ["...", "..."]}}

Question: {question}"""


def _rule_based_variants(question: str) -> list[str]:
    q = normalise(question)
    variants = [q]
    stripped = " ".join(w for w in q.split()
                        if w not in {"what", "is", "the", "of", "a", "for", "ما", "هي", "هو", "في"})
    if stripped and stripped != q:
        variants.append(stripped)
    variants.append(f"policy procedure {stripped}" if not has_arabic(q)
                    else f"سياسة إجراءات {stripped}")
    return list(dict.fromkeys(variants))


def expand_queries(question: str, n: int = 3, *, allow_stub: bool = True) -> tuple[list[str], str]:
    """Returns (queries, generator) where generator is 'llm' or 'rule-based'."""
    data = chat_json([{"role": "user",
                       "content": EXPANSION_PROMPT.format(n=n, question=question)}],
                     default=None, allow_stub=allow_stub)
    if isinstance(data, dict) and isinstance(data.get("queries"), list) and data["queries"]:
        qs = [question] + [str(q) for q in data["queries"]][:n]
        return list(dict.fromkeys(qs)), "llm"
    return _rule_based_variants(question)[: n + 1], "rule-based"


def multiquery_search(backend, question: str, *, n: int = 3,
                      fetch_k: int | None = None, top_k: int | None = None,
                      ctx: AccessContext | None = None) -> tuple[list[Hit], dict]:
    ctx = ctx or AccessContext()
    queries, generator = expand_queries(question, n=n)
    rankings = [hybrid_search(backend, q, fetch_k=fetch_k, ctx=ctx) for q in queries]
    from ..retrieve.hybrid import rrf_fuse
    fused = rrf_fuse([r for r in rankings if r])
    hits, did_rerank = rerank(question, fused[: (fetch_k or settings.fetch_k)], top_k=top_k)
    return hits, {"path": "multi_query", "queries": queries,
                  "expansion_generator": generator, "reranked": did_rerank,
                  "retrieved_chunk_ids": [h.chunk_id for h in hits],
                  "retrieved_doc_ids": sorted({h.doc_id for h in hits})}
