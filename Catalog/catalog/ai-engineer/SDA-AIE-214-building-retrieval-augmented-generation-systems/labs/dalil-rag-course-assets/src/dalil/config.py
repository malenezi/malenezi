"""Central configuration. Everything tunable in a lab lives here or in .env.

Rule the course enforces: no magic numbers scattered through lab code. If a
participant tunes fetch_k in Lab 4, they change it in one place and the change
is visible in `git diff` — which is how DECISIONS.md gets written honestly.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field, asdict


def _env(key: str, default):
    raw = os.getenv(key)
    if raw is None:
        return default
    if isinstance(default, bool):
        return raw.strip().lower() in {"1", "true", "yes", "on"}
    if isinstance(default, int):
        return int(raw)
    if isinstance(default, float):
        return float(raw)
    return raw


@dataclass
class Settings:
    # ---- corpus -----------------------------------------------------------
    corpus_dir: str = _env("DALIL_CORPUS", "data/corpus/corpus_v1")
    corpus_v2_dir: str = _env("DALIL_CORPUS_V2", "data/corpus/corpus_v2")
    layer_a_dir: str = _env("DALIL_LAYER_A", "data/corpus/layer_a")

    # ---- embedding / index ------------------------------------------------
    embed_model: str = _env("DALIL_EMBED_MODEL", "BAAI/bge-m3")
    embed_dim: int = _env("DALIL_EMBED_DIM", 1024)
    contrast_model: str = _env("DALIL_CONTRAST_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    reranker_model: str = _env("DALIL_RERANKER", "BAAI/bge-reranker-v2-m3")
    qdrant_url: str = _env("QDRANT_URL", "http://localhost:6333")
    collection: str = _env("DALIL_COLLECTION", "dalil")
    hnsw_m: int = _env("DALIL_HNSW_M", 16)
    hnsw_ef_construct: int = _env("DALIL_HNSW_EF_CONSTRUCT", 128)
    hnsw_ef_search: int = _env("DALIL_EF", 128)          # Lab 3 tunes this
    quantization: str = _env("DALIL_QUANT", "int8")      # none|int8|binary

    # ---- chunking ---------------------------------------------------------
    chunk_target_chars: int = _env("DALIL_CHUNK", 900)
    chunk_overlap_chars: int = _env("DALIL_OVERLAP", 120)
    tables_atomic: bool = _env("DALIL_TABLES_ATOMIC", True)
    ocr_dpi: int = _env("DALIL_OCR_DPI", 300)
    # Measured on the shipped scanned-Arabic subset (22 docs, tuned settings):
    # mean CER 0.053, p95 0.062, worst 0.100. The gate is set just above the
    # measured mean so it is a REAL gate -- a participant who leaves the naive
    # OCR settings in place lands around 0.084 and fails it. 0.05 is the stretch
    # target and the fast-finisher task; see assessments/keys/lab2_ocr_key.md.
    ocr_cer_gate: float = _env("DALIL_OCR_CER_GATE", 0.06)

    # ---- retrieval budget (Lab 4) -----------------------------------------
    fetch_k: int = _env("DALIL_FETCH_K", 40)
    top_k: int = _env("DALIL_TOP_K", 6)
    rrf_k: int = _env("DALIL_RRF_K", 60)
    rerank_enabled: bool = _env("DALIL_RERANK", True)

    # ---- generation (Lab 5) -----------------------------------------------
    llm_base_url: str = _env("DALIL_LLM_BASE_URL", "http://localhost:8000/v1")
    llm_model: str = _env("DALIL_LLM_MODEL", "course-gateway-model")
    llm_api_key: str = _env("DALIL_LLM_API_KEY", "")
    temperature: float = _env("DALIL_TEMPERATURE", 0.0)
    context_token_budget: int = _env("DALIL_CTX_BUDGET", 3000)
    refusal_threshold: float = _env("DALIL_REFUSAL_TAU", 0.35)

    # ---- evaluation (Lab 6) ------------------------------------------------
    judge_model: str = _env("DALIL_JUDGE_MODEL", "course-gateway-judge")
    judge_temperature: float = 0.0
    gate_tolerance: float = _env("DALIL_GATE_TOLERANCE", 0.03)

    # ---- advanced (Lab 7) --------------------------------------------------
    max_hops: int = _env("DALIL_MAX_HOPS", 2)
    corrective_max_retries: int = _env("DALIL_CORRECTIVE_RETRIES", 1)
    router_enabled: bool = _env("DALIL_ROUTER", True)

    # ---- access control ----------------------------------------------------
    access_tiers: tuple = ("public", "internal", "restricted")

    def as_dict(self) -> dict:
        return asdict(self)


settings = Settings()
