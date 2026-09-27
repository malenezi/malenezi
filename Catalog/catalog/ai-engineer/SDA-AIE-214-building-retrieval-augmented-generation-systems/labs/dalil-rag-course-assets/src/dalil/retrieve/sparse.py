"""BM25 in ~90 lines of standard library.

Why a hand-rolled BM25 in a course that also uses Qdrant's sparse vectors:

  * Module 4's thesis is that dense retrieval blurs exact tokens and lexical
    retrieval does not. A participant who has read this file understands *why*
    "Circular 44/2025" scores where it does; a participant who called a library
    has only been told.
  * It makes the whole retrieval stack runnable with no server and no model
    download — the evaluation harness, the practical-assessment kits and the
    unit tests all run on a plane. That is not a convenience, it is what keeps
    a 20-hour course from losing an hour to infrastructure.

Tokenisation runs through dalil.arabic.normalise, so Arabic-Indic digits,
presentation forms and alef variants are folded before term counting. That one
line is why "التعميم ٤٤/٢٠٢٥" and "circular 44/2025" hit the same postings.
"""
from __future__ import annotations

import math
import re
from collections import Counter, defaultdict

from ..arabic import normalise, normalise_identifier

_TOKEN = re.compile(r"[0-9]+(?:/[0-9]+)*|[a-z]+|[ء-ي]+")


def tokenize(text: str) -> list[str]:
    t = normalise_identifier(text)
    return _TOKEN.findall(t)


class BM25:
    """Okapi BM25 with the standard k1=1.5, b=0.75."""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1, self.b = k1, b
        self.doc_ids: list[str] = []
        self.doc_len: list[int] = []
        self.tf: list[Counter] = []
        self.df: Counter = Counter()
        self.postings: dict[str, list[int]] = defaultdict(list)
        self.avgdl: float = 0.0

    def add(self, doc_id: str, text: str) -> None:
        toks = tokenize(text)
        tf = Counter(toks)
        i = len(self.doc_ids)
        self.doc_ids.append(doc_id)
        self.doc_len.append(len(toks))
        self.tf.append(tf)
        for term in tf:
            self.df[term] += 1
            self.postings[term].append(i)

    def finalise(self) -> "BM25":
        self.avgdl = (sum(self.doc_len) / len(self.doc_len)) if self.doc_len else 0.0
        return self

    def idf(self, term: str) -> float:
        n = len(self.doc_ids)
        df = self.df.get(term, 0)
        return math.log(1 + (n - df + 0.5) / (df + 0.5))

    def search(self, query: str, k: int = 10) -> list[tuple[str, float]]:
        q = tokenize(query)
        scores: dict[int, float] = defaultdict(float)
        for term in q:
            if term not in self.postings:
                continue
            idf = self.idf(term)
            for i in self.postings[term]:
                f = self.tf[i][term]
                dl = self.doc_len[i] or 1
                denom = f + self.k1 * (1 - self.b + self.b * dl / (self.avgdl or 1))
                scores[i] += idf * (f * (self.k1 + 1)) / (denom or 1)
        ranked = sorted(scores.items(), key=lambda kv: -kv[1])[:k]
        return [(self.doc_ids[i], s) for i, s in ranked]
