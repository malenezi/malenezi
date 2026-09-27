from dalil.ingest.loaders import Block, ParsedDocument, _serialise_table
from dalil.ingest.chunker import chunk_document, chunk_quality_stats


def _doc(blocks):
    return ParsedDocument("d1", "d1.pdf", "pdf", blocks)


def test_tables_are_never_split_mid_row():
    md = _serialise_table([["Grade", "Amount"], ["Grade 11", "9,900"], ["Grade 12", "11,700"]])
    doc = _doc([Block("heading", "3. Bands"), Block("table", md)])
    chunks = chunk_document(doc, doc_meta={"title": "Allowances"})
    tables = [c for c in chunks if c.kind == "table"]
    assert len(tables) == 1
    # header travels with the data -- this is what makes the fact retrievable
    assert "Grade" in tables[0].text and "9,900" in tables[0].text


def test_heading_is_prefixed_to_prose_chunks():
    doc = _doc([Block("heading", "3. Provisions"),
                Block("paragraph", "The allowance shall not exceed 25% of basic salary. " * 6)])
    chunks = chunk_document(doc, doc_meta={"title": "Housing Policy"})
    assert all("Housing Policy" in c.text and "Provisions" in c.text
               for c in chunks if c.kind == "prose")


def test_chunk_ids_are_stable_across_runs():
    doc = _doc([Block("paragraph", "text " * 200)])
    a = [c.chunk_id for c in chunk_document(doc)]
    b = [c.chunk_id for c in chunk_document(doc)]
    assert a == b and len(set(a)) == len(a)


def test_no_empty_chunks_and_mid_sentence_is_low():
    doc = _doc([Block("heading", "1. Scope"),
                Block("paragraph", "Sentence one is complete. Sentence two is complete. " * 20)])
    chunks = chunk_document(doc)
    stats = chunk_quality_stats(chunks)
    assert stats["empty_chunks"] == 0
    assert stats["mid_sentence_pct"] < 20


def test_table_serialisation_survives_ragged_rows():
    md = _serialise_table([["A", "B", "C"], ["1"], ["2", "3"]])
    assert md.count("\n") == 3
