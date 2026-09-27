"""Token-budgeted context assembly with edge ordering and de-duplication.

Module 5, Lab 5.

Three ideas, in order of how much they buy:

1. BUDGET, NOT VOLUME. The context window is a budget you spend, not a bucket
   you fill. Every extra chunk costs input tokens on every single query for the
   life of the system, and dilutes the attention available to the chunk that
   actually holds the answer.

2. EDGE ORDERING. Transformers attend most reliably to the beginning and end of
   a long context ("lost in the middle"). So the best-ranked chunk goes FIRST,
   the second-best goes LAST, and the weaker middle ranks are buried in the
   middle where their being ignored costs least. This is a free accuracy gain:
   same chunks, same tokens, different order.

3. DE-DUPLICATION. Near-duplicate chunks (an Arabic and English edition of the
   same clause, a v1/v2 circular pair) waste budget twice over and make the
   model's citation choice arbitrary. Dedup by normalised-text shingle overlap.

Access control is RE-ASSERTED here even though the retriever already filtered.
Defence in depth: the retriever's filter is one line away from being disabled
by a well-meaning tuning change, and the capstone's "0 cross-department leaks"
gate has to survive that.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..arabic import normalise
from ..config import settings
from ..retrieve.backends import Hit, AccessContext


@dataclass
class ContextBlock:
    marker: int                 # the [n] the model must cite
    chunk_id: str
    doc_id: str
    text: str
    title: str = ""
    section: str = ""
    effective_date: str = ""
    lifecycle: str = ""
    score: float = 0.0
    reranked: bool = False

    def render(self) -> str:
        head = f"[{self.marker}] {self.title or self.doc_id}"
        if self.section:
            head += f" › {self.section}"
        if self.effective_date:
            head += f" (effective {self.effective_date}"
            head += f", {self.lifecycle})" if self.lifecycle else ")"
        return f"{head}\n{self.text}"


def estimate_tokens(text: str) -> int:
    """Deliberately crude and deliberately CONSERVATIVE for Arabic.

    Latin text runs ~4 chars/token; Arabic on most tokenizers runs closer to
    2.2 because of subword splitting on a non-Latin script. Using the Latin
    ratio for a bilingual corpus under-counts Arabic context by ~45% and is how
    teams blow their context window on Arabic queries only. Measure with the
    real tokenizer in production; this estimate is for budgeting."""
    if not text:
        return 0
    arabic = len(re.findall(r"[؀-ۿ]", text))
    ratio = 2.2 if arabic > len(text) * 0.3 else 4.0
    return int(len(text) / ratio) + 1


def _shingles(text: str, n: int = 6) -> set[str]:
    toks = normalise(text).split()
    return {" ".join(toks[i:i + n]) for i in range(max(len(toks) - n + 1, 1))}


def _near_duplicate(a: str, b: str, threshold: float = 0.6) -> bool:
    sa, sb = _shingles(a), _shingles(b)
    if not sa or not sb:
        return False
    return len(sa & sb) / min(len(sa), len(sb)) >= threshold


def edge_order(items: list) -> list:
    """[1st, 3rd, 5th, ..., 6th, 4th, 2nd] — strongest at both ends."""
    head, tail = [], []
    for i, x in enumerate(items):
        (head if i % 2 == 0 else tail).append(x)
    return head + tail[::-1]


def assemble_context(hits: list[Hit], *, budget_tokens: int | None = None,
                     ctx: AccessContext | None = None,
                     dedup: bool = True) -> tuple[list[ContextBlock], dict]:
    budget = budget_tokens or settings.context_token_budget
    ctx = ctx or AccessContext()

    kept: list[Hit] = []
    dropped = {"access": 0, "duplicate": 0, "budget": 0}
    used = 0
    for h in hits:
        if not ctx.allows(h.payload):
            dropped["access"] += 1              # defence in depth — see docstring
            continue
        if dedup and any(_near_duplicate(h.text, k.text) for k in kept):
            dropped["duplicate"] += 1
            continue
        cost = estimate_tokens(h.text)
        if used + cost > budget:
            dropped["budget"] += 1
            continue
        kept.append(h)
        used += cost

    ordered = edge_order(kept)
    blocks = []
    for i, h in enumerate(ordered, start=1):
        p = h.payload
        blocks.append(ContextBlock(
            marker=i, chunk_id=h.chunk_id, doc_id=h.doc_id, text=h.text,
            title=p.get("title", p.get("title_en", h.doc_id)),
            section=p.get("section_title", ""),
            effective_date=p.get("effective_date", ""),
            lifecycle=p.get("lifecycle", ""), score=h.score,
            reranked=bool(p.get("reranked"))))
    stats = {"blocks": len(blocks), "tokens_estimated": used, "budget": budget,
             "dropped": dropped,
             "rank_order": [b.chunk_id for b in blocks]}
    return blocks, stats


def render_context(blocks: list[ContextBlock]) -> str:
    return "\n\n".join(b.render() for b in blocks)
