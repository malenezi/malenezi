# Intelligent Support Ticket Assistant (English + Arabic)

Capstone project for the **Applied NLP Engineering** bootcamp, AI Engineering Track, SDAIA Academy.

- SDAIA Academy on GitHub: https://github.com/SDAIAAcademy
- Course page: https://sdaiaacademy.github.io/applied-nlp/

**Author:** Razan Saad Alshahrani (individual project)

> **ملخص بالعربي:** نظام يستقبل رسالة عميل (عربي أو إنجليزي) ويحدد نيّتها وفئتها وأولويتها، ويبحث عن حالات مشابهة سابقة، ثم يكتب ردًّا مقترحًا مبنيًّا على حلول تلك الحالات. يغطي المشروع التمثيل (Embeddings)، التوليد المقيَّد بالمصادر (RAG)، المقارنة بين النماذج، وتحليل الأخطاء.

## What it does

Given a customer message in English or Arabic, the system:

1. detects the **language**,
2. predicts **intent**, **category** (billing, technical, account, shipping, refund) and **priority** (high, medium, low),
3. retrieves the **most similar historical tickets** (semantic search),
4. drafts a **reply grounded in those cases' resolutions** and lists which cases it relied on.

```
ticket ──► language detect ──► multilingual embedding ──┬─► Logistic Regression ─► intent / category / priority
                                                        └─► FAISS search ─► similar cases ─► grounded reply
                                                                                   (template, or LLM + Pydantic validation)
```

## Repository layout

```
app.py                 Gradio demo
run_all.sh             data -> evaluation -> example outputs
src/make_data.py       synthetic bilingual dataset (380 tickets, ~12% deliberately hard)
src/data.py            loading, stratified split (no leakage), language detection
src/embedder.py        embeddings (Sentence-Transformers) + FAISS index (NumPy fallback)
src/models.py          three decision models compared in the evaluation
src/rag.py, llm.py     grounded reply drafting (template by default, optional LLM)
src/schemas.py         Pydantic schemas for outputs and LLM JSON validation
src/pipeline.py        TicketAssistant: the end-to-end system
src/finetune.py        full fine-tuning / LoRA of the encoder (GPU)
src/evaluate.py        model comparison, retrieval metrics, challenge set, error analysis
src/run_examples.py    runs sample inputs and saves examples/sample_outputs.json
data/                  tickets.csv (generated) and challenge.csv (20 hand-written tickets)
examples/              sample_inputs.json (+ sample_outputs.json after running)
results/               results.md, metrics.json, errors.csv, challenge_errors.csv, finetune_*.md (generated)
models/                fine-tuned weights created by src/finetune.py (git-ignored, large)
tests/                 smoke tests
```

## Setup and run

### Google Colab (recommended)

Use **Runtime > Change runtime type > GPU** (needed only for fine-tuning; everything else runs on CPU).
Then:

```python
!git clone https://github.com/rhatrash/support-ticket-assistant.git
%cd support-ticket-assistant
!pip install -q -r requirements.txt
!bash run_all.sh                                   # data -> evaluation -> example outputs

# adaptation experiments (GPU recommended)
!python -m src.finetune --target category          # full fine-tuning
!python -m src.finetune --target priority
!pip uninstall -y -q torchao                       # only needed if LoRA fails with a torchao version error
!python -m src.finetune --target category --lora
!python -m src.finetune --target priority --lora

!python app.py                                     # Gradio demo (change to demo.launch(share=True) for a public link)
```

### Local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
bash run_all.sh
python app.py
pytest -q                 # smoke tests (offline, no model download)
```

Offline / quick mode (no model download): `EMBED_BACKEND=tfidf bash run_all.sh`.
Optional LLM for the draft reply (any OpenAI-compatible endpoint): set `LLM_BASE_URL`, `LLM_MODEL`, `LLM_API_KEY`. Without them, a grounded template reply is used.

## Demo

`python app.py` opens a Gradio page: paste a customer message (English or Arabic) and it shows the category, priority, intent, the three most similar historical tickets and the grounded draft reply. `python -m src.run_examples` runs the same pipeline on `examples/sample_inputs.json` and saves the full outputs (including the drafted replies) to `examples/sample_outputs.json`. Sample run:

| Ticket | Lang | Category | Priority | Intent |
|---|---|---|---|---|
| I was charged twice for my Najm Plus subscription. This is urgent. | en | billing | high | double_charge |
| طلبي رقم 48213 ما وصل وتأخر 9 أيام. أحتاج مساعدة الآن لو سمحتم! | ar | shipping | high | late_delivery |
| تطبيق Tayseer يقفل لحاله كل ما أفتحه، مو مستعجل. | ar | technical | high (wrong: should be low, see error analysis) | app_crash |
| How can I change the email address on my account? No rush, just asking. | en | account | low | change_email |
| My account was hacked and someone placed an order using my card. | en | account | medium | mixed |
| الـ app يعلق لما أحاول أدفع payment. | ar | technical | low | mixed |

## Design decisions (model selection)

| Component | Choice | Why |
|---|---|---|
| Embeddings | `paraphrase-multilingual-MiniLM-L12-v2` | small, fast on CPU, supports Arabic and English in one space |
| Search | FAISS `IndexFlatIP` on normalized vectors | exact cosine search; dataset is tiny |
| Decision model | Logistic Regression on embeddings | cheap, fast, gives calibrated-ish confidence scores |
| Baselines | char n-gram TF-IDF + LR, and kNN vote | show whether embeddings and a learned head actually help |
| Reply generation | retrieval-grounded template (default) or LLM with JSON schema + case-id check | answers use only retrieved resolutions; ungrounded LLM output is rejected |

**Adaptation: fine-tuning and LoRA.** `src/finetune.py` fine-tunes the multilingual encoder for classification with the Hugging Face `Trainer` (validation split carved from train only, early stopping on validation macro-F1, same held-out test set as the baselines). Two modes:

```bash
python -m src.evaluate                                # baselines first (needed for the comparison table)
python -m src.finetune --target category              # full fine-tuning
python -m src.finetune --target category --lora       # LoRA via PEFT (r=16 on attention + dense layers, lr 1e-3, up to 30 epochs)
python -m src.finetune --target priority
```

Results go to `results/finetune_*.md` and are compared with the frozen-embeddings + Logistic Regression baseline on both the test set and the challenge set. A GPU (Colab T4) is recommended. I chose an encoder rather than an LLM for LoRA because the task is classification, the data is small, and an encoder is far cheaper and faster to serve.

## Evaluation

`python -m src.evaluate` writes everything to `results/`:

- model comparison on a stratified held-out test set (macro-F1, accuracy, latency per ticket),
- retrieval quality (Hit@1/3/5, MRR@5),
- a **challenge set** of 20 hand-written tickets whose wording does not appear in the templates,
- error analysis: `errors.csv`, per-language and per-difficulty accuracy, top confusions, per-class report.

### Results

All numbers are macro-F1 from a Colab GPU run (seed 42). Split: 304 train / 76 test tickets. The **challenge set** is 20 hand-written tickets (10 English, 10 Arabic) whose wording does not come from the generation templates, so it is the more honest measure of generalization.

| System | Category (test) | Category (challenge) | Priority (test) | Priority (challenge) |
|---|---|---|---|---|
| TF-IDF (char n-gram) + LR | 1.000 | 0.436 | 1.000 | 0.731 |
| Embeddings + LR (**used in the pipeline**) | 1.000 | 0.641 | 0.841 | 0.500 |
| kNN retrieval vote (k=5) | 0.894 | 0.520 | 0.391 | 0.070 |
| Full fine-tuning (encoder) | 0.956 | 0.627 | 1.000 | **0.857** |
| LoRA (r=16, lr 1e-3, final) | 0.916 | 0.632 | 1.000 | 0.537 |
| LoRA, first attempt (r=8, lr 3e-4) | 0.643 | 0.386 | 0.222 | 0.237 |

Intent (test macro-F1): TF-IDF 1.000, Embeddings + LR 0.985, kNN 0.880. Similar-case retrieval (relevant = same category): Hit@1 0.961, Hit@3 0.974, Hit@5 0.987, MRR@5 0.970.

**Main findings**

1. **The test set is saturated, the challenge set is not.** Category F1 drops from 1.00 to about 0.64 for the best systems when the wording changes. The test scores mostly reflect template memorization, so model choices are judged on the challenge set (20 tickets, so one ticket is worth 5 points; small differences are noise).
2. **Category:** the embedding-based systems (0.63-0.64) beat TF-IDF (0.44), which depends on exact vocabulary. Fine-tuning did not improve on frozen embeddings, which suggests the limit is data size and variety rather than model capacity.
3. **Priority:** full fine-tuning is clearly best on the challenge set (0.857), then TF-IDF (0.731). Frozen embeddings (0.500) capture topic more than urgency cues, while TF-IDF sees the cue words directly. Fine-tuning lets the encoder learn those cues. (This explanation is a hypothesis consistent with the results; it was not tested separately.)
4. **LoRA:** the first attempt underfitted (training loss still falling, and early stopping with patience 2 ended the priority run while it still predicted a single class). Raising the learning rate (3e-4 to 1e-3), rank (8 to 16), adapted modules (query/value to all attention and dense layers), epochs and patience fixed training, but LoRA still trailed full fine-tuning on challenge priority (0.537 vs 0.857) while training only 1.1% of the parameters. With this little data, full fine-tuning was the better adaptation.
5. **kNN voting** is useful for retrieving similar cases but is a poor classifier (priority F1 0.07 on the challenge set).

### Error analysis (final model: Embeddings + LR)

*On the test set:* category is perfect (no confusions); the 10 / 76 tickets with at least one wrong label are all priority or intent errors (see `results/errors.csv`). Accuracy on "hard" tickets equals regular tickets (both 1.0) most likely because the same hard sentences also appear in the training split with different urgency phrases.

*On the challenge set:* 14 of 20 tickets had at least one wrong prediction (`results/challenge_errors.csv`): 7 category errors and 10 priority errors.

- **Arabic is much weaker than English for category.** English accuracy 9/10, Arabic 4/10. The wrong Arabic tickets use short, informal or dialectal phrasing that the templates never contained, for example a message saying a different item than ordered arrived was labeled `account` (confidence 0.54), "I forgot the password and the reset message did not arrive" was labeled `refund` (0.82), and "can I edit my registered mobile number" was labeled `shipping` (0.59). Likely causes (not tested): the small multilingual encoder is weaker on dialect, and the training data has only four phrasings per category and language.
- **Mixed or implicit intent.** "The box was crushed and the screen inside is broken" (true: shipping) was predicted `technical` (0.49): "screen" and "broken" pull toward a technical issue, although the customer is reporting damage in delivery.
- **Priority bias on tickets without explicit cues.** 7 of the 10 `medium` tickets were wrong (5 predicted `low`, 2 predicted `high`). The model effectively learned "urgency words mean high, polite words mean low, everything else is guesswork".
- **Explicit urgency was missed.** "The parcel is two weeks late and nobody answers me, urgent please!" (Arabic) was predicted `low` (0.75) and also got the wrong category (`refund`, 0.40), even though it contains an urgency word.
- **Negation is handled inconsistently.** "Please erase my profile ... no rush" (true: low) was predicted `high`, and in the demo examples an Arabic ticket saying "not urgent" was labeled `high`, while two other "not urgent" Arabic tickets were correct. The model reacts to the urgency word but not reliably to its negation.
- **Confidence is informative.** Among the challenge tickets in `challenge_errors.csv`, 6 of the 7 wrong category predictions had confidence of 0.59 or lower, whereas every correct category prediction there had confidence of 0.68 or higher. One error was confident (password reset predicted `refund`, 0.82), so a threshold would not catch everything, and this is based on very few examples.

**Possible improvements**

1. Route tickets with low confidence (for example below 0.6) to a human agent instead of auto-answering.
2. Use the fine-tuned model, or a hybrid of TF-IDF cue words and embeddings, for priority. The fine-tuned priority model is the best on the challenge set but is not wired into the pipeline, because its weights are large and would make the project harder to reproduce.
3. Add far more varied training data, especially Arabic dialect and mixed-intent tickets, and ideally real tickets.
4. Try a larger encoder with stronger Arabic support, and add negation examples ("no rush", "not urgent") to the training data.

## Limitations (please read)

- The dataset is **synthetic and template-based**, so test-set scores are optimistic. The challenge set is the more honest measure of generalization; expect lower numbers there.
- Labels for hard tickets follow one rule ("what the customer most needs resolved") and are subjective.
- Historical "resolutions" are invented, one per category and language; the grounded reply is only as good as those resolutions.
- The validation split used for early stopping comes from the same templates, so validation F1 reached 1.0 after a few epochs and could not separate checkpoints by generalization.
- Priority is predicted from wording only (urgency cues), not from customer tier or SLA data.
- The template reply mode does not personalize beyond the retrieved resolution.

## Acknowledgements

Built following the labs of the Applied NLP Engineering course, SDAIA Academy: https://github.com/SDAIAAcademy
