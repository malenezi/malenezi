# Modern Data Engineering for Advanced AI Systems

## Smart Resume & Job Matching RAG System

### Project Description

This project is a Retrieval-Augmented Generation (RAG) application developed as part of the Modern Data Engineering for Advanced AI Systems program by SDAIA Academy.

The application analyzes a candidate's resume and compares it with a job description to provide an AI-powered job matching recommendation.

### How It Works

The system:

1. Extracts text from the uploaded resume.
2. Splits the resume into smaller text chunks.
3. Generates embeddings for each chunk.
4. Converts the job description or user query into an embedding.
5. Uses cosine similarity to retrieve the most relevant resume information.
6. Sends the retrieved context to a Large Language Model (LLM).
7. Generates a job matching analysis including:
   - Recommendation
   - Matching skills
   - Missing skills
   - Explanation

### Technologies Used

- Python
- Google Colab
- OpenRouter API
- Large Language Models (LLMs)
- Embeddings
- Retrieval-Augmented Generation (RAG)
- Cosine Similarity

### Project File

Smart_Resume_Job_Matching_RAG.ipynb


### Program

Modern Data Engineering for Advanced AI Systems  
[SDAIA Academy](https://github.com/SDAIAAcademy)
