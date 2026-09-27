"""Question decomposition and multi-hop retrieval. Module 7, Lab 7.

The class of question a linear pipeline structurally cannot answer:

    "Our internal procedure requires a transfer risk assessment before exporting
     personal data — which SDAIA instrument imposes that, and what does it
     require the assessment to cover?"

No single chunk contains both halves. One retrieval pass returns chunks about
one half and the model either answers half the question confidently or
hallucinates the bridge. Two passes, composed, answer it.

Design decisions worth defending in DECISIONS.md:

  * HOPS ARE CAPPED (settings.max_hops, default 2). Uncapped hopping is how a
    "smart" pipeline spends 40 seconds and SAR 3 on a question it will refuse.
  * SUB-QUESTIONS ARE DEDUPED. The most common Lab 7 bug is a decomposer that
    emits two paraphrases of the same sub-question, doubling cost for identical
    evidence. `decompose` drops near-duplicates before any retrieval happens.
  * HOP 2 IS CONDITIONED ON HOP 1. Retrieving both sub-questions independently
    and concatenating is not multi-hop, it is multi-query with extra steps.
    Hop 2's query is rewritten using what hop 1 found.
  * EVIDENCE FROM ALL HOPS IS KEPT AND LABELLED, so the final answer can cite
    both documents — which is the point of asking the question at all.
"""
from __future__ import annotations

from ..arabic import normalise
from ..config import settings
from ..retrieve.backends import AccessContext, Hit
from ..retrieve.hybrid import hybrid_search
from ..retrieve.rerank import rerank
from ..generate.llm import chat_json

DECOMPOSE_PROMPT = """Break the question into the minimum number of independent \
sub-questions needed to answer it (1 if it needs only one document, 2 if it genuinely \
requires composing two). Do not invent sub-questions: if one document answers it, \
return one.

Return JSON: {{"sub_questions": ["...", "..."], "needs_composition": true|false}}

Question: {question}"""

BRIDGE_PROMPT = """Given what we found for the first sub-question, write the search \
query for the second sub-question, substituting anything the first answer identified.

First sub-question: {q1}
What we found: {found}
Second sub-question: {q2}

Return JSON: {{"query": "..."}}"""


_PUNCT_STRIP = "?؟.,;:!()[]{}\"'،؛"


def _tokset(text: str) -> set[str]:
    return {t.strip(_PUNCT_STRIP) for t in normalise(text).lower().split()} - {""}


def _overlap(a: str, b: str) -> float:
    ta, tb = _tokset(a), _tokset(b)
    return len(ta & tb) / max(min(len(ta), len(tb)), 1)


def decompose(question: str, *, allow_stub: bool = True) -> tuple[list[str], str]:
    data = chat_json([{"role": "user",
                       "content": DECOMPOSE_PROMPT.format(question=question)}],
                     default=None, allow_stub=allow_stub)
    subs: list[str] = []
    if isinstance(data, dict) and isinstance(data.get("sub_questions"), list):
        subs = [str(s).strip() for s in data["sub_questions"] if str(s).strip()]
    if not subs:
        # rule-based fallback: split on the coordinating conjunction that most
        # reliably marks a two-part regulatory question
        for sep in (" and what ", " and which ", "، وما ", " وما هي ", "; "):
            if sep in question:
                left, right = question.split(sep, 1)
                subs = [left.strip(" ?؟"), right.strip(" ?؟")]
                break
        if not subs:
            subs = [question]
    # dedupe near-identical sub-questions -- the twin-sub-question bug
    kept: list[str] = []
    for s in subs:
        if not any(_overlap(s, k) > 0.8 for k in kept):
            kept.append(s)
    return kept[: settings.max_hops], ("llm" if isinstance(data, dict) else "rule-based")


def multihop_answer(backend, question: str, *, ctx: AccessContext | None = None,
                    fetch_k: int | None = None, top_k: int | None = None
                    ) -> tuple[list[Hit], dict]:
    ctx = ctx or AccessContext()
    subs, generator = decompose(question)
    hops: list[dict] = []
    all_hits: list[Hit] = []
    found_summary = ""

    for i, sub in enumerate(subs, start=1):
        query = sub
        if i > 1 and found_summary:
            data = chat_json([{"role": "user", "content": BRIDGE_PROMPT.format(
                q1=subs[0], found=found_summary[:600], q2=sub)}], default=None)
            if isinstance(data, dict) and data.get("query"):
                query = str(data["query"])
        cands = hybrid_search(backend, query, fetch_k=fetch_k, ctx=ctx)
        hits, _ = rerank(query, cands, top_k=top_k or 4)
        for h in hits:
            h.payload["hop"] = i
        all_hits.extend(hits)
        found_summary = " ".join(h.text[:300] for h in hits[:2])
        hops.append({"hop": i, "sub_question": sub, "query": query,
                     "doc_ids": sorted({h.doc_id for h in hits}),
                     "chunk_ids": [h.chunk_id for h in hits]})

    seen, deduped = set(), []
    for h in all_hits:
        if h.chunk_id in seen:
            continue
        seen.add(h.chunk_id)
        deduped.append(h)

    return deduped, {
        "path": "multi_hop", "sub_questions": subs, "decomposer": generator,
        "hops": hops, "hop_count": len(subs),
        "retrieved_chunk_ids": [h.chunk_id for h in deduped],
        "retrieved_doc_ids": sorted({h.doc_id for h in deduped}),
        "documents_composed": len({h.doc_id for h in deduped}),
    }
