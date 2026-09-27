from dalil.advanced.multihop import decompose, _overlap
from dalil.advanced.corrective import grade_retrieval
from dalil.retrieve.backends import Hit


def test_twin_subquestions_are_deduped():
    """The Lab 7 bug: a decomposer that emits two paraphrases of one question
    doubles cost for identical evidence."""
    assert _overlap("what is the housing allowance", "what is the housing allowance?") > 0.8


def test_decompose_falls_back_to_rule_based_split():
    q = ("Which SDAIA instrument requires a transfer risk assessment and what does "
         "that assessment cover?")
    subs, gen = decompose(q)
    assert len(subs) >= 1
    assert all(s.strip() for s in subs)


def test_grader_returns_none_for_empty_retrieval():
    g = grade_retrieval("anything", [])
    assert g.grade == "none"


def test_grader_can_say_none_so_the_loop_can_refuse():
    """Without a 'none' verdict, a corrective loop retries to the cap and then
    answers an unanswerable question from irrelevant context."""
    hits = [Hit("c1", "d1", "completely unrelated text about backup schedules", 1.0)]
    g = grade_retrieval("parental leave entitlement for seconded contractors", hits)
    assert g.grade in {"none", "partial"}
