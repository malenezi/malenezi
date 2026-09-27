"""Guards on the shipped data. These fail loudly when someone regenerates the
corpus with a different seed and forgets to regenerate the evaluation sets."""
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "data/corpus/layer_b_index.json"


@pytest.fixture(scope="module")
def index():
    if not INDEX.exists():
        pytest.skip("run `make corpus` first")
    return json.loads(INDEX.read_text(encoding="utf-8"))


def _jsonl(p):
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def test_corpus_has_the_four_things_layer_a_cannot_provide(index):
    docs = index["documents"]
    assert sum(1 for d in docs if d["format"] == "pdf_scanned") >= 20, "OCR path"
    assert sum(1 for d in docs if d["format"] == "xlsx") >= 8, "tabular facts"
    assert sum(1 for d in docs if d.get("access_tier") == "restricted") >= 40, "access control"
    assert sum(1 for d in docs
               if (d.get("lifecycle_by_corpus") or {}).get("v2") == "superseded") == 12


def test_every_layer_b_document_cites_a_layer_a_instrument(index):
    assert all(d.get("cites") for d in index["documents"])


def test_ocr_gold_exists_for_every_scanned_document(index):
    for d in index["documents"]:
        if d["format"] == "pdf_scanned":
            assert (ROOT / "data/corpus" / d["ocr_gold"]).exists()


def test_golden_set_answers_match_the_generated_corpus(index):
    """The whole point of deriving eval sets from the corpus: this can never
    silently drift."""
    golden = ROOT / "data/golden/golden_qa_v1.jsonl"
    if not golden.exists():
        pytest.skip("run `make eval-sets` first")
    by_id = {d["doc_id"]: d for d in index["documents"]}
    checked = 0
    for row in _jsonl(golden):
        if row.get("verify") or not row.get("ground_truth"):
            continue
        for doc_id in row["relevant_doc_ids"]:
            d = by_id.get(doc_id)
            if not d or not d.get("facts"):
                continue
            if row["query_class"] == "factoid" and "max_entitlement_pct" in d["facts"]:
                assert str(d["facts"]["max_entitlement_pct"]) in row["ground_truth"]
                checked += 1
    assert checked > 10, "expected the generated facts to appear in the answer keys"


def test_failure_gallery_covers_all_eight_classes():
    p = ROOT / "data/probes/failure_gallery.jsonl"
    if not p.exists():
        pytest.skip("run `make eval-sets` first")
    classes = {r["failure_class"] for r in _jsonl(p)}
    assert classes == {f"F{i}" for i in range(1, 9)}


def test_unanswerable_set_is_bilingual():
    p = ROOT / "data/redteam/unanswerable.jsonl"
    if not p.exists():
        pytest.skip("run `make eval-sets` first")
    langs = {r["language"] for r in _jsonl(p)}
    assert langs == {"ar", "en"}, "refusal must be tested in both languages"
