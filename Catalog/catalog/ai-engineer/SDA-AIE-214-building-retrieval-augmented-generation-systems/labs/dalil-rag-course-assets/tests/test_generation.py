from dalil.generate.context import (assemble_context, edge_order, estimate_tokens,
                                    _near_duplicate)
from dalil.generate.answer import verify_citations
from dalil.retrieve.backends import Hit, AccessContext


def _hit(i, text, tier="public", score=1.0, dept="hr"):
    return Hit(f"c{i}", f"d{i}", text, score,
               {"access_tier": tier, "department": dept, "lifecycle": "current",
                "title": f"Doc {i}"})


def test_edge_ordering_puts_best_first_and_second_last():
    assert edge_order([1, 2, 3, 4, 5]) == [1, 3, 5, 4, 2]


def test_arabic_costs_more_tokens_per_character():
    ar = "سياسة تصنيف البيانات الشخصية في الجهات الحكومية"
    en = "personal data classification policy for government entities"
    assert estimate_tokens(ar) > estimate_tokens(en) * 0.9


def test_budget_is_respected():
    hits = [_hit(i, "word " * 400) for i in range(20)]
    blocks, stats = assemble_context(hits, budget_tokens=300)
    assert stats["tokens_estimated"] <= 300
    assert stats["dropped"]["budget"] > 0


def test_access_is_reasserted_at_context_construction():
    hits = [_hit(1, "public text"), _hit(2, "secret text", tier="restricted")]
    blocks, stats = assemble_context(hits, ctx=AccessContext(max_tier="public"))
    assert stats["dropped"]["access"] == 1
    assert all("secret" not in b.text for b in blocks)


def test_near_duplicates_are_dropped():
    text = "The housing allowance shall not exceed twenty five percent of basic salary"
    hits = [_hit(1, text), _hit(2, text + " as amended")]
    blocks, stats = assemble_context(hits)
    assert stats["dropped"]["duplicate"] == 1


def test_invented_citation_is_detected():
    blocks, _ = assemble_context([_hit(1, "a"), _hit(2, "b")])
    v = verify_citations("The answer is X [1]. Also Y [7].", blocks)
    assert v["invented_citations"] == [7]
    assert v["citations"] == [1]


def test_uncited_sentence_is_counted():
    blocks, _ = assemble_context([_hit(1, "a")])
    v = verify_citations("This sentence has no citation at all.", blocks)
    assert v["uncited_sentences"] == 1
