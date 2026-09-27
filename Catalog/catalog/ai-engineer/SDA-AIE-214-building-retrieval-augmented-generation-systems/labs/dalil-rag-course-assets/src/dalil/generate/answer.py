"""Grounded, cited, refusal-capable generation. Module 5, Lab 5.

The prompt below is the course's most-copied artefact, so it is worth saying
exactly what each constraint is defending against:

  "ONLY the context"        -> ungrounded fluency (RAGAS faithfulness)
  "cite [n] after each claim"-> unverifiable answers (audit requirement)
  "if insufficient, say so" -> F7: the confident answer to a question the
                               corpus cannot answer
  "prefer the most recent"  -> F8: quoting a superseded circular
  "answer in the language
   of the question"         -> an Arabic question answered in English is a
                               failure even when it is factually correct

Then the code does the part a prompt cannot: it RESOLVES every citation the
model emitted against the context blocks it was actually given. A citation that
does not resolve is not a formatting problem, it is a fabricated source, and
the pipeline reports it as `invented_citations`. The capstone requires zero.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..config import settings
from .context import ContextBlock, render_context
from .llm import chat, LLMResponse

SYSTEM_PROMPT = """You are Dalil (دليل), the knowledge assistant of a Saudi public-sector \
organisation. You answer strictly from the numbered context passages supplied to you.

Rules you must follow without exception:
1. Use ONLY the information in the context. You have no other knowledge. Do not \
infer, complete, or generalise beyond what the passages state.
2. Support every factual claim with a citation marker of the form [n] naming the \
passage it came from. A sentence with no citation is not allowed.
3. If the context does not contain enough information to answer, reply exactly: \
"I don't have enough information in the provided documents to answer this." \
(In Arabic: "لا تتوفر لدي معلومات كافية في الوثائق المتاحة للإجابة على هذا السؤال.") \
Do not guess, and do not offer a partial answer dressed as a complete one.
4. When passages disagree, prefer the one with the later effective date, say \
explicitly that an earlier version was superseded, and cite both.
5. Answer in the language of the question: Arabic question, Arabic answer.
6. Be concise. Quote figures, dates and identifiers exactly as they appear."""

USER_TEMPLATE = """Context passages:
{context}

Question: {question}

Answer using only the passages above, citing each claim as [n]."""

REFUSAL_MARKERS = [
    "don't have enough information", "do not have enough information",
    "لا تتوفر لدي معلومات كافية", "insufficient information in the provided",
]


@dataclass
class GroundedAnswer:
    question: str
    text: str
    citations: list[int] = field(default_factory=list)
    cited_chunk_ids: list[str] = field(default_factory=list)
    cited_doc_ids: list[str] = field(default_factory=list)
    invented_citations: list[int] = field(default_factory=list)
    refused: bool = False
    uncited_sentences: int = 0
    context_stats: dict = field(default_factory=dict)
    telemetry: dict = field(default_factory=dict)
    usage: dict = field(default_factory=dict)

    @property
    def fully_cited(self) -> bool:
        return self.refused or (self.uncited_sentences == 0 and not self.invented_citations)


_SENT = re.compile(r"[^.!?؟\n]+[.!?؟]?")
_CITE = re.compile(r"\[(\d+)\]")


def _looks_like_refusal(text: str) -> bool:
    low = text.lower()
    return any(m.lower() in low for m in REFUSAL_MARKERS)


def verify_citations(text: str, blocks: list[ContextBlock]) -> dict:
    """Resolve emitted [n] markers against the blocks actually supplied.

    This is the difference between a system that *looks* cited and one an
    auditor can follow: an answer citing [7] when only six passages were given
    has invented a source, and no amount of eloquence redeems it.
    """
    by_marker = {b.marker: b for b in blocks}
    emitted = [int(m) for m in _CITE.findall(text)]
    valid = [n for n in emitted if n in by_marker]
    invented = sorted({n for n in emitted if n not in by_marker})

    uncited = 0
    for s in _SENT.findall(text):
        s = s.strip()
        if len(s.split()) < 4:
            continue
        if not _CITE.search(s):
            uncited += 1

    return {
        "citations": sorted(set(valid)),
        "cited_chunk_ids": [by_marker[n].chunk_id for n in sorted(set(valid))],
        "cited_doc_ids": sorted({by_marker[n].doc_id for n in set(valid)}),
        "invented_citations": invented,
        "uncited_sentences": uncited,
    }


def evidence_strength(blocks: list[ContextBlock]) -> float:
    """Cheap pre-generation refusal signal: the top block's score.

    Refusing BEFORE calling the model saves the token spend on questions the
    corpus provably cannot answer, and it makes refusal a property of retrieval
    (measurable, tunable, τ in config) rather than a mood of the model.
    Scores are only comparable within one retriever configuration — which is
    why τ must be re-tuned whenever the retrieval stack changes, and why
    DECISIONS.md must record the value you chose and why.
    """
    if not blocks:
        return 0.0
    top = max(b.score for b in blocks)
    if any(b.reranked for b in blocks):
        # A cross-encoder score is already a calibrated relevance value in
        # [0, 1]; threshold it directly.
        return float(max(0.0, min(top, 1.0)))
    # Without a reranker the top score is an RRF sum (~1/(k+rank) per leg),
    # which is tiny and NOT a probability. Rescale against the theoretical RRF
    # maximum so that tau keeps its meaning. This is precisely why DECISIONS.md
    # must record which retrieval stack tau was tuned against: change the stack,
    # re-tune the threshold.
    rrf_max = 2.0 / (settings.rrf_k + 1)
    return float(min(top / rrf_max, 1.0))


def answer_question(question: str, blocks: list[ContextBlock], *,
                    context_stats: dict | None = None, telemetry: dict | None = None,
                    tau: float | None = None, model: str | None = None,
                    allow_stub: bool = True) -> GroundedAnswer:
    tau = settings.refusal_threshold if tau is None else tau

    if not blocks or evidence_strength(blocks) < tau:
        msg = ("لا تتوفر لدي معلومات كافية في الوثائق المتاحة للإجابة على هذا السؤال."
               if _is_arabic(question) else
               "I don't have enough information in the provided documents to answer this.")
        return GroundedAnswer(question, msg, refused=True,
                              context_stats=context_stats or {},
                              telemetry={**(telemetry or {}), "refused_before_generation": True})

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_TEMPLATE.format(
            context=render_context(blocks), question=question)},
    ]
    resp: LLMResponse = chat(messages, model=model, temperature=settings.temperature,
                             allow_stub=allow_stub)
    v = verify_citations(resp.text, blocks)
    return GroundedAnswer(
        question=question, text=resp.text, refused=_looks_like_refusal(resp.text),
        context_stats=context_stats or {},
        telemetry={**(telemetry or {}), "stub": resp.stub, "model": resp.model},
        usage={"prompt_tokens": resp.prompt_tokens,
               "completion_tokens": resp.completion_tokens},
        **v)


def _is_arabic(text: str) -> bool:
    from ..arabic import has_arabic
    return has_arabic(text)
