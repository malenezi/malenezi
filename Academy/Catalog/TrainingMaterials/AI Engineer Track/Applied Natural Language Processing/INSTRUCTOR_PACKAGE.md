# Natural Language Processing with Transformers
## معالجة اللغة الطبيعية باستخدام المحولات

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Natural Language Processing with Transformers |
| **Arabic Title** | معالجة اللغة الطبيعية باستخدام المحولات |
| **Module Code** | SDA-AIE-211 |
| **Level** | Specialist |
| **Duration** | 4 days × 5 learning hours = **20 hours** |
| **Audience** | AI engineers specialising in language applications |
| **Prerequisites** | SDA-AIE-112 |
| **Assessment** | Labs (60%) + Arabic/English NLP application project (40%) |
| **Stackability** | NLP specialisation badge · Counts toward the AI Engineer Specialist Certificate (AIE-216 + any 3 of AIE-211/212/213/214/215) · Feeds the GenAI Engineering specialisation · Next: SDA-AIE-213 |
| **Tools & Platforms** | Hugging Face Transformers · spaCy · sentence-transformers · CAMeL Tools |

## Course Description

A specialist module on modern NLP built around the transformer architecture. Participants tokenise and model text, fine-tune pretrained transformers for classification and extraction tasks, and handle Arabic-language processing challenges. The module bridges classic NLP pipelines and today's LLM-centric stack.

The course is built around a single evolving artefact: **"Bayan" — a bilingual (Arabic/English) citizen-feedback intelligence service** for a Saudi digital-government platform. Participants clean and tokenise the feedback corpus, fine-tune transformers to classify topics and sentiment, extract entities from complaint text, build semantic search over historical cases, evaluate every component with sliced error analysis, and finally optimise the models for production latency budgets. Every lab produces a component of the final project, so by Day 4 each participant owns a working, evaluated, optimised bilingual NLP application — the exact substrate that the LLM and RAG modules (SDA-AIE-213/214) later extend.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Implement text-preprocessing and tokenisation pipelines including Arabic-specific handling
2. **LO2** — Explain attention mechanisms and the transformer architecture
3. **LO3** — Fine-tune pretrained transformer models for classification, NER, and QA tasks
4. **LO4** — Develop embedding-based semantic search and similarity applications
5. **LO5** — Evaluate NLP models with task-appropriate metrics and error analysis
6. **LO6** — Optimize inference speed and memory for transformer deployment

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | From text to tensors | M1: Text Processing, Tokenisation & Embeddings · M2: Attention & the Transformer Architecture | 45% | 55% | Bilingual preprocessing/tokenisation pipeline + annotated attention-map notebook |
| **Day 2** | Make the model yours | M3: Fine-tuning BERT-family Models (classification, NER, QA) · M4 (intro): Arabic NLP | 40% | 60% | Fine-tuned topic/sentiment classifier + NER model on the Bayan corpus |
| **Day 3** | Arabic depth, search, and truth | M4: Arabic NLP (labs) · M5: Semantic Search with Sentence Embeddings · M6: Evaluation & Error Analysis | 40% | 60% | Arabic-tuned models + bilingual semantic search index + sliced evaluation report |
| **Day 4** | Fast, cheap, shipped | M7: Inference Optimisation & Serving · Capstone assembly · Demos | 30% | 70% | Quantised/exported models meeting latency budget + capstone demo + assessment |

## Hour-by-Hour Breakdown

### Day 1 — From Text to Tensors

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why NLP broke and got rebuilt** + course kickoff | Trace the pipeline → pretrain/fine-tune → LLM shift; meet the Bayan corpus and the capstone shape | Interactive lecture + corpus exploration | 80/20 |
| 2 | **Text processing, tokenisation, and embeddings** (M1) | Normalisation, subword algorithms (BPE/WordPiece/SentencePiece), tokenizer fertility, static vs contextual embeddings | Lecture + live tokenizer dissection | 70/30 |
| 3 | **Lab 1 — Bilingual preprocessing & tokenisation pipeline** | Build the cleaning + tokenisation pipeline for the Bayan corpus; measure Arabic vs English fertility | Guided lab (pairs) | 10/90 |
| 4 | **Attention and the transformer architecture** (M2) | Scaled dot-product attention, multi-head, positional encoding, encoder vs decoder families | Lecture + attention-math walkthrough | 75/25 |
| 5 | **Lab 2 — Anatomy of a transformer** | Count parameters, trace one forward pass, visualise attention heads on Arabic and English sentences | Guided lab (pairs) | 10/90 |

### Day 2 — Make the Model Yours

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Fine-tuning transformers I: classification** (M3) | Transfer learning economics, heads, Trainer API, hyperparameters that actually matter | Lecture + config walkthrough | 70/30 |
| 2 | **Lab 3a — Fine-tune the Bayan topic/sentiment classifier** | Fine-tune a BERT-family model; log metrics; beat the TF-IDF baseline | Guided lab (pairs) | 10/90 |
| 3 | **Fine-tuning transformers II: NER and extractive QA** (M3) | Token classification, subword label alignment, span extraction, task-head trade-offs | Lecture + alignment demo | 70/30 |
| 4 | **Lab 3b — Entity extraction and QA on complaints** | Fine-tune NER on the Bayan entity schema; run extractive QA on service documents | Guided lab (pairs) | 10/90 |
| 5 | **Arabic NLP: challenges, models, and resources** (M4) | Morphology, dialects, orthographic normalisation, the Arabic model landscape (AraBERT/CAMeLBERT/MARBERT) | Lecture + CAMeL Tools demo | 75/25 |

### Day 3 — Arabic Depth, Search, and Truth

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Lab 4 — Arabic pipeline and dialect-aware fine-tuning** | CAMeL Tools normalisation; fine-tune CAMeLBERT on Saudi-dialect feedback; compare against Day-2 multilingual model | Guided lab (pairs) | 10/90 |
| 2 | **Semantic search with sentence embeddings** (M5) | Bi-encoders vs cross-encoders, similarity metrics, ANN indexing, multilingual embedding spaces | Lecture + embedding-space demo | 70/30 |
| 3 | **Lab 5 — Bilingual semantic search over historical cases** | Build the FAISS index with sentence-transformers; add cross-encoder re-ranking; measure recall@k | Guided lab (pairs) | 10/90 |
| 4 | **Evaluation and error analysis for NLP** (M6) | Task-appropriate metrics, sliced evaluation, bootstrap confidence, behavioural tests, error taxonomies | Lecture + error-gallery walkthrough | 70/30 |
| 5 | **Lab 6 — The evaluation report** | Slice every Bayan model by language/dialect/length; bootstrap CIs; write the error-analysis report | Guided lab (pairs) | 10/90 |

### Day 4 — Fast, Cheap, Shipped

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Inference optimisation and serving** (M7) | Latency/throughput/memory levers: quantisation, ONNX export, distillation, batching, sequence-length control | Lecture + benchmark dissection | 65/35 |
| 2 | **Lab 7 — Hit the latency budget** | Quantise + export the classifier to ONNX Runtime; benchmark p50/p99; wire into the serving skeleton | Guided lab (pairs) | 10/90 |
| 3 | **Capstone assembly I** | Integrate classifier, NER, search, and evaluation into the Bayan service; complete the project checklist | Project work | 0/100 |
| 4 | **Capstone assembly II + peer review** | Finish integration; exchange projects for peer review against the rubric checklist | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 5-minute demos; rubric-based instructor + peer scoring; path to SDA-AIE-213 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module touches the same Bayan citizen-feedback corpus and service. Never introduce a throwaway dataset for a lab when a Bayan slice can carry the lesson — the capstone is achievable in Day 4 Hours 3–4 only because every lab already produced a component.
- **Pace control:** Labs 3a and 4 are the most overrun-prone (first Trainer run, first Arabic fine-tune). Publish checkpoint branches (`lab3-start`, `lab3-solution`, `lab4-start`, ...) and pre-trained fallback checkpoints on the shared drive so stragglers can fast-forward without losing the thread.
- **Pairing:** rotate pairs daily. Pair a strong-Python participant with a strong-Arabic-linguistics participant on Days 2–3; the skill transfer is the point — most cohorts have engineers who read Arabic natively but have never seen its NLP failure modes named.
- **Environment strategy:** primary = shared GPU pool (one T4-class GPU per pair) or Colab-style hosted notebooks; fallback = CPU with the provided small models (DistilBERT / MiniLM variants) and reduced epochs. Verify both the week before delivery; Lab 3 timings assume GPU.
- **Language:** deliver in English or Arabic; keep all code, identifiers, and commit messages in English. Arabic text appears in *data* (corpus samples, code-example strings) — that is the subject matter, not the language of instruction.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day-4 afternoon is deliberately lighter on theory.
- **Assessment logistics:** rubric scoring happens live during Day 4 Hour 5 demos; collect repository URLs and evaluation reports at the end of Hour 4 so metric claims can be spot-verified before demos begin.

---

# Module 1 — Text Processing, Tokenisation, and Embeddings

## Module Overview

**Purpose.** Everything a transformer does begins with a decision the model never sees: how raw text became integers. This module teaches the full path from messy real-world text — mixed Arabic/English, emoji, inconsistent orthography — to model-ready tensors: normalisation, subword tokenisation (BPE, WordPiece, SentencePiece), and the embedding layers that turn token ids into geometry. Participants learn to treat the tokenizer as a versioned model component with its own failure modes, not a preprocessing afterthought.

**Business relevance.** Tokenisation quality silently taxes every downstream system. A tokenizer with poor Arabic coverage fragments words into 3–4 pieces, which halves the effective context window, raises inference cost per request, and degrades accuracy — all before any model weight is touched. For Saudi organisations processing citizen text at national scale (millions of requests), tokenizer fertility is a direct line item in the GPU bill. Preprocessing bugs (inconsistent normalisation between training and serving) are the NLP equivalent of feature skew — and just as silent.

**Industry use cases.**
- A national contact-centre analytics platform must normalise speech-to-text output, chat transcripts, and web forms into one canonical text representation before any model sees them.
- A bank's document-processing pipeline discovers that its multilingual tokenizer splits Arabic legal terms into character fragments, blowing past the 512-token limit on half its contracts.
- An e-commerce search team measures that switching to an Arabic-aware tokenizer cuts average sequence length 38%, directly cutting embedding-service cost.

**Expected competencies.** After this module a participant can build a reproducible text-preprocessing pipeline (spaCy + custom normalisers), explain and compare BPE/WordPiece/SentencePiece, measure tokenizer fertility on a target corpus, distinguish static from contextual embeddings, and defend preprocessing decisions in review.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Build a deterministic, versioned preprocessing pipeline for bilingual text | LO1 |
| 1.2 | Explain BPE, WordPiece, and SentencePiece and choose between them for a given corpus | LO1 |
| 1.3 | Measure tokenizer fertility and sequence-length distributions on a target corpus | LO1, LO6 |
| 1.4 | Distinguish static and contextual embeddings and inspect embedding geometry | LO1, LO4 |
| 1.5 | Identify preprocessing skew between training and serving as a defect class | LO1, LO5 |

## Technical Content

### 1. Real text is hostile

The Bayan corpus (like every production corpus) contains: mixed Arabic and English in one sentence (code-switching), Arabic typed without diacritics but occasionally with them, three different Unicode forms of the same letter, elongated words for emphasis (tatweel and repeated letters), emoji carrying sentiment, phone numbers and national-ID-shaped strings that must be masked, and HTML artefacts from the web form. Name the defect classes explicitly:

- **Unicode inconsistency:** the same visible string can be composed of different codepoint sequences; without NFC/NFKC normalisation, "identical" strings hash differently, deduplication fails, and lookup tables silently miss.
- **Orthographic variance (Arabic preview):** alef variants (أ إ آ ا), ta marbuta vs ha (ة/ه), alef maqsura vs ya (ى/ي) — users interchange them freely; models treat them as different tokens unless normalised (Module 4 goes deep).
- **Noise vs signal:** emoji and elongation *are* sentiment signal in feedback text; stripping them "to clean the data" destroys label-relevant information. Cleaning decisions are modelling decisions.
- **PII:** national IDs, phone numbers, and names must be masked *before* text enters any training set — under PDPL, a training corpus is personal-data processing.

**Instructor note:** open `bayan_raw_sample.csv` on the projector and have the class call out problems for 5 minutes before naming them formally. Every cohort finds the tatweel elongation and the mixed-script rows unprompted; almost none find the NFC/NFD near-duplicates — that reveal lands hard.

### 2. The classic pipeline and where it still lives

Before transformers, the pipeline was explicit: sentence segmentation → tokenisation → lemmatisation/stemming → POS tagging → feature extraction. spaCy remains the industrial tool for the parts that survive:

- **Sentence segmentation** still matters — transformers have length limits, and chunking a document at arbitrary byte offsets destroys meaning. spaCy's rule-based and statistical segmenters handle abbreviations and numbering that naive `split(".")` butchers.
- **Linguistic annotation** (POS, lemmas, noun chunks) powers rule-based components that wrap models in production: candidate filtering before NER, template slots, keyword fallbacks when the model is down.
- **The pipeline mental model** — a sequence of typed, testable stages — is precisely what participants rebuilt in SDA-AIE-113 terms; here it becomes a `Doc`-in, `Doc`-out spaCy pipeline with custom components.

What did *not* survive: hand-engineered features as model input. Transformers consume subword ids; the classic pipeline now serves the model rather than replacing it.

### 3. Subword tokenisation: BPE, WordPiece, SentencePiece

Word-level vocabularies fail on morphologically rich languages (Arabic verb forms alone would explode the vocabulary) and out-of-vocabulary words; character-level models waste capacity relearning composition. Subword tokenisation is the compromise every modern model uses:

- **BPE (byte-pair encoding):** start from characters (or bytes — GPT-family "byte-level BPE" guarantees no unknown token ever), iteratively merge the most frequent adjacent pair. Deterministic merges learned from a corpus; vocabulary size is the stopping knob.
- **WordPiece (BERT family):** like BPE but merges the pair maximising corpus likelihood rather than raw frequency; continuation pieces carry the `##` prefix (`playing → play ##ing`).
- **SentencePiece (XLM-R, T5, most multilingual models):** treats the input as a raw stream including whitespace (encoded as ▁), so it needs no pre-tokenisation — critical for languages without whitespace conventions and convenient for Arabic clitics.
- **Fertility** — average subword pieces per word — is the health metric. English on BERT-base ≈ 1.15; Arabic on the same (English-centric) vocabulary ≈ 3–4; Arabic on CAMeLBERT ≈ 1.3. High fertility means shorter effective context, slower inference, and weaker representations. **Measure fertility on your corpus before choosing a model** — it is a five-line script (Lab 1) that prevents a five-week mistake.
- Tokenizers are **trained artefacts, versioned with the model**. Using checkpoint A's weights with checkpoint B's tokenizer is silent corruption — ids map to different strings. `AutoTokenizer.from_pretrained` on the same id as the model is not a convenience; it is a correctness requirement.

### 4. From ids to geometry: embeddings

- **The embedding matrix** is a lookup table `[vocab_size × hidden_size]` — for BERT-base, 30,522 × 768 ≈ 23M parameters, about 21% of the model. Token ids index rows; everything after is arithmetic on these vectors.
- **Static embeddings** (word2vec, GloVe, fastText) assign one vector per type: "bank" in "river bank" and "bank account" is one point. Still useful for lightweight similarity, initialisation, and analogy-style probes; fastText's character n-grams handle Arabic morphology surprisingly well for a pre-transformer method.
- **Contextual embeddings** are the transformer's output: the same word gets a different vector per context, computed by attention (Module 2). The classic demonstration — cosine similarity of "عين" (eye/spring/notable) across contexts — shows disambiguation happening in vector space.
- **Positional information:** attention is order-blind, so position must be injected — learned absolute embeddings (BERT), sinusoidal (original transformer), rotary (modern LLMs). Consequence participants must internalise: absolute-position models have a *hard* maximum length (BERT: 512); truncation policy is therefore a modelling decision (head, tail, head+tail?) with task-dependent answers.
- **[CLS], [SEP], [PAD], [MASK], [UNK]:** special tokens are contract, not decoration. Padding must be attention-masked or it pollutes representations; `[UNK]` rate on a corpus is another cheap health metric (byte-level BPE: zero by construction).

### 5. Common mistakes & production considerations

1. **Tokenizer/model mismatch** — loading tokenizer and weights from different checkpoints; ids silently mean different strings.
2. **Preprocessing skew** — normalising training data with one function and serving traffic with another (or with none). The fix is the SDA-AIE-113 fix: one versioned preprocessing module imported by both training and serving code.
3. **Cleaning away the signal** — stripping emoji/elongation from sentiment data; lowercasing before a cased model; dediacritising text for a model trained with diacritics.
4. **Ignoring truncation** — silently cutting complaints at 512 tokens and losing the resolution request that always comes last; measure the length distribution (Lab 1) and choose truncation policy deliberately.
5. **Padding to max-length everywhere** — padding every batch to 512 wastes 3–5× compute vs dynamic padding to the batch maximum (Module 7 quantifies this).
6. **PII entering the corpus** — masking must precede storage; log the masking rate, and audit samples before any fine-tune.

Production: pin tokenizer versions in the lock file and assert `tokenizer.vocab_size` + a canary string's ids at service startup (a three-line test that catches mismatch class outright); treat normalisation functions as public API with golden tests; record preprocessing version in every training run's metadata.

## Code Examples

### The versioned preprocessing module (imported by training AND serving)

```python
# src/bayan/preprocessing.py
"""Single source of preprocessing truth — the anti-skew module.
Training, evaluation, and the serving API all import THIS.
Bump PREPROC_VERSION on any behaviour change; golden tests pin it.
"""
import re
import unicodedata

PREPROC_VERSION = "1.2.0"

_TATWEEL = "ـ"
_PHONE_RE = re.compile(r"(?:\+?966|0)5\d{8}")          # KSA mobile numbers
_NATIONAL_ID_RE = re.compile(r"\b[12]\d{9}\b")          # 10-digit, starts 1/2
_MULTISPACE_RE = re.compile(r"\s+")
_REPEAT_RE = re.compile(r"(.)\1{2,}")                   # 3+ repeated chars


def normalize(text: str) -> str:
    """Deterministic normalisation for the Bayan corpus (AR + EN).

    Deliberately does NOT: lowercase (cased models), strip emoji
    (sentiment signal), or remove diacritics (Module 4 handles the
    Arabic-specific layer separately, model-dependent).
    """
    text = unicodedata.normalize("NFC", text)           # one codepoint form
    text = text.replace(_TATWEEL, "")                   # decorative elongation
    text = _REPEAT_RE.sub(r"\1\1", text)                # "رااااائع" -> "راائع"
    text = _MULTISPACE_RE.sub(" ", text).strip()
    return text


def mask_pii(text: str) -> str:
    """PDPL discipline: PII never enters a training set or a log."""
    text = _PHONE_RE.sub("<PHONE>", text)
    text = _NATIONAL_ID_RE.sub("<NATIONAL_ID>", text)
    return text


def preprocess(text: str) -> str:
    return normalize(mask_pii(text))
```

### spaCy pipeline with a custom component

```python
# src/bayan/segmentation.py
"""Sentence segmentation + light annotation for chunking long complaints.
spaCy handles structure; the transformer handles meaning."""
import spacy
from spacy.language import Language

from bayan.preprocessing import preprocess


@Language.component("bayan_preclean")
def bayan_preclean(doc):
    # Custom components see the Doc AFTER tokenisation; cleaning happens
    # before nlp() is called — this component only flags leftovers.
    for token in doc:
        if token.like_num and len(token.text) == 10:
            token._.set("pii_suspect", True)
    return doc


def build_pipeline() -> Language:
    nlp = spacy.blank("xx")                    # multilingual base: AR + EN
    nlp.add_pipe("sentencizer")
    from spacy.tokens import Token
    if not Token.has_extension("pii_suspect"):
        Token.set_extension("pii_suspect", default=False)
    nlp.add_pipe("bayan_preclean")
    return nlp


def split_sentences(raw: str, nlp: Language) -> list[str]:
    doc = nlp(preprocess(raw))
    return [s.text.strip() for s in doc.sents if s.text.strip()]
```

### Tokenizer comparison and fertility measurement

```python
# notebooks/01_tokenizer_audit.py
"""The five-line health check that prevents the five-week mistake:
measure how each candidate tokenizer treats YOUR corpus."""
import pandas as pd
from transformers import AutoTokenizer

CANDIDATES = {
    "bert-base-multilingual-cased": "mBERT (WordPiece, 104 langs)",
    "xlm-roberta-base": "XLM-R (SentencePiece, 100 langs)",
    "CAMeL-Lab/bert-base-arabic-camelbert-mix": "CAMeLBERT (Arabic-centric)",
    "distilbert-base-uncased": "DistilBERT (English-only — the trap)",
}

corpus = pd.read_csv("data/bayan_feedback.csv")


def fertility(tokenizer, texts: list[str]) -> float:
    words = pieces = 0
    for t in texts:
        ws = t.split()
        words += len(ws)
        pieces += len(tokenizer.tokenize(t))
    return pieces / max(words, 1)


for name, desc in CANDIDATES.items():
    tok = AutoTokenizer.from_pretrained(name)
    ar = corpus[corpus.lang == "ar"].text.tolist()
    en = corpus[corpus.lang == "en"].text.tolist()
    print(f"{desc:42s}  AR fertility={fertility(tok, ar):.2f}  "
          f"EN fertility={fertility(tok, en):.2f}")

# Reference output (Bayan corpus):
#   mBERT (WordPiece, 104 langs)       AR fertility=2.71  EN fertility=1.31
#   XLM-R (SentencePiece, 100 langs)   AR fertility=1.94  EN fertility=1.27
#   CAMeLBERT (Arabic-centric)         AR fertility=1.34  EN fertility=1.88
#   DistilBERT (English-only — trap)   AR fertility=6.90  EN fertility=1.18
```

### Contextual vs static: the disambiguation probe

```python
# notebooks/01_contextual_probe.py
"""Show contextual embeddings separating senses that static vectors merge."""
import torch
from transformers import AutoModel, AutoTokenizer

name = "CAMeL-Lab/bert-base-arabic-camelbert-mix"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModel.from_pretrained(name).eval()

sentences = {
    "eye":    "أصيبت عينه أثناء العمل",      # "his eye was injured at work"
    "spring": "شربنا من عين الماء الباردة",   # "we drank from the cold water spring"
}


def vector_for(sentence: str, target: str = "عين") -> torch.Tensor:
    enc = tok(sentence, return_tensors="pt")
    with torch.inference_mode():
        hidden = model(**enc).last_hidden_state[0]      # [seq, 768]
    ids = enc.input_ids[0].tolist()
    target_id = tok.convert_tokens_to_ids(tok.tokenize(target))[0]
    return hidden[ids.index(target_id)]

v_eye, v_spring = vector_for(sentences["eye"]), vector_for(sentences["spring"])
cos = torch.nn.functional.cosine_similarity(v_eye, v_spring, dim=0)
print(f"cosine('eye' sense, 'spring' sense) = {cos:.3f}")   # ≈ 0.55, not 1.0
```

## Hands-on Lab 1 — Bilingual Preprocessing and Tokenisation Pipeline

| | |
|---|---|
| **Objective** | Build the versioned preprocessing module for the Bayan corpus, audit four candidate tokenizers, and commit a data-driven tokenizer/model choice with evidence |
| **Duration** | 50 minutes |
| **Setup** | Python 3.12, `pip install transformers spacy pandas`, course repo cloned, `git checkout lab1-start`, `data/bayan_feedback.csv` (12,000 rows) |

**Instructions & tasks**

1. *(10 min)* Explore `bayan_raw_sample.csv`; catalogue at least six defect classes in `NOTES.md` (Unicode forms, tatweel, code-switching, PII, emoji, HTML remnants).
2. *(10 min)* Implement `normalize()` and `mask_pii()` in `src/bayan/preprocessing.py`; make the provided golden test pass (`pytest tests/test_preprocessing.py` — 25 input/output pairs).
3. *(10 min)* Build the spaCy segmentation pipeline; verify long complaints split into sensible sentences (spot-check the 5 flagged examples, including the numbered-list complaint).
4. *(10 min)* Run the tokenizer audit across the four candidates; produce the fertility table and the sequence-length histogram (95th percentile per language per tokenizer).
5. *(5 min)* Write the decision record `DECISIONS.md#tokenizer`: chosen checkpoint(s) for Arabic and bilingual work, justified by fertility + length numbers.
6. *(5 min)* Commit: `feat(preprocessing): versioned bilingual pipeline with tokenizer audit`.

**Expected output**
```
$ pytest tests/test_preprocessing.py -q
25 passed in 0.4s
$ python notebooks/01_tokenizer_audit.py
CAMeLBERT  AR fertility=1.34 ... (table as in code example)
p95 sequence length (CAMeLBERT, AR): 87 tokens  → 512 limit is comfortable
PII masking rate on raw corpus: 3.1% of rows contained PHONE or NATIONAL_ID
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Golden test fails on 2 Arabic pairs only | NFKC used instead of NFC | NFKC folds presentation forms *and* compatibility chars — too aggressive here; use NFC |
| Fertility ≈ 1.0 for DistilBERT on Arabic | Counting `[UNK]` as one piece per word | Count `tokenize()` output length; inspect — the text became `[UNK]` sequences, which is worse than high fertility |
| spaCy splits "د. أحمد" into two sentences | Sentencizer treats the abbreviation dot as terminal | Add the abbreviation to the sentencizer's exceptions or use a custom boundary rule |
| Emoji disappear after normalisation | Overzealous regex from an online snippet | Keep emoji; they carry label signal — the point of task 1's catalogue |

**Instructor notes.** The fertility table is the module's money shot — have every pair post their DistilBERT-on-Arabic number to the shared board; the 6–7× figure makes "model choice is a data decision" visceral. Watch for pairs whose masking rate is 0%: they ran `normalize` before `mask_pii` and the repeated-char collapse broke the phone regex — a perfect ordering-matters lesson. Fast finishers: measure `[UNK]` rates and add the startup canary assertion (tokenizer + one pinned string → pinned ids).

## Mini Exercises

**Quiz (5 questions)**
1. Why must the tokenizer come from the same checkpoint as the model weights? → ids are meaningless without the exact vocab/merges that trained the embedding rows.
2. Fertility of 3.5 on your corpus means what operationally? → ~3.5 pieces/word: shorter effective context, more compute per request, weaker downstream accuracy.
3. Which algorithm needs no pre-tokenisation and encodes whitespace explicitly? → SentencePiece.
4. Name a cleaning step that *destroys* signal for sentiment analysis. → stripping emoji / collapsing elongation entirely / lowercasing for a cased model.
5. True/False: byte-level BPE can produce `[UNK]`. → **False** — every byte sequence is representable.

**Debugging exercise.** Branch `sim-skew-preproc`: the serving API normalises with an older regex (keeps tatweel); offline eval looks fine, but live traffic accuracy is 9 points lower. Participants must find the divergence by diffing `preprocess()` outputs on 20 raw samples between the two code paths — then state the structural fix (one shared module, version asserted at startup).

**Code-review exercise.** Review a PR that lowercases all text "for consistency", strips all non-alphanumerics (killing Arabic diacritics *and* emoji), and applies masking after logging the raw text. Three findings, each with the concrete harm named.

**Discussion questions.**
- The team wants one tokenizer for Arabic and English to simplify ops. What evidence decides between one multilingual model and two monolingual ones? (fertility per language, traffic mix, latency budget, maintenance cost)
- Should preprocessing live in the model artefact (tokenizer config) or in service code? What breaks in each choice when you ship a v2?

## Case Study — Contact-Centre Analytics at a National Utilities Provider

**Scenario.** A Saudi utilities provider processes 40,000 customer interactions daily across IVR speech-to-text, WhatsApp, and a web portal. An analytics vendor's dashboard reports topic volumes that the operations team calls "obviously wrong" — outage complaints undercounted during a real outage week.

**Business context.** Topic volumes drive staffing and executive escalation. The undercount delayed a field-maintenance surge by two days during a heatwave; the incident review demands a root-cause within three weeks.

**Technical challenge.** Audit the text pipeline end-to-end: three ingestion channels, each with different encodings and noise profiles, feeding one English-centric multilingual model.

**Constraints.** The vendor model cannot be retrained this quarter; STT output has no diacritics and phonetic spellings of dialect words; WhatsApp text is heavy with elongation and emoji; PDPL requires PII masking before any text leaves the ingestion zone.

**Solution approach (facilitate, don't lecture).** The audit finds: (1) the STT channel emits NFD-form Arabic while the portal emits NFC — the dedup stage silently drops "duplicate" outage reports that were actually distinct; (2) fertility on the vendor tokenizer is 3.2 for Gulf-dialect words, and truncation at 128 tokens cuts the outage location off long WhatsApp messages; (3) elongated words ("الكهرباااء") tokenize into garbage pieces the topic model has never seen. Fixes in order of cost: unified NFC normalisation + elongation collapse at ingestion (days), truncation policy change to head+tail (days), tokenizer/model replacement (next quarter, with the fertility evidence as the procurement argument).

**Discussion questions.**
1. Why did the bug surface as *undercounting during an outage* specifically? (volume spike → more long/elongated messages → more truncation and dedup loss)
2. Which of the three fixes needs a regression test, and what does its golden file contain?
3. The vendor proposes "just lowercase and strip everything" — argue the counter-case with signal-loss examples.
4. Where must PII masking sit among the fixes, and why is order non-negotiable under PDPL?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Preprocessing golden tests | Correctness | 25/25 pass | pytest |
| Fertility (chosen AR tokenizer) | Efficiency | ≤ 1.5 on Bayan AR slice | audit script |
| p95 sequence length vs limit | Efficiency | documented, with truncation policy | audit script |
| PII masking recall | Compliance | 100% on the 60-case PII test set | masking test |
| Preprocessing throughput | Performance | ≥ 5,000 docs/s (normalise+mask, CPU) | timing harness |
| Skew canary at startup | Reliability | canary string → pinned ids asserted | startup test |

**Example benchmark table (filled during lab):**

| Tokenizer | AR fertility | EN fertility | AR p95 len | UNK rate (AR) |
|---|---|---|---|---|
| mBERT | 2.71 | 1.31 | 143 | 0.4% |
| XLM-R | 1.94 | 1.27 | 112 | 0.0% |
| CAMeLBERT-mix | 1.34 | 1.88 | 87 | 0.1% |
| DistilBERT (en) | 6.90 | 1.18 | 348 | 11.2% |

## Required Visuals and Training Assets

### Diagrams
1. **Text-to-tensor pipeline** — *Purpose:* anchor image for the module. *Elements:* raw text (with visible defects) → normalise → mask PII → segment → tokenizer (subword pieces shown) → ids → embedding lookup → tensor; a skew warning icon where training and serving paths must share the normalise box. *Style:* horizontal flow, monospace text samples at each stage, course palette. *Designer note:* show the same Arabic sentence transforming at every stage — continuity sells the pipeline.
2. **Subword algorithm comparison** — *Elements:* one sentence tokenised three ways (BPE/WordPiece/SentencePiece) with merge/likelihood/whitespace-symbol annotations; fertility number under each. *Style:* three-row comparison card.
3. **Fertility as cost** — *Elements:* bar chart of pieces-per-word across four tokenizers on Arabic text, with a second axis showing relative inference cost; the DistilBERT bar breaking the chart frame. *Style:* editorial bar chart, printable.
4. **Static vs contextual embeddings** — *Elements:* 2-D projection with the word "عين" as one static point vs three contextual clusters (eye/spring/notable), example sentences as callouts. *Style:* scatter with annotation arrows.

### Images (screenshots)
1. **Raw corpus in a data viewer** — *why:* participants must see real mess before cleaning it; *content:* 10 rows with tatweel, emoji, mixed script, and a masked-out PII column highlighted.
2. **Terminal screenshot — golden preprocessing tests green** — *why:* expected-state reference; *content:* 25 passed, versioned module path visible.
3. **Tokenizer audit table output** — *why:* the decision artefact; *content:* fertility table exactly as the lab produces it.
4. **Tokenizer playground screenshot** — *why:* piece-level intuition; *content:* one Arabic sentence in the Hugging Face tokenizer viewer showing WordPiece `##` fragments.

### Simulations
1. **Preprocessing skew incident** — *Setup:* branch `sim-skew-preproc` (serving path uses stale normaliser). *Expected:* offline metrics fine, live-replay accuracy drops 9 points; found by diffing pipeline outputs. *Learning objective:* preprocessing is a versioned model component.
2. **The English-only tokenizer trap** — *Setup:* fine-tune config pointed at DistilBERT for the Arabic slice. *Expected:* training "works", accuracy plateaus ~15 points low, sequences hit the length limit; fertility audit explains why. *Learning objective:* model choice starts at the tokenizer.

### Interactive Activities
- **Defect safari (10 min):** pairs race to find the most defect classes in the raw sample; board tally; instructor reveals the two nobody finds (NFD duplicates, zero-width characters).
- **"Clean or keep?" card sort (10 min):** 12 preprocessing operations sorted into always/never/task-dependent, defended against the sentiment and NER use cases.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `bayan_feedback.csv` | Synthetic, course-generated (Faker + dialect templates + defect injector; AR/EN citizen feedback with topic, sentiment, entity annotations) | CSV | 12,000 rows | Golden-thread corpus for all modules |
| `bayan_raw_sample.csv` | Uncleaned slice of the above | CSV | 200 rows | Defect safari + preprocessing tests |
| `pii_test_set.csv` | Crafted | CSV | 60 rows | Masking recall test |

### Demo Requirements
- **Instructor demo:** live tokenizer dissection — the same Arabic sentence through four tokenizers with piece counts on the projector; end with the DistilBERT wreckage.
- **Student demo:** two pairs present their `DECISIONS.md#tokenizer` record; class challenges the evidence.
- **Expected outputs:** green preprocessing tests, committed audit table, tokenizer decision recorded — all reused verbatim in Lab 3.

---

# Module 2 — Attention and the Transformer Architecture

## Module Overview

**Purpose.** Participants arrive able to *use* transformers (SDA-AIE-112 covered neural fundamentals); this module makes them able to *reason about* transformers: what self-attention computes, why multi-head helps, how positional information enters, and how the encoder/decoder/encoder-decoder families divide the task landscape. The goal is engineering-grade understanding — enough to predict memory blow-ups, choose the right architecture family, and debug attention-level failures — not re-derivation for its own sake.

**Business relevance.** Architecture literacy is what separates engineers who select models from engineers who inherit them. The O(n²) attention cost explains why a document-processing quote doubled when the client's contracts turned out to be 40 pages; encoder-vs-decoder literacy explains why a team burned a quarter forcing a generative model to do classification a 110M-parameter encoder does better and 50× cheaper. In procurement-heavy enterprise environments, the engineer who can read a model card's architecture section is the one who prevents expensive mismatches.

**Industry use cases.**
- A legal-tech team sizing a contract-analysis service must predict memory per request from sequence length — attention's quadratic term is the whole answer.
- A bank chooses between an encoder (classification of transaction disputes) and a decoder LLM; the encoder wins on latency, cost, and auditability for a fixed-label task.
- A ministry's translation pipeline uses an encoder-decoder model; understanding cross-attention is what lets engineers debug why named entities get mistranslated.

**Expected competencies.** Participants can compute scaled dot-product attention by hand for a toy example, explain Q/K/V roles and multi-head decomposition, account for every parameter in BERT-base, choose among encoder/decoder/encoder-decoder families for a task, and inspect attention maps to debug model behaviour.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Compute scaled dot-product attention for a toy sequence by hand and in PyTorch | LO2 |
| 2.2 | Explain multi-head attention, positional encoding, and the full encoder block | LO2 |
| 2.3 | Account for the parameter and memory budget of a BERT-class model | LO2, LO6 |
| 2.4 | Select encoder, decoder, or encoder-decoder families per task with justification | LO2, LO3 |
| 2.5 | Inspect attention maps to explain and debug model behaviour | LO2, LO5 |

## Technical Content

### 1. Self-attention: the core computation

Every token asks one question of every other token: *how relevant are you to what I mean here?* Mechanically, each token's embedding is projected three ways — **Query** (what I'm looking for), **Key** (what I advertise), **Value** (what I contribute):

```
Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V
```

Teach it as four steps on a whiteboard with a 4-token sentence ("the bank was closed" — or the Arabic عين example from M1):

1. **Scores:** `QKᵀ` — every query dotted with every key gives an n×n relevance matrix.
2. **Scale:** divide by √d_k — without it, dot products grow with dimension, softmax saturates, gradients vanish (this scaling constant is the most-asked interview question in the room; make them own it).
3. **Normalise:** row-wise softmax — each token's attention over all tokens sums to 1.
4. **Mix:** multiply by V — each output is a relevance-weighted average of value vectors. The output for "bank" now *contains* information from "closed", which is disambiguation happening as arithmetic.

Consequences worth stating explicitly: attention is **permutation-equivariant** (hence positional encodings), **fully parallel across tokens** (hence GPUs love it — this is the one-line answer to "why did transformers replace RNNs"), and **O(n²) in sequence length** for both compute and memory (hence the 512-token ceilings, hence Module 7's obsession with sequence length, hence the entire efficient-attention research industry).

### 2. Multi-head attention and the encoder block

One attention head averages; several heads *specialise*. Multi-head attention splits the hidden dimension into h subspaces (BERT-base: 12 heads × 64 dims), runs attention independently in each, concatenates, and projects. Empirically heads specialise: some track syntax-like relations, some track adjacency, some sit on `[SEP]`/punctuation as no-op sinks. Head-pruning research shows many heads are redundant — foreshadowing distillation (M7).

The full encoder block stacks: multi-head self-attention → residual add + LayerNorm → position-wise feed-forward (two linear layers with GELU, expanding 768→3072→768) → residual add + LayerNorm. Twelve of these blocks make BERT-base. Two engineering facts:

- **Residual connections** are why 12+ layer stacks train at all (gradients flow through the identity path — participants met this in AIE-112 with ResNets).
- **The FFN holds ⅔ of block parameters** — attention gets the fame, feed-forward gets the weights. Where does knowledge live? Largely in the FFNs; attention routes it.

**Parameter accounting exercise (do it live):** embeddings 30,522×768 + positional 512×768 + token-type 2×768 ≈ 23.8M; per block: attention 4×(768×768+768) ≈ 2.36M, FFN 2×768×3072 + biases ≈ 4.72M, LayerNorms ≈ 3K → ≈ 7.1M × 12 = 85M; pooler ≈ 0.6M. Total ≈ **110M**. When participants can produce this table themselves (Lab 2), model cards stop being marketing.

### 3. Positional encoding and sequence-length limits

Injecting order: **learned absolute embeddings** (BERT — hard 512 limit, positions beyond are literally out of the table), **sinusoidal** (original transformer — extrapolates in principle, poorly in practice), **relative/rotary** (T5, modern LLMs — encode offsets, extend better). For this course's BERT-family work the operational consequence is the hard limit: truncation policy (M1) and chunking strategy (M5's document search) are forced by architecture, not preference. Mention long-context encoders (Longformer-style sparse attention) as the escape hatch and its trade-off (approximation of full attention).

### 4. The three families and the pretraining objectives that shaped them

| Family | Attention pattern | Pretraining | Sees | Best at | Course examples |
|---|---|---|---|---|---|
| **Encoder** (BERT, CAMeLBERT, XLM-R) | Bidirectional | Masked-language modelling | Whole sentence both ways | Understanding: classification, NER, extractive QA, embeddings | M3, M4, M5 |
| **Decoder** (GPT family) | Causal (left-to-right mask) | Next-token prediction | Only the past | Generation | SDA-AIE-213's territory |
| **Encoder-decoder** (T5, mT5, MarianMT) | Bidirectional in, causal out + cross-attention | Span corruption / seq2seq | Input fully, output causally | Transformation: translation, summarisation | mentioned, not fine-tuned here |

MLM is why encoders excel at understanding: predicting a masked token from *both* sides forces bidirectional context integration; `[CLS]`'s NSP/pooling heritage is why it (or mean-pooling — M5 discusses which) serves as the sentence handle. The decision rule participants leave with: **fixed output space → encoder; free-form text out → decoder; text-to-text transformation → encoder-decoder.** Then the LLM-era caveat (bridge to AIE-213): a large decoder with a good prompt can zero-shot many understanding tasks — at 10–100× the serving cost and with harder evaluation; the specialist's job is knowing when the small encoder wins. That trade-off study is a capstone bonus task.

### 5. Reading attention maps (and not over-reading them)

`output_attentions=True` returns per-layer, per-head n×n matrices. Legitimate uses: debugging (is the model attending to `[PAD]`? — mask bug; does the QA head attend from question to the answer span?), teaching intuition, and communicating model behaviour to stakeholders. Illegitimate use: presenting attention weights as faithful *explanation* — research is clear that attention ≠ attribution; for accountable explanations use perturbation-based methods (M6 touches SHAP-style token attribution). Teach both the tool and its epistemic limits — Saudi public-sector deployments increasingly face explainability requirements, and "we showed a heatmap" does not survive audit.

### 6. Common mistakes & production considerations

1. Forgetting the attention mask on padded batches — `[PAD]` tokens leak into representations; accuracy drops mysteriously with batch size changes.
2. Sizing memory from parameters alone — activations scale with batch × length²; a 110M model OOMs on 4k-token inputs long before weights matter.
3. Choosing a decoder LLM for a 12-label classification task — 50× serving cost for worse calibrated outputs.
4. Treating `[CLS]` as automatically meaningful without a fine-tuned head — raw pretrained `[CLS]` is a poor sentence embedding (M5 shows the fix).
5. Comparing models by parameter count across families — 110M encoder ≠ 110M decoder in capability profile.
6. Over-trusting attention heatmaps as explanations in compliance documents.

Production: sequence length is the cost lever you control (M7 quantifies: halving length ≈ quartering attention compute); prefer dynamic batching by similar lengths; know your model's positional scheme before promising long-document support in an SOW.

## Code Examples

### Scaled dot-product attention from scratch (the whiteboard, executable)

```python
# notebooks/02_attention_from_scratch.py
"""Attention in ~20 lines. Participants verify against F.scaled_dot_product_attention."""
import math
import torch
import torch.nn.functional as F


def attention(q, k, v, mask=None):
    """q,k,v: [batch, heads, seq, d_k]; mask: [batch, 1, 1, seq] (1=keep)."""
    scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))   # [b,h,n,n]
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))  # pad never attended
    weights = scores.softmax(dim=-1)                           # rows sum to 1
    return weights @ v, weights


torch.manual_seed(0)
b, h, n, d = 1, 1, 4, 8                       # 4-token toy sentence, one head
q = k = v = torch.randn(b, h, n, d)

out, w = attention(q, k, v)
ref = F.scaled_dot_product_attention(q, k, v)
assert torch.allclose(out, ref, atol=1e-6)
print("attention weights (rows sum to 1):\n", w[0, 0].round(decimals=2))
```

### Multi-head attention module

```python
# notebooks/02_multihead.py
"""Multi-head = split hidden dim into subspaces, attend independently, re-mix."""
import torch
import torch.nn as nn

from attention_from_scratch import attention


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model: int = 768, n_heads: int = 12):
        super().__init__()
        assert d_model % n_heads == 0
        self.h, self.d_k = n_heads, d_model // n_heads
        self.wq, self.wk, self.wv = (nn.Linear(d_model, d_model) for _ in range(3))
        self.wo = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        b, n, _ = x.shape
        split = lambda t: t.view(b, n, self.h, self.d_k).transpose(1, 2)
        out, _ = attention(split(self.wq(x)), split(self.wk(x)),
                           split(self.wv(x)), mask)
        return self.wo(out.transpose(1, 2).contiguous().view(b, n, -1))


mha = MultiHeadAttention()
n_params = sum(p.numel() for p in mha.parameters())
print(f"MHA parameters: {n_params:,}")   # 2,362,368 — matches the accounting table
```

### Parameter accounting on the real model

```python
# notebooks/02_param_audit.py
"""Make the model card's '110M' auditable, layer by layer."""
from collections import defaultdict
from transformers import AutoModel

model = AutoModel.from_pretrained("bert-base-multilingual-cased")

buckets = defaultdict(int)
for name, p in model.named_parameters():
    if name.startswith("embeddings"):
        buckets["embeddings"] += p.numel()
    elif "attention" in name:
        buckets["attention (all layers)"] += p.numel()
    elif "intermediate" in name or ("output" in name and "attention" not in name):
        buckets["feed-forward (all layers)"] += p.numel()
    else:
        buckets["other (LayerNorm, pooler)"] += p.numel()

total = sum(buckets.values())
for k, v in sorted(buckets.items(), key=lambda kv: -kv[1]):
    print(f"{k:28s} {v/1e6:7.1f}M  ({v/total:5.1%})")
# mBERT: embeddings dominate (~46%) because vocab=119,547 — a multilingual tax
# that CAMeLBERT does not pay. Connect back to the M1 fertility discussion.
```

### Attention-map inspection on Bayan text

```python
# notebooks/02_attention_maps.py
"""Look at what a fine-tuned-free model attends to — and find the pad bug."""
import torch
from transformers import AutoModel, AutoTokenizer

name = "CAMeL-Lab/bert-base-arabic-camelbert-mix"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModel.from_pretrained(name, output_attentions=True).eval()

text = "انقطعت الكهرباء في حي النرجس منذ ثلاث ساعات"  # outage complaint sample
enc = tok(text, return_tensors="pt", padding="max_length", max_length=24)

with torch.inference_mode():
    att = model(**enc).attentions        # tuple of 12 × [1, 12, 24, 24]

layer, head = 8, 3
weights = att[layer][0, head]            # [24, 24]
tokens = tok.convert_ids_to_tokens(enc.input_ids[0])

# Diagnostic: how much attention mass lands on [PAD]?  (should be ~0 WITH mask)
pad_mass = weights[:, [i for i, t in enumerate(tokens) if t == "[PAD]"]].sum()
print(f"attention mass on PAD (mask on): {pad_mass:.4f}")
# Re-run model(**{k: v for k, v in enc.items() if k != 'attention_mask'})
# → pad mass jumps to ~0.3 per row: the silent bug, made visible.
```

## Hands-on Lab 2 — Anatomy of a Transformer

| | |
|---|---|
| **Objective** | Implement attention from scratch and verify against PyTorch; produce the full parameter accounting for two checkpoints; use attention maps to find a planted masking bug |
| **Duration** | 50 minutes |
| **Setup** | Lab 1 environment + `pip install torch matplotlib`, `git checkout lab2-start` (skeleton notebooks with failing asserts) |

**Instructions & tasks**

1. *(15 min)* Complete `attention()` and `MultiHeadAttention` skeletons until the equivalence asserts against `F.scaled_dot_product_attention` pass; print the 4×4 weight matrix and annotate, in comments, which token attends most to which and why that is arbitrary before training.
2. *(10 min)* Run the parameter audit on `bert-base-multilingual-cased` and `CAMeL-Lab/bert-base-arabic-camelbert-mix`; fill the comparison table in `NOTES.md`; explain the embedding-share difference in one sentence (vocab size — the multilingual tax).
3. *(10 min)* Causal-mask extension: modify the mask so position i attends only to ≤ i; verify the weight matrix is lower-triangular. State in one sentence what family you just built. (decoder)
4. *(10 min)* Attention-map diagnostics on three Bayan sentences: locate one head that tracks adjacency and one that sinks on `[SEP]`; then run branch `sim-pad-leak` and use pad-mass measurement to prove the attention mask is missing.
5. *(5 min)* Commit `feat(notebooks): attention implementation + parameter audit + pad-leak diagnosis`.

**Expected output**
```
attention equivalence: PASSED (atol=1e-6)
MHA parameters: 2,362,368
mBERT total: 177.9M (embeddings 46.4%) | CAMeLBERT total: 108.9M (embeddings 21.4%)
sim-pad-leak: PAD attention mass 0.31/row without mask vs 0.0002 with mask
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Equivalence assert fails at ~1e-3 | Scaling by d_model instead of d_k | Divide by √d_k (per-head dim), not √768 |
| Softmax outputs NaN with mask | `-inf` fill applied after softmax | Mask the *scores*, then softmax |
| Param audit misses ~0.6M | Pooler not bucketed | It lands in "other" — check bucket rules |
| Attention maps look uniform | Looking at layer 0 | Early layers are diffuse; inspect layers 6–10 |

**Instructor notes.** Task 1 is the conceptual heart of the course — resist the urge to rescue pairs quickly; the struggle with tensor shapes is where the understanding forms. Keep a shape-annotated solution on a hidden slide for the 35-minute mark. The pad-leak simulation sets up a running theme: *silent numerical wrongness beats loud crashes* — echo it in M3 (label misalignment) and M6 (leakage).

## Mini Exercises

**Quiz.** (1) Why divide by √d_k? → keeps score variance ~1 so softmax stays in its gradient-friendly range. (2) Complexity of self-attention in sequence length, and the operational consequence? → O(n²); sequence length is the dominant cost/memory lever. (3) Which family for: 12-label complaint routing / press-release drafting / AR→EN translation? → encoder / decoder / encoder-decoder. (4) Why can't BERT process 600 tokens? → learned absolute positional table has 512 rows. (5) True/False: high attention weight from token A to B proves B caused the prediction. → **False** — attention is not attribution.

**Debugging exercise.** Branch `sim-pad-leak` (used in the lab): a batched inference path drops `attention_mask`. Symptom presented first: "accuracy depends on batch composition." Participants must connect symptom → padding → mask → fix, and write the one-line regression test (pad-mass < 0.01).

**Code-review exercise.** Review a design doc proposing a 7B decoder LLM for Bayan topic classification. Required findings: cost per request vs encoder, latency, evaluation difficulty, and the case where the LLM *is* right (long-tail labels with no training data — zero-shot; note it as the AIE-213 bridge).

**Discussion.** Your stakeholder asks "which words did the model look at?" for a rejected-claim explanation. What do you show them, what do you refuse to show, and what caveat goes in writing?

## Case Study — Contract-Intelligence Sizing at a Riyadh Legal-Tech Firm

**Scenario.** A legal-tech startup serving Saudi corporate clients quotes a contract-analysis service (clause classification + obligation extraction) priced on 2-page contracts. The pilot client's procurement contracts average 38 pages with 200-line annex tables. First production batch: GPU out-of-memory crashes, then 11-minute per-document latency after a naive fix (processing full documents as one sequence on CPU).

**Business context.** The contract is fixed-price; the client's legal team expects results by Sunday board meetings. Renegotiation is possible only with a technically credible explanation of what changed.

**Technical challenge.** Explain the failure from architecture first principles, then redesign the processing strategy within the existing 110M-parameter encoder.

**Constraints.** No larger GPUs this quarter; the clause classifier is validated and retrained only quarterly; Arabic/English mixed contracts; extraction quality on annex tables is contractually exempt (tables go to a separate structured pipeline).

**Solution approach.** The sizing error is the quadratic term: 38 pages ≈ 12k tokens → attention memory ≈ (12k/512)² ≈ 550× the pilot's per-window cost if forced through as one sequence — architecturally impossible on the card, hence OOM. Redesign: sentence-window chunking (M1's segmenter) with 64-token overlap; per-window classification; document-level aggregation rules for clause labels; obligation extraction only on windows the classifier flags (cheap filter before expensive extraction); dynamic batching of similar-length windows. Result: 38-page document ≈ 90 windows ≈ 4 s on the existing GPU. The quote model is repriced per-window, not per-document — the architecture lesson became the pricing model.

**Discussion questions.**
1. Reconstruct the OOM from first principles: where exactly does the n² bite — weights, activations, or attention matrices?
2. What does window overlap protect against, and what does it cost? How would you pick 64 vs 128?
3. A vendor pitches a 100k-context LLM as "the simple fix". Build the cost-and-evaluation counter-argument, and name the one scenario where the vendor is right.
4. Which module of this course produces the evidence for the repricing conversation? (the benchmark tables — M7's methodology, applied early)

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Attention implementation equivalence | Correctness | allclose vs PyTorch, atol 1e-6 | notebook assert |
| Parameter accounting error | Understanding | ≤ 1% vs `numel()` total | audit script |
| Pad-mass regression check | Reliability | < 0.01 attention mass on PAD | diagnostic script |
| Family-selection quiz | Understanding | 100% on 6 scenario cards | in-class check |
| Memory prediction exercise | Understanding | within 2× of measured peak for n∈{128,512} | `torch.cuda.max_memory_allocated` |

**Example benchmark table (filled during lab):**

| Sequence length | Attention matrix memory (12 heads, fp32) | Measured peak (batch=8) | p50 forward latency (T4) |
|---|---|---|---|
| 128 | 9.4 MB | 1.1 GB | 11 ms |
| 256 | 37.7 MB | 1.6 GB | 19 ms |
| 512 | 150.9 MB | 3.4 GB | 46 ms |

## Required Visuals and Training Assets

### Diagrams
1. **Scaled dot-product attention, step by step** — *Purpose:* the course's most-reused teaching image. *Elements:* 4-token sentence; Q/K/V projections as three coloured arrows; the 4×4 score matrix with real numbers; softmax rows; the weighted mix producing one output vector. *Style:* four numbered panels, monospace numbers, course palette. *Designer note:* use the same sentence as diagram 2 in M1 for continuity.
2. **The encoder block exploded view** — *Elements:* MHA → add&norm → FFN → add&norm with residual arrows drawn as bypass pipes; parameter counts per component; ×12 stack indicator. *Style:* vertical exploded schematic.
3. **Three families poster** — *Elements:* encoder/decoder/encoder-decoder as three columns: attention pattern (bidirectional/causal/cross), pretraining objective icon, task list, cost band, example checkpoints incl. Arabic ones. *Style:* printable A4 reference card.
4. **The n² wall** — *Elements:* memory/compute curve vs sequence length with annotated real incidents (512 BERT limit, the 38-page contract); chunking shown as staying under the curve. *Style:* single curve chart with callouts.

### Images (screenshots)
1. **Attention heatmap grid** — *why:* pattern-recognition training; *content:* 3 heads on one Bayan sentence: adjacency head, [SEP]-sink head, and a content head, labelled.
2. **Pad-leak before/after heatmaps** — *why:* the module's bug made visible; *content:* same sentence with and without attention mask, PAD columns highlighted.
3. **Parameter audit terminal output** — *why:* expected-state reference; *content:* the bucket table for both checkpoints side by side.
4. **`nvidia-smi` during the length sweep** — *why:* memory realism; *content:* memory climbing across n=128/256/512 runs.

### Simulations
1. **Pad-mass leak** — *Setup:* branch `sim-pad-leak` (mask dropped in batched path). *Expected:* batch-composition-dependent outputs; diagnosed via pad-mass metric. *Learning objective:* masks are correctness, not plumbing.
2. **OOM cliff** — *Setup:* script sweeps sequence length 512→4096 on the lab GPU. *Expected:* OOM between 2048 and 4096 at batch 8; participants predict the cliff before running. *Learning objective:* activation memory scales with n², predictable in advance.

### Interactive Activities
- **Attention by hand (10 min):** pairs compute one attention row for a 3-token example with 2-dim vectors on paper; fastest correct pair explains at the board.
- **Family-selection speed round (10 min):** 6 scenario cards (complaint routing, khutbah summarisation, CV screening, AR↔EN translation, code completion, FAQ retrieval) sorted to families with one-line justification.

### Datasets
No new datasets; Bayan sentences from M1 feed all attention inspections — the golden thread continues.

### Demo Requirements
- **Instructor demo:** live whiteboard attention computation, then the same numbers falling out of the notebook — the "math you can run" moment; then the pad-leak reveal on the projector.
- **Student demo:** one pair presents their causal-mask matrix and names the family; one pair presents the CAMeLBERT-vs-mBERT parameter explanation.
- **Expected outputs:** everyone's equivalence asserts green; the pad-mass regression test lands in the shared test folder for reuse in M7's serving checks.

---

# Module 3 — Fine-tuning BERT-family Models for Downstream Tasks

## Module Overview

**Purpose.** Pretraining bought general language competence; fine-tuning spends it on your task. This module is the course's engineering core: participants fine-tune BERT-family encoders for the three workhorse task shapes — sequence classification (Bayan topic + sentiment), token classification (NER over the complaint entity schema), and extractive question answering — using the Hugging Face `Trainer`, with the hyperparameters, data handling, and failure modes that decide real-world outcomes.

**Business relevance.** Fine-tuned encoders remain the highest-accuracy-per-riyal option for fixed-schema enterprise NLP: a 110M model fine-tuned on 5k labelled examples routinely beats zero-shot LLMs on domain classification while serving at 10–100× lower cost — the economics that make national-scale text services affordable. The craft taught here (label alignment, stratified splits, early stopping, baseline discipline) is precisely what separates teams whose "95% accuracy" survives production from teams whose demo collapses on live traffic.

**Industry use cases.**
- A telecom fine-tunes a ticket-triage classifier routing 80k tickets/day to 14 queues; every point of F1 is a measurable reduction in mis-routed SLA breaches.
- A government-services platform extracts entities (service names, locations, dates, reference numbers) from free-text complaints to auto-populate case files.
- A bank's compliance team runs extractive QA over policy documents ("what is the reporting threshold for X?") with page-cited answers — the pre-LLM RAG pattern that AIE-214 generalises.

**Expected competencies.** Participants can prepare datasets with `datasets`, fine-tune with `Trainer` (mixed precision, early stopping, metric-driven checkpointing), implement correct subword label alignment for NER, fine-tune and post-process extractive QA, beat classical baselines honestly, and diagnose the standard fine-tuning pathologies.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Prepare and version datasets for fine-tuning with honest, stratified splits | LO3, LO5 |
| 3.2 | Fine-tune an encoder for sequence classification and beat a TF-IDF baseline | LO3 |
| 3.3 | Implement subword label alignment and fine-tune token classification (NER) | LO3, LO1 |
| 3.4 | Fine-tune and post-process extractive QA with span scoring | LO3 |
| 3.5 | Diagnose fine-tuning pathologies: overfitting, collapse, leakage, seed variance | LO3, LO5 |

## Technical Content

### 1. Transfer learning economics and the fine-tuning recipe

Fine-tuning updates all weights (or a parameter-efficient subset) of a pretrained encoder plus a small task head, on hundreds-to-thousands of labelled examples. The default recipe that works: small learning rate (2e-5 AdamW — 100× smaller than training from scratch; the pretrained weights are a good place, don't leave it fast), 2–4 epochs, linear warmup (~10% of steps) then decay, batch 16–32, early stopping on validation metric. Teach *why* each default exists, because participants will need to deviate:

- LR too high → catastrophic forgetting: loss drops then validation collapses as pretrained structure is destroyed.
- Too many epochs on small data → memorisation; the validation curve, not the training curve, is the truth.
- **Seed variance is real on small datasets:** ±1–2 F1 across seeds for 3k examples. Any claimed improvement smaller than the seed spread is noise — run 3 seeds before believing anything (M6 formalises with bootstrap CIs).
- Layer-wise learning-rate decay and gradual unfreezing exist; on BERT-base-scale models with ≥1k examples, full fine-tuning with the default recipe is rarely beaten — spend effort on data quality instead. **LoRA/PEFT** (adapters that freeze the base and train low-rank deltas) matter when models are large or many tasks share one base; concept introduced here, practised at scale in AIE-215.

**Baseline discipline:** before any transformer run, fit TF-IDF + linear SVM (minutes, CPU). It sets the floor, catches broken labels early (if the baseline gets 91%, your task may be too easy to justify a GPU), and gives the improvement denominator for the business case. Skipping baselines is the most common senior-review finding in real projects.

### 2. Sequence classification mechanics

`AutoModelForSequenceClassification` adds dropout + linear head over the pooled `[CLS]` representation; cross-entropy loss arrives free. The craft is around the model:

- **Splits before anything:** stratified by label *and* grouped by author/case-id — near-duplicate complaints from one citizen must not straddle train/test (leakage; M6's case study revisits). Freeze the test set on day one; it is read-only until the final report.
- **Class imbalance:** Bayan's topic distribution is Zipfian (outages dominate; "other-digital-services" is 2%). Options in order: get more minority data, class weights in the loss, resampling; and report macro-F1, never accuracy, so minority classes can't hide (M6).
- **Dynamic padding** via `DataCollatorWithPadding` — pad per batch, not to global max (3–5× throughput on short-text corpora like Bayan; M7 quantifies).
- **Multi-task note:** topic and sentiment are two heads on one encoder in the reference solution's stretch branch — halves serving cost; a taste of the shared-encoder pattern.

### 3. Token classification and the label-alignment trap

NER assigns BIO tags per *word*, but the model consumes *subwords* — the alignment between them is where most NER bugs live. `tokenizer(words, is_split_into_words=True)` + `word_ids()` maps each subword to its source word; the standard scheme labels the first subword with the word's tag and masks continuations with `-100` (ignored by the loss). Get this wrong and metrics are silently corrupted in either direction:

- Labelling all subwords with `B-LOC` mints extra entity beginnings → precision collapses in evaluation but the *loss looks fine*.
- Evaluating at subword level inflates scores (easy continuation tokens dominate) — evaluation must be at entity level with **seqeval** (M6).

Arabic raises the stakes: fertility 1.3–2 means a third of words split, and clitic prefixes (و/ب/ال attached to words) mean the "word" boundary itself is contested — CAMeL Tools segmentation (M4) can pre-split clitics so location names aren't buried inside token fragments. The Bayan entity schema: `SERVICE`, `LOCATION`, `DATE`, `REF_NUM`, `ORG` — deliberately small, production-shaped.

### 4. Extractive question answering

`AutoModelForQuestionAnswering` adds two heads predicting answer-span start and end over the context tokens; input is `[CLS] question [SEP] context [SEP]`. The engineering lives in pre/post-processing:

- **Long contexts:** slide a window (`stride≈128`) over the document; an example becomes several features; answers are aggregated across windows at inference.
- **Span scoring:** best (start, end) pair maximising `start_logit + end_logit` subject to `start ≤ end` and `end − start ≤ max_answer_len` — the naive argmax of each independently produces inverted spans; the constrained search is the classic exam question.
- **Unanswerable questions** (SQuAD-2-style): compare best span score against the `[CLS]` null score with a tuned threshold — production QA must be able to say "not in this document" or it hallucinates by construction. This single design point is the honest-QA lesson that carries into RAG (AIE-214).
- Offset mapping (`return_offsets_mapping=True`) converts token spans back to character spans in the *original* text — where normalisation (M1) can betray you if offsets are computed on normalised text but displayed against raw text.

### 5. Common mistakes & production considerations

1. **Test-set leakage** via near-duplicates or tuning-on-test ("just one more look") — the inflation that dies on live traffic.
2. **Label misalignment in NER** (continuation subwords labelled) — silently wrong metrics; the `-100` discipline.
3. **Trusting one seed** on a 3k-example dataset — report mean ± spread over 3 seeds.
4. **Skipping the classical baseline** — no floor, no business case, no broken-label tripwire.
5. **Fine-tuning on unnormalised text then serving normalised** (or vice versa) — M1's skew, third appearance; the preprocessing module is imported by the training script *by construction*.
6. **Checkpoint sprawl** — no `load_best_model_at_end`, final epoch ≠ best epoch; and undocumented checkpoints ("model_final_v2_REAL.bin") that no one can reproduce. Every kept checkpoint carries its training config, data version, seed, and metric.

Production: fine-tuned checkpoints are release artefacts — versioned, evaluated against the frozen test set, with a model card (M6 provides the template); training must be a re-runnable script (not a notebook state) — participants' AIE-113 instincts apply verbatim; GPU budget honesty: BERT-base fine-tune on 5k examples ≈ 8 minutes on a T4 — the expensive part is labelling, always.

## Code Examples

### Dataset preparation with honest splits

```python
# src/bayan/data.py
"""Dataset builder: preprocessing module applied HERE (anti-skew),
splits stratified by label and grouped by case author."""
from datasets import Dataset, DatasetDict
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit

from bayan.preprocessing import preprocess

TOPICS = ["outage", "billing", "water", "roads", "permits",
          "health_services", "digital_services", "other"]


def build_topic_dataset(csv_path: str, seed: int = 42) -> DatasetDict:
    df = pd.read_csv(csv_path)
    df["text"] = df["text"].map(preprocess)              # ONE preprocessing truth
    df["label"] = df["topic"].map(TOPICS.index)

    # Group by citizen_id: one author's near-duplicate complaints
    # must never straddle train/test. THE leakage defence.
    gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=seed)
    train_idx, test_idx = next(gss.split(df, groups=df["citizen_id"]))
    train_df, test_df = df.iloc[train_idx], df.iloc[test_idx]

    gss2 = GroupShuffleSplit(n_splits=1, test_size=0.125, random_state=seed)
    tr_idx, val_idx = next(gss2.split(train_df, groups=train_df["citizen_id"]))

    return DatasetDict(
        train=Dataset.from_pandas(train_df.iloc[tr_idx], preserve_index=False),
        validation=Dataset.from_pandas(train_df.iloc[val_idx], preserve_index=False),
        test=Dataset.from_pandas(test_df, preserve_index=False),   # FROZEN
    )
```

### Fine-tuning the topic classifier with Trainer

```python
# src/bayan/train_classifier.py
"""Re-runnable training script (not notebook state). One command, one artefact."""
import numpy as np
from datasets import DatasetDict
from sklearn.metrics import f1_score
from transformers import (AutoModelForSequenceClassification, AutoTokenizer,
                          DataCollatorWithPadding, EarlyStoppingCallback,
                          Trainer, TrainingArguments, set_seed)

from bayan.data import TOPICS, build_topic_dataset

CHECKPOINT = "CAMeL-Lab/bert-base-arabic-camelbert-mix"   # from Lab 1's decision


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = logits.argmax(-1)
    return {"macro_f1": f1_score(labels, preds, average="macro"),
            "accuracy": (preds == labels).mean()}


def main(seed: int = 42):
    set_seed(seed)
    tok = AutoTokenizer.from_pretrained(CHECKPOINT)
    ds: DatasetDict = build_topic_dataset("data/bayan_feedback.csv", seed=seed)
    ds = ds.map(lambda b: tok(b["text"], truncation=True, max_length=256),
                batched=True)

    model = AutoModelForSequenceClassification.from_pretrained(
        CHECKPOINT, num_labels=len(TOPICS),
        id2label=dict(enumerate(TOPICS)),
        label2id={t: i for i, t in enumerate(TOPICS)})

    args = TrainingArguments(
        output_dir=f"runs/topic-{seed}",
        learning_rate=2e-5,                    # the pretrained-weights-respecting LR
        per_device_train_batch_size=32,
        num_train_epochs=4,
        warmup_ratio=0.1,
        weight_decay=0.01,
        fp16=True,                             # mixed precision: ~2x throughput
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,           # best epoch, not last epoch
        metric_for_best_model="macro_f1",
        save_total_limit=2,
        logging_steps=50,
        seed=seed,
        report_to="none",
    )

    trainer = Trainer(model=model, args=args,
                      train_dataset=ds["train"], eval_dataset=ds["validation"],
                      data_collator=DataCollatorWithPadding(tok),
                      compute_metrics=compute_metrics,
                      callbacks=[EarlyStoppingCallback(early_stopping_patience=2)])
    trainer.train()

    # Test set touched ONCE, here, at the end.
    print(trainer.evaluate(ds["test"], metric_key_prefix="test"))
    trainer.save_model(f"artifacts/topic-classifier-{seed}")
    tok.save_pretrained(f"artifacts/topic-classifier-{seed}")


if __name__ == "__main__":
    main()
```

### NER: the label-alignment function (the trap, defused)

```python
# src/bayan/ner_alignment.py
"""Subword label alignment: first subword carries the tag, continuations -100.
Getting this wrong silently corrupts both training and evaluation."""
LABELS = ["O", "B-SERVICE", "I-SERVICE", "B-LOCATION", "I-LOCATION",
          "B-DATE", "I-DATE", "B-REF_NUM", "I-REF_NUM", "B-ORG", "I-ORG"]


def align_labels(batch, tokenizer):
    enc = tokenizer(batch["tokens"], is_split_into_words=True,
                    truncation=True, max_length=256)
    all_labels = []
    for i, word_tags in enumerate(batch["ner_tags"]):
        word_ids = enc.word_ids(batch_index=i)
        prev, labels = None, []
        for wid in word_ids:
            if wid is None:                 # [CLS]/[SEP]/pad
                labels.append(-100)
            elif wid != prev:               # first subword of a word
                labels.append(word_tags[wid])
            else:                           # continuation subword
                labels.append(-100)         # ignored by loss AND eval
            prev = wid
        all_labels.append(labels)
    enc["labels"] = all_labels
    return enc
```

### Extractive QA post-processing (constrained span search)

```python
# src/bayan/qa_postprocess.py
"""From logits to an answer string — or an honest 'not found'."""
import numpy as np


def best_span(start_logits, end_logits, offsets, context: str,
              null_threshold: float = 0.0, max_answer_len: int = 48,
              top_k: int = 20) -> dict:
    null_score = start_logits[0] + end_logits[0]          # [CLS] = "no answer"

    starts = np.argsort(start_logits)[-top_k:]
    ends = np.argsort(end_logits)[-top_k:]
    best = {"score": -1e9, "text": ""}
    for s in starts:
        for e in ends:
            if s == 0 or e == 0 or e < s or e - s + 1 > max_answer_len:
                continue                                   # inverted/oversized spans
            if offsets[s] is None or offsets[e] is None:
                continue                                   # question tokens
            score = start_logits[s] + end_logits[e]
            if score > best["score"]:
                best = {"score": float(score),
                        "text": context[offsets[s][0]:offsets[e][1]]}

    if null_score - best["score"] > null_threshold:
        return {"answer": None, "reason": "no_answer_in_context",
                "margin": float(null_score - best["score"])}
    return {"answer": best["text"], "score": best["score"]}
```

## Hands-on Lab 3 — Fine-tune the Bayan Models (Parts A and B)

| | |
|---|---|
| **Objective** | Part A: TF-IDF baseline + fine-tuned topic classifier beating it by ≥ 8 macro-F1. Part B: NER model with correct alignment (entity-F1 ≥ 0.80) + working QA post-processing incl. unanswerable handling |
| **Duration** | 2 × 50 min (Day 2 H2 + H4) |
| **Setup** | GPU pool or Colab fallback; `pip install transformers datasets scikit-learn seqeval`; `git checkout lab3-start`; artifacts from Lab 1 (preprocessing module, tokenizer decision) |

**Part A tasks (50 min)**
1. *(10 min)* Run the provided TF-IDF + LinearSVC baseline; record macro-F1 in `BENCHMARKS.md` (reference: 0.71).
2. *(10 min)* Complete `build_topic_dataset` — the grouped split is the graded part; prove no `citizen_id` overlap across splits with the provided assertion.
3. *(20 min)* Complete and launch `train_classifier.py`; while it runs (~8 min on T4), predict with the class: which topics will confuse? (billing↔digital_services — both mention fees).
4. *(10 min)* Evaluate on the frozen test set; fill the benchmark row; commit `feat(models): topic classifier beats baseline by +11 macro-F1`.

**Part B tasks (50 min)**
1. *(15 min)* Implement `align_labels`; make the provided alignment unit tests pass (they include an Arabic clitic-splitting case that fails naive implementations).
2. *(15 min)* Fine-tune `AutoModelForTokenClassification` on the Bayan NER split; evaluate with seqeval at entity level.
3. *(15 min)* Implement `best_span` for the provided QA checkpoint; run the 12-question smoke set over service documents — including the 3 unanswerable ones.
4. *(5 min)* Commit `feat(models): NER + extractive QA with honest null handling`.

**Expected outputs**
```
baseline (TF-IDF+SVC):        macro-F1 0.71
topic classifier (seed 42):   macro-F1 0.82  test accuracy 0.86
alignment tests: 8/8 passed (incl. clitic case)
NER (seqeval, entity-level):  F1 0.83  (LOCATION 0.88, REF_NUM 0.91, SERVICE 0.74)
QA smoke set: 9/9 answerable correct-span, 3/3 unanswerable → answer=None
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Loss ≈ ln(8) flat forever | LR 2e-3 instead of 2e-5, or labels all one class after a bad map | Check LR first, then `Counter(ds['train']['label'])` |
| Validation F1 falls while train loss falls | Overfitting past epoch 2 on this data size | Early stopping is on — check `load_best_model_at_end` actually loaded best |
| NER F1 suspiciously high (0.95+) | Subword-level evaluation | Evaluate with seqeval on word-level predictions only (mask -100) |
| QA returns inverted/garbage spans | Independent argmax on start/end | Use the constrained search; the unit test covers it |
| CUDA OOM at batch 32 | 256-token sequences + fp32 | Confirm `fp16=True`; else batch 16 + gradient accumulation 2 |

**Instructor notes.** Part A's prediction game (which classes will confuse) primes M6's error analysis — write predictions on the board and revisit them in Lab 6 against the real confusion matrix. In Part B, at least one pair will get seqeval 0.95+ from subword-level evaluation; make that a public teachable moment: *plausible numbers are the dangerous ones*. Fast finishers: 3-seed variance study (spread lands ±1.5 F1 — feeds M6), or the two-headed topic+sentiment stretch branch.

## Mini Exercises

**Quiz.** (1) Why 2e-5 and not 2e-3? → pretrained weights are a good optimum; big steps destroy it (catastrophic forgetting). (2) Why group splits by citizen_id? → near-duplicates straddling splits = leakage = inflated test scores. (3) What does `-100` do? → excluded from loss/eval; continuation subwords and special tokens don't vote. (4) Why must QA compare against the null score? → otherwise the model always extracts *something* — hallucination by construction. (5) Your improvement is +0.8 F1 on one seed; seed spread is ±1.5. Ship it? → No claim yet — run seeds, then M6's bootstrap.

**Debugging exercise.** Branch `sim-align-bug`: NER trained with continuation subwords labelled `I-*`. Training loss looks *better* than the correct version; entity-level F1 is 14 points worse. Participants must explain both facts (more supervised tokens → lower loss; minted entity fragments → precision collapse).

**Code-review exercise.** Review a training PR: test set evaluated every epoch and used for checkpoint selection, no seed set, notebook-only training, checkpoint named `final_v3_best_REALLY.bin`. Four findings with the fix for each.

**Discussion.** Labelling budget is 2,000 more examples OR a hyperparameter search of the same cost. The classifier's weakest class has 90 training examples. Where does the money go, and what evidence decides? (data — and the per-class learning curve is the evidence)

## Case Study — Ticket Triage at a Saudi Telecom Operator

**Scenario.** A telecom's support platform routes 80,000 daily tickets to 14 resolution queues. The incumbent keyword router achieves 61% accuracy; mis-routed tickets bounce an average of 2.3 times, each bounce adding ~4 hours to resolution. An internal team fine-tuned an Arabic BERT to 88% validation accuracy — but the pilot showed 79% on live traffic, and the project is now under review.

**Business context.** Every accuracy point ≈ 800 correctly routed tickets/day ≈ measurable SLA-breach reduction. The gap between claimed 88 and observed 79 has cost the team its credibility with the operations VP; the review must explain the gap and produce a number the business can trust.

**Technical challenge.** Audit the training pipeline for the inflation sources, then rebuild the evaluation so offline numbers predict live numbers.

**Constraints.** Labels come from historical routing decisions — which include the keyword router's own errors (noisy labels); ticket mix shifts weekly (promotions, outages); some queues merged last quarter (label schema drift); PII rules forbid exporting raw tickets to external tools.

**Solution approach.** The audit finds three inflation sources: (1) random split with near-duplicate tickets (same customer, same issue, re-opened) straddling train/test — grouped splitting drops offline accuracy to 83; (2) evaluation on the *old* 14-queue schema while production runs 12 — schema-mapped re-evaluation: 81; (3) training labels inherited keyword-router errors concentrated in two queues — a 600-ticket gold re-label of those queues shows the model actually *beats* its labels there. Rebuilt evaluation: grouped splits, current schema, gold-labelled eval slice, plus a weekly live-sampled 200-ticket audit — offline 81 now tracks live 80±1. The number the VP gets is 80, with a confidence band and a drift-monitoring plan (M6's methodology; the monitoring itself is SDA-AIE-216's business).

**Discussion questions.**
1. Rank the three inflation sources by how commonly you expect them in the wild, and by detection cost.
2. Training labels were machine-generated by the system being replaced — what does that do to the ceiling, and how do you measure "beats its own labels"?
3. Design the weekly live-audit protocol: sample size, who labels, what triggers retraining.
4. The VP asks for "one number". What do you give, and what do you refuse to compress into it?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Topic classifier vs baseline | Accuracy | ≥ +8 macro-F1 over TF-IDF | frozen test set |
| Grouped-split integrity | Correctness | 0 citizen_id overlap | split assertion |
| NER entity-level F1 | Accuracy | ≥ 0.80 (seqeval) | frozen test set |
| Alignment unit tests | Correctness | 8/8 incl. clitic case | pytest |
| QA smoke set | Correctness | 9/9 spans + 3/3 nulls | smoke script |
| Fine-tune wall-clock (T4) | Performance | ≤ 12 min topic, ≤ 15 min NER | Trainer logs |
| Seed spread (3 seeds, stretch) | Rigour | reported ± in BENCHMARKS.md | repeat runs |

**Example benchmark table (filled during lab):**

| Model | Metric | Validation | Frozen test | Train time (T4) |
|---|---|---|---|---|
| TF-IDF + LinearSVC | macro-F1 | 0.72 | 0.71 | 40 s (CPU) |
| CAMeLBERT topic (seed 42) | macro-F1 | 0.84 | 0.82 | 8 m 10 s |
| CAMeLBERT NER | entity F1 | 0.85 | 0.83 | 11 m 30 s |
| QA (fine-tuned, provided) | EM / F1 | 0.68 / 0.81 | 0.66 / 0.79 | (pre-trained for lab) |

## Required Visuals and Training Assets

### Diagrams
1. **Three task heads, one encoder** — *Purpose:* the module's anchor. *Elements:* shared 12-layer encoder trunk; three detachable heads (classification over [CLS]; per-token tags; start/end span pointers) with input/output examples from Bayan. *Style:* trunk-and-branches schematic, course palette. *Designer note:* make the heads visibly small relative to the trunk — "you train a twig, you rent a tree."
2. **Label-alignment walkthrough** — *Elements:* an Arabic sentence with a LOCATION entity; word row, subword row, tag row, aligned-label row with -100s greyed out; a red "wrong way" panel showing continuation labelling minting a fake entity. *Style:* four-row alignment table, monospace.
3. **The leakage map** — *Elements:* dataset as dots grouped by citizen; random split cutting through a group (red) vs grouped split (green); offline-vs-live accuracy gauge for each. *Style:* before/after split panel.
4. **QA span search** — *Elements:* start/end logit bars over context tokens; valid-span triangle (start≤end, length cap); null-score comparison gate. *Style:* annotated logit plot.

### Images (screenshots)
1. **Trainer console during fine-tuning** — *why:* expected-state reference; *content:* loss curve, per-epoch eval, early-stopping trigger, best-checkpoint reload line.
2. **Confusion matrix (topic classifier)** — *why:* primes M6; *content:* 8×8 matrix with billing↔digital_services confusion visible.
3. **seqeval report** — *why:* entity-level evaluation literacy; *content:* per-entity P/R/F1 with SERVICE lagging.
4. **QA smoke-set output** — *why:* honest-null behaviour; *content:* 12 questions, 3 returning `answer=None` with margins.

### Simulations
1. **Alignment bug** — *Setup:* branch `sim-align-bug`. *Expected:* better loss, worse entity F1; diagnosed via seqeval + inspection. *Learning objective:* the loss is not the metric.
2. **Catastrophic forgetting** — *Setup:* config with LR 2e-3. *Expected:* training loss drops then validation collapses to near-majority-class. *Learning objective:* why 2e-5.
3. **Leaky split** — *Setup:* branch with random (ungrouped) split. *Expected:* +5 macro-F1 offline, exposed by the overlap assertion and a live-replay slice. *Learning objective:* inflation you can generate on demand stops being abstract.

### Interactive Activities
- **Prediction market (5 min, Part A):** pairs bet on which topic pairs will confuse; board odds revisited in Lab 6.
- **Alignment by hand (10 min):** pairs align tags for one clitic-heavy Arabic sentence on paper before implementing; compare against the function's output.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Bayan topic/sentiment split | M1 corpus + labels | HF `datasets` | 12,000 rows | Classification fine-tune |
| Bayan NER annotations | Course-annotated slice (BIO, 5 entity types) | CoNLL-style | 4,000 sentences | Token classification |
| Bayan QA set | Course-crafted over 40 service documents | SQuAD-2-style JSON | 600 questions (15% unanswerable) | Extractive QA |
| `qa_smoke_set.json` | Hand-picked | JSON | 12 questions | Lab smoke test |

### Demo Requirements
- **Instructor demo:** launch the fine-tune live at hour start so the loss curve evolves on the projector during the lecture; the alignment walkthrough on the document camera with paper tokens.
- **Student demo:** one pair presents their baseline-vs-transformer delta and defends the business case in two sentences; one pair shows the clitic alignment test passing.
- **Expected outputs:** three model artefacts in `artifacts/` with configs and metrics committed — Lab 5 (search), Lab 6 (evaluation), and Lab 7 (optimisation) all consume them.

---

# Module 4 — Arabic NLP: Challenges, Models, and Resources

## Module Overview

**Purpose.** Every module so far has treated Arabic as one language among two; this module treats it as the engineering problem it actually is. Participants learn why Arabic stresses every stage of the NLP stack — root-and-pattern morphology, attached clitics, optional diacritics, orthographic free variation, and a dialect continuum that no single training corpus covers — and learn the tools that answer each stress: CAMeL Tools for normalisation, morphological disambiguation, and dialect identification, plus the Arabic pretrained-model landscape (AraBERT, CAMeLBERT variants, MARBERT) and the criteria for choosing among them. The Day-2 models get rebuilt Arabic-first and measurably improve.

**Business relevance.** Arabic NLP competence is a national capability, not a feature. Saudi organisations serve citizens who write Najdi and Hijazi dialect in chat, MSA in formal complaints, and Arabizi in social channels — often in the same thread. Teams that deploy English-centric or MSA-only models against this traffic ship systems that quietly fail on exactly the users government services most need to hear; teams that can *measure* dialect-slice performance and choose Arabic-aware checkpoints deliver the accuracy the multilingual defaults leave on the table. In procurement, "does it actually work on Saudi dialect?" is the question this module teaches participants to answer with evidence.

**Industry use cases.**
- A ministry's complaint platform discovers its MSA-trained sentiment model scores angry Najdi-dialect feedback as neutral — the escalation queue misses precisely the citizens who are most upset.
- A Hajj-season operations centre must triage feedback written in Gulf, Egyptian, Levantine, and Maghrebi dialects within minutes — dialect identification routes each message to the model and the team that handles it best.
- A bank's KYC document pipeline uses morphological segmentation to stop location entities disappearing inside clitic-attached tokens ("وبالرياض" — "and-in-Riyadh" — is one whitespace token).

**Expected competencies.** After this module a participant can apply Arabic-specific orthographic normalisation correctly (and know when *not* to), use CAMeL Tools for morphological analysis, disambiguation, and clitic segmentation, run dialect identification, select among Arabic pretrained checkpoints using corpus evidence, and fine-tune a dialect-appropriate model that beats the multilingual baseline on the dialect slice.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Explain Arabic morphology, orthographic variation, and the dialect continuum as NLP defect sources | LO1 |
| 4.2 | Apply CAMeL Tools normalisation, dediacritisation, and morphological segmentation correctly per model | LO1 |
| 4.3 | Run dialect identification and use it for routing and sliced evaluation | LO1, LO5 |
| 4.4 | Select among Arabic pretrained models (AraBERT, CAMeLBERT, MARBERT) with corpus evidence | LO3 |
| 4.5 | Fine-tune a dialect-aware model that beats the Day-2 multilingual baseline on the dialect slice | LO3, LO5 |

## Technical Content

### 1. Why Arabic stresses the stack: morphology first

Arabic words are built, not listed. A three-consonant root (ك-ت-ب, "writing") interlocks with patterns to derive dozens of stems (كتب wrote, كاتب writer, مكتوب written, مكتبة library), and each stem then takes prefixes and suffixes that English expresses as separate words: conjunctions (و "and"), prepositions (ب "in/with"), the definite article (ال), object pronouns (ها "her/it"). The single whitespace token **وسيكتبونها** unpacks to "and-will-they-write-it" — five English words. Consequences participants must internalise:

- **Vocabulary explosion:** one verb root yields thousands of surface forms; word-level vocabularies are hopeless, and even subword tokenizers trained on English-heavy corpora fragment Arabic badly (M1's fertility table was the preview; morphology is the cause).
- **The "word" is contested:** NER taught label-per-word (M3) — but if the location is buried inside وبالرياض, word-level tags cannot even *express* the right answer. Clitic segmentation (§3) restores the boundary.
- **Sparsity moves:** with morphology handled, Arabic behaves; ignored, every downstream dataset is effectively 3–5× smaller because surface forms don't share statistics.

### 2. Orthography: the variation users produce and models must survive

Written Arabic gives users freedom that breaks string matching and embedding lookup alike:

- **Diacritics (tashkeel)** mark short vowels and are *usually omitted* — كتب without diacritics is "he wrote" / "books" / "it was written"; readers disambiguate from context, models must too. Real traffic is ~1–2% diacritised, so a model trained on diacritised text sees out-of-distribution input at serving time. Dediacritisation at both train and serve time is the common policy — **but it is model-dependent**: strip diacritics for a model pretrained without them; keep them for the rare model that used them. This is M1's skew lesson wearing Arabic dress.
- **Letter variants used interchangeably:** alef forms (أ إ آ → ا), alef maqsura vs ya (ى/ي), ta marbuta vs ha (ة/ه), hamza carriers. Users type whichever is fastest; search misses and duplicate embeddings follow unless normalised — and CAMeLBERT-family models were pretrained on text normalised exactly this way, so *matching the checkpoint's normalisation recipe* is part of the tokenizer-model contract from M1.
- **What not to normalise:** ta marbuta→ha folding merges some real word distinctions; aggressive normalisation before *generation or display* produces text that looks illiterate to users. Rule: normalise the model's input copy, preserve the original for display and offsets — the QA offset-mapping lesson (M3) returns with force.

### 3. CAMeL Tools: analysis, disambiguation, segmentation

CAMeL Tools (CAMeL Lab, NYU Abu Dhabi) is the reference open-source suite for Arabic processing, and the course's fourth pillar tool:

- **Normalisation utilities** implement the §2 recipe as tested functions (`normalize_unicode`, `normalize_alef_ar`, `normalize_alef_maksura_ar`, `normalize_teh_marbuta_ar`, `dediac_ar`) — use these, not hand-rolled regexes; the edge cases (hamza seats, combining marks) are exactly where regexes rot.
- **Morphological analyzer** returns *all* readings of a word out of context (كتب → verb "wrote", noun "books", passive "was written" — each with lemma, POS, diacritisation); the **MLE disambiguator** picks the contextually best reading per token. Analysis without disambiguation is a common misuse: downstream code silently takes the first (arbitrary) reading.
- **Morphological tokenizer** uses the disambiguator to split clitics on a chosen scheme (`d3tok` splits conjunction + preposition + article: وبالرياض → و+ ب+ ال+ رياض). Fed into M3's NER pipeline, segmentation makes buried entities visible: on the Bayan entity set, pre-segmentation lifts LOCATION recall ~5 points because the model finally *sees* the location as a token.
- One-time model download (`camel_data -i defaults`) — in the lab environment this is pre-installed; in production it is a build-time artefact, not a runtime download (AIE-113 discipline).

### 4. The dialect continuum and dialect identification

MSA (الفصحى) is the written standard — news, law, formal complaints. Dialects (العامية) are what people actually type in chat and social media, differing from MSA and from each other in vocabulary (Najdi وش "what" vs MSA ماذا), morphology, and negation patterns; there is no standard orthography for any of them. Engineering facts:

- **MSA-trained models degrade on dialect** — typically 10–20 points on sentiment tasks — and the degradation is silent: dialect text is still Arabic script, so nothing crashes. Only sliced evaluation (M6) reveals it, which is why `dialect` is a first-class column in the Bayan corpus.
- **Dialect identification** is itself a classification task with mature tooling: CAMeL Tools ships a MADAR-trained identifier (26 city-level classes + MSA); coarse routing (Gulf vs Egyptian vs Levantine vs Maghrebi vs MSA) is reliable; city-level is noisy on short texts — set expectations accordingly.
- Uses in this course: **routing** (send dialect traffic to the dialect-tuned model), **sliced evaluation** (report per-dialect metrics), and **data auditing** (what does our corpus actually contain? The Bayan answer: 46% Saudi dialect, 38% MSA, 16% English — a distribution that indicts any MSA-only model choice).
- **Arabizi** (Arabic in Latin script: "mashkurin 3al khidmeh") appears in social channels; transliteration models exist, but the honest engineering answer at this course's scope is: detect it, measure its volume, and route it to a multilingual model or a transliteration step — never let it silently hit an Arabic-script-only model as `[UNK]` soup.

### 5. The Arabic model landscape and how to choose

| Checkpoint | Pretraining data | Strengths | Watch out |
|---|---|---|---|
| **AraBERT** (AUB) | Large MSA corpus (news, Wikipedia) | Strong MSA baseline, widely benchmarked | Requires its own pre-segmentation variant matching; weaker on dialect |
| **CAMeLBERT-MSA / -DA / -CA / -mix** | MSA / dialectal / classical / all three | The variant system *is* the lesson: match pretraining to traffic; `-mix` is the safe default, `-DA` wins on dialect-heavy tasks | Normalised pretraining text — match the recipe |
| **MARBERT / ARBERT** (UBC) | 1B dialectal tweets / MSA | MARBERT is the dialect + social-media specialist | Tweet-domain flavour; 128-token pretraining length |
| **XLM-R / mBERT** | 100+ languages | One model for AR+EN traffic, code-switching tolerance | Multilingual tax (M2's embedding share); fertility 1.9+ |

The decision procedure, not a brand loyalty: (1) measure your traffic's language/dialect mix (the §4 audit); (2) measure candidate fertility on *your* corpus (M1's five-line script); (3) fine-tune the two best candidates on a pilot slice and compare **on the dialect slice, not just the aggregate** (Lab 4). For Bayan: CAMeLBERT-DA wins the Saudi-dialect slice by ~6 macro-F1 over Day-2's CAMeLBERT-mix, which itself beat XLM-R — and the aggregate number alone would have hidden most of that.

**Resources to name** (participants leave with a map, not just models): ANERcorp (Arabic NER), ArSAS and ASTD (sentiment), MADAR and NADI (dialect ID), Arabic-SQuAD and TyDi QA (QA), the Masader catalogue of Arabic datasets; and the scarcity fact that shapes projects — labelled *Saudi-dialect* data is thin, which is why the capstone's labelling-budget question (spend on data, not architecture) is usually the right call.

### 6. Common mistakes & production considerations

1. **One normalisation recipe for all models** — dediacritising for a diacritics-trained model, or skipping alef normalisation for CAMeLBERT; the checkpoint's card defines the recipe, and the preprocessing module (M1) grows a per-model profile.
2. **Normalising the display copy** — users see ه where they typed ة; offsets drift; QA answers highlight the wrong span. Normalise a *shadow copy* for the model; keep raw text authoritative.
3. **Evaluating on MSA, deploying on dialect** — the aggregate-hides-the-slice failure; per-dialect rows in every evaluation report (M6 makes this mechanical).
4. **Trusting city-level dialect ID on 5-word messages** — coarse classes for routing decisions; confidence thresholds; fall back to `-mix`.
5. **Running the analyzer without the disambiguator** — arbitrary readings poison downstream lemma features.
6. **Segmentation mismatch between train and serve** — if NER trained on d3tok segmentation, serving must segment identically; the segmentation scheme joins `PREPROC_VERSION` in the skew canary.

Production: pin `camel-tools` and its data-package versions (the MLE models are artefacts); pre-bake CAMeL data into the container image; log the dialect-ID distribution of live traffic weekly — dialect drift is real drift (a new user population arrives) and it is invisible in loss curves.

## Code Examples

### The Arabic normalisation profile (extends M1's module)

```python
# src/bayan/arabic.py
"""Arabic-specific normalisation layer over bayan.preprocessing.
Per-MODEL profiles: the checkpoint's pretraining recipe decides."""
from camel_tools.utils.dediac import dediac_ar
from camel_tools.utils.normalize import (normalize_alef_ar,
                                         normalize_alef_maksura_ar,
                                         normalize_teh_marbuta_ar,
                                         normalize_unicode)

from bayan.preprocessing import preprocess

ARABIC_PREPROC_VERSION = "1.0.0"

PROFILES = {
    # CAMeLBERT family: pretrained on alef/ya/ta-normalised, dediacritised text
    "camelbert": ["unicode", "alef", "alef_maksura", "teh_marbuta", "dediac"],
    # XLM-R: raw text pretraining — only unicode + course-generic cleaning
    "xlmr": ["unicode"],
}

_STEPS = {
    "unicode": normalize_unicode,
    "alef": normalize_alef_ar,
    "alef_maksura": normalize_alef_maksura_ar,
    "teh_marbuta": normalize_teh_marbuta_ar,
    "dediac": dediac_ar,
}


def normalize_arabic(text: str, profile: str = "camelbert") -> str:
    """Model-input copy ONLY. The raw text stays authoritative for
    display and character offsets (QA lesson, M3)."""
    text = preprocess(text)                      # shared bilingual layer first
    for step in PROFILES[profile]:
        text = _STEPS[step](text)
    return text
```

### Dialect identification and the corpus audit

```python
# notebooks/04_dialect_audit.py
"""What does the Bayan corpus actually contain? Route + slice on the answer."""
import pandas as pd
from camel_tools.dialectid import DialectIdentifier

did = DialectIdentifier.pretrained()             # MADAR-26 + MSA

df = pd.read_csv("data/bayan_feedback.csv")
ar = df[df.lang == "ar"]

preds = did.predict(ar.text.tolist(), "region")  # coarse: region-level classes
ar = ar.assign(dialect_region=[p.top for p in preds])

print(ar.dialect_region.value_counts(normalize=True).round(3))
# Reference output (Bayan AR slice):
#   Gulf    0.548   ← Saudi-dialect feedback dominates
#   MSA     0.451   ← formal complaints
#   Other   0.001
# Engineering consequence: any model evaluated only on MSA is
# unevaluated on half the Arabic traffic.
```

### Clitic segmentation feeding the NER pipeline

```python
# src/bayan/segmentation_ar.py
"""Morphological tokenisation: make entities visible to word-level NER.
وبالرياض  →  و+ ب+ ال+ رياض   — the LOCATION is now its own token."""
from camel_tools.disambig.mle import MLEDisambiguator
from camel_tools.tokenizers.morphological import MorphologicalTokenizer
from camel_tools.tokenizers.word import simple_word_tokenize

_disambig = MLEDisambiguator.pretrained()        # load once, module-level
_seg = MorphologicalTokenizer(_disambig, scheme="d3tok", split=True)


def segment(text: str) -> list[str]:
    words = simple_word_tokenize(text)
    return _seg.tokenize(words)


if __name__ == "__main__":
    sample = "انقطعت الكهرباء وبالرياض تأخرت الصيانة"
    print(segment(sample))
    # ['انقطعت', 'ال+', 'كهرباء', 'و+', 'ب+', 'ال+', 'رياض', 'تأخرت', 'ال+', 'صيانة']
    # NER label alignment (M3) now tags 'رياض' as B-LOCATION directly.
```

### The dialect-slice bake-off driver

```python
# notebooks/04_model_bakeoff.py
"""Same data, same recipe, three checkpoints — judged on the dialect slice.
Reuses M3's train_classifier machinery; only the checkpoint varies."""
from bayan.train_classifier import run_experiment   # refactored from Lab 3

CANDIDATES = [
    "CAMeL-Lab/bert-base-arabic-camelbert-mix",     # Day-2 incumbent
    "CAMeL-Lab/bert-base-arabic-camelbert-da",      # dialect-pretrained
    "UBC-NLP/MARBERT",                              # dialectal-tweet specialist
]

for ckpt in CANDIDATES:
    metrics = run_experiment(checkpoint=ckpt, seed=42,
                             normalize_profile="camelbert",
                             slices=["dialect_region"])
    print(f"{ckpt.split('/')[-1]:34s} "
          f"macro-F1 all={metrics['all']:.3f}  "
          f"Gulf={metrics['Gulf']:.3f}  MSA={metrics['MSA']:.3f}")

# Reference output (Bayan sentiment task):
#   bert-base-arabic-camelbert-mix     macro-F1 all=0.79  Gulf=0.74  MSA=0.84
#   bert-base-arabic-camelbert-da      macro-F1 all=0.82  Gulf=0.80  MSA=0.83
#   MARBERT                            macro-F1 all=0.81  Gulf=0.79  MSA=0.82
# The aggregate says "+3"; the Gulf slice says "+6" — slices tell the truth.
```

## Hands-on Lab 4 — Arabic Pipeline and Dialect-Aware Fine-tuning

| | |
|---|---|
| **Objective** | Build the per-model Arabic normalisation profile, audit the corpus dialect mix, add clitic segmentation to NER, and fine-tune a dialect-aware checkpoint that beats the Day-2 model on the Saudi-dialect slice by ≥ 4 macro-F1 |
| **Duration** | 50 minutes |
| **Setup** | Lab 3 environment + `pip install camel-tools` (CAMeL data pre-installed on lab machines: `camel_data -i defaults`); `git checkout lab4-start`; Day-2 artefacts in `artifacts/` |

**Instructions & tasks**

1. *(10 min)* Implement `normalize_arabic` with the two profiles; make the golden tests pass (30 pairs, including the hamza-seat and combining-mark cases hand-rolled regexes fail).
2. *(10 min)* Run the dialect audit; record the region distribution in `NOTES.md` and answer in one sentence: what does this distribution say about evaluating only on MSA?
3. *(10 min)* Wire `segment()` into the NER data pipeline (branch flag `--presegment`); re-evaluate the Day-2 NER model on segmented input; record the LOCATION recall delta.
4. *(15 min)* Run the bake-off driver on CAMeLBERT-mix vs CAMeLBERT-DA (MARBERT if time allows); fill the sliced comparison table in `BENCHMARKS.md`; update `DECISIONS.md#arabic-model` with the winner and the *slice* evidence.
5. *(5 min)* Commit: `feat(arabic): normalisation profiles + dialect audit + DA model beats mix on Gulf slice`.

**Expected output**
```
$ pytest tests/test_arabic_normalize.py -q
30 passed in 0.6s
dialect audit: Gulf 54.8% | MSA 45.1%
NER LOCATION recall: 0.84 → 0.89 with d3tok pre-segmentation
camelbert-mix   Gulf=0.74   camelbert-da   Gulf=0.80   (+6 macro-F1 on the slice)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `DialectIdentifier.pretrained()` fails | CAMeL data package missing | `camel_data -i defaults` (pre-installed on lab machines; check `$CAMELTOOLS_DATA`) |
| Golden test fails only on diacritised pairs | Profile order: dediac before unicode normalisation | Unicode NFC first — combining diacritics must be composed before stripping |
| NER F1 *drops* after segmentation | Model fine-tuned on unsegmented text, evaluated on segmented | Segmentation is train-AND-serve or neither — re-fine-tune with `--presegment` |
| Bake-off shows no slice difference | Evaluating on the full test set without the dialect filter | Slice masks come from the audit's `dialect_region` column; check the join |
| MARBERT sequences truncated aggressively | 128-token pretraining length | Cap `max_length=128` for MARBERT; note it in the comparison table |

**Instructor notes.** Task 3 is the module's trap-and-reveal: most pairs will evaluate the *unsegmented-trained* model on segmented input first and watch F1 drop — let it happen, then name it: segmentation is part of the model contract, third verse of the skew song. The bake-off's aggregate-vs-slice gap is the bridge to M6; write "+3 or +6?" on the board and leave it there until Lab 6. Fast finishers: run the dialect identifier on the *English* rows (it should abstain/low-confidence — does it?), or add Arabizi detection via character-set heuristic and measure its volume (~0.8% of Bayan).

## Mini Exercises

**Quiz (5 questions)**
1. Why does وبالرياض defeat word-level NER, and what fixes it? → the location is inside one whitespace token with clitics attached; morphological segmentation (d3tok) splits them.
2. When must you NOT dediacritise? → when the checkpoint was pretrained with diacritics (recipe must match pretraining), and never on the display/offset copy.
3. Your sentiment model scores 0.84 overall and traffic is half Saudi dialect. What number do you demand before shipping? → the dialect-slice macro-F1.
4. CAMeLBERT ships four variants — what question do they answer? → match pretraining data (MSA/DA/CA/mix) to your traffic mix.
5. True/False: dialect identification at city level is reliable on short chat messages. → **False** — use coarse region classes with confidence thresholds for routing.

**Debugging exercise.** Branch `sim-seg-skew`: NER was fine-tuned with pre-segmentation, but the serving path feeds raw unsegmented text. Entity F1 in the live-replay harness is 19 points below the offline report. Participants diff the two input pipelines, find the missing `segment()` call, and extend the startup canary to assert the segmentation scheme.

**Code-review exercise.** Review a PR that (a) normalises with a hand-rolled alef regex missing آ, (b) dediacritises the display copy so QA highlights drift, and (c) hardcodes `camelbert` normalisation for an XLM-R fine-tune. Three findings, each with the concrete harm and the fix.

**Discussion questions.**
- The team can label 3,000 more examples: all MSA (cheap, fast annotators) or 1,500 Saudi-dialect (slower, costlier). Use the audit and bake-off numbers to argue the allocation.
- A vendor claims "full Arabic support". Write the three acceptance tests you would run before believing it. (fertility on your corpus, dialect-slice metrics, normalisation-recipe documentation)

## Case Study — Multi-Dialect Pilgrim Feedback at a Hajj-Season Transport Operator

**Scenario.** A transport operator serving Hajj pilgrims collects feedback via WhatsApp and QR-code web forms — roughly two million messages across six weeks, written in Gulf, Egyptian, Levantine, and Maghrebi dialects, MSA, Arabizi, and a dozen non-Arabic languages. Last season's sentiment dashboard, built on an MSA-trained model, rated the season "89% neutral-or-positive" while the on-ground operations log recorded three shuttle-service near-crises that the dashboard never surfaced.

**Business context.** Feedback triage during Hajj is a safety function, not analytics decoration: a spike of angry messages about an overcrowded shuttle stop is an early-warning signal with a response-time budget of minutes. The operator must fix the pipeline before the next season, with a fixed model-hosting budget.

**Technical challenge.** Diagnose why the dashboard missed the crises, and redesign the language-handling front end: identification, routing, normalisation, and dialect-aware modelling within one serving budget.

**Constraints.** Egyptian and Maghrebi dialect volumes spike only during the season (no year-round data); annotation budget covers 8,000 messages; latency budget is 2 s end-to-end; PDPL masking before any text leaves the ingestion zone; the team can host at most two fine-tuned models.

**Solution approach (facilitate, don't lecture).** The post-mortem finds: (1) the MSA model scored dialectal anger as neutral — the crisis messages were almost entirely dialect ("الباصات واقفة ساعتين والحر قاتلنا") and the model had never seen their negation patterns or vocabulary; (2) Arabizi messages (~7% during the season) tokenised to `[UNK]` fragments and defaulted to neutral; (3) normalisation was English-centric — no alef/ya folding, so even MSA deduplication undercounted repeated complaints from the same stop. Redesign: dialect+language ID at ingestion (coarse regions + Arabizi detection); route Arabic to a CAMeLBERT-DA fine-tune (spend 6,000 of the annotation budget on dialect examples stratified by the audit), everything else to XLM-R (the second hosted model); shared Arabic normalisation profile; and a *volume-anomaly* fallback that pages operations when any stop's message rate spikes regardless of sentiment — the model is a filter, not the only tripwire. Sliced evaluation per dialect region becomes a seasonal acceptance gate.

**Discussion questions.**
1. Why did the failure concentrate in exactly the messages that mattered most? (crisis text is emotional → dialectal; formal MSA is the calm register)
2. Defend the 6,000/2,000 annotation split against "label everything MSA — it's cheaper per label".
3. The volume-anomaly fallback needs no NLP at all. What does its inclusion say about defence-in-depth for ML systems?
4. Which slice metrics go into next season's acceptance test, and what threshold would you set for the Gulf slice given the bake-off numbers?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Arabic normalisation golden tests | Correctness | 30/30 pass | pytest |
| Dialect audit of Bayan AR slice | Understanding | distribution recorded + implication stated | notebook + NOTES.md |
| NER LOCATION recall with segmentation | Accuracy | ≥ +4 points vs unsegmented | seqeval on frozen test |
| Dialect-slice macro-F1 (DA vs mix) | Accuracy | ≥ +4 macro-F1 on Gulf slice | sliced evaluation |
| Segmentation skew canary | Reliability | scheme asserted at startup | startup test |
| Bake-off wall-clock (2 models, T4) | Performance | ≤ 25 min total | Trainer logs |

**Example benchmark table (filled during lab):**

| Checkpoint | macro-F1 (all) | Gulf slice | MSA slice | AR fertility |
|---|---|---|---|---|
| CAMeLBERT-mix (Day 2) | 0.79 | 0.74 | 0.84 | 1.34 |
| CAMeLBERT-DA | 0.82 | 0.80 | 0.83 | 1.36 |
| MARBERT | 0.81 | 0.79 | 0.82 | 1.41 |

## Required Visuals and Training Assets

### Diagrams
1. **The Arabic word, exploded** — *Purpose:* the module's anchor image. *Elements:* وسيكتبونها split into و+ س+ يكتبون+ ها with glosses; root ك-ت-ب highlighted inside; a side panel showing five surface forms sharing the root. *Style:* typographic exploded view, large Arabic type, course palette. *Designer note:* set the Arabic in a proper naskh face — the diagram fails if the letterforms look wrong to native readers.
2. **Normalisation decision tree** — *Elements:* input text → per-model profile branch (CAMeLBERT recipe vs XLM-R recipe); a red "display copy" branch that bypasses normalisation entirely; skew warnings where train/serve must match. *Style:* flowchart with two exits.
3. **The dialect map** — *Elements:* Arabic-speaking region with coarse dialect zones; callout bubbles with one sentence ("what" in MSA/Najdi/Egyptian/Levantine); the Bayan corpus distribution as a pie inset. *Style:* stylised map, non-political boundaries, editorial.
4. **Aggregate hides the slice** — *Elements:* two bars (mix 0.79, DA 0.82) that explode into per-slice bars showing the Gulf gap tripling; "+3 or +6?" as the caption. *Style:* drill-down bar chart, printable — this poster returns in M6.

### Images (screenshots)
1. **CAMeL Tools disambiguator output** — *why:* show all-readings vs chosen-reading; *content:* كتب with three analyses, MLE pick highlighted.
2. **Dialect audit console output** — *why:* expected-state reference; *content:* region distribution table exactly as Lab 4 produces it.
3. **Segmented vs unsegmented NER visualisation** — *why:* the entity becoming visible; *content:* displaCy-style span view of وبالرياض before/after d3tok.
4. **Bake-off benchmark table committed in BENCHMARKS.md** — *why:* the decision artefact; *content:* the sliced comparison with the Gulf column highlighted.

### Simulations
1. **Segmentation skew** — *Setup:* branch `sim-seg-skew` (serving path skips `segment()`). *Expected:* live-replay entity F1 19 points under offline; canary extension fixes the class. *Learning objective:* every preprocessing choice is a train-and-serve contract.
2. **The MSA-only evaluation trap** — *Setup:* evaluation config filtered to MSA rows "because they're cleaner". *Expected:* report says 0.84; dialect slice is 0.74; the dashboard-vs-reality gap from the case study, reproduced on Bayan. *Learning objective:* evaluate on the traffic you serve.

### Interactive Activities
- **Reading-race (10 min):** pairs get five undiacritised Arabic words in ambiguous sentences; native readers explain *how* they disambiguated — the class derives why context windows beat lexicons.
- **Normalise or preserve? (10 min):** card sort of 10 operations (alef folding, dediac, ta marbuta, tatweel, Arabizi transliteration...) against three targets: model input, search index, display copy.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Bayan AR slice + dialect labels | M1 corpus, `dialect_region` column added by audit | CSV | ~6,700 rows | Bake-off + sliced evaluation |
| `arabic_normalize_golden.csv` | Crafted (incl. hamza-seat, combining-mark edge cases) | CSV | 30 pairs | Normalisation golden tests |
| Bayan NER (segmented variant) | M3 NER set re-tokenised with d3tok | CoNLL-style | 4,000 sentences | Segmentation experiment |

### Demo Requirements
- **Instructor demo:** live disambiguation of كتب on the projector (all readings → MLE choice), then the segmentation of وبالرياض flowing straight into the M3 alignment function — two modules connecting in one cell.
- **Student demo:** one pair presents their `DECISIONS.md#arabic-model` with the slice evidence; class challenges whether +6 on Gulf justifies hosting a second model (it does here — but make them argue it).
- **Expected outputs:** dialect-aware classifier artefact in `artifacts/`, normalisation profiles in the shared module — both consumed by Lab 5 (bilingual search) and Lab 6 (sliced evaluation).

---

# Module 5 — Semantic Search with Sentence Embeddings

## Module Overview

**Purpose.** Classification answers "which bucket?"; search answers "what else is like this?" — and half of enterprise NLP is the second question wearing the first's budget. This module teaches embedding-based semantic search end-to-end: why raw `[CLS]` vectors fail as sentence embeddings and how contrastively trained sentence-transformers fix them, bi-encoder retrieval vs cross-encoder re-ranking, similarity metrics and their normalisation traps, approximate-nearest-neighbour indexing with FAISS, multilingual embedding spaces that let an English query find an Arabic document, and retrieval evaluation (recall@k, MRR). Participants build Bayan's case-search component: given a new complaint, retrieve the most similar resolved historical cases.

**Business relevance.** Semantic search is the highest-leverage NLP capability per engineering hour: it needs no labels (embeddings are pretrained), ships in days, and upgrades every keyword system it touches — contact-centre deflection, duplicate-case detection, precedent lookup, catalogue search. It is also the retrieval half of RAG: every architectural decision in this module (chunking, index choice, re-ranking, evaluation) reappears verbatim when SDA-AIE-214 bolts an LLM on top. Teams that learn retrieval quality *here*, where it can be measured cheaply, do not debug it *there*, where every retrieval miss becomes a confident hallucination.

**Industry use cases.**
- A government service desk deflects 30% of new tickets by showing citizens the three most similar resolved cases before they submit.
- A bank's fraud team searches two years of case notes by *meaning* — "customer claims SMS never arrived" finds cases phrased twelve different ways, in two languages.
- A legal-services platform retrieves precedent clauses across Arabic and English contracts from one multilingual index.

**Expected competencies.** Participants can choose and justify a sentence-embedding model (multilingual vs monolingual, dimension, speed), build and persist a FAISS index with correct normalisation, implement two-stage retrieve-then-re-rank, chunk documents for indexing, evaluate retrieval with recall@k and MRR against a labelled query set, and state the cost/quality trade-offs of index types.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Explain why pooled `[CLS]` fails as a sentence embedding and how contrastive training fixes it | LO2, LO4 |
| 5.2 | Build a bi-encoder retrieval pipeline with sentence-transformers and FAISS | LO4 |
| 5.3 | Add cross-encoder re-ranking and quantify its quality/latency trade-off | LO4, LO6 |
| 5.4 | Retrieve across languages using multilingual embedding spaces | LO4, LO1 |
| 5.5 | Evaluate retrieval with recall@k and MRR against a labelled query set | LO5 |

## Technical Content

### 1. From token vectors to sentence vectors — and why the obvious way fails

A transformer outputs one vector per token; search needs one vector per sentence. The naive answers disappoint, measurably: raw pretrained `[CLS]` was trained for NSP-style objectives, not similarity — cosine distances in that space correlate poorly with human similarity judgements, and mean-pooling raw BERT is only slightly better. The fix is **contrastive fine-tuning** (the Sentence-BERT recipe): train a *siamese* network on pairs/triplets so that similar sentences pull together and dissimilar ones push apart, with mean-pooling over token vectors as the sentence handle. The result is an embedding space where cosine similarity *means* semantic similarity — the property everything else in this module rents.

Operational takeaways: use models published for the purpose (the `sentence-transformers` model hub: MiniLM distillates for speed, mpnet-base for quality, `paraphrase-multilingual-*` for cross-lingual work); check the model card's *training data and intended similarity notion* — "similar" for paraphrase models ≠ "relevant" for QA-retrieval models (`multi-qa-*`), and picking the wrong notion silently degrades retrieval; embedding dimension (384 vs 768) is a live cost knob — index memory and search latency scale with it.

### 2. Similarity metrics and the normalisation trap

- **Cosine similarity** compares directions; **dot product** rewards magnitude too; **Euclidean distance** on L2-normalised vectors is a monotone transform of cosine. Most sentence-transformers are trained for cosine — so **L2-normalise before indexing and before querying**, then inner product ≡ cosine. Forgetting one of the two normalisations is the classic silent bug: results look plausible (long, information-dense sentences bubble up on magnitude) and are quietly wrong.
- Score *calibration* does not come free: a cosine of 0.71 is not "71% relevant", and thresholds for "no good match" must be tuned on a labelled set per model — the M3 null-answer lesson in retrieval clothing.
- **Chunking:** documents longer than the encoder's window must be split (M1's segmenter returns) — sentence- or paragraph-level chunks with small overlap; index chunks, aggregate to documents at result time (max or top-2 mean of chunk scores). Chunk size is a retrieval hyperparameter: too large dilutes the vector, too small starves it of context; for Bayan's case notes, 2–4 sentence chunks win on the labelled set.

### 3. Bi-encoders, cross-encoders, and the two-stage pattern

- **Bi-encoder:** encode query and documents *independently*; documents are embedded once, offline; query-time cost is one encode + one index lookup. Scales to millions; misses fine-grained interaction ("payment failed *after* update" vs "update failed after payment" land close).
- **Cross-encoder:** concatenate query+candidate and run the full transformer per pair; sees every token interaction, scores far better — and cannot pre-compute anything, so it is O(candidates) full forward passes per query.
- **The production answer is both:** bi-encoder retrieves top-100 from the index (milliseconds), cross-encoder re-ranks the top-100 to produce the top-5 (tens of milliseconds). On Bayan, re-ranking lifts MRR@10 from 0.61 to 0.74 for ~45 ms extra at k=50 — the benchmark table participants fill in Lab 5. The pattern generalises: cheap-filter-then-expensive-judge appeared in M2's case study (classifier gating extraction) and returns in AIE-214 as retrieve-then-generate.

### 4. Approximate nearest neighbours: FAISS index choices

Exact search compares the query against every vector — fine to ~10⁵ vectors on CPU, then latency grows linearly. ANN indexes trade tiny recall losses for large speedups:

| Index | How | Memory | Build | Query | Use when |
|---|---|---|---|---|---|
| `IndexFlatIP` | Exact inner product | vectors as-is | none | O(N) | ≤ ~100k vectors — **Bayan's answer**; exactness simplifies debugging |
| `IndexIVFFlat` | Cluster, probe nearest `nprobe` cells | + centroids | needs training pass | sub-linear | 10⁵–10⁷ vectors; tune nprobe for recall |
| `IndexHNSWFlat` | Navigable small-world graph | + graph links | incremental | logarithmic-ish | Low-latency serving, no training pass |
| + `PQ` variants | Product quantisation compresses vectors | ~10–30× smaller | training pass | fast, lossy | RAM-bound corpora |

Method: **measure recall@k of the ANN index against the flat index** on your own queries before adopting it — a one-cell experiment (Lab 5 stretch) that replaces folklore with a number. Persistence and versioning: an index is a build artefact derived from (model version × preprocessing version × corpus snapshot); rebuilding on model upgrade is mandatory — mixing vectors from two encoder versions in one index is the retrieval flavour of the tokenizer-mismatch bug, and nothing crashes.

### 5. Multilingual and cross-lingual retrieval

`paraphrase-multilingual-MiniLM-L12-v2` and siblings are trained so translations land close together: one index serves Arabic and English documents, and an English query retrieves Arabic cases (and vice versa). Facts to teach honestly: cross-lingual retrieval is 5–10 recall points behind monolingual on typical benchmarks — measure the gap on the Bayan bilingual query set rather than assuming it away; Arabic normalisation (M4) must be applied identically at index-build and query time (the skew canary grows an embedding check: one pinned sentence → pinned vector hash); and dialect text embeds worse than MSA (pretraining scarcity again) — the sliced-evaluation habit applies to retrieval too, and Lab 6 will slice recall@10 by language exactly as it slices F1.

### 6. Common mistakes & production considerations

1. **Skipping normalisation on one side** — query vectors unnormalised against a normalised index; plausible-but-wrong rankings.
2. **Using a classification fine-tune as an embedder** — Day-2's topic classifier produces clustered-by-topic vectors, terrible for within-topic similarity; embedding models are their own artefact class.
3. **Indexing whole documents** — 40-sentence case notes averaged into one mud vector; chunk, then aggregate.
4. **No labelled query set** — retrieval "evaluated" by eyeballing three queries; build the 150-query labelled set first (Lab 5 provides it; real projects must budget for it).
5. **Stale index after model or preprocessing upgrade** — mixed-version vectors; index metadata must pin model + preprocessing versions, asserted at load.
6. **Cross-encoder on the full corpus** — someone will try to re-rank 100k candidates; the two-stage pattern exists because arithmetic says so.

Production: embed at write-time (new cases embedded on ingestion, not batch-nightly) or accept the staleness window explicitly; monitor the *no-good-match rate* (score-below-threshold fraction) as a drift signal; GPU is optional for serving bi-encoders (MiniLM encodes a query in ~15 ms on CPU) but batch index builds want it; memory-map large indexes rather than loading per-worker.

## Code Examples

### Building the Bayan case index

```python
# src/bayan/search_index.py
"""Embed → normalise → index → persist. The index is a versioned build
artefact: (embedding model × preprocessing × corpus snapshot)."""
import json

import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

from bayan.arabic import ARABIC_PREPROC_VERSION, normalize_arabic
from bayan.preprocessing import PREPROC_VERSION

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def build_index(cases_csv: str, out_prefix: str) -> None:
    model = SentenceTransformer(MODEL_NAME)
    df = pd.read_csv(cases_csv)                      # resolved historical cases
    texts = [normalize_arabic(t) if lang == "ar" else t
             for t, lang in zip(df.summary, df.lang)]

    emb = model.encode(texts, batch_size=64, show_progress_bar=True,
                       convert_to_numpy=True)
    faiss.normalize_L2(emb)                          # cosine via inner product
    index = faiss.IndexFlatIP(emb.shape[1])          # exact: 20k cases, CPU-fine
    index.add(emb)

    faiss.write_index(index, f"{out_prefix}.faiss")
    df[["case_id", "summary", "resolution", "lang"]].to_parquet(
        f"{out_prefix}_meta.parquet")
    json.dump({"model": MODEL_NAME, "dim": int(emb.shape[1]),
               "preproc": PREPROC_VERSION, "arabic_preproc": ARABIC_PREPROC_VERSION,
               "n_vectors": int(index.ntotal)},
              open(f"{out_prefix}_manifest.json", "w"))
```

### Two-stage search: retrieve, then re-rank

```python
# src/bayan/search.py
"""Bi-encoder recall, cross-encoder precision. The production pattern."""
import json

import faiss
import pandas as pd
from sentence_transformers import CrossEncoder, SentenceTransformer

from bayan.arabic import normalize_arabic

RERANKER = "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"   # multilingual CE


class CaseSearch:
    def __init__(self, prefix: str):
        self.manifest = json.load(open(f"{prefix}_manifest.json"))
        self.index = faiss.read_index(f"{prefix}.faiss")
        self.meta = pd.read_parquet(f"{prefix}_meta.parquet")
        self.encoder = SentenceTransformer(self.manifest["model"])
        self.reranker = CrossEncoder(RERANKER)
        assert self.index.ntotal == self.manifest["n_vectors"]   # load canary

    def search(self, query: str, k: int = 5, candidates: int = 50,
               min_score: float = 0.25) -> list[dict]:
        q = self.encoder.encode([normalize_arabic(query)],
                                convert_to_numpy=True)
        faiss.normalize_L2(q)
        scores, idx = self.index.search(q, candidates)           # stage 1

        cand = self.meta.iloc[idx[0]].copy()
        pairs = [(query, s) for s in cand.summary]
        cand["ce_score"] = self.reranker.predict(pairs)          # stage 2
        cand = cand.sort_values("ce_score", ascending=False).head(k)

        if cand.ce_score.max() < min_score:                      # honest empty
            return []
        return cand.to_dict("records")
```

### Retrieval evaluation: recall@k and MRR

```python
# notebooks/05_retrieval_eval.py
"""No labelled query set, no retrieval claims. 150 queries, graded relevance."""
import numpy as np
import pandas as pd

from bayan.search import CaseSearch

queries = pd.read_json("data/bayan_queries.jsonl", lines=True)
# columns: query, lang, relevant_case_ids (1-3 per query, human-judged)

search = CaseSearch("artifacts/case_index_v1")


def evaluate(k: int = 10, rerank: bool = True) -> dict:
    hits, rr = [], []
    for _, row in queries.iterrows():
        results = (search.search(row.query, k=k, candidates=50) if rerank
                   else search.search(row.query, k=k, candidates=k))
        ids = [r["case_id"] for r in results]
        rank = next((i + 1 for i, c in enumerate(ids)
                     if c in row.relevant_case_ids), None)
        hits.append(rank is not None)
        rr.append(1 / rank if rank else 0.0)
    return {"recall@k": float(np.mean(hits)), "mrr": float(np.mean(rr))}


for rerank in (False, True):
    m = evaluate(rerank=rerank)
    print(f"rerank={rerank!s:5s}  recall@10={m['recall@k']:.2f}  "
          f"MRR@10={m['mrr']:.2f}")
# Reference output (Bayan query set):
#   rerank=False  recall@10=0.83  MRR@10=0.61
#   rerank=True   recall@10=0.85  MRR@10=0.74   ← CE fixes the ORDER, mostly
```

### Cross-lingual spot check

```python
# notebooks/05_crosslingual_probe.py
"""One embedding space, two languages: EN query -> AR case."""
from bayan.search import CaseSearch

search = CaseSearch("artifacts/case_index_v1")
for r in search.search("street light broken for two weeks", k=3):
    print(f"[{r['lang']}] {r['ce_score']:.2f}  {r['summary'][:60]}")
# Top hit is an Arabic case: "عمود الإنارة معطل في شارعنا منذ أسبوعين..."
# — translations land close in the multilingual space. Measure, don't marvel:
# the bilingual query slice quantifies the cross-lingual gap in Lab 5.
```

## Hands-on Lab 5 — Bilingual Semantic Search over Historical Cases

| | |
|---|---|
| **Objective** | Build the Bayan case-search component: FAISS index over 20k resolved cases, two-stage retrieval, evaluated at recall@10 ≥ 0.80 and MRR@10 ≥ 0.70 on the labelled bilingual query set |
| **Duration** | 50 minutes |
| **Setup** | `pip install sentence-transformers faiss-cpu`; `git checkout lab5-start`; `data/bayan_cases.csv` (20k resolved cases) + `data/bayan_queries.jsonl` (150 judged queries, 40% Arabic) |

**Instructions & tasks**

1. *(10 min)* Complete `build_index`: encode, **normalise**, index, persist with manifest. The provided test checks the manifest pins model + preprocessing versions.
2. *(10 min)* Implement stage-1 search; run the 150-query evaluation *without* re-ranking; record recall@10 and MRR@10 in `BENCHMARKS.md`.
3. *(10 min)* Add cross-encoder re-ranking; re-run the evaluation; record the MRR lift and the added latency per query (time both stages separately).
4. *(10 min)* Slice the evaluation by query language (EN query→AR doc counts as cross-lingual); record the cross-lingual gap; tune `min_score` on the 20 no-answer queries so the empty-result behaviour is honest.
5. *(5 min)* Run the planted-bug check: branch `sim-unnormalized` serves an index built without `normalize_L2`; explain in one sentence why its results look plausible; commit `feat(search): two-stage bilingual case search, MRR@10 0.74`.
6. *(5 min stretch)* Swap `IndexFlatIP` for `IndexHNSWFlat`; measure recall-vs-flat and query latency; one-line verdict for a 20k corpus. (flat wins; HNSW is for the 2M-case future)

**Expected output**
```
index built: 20,000 vectors, dim=384, manifest pinned
stage 1 only:   recall@10=0.83  MRR@10=0.61   (encode+search: 18 ms/query CPU)
with re-rank:   recall@10=0.85  MRR@10=0.74   (+45 ms/query at candidates=50)
cross-lingual slice: recall@10=0.78 (monolingual 0.88) — gap recorded
no-answer queries: 18/20 correctly return []  (min_score=0.25)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| recall@10 ≈ 0.4, long documents dominate results | Missing `normalize_L2` on index or query side | Normalise both; this is `sim-unnormalized` — did you just build it yourself? |
| Arabic queries score far below English | Query path skips `normalize_arabic` while index used it | Same normalisation both sides; extend the skew canary with the pinned-vector check |
| Re-ranking makes results *worse* | Monolingual English cross-encoder on Arabic pairs | Use the multilingual CE (`mmarco-mMiniLMv2`); check the model card's languages |
| Evaluation takes > 5 min | Cross-encoder on 50 candidates × 150 queries on CPU without batching | `reranker.predict(pairs, batch_size=64)`; or candidates=25 for the lab |
| MRR fine, users complain results are "same case five times" | Near-duplicate cases in the corpus | Deduplicate at index-build (embedding similarity > 0.95 → keep newest) — stretch task |

**Instructor notes.** Task 5's planted bug is the module's teeth: the unnormalised index returns *plausible* results — long, keyword-rich cases — and eyeballing approves them; only the metric catches it. Say the sentence explicitly: *retrieval without a labelled query set is vibes*. The stage-timing numbers from task 3 seed M7's latency-budget thinking — have pairs post encode/search/re-rank timings to the shared board and leave them up. Fast finishers: HNSW comparison (task 6), embedding-similarity dedup, or index the *resolutions* separately and search both fields.

## Mini Exercises

**Quiz (5 questions)**
1. Why is raw pretrained `[CLS]` a poor sentence embedding? → never trained for similarity; contrastive fine-tuning (SBERT) shapes the space so cosine means similarity.
2. What exactly breaks when only the index side is L2-normalised? → inner product mixes direction with query magnitude; rankings skew toward dense/long texts, silently.
3. Bi-encoder vs cross-encoder: which pre-computes, which sees token interaction, and the pattern that uses both? → bi-encoder pre-computes docs; CE sees interactions; retrieve-then-re-rank.
4. When does `IndexFlatIP` beat every ANN index? → small corpora (≲100k): exact, zero tuning, simpler debugging — speed isn't a constraint yet.
5. Your encoder gets upgraded from v1 to v2. What must happen to the index, and why? → full rebuild; v1/v2 vectors are incomparable spaces — the tokenizer-mismatch bug's retrieval twin.

**Debugging exercise.** Branch `sim-stale-index`: the corpus grew 4k new cases but the index wasn't rebuilt; users report "recent cases never come up". Participants must find the mismatch (manifest `n_vectors` vs corpus rows), then design the fix class: write-time embedding or scheduled rebuild with staleness SLO — and say which Bayan should choose (write-time; case volume is low).

**Code-review exercise.** Review a PR that: embeds with the Day-2 *topic classifier's* encoder ("we already have it deployed"), indexes full 40-sentence documents as one vector, and re-ranks all 20k cases with the cross-encoder "for accuracy". Three findings with the harm and fix for each.

**Discussion questions.**
- The service desk wants "no results" shown rather than bad results. Where does that threshold come from, who owns its false-negative cost, and how does the no-answer query slice inform it?
- One multilingual index vs two monolingual indexes with query-language routing: argue both sides using the cross-lingual gap you measured.

## Case Study — Semantic FAQ Deflection at a Saudi Retail Bank

**Scenario.** A retail bank's app has a search box over 900 FAQ and help articles. Keyword search satisfies 31% of queries; everything else becomes a call or chat session at SAR 18 average handling cost. The content team's response — writing more keyword variants into articles — has made articles unreadable without moving the number. A two-engineer team gets six weeks to fix search before the bank licenses a conversational-AI suite at forty times the cost.

**Business context.** 1.4M in-app searches monthly; every 10-point deflection gain saves roughly SAR 2.5M annually. The conversational-suite decision hinges on this pilot: if plain semantic search closes most of the gap, the LLM procurement gets re-scoped from "replace search" to "add generation on top of it" — a far smaller cheque.

**Technical challenge.** Queries are short (median 4 words), heavily dialectal ("وش رسوم التحويل الدولي"), often Arabizi, and the FAQ articles are formal MSA and English — a register *and* language mismatch that defeats keyword matching by construction.

**Constraints.** On-prem serving only (banking data residency); 150 ms search-latency budget at p95; content team owns article text and will not restructure 900 articles; six weeks includes evaluation-set construction.

**Solution approach (facilitate, don't lecture).** Week 1 builds the labelled set *first*: 400 real queries sampled from logs, judged against articles by the content team — the pilot's spine. The build: multilingual MiniLM bi-encoder; articles chunked by section (the H2 structure was there all along) with title prepended to each chunk; FAISS flat index (900 articles ≈ 5k chunks — exactness is free); dialect normalisation (M4 profile) on the query path; cross-encoder re-rank of top-30. Results on the labelled set: keyword baseline recall@5 0.34 → bi-encoder 0.71 → +re-rank 0.79; Arabizi slice lags at 0.55 → a transliteration pre-step lifts it to 0.68. Deflection in the A/B pilot: 31% → 52%. The board decision re-scopes the conversational suite to RAG over *this* retrieval layer — the module's pattern becoming procurement strategy.

**Discussion questions.**
1. Why was building the labelled query set week 1 rather than week 5 the highest-leverage decision in the project?
2. Prepending the article title to every chunk lifted recall 4 points. Form a hypothesis for why, and design the ablation that tests it.
3. The Arabizi slice still lags after transliteration. Present the options (better transliteration, Arabizi-inclusive embedder, UI language toggle) with cost and evidence for each.
4. The vendor argues their end-to-end suite "makes retrieval quality irrelevant". Using what this module measured, rebut in three sentences — then name what the suite *would* add. (generation, dialogue state — on top of, not instead of, retrieval)

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| recall@10 (bi-encoder, all queries) | Quality | ≥ 0.80 | 150-query labelled set |
| MRR@10 with re-ranking | Quality | ≥ 0.70 | labelled set |
| Cross-lingual slice recall@10 | Quality | measured + gap recorded | language-sliced eval |
| No-answer honesty | Quality | ≥ 17/20 empty-correct | no-answer query slice |
| Stage-1 query latency (CPU) | Performance | ≤ 30 ms p50 | timing harness |
| End-to-end with re-rank (candidates=50) | Performance | ≤ 100 ms p50 | timing harness |
| Index manifest integrity | Reliability | versions pinned + asserted at load | load canary test |

**Example benchmark table (filled during lab):**

| Configuration | recall@10 | MRR@10 | p50 latency/query |
|---|---|---|---|
| Keyword baseline (BM25, provided) | 0.62 | 0.44 | 4 ms |
| Bi-encoder only (MiniLM, flat) | 0.83 | 0.61 | 18 ms |
| + cross-encoder re-rank (k=50) | 0.85 | 0.74 | 63 ms |
| Cross-lingual slice (with re-rank) | 0.78 | 0.66 | 63 ms |

## Required Visuals and Training Assets

### Diagrams
1. **The two-stage retrieval pipeline** — *Purpose:* module anchor. *Elements:* query → normalise → encode → FAISS top-50 (fast/cheap lane) → cross-encoder → top-5 (slow/smart lane); latency badges on each stage; offline lane below showing corpus → chunks → embeddings → index with the version manifest. *Style:* two-lane flow, course palette. *Designer note:* draw the offline/online boundary as a wall — students must see the index is a *build artefact*.
2. **Embedding space, before and after SBERT** — *Elements:* 2-D projection: raw-BERT `[CLS]` cloud (paraphrases scattered) vs sentence-transformer space (paraphrase pairs adjacent, AR/EN translations co-located); three labelled example pairs. *Style:* side-by-side scatter with connecting lines.
3. **Bi-encoder vs cross-encoder** — *Elements:* siamese towers with a cosine bridge vs one tower consuming `query [SEP] doc`; pre-compute badge on the bi-encoder, per-pair-cost badge on the CE; the retrieve-then-re-rank handshake between them. *Style:* architecture comparison card.
4. **Index-choice ladder** — *Elements:* corpus size axis with flat → IVF → HNSW → PQ rungs; recall/latency/memory trade-off icons; a "you are here (20k)" marker on flat. *Style:* decision ladder, printable A4.

### Images (screenshots)
1. **Retrieval evaluation console output** — *why:* expected-state reference; *content:* the rerank=False/True comparison exactly as the lab prints it.
2. **Cross-lingual hit** — *why:* the module's magic moment; *content:* English query returning an Arabic case with scores.
3. **Unnormalised-index results side by side** — *why:* the plausible-but-wrong trap; *content:* same query, normalised vs unnormalised top-5, long-document bias visible.
4. **Index manifest JSON** — *why:* versioning discipline; *content:* model, dim, preproc versions, vector count.

### Simulations
1. **The unnormalised index** — *Setup:* branch `sim-unnormalized`. *Expected:* plausible-looking results, recall@10 collapses to ~0.4; caught only by the metric. *Learning objective:* retrieval quality is measured, never eyeballed.
2. **Stale index drift** — *Setup:* branch `sim-stale-index` (corpus grew, index didn't). *Expected:* "recent cases missing" reports; manifest count mismatch reveals it. *Learning objective:* indexes have freshness contracts.

### Interactive Activities
- **Human retrieval (10 min):** pairs receive one query and eight printed case summaries; rank by relevance, then compare with the bi-encoder's ranking and the CE's — where do humans and models disagree, and which model disagrees *less*?
- **Threshold auction (10 min):** given ten borderline query-result pairs with CE scores, the class sets `min_score` by voting show/hide per pair — then compares its collective threshold to the tuned one.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `bayan_cases.csv` | Synthetic resolved-case corpus (course-generated, AR/EN, with resolutions) | CSV | 20,000 cases | Index corpus |
| `bayan_queries.jsonl` | Course-judged query set (incl. 20 no-answer queries, 40% AR) | JSONL | 150 queries | Retrieval evaluation |
| BM25 baseline results | Provided script output | JSONL | 150 rows | Baseline comparison |

### Demo Requirements
- **Instructor demo:** live cross-lingual search on the projector (English query → Arabic case), then the `sim-unnormalized` reveal: same query, both indexes, metric verdict.
- **Student demo:** one pair defends their `min_score` choice using the no-answer slice; one pair presents the cross-lingual gap number and what they'd do about it.
- **Expected outputs:** versioned index + search module in `artifacts/` — the capstone's search endpoint wraps it, and Lab 6 slices its recall by language.

---

# Module 6 — Evaluation and Error Analysis for NLP

## Module Overview

**Purpose.** Every module so far produced a number; this module decides whether to believe it. Participants learn task-appropriate metrics (and the failure of accuracy on imbalanced text tasks), sliced evaluation as the default rather than the audit exception, bootstrap confidence intervals so that "+0.8 F1" stops being treated as fact, behavioural testing (invariance and directional tests for NLP), systematic error analysis with an error taxonomy, and the model card as the artefact that carries all of it. The Bayan models built in Labs 3–5 get their honest report card — and several of their numbers change.

**Business relevance.** The gap between claimed and delivered accuracy is where NLP projects die — M3's telecom case put the pattern on the table (88 claimed, 79 delivered), and this module teaches the machinery that closes it. Sliced evaluation is also becoming regulation-shaped: fairness across dialect groups, documented limitations, and evidence-backed claims are what national AI-governance frameworks increasingly require of deployed systems. The engineer who can produce a defensible evaluation report — metrics with confidence intervals, per-slice tables, known failure modes — is the one whose systems survive procurement review, audit, and contact with live traffic.

**Industry use cases.**
- A ministry procurement team runs a bake-off between two vendor NLP systems; the decision must survive vendor protest, so every claimed difference needs a confidence interval.
- A bank's model-risk team requires per-segment performance evidence before any customer-facing NLP model ships — dialect and language slices included.
- An operations team triages a "model got worse" complaint: error analysis distinguishes drift, a data-pipeline bug, and normal variance in one afternoon instead of one month.

**Expected competencies.** Participants can choose and defend task-appropriate metrics, produce sliced evaluations by language/dialect/class/length, attach bootstrap confidence intervals to any metric, write behavioural tests that model updates must pass, run a disciplined error-analysis session that outputs a labelled error taxonomy and a prioritised fix list, and assemble a model card.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Select task-appropriate metrics and explain what each hides | LO5 |
| 6.2 | Produce sliced evaluations across language, dialect, class, and length | LO5 |
| 6.3 | Attach bootstrap confidence intervals to metrics and compare models honestly | LO5 |
| 6.4 | Write behavioural (invariance/directional) tests for NLP models | LO5, LO3 |
| 6.5 | Run systematic error analysis producing a taxonomy and prioritised fixes | LO5 |
| 6.6 | Assemble a model card that carries metrics, slices, and limitations | LO5, LO6 |

## Technical Content

### 1. Task-appropriate metrics — and what each one hides

The course has already used the right metrics; now make the choices explicit and defensible:

- **Classification:** accuracy dies on imbalance (predicting "outage" always scores 41% on Bayan and 0 usefulness). **Macro-F1** weights classes equally — the minority-class advocate; **weighted-F1** follows traffic; report both, decide by *cost structure*: if missing the 2% "other-digital-services" class is expensive, macro is your headline. Per-class precision/recall is where decisions live: the confusion matrix is the diagnostic, the scalar is the summary.
- **NER:** entity-level F1 via seqeval (M3's lesson), with the strictness caveat — a one-token boundary miss scores zero; report *relaxed/partial-match* alongside strict when boundaries are genuinely fuzzy (dates), and per-entity-type always (SERVICE at 0.74 hides inside an 0.83 aggregate).
- **Extractive QA:** exact match (EM) and token-overlap F1; for the unanswerable class, the null-accuracy trade-off curve against the threshold (M3's `null_threshold` finally gets tuned with evidence, not vibes).
- **Retrieval:** recall@k (did anything relevant arrive?) and MRR (did it arrive *first*?) — M5's pair; choose k from the UI (users see 5 results → recall@5 is the product metric, recall@50 is the re-ranker's input budget).
- **The meta-rule:** the metric is a *proxy* for a business quantity (mis-routed tickets, missed escalations, deflected calls). Write the mapping down; when the proxy and the business number diverge, the proxy loses.

### 2. Sliced evaluation as the default

One aggregate number is an average over stories, and averages hide the stories that matter. The course has planted the evidence: M4's bake-off (+3 aggregate was +6 on the Gulf slice), M5's cross-lingual gap (0.88 vs 0.78). Method, not inspiration:

- **Standard slices for bilingual NLP:** language (AR/EN), dialect region (M4's audit column), class/entity type, input length (short chat vs long complaint — length correlates with truncation and with dialect), channel (web form vs WhatsApp), and time (last month vs training period — the drift preview).
- Slices need **minimum sizes** to mean anything: a slice of 30 examples has a ±13-point F1 confidence interval — flag small slices in the report rather than deleting them (absence is information: "we cannot yet evaluate Maghrebi dialect" is a finding).
- **Disaggregate before celebrating and before panicking:** improvements and regressions both concentrate; the per-slice delta table is the change-review artefact for any model update, and the capstone's evaluation report requires it.

### 3. Bootstrap confidence intervals: the end of "+0.8"

M3 planted the seed variance fact (±1.5 F1 across seeds); the bootstrap generalises it to *test-set* variance. Resample the test set with replacement 1,000 times, recompute the metric each time, take the 2.5th/97.5th percentiles: a 95% CI in eight lines of NumPy, no distributional assumptions, works for any metric including seqeval F1 and MRR. For **model comparison**, bootstrap the *paired difference* on the same resamples — if the difference CI contains zero, you have a coin flip wearing a decimal point. Rules of thumb participants take away: 1,200 test examples → roughly ±2 points of F1 CI; slices inherit *wider* intervals; and any claimed improvement smaller than the CI half-width is not yet a claim — it is a hypothesis needing more data. This single habit would have saved the M3 telecom team its credibility.

### 4. Behavioural testing: unit tests for language behaviour

Metrics measure *aggregate* correctness on one distribution; behavioural tests probe *specific capabilities* the metric can't see (the CheckList framing, adapted to Bayan):

- **Invariance tests:** the prediction must NOT change when meaning doesn't — swap a Riyadh neighbourhood for a Jeddah one in an outage complaint (topic must hold), add the greeting "السلام عليكم" prefix (sentiment must hold), replace a name with another name (NER types must hold), tatweel elongation (everything must hold — M1's normaliser earns its keep here).
- **Directional tests:** the prediction MUST change appropriately — negate the complaint's resolution ("تم الحل" → "لم يتم الحل") and sentiment must not improve; append "and now it happened again" and urgency-adjacent outputs should not decrease.
- **Minimum functionality tests:** templated basics that must always pass — every service name in the registry, standing alone in a template, must be extracted as SERVICE.
- Mechanics: templates × term lists generate hundreds of cases cheaply; failures are *rates* per test type, tracked across model versions — they enter CI exactly like AIE-113's golden tests, and a fine-tune that lifts F1 while doubling the negation-failure rate is a regression, caught before shipping.

### 5. Error analysis: from failure pile to fix list

The discipline that turns "the model is wrong sometimes" into an engineering queue:

1. **Collect** every validation error (never the frozen test set — analysis is tuning, and touching test for it is leakage) plus behavioural-test failures.
2. **Read them.** 100 errors, by hand, in a spreadsheet — the step everyone wants to skip and the step that finds everything. Each error gets hypothesis tags from a growing **taxonomy**: label noise, truncation, dialect gap, negation, entity-boundary, class-confusion (billing↔digital_services — the Lab 3 prediction-market bet gets settled here), preprocessing artefact, genuinely-hard.
3. **Count.** The taxonomy histogram is the prioritisation: on Bayan's classifier, label noise (23%) and the billing↔digital_services confusion (19%) dominate; dialect-gap errors cluster in *short* messages (the slice interaction the aggregate never shows).
4. **Cost the fixes:** relabel noisy classes (annotation budget), merge or clarify confusable classes (product decision, not modelling), dialect data (M4's answer), truncation policy (M1's answer). Each fix is an experiment with a predicted metric delta — error analysis produces *hypotheses*, the next fine-tune tests them.
5. Close the loop with **regression artefacts:** every diagnosed error class becomes a behavioural test or a golden-set addition, so the same failure cannot ship twice unnoticed.

### 6. Common mistakes & production considerations

1. **Tuning on the test set** — every "quick look" leaks; the frozen-test discipline from M3 is the whole defence, and the error-analysis-on-validation rule is its corollary.
2. **Comparing models on different test sets** (or different preprocessing of the same set) — non-claims; pin the evaluation set version like a model artefact.
3. **Reporting the aggregate without slices** — the M4/M5 evidence made this vivid; the report template makes it structurally impossible.
4. **Metric theatre:** subword-level NER scores, accuracy on imbalanced classes, recall@50 sold as user-facing quality — each inflates by construction; name them in review.
5. **CI-free deltas:** "+0.8" without an interval; the paired bootstrap is one function call away.
6. **One-off analysis:** an error analysis that lives in someone's notebook and dies there; taxonomy, tests, and the model card are how findings persist.

Production: the **model card** (per checkpoint: intended use, training data version, metrics with CIs, slice table, behavioural-test rates, known limitations, contacts) ships with every artefact — the capstone requires one per model; evaluation sets are versioned data artefacts with change logs; live-traffic sampled audits (M3's telecom fix) are scheduled, not heroic; and drift monitoring — the *ongoing* form of everything here — is deliberately deferred to SDA-AIE-216, but the slice definitions written today are exactly what that module will monitor.

## Code Examples

### Bootstrap confidence intervals and paired comparison

```python
# src/bayan/eval_stats.py
"""Bootstrap CIs: any metric, no distributional assumptions, 8 lines each."""
import numpy as np


def bootstrap_ci(y_true, y_pred, metric_fn, n_boot: int = 1000,
                 alpha: float = 0.05, seed: int = 42) -> tuple:
    rng = np.random.default_rng(seed)
    n, stats = len(y_true), []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)                    # resample WITH replacement
        stats.append(metric_fn(y_true[idx], y_pred[idx]))
    lo, hi = np.percentile(stats, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return float(np.mean(stats)), float(lo), float(hi)


def paired_bootstrap_diff(y_true, pred_a, pred_b, metric_fn,
                          n_boot: int = 1000, seed: int = 42) -> dict:
    """Difference CI on the SAME resamples: is B actually better than A?"""
    rng = np.random.default_rng(seed)
    n, diffs = len(y_true), []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        diffs.append(metric_fn(y_true[idx], pred_b[idx])
                     - metric_fn(y_true[idx], pred_a[idx]))
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    return {"diff_mean": float(np.mean(diffs)), "ci": (float(lo), float(hi)),
            "significant": not (lo <= 0 <= hi)}
```

### The sliced evaluation report

```python
# src/bayan/eval_report.py
"""One function, every model, every slice — the report is generated, not written."""
from functools import partial

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score

from bayan.eval_stats import bootstrap_ci

macro_f1 = partial(f1_score, average="macro")

SLICES = ["lang", "dialect_region", "channel", "length_bucket"]
MIN_SLICE = 50                                   # below this: flag, don't trust


def sliced_report(df: pd.DataFrame) -> pd.DataFrame:
    """df columns: y_true, y_pred, + slice columns. Returns the report table."""
    rows = []
    for slice_col in ["ALL"] + SLICES:
        groups = [("all", df)] if slice_col == "ALL" \
            else list(df.groupby(slice_col))
        for name, g in groups:
            mean, lo, hi = bootstrap_ci(g.y_true.to_numpy(),
                                        g.y_pred.to_numpy(), macro_f1)
            rows.append({"slice": f"{slice_col}={name}", "n": len(g),
                         "macro_f1": round(mean, 3),
                         "ci_95": f"[{lo:.3f}, {hi:.3f}]",
                         "flag": "SMALL SLICE" if len(g) < MIN_SLICE else ""})
    return pd.DataFrame(rows)

# Reference output (Bayan topic classifier, seed 42):
#   slice                      n     macro_f1  ci_95            flag
#   ALL=all                    2400  0.820     [0.803, 0.836]
#   lang=ar                    1610  0.801     [0.780, 0.821]
#   lang=en                    790   0.856     [0.831, 0.879]
#   dialect_region=Gulf        882   0.762     [0.729, 0.793]   ← the story
#   dialect_region=MSA         728   0.844     [0.815, 0.870]
#   length_bucket=short(<16w)  693   0.771     [0.735, 0.804]
#   ...
```

### Behavioural tests for the Bayan models

```python
# tests/test_behavioural.py
"""Invariance and directional tests — CI-enforced, tracked per model version."""
import pytest

from bayan.serve_local import classify_sentiment, classify_topic, extract_entities

NEIGHBOURHOODS = ["النرجس", "العليا", "الروضة", "السلامة"]      # swap-invariant


@pytest.mark.parametrize("hood", NEIGHBOURHOODS)
def test_topic_invariant_to_location(hood):
    text = f"انقطعت الكهرباء في حي {hood} منذ ثلاث ساعات"
    assert classify_topic(text) == "outage"            # location must not matter


def test_sentiment_invariant_to_greeting():
    base = "الخدمة تأخرت كثيرا ولم يرد أحد على طلبي"
    assert (classify_sentiment("السلام عليكم، " + base)
            == classify_sentiment(base))               # politeness ≠ positivity


def test_sentiment_directional_negation():
    resolved = "تم حل المشكلة وأشكركم على سرعة الاستجابة"
    unresolved = "لم يتم حل المشكلة رغم مرور أسبوعين"
    order = ["negative", "neutral", "positive"]
    assert order.index(classify_sentiment(unresolved)) \
        < order.index(classify_sentiment(resolved))    # negation must bite


def test_ner_mft_service_registry():
    """Minimum functionality: every registry service name is extractable."""
    misses = []
    for service in open("data/service_registry.txt", encoding="utf-8").read().split("\n"):
        if not service:
            continue
        ents = extract_entities(f"أواجه مشكلة في خدمة {service} منذ يومين")
        if not any(e["label"] == "SERVICE" and service in e["text"] for e in ents):
            misses.append(service)
    assert len(misses) / 41 < 0.10, f"MFT failure rate too high: {misses}"
```

### The error-analysis worksheet driver

```python
# notebooks/06_error_analysis.py
"""Materialise the error pile for hand-reading; count the taxonomy after."""
import pandas as pd

val = pd.read_parquet("artifacts/topic_val_predictions.parquet")
errors = val[val.y_true != val.y_pred].copy()

# The columns a human needs to diagnose, nothing else:
sheet = errors[["text", "y_true", "y_pred", "confidence",
                "lang", "dialect_region", "n_words"]]
sheet["taxonomy_tag"] = ""                       # filled BY HAND — that's the point
sheet["fix_hypothesis"] = ""
sheet.sample(min(120, len(sheet)), random_state=42) \
     .to_csv("reports/error_worksheet.csv", index=False)

print(f"{len(errors)} errors → 120 sampled for hand-reading")
print(errors.groupby(["y_true", "y_pred"]).size().nlargest(5))
# Top confusion: billing → digital_services (both mention fees/رسوم)
# — the Lab 3 prediction market pays out here.
```

## Hands-on Lab 6 — The Evaluation Report

| | |
|---|---|
| **Objective** | Produce the honest report card for every Bayan model: sliced metrics with bootstrap CIs, behavioural-test rates, a hand-built error taxonomy with prioritised fixes, and a model card per artefact |
| **Duration** | 50 minutes |
| **Setup** | `git checkout lab6-start`; all Lab 3–5 artefacts + validation predictions pre-materialised; `pip install seqeval` already present |

**Instructions & tasks**

1. *(10 min)* Implement `bootstrap_ci` and `paired_bootstrap_diff`; answer the planted question: Lab 3's classifier (0.820) vs the stretch two-headed variant (0.828) — real improvement or noise? (CI of the difference straddles zero: noise)
2. *(10 min)* Run `sliced_report` on the topic classifier and the M4 dialect-aware variant; write the two-sentence headline a manager would read (the Gulf slice is the story; the aggregate is the summary).
3. *(10 min)* Complete the four behavioural-test skeletons; run against both classifier versions; record failure rates per test type in `BENCHMARKS.md` — note where the M4 model wins behaviourally despite similar aggregates.
4. *(15 min)* The hand-reading: 120 sampled errors, taxonomy tags in pairs (taxonomy starter provided; extend it when a class doesn't fit); produce the histogram and the top-3 prioritised fixes *with predicted metric deltas*.
5. *(5 min)* Generate the model card from the template (`model_card.md.j2` — metrics, slices, behavioural rates, limitations auto-filled; *known limitations* written by hand); commit `docs(eval): sliced report + taxonomy + model cards`.

**Expected output**
```
paired diff (two-head vs single): +0.008  CI [-0.006, +0.021]  → NOT significant
sliced report: 14 rows, Gulf slice 0.762 [0.729, 0.793] flagged as headline
behavioural: invariance 96% | negation-directional 88% | MFT services 39/41
taxonomy (120 errors): label-noise 23% | billing↔digital 19% | dialect-gap 17%
  | truncation 9% | negation 8% | boundary 7% | hard 17%
3 model cards committed to artifacts/*/MODEL_CARD.md
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Bootstrap CI absurdly wide on a slice | Slice n < 50 | That IS the finding — flag it, don't resample harder; more data or merged slices |
| Paired diff significant but tiny (+0.3) | Large n makes small effects detectable | Significance ≠ importance; report both the CI and the cost of switching |
| Behavioural tests all pass suspiciously | Tests hitting the *mock* serving stub | `serve_local` must load real artefacts; check the fixture flag |
| seqeval crashes on the NER slice report | -100 masks leaked into label lists | Filter to word-level predictions first (M3's alignment discipline) |
| Pairs disagree on taxonomy tags | Taxonomy categories overlap | Good — merge or split categories *as a class*; convergence is the exercise |

**Instructor notes.** Task 4 is the module: protect the 15 minutes fiercely — the temptation to script the reading defeats the point, and the pairs who read errors aloud to each other find the label noise fastest. Settle the Lab 3 prediction-market bets publicly against the confusion matrix; the room's bet is usually right about billing↔digital_services and wrong about which direction dominates. Close by resurfacing the "+3 or +6?" board note from Lab 4 — now answered with a CI. Fast finishers: sliced recall@10 for the M5 index by query language (the gap gets its interval), or the null-threshold trade-off curve for QA.

## Mini Exercises

**Quiz (5 questions)**
1. Why macro-F1 rather than accuracy for Bayan topics? → Zipfian classes; accuracy rewards predicting the majority; macro makes minority classes count.
2. Your improvement is +0.9 F1 and the paired-bootstrap CI is [-0.2, +2.0]. What do you say in review? → not yet a claim; the interval contains zero — gather data or accept it's indistinguishable.
3. Invariance vs directional test — one Bayan example of each? → location-swap must not change topic; negating resolution must not improve sentiment.
4. Why must error analysis run on validation, not the frozen test set? → analysis drives tuning decisions; touching test for it is leakage — the number stops predicting live traffic.
5. What belongs on a model card that a metrics table alone doesn't carry? → intended use, data version, slice table, behavioural rates, *known limitations*, contacts.

**Debugging exercise.** Branch `sim-eval-leak`: a helper "cleaned" the test set by dropping rows the model got wrong in a previous run ("obvious label errors"). Aggregate F1 jumps 4 points; nothing else changed. Participants must spot the survivorship bias, quantify it by restoring the rows, and write the rule: evaluation sets change only by versioned, documented curation — never conditioned on model output.

**Code-review exercise.** Review an evaluation PR claiming "new model +2.1 F1, ship it": single seed, no CI, aggregate only, evaluation set silently re-preprocessed with the new normaliser, and the behavioural suite deleted "because three tests failed". Four findings, each with the fix.

**Discussion questions.**
- The Gulf slice is 8 points behind and the fix costs 6,000 dialect annotations. The aggregate meets the contract SLA. Who decides whether to spend, and what does the slice table do to that conversation?
- A regulator asks "how do you know the model treats dialect speakers fairly?" — which artefacts from this module answer, and what's still missing? (slice CIs, behavioural rates; missing: outcome-level fairness, monitoring — AIE-216)

## Case Study — Procurement Bake-off at a National Health Call Centre

**Scenario.** A national health call centre (40k calls/day) is procuring an Arabic triage-note classification system. Two vendors passed the demo stage. Vendor A claims 91% accuracy; Vendor B claims 89% but includes a per-dialect breakdown in its proposal. The evaluation committee — two clinicians, a procurement officer, and one AI engineer (the participant's role) — must produce a decision that survives vendor protest and an eventual audit.

**Business context.** Triage-note classification feeds callback prioritisation: misclassifying an urgent-symptom note as routine has clinical consequences, so the *urgent* class's recall matters more than any aggregate. The contract runs five years; a wrong choice compounds.

**Technical challenge.** Design and run the bake-off: evaluation set, metrics, slices, statistical comparison, and behavioural probes — on infrastructure where vendor models are black-box APIs (no weights, no training data visibility).

**Constraints.** 3,000 historical triage notes can be labelled by clinicians within the timeline (each note needs two clinical annotators); vendor APIs are rate-limited; notes contain PHI — evaluation runs on-premises through an anonymisation gateway; the committee's non-technical members must be able to follow the decision logic.

**Solution approach (facilitate, don't lecture).** The engineer's design: a *committee-owned* evaluation set (never shared with vendors — the frozen-test discipline at procurement scale), stratified by dialect region, note length, and clinical urgency; headline metric chosen with the clinicians — urgent-class recall, with macro-F1 secondary; paired bootstrap on identical notes for the A-vs-B comparison. Results: A's 91% claim shrinks to 84.2% [82.9, 85.5] on the committee's set (its training data was clean MSA physician notes; live notes are dialect-heavy transcriptions); B scores 83.1% [81.7, 84.4] aggregate — statistically indistinguishable — but B's urgent-recall is 0.91 vs A's 0.83, and the paired difference CI excludes zero. Behavioural probes seal it: A's urgent-recall drops 11 points when symptoms are phrased in Gulf dialect; B's drops 3. The committee selects B, and the decision memo's core exhibit is the slice table with intervals — legible to the clinicians, defensible to the auditor, and immune to the vendors' aggregate-number theatre. Acceptance testing (quarterly, on a refreshed committee set) is written into the contract.

**Discussion questions.**
1. Why must the evaluation set never reach the vendors — and what real-world evidence from this course predicts what happens if it does?
2. Defend choosing urgent-class recall over macro-F1 as the headline, and name what that choice deliberately sacrifices.
3. Vendor A protests: "our internal benchmarks show 91%." Draft the two-sentence reply that a procurement officer could sign.
4. Design the quarterly acceptance test: set size, refresh policy, slices, and the threshold that triggers contract review.

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Bootstrap functions correctness | Correctness | provided unit tests 6/6 | pytest |
| Sliced report generated | Completeness | ≥ 12 slices, small slices flagged | report script |
| Paired-comparison verdicts | Rigour | 2 comparisons with CIs recorded | BENCHMARKS.md |
| Behavioural failure rates | Quality | invariance ≥ 95%, MFT ≥ 90% | test suite |
| Error taxonomy | Discipline | 120 errors tagged, histogram + top-3 fixes | worksheet review |
| Model cards | Discipline | 3 cards with hand-written limitations | artefact review |

**Example benchmark table (filled during lab):**

| Model | Aggregate macro-F1 [CI] | Gulf slice [CI] | Invariance pass | Negation pass |
|---|---|---|---|---|
| Topic classifier (M3, mix) | 0.820 [0.803, 0.836] | 0.762 [0.729, 0.793] | 96% | 84% |
| Dialect-aware (M4, DA) | 0.834 [0.818, 0.850] | 0.809 [0.778, 0.838] | 97% | 91% |
| Paired diff (DA − mix) | +0.014 [+0.004, +0.025] ✓ | +0.047 [+0.028, +0.066] ✓ | — | — |

## Required Visuals and Training Assets

### Diagrams
1. **The evaluation pyramid** — *Purpose:* module anchor. *Elements:* base = golden/unit tests (M1/M3), then behavioural suites, then sliced metrics with CIs, apex = live-traffic audit; each layer labelled with what it catches and when it runs. *Style:* layered pyramid, course palette. *Designer note:* mirror the classic test pyramid deliberately — participants know it from AIE-113.
2. **The aggregate, dissected** — *Elements:* one big 0.82 bar decomposing into slice bars with CI whiskers, the Gulf bar visibly low; the "+3 or +6?" motif from M4 resolved with intervals. *Style:* exploded bar chart — the M4 poster, completed.
3. **Paired bootstrap intuition** — *Elements:* two models' predictions on the same resampled sets; the difference distribution as a histogram with the zero line; two verdict examples (CI excluding vs straddling zero). *Style:* three-panel statistical explainer, no formulas bigger than the pictures.
4. **Error-analysis loop** — *Elements:* collect → read (a human icon, prominent) → tag → count → cost fixes → regression tests → retrain; arrows back into behavioural suites and golden sets. *Style:* circular flow with the human step visually largest.

### Images (screenshots)
1. **Sliced report console output** — *why:* expected-state reference; *content:* the 14-row table with the flag column and the Gulf headline.
2. **Behavioural test run** — *why:* NLP behaviour as CI output; *content:* pytest run with one directional failure expanded, showing the sentence pair.
3. **The error worksheet, mid-reading** — *why:* legitimise the manual step; *content:* spreadsheet with taxonomy tags half-filled, one disputed row highlighted.
4. **Finished model card** — *why:* the artefact standard; *content:* the dialect-aware classifier's card with slice table and limitations section.

### Simulations
1. **Survivorship-biased test set** — *Setup:* branch `sim-eval-leak` (error rows quietly dropped). *Expected:* +4 F1 from nothing; caught by set-size diff and version log. *Learning objective:* evaluation sets are immutable artefacts.
2. **The behavioural regression** — *Setup:* an "improved" checkpoint (+1 F1) whose negation-failure rate doubled. *Expected:* metric says ship, behavioural suite says block; participants must adjudicate. *Learning objective:* aggregate metrics are necessary, not sufficient.

### Interactive Activities
- **Error-reading jigsaw (15 min, inside Lab 6):** each pair reads a different 30-error shard, then shards merge taxonomies on the whiteboard — the class-level histogram emerges live.
- **"Ship it?" tribunal (10 min):** three model-update scenarios (metric up/behaviour down; aggregate flat/slice up; big gain/no CI); the class votes ship/block/measure-more, then defends against the instructor's cross-examination.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| Validation predictions (all models) | Materialised from Labs 3–5 artefacts | Parquet | 2,400 rows/model | Slicing + error analysis |
| Behavioural test templates | Course-crafted (terms × templates) | Python/CSV | ~400 generated cases | Behavioural suite |
| `service_registry.txt` | Course fixture | TXT | 41 services | MFT test |
| Taxonomy starter | Course handout | MD | 8 categories | Error-analysis worksheet |

### Demo Requirements
- **Instructor demo:** run the paired bootstrap live on the two-head-vs-single question and let the room watch a "+0.8 improvement" dissolve into a coin flip; then one behavioural failure read aloud in Arabic.
- **Student demo:** one pair presents their top-3 prioritised fixes with predicted deltas; the class challenges the predictions (they'll be tested against reality if the pair fast-forwards a re-fine-tune).
- **Expected outputs:** evaluation report, behavioural suite, and model cards in the repo — the capstone's evaluation chapter is this lab's output, extended.

---

# Module 7 — Inference Optimisation and Serving

## Module Overview

**Purpose.** Accuracy got the Bayan models built; economics decides whether they ship. This module teaches the levers that turn a research checkpoint into a servable component: sequence-length control and dynamic padding (the free wins), ONNX export and graph optimisation, post-training quantisation (INT8), knowledge distillation as a model-selection strategy, batching policies, and a disciplined benchmarking methodology (p50/p99 under concurrency, not single-shot means). Participants take the Day-2/3 models through the optimisation ladder, measure accuracy cost at every rung with M6's machinery, and wire the result into the serving skeleton they know from SDA-AIE-113.

**Business relevance.** Inference is where NLP budgets live or die: training the Bayan classifier cost eight GPU-minutes; serving it at national scale costs GPU-*years*. A 3× latency reduction is not an engineering vanity metric — it is two-thirds of the serving fleet returned to the budget, or the difference between a 200 ms citizen-facing experience and a 700 ms one that measurably drops completion rates. The optimisation ladder taught here (free wins → export → quantise → distil) is also the procurement counter-argument: teams that can serve a fine-tuned encoder at 15 ms/request on CPU stop renting GPUs for tasks that never needed them.

**Industry use cases.**
- A government platform serves 4M classification requests daily; moving from fp32 PyTorch to INT8 ONNX on CPU cuts the per-request cost ~70% with a measured 0.5-point F1 sacrifice.
- An e-commerce marketplace must survive Ramadan-peak traffic at fixed infrastructure — dynamic batching and length-bucketing triple throughput without touching the model.
- A bank's on-prem deployment cannot add GPUs for compliance-workload isolation reasons; distilled + quantised encoders make CPU serving viable within the latency SLA.

**Expected competencies.** Participants can benchmark inference honestly (p50/p99, warm-up, concurrency), rank and apply the optimisation levers in cost order, export to ONNX Runtime and apply dynamic INT8 quantisation with `optimum`, quantify every speed/accuracy trade with paired evaluation, choose between distillation and quantisation for a given budget, and serve the result behind the AIE-113 FastAPI skeleton with the course's canary checks.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Benchmark transformer inference honestly: p50/p99, warm-up, batching, concurrency | LO6, LO5 |
| 7.2 | Apply the free levers first: sequence-length control, dynamic padding, length-bucketed batching | LO6 |
| 7.3 | Export models to ONNX Runtime and apply post-training INT8 quantisation | LO6 |
| 7.4 | Quantify the accuracy cost of every optimisation with paired evaluation | LO6, LO5 |
| 7.5 | Select distillation vs quantisation vs hardware for a given latency/cost budget | LO6 |
| 7.6 | Serve optimised models behind a validated API with skew canaries | LO6, LO1 |

## Technical Content

### 1. The cost model: where transformer milliseconds go

Inference cost decomposes predictably, and the decomposition *is* the optimisation strategy: compute scales with layers × sequence-length-dependent terms — the attention matrices are O(n²·d) but for typical lengths the O(n·d²) linear layers dominate; memory traffic (weights + activations through the memory hierarchy) is why smaller numeric types speed up CPUs even when FLOPs don't change; and Python/framework overhead is a fixed tax per call that batching amortises. Consequences participants must own before touching any tool: **sequence length is the first lever** (Bayan's p95 is 87 tokens — padding everything to 512 buys nothing but heat; the M1 length audit becomes money here); **batching trades latency for throughput** (one request's p50 rises slightly, the fleet's requests-per-second triples); and **measure before optimising** — the benchmark harness comes first, because every later claim is a diff against it.

### 2. Honest benchmarking methodology

The single-shot `time.time()` around one forward pass produces numbers that are wrong in every direction that matters:

- **Warm-up:** first calls pay one-time costs (allocator pools, kernel selection, ORT graph capture) — discard the first 20–50 iterations.
- **Distribution, not mean:** report p50 and p99; NLP latency is length-dependent, so the *input mix* must mirror production (benchmark on the real length histogram from M1's audit, not on one synthetic sentence).
- **Concurrency:** a model that does 12 ms alone may do 80 ms at 16 concurrent requests (thread contention, cache pressure); benchmark at the target concurrency with a load generator, on the serving path (HTTP included), not just the bare `model()` call.
- **Environment honesty:** pin threads (`OMP_NUM_THREADS`, `torch.set_num_threads`), note the hardware, disable frequency-scaling surprises where possible; record all of it in `BENCHMARKS.md` — a benchmark without its environment is an anecdote.
- **Accuracy is part of the benchmark:** every optimisation row carries its macro-F1 (paired against the fp32 baseline with M6's bootstrap) — speed tables without accuracy columns are how silent quality regressions ship.

### 3. Free wins: length control, dynamic padding, length bucketing

Before any model surgery: **truncation to the measured need** (`max_length=128` covers Bayan's p99 with margin; vs 512 that's ~4× less attention compute and ~4× less padding waste); **dynamic padding** (pad to batch max, not model max — M3's `DataCollatorWithPadding` habit, now on the serving path); **length-bucketed batching** (group similar-length requests so batches aren't hostage to their longest member — a queue-time trade measured in Lab 7); and **tokenisation cost itself** (the fast Rust tokenizers are default, but pre-normalisation in Python can dominate at high QPS — profile the whole pipeline, not just the model). Together these typically deliver 2–4× throughput on short-text workloads *before* export or quantisation — which is why they are rung one of the ladder, and why skipping to the exotic rungs first is the module's named anti-pattern.

### 4. Export and quantisation: ONNX Runtime + INT8

- **ONNX export** freezes the model into a portable graph; **ONNX Runtime** then applies graph optimisations PyTorch's eager mode cannot: operator fusion (attention as one fused kernel), constant folding, layout optimisation. On CPU, export alone is typically worth 1.5–2× on BERT-class encoders. The `optimum` library wraps export for Hugging Face models (`ORTModelForSequenceClassification.from_pretrained(..., export=True)`) and keeps the tokenizer contract intact.
- **Post-training dynamic quantisation** stores weights as INT8 and quantises activations on the fly: ~4× smaller weights, 2–3× CPU speed-up, no calibration set needed — the right default for encoder serving. *Static* quantisation (calibrated activations) squeezes further but needs representative data and care; QAT (quantisation-aware training) is the escape hatch when post-training accuracy loss is unacceptable — rare for classification heads, likelier for token-level tasks.
- **The accuracy tax is measured, not assumed:** Bayan classifier fp32 → INT8 costs 0.4 macro-F1 points (paired CI includes the loss; it's real but small); the NER model costs 0.9 entity-F1 — token-level tasks are more quantisation-sensitive, a finding participants produce themselves in Lab 7.
- **Embedding models quantise well** for search (M5's MiniLM at INT8 loses ~0.5 recall@10 points) — but re-embedding the *corpus* with a changed model means an index rebuild (M5's versioning rule catches this; the manifest's model field now includes the quantisation state).

### 5. Distillation, hardware choice, and the decision framework

**Knowledge distillation** trains a small student to match a large teacher's output distribution; as *consumers*, participants choose pre-distilled checkpoints (DistilBERT ≈ 40% smaller/60% faster at ~97% of GLUE; MiniLM similarly for embeddings) — distilling their own models is beyond this module's scope but the economics are named: distillation costs a training project, quantisation costs an afternoon; do the afternoon first. **Hardware:** GPU wins at high sustained QPS with batching (throughput per riyal), CPU wins at modest QPS, spiky traffic, and on-prem constraints (no batch-assembly latency, simpler ops); the crossover is a calculation, not a religion — Lab 7's numbers feed it. The **decision ladder**, in the order a budget-constrained team should climb: (1) length + padding + batching (free), (2) ONNX export (hours), (3) dynamic INT8 (afternoon + accuracy check), (4) smaller/distilled checkpoint (re-fine-tune + full M6 re-evaluation), (5) hardware change (procurement). Each rung's exit criterion: does p99 now meet the budget with acceptable accuracy? Stop climbing when yes.

### 6. Common mistakes & production considerations

1. **Optimising before benchmarking** — no baseline, no claim; the harness precedes the surgery.
2. **Single-sentence benchmarks** — length-dependence means the input mix is part of the method; use the production length histogram.
3. **Speed tables without accuracy columns** — the silent-regression channel; every row pairs latency with paired-eval F1.
4. **Quantising the model but not re-running the skew canaries** — the ONNX path must produce the same tokenisation and normalisation; the M1 canary (pinned string → pinned ids → now pinned *logits within tolerance*) rides along.
5. **Padding to max_length on the serving path** — the training-time habit that quietly triples serving cost; dynamic padding everywhere.
6. **Comparing ORT-INT8 numbers on the laptop to fp32 numbers from the GPU pool** — environment-mismatched benchmarks; same box, same threads, same mix.

Production: version optimised artefacts as first-class releases (the ONNX file + tokenizer + manifest + model card noting the quantisation and its measured tax); keep the fp32 artefact as the accuracy reference and the rollback path; alert on the *no-answer/low-confidence rate* shifting after an optimisation rollout (quality drift shows there first); and hand the deployment pipeline itself to SDA-AIE-216 — this module ends at the validated, benchmarked, servable artefact.

## Code Examples

### The benchmark harness (built first, argued from later)

```python
# src/bayan/bench.py
"""Honest inference benchmarking: warm-up, real length mix, percentiles."""
import time

import numpy as np


def benchmark(predict_fn, texts: list[str], warmup: int = 30,
              iters: int = 300, seed: int = 42) -> dict:
    """predict_fn: text -> label. texts: sampled from the PRODUCTION length mix."""
    rng = np.random.default_rng(seed)
    sample = [texts[i] for i in rng.integers(0, len(texts), iters + warmup)]

    for t in sample[:warmup]:                       # pay one-time costs off-book
        predict_fn(t)

    lat = []
    for t in sample[warmup:]:
        t0 = time.perf_counter()
        predict_fn(t)
        lat.append((time.perf_counter() - t0) * 1000)

    return {"p50_ms": float(np.percentile(lat, 50)),
            "p99_ms": float(np.percentile(lat, 99)),
            "mean_ms": float(np.mean(lat)),
            "throughput_rps_1worker": 1000 / float(np.mean(lat))}
```

### Export + dynamic INT8 quantisation with optimum

```python
# src/bayan/optimize.py
"""The ladder, rungs 2-3: ONNX export, then dynamic INT8. Afternoon work."""
from optimum.onnxruntime import ORTModelForSequenceClassification, ORTQuantizer
from optimum.onnxruntime.configuration import AutoQuantizationConfig
from transformers import AutoTokenizer

SRC = "artifacts/topic-classifier-42"               # Lab 3's fp32 artefact


def export_and_quantize(out_dir: str = "artifacts/topic-onnx") -> None:
    # Rung 2: export — graph fusion and constant folding come free with ORT
    model = ORTModelForSequenceClassification.from_pretrained(SRC, export=True)
    tok = AutoTokenizer.from_pretrained(SRC)
    model.save_pretrained(out_dir)
    tok.save_pretrained(out_dir)

    # Rung 3: dynamic INT8 — weights quantised, activations on the fly
    quantizer = ORTQuantizer.from_pretrained(out_dir)
    qconfig = AutoQuantizationConfig.avx512_vnni(is_static=False, per_channel=False)
    quantizer.quantize(save_dir=f"{out_dir}-int8", quantization_config=qconfig)
    # NOTE: pick the qconfig for the SERVING CPU (avx2 fallback provided in
    # the lab repo) — quantisation kernels are ISA-specific; benchmark on
    # the target box, not the laptop.
```

### The ladder, measured end to end

```python
# notebooks/07_ladder.py
"""Every rung: latency AND paired accuracy. The table IS the deliverable."""
import numpy as np
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

from bayan.bench import benchmark
from bayan.eval_stats import paired_bootstrap_diff

texts = np.load("data/bench_mix.npy", allow_pickle=True).tolist()  # prod length mix

RUNGS = {
    "fp32 torch, max_length=512 pad": dict(path="artifacts/topic-classifier-42",
                                           ort=False, max_length=512, pad="max_length"),
    "fp32 torch, dynamic pad @128":   dict(path="artifacts/topic-classifier-42",
                                           ort=False, max_length=128, pad=True),
    "onnx fp32 @128":                 dict(path="artifacts/topic-onnx",
                                           ort=True, max_length=128, pad=True),
    "onnx int8 @128":                 dict(path="artifacts/topic-onnx-int8",
                                           ort=True, max_length=128, pad=True),
}

for name, cfg in RUNGS.items():
    cls = ORTModelForSequenceClassification if cfg["ort"] \
        else AutoModelForSequenceClassification
    pipe = pipeline("text-classification", model=cls.from_pretrained(cfg["path"]),
                    tokenizer=AutoTokenizer.from_pretrained(cfg["path"]),
                    device=-1)                       # CPU: the serving target
    stats = benchmark(lambda t: pipe(t, truncation=True,
                                     max_length=cfg["max_length"]), texts)
    print(f"{name:34s} p50={stats['p50_ms']:6.1f} ms  p99={stats['p99_ms']:6.1f} ms")

# Reference output (4-core CPU, OMP_NUM_THREADS=4):
#   fp32 torch, max_length=512 pad     p50=  96.3 ms  p99= 141.8 ms
#   fp32 torch, dynamic pad @128       p50=  41.7 ms  p99=  74.2 ms   ← free
#   onnx fp32 @128                     p50=  24.9 ms  p99=  43.1 ms
#   onnx int8 @128                     p50=  11.8 ms  p99=  21.4 ms   ← 8x total
# Accuracy (paired vs fp32 baseline): onnx fp32 ±0.000; int8 -0.004 macro-F1
# CI [-0.007, -0.001] → real but purchasable. NER int8: -0.009 entity-F1.
```

### The serving endpoint with skew canaries (AIE-113 skeleton, NLP organs)

```python
# src/bayan/api.py
"""FastAPI serving slice: validated input, optimised model, canaries at startup."""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from optimum.onnxruntime import ORTModelForSequenceClassification
from pydantic import BaseModel, Field
from transformers import AutoTokenizer, pipeline

from bayan.arabic import normalize_arabic
from bayan.preprocessing import PREPROC_VERSION

MODEL_DIR = "artifacts/topic-onnx-int8"
CANARY = "انقطعت الكهرباء في حي النرجس"          # pinned input …
CANARY_LABEL = "outage"                            # … pinned behaviour

state = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    tok = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = ORTModelForSequenceClassification.from_pretrained(MODEL_DIR)
    state["pipe"] = pipeline("text-classification", model=model,
                             tokenizer=tok, device=-1)
    # Skew canaries: tokenizer contract + end-to-end behaviour, at startup
    assert tok(CANARY).input_ids == [2, 14338, 9645, 1029, 3541, 22001, 3]
    assert state["pipe"](normalize_arabic(CANARY))[0]["label"] == CANARY_LABEL
    yield


app = FastAPI(lifespan=lifespan)


class FeedbackIn(BaseModel):
    text: str = Field(min_length=3, max_length=4000)


@app.post("/v1/classify")
def classify(body: FeedbackIn) -> dict:                    # CPU-bound: plain def
    result = state["pipe"](normalize_arabic(body.text),
                           truncation=True, max_length=128)[0]
    return {"topic": result["label"], "confidence": round(result["score"], 4),
            "model": f"{MODEL_DIR}@int8", "preproc": PREPROC_VERSION}
```

## Hands-on Lab 7 — Hit the Latency Budget

| | |
|---|---|
| **Objective** | Take the Bayan classifier down the optimisation ladder to **p99 ≤ 25 ms on the lab CPU at the production length mix**, with the accuracy tax of every rung measured and the winner wired into the serving endpoint with canaries green |
| **Duration** | 50 minutes |
| **Setup** | `pip install optimum[onnxruntime] fastapi uvicorn`; `git checkout lab7-start`; Lab 3/4 artefacts + `data/bench_mix.npy`; 4 CPU cores pinned (`OMP_NUM_THREADS=4`) |

**Instructions & tasks**

1. *(10 min)* Complete the benchmark harness; produce the **baseline row** (fp32, max_length=512, padded) and the free-wins row (dynamic pad @128) — record both before touching optimum; state the speed-up and its cost (zero — that's the point of rung 1).
2. *(10 min)* Export to ONNX; benchmark; run the paired accuracy check vs fp32 (expected: identical within tolerance).
3. *(10 min)* Quantise to INT8 (pick the qconfig matching the lab CPU); benchmark; paired accuracy check — record the tax with its CI in the ladder table.
4. *(10 min)* Repeat export+INT8 for the **NER model**; compare its quantisation tax to the classifier's; one-sentence explanation of the difference (token-level outputs are more sensitive than pooled classification).
5. *(5 min)* Wire the winning artefact into `api.py`; start the service; run the provided load script (`hey`, 16 concurrent, 60 s) against `/v1/classify`; confirm p99 under budget *through HTTP* and canaries green at startup.
6. *(5 min)* Commit `perf(serving): int8 onnx classifier, p99 21ms (-8x), -0.4 F1 measured`; fill the ladder table in `BENCHMARKS.md`.

**Expected output**
```
ladder (classifier, 4-core CPU):
  fp32@512 padded      p50  96 ms   p99 142 ms   F1 0.820  (baseline)
  fp32@128 dynamic     p50  42 ms   p99  74 ms   F1 0.820  (free, 2.3x)
  onnx fp32@128        p50  25 ms   p99  43 ms   F1 0.820  (3.9x)
  onnx int8@128        p50  12 ms   p99  21 ms   F1 0.816  (8.2x, tax CI-confirmed)
NER int8 tax: -0.009 entity-F1 → keep fp32-onnx for NER, int8 for topic (defended)
HTTP load test: 16 conc / 60 s → p99 34 ms, 0 errors, canaries asserted at boot
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| ONNX slower than PyTorch | Benchmarking cold, or thread oversubscription (ORT × OMP both spawning) | Warm-up 30 iters; set `OMP_NUM_THREADS` and ORT `intra_op_num_threads` coherently |
| INT8 accuracy collapses (>5 points) | avx512_vnni qconfig on a CPU without VNNI | Use the avx2 qconfig fallback; check `lscpu` flags — ISA-specific kernels |
| p99 fine in the notebook, 3× worse over HTTP | Per-request tokenisation + JSON overhead unmeasured before | That's why task 5 exists; profile the full path — the model was never the whole story |
| Load test shows rising latency over 60 s | Memory growth from unbounded pipeline batching | Pin batch size; check `hey` isn't saturating the same cores as the server |
| Canary logit assert fails after quantisation | Exact-match tolerance on quantised outputs | Canary asserts the *label* and ids exactly, logits within tolerance — read the assert |

**Instructor notes.** Insist on the baseline-first discipline — pairs who jump straight to INT8 have no denominator and must redo rung 0; that redo *is* the lesson. Task 4's split decision (int8 for topic, fp32-onnx for NER) is the module's judgement moment: different tasks buy different rungs, and the ladder table defends the choice in review. The HTTP-vs-notebook gap in task 5 reliably surprises the room — connect it forward: everything after the artefact (deployment, autoscaling, monitoring) is SDA-AIE-216's territory, and it inherits exactly this benchmark discipline. Fast finishers: length-bucketed batch endpoint (`/v1/classify:batch`), or quantise M5's embedder and measure recall@10 tax + the index-rebuild consequence.

## Mini Exercises

**Quiz (5 questions)**
1. Order the ladder and its unit costs. → length/padding/batching (free) → ONNX export (hours) → dynamic INT8 (afternoon + eval) → distilled checkpoint (training project) → hardware (procurement).
2. Why must the benchmark use the production length mix? → latency is length-dependent; a single-sentence benchmark measures a workload you don't serve.
3. Dynamic vs static quantisation — difference and default? → dynamic quantises weights only, activations on the fly, no calibration set — the encoder-serving default; static calibrates activations for more speed, more effort, more risk.
4. Your INT8 model shows -0.4 F1 with CI [-0.7, -0.1]. Ship? → a real but small tax; ship if the latency win funds it and the model card records it — the point is it's a *decision with numbers*, not a hope.
5. Why keep the fp32 artefact after INT8 ships? → accuracy reference for future paired evals + instant rollback path.

**Debugging exercise.** Branch `sim-serving-gap`: offline ladder says p99 21 ms, production dashboard says p99 180 ms. Participants profile the serving path and find three stacked causes: max_length=512 crept back in via a config default, padding="max_length" on the API path, and tokenisation running inside the request loop without the fast tokenizer. Fix order and re-measure — the ladder's free rungs, relearned where they were lost.

**Code-review exercise.** Review a perf PR: benchmark = mean of 10 unwarmed single-sentence calls on the author's laptop, no accuracy column, INT8 artefact replacing fp32 in-place (no version bump, fp32 deleted), canaries removed "because they failed after quantisation". Four findings, each with the fix.

**Discussion questions.**
- The classifier's INT8 CPU cost is now lower than the GPU amortised cost at your QPS. What has to be true about traffic growth before the GPU wins back — and who should own that recalculation?
- Rung 4 (distilled model) would need a full M6 re-evaluation. Why does rung 3 not need the *behavioural* suite re-run in full — or does it? Defend either answer. (it does — cheap insurance; quantisation can shift decision boundaries near thresholds)

## Case Study — Ramadan Peak at a Regional E-Commerce Marketplace

**Scenario.** A Gulf e-commerce marketplace runs transformer NLP on every product review and seller message: moderation classification, review sentiment, and semantic dedup of seller listings. Normal load is 90 requests/s; the two weeks before Eid multiply it by six. Last year the team "solved" the peak by renting eight additional GPU instances for a month — SAR 190,000 — and still breached the moderation-latency SLA on peak evenings because the fleet scaled on CPU metrics while the bottleneck was batch-assembly latency on the GPUs.

**Business context.** Moderation latency is trust-critical: reviews and seller replies publish only after moderation, and sellers watch the delay. Finance has rejected a repeat of the GPU rental; the SLA (p99 ≤ 300 ms end-to-end) stands. The NLP platform team gets one quarter to make peak survivable at near-baseline cost.

**Technical challenge.** Re-architect the inference tier under a fixed budget: model-level optimisation, batching policy, and per-task hardware placement — with measured accuracy taxes the moderation-policy team must co-sign.

**Constraints.** Moderation recall on the "prohibited" class may not drop more than 1 point (policy team's red line); the review-sentiment model tolerates 2 points; dedup embeddings feed a 40M-vector index that cannot be rebuilt during the peak freeze; the serving fleet is Kubernetes on CPU nodes with a small shared GPU pool.

**Solution approach (facilitate, don't lecture).** The audit finds the classic waste stack: all three models served fp32 PyTorch at max_length=512 on GPUs, padding to max, batch size tuned once in 2023. The redesign, ladder-ordered: length audit shows review p95 = 74 tokens → max_length=128 everywhere; dynamic padding + length-bucketed batching (the free 3×); moderation and sentiment classifiers exported to ONNX INT8 on CPU nodes — moderation's prohibited-class recall drops 0.3 points (paired CI, co-signed), sentiment drops 0.8; the embedder stays fp32-ONNX on the GPU pool *because* the index-rebuild freeze forbids changing its vectors (M5's versioning rule making a hardware decision). Peak simulation at 6× replayed traffic: p99 210 ms on the CPU fleet with autoscaling on queue depth instead of CPU%. Peak cost delta vs last year: the eight rented GPUs become two burst CPU node-pools — ~85% cheaper — and the SLA holds through Eid. The postmortem's first line: "we were renting GPUs to pay a padding bill."

**Discussion questions.**
1. Rank the redesign's wins by riyal saved and by engineering hours spent — which rung had the best ratio, and why is that the general pattern?
2. Why did the embedder's quantisation decision differ from the classifiers' — and what would make it change after the freeze?
3. The policy team's 1-point red line: translate it into the paired-bootstrap acceptance test that gates the INT8 rollout.
4. Autoscaling moved from CPU% to queue depth. Connect that to the batch-assembly failure last year — what was the old signal blind to?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Classifier p99 (CPU, prod mix) | Performance | ≤ 25 ms (bare), ≤ 40 ms (HTTP, 16 conc) | harness + `hey` |
| Total speed-up vs baseline | Performance | ≥ 6× | ladder table |
| INT8 accuracy tax (classifier) | Quality | measured with paired CI, ≤ 1 macro-F1 | paired bootstrap |
| NER quantisation decision | Judgement | documented with numbers in DECISIONS.md | artefact review |
| Startup canaries (ids + behaviour) | Reliability | green at service boot | lifespan asserts |
| Ladder table completeness | Discipline | 4 rungs × latency + accuracy columns | BENCHMARKS.md |

**Example benchmark table (filled during lab):**

| Rung | p50 | p99 | macro-F1 [paired Δ] | Artefact size |
|---|---|---|---|---|
| fp32 torch @512 padded | 96 ms | 142 ms | 0.820 [—] | 517 MB |
| fp32 torch @128 dynamic | 42 ms | 74 ms | 0.820 [±0.000] | 517 MB |
| ONNX fp32 @128 | 25 ms | 43 ms | 0.820 [±0.000] | 516 MB |
| ONNX INT8 @128 | 12 ms | 21 ms | 0.816 [−0.004, CI −0.007..−0.001] | 130 MB |

## Required Visuals and Training Assets

### Diagrams
1. **The optimisation ladder** — *Purpose:* module anchor and take-home poster. *Elements:* five rungs (free wins → export → INT8 → distil → hardware) with unit-cost tags (free/hours/afternoon/project/procurement), exit criterion banner ("p99 meets budget? stop climbing"), and the Bayan numbers on each rung. *Style:* literal ladder, printable A4.
2. **Where the milliseconds go** — *Elements:* stacked bar of one request's time: tokenise → pad waste → linear layers → attention → overhead; before/after bars for each rung showing which segment each optimisation eats. *Style:* stacked-bar waterfall pair.
3. **Latency vs throughput vs batching** — *Elements:* curves of p50 and requests/s against batch size; the queue-time shadow at low traffic; length-bucketing shown as tighter batches. *Style:* dual-axis curve chart with annotated sweet spot.
4. **The serving slice** — *Elements:* request → validation wall → normalise (versioned) → fast tokenizer → ORT INT8 session → response; canary checks drawn as gates at boot; the fp32 artefact parked beside as rollback. *Style:* horizontal pipeline echoing M1's text-to-tensor diagram — the course's first and last diagrams rhyme.

### Images (screenshots)
1. **Ladder console output** — *why:* expected-state reference; *content:* the four-rung table exactly as the notebook prints it.
2. **`hey` load-test summary** — *why:* HTTP-path realism; *content:* 16-concurrency run with the latency histogram and 0 errors.
3. **Netron view of the ONNX graph** — *why:* make "graph optimisation" concrete; *content:* fused attention node vs the eager-mode operator soup.
4. **Startup log with canaries** — *why:* the discipline artefact; *content:* service boot printing tokenizer + behaviour canary asserts green, model version line.

### Simulations
1. **The serving gap** — *Setup:* branch `sim-serving-gap` (config drift re-introduced 512/pad-max/slow-tokenizer on the API path). *Expected:* 21 ms offline vs 180 ms served; profiled and fixed in ladder order. *Learning objective:* optimisations live in configs and die in config drift.
2. **The ISA mismatch** — *Setup:* VNNI qconfig artefact run on an avx2-only container. *Expected:* accuracy collapse or fallback slowness; caught by the boot canary. *Learning objective:* quantised artefacts are hardware-coupled; canaries are the seatbelt.

### Interactive Activities
- **Budget game (10 min):** teams get a latency budget, a QPS, and price cards (CPU node, GPU node, engineer-day); build the cheapest compliant serving plan for the three Bayan models; plans defended against the instructor's traffic-spike card.
- **Predict the rung (5 min):** before running the ladder, every pair writes down predicted p50 for each rung; closest pair explains their reasoning — calibrated intuition is the goal.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `bench_mix.npy` | Sampled from Bayan corpus preserving the production length histogram | NumPy | 2,000 texts | Benchmark input mix |
| Load-test script + config | Course repo (`hey` wrapper) | Shell/YAML | — | HTTP-path benchmarking |
| fp32 artefacts | Labs 3–4 outputs | HF format | 3 models | Ladder inputs |

### Demo Requirements
- **Instructor demo:** run the ladder live with predictions collected first (the "predict the rung" activity), then the `sim-serving-gap` reveal — offline heroics erased by one config default.
- **Student demo:** one pair defends the split decision (INT8 topic, fp32-ONNX NER) as if to a change-review board; one pair shows their HTTP p99 meeting budget.
- **Expected outputs:** optimised, canaried, benchmarked serving artefacts — the capstone's runtime, ready for assembly in the next hour.

---

# Final Capstone Project

## Title: Bayan — Bilingual Citizen-Feedback Intelligence Service

## Project Scenario

You are the NLP engineer for **"Bayan" (بيان)**, the citizen-feedback intelligence capability of a Saudi digital-government platform. The platform receives thousands of Arabic and English feedback messages daily — dialect chat, formal MSA complaints, English web-form entries. Your mandate: deliver the working, evaluated, optimised NLP service the case-management team will build on — topic classification and sentiment, entity extraction into case fields, similar-case retrieval, and an evaluation report leadership can trust. Everything built in Labs 1–7 is a component; the capstone is the integration plus your own extension — and the demo is delivered in the roles you will actually play at work: the engineer defending the numbers.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Preprocessing & Arabic handling (LO1):** one versioned preprocessing module (bilingual layer + per-model Arabic profiles) imported by training, evaluation, and serving; PII masking with 100% recall on the test set; segmentation scheme consistent train-to-serve; skew canaries asserted at service startup.
2. **Fine-tuned models (LO3):** topic classifier beating the TF-IDF baseline by ≥ 8 macro-F1; dialect-aware variant beating the multilingual incumbent on the Gulf slice with a CI-backed claim; NER at entity-F1 ≥ 0.80 with the clitic alignment tests green; extractive QA with honest null handling (≥ 17/20 on the no-answer slice).
3. **Semantic search (LO4):** versioned FAISS index with manifest; two-stage retrieve-and-re-rank; recall@10 ≥ 0.80 and MRR@10 ≥ 0.70 on the labelled query set; cross-lingual gap measured and reported.
4. **Evaluation report (LO5):** sliced metrics (language, dialect, class, length) with bootstrap CIs; behavioural suite ≥ 95% invariance / ≥ 90% MFT pass; error taxonomy from ≥ 100 hand-read errors with top-3 prioritised fixes; one model card per artefact with hand-written limitations.
5. **Optimised serving (LO6):** the classifier served at p99 ≤ 40 ms over HTTP (16 concurrent, lab CPU); complete ladder table with paired accuracy taxes; documented quantisation decision per model; fp32 rollback artefacts retained.
6. **Transformer literacy (LO2):** `DECISIONS.md` includes the architecture-grounded rationale for every model-family and checkpoint choice (encoder vs decoder, multilingual vs Arabic-centric, with fertility and slice evidence).
7. **Engineering hygiene:** re-runnable training scripts (no notebook-state artefacts); frozen test set untouched until the final report; `BENCHMARKS.md` filled from *your* runs; meaningful commit history across all four days.

**One extension (choose at least one):**
- **Dialect router:** dialect-ID front end routing Gulf traffic to the DA model and the rest to mix, with sliced evidence that routing beats either model alone
- **Two-headed encoder:** shared-trunk topic+sentiment model with the serving-cost comparison and paired accuracy verdict vs two single models
- **Search-quality upgrade:** embedding-similarity dedup at index build + title/field-boosted chunking, with before/after retrieval metrics
- **Batch endpoint:** `/v1/classify:batch` with length-bucketed batching and a measured throughput curve vs batch size
- **QA over service documents:** wire the extractive QA model into the API with windowing over long documents and the null-threshold trade-off curve

## Architecture (target state)

```
                        ┌────────────────────────── Bayan service ──────────────────────────┐
citizen text ──HTTP──►  validation wall → preprocess (versioned, per-model AR profiles)     │
                        │        │                                                          │
                        │        ├─► topic+sentiment (ONNX INT8, canaried)  ─► case fields  │
                        │        ├─► NER (ONNX fp32, d3tok-segmented)       ─► case fields  │
                        │        └─► embed → FAISS (manifest-pinned) → CE re-rank           │
                        │                                   └─► similar resolved cases      │
                        └───────────────────────────────────────────────────────────────────┘
offline:  corpus ─► training scripts ─► artifacts/ (models + cards + BENCHMARKS + ladder)
          eval sets (frozen) ─► sliced report + behavioural suite ─► EVALUATION_REPORT.md
```

## Deliverables

1. Repository (instructor-shared) with full four-day commit history and re-runnable scripts
2. Running service: one `make serve` from a clean clone, startup canaries green, all endpoints live
3. `EVALUATION_REPORT.md`: sliced metrics with CIs, behavioural rates, error taxonomy, top-3 fixes — plus a model card per artefact
4. `BENCHMARKS.md`: every course benchmark table filled from the participant's own runs, including the full optimisation ladder
5. `DECISIONS.md`: the decision records accumulated across labs (tokenizer, Arabic model, min_score, quantisation split) — each with its evidence
6. 5-minute demo: live bilingual request → classified, extracted, similar-cases response; one behavioural test explained; one number defended under challenge

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: preprocessing + tokenizer decision (Lab 1) | End Day 1 | golden tests green, DECISIONS.md#tokenizer |
| M-B: three fine-tuned models (Labs 3a/3b) | End Day 2 | baseline beaten, alignment tests green |
| M-C: Arabic-aware models + search + evaluation report (Labs 4–6) | End Day 3 | slice tables with CIs, MRR ≥ 0.70 |
| M-D: optimised serving assembled (Lab 7 + capstone hours) | Day 4 H4 | HTTP p99 in budget, canaries green, extension working |
| M-E: demo + assessment | Day 4 H5 | rubric scoring live |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Preprocessing & Arabic handling | 15 | One versioned module everywhere; profiles per model; canaries at boot; PII 100% | Minor gaps (one duplicated normaliser, canary missing on one path) | Divergent train/serve preprocessing; PII misses |
| Fine-tuned models | 20 | All targets met; CI-backed slice claim; honest nulls; clitic tests green | Targets mostly met; one weak model or missing CI on the slice claim | Baseline unbeaten, leaky splits, or subword-level NER scores |
| Semantic search | 15 | Two-stage, manifest-pinned, targets met, cross-lingual gap reported | Targets met but versioning thin or no-answer handling crude | Unnormalised vectors, no labelled evaluation, stale index |
| Evaluation & error analysis | 20 | Slices+CIs, behavioural suite, real hand-read taxonomy with costed fixes, cards complete | Report present but slices thin or taxonomy shallow | Aggregate-only claims, test-set tuning, no cards |
| Optimised serving | 15 | Ladder complete with paired taxes; p99 in budget over HTTP; defensible quantisation split | Budget met but ladder partial or taxes unmeasured | No baseline, laptop-only numbers, canaries removed |
| Decisions & demo | 15 | DECISIONS.md evidence-dense; demo crisp; numbers defended under challenge | Demo works; some decisions asserted rather than evidenced | Cannot run own service cold or explain own numbers |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope scores ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the repository evidence first* (BENCHMARKS.md numbers spot-checked against artefacts, frozen-test discipline visible in history), demo second — the course's thesis is that claims carry their evidence.
- Spot-verify one claim per participant live: re-run their sliced report on one model, or fire the canary string at their running service.
- Anti-pattern flags that cap a criterion at 70%: test-set rows touched before the final report (check git history on the eval-set path); slice claims without CIs; benchmark tables copied from the course reference numbers rather than measured (the reference numbers are seeded differently per cohort — copies are detectable); behavioural suite weakened to pass.
- The challenge question in the demo is mandatory: pick one number from their report and ask "why should I believe this?" — the answer quality *is* LO5.

## Bonus Tasks (for early finishers / distinction seekers)

1. **Zero-shot showdown:** compare the fine-tuned classifier against a zero-shot NLI-based classifier on the same frozen test set — cost, latency, and slice behaviour; write the one-page "when would the LLM-era approach win?" memo (the AIE-213 bridge, evidenced).
2. **Arabizi lane:** detect Arabizi at ingestion, transliterate, and measure the slice's classification lift.
3. **Drift tripwire:** weekly-slice simulation over the corpus's timestamp field — show which slice metric moves first under the provided drift injection, and propose the alert threshold (the AIE-216 bridge).
4. **Index at scale:** rebuild the case index with IVF and HNSW at 10× corpus (provided synthetic expansion); recall-vs-latency curves against flat; the "when do we leave flat?" decision memo.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** Why must tokenizer and model weights come from the same checkpoint? → ids only mean what that checkpoint's vocab/merges trained them to mean; mismatch is silent corruption.
**Q2.** Fertility 3.5 on your corpus — name two operational consequences. → shorter effective context (truncation risk) and higher compute per request (also weaker representations).
**Q3.** Why divide attention scores by √d_k? → keeps score variance ~1 so softmax stays out of saturation and gradients flow.
**Q4.** Self-attention's complexity in sequence length and the cheapest mitigation? → O(n²); control sequence length (truncate to measured need, chunk documents).
**Q5.** Fixed 12-label routing task: encoder or decoder LLM, and why? → encoder — better calibrated, 10–100× cheaper to serve, easier to evaluate; LLM wins only zero-shot/long-tail.
**Q6.** What does `-100` do in NER fine-tuning? → excludes continuation subwords and special tokens from loss and evaluation — the alignment discipline.
**Q7.** Why group train/test splits by citizen_id? → near-duplicate texts from one author straddling splits inflate offline metrics that die on live traffic.
**Q8.** Why must extractive QA compare the best span against the null score? → otherwise it always extracts something — hallucination by construction on unanswerable questions.
**Q9.** Name two Arabic orthographic normalisations and the rule governing their use. → alef-variant folding, dediacritisation (also ya/ta marbuta); match the checkpoint's pretraining recipe, never touch the display copy.
**Q10.** Why did the MSA-trained sentiment model miss the crisis messages (M4 case)? → crisis text is dialectal; MSA models degrade silently on dialect — only sliced evaluation shows it.
**Q11.** What does clitic segmentation (d3tok) fix for NER? → entities buried inside whitespace tokens (وبالرياض) become their own tokens the tagger can label.
**Q12.** Why is raw pretrained `[CLS]` a poor sentence embedding, and what fixes it? → never trained for similarity; contrastive (SBERT-style) fine-tuning shapes the space so cosine means similarity.
**Q13.** What breaks if only the index side is L2-normalised? → inner product mixes magnitude in; rankings skew to long/dense texts — plausible and wrong.
**Q14.** Retrieve-then-re-rank: why both stages? → bi-encoder pre-computes and scales (recall); cross-encoder sees token interactions (precision) but costs a forward pass per pair.
**Q15.** When does an ANN index beat `IndexFlatIP`, and what must you measure first? → beyond ~10⁵ vectors; recall@k of the ANN against flat on your own queries.
**Q16.** A "+0.8 F1" improvement — what two checks before you believe it? → paired bootstrap CI excluding zero; seed spread smaller than the claimed gain.
**Q17.** Invariance vs directional behavioural test — one example each. → location swap must not change topic; negating the resolution must not improve sentiment.
**Q18.** Why does error analysis run on validation, never the frozen test set? → analysis drives tuning; touching test for it is leakage and the number stops predicting production.
**Q19.** Order the inference-optimisation ladder by unit cost. → length/padding/batching (free) → ONNX export → dynamic INT8 → distilled checkpoint → hardware.
**Q20.** Why keep the fp32 artefact after INT8 ships? → paired-eval accuracy reference and instant rollback path.

## Practical Assessments

**PA-1 (30 min, Day 3 H5 tail or self-paced):** Given a broken repo slice — serving path skips Arabic normalisation, NER evaluated at subword level, unnormalised query vectors — produce green canaries and corrected metrics with a short diagnosis note per bug. Scored: diagnosis (40%), fixes (40%), verification evidence (20%).

**PA-2 (30 min, Day 4 H2 tail):** Given a rival team's evaluation report (aggregate-only, no CIs, test-set tuning visible in the appendix, one behavioural regression buried), write the review: what may ship, what must change, what needs measurement. Scored against the model review: triage correctness (50%), review actionability (30%), statistical reasoning (20%).

**PA-3:** Capstone (rubric above) — the Arabic/English NLP application project, 40% of course grade. Labs + PA-1/PA-2 + quiz form the labs component — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (Labs 1–7) | 35% | checkpoint commits + expected outputs per lab |
| PA-1 + PA-2 | 15% | artefacts + diagnosis/review notes |
| Quiz | 10% | 10-question selection, closed book |
| Capstone project (Arabic/English NLP application) | 40% | rubric, repository-first |

Badge issuance (NLP specialisation badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (benchmark tables are cohort-seeded; identical numbers across repos are checked). The module counts toward the AI Engineer Specialist Certificate (AIE-216 + any 3 of AIE-211/212/213/214/215) and feeds the GenAI Engineering specialisation.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone course org repos; push checkpoint tags (`lab1-start` … `lab7-start`) and all `sim-*` branches (`sim-skew-preproc`, `sim-pad-leak`, `sim-align-bug`, `sim-seg-skew`, `sim-unnormalized`, `sim-stale-index`, `sim-eval-leak`, `sim-serving-gap`)
- [ ] Regenerate the cohort-seeded Bayan corpus, benchmark reference numbers, and fallback checkpoints; verify all lab expected-outputs against the pinned library versions
- [ ] Dry-run all 7 labs end-to-end on a clean GPU-pool machine **and** the CPU fallback path (small models, reduced epochs); Lab 3 timing assumes T4-class GPU per pair
- [ ] Pre-install CAMeL Tools data (`camel_data -i defaults`) on all lab machines and bake it into the fallback container image
- [ ] Pre-download all checkpoints (CAMeLBERT mix/DA, mBERT, XLM-R, MARBERT, MiniLM bi-encoder, mmarco cross-encoder, DistilBERT) to the shared cache — first-run downloads over classroom Wi-Fi kill Lab 3
- [ ] Print A4 posters: text-to-tensor pipeline, three-families card, aggregate-hides-the-slice, the optimisation ladder
- [ ] Prepare the shared leaderboard (fertility numbers, macro-F1, MRR, ladder p99) and the Lab 3 prediction-market board
- [ ] Confirm classroom network allows huggingface.co, pypi, github.com (or mirror configured); in restricted environments pre-pull everything to the local registry
- [ ] Verify a native-Arabic-reading instructor or assistant is scheduled for Days 2–3 (dialect examples land differently read aloud)

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + git + a GitHub account with SSH or PAT auth
- [ ] `pip install transformers datasets sentence-transformers spacy camel-tools scikit-learn seqeval faiss-cpu "optimum[onnxruntime]" fastapi uvicorn pytest pandas matplotlib`
- [ ] `hey` binary (provided in course bundle for offline install)
- [ ] GPU-pool credentials tested (or Colab account as fallback) — Lab 3 email includes the connection check
- [ ] Clone course repo; run `make doctor` (validates versions, CAMeL data, checkpoint cache, Arabic text rendering in the terminal — prints ✓/✗)
- [ ] Editor/terminal font that renders Arabic script correctly (the doctor script tests this; it matters more than participants expect)

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| Checkpoint downloads stall on classroom Wi-Fi | High | Shared HF cache pre-populated; `HF_HOME` set by `make doctor` |
| CUDA OOM in Lab 3 (batch 32, fp32) | High | `fp16=True` first, then batch 16 + gradient accumulation; CPU fallback = DistilBERT-class models, 1 epoch |
| Arabic renders reversed/disjointed in terminals | High | The doctor-script font check; VS Code integrated terminal handles RTL best; never debug Arabic by eyeballing a broken terminal |
| CAMeL data package missing (`DialectIdentifier` fails) | Medium | `camel_data -i defaults`; check `$CAMELTOOLS_DATA`; pre-installed image as fallback |
| Windows path/encoding errors on Arabic CSVs | Medium | `encoding="utf-8"` everywhere (repo helpers do this); WSL2 recommended in the pre-course email |
| Participants evaluate NER at subword level and celebrate | Medium | It's a planned teachable moment (Lab 3B); the seqeval discipline, publicly named |
| faiss-cpu install conflicts on Apple Silicon | Medium | conda-forge build documented in repo README; flat-index NumPy fallback provided |
| ONNX INT8 accuracy collapse on non-VNNI CPUs | Low | avx2 qconfig fallback in lab repo; `lscpu` check in Lab 7 task 3 |
| Strong-Arabic participants bored in M1, lost in M3 (or inverse for strong-Python) | Medium | The pairing strategy is the fix — rotate deliberately, name the skill-transfer goal aloud |

## Timing Recommendations

- Protect Lab 3 (both parts) and Lab 6's hand-reading segment at full length; compress M5's index-type taxonomy (the ladder diagram carries it) if behind.
- Day 2 H5 (M4 lecture) can shed the resources tour to 5 minutes if Lab 3B overran — the Lab 4 tasks re-teach it by doing.
- If a cohort is strong: pull the dialect-router extension into main capstone scope and run the zero-shot showdown as a plenary on Day 4.
- If a cohort is weak: make Lab 5's cross-encoder stage a guided demo and drop task 6; never drop the retrieval *evaluation* — un-evaluated search is the anti-lesson.
- Hard rule: capstone assembly (Day 4 H3) starts on time even if Lab 7 is unfinished — the fallback optimised artefacts exist precisely for this.

## Discussion Prompts (use during transitions)

1. "What is the most expensive NLP failure you've seen that a fertility check or a slice table would have caught for five lines of code?"
2. "Your model scores 0.82. Your dialect-speaking citizens experience 0.76. Which number goes in the press release — and who decided?"
3. "A vendor demo dazzles on ten hand-picked queries. Using this course, write the three-line email that turns the demo into an evaluation."
4. "When the LLM era reached your organisation, which of this course's disciplines became *more* important, not less?" (evaluation, retrieval quality, preprocessing skew — all of them feed AIE-213/214)
5. "Which Bayan component would you bet breaks first in production — and which of your tests would know before your users do?"

## Wrap-up (Day 4, final 15 minutes)

- Map each capstone requirement to the module that taught it (one slide) — the golden thread made explicit one last time.
- Forward pointers: SDA-AIE-213 builds LLM applications on exactly this substrate (tokenisation, embeddings, evaluation discipline); the M5 retrieval component is AIE-214's RAG foundation; serving and monitoring mature in AIE-216. The NLP specialisation badge counts toward the AI Engineer Specialist Certificate and feeds the GenAI Engineering specialisation.
- Collect: repo URLs, `EVALUATION_REPORT.md`, `BENCHMARKS.md`, `DECISIONS.md`; issue badge recommendations within 5 working days.
- Last word: the course's one-sentence thesis, returned to the room — *in NLP engineering, the model is the easy part; the tokenizer, the slices, and the milliseconds are where the profession lives.*

---

*End of instructor package. All code samples target Python 3.12, transformers ≥ 4.40, sentence-transformers ≥ 3.0, camel-tools ≥ 1.5, optimum ≥ 1.19, faiss-cpu ≥ 1.8. Verify pinned versions in the course lock file before each delivery.*

