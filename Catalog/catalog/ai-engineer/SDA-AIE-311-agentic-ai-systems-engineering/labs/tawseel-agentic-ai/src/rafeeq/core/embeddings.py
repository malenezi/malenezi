"""Module 4 — embeddings for Rafeeq's long-term memory and knowledge base.

`get_embeddings()` returns real multilingual embeddings when
`RAFEEQ_EMBED_MODE=live` (lazy-imported so Layer A never needs the
third-party model to import this module), otherwise a deterministic,
dependency-free `HashingEmbeddings` — this is what makes Lab 4 (memory,
vector search, cross-lingual recall) runnable offline with no Qdrant, no
model download, and no network call at import time.

`HashingEmbeddings` is genuinely cross-lingual-*ish*, not just a bag of
random hashed n-grams: on top of generic character-n-gram feature hashing
it also indexes a small AR<->EN term map for Tawseel's domain vocabulary
(order/طلب, refund/استرداد, delivery/توصيل, ...). Whichever language a term
appears in, the SAME canonical hash contribution is added, so an Arabic
query about "استرداد" (refund) and an English query about "refund" land
close together in vector space for that concept — exactly the property
Module 4's cross-lingual recall exercise needs, without training or
downloading a multilingual model.

Both this class and the real embedding model expose the same minimal
surface used across the codebase: `embed_query(text) -> list[float]` and
`embed_documents(texts) -> list[list[float]]` (the LangChain `Embeddings`
convention), so `rafeeq.memory.vector_store` and the (Layer-B) long-term
memory module can swap one for the other without changing call sites.
"""
from __future__ import annotations

import hashlib
import math
import re
from typing import Iterable

from rafeeq.core.config import get_settings

DIMS = 256

# Canonical domain term -> every surface form (English + Arabic + common
# variants/spellings) that should hash to the SAME contribution. This is
# the cross-lingual bridge: generic character n-grams cannot align Latin
# and Arabic script, so we special-case the vocabulary Rafeeq actually
# needs (order status, refunds, delivery, policy terms).
AR_EN_TERM_MAP: dict[str, list[str]] = {
    "order": ["order", "orders", "طلب", "طلبي", "الطلب", "طلبات"],
    "refund": ["refund", "refunded", "reimburse", "استرداد", "استرجاع", "استرد", "ارجاع"],
    "delivery": ["delivery", "deliver", "shipment", "توصيل", "شحنة", "التوصيل"],
    "late": ["late", "delayed", "overdue", "متأخر", "تأخر", "تأخير"],
    "invoice": ["invoice", "receipt", "bill", "فاتورة", "الفاتورة", "ايصال", "إيصال"],
    "track": ["track", "tracking", "status", "تتبع", "تتبع الطلب", "حالة الطلب"],
    "reschedule": ["reschedule", "postpone", "تأجيل", "تغيير الموعد", "أجل"],
    "damaged": ["damaged", "broken", "تالف", "معطوب", "مكسور"],
    "lost": ["lost", "missing", "مفقود", "ضاع", "ضائع"],
    "cancel": ["cancel", "cancelled", "إلغاء", "الغاء", "ملغي"],
    "payment": ["payment", "paid", "دفع", "الدفع", "مدفوع"],
    "customer": ["customer", "client", "عميل", "العميل", "زبون"],
    "policy": ["policy", "policies", "سياسة", "السياسة"],
    "complaint": ["complaint", "issue", "problem", "شكوى", "مشكلة"],
    "escalate": ["escalate", "escalation", "تصعيد"],
    "fraud": ["fraud", "احتيال", "تزوير"],
    "driver": ["driver", "courier", "سائق", "مندوب"],
    "eta": ["eta", "arrival", "موعد الوصول", "الوصول"],
    "address": ["address", "عنوان", "العنوان"],
}

# surface form (lowercased for latin script; raw for Arabic) -> canonical key
_SURFACE_TO_CANONICAL: dict[str, str] = {}
for _canon, _forms in AR_EN_TERM_MAP.items():
    for _form in _forms:
        _SURFACE_TO_CANONICAL[_form.lower() if _form.isascii() else _form] = _canon

_WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


def _stable_hash_index(token: str, salt: str = "") -> tuple[int, float]:
    """Deterministic (index, sign) pair for the hashing trick. Uses sha256
    rather than Python's builtin `hash()` because `hash()` is randomised
    per-process (PYTHONHASHSEED) — this MUST be stable across runs and
    processes for embeddings to be comparable at all."""
    digest = hashlib.sha256(f"{salt}:{token}".encode("utf-8")).digest()
    idx = int.from_bytes(digest[:4], "big") % DIMS
    sign = 1.0 if digest[4] % 2 == 0 else -1.0
    return idx, sign


def _char_ngrams(text: str, n: int = 3) -> Iterable[str]:
    padded = f"  {text}  "
    for i in range(len(padded) - n + 1):
        gram = padded[i : i + n]
        if gram.strip():
            yield gram


def _l2_normalise(vec: list[float]) -> list[float]:
    norm = math.sqrt(sum(v * v for v in vec))
    if norm == 0.0:
        return vec
    return [v / norm for v in vec]


class HashingEmbeddings:
    """Deterministic, dependency-free embeddings: character-3-gram feature
    hashing into `DIMS` (256) dimensions, L2-normalised, plus a domain
    AR<->EN term bridge (see module docstring). No model, no network, no
    randomness — the same text always produces the same vector, which is
    what makes offline tests and Lab 4's cross-lingual recall reproducible.

    Call surface matches the LangChain `Embeddings` convention so it is a
    drop-in for `QdrantVectorStore(embedding=...)` and for
    `rafeeq.memory.vector_store.SimpleVectorStore`.
    """

    dims = DIMS

    def __init__(self, dims: int = DIMS, ngram: int = 3, term_weight: float = 3.0) -> None:
        self.dims = dims
        self.ngram = ngram
        self.term_weight = term_weight

    def embed_query(self, text: str) -> list[float]:
        return self._embed_one(text or "")

    def embed_documents(self, texts: Iterable[str]) -> list[list[float]]:
        return [self._embed_one(t or "") for t in texts]

    # LangChain Embeddings compatibility alias some call sites use.
    def __call__(self, text: str) -> list[float]:
        return self.embed_query(text)

    def _embed_one(self, text: str) -> list[float]:
        vec = [0.0] * self.dims

        # 1. generic character-n-gram hashing — captures surface similarity
        #    within a language/script.
        for gram in _char_ngrams(text, self.ngram):
            idx, sign = _stable_hash_index(gram, salt="ngram")
            vec[idx] += sign

        # 2. domain term bridge — the cross-lingual part. Every recognised
        #    surface form (in either language) contributes to the SAME
        #    canonical-key hash, several times over for robustness, so the
        #    concept dominates the n-gram noise for short queries.
        for word in _WORD_RE.findall(text):
            key = word.lower() if word.isascii() else word
            canonical = _SURFACE_TO_CANONICAL.get(key)
            if canonical is None:
                continue
            for rep in range(4):  # spread the concept over a few dims
                idx, sign = _stable_hash_index(canonical, salt=f"term{rep}")
                vec[idx] += sign * self.term_weight

        return _l2_normalise(vec)


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Cosine similarity for two vectors of equal length. Vectors from
    `HashingEmbeddings` are already L2-normalised, so this reduces to a dot
    product, but we compute it properly so it also works for un-normalised
    (e.g. live-model) vectors."""
    if not a or not b:
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)


_MISSING_LIVE_EMBED_HINT = (
    "RAFEEQ_EMBED_MODE=live requires a real multilingual embedding model "
    "(e.g. `sentence-transformers` with a multilingual checkpoint, or an API "
    "embedding client) which is not installed in this environment. Install it, "
    "or use the default offline HashingEmbeddings (unset RAFEEQ_EMBED_MODE, or "
    "set it to anything other than 'live')."
)


def _live_embeddings() -> object:
    """Lazy import so Layer A never needs the real embedding dependency to
    import this module (SPEC §1 import-guard rule)."""
    try:
        from sentence_transformers import SentenceTransformer  # type: ignore[import-not-found]
    except ImportError as exc:  # pragma: no cover - not installed in this sandbox
        raise ImportError(_MISSING_LIVE_EMBED_HINT) from exc

    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

    class _SentenceTransformerEmbeddings:
        def embed_query(self, text: str) -> list[float]:
            return model.encode(text).tolist()

        def embed_documents(self, texts: Iterable[str]) -> list[list[float]]:
            return [v.tolist() for v in model.encode(list(texts))]

    return _SentenceTransformerEmbeddings()


def get_embeddings() -> object:
    """Return an embeddings object with `embed_query`/`embed_documents`.
    Real multilingual embeddings when `RAFEEQ_EMBED_MODE=live`, otherwise
    the deterministic, offline `HashingEmbeddings` (the default — this is
    what makes Lab 4 runnable without Qdrant or a model download)."""
    settings = get_settings()
    if settings.embed_mode == "live":
        return _live_embeddings()
    return HashingEmbeddings()
