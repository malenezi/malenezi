"""The end-to-end grounded pipeline: one call, one auditable trace.

    ask("ما مقدار بدل السكن للمرتبة الحادية عشرة؟")
        -> route -> hybrid retrieve -> rerank -> access re-check
        -> budgeted, edge-ordered context -> grounded generation
        -> citation resolution -> AnswerTrace

Everything the capstone's EVALUATION.md must report is in the returned trace:
query class, path taken, chunk ids retrieved AND cited, refusal, token usage,
and stage latencies. Telemetry is not an add-on here; a RAG system that cannot
tell you which chunk produced which sentence is not auditable, and an
unauditable assistant cannot be put in front of citizens.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field, asdict

from ..config import settings
from ..retrieve.backends import AccessContext, build_backend
from ..retrieve.rerank import two_stage
from .context import assemble_context
from .answer import answer_question, GroundedAnswer


@dataclass
class AnswerTrace:
    question: str
    answer: str
    refused: bool
    citations: list[int] = field(default_factory=list)
    cited_chunk_ids: list[str] = field(default_factory=list)
    cited_doc_ids: list[str] = field(default_factory=list)
    retrieved_chunk_ids: list[str] = field(default_factory=list)
    retrieved_doc_ids: list[str] = field(default_factory=list)
    invented_citations: list[int] = field(default_factory=list)
    query_class: str = ""
    path: str = ""
    latency_ms: dict = field(default_factory=dict)
    context_stats: dict = field(default_factory=dict)
    usage: dict = field(default_factory=dict)
    stub: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


class Dalil:
    def __init__(self, backend=None, chunks=None, *, ctx: AccessContext | None = None,
                 allow_stub: bool = True):
        self.backend = backend or build_backend(chunks)
        self.ctx = ctx or AccessContext(max_tier="restricted")
        self.allow_stub = allow_stub

    def ask(self, question: str, *, ctx: AccessContext | None = None,
            fetch_k: int | None = None, top_k: int | None = None,
            budget: int | None = None, tau: float | None = None) -> AnswerTrace:
        ctx = ctx or self.ctx
        lat = {}

        t0 = time.perf_counter()
        hits, tele = two_stage(self.backend, question, fetch_k=fetch_k, top_k=top_k, ctx=ctx)
        lat["retrieve_ms"] = round((time.perf_counter() - t0) * 1000, 1)

        t0 = time.perf_counter()
        blocks, cstats = assemble_context(hits, budget_tokens=budget, ctx=ctx)
        lat["context_ms"] = round((time.perf_counter() - t0) * 1000, 1)

        t0 = time.perf_counter()
        ans: GroundedAnswer = answer_question(question, blocks, context_stats=cstats,
                                              telemetry=tele, tau=tau,
                                              allow_stub=self.allow_stub)
        lat["generate_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        lat["total_ms"] = round(sum(lat.values()), 1)

        return AnswerTrace(
            question=question, answer=ans.text, refused=ans.refused,
            citations=ans.citations, cited_chunk_ids=ans.cited_chunk_ids,
            cited_doc_ids=ans.cited_doc_ids,
            retrieved_chunk_ids=tele.get("retrieved_chunk_ids", []),
            retrieved_doc_ids=tele.get("retrieved_doc_ids", []),
            invented_citations=ans.invented_citations,
            query_class=tele.get("query_class", ""), path=tele.get("path", ""),
            latency_ms=lat, context_stats=cstats, usage=ans.usage,
            stub=bool(ans.telemetry.get("stub")))
