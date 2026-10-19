# Arabic Employee Rights Assistant

My capstone project for the **Applied NLP Engineering** course at **SDAIA Academy**.

This project helps users find information in an official Arabic employee rights guide without searching through the full document manually. It retrieves relevant passages and generates an Arabic answer with PDF-page references. When the available information is insufficient, the assistant is instructed to say so.

**Academy:** [SDAIA Academy](https://github.com/SDAIAAcademy)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hajaralswaidan/Arabic-Employee-Rights-Assistant/blob/main/Employee_Rights_RAG.ipynb)

---

## Data Source

The project uses **دليل توعوي بالحقوق والواجبات لأصحاب العمل والعمال**, published by the Ministry of Human Resources and Social Development.

The 32-page PDF produced **77 indexed text chunks**, each stored with its source filename and PDF page number.

[Download the Official Guide](https://www.hrsd.gov.sa/sites/default/files/2025-12/dlyl-tw-wy-balhqwq-walwajbat-lashab-al-ml-wal-mal.pdf)

---

## Inputs and Outputs

| Component | Input | Output |
|---|---|---|
| Embedding Model | Document chunks or a question | One 1,024-dimensional vector per text |
| Retriever | Question embedding | Top 3 relevant chunks with source metadata |
| Generation Model | Question, instructions, and retrieved context | An Arabic answer with PDF references, or abstention |
| Chat Interface | A complete Arabic question | The assistant's response |

The embedding model supports search, while the generation model writes the answer. The assistant does not access personal HR records, and each question is processed independently.

---

## Baseline and Results

The **BM25 baseline** uses lexical matching. The main method uses **dense embeddings with cosine distance in Chroma**.

Both retrievers were evaluated on the same chunks and 15 development questions.

| Method | Page Hit@3 |
|---|---:|
| BM25 | 100% |
| Dense Embeddings | 100% |

Page Hit@3 measures the percentage of questions where a reference
page appears among the top three retrieved chunks. It measures
retrieval success, not final answer accuracy.

During manual review, a working-hours answer confused daily and weekly values. Formatting the extracted value/label pairs corrected the numbers in a later test, although some conditions can still be omitted.

---

## Documentation

- [Methodology and Model Settings](methodology.md): document preparation, chunking, embeddings, models, and generation.
- [Evaluation and Error Analysis](evaluation.md): evaluation design, manual checks, observed errors, and limitations.

---

## Interface and Examples

### Chat Interface

![Chat interface](screenshots/interface.png)

### Answer with a Source

A question about Ramadan working hours, answered with the relevant condition and PDF-page reference.

![Ramadan answer](screenshots/ramadan-answer.png)

### Saudi Dialect Question

A probation question written in Saudi dialect.

![Probation answer](screenshots/probation-answer.png)

### Missing Personal Information

The assistant explains that it cannot determine a personal leave balance from the guide.

![Abstention example](screenshots/abstention.png)

These screenshots show individual development tests, not a comprehensive accuracy evaluation. Citations refer to PDF-viewer pages rather than the page numbers printed inside the guide.

---

## Tools and Libraries

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)
![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-00695C?style=for-the-badge&logo=python&logoColor=white)
![Chroma](https://img.shields.io/badge/Chroma-FF6F00?style=for-the-badge)
![OpenRouter](https://img.shields.io/badge/OpenRouter-6467F2?style=for-the-badge)
![OpenAI Python SDK](https://img.shields.io/badge/OpenAI_Python_SDK-412991?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Rank BM25](https://img.shields.io/badge/Rank_BM25-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-F97316?style=for-the-badge&logo=gradio&logoColor=white)

The OpenAI Python SDK connects to Liquid models through OpenRouter. No model was trained from scratch or fine-tuned.

---

## How to Run

1. Open `Employee_Rights_RAG.ipynb` using the **Open in Colab** button above.
2. Run the installation and import cells.
3. Add your OpenRouter key to Colab **Secrets** as `OPENROUTER_API_KEY` and enable notebook access.
4. Download the official guide linked above and upload it when requested.
5. Run the document preparation, embedding, storage, and function-definition cells in order.
6. Run the baseline and comparison cells if you want to reproduce the evaluation.
7. Run the Gradio installation and interface cells, including `demo.launch()`.
8. Enter a complete question in the displayed chat.

The package versions used during development are recorded in
[requirements.txt](requirements.txt). The notebook's installation cells
do not automatically use these pinned versions.

A GPU is not required because the models run through API calls. Keep the Colab runtime active while using the interface.

Keep the API key in Secrets and out of the repository. Repeated API calls consume quota; a `429` response may indicate a per-minute or per-day limit. Restarting the runtime clears the in-memory collection.
