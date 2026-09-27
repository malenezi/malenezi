"""Masar (مسار) Lakehouse — the code spine of SDA-DSC-214.

Masar is a national smart-mobility platform: ride-hailing plus public
transit, three Saudi cities, one lakehouse. Every module here is one layer of
that platform, and every lab grows the SAME lakehouse rather than a new toy.

Layout (mirrors the medallion, not the tooling)::

    masar.spark          the ONE Spark + Delta session builder
    masar.config         paths, env, and the canonical table registry
    masar.ingest         raw feeds -> bronze (append-only, with lineage)
    masar.econ           compute/storage cost model + scan benchmarks
    masar.delta          ACID: constraints, MERGE, time travel, maintenance
    masar.stream         Kafka -> bronze -> silver, exactly-once
    masar.quality        the promotion gate, observability, GX plumbing
    masar.governance     PDPL classification, retention, erasure
    masar.transform      silver and gold builds (idempotent, documented grain)
    masar.serve          AI feature serving + BI star schema + PDPL boundary
    masar.orchestration  the dependency-ordered runner (no Airflow required)
    masar.tools          small CLIs the labs lean on (count, sql, snapshot...)

Importing this package NEVER imports PySpark. Every heavy dependency
(pyspark, delta, kafka, redis, sklearn, great_expectations) is imported
inside the function that needs it, so that:

  * ``python -c "import masar"`` works on a machine with no Spark at all,
  * ``scripts/doctor.py`` can report a MISSING dependency instead of dying on
    an ImportError while trying to tell you about it,
  * the pure-Python unit tests in ``tests/`` run in under a second.

The unifying question this package exists to answer:
    "What happens to Masar's AI system if THIS part of the data platform fails?"
"""

from __future__ import annotations

__version__ = "1.0.0"
__course__ = "SDA-DSC-214 — Modern Data Engineering for AI Systems"
__all__ = ["__version__", "__course__"]
