# Voice of Customer — Customer Review Analyzer

**SDAIA Applied NLP Capstone | English customer feedback analysis**

## Project Overview

Voice of Customer is an end-to-end natural language processing (NLP) application that classifies the sentiment of customer reviews and explores recurring complaints. It combines a trained traditional machine-learning baseline, a pretrained Transformer sentiment classifier, an improved embedding-based classifier, and unsupervised clustering in a Gradio interface.

The implementation runs in **Google Colab** with publicly available models and data. It does **not** require an OpenAI API key, paid inference API, or retrieval-augmented generation (RAG). The Transformer models are used for **text representation and classification**, not generative response production.

### Application features

- **Single Review:** Accepts an English review and displays predictions from three sentiment classifiers. If the improved model predicts negative sentiment, the interface also shows the nearest exploratory complaint cluster.
- **Recurring Complaints:** Shows cluster sizes, representative reviews, and human-interpreted issue themes.
- **Evaluation:** Displays the measured classification scores and the complaint-clustering Silhouette Score.

## Dataset and Preprocessing

**Dataset:** [Amazon Reviews Multi — English](https://huggingface.co/datasets/goosmanlei/amazon_reviews_multi)

| Split | Negative | Positive | Total |
|---|---:|---:|---:|
| Training | 600 | 600 | 1,200 |
| Validation | 75 | 75 | 150 |
| Held-out test | 50 | 50 | 100 |

**Rating-derived sentiment labels:**

- `0 = Negative`: reviews with **1–2 stars**.
- `1 = Positive`: reviews with **4–5 stars**.
- **Three-star reviews are excluded** to keep the task binary.

Reviews shorter than 12 characters are excluded. The notebook streams each official dataset split and retains the **first eligible reviews needed to balance each class**, then shuffles the selected rows with a fixed random seed (`42`). Therefore, these are **balanced convenience samples, not uniform random samples** of the full Amazon dataset. The notebook also checks for duplicate text across the sampled splits; this does not rule out all near-duplicates.

Star ratings are **proxy labels**, not independently verified sentiment annotations. A review's wording may contradict its star rating, so label quality is examined separately during manual evaluation.

## NLP Methods

### 1. Baseline: TF-IDF + Logistic Regression

A supervised binary classifier is trained on the 1,200 labeled reviews. TF-IDF converts text into numerical features using unigrams and bigrams (up to 15,000 features); Logistic Regression learns to predict positive or negative sentiment from those features.

### 2. Pretrained sentiment Transformer: DistilBERT

The model [`distilbert/distilbert-base-uncased-finetuned-sst-2-english`](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english) is used directly for inference. It was previously fine-tuned on SST-2, but **was not fine-tuned further on the Amazon review dataset**. This provides a comparison with an existing Transformer classifier from a different review domain.

### 3. Improved model: Frozen Embeddings + Linear Head

The pretrained [`sentence-transformers/all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model converts reviews into normalized, 384-dimensional semantic embeddings. Its weights remain **frozen**. A separate Logistic Regression classification head is trained using the Amazon training labels. The regularization parameter `C` is selected from `0.1`, `1`, and `10` based on **validation Macro F1**, not by tuning on the test set.

### 4. Complaint clustering: Sentence Embeddings + K-Means

A sample of **200 negative reviews** from the training and validation partitions is converted into embeddings and grouped using **K-Means (`k=4`)**. Representative reviews closest to each cluster center provide evidence for provisional human-written issue descriptions. The cluster IDs and descriptions are **not verified issue-category labels**, and the summaries are **not LLM-generated**.

## Quantitative Evaluation

All three classifiers were evaluated on the **same 100 held-out test reviews**. Results from the completed Google Colab run:

| Model | Accuracy | Macro F1 | Test-batch elapsed time* |
|---|---:|---:|---:|
| TF-IDF + Logistic Regression (baseline) | 0.900 | 0.900 | 0.01 s |
| Pretrained DistilBERT | 0.820 | 0.816 | 15.74 s |
| **Frozen Embeddings + Linear Head** | **0.920** | **0.920** | **5.17 s** |

*Elapsed times are specific to the Colab execution and are **not controlled, like-for-like latency benchmarks**. The embedding-head timing includes embedding generation, and hardware and execution conditions can affect measurements.*

The improved model achieved a **0.020 absolute Macro F1 increase** (two percentage points) over the baseline on this 100-example test set. This is an observed result on a small sample, **not proof of general superiority**.

### Improved model confusion matrix

| Actual / Predicted | Negative | Positive |
|---|---:|---:|
| Negative | 46 | 4 |
| Positive | 4 | 46 |

The improved classifier correctly predicted **92 of 100** reviews. Precision, recall, and F1-score were **0.92 for each sentiment class**.

### Clustering findings

| Cluster | Reviews | Provisional theme |
|---|---:|---|
| 0 | 22 | Misleading product descriptions and adverse reactions |
| 1 | 66 | Missing or disputed deliveries |
| 2 | 54 | Product functionality and replacement difficulties |
| 3 | 58 | Materials, fit, and durability complaints |

**Silhouette Score: 0.038.** This score indicates weak geometric separation and significant overlap among the four embedding clusters. The theme names are interpretations of representative examples; cluster counts should not be treated as validated business issue frequencies beyond this sample.

## Manual Label Audit and Error Analysis

A **30-review sample** from the held-out test set was selected for manual sentiment-label checking. The reviewer examined the written sentiment, recorded a positive (`1`) or negative (`0`) judgment, and flagged ambiguous or mixed reviews for explanation. The completed review worksheet should be included with the submission; the original blank `30_test_reviews_TO_HAND_CHECK.csv` alone does **not** demonstrate completed manual checking.

DistilBERT disagreed with the rating-derived labels on **18 of 100** test reviews. At least **10 cases** were selected for categorized failure analysis, considering mixed sentiment, negation, ambiguous wording, domain-specific language, and possible star/text label conflicts. Categories and explanations must be confirmed from the **full review text**; automated keyword-based suggestions are not verified error causes. Some apparent model errors may actually be **label noise**.

The reported classification metrics use the **original rating-derived labels**. Manually checked labels are recorded separately and do not silently replace the original test labels.

## How to Run in Google Colab

1. Download or open `Voice_of_Customer_Capstone.ipynb` from this repository in [Google Colab](https://colab.research.google.com/).
2. Run the notebook cells **from top to bottom**. The notebook installs Python dependencies, downloads the public dataset and pretrained weights, and creates the training/validation/test samples.
3. Train the TF-IDF baseline and frozen-embedding linear head, then run the test evaluation cells. The final evaluation table should contain **all three models**.
4. Run the clustering and evidence-summary cells before launching Gradio. Avoid rerunning an older two-model evaluation cell after exporting the final three-model scores unless the improved-model evaluation is rerun afterward.
5. Run the Gradio cell and open its generated temporary `.gradio.live` link. Test the **Single Review**, **Recurring Complaints**, and **Evaluation** tabs.

**Example input:** `The product arrived late and the packaging was broken.`

In the recorded demo, all three sentiment models predicted **Negative**, and the nearest learned complaint cluster was **1**. The application only assigns a complaint cluster when the improved model predicts negative sentiment.

Gradio share links are temporary and depend on the Colab runtime remaining active. The GitHub notebook is the source submission, **not a permanently hosted web service**. Saved Colab files such as `.joblib` models or `.csv` outputs may need to be downloaded before the runtime resets. No API secret should be committed to the repository.

## Reproducibility and Limitations

- Dataset sampling uses the first eligible reviews per class, rather than uniform sampling across the entire source dataset.
- Binary sentiment labels exclude neutral feedback, and rating-derived labels sometimes disagree with the review text.
- The test set contains 100 reviews; reported differences are sensitive to sample size and review difficulty.
- The improved approach was developed after initial test results had already been inspected. Although its `C` value was selected on validation data, confirmation on a **new untouched test set** would provide stronger evidence of improvement.
- The pretrained DistilBERT classifier was adapted to SST-2 rather than this Amazon dataset; domain differences may affect performance.
- K-Means clusters overlap substantially (`Silhouette = 0.038`); descriptions are exploratory and human-interpreted.
- No additional Transformer fine-tuning, confidence-threshold abstention, generative LLM summaries, or RAG pipeline was implemented. These are potential future extensions, not claims about the current system.

## Course Reference

The project uses concepts covered in the **SDAIA Academy Applied NLP** course, including supervised baselines, Transformer-based inference, sentence embeddings, model evaluation, and interactive demonstrations.

**Official SDAIA course repository:** https://github.com/SDAIAAcademy/applied-nlp

Dataset and pretrained model credits belong to their respective providers. Their source documentation and licensing conditions should be consulted before redistribution or production use.
