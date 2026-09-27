"""Module 4 — a dependency-free vector store for offline memory/KB labs.

`SimpleVectorStore` is an in-memory, cosine-similarity store over
`rafeeq.core.embeddings.HashingEmbeddings` (or any embedding object with
`embed_query`/`embed_documents`). It mirrors the call surface the
instructor package uses against `QdrantVectorStore` — `add_documents`,
`similarity_search`, `similarity_search_with_score`, `delete` — so
`rafeeq.memory.long_term` and `rafeeq.memory.knowledge_base` (Layer B,
owned elsewhere in this repo) can be pointed at either store without
changing call sites. `get_store(collection)` is the single switch: Qdrant
when `RAFEEQ_VECTOR_MODE=qdrant`, this store otherwise — which is what
makes Lab 4 (memory, retrieval, cross-lingual recall, PDPL erasure)
runnable with no Qdrant instance, no network, no keys.

TEACHING POINT — metadata filter-before-rank is a PDPL control, not an
optimisation (Module 4 §3-4): every `similarity_search` here applies
`filter` to the candidate set BEFORE computing cosine similarity, never
after. Ranking-then-filtering can silently return zero results for a
narrow filter after truncating to top-k, or — worse, in a real system —
create a window where a slow filter step lets an over-broad top-k leak
through before it's trimmed. Filtering first makes "only this customer's
memories, only the current policy version" a structural guarantee, not a
hope. This is also why `delete(filter=...)` exists: PDPL erasure
(`forget_customer`) must be a real removal, not a rank-time exclusion.
"""
from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Any, Iterable

from rafeeq.core.config import get_settings
from rafeeq.core.embeddings import cosine_similarity, get_embeddings


@dataclass
class Document:
    """Drop-in shape for `langchain_core.documents.Document` (same two
    fields) — code written against one works against the other without
    a langchain import in Layer A."""

    page_content: str
    metadata: dict[str, Any] = field(default_factory=dict)


# --------------------------------------------------------------------------
# Filter matching — supports both the Qdrant-ish shape the instructor
# package writes (`{"must": [{"key": "customer_id", "match": {"value": v}}]}`)
# and a flat shorthand (`{"customer_id": v}`) for convenience in tests.
# --------------------------------------------------------------------------
def _matches(metadata: dict[str, Any], flt: dict[str, Any] | None) -> bool:
    if not flt:
        return True
    if "must" in flt:
        for clause in flt["must"]:
            key = clause.get("key")
            match = clause.get("match", {})
            if "value" in match:
                if metadata.get(key) != match["value"]:
                    return False
            elif "any" in match:
                if metadata.get(key) not in match["any"]:
                    return False
        return True
    # Flat shorthand: every key must match exactly.
    return all(metadata.get(k) == v for k, v in flt.items())


@dataclass
class _Record:
    doc_id: str
    document: Document
    vector: list[float]


class SimpleVectorStore:
    """Dependency-free, in-memory, cosine-similarity vector store.

    Not persisted to disk and not shared across processes — that is
    deliberate: it is a lab/test double for Qdrant, not a production
    substitute. Production deployments set `RAFEEQ_VECTOR_MODE=qdrant`.
    """

    def __init__(self, collection_name: str, embedding: Any | None = None) -> None:
        self.collection_name = collection_name
        self.embedding = embedding or get_embeddings()
        self._records: dict[str, _Record] = {}

    # -- writes -----------------------------------------------------------
    def add_documents(self, documents: Iterable[Any], ids: list[str] | None = None) -> list[str]:
        """Embed and store `documents` (each with `.page_content` /
        `.metadata`, matching `Document` above or a LangChain `Document`).
        Returns the ids assigned (generated if `ids` is not given)."""
        documents = list(documents)
        texts = [getattr(d, "page_content", "") for d in documents]
        vectors = self.embedding.embed_documents(texts)
        assigned_ids = list(ids) if ids else [str(uuid.uuid4()) for _ in documents]
        for doc_id, doc, vec in zip(assigned_ids, documents, vectors):
            metadata = dict(getattr(doc, "metadata", {}) or {})
            self._records[doc_id] = _Record(
                doc_id=doc_id,
                document=Document(page_content=getattr(doc, "page_content", ""), metadata=metadata),
                vector=vec,
            )
        return assigned_ids

    # -- reads --------------------------------------------------------------
    def similarity_search(self, query: str, k: int = 4, filter: dict[str, Any] | None = None) -> list[Document]:
        return [doc for doc, _score in self.similarity_search_with_score(query, k=k, filter=filter)]

    def similarity_search_with_score(
        self, query: str, k: int = 4, filter: dict[str, Any] | None = None,
    ) -> list[tuple[Document, float]]:
        # FILTER FIRST, then rank — see module docstring. Never reverse this.
        candidates = [r for r in self._records.values() if _matches(r.document.metadata, filter)]
        if not candidates:
            return []
        query_vec = self.embedding.embed_query(query)
        scored = [(r.document, cosine_similarity(query_vec, r.vector)) for r in candidates]
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return scored[:k]

    def get_all(self, filter: dict[str, Any] | None = None) -> list[Document]:
        """Non-ranked listing of every document matching `filter` — used by
        erasure verification (count remaining records for a customer)."""
        return [r.document for r in self._records.values() if _matches(r.document.metadata, filter)]

    # -- deletes -------------------------------------------------------------
    def delete(self, filter: dict[str, Any] | None = None, ids: list[str] | None = None) -> int:
        """Remove matching records. Either `filter` (metadata-scoped, e.g.
        PDPL erasure by `customer_id`) or `ids` (specific records) — at
        least one must narrow the deletion; an empty call deletes nothing,
        it does not wipe the collection."""
        if ids:
            to_remove = [i for i in ids if i in self._records]
        elif filter:
            to_remove = [r.doc_id for r in self._records.values() if _matches(r.document.metadata, filter)]
        else:
            return 0
        for doc_id in to_remove:
            del self._records[doc_id]
        return len(to_remove)

    def count(self, filter: dict[str, Any] | None = None) -> int:
        return len(self.get_all(filter))

    def reset(self) -> None:
        """Clear the whole collection — test/lab convenience, not a PDPL
        erasure primitive (use `delete(filter=...)` for that)."""
        self._records.clear()


# --------------------------------------------------------------------------
# Factory
# --------------------------------------------------------------------------
_MISSING_QDRANT_HINT = (
    "RAFEEQ_VECTOR_MODE=qdrant requires `qdrant-client` and `langchain-qdrant` "
    "plus a running Qdrant instance (see docker-compose.yml), none of which "
    "are available in this environment. Unset RAFEEQ_VECTOR_MODE (or set it "
    "to anything else) to use the offline SimpleVectorStore instead."
)


def _qdrant_store(collection: str) -> Any:
    """Lazy import so Layer A never needs qdrant installed to import this
    module (SPEC §1 import-guard rule)."""
    try:
        from langchain_qdrant import QdrantVectorStore  # type: ignore[import-not-found]
    except ImportError as exc:  # pragma: no cover - not installed in this sandbox
        raise ImportError(_MISSING_QDRANT_HINT) from exc

    return QdrantVectorStore.from_existing_collection(collection_name=collection, embedding=get_embeddings())


def get_store(collection: str) -> Any:
    """Return a vector store for `collection`: Qdrant when
    `RAFEEQ_VECTOR_MODE=qdrant`, the offline `SimpleVectorStore` otherwise
    (the default — every lab and the eval harness run this way unless a
    participant opts into a real Qdrant instance).
    """
    settings = get_settings()
    if settings.vector_mode == "qdrant":
        return _qdrant_store(collection)
    return SimpleVectorStore(collection_name=collection)
