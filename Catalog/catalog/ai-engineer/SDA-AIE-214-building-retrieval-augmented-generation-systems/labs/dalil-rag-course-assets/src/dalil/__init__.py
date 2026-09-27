"""Dalil (دليل) — the golden-thread RAG system of SDA-AIE-214.

Every module in this package corresponds to one stage of the reference
architecture taught in the course, and to one lab:

    ingest/     Module 2 · Lab 2      parse, OCR, normalise, chunk
    index/      Module 3 · Lab 3      embed, collection, payload filters
    retrieve/   Module 3-4 · Lab 3-4  dense, sparse, RRF fusion, reranking
    generate/   Module 5 · Lab 5      context budget, grounded prompt, citations
    evaluation/ Module 6 · Lab 6      retrieval metrics, RAGAS, regression gate
    advanced/   Module 7 · Lab 7      multi-query, multi-hop, corrective RAG
    benchmarks/ cross-cutting         MIRACL-ar, BEIR, TechQA sanity checks

Import discipline: heavy dependencies (torch, qdrant-client, FlagEmbedding) are
imported lazily inside functions, so the package imports and its unit tests run
on a laptop with nothing but the standard library plus pytest. Labs fail loudly
with an actionable message when a real dependency is missing.
"""

__version__ = "1.0.0"
__course__ = "SDA-AIE-214"
