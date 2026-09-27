"""Public IR benchmarks used as *instruments*, not as the course project.

The Dalil corpus proves the system works on the documents that matter. These
three public benchmarks prove the participant's INSTRUMENTS work — that their
recall@k code is right, that their Arabic pipeline is competitive against a
published number, and that their evaluation harness generalises beyond the one
corpus it was written for.

    miracl_ar   Arabic retrieval with human relevance judgements. The honest
                answer to "is our Arabic retrieval actually good, or does it
                just look good on a corpus we built?"
    beir        Corpus + queries + qrels in one shape across 18 datasets and
                nine task types. Because the structure is uniform, recall@k,
                MRR and nDCG code written once runs everywhere -- which is
                exactly why it is the right harness for the metrics lab.
    techqa      Enterprise technical support Q&A (eManual / TechQA, as packaged
                in RAGBench). The closest public analogue to the enterprise
                support assistant most participants will build at work, and it
                carries genuinely unanswerable questions -- the only public set
                in the course that grades REFUSAL rather than answering.

All three loaders degrade to a small bundled sample when `datasets` is missing
or the classroom has no network, and every report states which mode it ran in.
A benchmark that silently ran on 40 rows instead of 40,000 is worse than no
benchmark.
"""
from .common import BenchmarkResult, evaluate_run  # noqa: F401
