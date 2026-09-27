import pytest

from dalil.retrieve.sparse import BM25, tokenize
from dalil.retrieve.hybrid import rrf_fuse
from dalil.retrieve.backends import Hit, AccessContext
from dalil.retrieve.router import classify_query, QueryClass, route


def test_bm25_finds_exact_identifier():
    b = BM25()
    b.add("a", "Circular 44/2025 sets the housing allowance band")
    b.add("b", "Circular 45/2025 concerns travel per-diem")
    b.add("c", "General guidance on allowances and entitlements")
    b.finalise()
    top = b.search("circular 44/2025", k=1)
    assert top and top[0][0] == "a"


def test_bm25_matches_across_digit_sets():
    b = BM25()
    b.add("a", "التعميم رقم ٤٤/٢٠٢٥ بشأن بدل السكن")
    b.finalise()
    assert b.search("circular 44/2025", k=1)[0][0] == "a"


def test_rrf_prefers_agreement_over_any_single_rank():
    dense = [Hit("x", "d", "", 0.9), Hit("y", "d", "", 0.8), Hit("z", "d", "", 0.7)]
    sparse = [Hit("z", "d", "", 12.0), Hit("x", "d", "", 9.0)]
    fused = rrf_fuse([dense, sparse])
    # x is rank 1 and rank 2; z is rank 3 and rank 1 -> x wins on agreement
    assert fused[0].chunk_id == "x"


def test_rrf_is_scale_invariant():
    a = [Hit("p", "d", "", 0.51), Hit("q", "d", "", 0.50)]
    b = [Hit("q", "d", "", 5000.0), Hit("p", "d", "", 1.0)]
    fused = rrf_fuse([a, b])
    assert {h.chunk_id for h in fused} == {"p", "q"}
    assert abs(fused[0].score - fused[1].score) < 1e-9   # ranks 1+2 both ways


@pytest.mark.parametrize("q,expected", [
    ("What figure does Circular 44/2025 set?", QueryClass.IDENTIFIER),
    ("ما مضمون التعميم ٤٤/٢٠٢٥؟", QueryClass.IDENTIFIER),
    ("How much is the housing allowance for Grade 11?", QueryClass.TABULAR),
    ("How do I request leave?", QueryClass.PROCEDURAL),
    ("What is the weather in Riyadh?", QueryClass.UNANSWERABLE),
    ("remote work", QueryClass.AMBIGUOUS),
])
def test_query_classification(q, expected):
    assert classify_query(q) is expected


def test_identifier_queries_get_mandatory_sparse():
    assert route("Circular 44/2025")["sparse_weight"] == "mandatory"


def test_access_context_blocks_higher_tier():
    ctx = AccessContext(max_tier="internal")
    assert ctx.allows({"access_tier": "public"})
    assert ctx.allows({"access_tier": "internal"})
    assert not ctx.allows({"access_tier": "restricted"})


def test_access_context_blocks_other_departments():
    ctx = AccessContext(max_tier="restricted", departments={"hr"})
    assert ctx.allows({"access_tier": "restricted", "department": "hr"})
    assert ctx.allows({"access_tier": "restricted", "department": "general"})
    assert not ctx.allows({"access_tier": "restricted", "department": "finance"})


def test_superseded_is_excluded_by_default():
    ctx = AccessContext(max_tier="restricted")
    assert not ctx.allows({"access_tier": "public", "lifecycle": "superseded"})
    assert AccessContext(max_tier="restricted", include_superseded=True).allows(
        {"access_tier": "public", "lifecycle": "superseded"})
