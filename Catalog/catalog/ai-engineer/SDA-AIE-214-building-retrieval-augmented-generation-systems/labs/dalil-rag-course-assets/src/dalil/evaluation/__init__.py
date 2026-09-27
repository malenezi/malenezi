"""Evaluation package.

Submodules are imported lazily (`from dalil.evaluation import gate`) rather than
re-exported here, so that `python -m dalil.evaluation.gate` does not trigger the
double-import warning that a package-level re-export causes.
"""
__all__ = ["retrieval_metrics", "by_class", "ragas_harness", "gate",
           "staleness_redteam", "report"]
