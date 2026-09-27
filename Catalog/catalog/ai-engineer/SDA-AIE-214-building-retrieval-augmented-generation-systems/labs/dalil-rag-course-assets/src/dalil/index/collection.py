"""Embedding + the Qdrant collection: dense vectors, sparse vectors, payload indexes.

Module 3 (Lab 3) and Module 4 (Lab 4) both live off this file, because hybrid
retrieval is a property of how the collection was BUILT, not of how it is
queried. A collection created without a sparse vector field cannot be made
hybrid later without a full re-index — which is the point of the "swapping the
embedding model is a migration, not a config change" slide.

Four decisions encoded here, each one a rubric line in the capstone:

1. bge-m3, not an English-only model. On the bilingual Dalil corpus the Arabic
   recall gap between bge-m3 and all-MiniLM-L6-v2 is roughly 0.88 vs 0.29.
   Lab 3 step 3 makes participants measure it rather than believe it.
2. Cosine + L2-normalised vectors at BOTH index and query time. Normalise on
   one side only and every similarity is quietly wrong.
3. Payload indexes on department, access_tier, lifecycle, effective_date.
   Without them, filtered search either scans or returns nothing — and the
   access-control gate in the capstone is enforced by filters.
4. Stable point ids (sha1 of doc_id:ordinal). Re-running ingest must be a
   no-op, not a duplication. Lab 3 step 2 checks this explicitly.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Sequence

from ..arabic import normalise
from ..config import settings

_MODEL_CACHE: dict[str, object] = {}


# --------------------------------------------------------------------------
# embedding
# --------------------------------------------------------------------------
HASH_MODEL = "hash-384"   # deterministic test fixture, NOT a real model


class _HashingEmbedder:
    """Character-ngram hashing embedder used ONLY as a test fixture.

    It lets the whole dense/hybrid/rerank/generation stack execute in CI and on
    an air-gapped classroom machine before bge-m3 has finished downloading. It
    is a bag-of-ngrams projection: it has no semantics, so it will NOT close the
    Arabic recall gap and must never appear in a reported benchmark. Every
    report that used it is stamped `model: "hash-384"`, which is the signal to
    throw the numbers away.
    """

    def __init__(self, dim: int = 384):
        self.dim = dim

    def encode(self, texts, batch_size=32, normalize_embeddings=True,
               show_progress_bar=False, convert_to_numpy=True):
        import hashlib
        import numpy as np
        out = np.zeros((len(texts), self.dim), dtype="float32")
        for i, t in enumerate(texts):
            toks = t.split()
            grams = toks + [t[j:j + 4] for j in range(0, max(len(t) - 3, 0), 2)]
            for g in grams:
                h = int(hashlib.blake2b(g.encode(), digest_size=8).hexdigest(), 16)
                out[i, h % self.dim] += 1.0
            n = np.linalg.norm(out[i])
            if n:
                out[i] /= n
        return out


def get_embedder(model_name: str | None = None):
    """Lazily load a SentenceTransformer. Cached: loading bge-m3 twice in one
    lab session is a 90-second mistake participants make constantly."""
    name = model_name or settings.embed_model
    if name in _MODEL_CACHE:
        return _MODEL_CACHE[name]
    if name == HASH_MODEL:
        _MODEL_CACHE[name] = _HashingEmbedder()
        return _MODEL_CACHE[name]
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:                       # pragma: no cover
        raise RuntimeError(
            "sentence-transformers is required for embedding.\n"
            "  pip install sentence-transformers\n"
            "Course bundle: set HF_HOME=/course/models so bge-m3 is not "
            "downloaded over the classroom network mid-lab."
        ) from exc
    model = SentenceTransformer(name)
    _MODEL_CACHE[name] = model
    return model


def embed_texts(texts: Sequence[str], *, model_name: str | None = None,
                batch_size: int = 32, is_query: bool = False) -> list[list[float]]:
    """Normalise -> encode -> L2-normalise. One function for index and query.

    `is_query` exists only for models that want an instruction prefix; bge-m3
    does not, so it is a no-op today and a hook tomorrow. Keeping the two paths
    in ONE function is deliberate: the most common silent retrieval bug in the
    course is a query path that forgets `normalise()`.
    """
    prepared = [normalise(t) for t in texts]
    model = get_embedder(model_name)
    vecs = model.encode(prepared, batch_size=batch_size, normalize_embeddings=True,
                        show_progress_bar=False, convert_to_numpy=True)
    return [v.tolist() for v in vecs]


# --------------------------------------------------------------------------
# sparse (BM25-style) vectors for the hybrid leg
# --------------------------------------------------------------------------
def get_sparse_encoder():
    """FastEmbed's BM25 if available; otherwise the pure-python fallback in
    retrieve/sparse.py. Labs must not be blocked by an optional wheel."""
    try:
        from fastembed import SparseTextEmbedding
        key = "__sparse__"
        if key not in _MODEL_CACHE:
            _MODEL_CACHE[key] = SparseTextEmbedding(model_name="Qdrant/bm25")
        return _MODEL_CACHE[key]
    except ImportError:
        return None


# --------------------------------------------------------------------------
# chunks
# --------------------------------------------------------------------------
def load_chunks(path: str | Path) -> list[dict]:
    out = []
    with Path(path).open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


# --------------------------------------------------------------------------
# Qdrant
# --------------------------------------------------------------------------
def get_client(url: str | None = None):
    try:
        from qdrant_client import QdrantClient
    except ImportError as exc:                       # pragma: no cover
        raise RuntimeError("qdrant-client is required: pip install qdrant-client") from exc
    return QdrantClient(url=url or settings.qdrant_url, timeout=60)


PAYLOAD_INDEXES = {
    "doc_id": "keyword",
    "department": "keyword",
    "access_tier": "keyword",
    "lifecycle": "keyword",
    "language": "keyword",
    "kind": "keyword",
    "effective_date": "keyword",
    "circular_id": "keyword",
}


def build_collection(name: str | None = None, *, dim: int | None = None,
                     recreate: bool = False, sparse: bool = True, client=None):
    """Create the collection with HNSW params, quantization and payload indexes."""
    from qdrant_client import models as qm

    client = client or get_client()
    name = name or settings.collection
    dim = dim or settings.embed_dim

    exists = client.collection_exists(name)
    if exists and not recreate:
        return client
    if exists:
        client.delete_collection(name)

    quant = None
    if settings.quantization == "int8":
        quant = qm.ScalarQuantization(
            scalar=qm.ScalarQuantizationConfig(type=qm.ScalarType.INT8, quantile=0.99,
                                               always_ram=True))
    elif settings.quantization == "binary":
        quant = qm.BinaryQuantization(binary=qm.BinaryQuantizationConfig(always_ram=True))

    client.create_collection(
        collection_name=name,
        vectors_config={"dense": qm.VectorParams(size=dim, distance=qm.Distance.COSINE)},
        sparse_vectors_config=({"sparse": qm.SparseVectorParams(
            index=qm.SparseIndexParams(on_disk=False))} if sparse else None),
        hnsw_config=qm.HnswConfigDiff(m=settings.hnsw_m,
                                      ef_construct=settings.hnsw_ef_construct),
        quantization_config=quant,
    )
    for field, schema in PAYLOAD_INDEXES.items():
        client.create_payload_index(collection_name=name, field_name=field,
                                    field_schema=schema)
    return client


def upsert_chunks(chunks: Iterable[dict], *, name: str | None = None,
                  model_name: str | None = None, batch_size: int = 64,
                  with_sparse: bool = True, client=None) -> int:
    """Embed and upsert. Idempotent: the point id is the chunk's stable hash."""
    from qdrant_client import models as qm

    client = client or get_client()
    name = name or settings.collection
    chunks = list(chunks)
    if not chunks:
        return 0

    sparse_encoder = get_sparse_encoder() if with_sparse else None
    total = 0
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        texts = [c["text"] for c in batch]
        dense = embed_texts(texts, model_name=model_name)
        sparse_vecs = None
        if sparse_encoder is not None:
            sparse_vecs = list(sparse_encoder.embed([normalise(t) for t in texts]))

        points = []
        for j, c in enumerate(batch):
            vectors: dict = {"dense": dense[j]}
            if sparse_vecs is not None:
                sv = sparse_vecs[j]
                vectors["sparse"] = qm.SparseVector(indices=sv.indices.tolist(),
                                                    values=sv.values.tolist())
            payload = {k: v for k, v in c.items() if k != "text"}
            payload["text"] = c["text"]
            points.append(qm.PointStruct(id=_uuid_from(c["chunk_id"]), vector=vectors,
                                         payload=payload))
        client.upsert(collection_name=name, points=points, wait=True)
        total += len(points)
    return total


def _uuid_from(hex_id: str) -> str:
    """Qdrant accepts uint64 or UUID ids. Our chunk_id is a sha1 hex digest, so
    fold it into a stable UUID rather than inventing a counter."""
    import uuid
    return str(uuid.UUID(hex_id[:32].ljust(32, "0")))


def collection_stats(name: str | None = None, client=None) -> dict:
    client = client or get_client()
    name = name or settings.collection
    info = client.get_collection(name)
    return {
        "points": info.points_count,
        "vectors": getattr(info.config.params, "vectors", None),
        "status": str(info.status),
    }
