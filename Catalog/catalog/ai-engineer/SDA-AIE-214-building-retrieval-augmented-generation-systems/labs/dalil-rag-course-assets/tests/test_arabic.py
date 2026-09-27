"""Arabic normalisation is load-bearing for the whole course; test it hardest."""
from dalil.arabic import (normalise, normalise_arabic, normalise_identifier,
                          contains_identifier, has_arabic, fold_presentation_forms)


def test_presentation_forms_fold_to_base_letters():
    # exactly what a bidi-less PDF writer stores
    assert normalise("ﺗﺤﺪﻳﺚ ﺷﺮﺍﺋﺢ ﺑﺪﻝ ﺍﻟﺴﻜﻦ") == "تحديث شرائح بدل السكن"


def test_alef_and_ya_variants_unify():
    assert normalise("إجراءات") == normalise("اجراءات") == normalise("أجراءات")
    assert normalise("مبنى") == normalise("مبني")


def test_diacritics_and_tatweel_removed():
    assert normalise("سِيَاسَةُ التَّصْنِيفِ") == normalise("سياسة التصنيف")
    assert "ـ" not in normalise("سـياسـة")


def test_arabic_indic_digits_become_ascii():
    assert "44/2025" in normalise("التعميم ٤٤/٢٠٢٥")


def test_identifier_detection():
    assert contains_identifier("circular 44/2025")
    assert contains_identifier("ما مضمون التعميم ٤٤/٢٠٢٥؟")
    assert contains_identifier("NDSA-HR-101")
    assert not contains_identifier("what is the housing allowance")


def test_identifier_separator_normalisation():
    a = normalise_identifier("Circular 44 - 2025")
    b = normalise_identifier("circular 44/2025")
    assert a == b


def test_index_and_query_paths_agree():
    """The single most important invariant in the course: the same string
    normalised on the index path and the query path must be identical."""
    doc = "التعميم رقم ٤٤/٢٠٢٥ بشأن بدل السكن"
    query = "ما مضمون التعميم 44/2025؟"
    assert normalise(doc).split("44/2025")[0]  # doc contains the ascii form
    assert "44/2025" in normalise(doc) and "44/2025" in normalise(query)


def test_latin_text_passes_through():
    assert normalise("  Housing   Allowance  ") == "Housing Allowance"
    assert not has_arabic("Housing Allowance")
