"""Two interchangeable retrieval backends behind one interface.

    MemoryBackend  -- BM25 + optional dense vectors, entirely in-process.
                      Used by tests, the evaluation harness in offline mode,
                      and the practical-assessment kits. No Docker, no model
                      download, no excuses.
    QdrantBackend  -- the real thing the labs and the capstone use.

Both honour the same access-control contract: a search NEVER returns a chunk
whose access_tier or department the caller was not granted. Enforcing this at
the backend rather than in a post-filter is deliberate — a post-filter that
runs after top-k has already thrown away the results the user WAS allowed to
see, and silently degrades their answers instead of protecting anything.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, Sequence

from ..config import settings
from .sparse import BM25

TIER_ORDER = {"public": 0, "internal": 1, "restricted": 2}


@dataclass
class Hit:
    chunk_id: str
    doc_id: str
    text: str
    score: float
    payload: dict = field(default_factory=dict)

    @property
    def department(self) -> str:
        return self.payload.get("department", "general")

    @property
    def lifecycle(self) -> str:
        return self.payload.get("lifecycle", "unknown")


@dataclass
class AccessContext:
    """Who is asking. `max_tier` is the highest classification they may see;
    `departments` is None for org-wide roles or a set for scoped ones."""
    max_tier: str = "public"
    departments: set[str] | None = None
    include_superseded: bool = False

    def allows(self, payload: dict) -> bool:
        tier = payload.get("access_tier", "restricted")
        if TIER_ORDER.get(tier, 2) > TIER_ORDER.get(self.max_tier, 0):
            return False
        if self.departments is not None:
            if payload.get("department", "general") not in self.departments | {"general"}:
                return False
        if not self.include_superseded and payload.get("lifecycle") == "superseded":
            return False
        return True


class Backend(Protocol):
    def search_dense(self, query: str, k: int, ctx: AccessContext) -> list[Hit]: ...
    def search_sparse(self, query: str, k: int, ctx: AccessContext) -> list[Hit]: ...


class MemoryBackend:
    """In-process backend. Dense leg is optional: without sentence-transformers
    it degrades to sparse-only and SAYS SO rather than silently returning
    lexical results dressed up as semantic ones."""

    def __init__(self, chunks: Sequence[dict], *, dense: bool = False,
                 model_name: str | None = None):
        self.chunks = {c["chunk_id"]: c for c in chunks}
        self.bm25 = BM25()
        for c in chunks:
            self.bm25.add(c["chunk_id"], c["text"])
        self.bm25.finalise()
        self.dense_enabled = False
        self._vectors: dict[str, list[float]] = {}
        if dense:
            try:
                from ..index.collection import embed_texts
                ids = list(self.chunks)
                vecs = embed_texts([self.chunks[i]["text"] for i in ids],
                                   model_name=model_name)
                self._vectors = dict(zip(ids, vecs))
                self._model_name = model_name
                self.dense_enabled = True
            except Exception as exc:                 # pragma: no cover
                self.dense_error = str(exc)

    # -- helpers -----------------------------------------------------------
    def _hit(self, cid: str, score: float) -> Hit:
        c = self.chunks[cid]
        return Hit(cid, c.get("doc_id", ""), c.get("text", ""), score, c)

    def _filter(self, hits: list[Hit], ctx: AccessContext) -> list[Hit]:
        return [h for h in hits if ctx.allows(h.payload)]

    # -- interface ---------------------------------------------------------
    def search_sparse(self, query: str, k: int, ctx: AccessContext) -> list[Hit]:
        raw = self.bm25.search(query, k=k * 4)
        return self._filter([self._hit(cid, s) for cid, s in raw], ctx)[:k]

    def search_dense(self, query: str, k: int, ctx: AccessContext) -> list[Hit]:
        if not self.dense_enabled:
            return []
        from ..index.collection import embed_texts
        qv = embed_texts([query], model_name=getattr(self, "_model_name", None))[0]
        scored = []
        for cid, v in self._vectors.items():
            scored.append((cid, sum(a * b for a, b in zip(qv, v))))
        scored.sort(key=lambda kv: -kv[1])
        hits = [self._hit(cid, s) for cid, s in scored[:k * 4]]
        return self._filter(hits, ctx)[:k]


class QdrantBackend:
    """The production backend. Filters are pushed INTO the search."""

    def __init__(self, client=None, collection: str | None = None,
                 model_name: str | None = None):
        from ..index.collection import get_client
        self.client = client or get_client()
        self.collection = collection or settings.collection
        self.model_name = model_name

    def _filter(self, ctx: AccessContext):
        from qdrant_client import models as qm
        must = []
        allowed = [t for t, o in TIER_ORDER.items() if o <= TIER_ORDER.get(ctx.max_tier, 0)]
        must.append(qm.FieldCondition(key="access_tier", match=qm.MatchAny(any=allowed)))
        if ctx.departments is not None:
            must.append(qm.FieldCondition(
                key="department", match=qm.MatchAny(any=sorted(ctx.departments | {"general"}))))
        if not ctx.include_superseded:
            must.append(qm.FieldCondition(key="lifecycle",
                                          match=qm.MatchExcept(**{"except": ["superseded"]})))
        return qm.Filter(must=must)

    def search_dense(self, query: str, k: int, ctx: AccessContext) -> list[Hit]:
        from qdrant_client import models as qm
        from ..index.collection import embed_texts
        qv = embed_texts([query], model_name=self.model_name)[0]
        res = self.client.query_points(
            collection_name=self.collection, query=qv, using="dense", limit=k,
            query_filter=self._filter(ctx), with_payload=True,
            search_params=qm.SearchParams(hnsw_ef=settings.hnsw_ef_search),
        ).points
        return [Hit(p.payload.get("chunk_id", str(p.id)), p.payload.get("doc_id", ""),
                    p.payload.get("text", ""), p.score, p.payload) for p in res]

    def search_sparse(self, query: str, k: int, ctx: AccessContext) -> list[Hit]:
        from qdrant_client import models as qm
        from ..arabic import normalise
        from ..index.collection import get_sparse_encoder
        enc = get_sparse_encoder()
        if enc is None:
            return []
        sv = next(iter(enc.embed([normalise(query)])))
        res = self.client.query_points(
            collection_name=self.collection,
            query=qm.SparseVector(indices=sv.indices.tolist(), values=sv.values.tolist()),
            using="sparse", limit=k, query_filter=self._filter(ctx), with_payload=True,
        ).points
        return [Hit(p.payload.get("chunk_id", str(p.id)), p.payload.get("doc_id", ""),
                    p.payload.get("text", ""), p.score, p.payload) for p in res]


def build_backend(chunks: Sequence[dict] | None = None, *, kind: str = "auto",
                  dense: bool = True):
    """`kind`: 'memory' | 'qdrant' | 'auto'. 'auto' prefers Qdrant when the
    server answers and falls back to memory, printing which it chose — never
    silently, because a benchmark number that came from a different backend
    than the participant thinks is a wasted lab."""
    if kind == "memory" or (kind == "auto" and chunks is not None and not _qdrant_up()):
        if chunks is None:
            raise ValueError("memory backend needs chunks")
        return MemoryBackend(chunks, dense=dense)
    return QdrantBackend()


def _qdrant_up() -> bool:
    try:
        from ..index.collection import get_client
        get_client().get_collections()
        return True
    except Exception:
        return False
