#!/usr/bin/env python3
"""
build_slides.py -- add the corpus / benchmark / pre-work / governance slides to
the SDA-AIE-214 instructor deck, in the deck's own visual language.

Design system reverse-engineered from the existing 158 slides:
    canvas          13.333 x 7.5 in
    title           Calibri 24 bold  #1D2A5C  at (0.55, 0.30, 10.55, 0.62)
    arabic subtitle Calibri 13       #00A79D  at (0.55, 0.94, 10.55, 0.34)
    accent rule     0.85 x 0.04      #00A79D  at (0.55, 1.36)
    content band    y = 1.62 .. 5.80
    callout         rounded rect     #E6F5F4  at (0.55, 5.95, 12.23, 0.80)
    footer          Calibri 8        label #00A79D bold + text #6E7B8A
    page number     Calibri 8 right  #6E7B8A  at (12.35, 7.14)
    table header    #1D2A5C fill, white bold 11pt; body #F2F6F8, 10.5pt
    accent sequence #00A79D #29ABE2 #F7941D #8CC63F #1D2A5C

New slides are INSERTED at their teaching position, not appended, and every
page number in the deck is renumbered afterwards.
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else
           "/mnt/user-data/uploads/Building Retrieval-Augmented Generation Systems/"
           "SDA-AIE-214_Instructor_Training_Deck.pptx")
DST = Path(sys.argv[2] if len(sys.argv) > 2 else
           "/home/claude/SDA-AIE-214_Instructor_Training_Deck_v2.pptx")

NAVY = RGBColor(0x1D, 0x2A, 0x5C)
TEAL = RGBColor(0x00, 0xA7, 0x9D)
BLUE = RGBColor(0x29, 0xAB, 0xE2)
ORANGE = RGBColor(0xF7, 0x94, 0x1D)
GREEN = RGBColor(0x8C, 0xC6, 0x3F)
GREY = RGBColor(0x6E, 0x7B, 0x8A)
INK = RGBColor(0x2B, 0x2B, 0x2B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BODYFILL = RGBColor(0xF2, 0xF6, 0xF8)
CALLOUT = RGBColor(0xE6, 0xF5, 0xF4)
ACCENTS = [TEAL, BLUE, ORANGE, GREEN, NAVY]

FONT = "Calibri"


# --------------------------------------------------------------------- utils
def txbox(slide, l, t, w, h, *, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tf


def run(para, text, *, size=11, bold=False, color=INK, italic=False):
    r = para.add_run()
    r.text = text
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    return r



_BOLD_SEG = None


def rich(para, text, *, size=11, color=INK, bold_color=NAVY):
    """Render `**bold**` segments as real runs.

    Markdown-style emphasis in a table cell is convenient to author and looks
    like a typo on a projector, so it gets parsed rather than printed.
    """
    global _BOLD_SEG
    if _BOLD_SEG is None:
        import re as _re
        _BOLD_SEG = _re.compile(r"\*\*(.+?)\*\*", _re.S)
    pos = 0
    for m in _BOLD_SEG.finditer(text):
        if m.start() > pos:
            run(para, text[pos:m.start()], size=size, color=color)
        run(para, m.group(1), size=size, bold=True, color=bold_color)
        pos = m.end()
    if pos < len(text):
        run(para, text[pos:], size=size, color=color)
    if not para.runs:
        run(para, text, size=size, color=color)


def rect(slide, l, t, w, h, color, *, shape=MSO_SHAPE.RECTANGLE):
    sp = slide.shapes.add_shape(shape, Inches(l), Inches(t), Inches(w), Inches(h))
    sp.fill.solid()
    sp.fill.fore_color.rgb = color
    sp.line.fill.background()
    sp.shadow.inherit = False
    return sp


def chrome(slide, title_en, title_ar, footer_label, logo_blob=None):
    tf = txbox(slide, 0.55, 0.30, 10.55, 0.62)
    run(tf.paragraphs[0], title_en, size=24, bold=True, color=NAVY)
    tf2 = txbox(slide, 0.55, 0.94, 10.55, 0.34)
    p = tf2.paragraphs[0]
    run(p, title_ar, size=13, color=TEAL)
    rect(slide, 0.55, 1.36, 0.85, 0.04, TEAL)
    if logo_blob:
        slide.shapes.add_picture(logo_blob(), Inches(11.62), Inches(0.34),
                                 Inches(1.18), Inches(0.29))
    tf3 = txbox(slide, 0.55, 7.14, 9.50, 0.24)
    p3 = tf3.paragraphs[0]
    run(p3, f"{footer_label}   ", size=8, bold=True, color=TEAL)
    run(p3, "SDA-AIE-214 · Building RAG Systems · SDAIA Academy", size=8, color=GREY)
    tf4 = txbox(slide, 12.35, 7.14, 0.45, 0.24)
    tf4.paragraphs[0].alignment = PP_ALIGN.RIGHT
    r = run(tf4.paragraphs[0], "0", size=8, color=GREY)
    slide._page_number_run = r          # renumbered later
    return slide


def callout(slide, label, text, top=5.95, height=0.80):
    rect(slide, 0.55, top, 12.23, height, CALLOUT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    tf = txbox(slide, 0.80, top, 11.73, height, anchor=MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]
    run(p, f"{label}   ", size=10.5, bold=True, color=TEAL)
    run(p, text, size=11.5, color=INK)


def table(slide, headers, rows, *, top=1.62, widths=None, height=None,
          font_size=10.5, header_size=11, left=0.55, width=12.23):
    nrows, ncols = len(rows) + 1, len(headers)
    h = height or min(0.4567 * nrows, 4.1)
    shape = slide.shapes.add_table(nrows, ncols, Inches(left), Inches(top),
                                   Inches(width), Inches(h))
    tbl = shape.table
    tbl.first_row = True
    if widths:
        total = sum(widths)
        for i, w in enumerate(widths):
            tbl.columns[i].width = Inches(width * w / total)
    for j, htxt in enumerate(headers):
        c = tbl.cell(0, j)
        c.fill.solid()
        c.fill.fore_color.rgb = NAVY
        c.margin_left = c.margin_right = Inches(0.08)
        tf = c.text_frame
        tf.word_wrap = True
        run(tf.paragraphs[0], htxt, size=header_size, bold=True, color=WHITE)
    for i, r in enumerate(rows, start=1):
        for j, val in enumerate(r):
            c = tbl.cell(i, j)
            c.fill.solid()
            c.fill.fore_color.rgb = BODYFILL
            c.margin_left = c.margin_right = Inches(0.08)
            tf = c.text_frame
            tf.word_wrap = True
            rich(tf.paragraphs[0], val, size=font_size)
    return tbl


def numbered_list(slide, items, *, top=1.90, gap=1.03, badge=0.44, text_size=12):
    # Guard against the commonest layout bug in this deck: a five-item list at
    # the default gap runs its last badge underneath the WHY IT MATTERS callout.
    if top + len(items) * gap > 5.85:
        gap = (5.85 - top) / len(items)
    """The deck's signature numbered-badge list (see slide 12)."""
    for i, (head, body) in enumerate(items):
        y = top + i * gap
        rect(slide, 0.55, y, badge, badge, ACCENTS[i % len(ACCENTS)])
        tf = txbox(slide, 0.55, y, badge, badge, anchor=MSO_ANCHOR.MIDDLE)
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        run(tf.paragraphs[0], str(i + 1), size=13, bold=True, color=WHITE)
        tf2 = txbox(slide, 1.25, y - 0.11, 11.53, gap - 0.15, anchor=MSO_ANCHOR.MIDDLE)
        p = tf2.paragraphs[0]
        run(p, f"{head}   ", size=text_size, bold=True, color=NAVY)
        run(p, body, size=text_size, color=INK)


def stat_row(slide, stats, *, top=1.90, height=1.35):
    """Big-number tiles, as on slides 18/37/54."""
    n = len(stats)
    gap = 0.22
    w = (12.23 - gap * (n - 1)) / n
    for i, (big, label, sub) in enumerate(stats):
        x = 0.55 + i * (w + gap)
        rect(slide, x, top, w, height, BODYFILL)
        rect(slide, x, top, w, 0.05, ACCENTS[i % len(ACCENTS)])
        tf = txbox(slide, x + 0.18, top + 0.16, w - 0.36, 0.55)
        run(tf.paragraphs[0], big, size=26, bold=True, color=NAVY)
        tf2 = txbox(slide, x + 0.18, top + 0.72, w - 0.36, 0.28)
        run(tf2.paragraphs[0], label, size=10.5, bold=True, color=TEAL)
        tf3 = txbox(slide, x + 0.18, top + 0.98, w - 0.36, 0.30)
        run(tf3.paragraphs[0], sub, size=9.5, color=GREY)


def bullets(slide, items, *, top=1.75, left=0.55, width=12.23, size=12.5, gap=0.10):
    tf = txbox(slide, left, top, width, 4.0)
    first = True
    for it in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_after = Pt(gap * 72)
        run(p, "▪  ", size=size, bold=True, color=TEAL)
        if isinstance(it, tuple):
            run(p, f"{it[0]}  ", size=size, bold=True, color=NAVY)
            run(p, it[1], size=size, color=INK)
        else:
            run(p, it, size=size, color=INK)
    return tf


# --------------------------------------------------------------- slide bodies
def s_corpus_is_real(slide):
    chrome(slide, "Dalil's Corpus Is Real",
           "مدونة «دليل» مبنية على وثائق حقيقية", "DAY 1 · SETUP")
    numbered_list(slide, [
        ("Layer A — 17 published SDAIA / NDMO documents.",
         "PDPL and its Implementing Regulation · Data Transfer Regulation · "
         "Classification, Sharing, Open Data and Monetization policies · AI Ethics "
         "Principles · Generative AI Guidelines · AI Adoption Framework"),
        ("Layer B — 134 synthetic internal documents.",
         "A fictional adopter of those rules, supplying only what public regulation "
         "cannot: access tiers, superseded editions, scanned Arabic, tabular facts"),
        ("Every Layer B document cites a Layer A instrument by title.",
         "That is what makes them one corpus — and it creates the multi-hop question "
         "class that no single chunk can answer"),
        ("Invented corpora flatter the systems built on them.",
         "One author, one vocabulary, one structure, and the same person wrote the "
         "questions and the answers"),
        ("This is the corpus your organisation is already bound by.",
         "Four days debugging retrieval over regulation you will be asked about the "
         "month you get back to your desk"),
    ], top=1.85, gap=1.00)
    callout(slide, "WHY IT MATTERS",
            "You are not doing an exercise. You are building the index you will be "
            "asked for — over the instruments that govern the assistant you build.")


def s_layer_a(slide):
    chrome(slide, "Layer A — The SDAIA Regulatory Corpus",
           "الطبقة الأولى: المدونة التنظيمية لسدايا", "DAY 1 · SETUP")
    table(slide,
          ["Tier", "Documents", "Teaches"],
          [["Law", "Personal Data Protection Law (RD M/19, amended M/148)",
            "identifier queries · article-level citation"],
           ["Regulation", "PDPL Implementing Regulation · Data Transfer Regulation",
            "multi-hop: law → regulation"],
           ["National data", "Classification · Sharing · Open Data · Monetization policies",
            "tables (F1) · near-duplicate confusion (F5)"],
           ["Guidelines", "Anonymisation · Destruction · Transfer Risk Assessment",
            "procedure extraction · three-document hops"],
           ["AI", "AI Ethics Principles · GenAI Guidelines (Gov + Public) · "
                  "AI Adoption Framework · Deepfakes",
            "enumeration · governance of the system you are building"],
           ["Workforce", "National Occupational Standards for Data & AI",
            "long enumeration retrieval"]],
          widths=[1.6, 6.4, 4.2], top=1.70, height=3.4)
    tf = txbox(slide, 0.55, 5.25, 12.23, 0.55)
    p = tf.paragraphs[0]
    run(p, "The URLs move.  ", size=11.5, bold=True, color=ORANGE)
    run(p, "The fetcher tries each candidate, falls back to link discovery, then "
           "records UNRESOLVED and continues. A partially resolved Layer A is a "
           "supported state — validate_corpus.py prints which labs are affected.",
        size=11.5, color=INK)
    callout(slide, "T-1 WEEK",
            "make corpus-fetch && make corpus-verify — then commit corpus/LOCK.json. "
            "Cohorts that index different bytes cannot compare numbers.")


def s_layer_b(slide):
    chrome(slide, "Layer B — What Public Regulation Cannot Teach",
           "الطبقة الثانية: ما لا تستطيع الأنظمة المنشورة تعليمه", "DAY 1 · SETUP")
    table(slide,
          ["Missing from Layer A", "Layer B supplies", "Serves"],
          [["Access control — everything public is public",
            "48 restricted + 62 internal documents across 6 departments",
            "M5 filter · capstone “0 leaks”"],
           ["Supersession — only current editions are published",
            "12 matched v1 / v2 circular pairs; v2 lands only in corpus_v2",
            "F8 · the Day-4 staleness drill"],
           ["Scanned Arabic — SDAIA PDFs have clean text layers",
            "22 image-only Arabic policy PDFs + hand-quality transcripts",
            "F1 · the OCR path and CER gate"],
           ["Tabular facts — few retrievable numeric tables",
            "8 XLSX allowance tables, plus in-PDF tables",
            "F1 · “the table nobody could retrieve”"]],
          widths=[4.0, 5.2, 3.0], top=1.70, height=3.0, font_size=11)
    tf = txbox(slide, 0.55, 4.95, 12.23, 0.85)
    p = tf.paragraphs[0]
    run(p, "Fictional, and marked as such.  ", size=11.5, bold=True, color=NAVY)
    run(p, "Every generated file carries an X-Dalil-Synthetic metadata marker and a "
           "visible bilingual disclaimer. Generation is deterministic from a seed, so "
           "every cohort worldwide indexes byte-identical documents.",
        size=11.5, color=INK)
    callout(slide, "THE DESIGN RULE",
            "Layer B supplies exactly the four gaps and nothing else. Anything a real "
            "regulator publishes, we use the real thing.")


def s_one_corpus(slide):
    chrome(slide, "One Corpus, Not Two",
           "مدونة واحدة لا مدونتان", "DAY 4 · M7")
    tf = txbox(slide, 0.55, 1.75, 12.23, 0.6)
    p = tf.paragraphs[0]
    run(p, "The question class that justifies the whole design:", size=13, bold=True,
        color=NAVY)
    rect(slide, 0.55, 2.35, 12.23, 0.95, BODYFILL)
    rect(slide, 0.55, 2.35, 0.06, 0.95, ORANGE)
    tf2 = txbox(slide, 0.85, 2.50, 11.7, 0.7, anchor=MSO_ANCHOR.MIDDLE)
    run(tf2.paragraphs[0],
        "“Our Data Export Procedure requires a transfer risk assessment before "
        "exporting personal data — which SDAIA instrument imposes that, and what does "
        "it require the assessment to cover?”", size=13.5, italic=True, color=NAVY)
    for i, (label, where, what) in enumerate([
        ("HOP 1", "Layer B — NDSA Data Export Procedure (internal, DOCX)",
         "finds the internal requirement and the instrument it cites"),
        ("HOP 2", "Layer A — SDAIA Data Transfer Regulation + Risk Assessment Guideline",
         "finds what the assessment must actually cover"),
    ]):
        y = 3.55 + i * 1.02
        rect(slide, 0.55, y, 1.05, 0.72, ACCENTS[i])
        tfl = txbox(slide, 0.55, y, 1.05, 0.72, anchor=MSO_ANCHOR.MIDDLE)
        tfl.paragraphs[0].alignment = PP_ALIGN.CENTER
        run(tfl.paragraphs[0], label, size=11, bold=True, color=WHITE)
        tfr = txbox(slide, 1.80, y, 10.98, 0.72, anchor=MSO_ANCHOR.MIDDLE)
        p = tfr.paragraphs[0]
        run(p, where + "\n", size=12, bold=True, color=NAVY)
        p2 = tfr.add_paragraph()
        run(p2, what, size=11.5, color=INK)
    callout(slide, "NO SINGLE CHUNK ANSWERS IT",
            "That is Module 7's entire thesis — demonstrated on real instruments, "
            "not on a toy example built to make decomposition look necessary.")


def s_corpus_numbers(slide):
    chrome(slide, "Corpus by the Numbers — Measured, Not Estimated",
           "المدونة بالأرقام: قياس لا تقدير", "DAY 1 · SETUP")
    stat_row(slide, [
        ("151", "documents", "17 real SDAIA · 134 synthetic internal"),
        ("41.5%", "naive mid-sentence", "→ 4.1% structure-aware"),
        ("0 → 56", "tables surviving", "naive chunking destroys all of them"),
        ("0.084 → 0.053", "OCR CER", "naive settings → tuned; gate 0.06"),
    ], top=1.80)
    table(slide,
          ["BM25 alone, by query class", "n", "recall@10", "What it means"],
          [["identifier", "60", "**1.000**", "exact tokens — dense retrieval cannot do this"],
           ["tabular", "24", "**1.000**", "the figure lives beside its header"],
           ["procedural", "20", "**0.300**", "paraphrase — lexical matching is helpless"],
           ["factoid", "22", "**0.239**", "paraphrase, often across languages"],
           ["aggregate", "138", "0.777", "hides both of the rows above"]],
          widths=[3.4, 0.9, 1.6, 6.3], top=3.45, height=2.3, font_size=11)
    callout(slide, "THE COURSE IN ONE TABLE",
            "Lexical retrieval is perfect at exactly what dense retrieval cannot do, "
            "and helpless at everything else. Modules 3 and 4 are that sentence, "
            "measured.")


def s_prework(slide):
    chrome(slide, "Before Day 2 — Required Pre-Work",
           "العمل التحضيري المطلوب قبل اليوم الثاني", "PRE-COURSE")
    tf = txbox(slide, 0.55, 1.72, 12.23, 0.5)
    p = tf.paragraphs[0]
    run(p, "Chroma · Advanced Retrieval for AI", size=15, bold=True, color=NAVY)
    run(p, "   ~52 minutes · DeepLearning.AI", size=12, color=GREY)
    table(slide,
          ["Lesson", "Required", "Maps to", "What Day 2 then adds"],
          [["Pitfalls of retrieval — when vector search fails", "**YES**", "M4 §1",
            "the identifier failure specifically, priced per query class"],
           ["Cross-encoder re-ranking", "**YES**", "M4 §3",
            "the two-stage budget as an economic argument"],
           ["Embeddings-based retrieval", "optional", "M3",
            "bilingual model choice, measured; payload filters; the ef curve"],
           ["Query expansion", "optional", "M7 §2",
            "routing — expansion only where it pays"]],
          widths=[4.6, 1.2, 1.2, 5.2], top=2.35, height=2.1, font_size=11)
    tf2 = txbox(slide, 0.55, 4.70, 12.23, 1.05)
    p = tf2.paragraphs[0]
    run(p, "We will not re-teach it.  ", size=12.5, bold=True, color=ORANGE)
    run(p, "Day 2 Hour 3 opens by assuming it: “You saw last night that semantic "
           "search misses exact tokens. Here is what that costs on a real Saudi "
           "regulatory corpus, by query class.” The identifier row lands ten times "
           "harder on a room that already knows the mechanism.", size=12.5, color=INK)
    callout(slide, "BRING TO DAY 2 HOUR 1",
            "Five one-sentence answers (prework/readiness_check.md). Not graded — "
            "but you will be asked, and question 5 comes back on Day 4.")


def s_dlai_companion(slide):
    chrome(slide, "Day 3 Companion — and the Metric Name Map",
           "المقرر المرافق لليوم الثالث وخريطة أسماء المقاييس", "DAY 3 · M6")
    tf = txbox(slide, 0.55, 1.70, 12.23, 0.45)
    p = tf.paragraphs[0]
    run(p, "LlamaIndex · Building and Evaluating Advanced RAG", size=14.5, bold=True,
        color=NAVY)
    run(p, "   ~1h55m with code · assigned end of Day 2", size=11.5, color=GREY)
    table(slide,
          ["DLAI lesson", "Our module", "Relationship"],
          [["Sentence-window retrieval", "M2 chunking · M5 context",
            "same problem, two answers — theirs widens the window, ours prepends the heading"],
           ["Auto-merging retrieval", "M2 chunking",
            "hierarchical merge vs structure-aware split — decide with evidence, not preference"],
           ["RAG triad · context relevance", "context_precision", "**same metric, different name**"],
           ["RAG triad · groundedness", "**faithfulness**", "**same metric, different name**"],
           ["RAG triad · answer relevance", "answer_relevancy", "**same metric, different name**"],
           ["TruLens evaluation", "RAGAS harness + gate",
            "different tool, same discipline — we add the pinned judge and the gate that fails the build"]],
          widths=[3.9, 2.9, 6.2], top=2.30, height=3.1, font_size=11)
    callout(slide, "THE POINT OF THIS TABLE",
            "Every RAG framework renames the same four measurements. Map RAGAS ↔ "
            "TruLens ↔ the RAG triad once, and you will never be lost by whichever one "
            "your employer standardised on.")


def s_miracl(slide):
    chrome(slide, "Reality Check — MIRACL Arabic",
           "اختبار الواقع: مقياس ميراكل العربي", "DAY 2 · M3")
    tf = txbox(slide, 0.55, 1.72, 12.23, 0.75)
    p = tf.paragraphs[0]
    run(p, "Our Arabic number is self-graded.  ", size=13, bold=True, color=ORANGE)
    run(p, "We wrote the corpus and we wrote the labels. MIRACL-ar is human-annotated "
           "Arabic retrieval, by people with no stake in this course. Fifteen minutes "
           "to find out whether the last two days were real.", size=13, color=INK)
    table(slide,
          ["Your Dalil Arabic recall", "Your MIRACL-ar recall@100", "What it means"],
          [["high", "in the published range for your model",
            "your pipeline is sound — carry on"],
           ["high", "far below the range",
            "**the corpus was flattering you** — your queries and passages share "
            "vocabulary a real user's phrasing would not"],
           ["low", "in the published range",
            "the pipeline is fine; ingestion or normalisation is losing the Arabic"]],
          widths=[3.0, 3.6, 6.4], top=2.75, height=1.9, font_size=11.5)
    tf2 = txbox(slide, 0.55, 4.90, 12.23, 0.5)
    run(tf2.paragraphs[0], "make bench-miracl", size=13, bold=True, color=TEAL)
    callout(slide, "RUN IT AS A SIDEBAR, NOT A LAB",
            "The middle row is the one worth the fifteen minutes — it is the only way "
            "to discover that a good number came from an easy corpus.")


def s_beir(slide):
    chrome(slide, "Validate the Ruler Before You Measure With It — BEIR",
           "تحقق من أداة القياس قبل استخدامها", "DAY 3 · M6")
    numbered_list(slide, [
        ("One shape, eighteen datasets, nine task types.",
         "Every BEIR dataset ships corpus + queries + qrels in the same structure"),
        ("So your metric code runs unmodified.",
         "recall@k, MRR and nDCG written once for Dalil work everywhere — that "
         "uniformity is why BEIR belongs in the metrics lab specifically"),
        ("Point YOUR implementation at a published baseline.",
         "If your nDCG@10 on SciFact with a known model is far off the published "
         "figure, the bug is in your metric code"),
        ("You have just avoided grading your capstone with a broken ruler.",
         "scifact (tiny, graded) · nfcorpus (vocabulary mismatch) · trec-covid "
         "(0/1/2 grades, where nDCG and recall visibly diverge)"),
    ], top=2.00, gap=1.02)
    tf = txbox(slide, 0.55, 5.35, 12.23, 0.45)
    run(tf.paragraphs[0], "make bench-beir", size=13, bold=True, color=TEAL)
    callout(slide, "FIFTEEN MINUTES, BEFORE LAB 6",
            "Nobody discovers a broken metric implementation while grading their own "
            "capstone. They discover it here, or they never discover it.")


def s_techqa(slide):
    chrome(slide, "The Only Benchmark That Grades Refusal — TechQA",
           "المقياس الوحيد الذي يقيّم الامتناع", "DAY 3 · M6")
    tf = txbox(slide, 0.55, 1.70, 12.23, 0.72)
    p = tf.paragraphs[0]
    run(p, "Every other benchmark rewards retrieving something.  ", size=13,
        bold=True, color=ORANGE)
    run(p, "A meaningful share of TechQA's questions are deliberately unanswerable "
           "from the supplied corpus — which is the behaviour the capstone requires "
           "and production support assistants fail at.", size=13, color=INK)
    table(slide,
          ["Metric", "Measures", "Gaming risk"],
          [["recall@k · nDCG@10", "retrieval, on the answerable subset only", "—"],
           ["refusal_recall", "unanswerable questions correctly refused",
            "trivially gamed by refusing everything"],
           ["false_answer_rate", "unanswerable questions answered anyway — **F7**",
            "the number that ends careers"],
           ["**over_refusal_rate**", "**answerable questions wrongly refused**",
            "**the companion that stops the gaming**"]],
          widths=[2.7, 6.0, 4.3], top=2.60, height=2.0, font_size=11.5)
    tf2 = txbox(slide, 0.55, 4.80, 12.23, 0.6)
    p = tf2.paragraphs[0]
    run(p, "A system that refuses everything scores 1.00 on refusal recall and is "
           "worthless. ", size=12.5, color=INK)
    run(p, "That is the anti-pattern the capstone rubric caps at 70%.", size=12.5,
        bold=True, color=NAVY)
    callout(slide, "MEASURED ON THE SHIPPED FIXTURE",
            "At the default τ, false_answer_rate = 1.00 — the baseline answers every "
            "unanswerable question. Now go choose a threshold.")


def s_tau_curve(slide):
    chrome(slide, "A Refusal Threshold Is a Curve, Not a Number",
           "عتبة الامتناع منحنى لا رقم", "DAY 3 · M5")
    table(slide,
          ["τ", "refusal_recall", "over_refusal", "Who would choose this point"],
          [["0.10", "low", "≈ 0", "nobody — the system answers everything"],
           ["0.35", "moderate", "low", "an internal helpdesk: tickets cost less than silence"],
           ["0.55", "high", "moderate", "a compliance assistant preparing audit responses"],
           ["0.80", "very high", "high", "a public citizen-facing service: a wrong answer reaches the press"]],
          widths=[0.8, 2.2, 2.0, 7.2], top=1.75, height=2.1, font_size=11.5)
    tf = txbox(slide, 0.55, 4.05, 12.23, 1.6)
    for i, (b, t) in enumerate([
        ("The engineer owns the measurement.",
         "the sweep, the curve, both rates at every point"),
        ("The business or risk owner chooses the point.",
         "τ encodes a stated risk appetite, not a technical constant"),
        ("Their name goes in DECISIONS.md next to the value.",
         "if the decision has no owner, it was not made — it was defaulted"),
    ]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(7)
        run(p, "▪  ", size=12.5, bold=True, color=TEAL)
        run(p, f"{b}  ", size=12.5, bold=True, color=NAVY)
        run(p, t, size=12.5, color=INK)
    tf2 = txbox(slide, 0.55, 5.45, 12.23, 0.4)
    run(tf2.paragraphs[0], "make tau-sweep", size=13, bold=True, color=TEAL)
    callout(slide, "THE QUESTION THAT ENDS THE DISCUSSION",
            "“Your τ makes the system refuse 8% of answerable questions. Who hears "
            "about those — and how would you ever find out?”")


def s_pdpl(slide):
    chrome(slide, "PDPL and the Architecture Choice",
           "نظام حماية البيانات الشخصية وأثره على قرار البنية", "DAY 3 · M5")
    tf = txbox(slide, 0.55, 1.70, 12.23, 0.62)
    p = tf.paragraphs[0]
    run(p, "“RAG or fine-tune” is not only an engineering question.  ", size=13,
        bold=True, color=NAVY)
    run(p, "It decides where personal data lives — in retrievable documents with "
           "access control, or baked irreversibly into model weights.", size=13,
        color=INK)
    table(slide,
          ["Obligation", "Retrieval architecture", "Weights"],
          [["Erasure of personal data on request",
            "delete the document, re-index — provable",
            "**not achievable without retraining**"],
           ["Access control by role and department",
            "payload filter at retrieval, re-asserted at context",
            "**weights cannot enforce who may see what**"],
           ["Attribution — which document produced this answer",
            "chunk-level citation an auditor can follow",
            "**no mechanism**"],
           ["Freshness against a changing instrument",
            "re-index in minutes; lifecycle filtering",
            "retraining cadence can never match regulatory cadence"],
           ["Cross-border transfer control",
            "the corpus and index have a location; a transfer risk assessment applies to it",
            "the same data is diffused into parameters"]],
          widths=[4.0, 5.4, 3.6], top=2.45, height=2.7, font_size=11)
    callout(slide, "IN YOUR CAPSTONE",
            "DECISIONS.md needs a short PDPL paragraph: where personal data lives, why "
            "retrieval keeps it deletable and access-controlled, and what would require "
            "a transfer risk assessment.")


def s_assets(slide):
    chrome(slide, "The Asset Repository — Every Lab Command Has a Name",
           "مستودع الأصول: لكل خطوة أمر واضح", "DAY 1 · SETUP")
    table(slide,
          ["Day", "Commands", "Produces"],
          [["T-1 week", "make corpus-fetch · corpus-verify · corpus · eval-sets",
            "Layer A + LOCK.json, Layer B, all evaluation sets"],
           ["T-2 days", "make doctor",
            "24 environment checks, each printing its own fix"],
           ["Day 1", "make ingest-naive · probe SET=failure_gallery · ingest",
            "the baseline, the failure gallery, the real pipeline"],
           ["Day 2", "make qdrant · index · eval-retrieval · ablation · ef-sweep · bench-miracl",
            "the per-class table and the recall/latency curve"],
           ["Day 3", "make eval-golden · eval-ragas · gate · baseline · redteam · tau-sweep",
            "RAGAS report, committed baseline, CI gate, refusal curve"],
           ["Day 4", "make ingest-v2 · staleness · report · demo",
            "the staleness verdict, EVALUATION.md, the six-minute demo"]],
          widths=[1.3, 6.6, 5.1], top=1.70, height=3.1, font_size=11)
    tf = txbox(slide, 0.55, 4.95, 12.23, 0.85)
    p = tf.paragraphs[0]
    run(p, "All of it runs offline.  ", size=12.5, bold=True, color=NAVY)
    run(p, "No Docker, no GPU, no model download and no gateway key are required for "
           "any of it to execute — the labs use the real stack, but nothing is "
           "blocked on it. A 20-hour course cannot afford to lose an hour to "
           "infrastructure.", size=12.5, color=INK)
    callout(slide, "COMMANDS NOBODY REMEMBERS",
            "…are commands nobody reproduces, and an unreproducible benchmark is not "
            "evidence. On Day 4 a stranger must reach a working assistant with "
            "make demo in ten minutes.")


def s_no_silent_degradation(slide):
    chrome(slide, "Nothing Degrades Silently",
           "لا تدهور صامت في أي مرحلة", "DAY 1 · SETUP")
    tf = txbox(slide, 0.55, 1.72, 12.23, 0.55)
    p = tf.paragraphs[0]
    run(p, "The worst outcome in this course ", size=13.5, color=INK)
    run(p, "is a participant trusting a number produced by a stage that never ran.",
        size=13.5, bold=True, color=ORANGE)
    table(slide,
          ["If this is missing", "The system does NOT pretend", "How you know"],
          [["cross-encoder reranker", "returns the input order unchanged",
            "reranked: false — in the telemetry"],
           ["embedding model", "falls back to BM25 only",
            "a warning inside the report's notes field"],
           ["evaluation judge", "runs lexical proxy metrics",
            "judge: offline-proxy — plus a warning in the JSON"],
           ["a real embedding model in CI", "uses the hash-384 test fixture",
            "model: hash-384 — stamped in every report"],
           ["network for a benchmark", "uses the bundled fixture",
            "mode: sample — “not comparable to published numbers”"],
           ["Layer A documents", "labs run on Layer B alone",
            "validate_corpus.py prints a per-lab readiness verdict"]],
          widths=[3.3, 5.0, 4.4], top=2.45, height=2.9, font_size=11)
    callout(slide, "AND IN THE CAPSTONE",
            "Presenting substitute-stamped numbers as results is an automatic fail on "
            "that criterion. Every substitute writes its own name into the file — so "
            "doing it is a choice, never an accident.")


def s_wall_of_numbers(slide):
    chrome(slide, "What Changed, and What It Cost",
           "ما الذي تغيّر وما كلفته", "CLOSING")
    table(slide,
          ["Change", "Added hours", "What it buys"],
          [["Real SDAIA corpus (Layer A) + synthetic overlay (Layer B)", "0",
            "authority, heterogeneity, cross-layer multi-hop, and a corpus participants "
            "are legally bound by"],
           ["MIRACL-ar sidebar (Day 2)", "0 — fits the Lab 3 buffer",
            "an independent check on the Arabic claim"],
           ["BEIR sidebar (Day 3)", "0 — fits the M6 lecture",
            "validation of the participant's own metric code"],
           ["TechQA + τ sweep (Day 3)", "0 — replaces hand-waving in the red-team hour",
            "the only public measurement of refusal, and a defensible threshold"],
           ["Chroma pre-work (required)", "0 in class · ~52 min before",
            "Day 2 starts from the mechanism instead of teaching it"],
           ["LlamaIndex companion (Day 3)", "0 in class · optional",
            "the same ideas in a second vocabulary — and the metric name map"]],
          widths=[4.6, 2.8, 5.4], top=1.70, height=3.3, font_size=11)
    tf = txbox(slide, 0.55, 5.15, 12.23, 0.6)
    p = tf.paragraphs[0]
    run(p, "Net schedule impact: zero added hours.  ", size=13, bold=True, color=NAVY)
    run(p, "Everything fits inside existing buffers, and the τ sweep replaces the "
           "arm-waving that used to occupy the same slot.", size=13, color=INK)
    callout(slide, "THE ONE-LINE VERSION",
            "Same four days, same rubric — measured against real regulation, with "
            "independent instruments, and every number reproducible by a stranger "
            "with one command.")


NEW_SLIDES = [
    # (builder, insert-after title fragment, fallback index)
    (s_corpus_is_real,        "Dalil: The Golden-Thread Project"),
    (s_layer_a,               None),
    (s_layer_b,               None),
    (s_corpus_numbers,        None),
    (s_prework,               "Assessment & Certification"),
    (s_assets,                None),
    (s_no_silent_degradation, None),
    (s_miracl,                "Benchmarks After Module 3"),
    (s_beir,                  "The Golden Set: Your Measuring Instrument"),
    (s_techqa,                None),
    (s_tau_curve,             None),
    (s_dlai_companion,        None),
    (s_pdpl,                  "Access Control: Defence in Depth"),
    (s_one_corpus,            "Decomposition and Multi-Hop Retrieval"),
    (s_wall_of_numbers,       "Learning Outcomes — Achieved"),
]


# ------------------------------------------------------------------- assembly
def blank_layout(prs):
    """The deck has a single 'DEFAULT' layout carrying only the background."""
    return prs.slide_masters[0].slide_layouts[0]


def strip_placeholders(slide):
    for ph in list(slide.placeholders):
        ph._element.getparent().remove(ph._element)


def logo_extractor(prs):
    """Reuse the deck's own logo image rather than shipping a second copy."""
    import io
    for s in prs.slides:
        for sh in s.shapes:
            if sh.shape_type == 13:               # PICTURE
                blob = sh.image.blob
                return lambda: io.BytesIO(blob)
    return None


def title_of(slide) -> str:
    for sh in slide.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip():
            return sh.text_frame.text.strip().split("\n")[0]
    return ""


def move_slide(prs, from_idx, to_idx):
    sldIdLst = prs.slides._sldIdLst
    ids = list(sldIdLst)
    el = ids[from_idx]
    sldIdLst.remove(el)
    sldIdLst.insert(to_idx, el)


def renumber(prs):
    """Rewrite every page-number textbox: the one at x≈12.35, y≈7.14, right-aligned."""
    from pptx.util import Emu
    fixed = 0
    for i, slide in enumerate(prs.slides, start=1):
        for sh in slide.shapes:
            if not sh.has_text_frame:
                continue
            if abs(Emu(sh.left).inches - 12.35) < 0.12 and abs(Emu(sh.top).inches - 7.14) < 0.12:
                txt = sh.text_frame.text.strip()
                if txt.isdigit() or txt == "0":
                    for para in sh.text_frame.paragraphs:
                        for r in para.runs:
                            r.text = ""
                        if para.runs:
                            para.runs[0].text = str(i)
                    fixed += 1
                    break
    return fixed


def main() -> int:
    prs = Presentation(str(SRC))
    n_before = len(prs.slides)
    layout = blank_layout(prs)
    logo = logo_extractor(prs)

    titles = [title_of(s) for s in prs.slides]

    # Build every new slide at the end first, then move it into position. Doing
    # it in two passes keeps the anchor indices stable while we search for them.
    built = []
    for builder, anchor in NEW_SLIDES:
        slide = prs.slides.add_slide(layout)
        strip_placeholders(slide)
        # inject the logo helper into chrome() via a default-arg closure
        global _LOGO
        _LOGO = logo
        builder(slide)
        if logo:
            slide.shapes.add_picture(logo(), Inches(11.62), Inches(0.34),
                                     Inches(1.18), Inches(0.29))
        built.append((slide, anchor))

    # Resolve insert positions against the ORIGINAL slide order.
    positions = []
    cursor = None
    for slide, anchor in built:
        if anchor:
            idx = next((i for i, t in enumerate(titles) if anchor.lower() in t.lower()), None)
            if idx is None:
                print(f"  [warn] anchor not found: {anchor!r} — appending in place")
                cursor = (cursor if cursor is not None else len(titles) - 1)
            else:
                cursor = idx
        cursor = (cursor if cursor is not None else len(titles) - 1)
        cursor += 1
        positions.append(cursor)
        titles.insert(cursor, title_of(slide))

    # Move each built slide (which currently sits at the end) into its slot.
    total = len(prs.slides)
    n_new = len(built)
    for k, target in enumerate(positions):
        src_idx = total - n_new + k          # where the k-th built slide now sits
        # account for slides already moved out from behind it
        moved_before = sum(1 for p in positions[:k] if p <= src_idx)
        move_slide(prs, src_idx - 0, target)
        # after a move, everything shifts; recompute by locating it again next loop
        total = len(prs.slides)

    fixed = renumber(prs)
    prs.save(str(DST))
    print(f"{n_before} slides + {n_new} new = {len(prs.slides)}")
    print(f"page numbers rewritten on {fixed} slides")
    print(f"-> {DST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
