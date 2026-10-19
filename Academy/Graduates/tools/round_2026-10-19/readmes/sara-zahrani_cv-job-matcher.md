# CV → Job Matcher

**Modern Data Engineering for Advanced AI Systems** — [SDAIA Academy](https://github.com/SDAIAAcademy)

## What is this project?

A demo AI application that matches a CV to jobs.

It works in two stages. First, it collects job postings, checks them for missing or duplicate data, saves the good ones, and turns each into a vector so it can be searched by meaning. Then, when someone uploads a CV, the app turns it into a vector the same way, finds the closest postings, and gives those postings and the CV to a language model. The model writes a short assessment for each job: why it fits, what's missing, and which one to apply to first.

The model only sees the postings the app found. It doesn't search the internet or invent jobs. That's what makes this retrieval-augmented generation: retrieve the relevant data first, then generate an answer grounded in it.

For the demo, the postings are 50 sample records I generated. In a real deployment they would come from a job board's API, and only the collection step would change.

## Why didn't I build it in Colab?

I wanted to learn how I would build this in real life. Colab hides a lot: how a project is structured, how dependencies and secrets are managed, how the pieces connect, and how you test each part on its own. The models were never inside Colab anyway, they are behind an API.

I had my AI agent as a mentor the whole way. It explained each concept first, then wrote the code in small pieces, and I ran and questioned every piece before moving on.

## How does it work?

The project has two parts. The first prepares the jobs. The second matches a CV against them.

**Preparing the jobs (runs once, or when new jobs come in):**

1. Jobs arrive. I start with 50 job postings in a JSON file, generated with AI as sample data. Six are broken on purpose so the cleaning step has something to catch.
2. Each job is put in a queue by a producer, and taken out one at a time by a consumer. Producer, broker, consumer.
3. Each job is checked: required fields present, valid date, not a duplicate.
4. Good jobs are saved to a Delta table. Bad jobs go to a quarantine file with the reason they failed.
5. Each saved job is turned into a vector and stored in a vector database.

Running this twice doesn't save anything twice. It skips what it already has.

**Matching a CV (runs on every upload):**

1. Read the CV text and remove the name, email, and phone.
2. Turn the CV into a vector, using the same model that was used for the jobs.
3. Find the 5 closest jobs in the vector database.
4. If the best score is too low, stop and say there's no strong match.
5. Otherwise, give the CV and the 5 jobs to the language model and ask it to explain the fit and the gaps, using only that text.
6. Show the results, and the steps that ran.

## Why these tools?

- **Python with uv.** Same as the course.
- **asyncio queue** as the broker. Kafka would be a whole server for 50 messages.
- **Delta table** through the `deltalake` package. Same format as the course lab, no Spark, no Java.
- **Qdrant** as the vector database, in local mode. I started with Chroma like the lab, but it wouldn't install on my Mac. Same idea, different tool, one file changed.
- **OpenRouter** for both the embedding model and the chat model. One key.
- **FastAPI** with one plain HTML page.

## Does the matching actually work?

I tested it with 8 sample CVs in `data/eval/`. Focused CVs, like a backend engineer or an SRE, get the right roles at the top with a clear gap under them. Off-topic CVs, like a civil engineer, get low scores everywhere, which is why there is a threshold. Mixed-career CVs land in between.

The language model doesn't change the ranking, but it does read the postings. For the backend engineer it correctly marked two Node.js roles as weak, even though they scored highest, because the CV is Python and Go.

## What I'd do next

- Search by keywords as well as by meaning, and merge the results. Job postings are full of tool names, and keyword search catches those exactly.
- Get the top 20 by vector search, then use a second model that reads the CV and each job side by side to pick the best 5.
- Split the CV into sections and search with each, then merge. I tested cutting the CV to its summary and it didn't help, so this is a maybe.
- Replace the JSON file with a real job API. Only the producer changes.

## How to run

```bash
git clone https://github.com/sara-zahrani/cv-job-matcher.git
cd cv-job-matcher
uv sync
cp .env.example .env       # add your OpenRouter key

uv run python -m app.pipeline           # prepare the jobs
uv run uvicorn app.main:app --reload    # open http://localhost:8000
```

Free tier note: OpenRouter allows 50 free model calls a day. The pipeline uses 1, each match uses 2.

## Project structure

```
app/ingestion/    producer and broker
app/quality/      the checks and the consumer loop
app/storage/      Delta table
app/rag/          embeddings, vector store, CV, matcher, prompt, LLM
app/pipeline.py   runs the "preparing the jobs" half
app/main.py       the API and the page
data/jobs.json    the 50 sample postings
data/eval/        8 sample CVs
```
