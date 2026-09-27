import math

from dalil.evaluation.retrieval_metrics import (recall_at_k, mrr, ndcg_at_k,
                                                evaluate_retrieval)
from dalil.evaluation.by_class import evaluate_by_class
from dalil.evaluation.gate import check_gate
from dalil.evaluation.staleness_redteam import score_answer
from dalil.ingest.ocr import cer, levenshtein


def test_recall_and_mrr_basics():
    assert recall_at_k(["a", "b", "c"], {"a", "z"}, 3) == 0.5
    assert mrr(["x", "a"], {"a"}) == 0.5
    assert mrr(["x", "y"], {"a"}) == 0.0


def test_ndcg_rewards_ordering():
    perfect = ndcg_at_k(["a", "b"], {"a": 2.0, "b": 1.0}, 2)
    swapped = ndcg_at_k(["b", "a"], {"a": 2.0, "b": 1.0}, 2)
    assert math.isclose(perfect, 1.0)
    assert swapped < perfect


def test_aggregate_hides_a_collapsed_class():
    """The reason the rubric demands per-class reporting."""
    results = (
        [{"retrieved": ["a"], "relevant": ["a"], "query_class": "factoid"}] * 90 +
        [{"retrieved": ["z"], "relevant": ["a"], "query_class": "identifier"}] * 10
    )
    rep = evaluate_by_class(results, k=1)
    assert rep["aggregate"]["recall@1"] == 0.9        # looks healthy
    assert rep["by_class"]["identifier"]["recall@1"] == 0.0   # is not
    assert rep["weakest_class"] == "identifier"


def test_gate_fails_on_regression_beyond_tolerance():
    base = {"metrics": {"faithfulness": 0.93}, "config": {}, "judge": "j"}
    cur = {"metrics": {"faithfulness": 0.88}, "config": {}, "judge": "j"}
    res = check_gate(cur, base, tolerance=0.03)
    assert not res.passed


def test_gate_warns_when_config_drifted():
    base = {"metrics": {"faithfulness": 0.95}, "config": {"top_k": 6}, "judge": "j"}
    cur = {"metrics": {"faithfulness": 0.95}, "config": {"top_k": 10}, "judge": "j"}
    res = check_gate(cur, base)
    assert any("config differs" in w for w in res.warnings)


def test_gate_warns_when_judge_changed():
    base = {"metrics": {"faithfulness": 0.95}, "config": {}, "judge": "judge-a"}
    cur = {"metrics": {"faithfulness": 0.95}, "config": {}, "judge": "judge-b"}
    assert any("judge changed" in w for w in check_gate(cur, base).warnings)


def test_absolute_floor_fails_even_without_baseline():
    cur = {"metrics": {"faithfulness": 0.5}, "config": {}, "judge": "j"}
    assert not check_gate(cur, None).passed


def test_staleness_verdicts():
    assert score_answer("The figure is 30", "30", "20", False) == "answered_current"
    assert score_answer("The figure is 20", "30", "20", False) == "answered_stale"
    assert score_answer("no idea", "30", "20", True) == "refused"


def test_cer_is_zero_for_identical_normalised_text():
    assert cer("سياسة التصنيف", "سِيَاسَةُ التَّصْنِيفِ") == 0.0
    assert levenshtein("abc", "abd") == 1
