# LLMOps and Production AI Observability
## عمليات النماذج اللغوية ومراقبة الذكاء الاصطناعي الإنتاجي

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | LLMOps and Production AI Observability |
| **Arabic Title** | عمليات النماذج اللغوية ومراقبة الذكاء الاصطناعي الإنتاجي |
| **Code** | SDA-AIE-312 |
| **Level** | Expert |
| **Duration** | 4 days × 5 learning hours = **20 hours** |
| **Audience** | Engineers operating GenAI services at scale |
| **Prerequisites** | SDA-AIE-216; SDA-AIE-213 |
| **Assessment** | Labs; observability dashboard project |
| **Stackability** | Expert operations badge · part of the MLOps & Reliability specialisation · Next: SDA-AIE-314 / SDA-AIE-390 |
| **Tools & Platforms** | LangSmith/Langfuse · OpenTelemetry · Grafana · evaluation pipelines |

## Course Description

An expert module on operating LLM and generative-AI workloads in production. Participants implement tracing, quality monitoring, feedback loops, and incident response for AI services, extending MLOps discipline to non-deterministic systems. The module covers evaluation-in-production, prompt/version management, and reliability engineering for AI platforms.

The course is built around a single evolving artefact: **"Musaid" (مساعد)**, a bilingual (Arabic/English) citizen-services assistant for a national digital-government portal. Musaid is a RAG-plus-tools LLM service that answers questions about government procedures — renewing an ID, booking an appointment, checking a violation. It was designed and deployed in earlier modules; in SDA-AIE-312 the class does not build the model, it **operates** it. Every lab instruments, measures, or hardens Musaid, so by Day 4 each participant owns a fully observable, evaluated, SLO-governed LLM service with an incident runbook and a live Grafana dashboard — the same operational surface they will defend in the AI Engineer capstone (SDA-AIE-390).

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Design observability architectures for LLM applications with distributed tracing
2. **LO2** — Implement online evaluation, quality scoring, and user-feedback loops
3. **LO3** — Develop prompt and model version-management workflows with safe rollouts
4. **LO4** — Analyze production incidents in AI systems and build response runbooks
5. **LO5** — Implement SLOs, alerting, and reliability dashboards for AI services
6. **LO6** — Optimize the operations lifecycle for continuous improvement of deployed LLM systems

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Seeing inside the black box | M1: From MLOps to LLMOps · M2: Tracing and Logging for LLM Pipelines | 45% | 55% | Fully traced Musaid request path with span tree in Langfuse + OTel |
| **Day 2** | Measuring quality in production | M3: Online Evaluation and Quality Monitoring · M4: Prompt Registries and Version Management | 40% | 60% | Online eval pipeline scoring live traffic + versioned prompt registry with a shadow rollout |
| **Day 3** | Closing the loop and staying up | M5: Feedback Loops and Data Flywheels · M6: SLOs, Alerting, and Incident Response | 35% | 65% | Feedback ingestion → curated dataset + SLO/error-budget dashboard with firing alert and runbook |
| **Day 4** | Platform reliability and capstone | M7: Reliability Engineering for AI Platforms · Capstone | 30% | 70% | Reliability-hardened service + capstone observability dashboard demo |

## Hour-by-Hour Breakdown

### Day 1 — Seeing Inside the Black Box

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why LLM systems break the MLOps playbook** + course kickoff | Name what changes from MLOps to LLMOps: non-determinism, open-ended I/O, no single accuracy metric, cost/latency variance | Interactive lecture + incident-story discussion | 80/20 |
| 2 | **The LLMOps lifecycle and observability foundation** (M1) | Reference architecture; the four pillars (traces, metrics, logs, quality); where blind spots live today | Lecture + architecture walkthrough | 70/30 |
| 3 | **Lab 1 — Baseline the blindness** | Run Musaid, generate traffic, prove you cannot answer 5 operational questions; establish cost/latency baseline | Guided lab (pairs) | 15/85 |
| 4 | **Tracing and logging for LLM pipelines** (M2) | Spans for RAG+tools; OTel GenAI semantic conventions; what to capture and what never to log | Lecture + live instrumentation demo | 65/35 |
| 5 | **Lab 2a — Instrument the request path** | Add tracing to retriever, prompt build, LLM call, tool calls; view the span tree in Langfuse | Guided lab (pairs) | 10/90 |

### Day 2 — Measuring Quality in Production

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Lab 2b — Structured logging and cost/token capture** | Correlate logs to traces; capture token usage, cost, model version per span; sample high-volume traffic | Lab + micro-lecture | 20/80 |
| 2 | **Online evaluation and quality monitoring** (M3) | Reference-free evaluators; LLM-as-judge; RAG faithfulness; sampling and guardrail scores; drift on quality | Lecture + evaluator design demo | 65/35 |
| 3 | **Lab 3 — Score live traffic** | Build an async online-eval worker; faithfulness + relevance + safety scores on sampled traces; quality dashboard tile | Guided lab | 10/90 |
| 4 | **Prompt registries and version management** (M4) | Prompt as versioned artefact; registry patterns; linking versions to traces; canary/shadow rollouts | Lecture + registry walkthrough | 65/35 |
| 5 | **Lab 4 — Versioned prompts and a shadow rollout** | Move prompts into Langfuse registry; run v2 in shadow; compare eval scores before promotion | Guided lab | 10/90 |

### Day 3 — Closing the Loop and Staying Up

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Feedback loops and data flywheels** (M5) | Explicit vs implicit feedback; trace→dataset curation; the flywheel; annotation queues; PDPL-safe handling | Lecture + flywheel design demo | 60/40 |
| 2 | **Lab 5 — Build the flywheel** | Capture thumbs + implicit signals; route low-score traces to an annotation queue; export a curated eval set | Guided lab | 10/90 |
| 3 | **SLOs, alerting, and incident response** (M6) | SLIs/SLOs/error budgets for LLM services; multi-window burn-rate alerts; runbooks; AI-specific incidents | Lecture + SLO math + runbook demo | 55/45 |
| 4 | **Lab 6a — SLO dashboard and burn-rate alerts** | Define SLIs; build Grafana SLO panel; wire a burn-rate alert; trigger it with a fault injection | Guided lab | 10/90 |
| 5 | **Lab 6b — Run an incident** | Inject a hallucination-spike incident; follow the runbook; write the postmortem | Simulation + lab | 10/90 |

### Day 4 — Platform Reliability and Capstone

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Reliability engineering for AI platforms** (M7) | Graceful degradation, fallbacks, timeouts, circuit breakers, caching, load shedding; multi-provider resilience | Lecture + reliability-pattern demo | 60/40 |
| 2 | **Lab 7 — Harden Musaid** | Add fallback model, semantic cache, timeout+retry budget, circuit breaker; prove behaviour under provider outage | Guided lab | 10/90 |
| 3 | **Capstone assembly** | Integrate tracing + eval + registry + feedback + SLO + reliability into one dashboard; complete checklist | Project work | 0/100 |
| 4 | **Capstone assembly + peer review** | Finalize dashboard, runbook, and DECISIONS.md; peer operational-readiness review round | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 6-minute demos; rubric-based peer + instructor scoring; path to SDA-AIE-314/390 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module operates the same service — **Musaid**, the bilingual citizen-services assistant. Never introduce a throwaway toy chatbot; always instrument, evaluate, or harden Musaid. This is what makes the Day-4 capstone assembly (not build) achievable.
- **Pace control:** Labs 3 (online eval) and 6 (SLO + incident) are the most overrun-prone. Publish checkpoint commits (`lab1-start`, `lab2-solution`, `lab3-start`, …) and pre-seeded trace data so stragglers can `git checkout lab3-start` and still have realistic traffic to score.
- **Pairing:** rotate pairs each day. Pair a strong-SRE/ops participant with a strong-LLM/ML participant — the whole point of LLMOps is fusing those two cultures.
- **Environment strategy:** primary = Docker Compose stack (Musaid API + Langfuse + Postgres + Prometheus + Grafana + OTel Collector) on the lab laptop; fallback = a shared classroom cluster and a mock-LLM mode (deterministic canned responses) so labs never block on external LLM API access or quota.
- **Language and data residency:** deliver in English or Arabic; keep all code, identifiers, span names, and commit messages in English. Musaid handles Arabic and English user text — treat all user content as personal data under **PDPL**; no raw prompts/PII leave the sovereign boundary in logs or eval payloads without masking.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day-4 morning protects build time; cut discussion, not assembly.
- **Assessment logistics:** rubric scoring happens live during Day 4 Hour 5 demos; collect dashboard URLs and repo URLs at the end of Hour 4 so the instructor can verify live SLO panels and eval history before demos begin.
- **Cost discipline:** the course itself is an LLMOps exercise — run labs in mock-LLM mode by default and switch to a real provider only for the evaluation and rollout labs, capping spend with the same budget alerts the course teaches.

---

# Module 1 — From MLOps to LLMOps: What Changes

## Module Overview

**Purpose.** Participants arriving from SDA-AIE-216 already own the MLOps backbone: pipelines, registries, drift monitors, canary releases. This module names precisely what that backbone does *not* cover once the model is a non-deterministic, open-ended, externally-hosted LLM, and re-frames observability — not accuracy dashboards — as the foundation of operating generative AI. It sets the reference architecture and vocabulary the rest of the course builds on.

**Business relevance.** A national citizen-services assistant cannot be operated like a churn classifier. There is no held-out test set that predicts tomorrow's user questions; a single prompt or model-provider change can silently degrade answer quality for millions of interactions; cost scales with tokens, not requests; and a wrong answer about renewing an Iqama is a public-trust and compliance event, not a rounding error in an F1 score. Saudi entities operating GenAI at scale (government portals, banks under SAMA, health providers) need an operations discipline that treats quality, cost, and safety as first-class production signals.

**Industry use cases.**
- A government portal assistant whose answer quality drifts after the provider silently updates the base model behind the same API name.
- A banking support copilot where a two-word prompt tweak doubles average latency and blows the monthly token budget.
- A health triage assistant that must prove, per interaction, which model version and which knowledge snapshot produced each answer for audit.

**Expected competencies.** After this module a participant can articulate the MLOps→LLMOps deltas, draw the LLMOps reference architecture, identify the four observability pillars for an LLM service, enumerate the new failure modes, and state which operational questions a currently un-instrumented service cannot answer.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Explain how non-determinism, open-ended I/O, and external hosting break MLOps assumptions | LO1 |
| 1.2 | Enumerate LLM-specific failure modes and the signal each requires | LO1, LO5 |
| 1.3 | Draw the LLMOps reference architecture and the four observability pillars | LO1 |
| 1.4 | Map which operational questions require traces vs metrics vs quality scores | LO1, LO6 |
| 1.5 | Assess an un-instrumented service against an operational-readiness checklist | LO6 |

## Technical Content

### 1. Why LLM systems break the MLOps playbook

MLOps was designed around a comforting set of assumptions: the model is a deterministic function, quality collapses to a small set of metrics computable against labelled data, the input space is a fixed schema, and the model runs on infrastructure you control. Every one of these assumptions fails for a production LLM service.

- **Non-determinism.** The same request can produce different outputs (temperature > 0, provider-side batching, model updates). "Reproduce the bug" is not a given; you reproduce *distributions*, not single runs.
- **Open-ended input and output.** Users type anything, in Arabic or English, in any register. There is no `pydantic` schema that constrains meaning. Output is free text whose correctness is contextual.
- **No single accuracy number.** Quality is multi-dimensional: faithfulness to retrieved context, relevance, safety, tone, format, refusal-appropriateness. No held-out set predicts tomorrow's traffic.
- **External, mutable dependencies.** The "model" is often an API. The vendor can change it under you. Rate limits, outages, and latency spikes are *their* infrastructure, surfacing as *your* incident.
- **Cost is a runtime variable.** Spend scales with tokens per request × requests, and a longer prompt or a chattier model silently multiplies the bill. Cost is an SLI now, not a procurement line item.

**Instructor note:** open the discussion by asking the room "how would you reproduce a bad answer a user reported yesterday?" Let the impossibility surface naturally — it motivates tracing (M2) and captured inputs before you name any tool.

### 2. The new failure modes and the signal each demands

Name these explicitly; each maps to a later module's remedy.

| Failure mode | What it looks like | Signal that catches it | Covered in |
|---|---|---|---|
| Hallucination | Confident, wrong, ungrounded answer | Online faithfulness eval on sampled traces | M3 |
| Silent quality decay | No errors, no latency change — answers just get worse | Trend on quality scores; regression vs golden set | M3, M5 |
| Prompt drift / regression | A "small" prompt edit degrades a segment | Prompt version linked to eval scores; shadow test | M4 |
| Provider model swap | Same API, new weights, different behaviour | Model-version tag on every trace; canary eval | M2, M4 |
| Cost/token blowout | Bill triples with no traffic change | Token + cost per span; budget-burn alert | M2, M6 |
| Latency variance | p99 spikes from provider or long contexts | Span timing; latency SLO | M2, M6 |
| Retrieval failure | RAG returns irrelevant/empty context | Context-relevance score; retrieval span inspection | M2, M3 |
| Feedback blindness | Users are unhappy, you cannot see it | Explicit + implicit feedback capture | M5 |
| Cascading outage | Provider down → whole service down | Fallbacks, circuit breakers, error-budget alert | M6, M7 |

### 3. The LLMOps lifecycle and reference architecture

LLMOps is a loop, not a pipeline. The operational cycle: **serve → observe (trace) → evaluate (score) → learn (feedback/datasets) → improve (prompt/model change) → roll out safely → serve.** MLOps' train/deploy/monitor loop still exists underneath (for any fine-tuned components), but the fast, dominant loop in production is this observe-evaluate-improve cycle running on live traffic.

The reference architecture for Musaid:

```
                         ┌─────────────────────────── Observability plane ──────────────────────────┐
 user ──► API gateway ──► Musaid app ──► retriever ──► prompt build ──► LLM (provider) ──► tools     │
            │              │  (spans emitted at every hop via OpenTelemetry)                          │
            │              └──► OTel SDK ──► OTel Collector ──► ┬─► Langfuse (traces, eval, prompts)   │
            │                                                  ├─► Tempo (trace store)                 │
            │                                                  ├─► Prometheus (metrics: latency, cost) │
            │                                                  └─► Loki (structured logs)              │
            │                                                                                          │
            └──► feedback endpoint ──► Langfuse scores ──► annotation queue ──► curated datasets       │
                                                              │                                        │
   online-eval worker ◄── samples traces ── scores ──────────┘                                        │
   Grafana ◄── dashboards (latency / cost / quality / SLO) + Alertmanager (burn-rate alerts)          │
                         └────────────────────────────────────────────────────────────────────────────┘
```

Two ideas anchor everything downstream:

1. **The trace is the unit of truth.** Every operational question — why was this answer wrong, what did it cost, which prompt/model produced it, how long did retrieval take — is answered by inspecting one trace with rich spans. If it is not on the trace, it did not happen as far as operations is concerned.
2. **Quality is a pillar, not an afterthought.** Classic observability has three pillars (traces, metrics, logs). For LLM systems there is a fourth first-class pillar — **quality/evaluation scores** — and it is the one that distinguishes LLMOps from ordinary APM.

### 4. What carries over vs what changes

| Concern | MLOps (SDA-AIE-216) | LLMOps (this course) |
|---|---|---|
| Versioning | Model + data versioning | + **prompt** versioning, + context/knowledge snapshot, + provider model tag |
| Monitoring | Feature/prediction drift, perf decay | + faithfulness/quality drift, hallucination rate, refusal rate |
| Evaluation | Offline on held-out set | + **online** eval on sampled live traffic (reference-free, LLM-as-judge) |
| Release | Canary/blue-green on your infra | + prompt canary/shadow, provider fallback, cost-aware rollout |
| Core SLIs | Availability, latency, accuracy | + quality score, token cost, hallucination rate, groundedness |
| Debugging | Logs + metrics | + **distributed traces of the reasoning path** (retrieval→prompt→LLM→tools) |
| Incident cause | Data/infra | + prompt regression, provider change, retrieval failure, jailbreak |
| Feedback | Labels from a labelling team | + live user thumbs/edits feeding a data flywheel |

The message: LLMOps does not replace MLOps; it **extends** it with a quality pillar, prompt lifecycle, online evaluation, and provider-resilience — all resting on distributed tracing.

### 5. Observability as the foundation — the four pillars

- **Traces** — the causal path of one request across retrieval, prompt assembly, model call, and tool use, with inputs/outputs and timing at each span. The primary debugging surface.
- **Metrics** — aggregable time series: request rate, latency percentiles, error rate, tokens, cost, cache hit rate. The primary alerting surface.
- **Logs** — structured, correlated-by-trace-id events; the "why" details a metric cannot hold.
- **Quality** — evaluation scores (faithfulness, relevance, safety, format) attached to traces and aggregated as time series. The pillar that answers "is the service *good*", not just "is it up".

A team that has all four for Musaid can, within minutes, answer: *what is our hallucination rate this hour, on which topics, at what cost, produced by which prompt and model version, and can I open the exact trace of the worst example?* A team that has none is operating blind — which is where Lab 1 deliberately starts.

### 6. Real-world example walkthrough

Narrate this (5 minutes, no slides): a public-sector assistant went live with excellent launch-week feedback. Ten weeks later, complaint volume crept up. There were no errors in the logs, latency was flat, the dashboard was green. What had happened: the model provider rolled a minor version behind the same API name; the new weights were more verbose and slightly less willing to say "I don't know", so on edge-case procedural questions Musaid began confidently inventing steps. Nobody could see it because (a) no model-version tag was on requests, (b) no online quality eval existed, and (c) user unhappiness never became a signal. The fix was not a better model — it was the four pillars. This course builds exactly that instrumentation.

## Code Examples

### The Musaid request path (the thing we will instrument)

```python
# src/musaid/service/assistant.py
"""Musaid: bilingual citizen-services assistant (RAG + tools).

This is the ALREADY-BUILT service from prior modules. In SDA-AIE-312 we do
not change its logic first — we make it OBSERVABLE. Read it as the map of
where spans, scores, and costs must be captured.
"""
from dataclasses import dataclass

from musaid.domain.entities import UserQuery, Answer
from musaid.service.interfaces import Retriever, LLMClient, ToolRegistry
from musaid.service.prompts import build_prompt


@dataclass
class MusaidAssistant:
    retriever: Retriever          # vector search over gov-service docs
    llm: LLMClient                # provider-backed chat model
    tools: ToolRegistry           # e.g. appointment lookup, fee calculator
    prompt_name: str = "citizen_assistant"
    prompt_version: str = "v1"

    def answer(self, query: UserQuery) -> Answer:
        # 1) retrieve grounding context (RAG)
        chunks = self.retriever.search(query.text, k=6, lang=query.lang)
        # 2) assemble the prompt from a named, versioned template
        messages = build_prompt(self.prompt_name, self.prompt_version,
                                query=query.text, context=chunks, lang=query.lang)
        # 3) call the model (may itself request a tool call)
        completion = self.llm.chat(messages)
        # 4) if the model asked for a tool, run it and re-ask
        if completion.tool_call:
            result = self.tools.run(completion.tool_call)
            messages.append(result.as_message())
            completion = self.llm.chat(messages)
        return Answer(
            text=completion.text,
            citations=[c.source_id for c in chunks],
            model_version=completion.model_version,
            prompt_version=self.prompt_version,
        )
```

### The five operational questions we currently cannot answer

```python
# tests/operability/test_blind_spots.py
"""Lab 1 makes these five questions concrete. Today every one raises
NotImplementedError because the signal does not exist. By end of course,
each is a dashboard query or a trace lookup.
"""
import pytest

BLIND_SPOTS = [
    "What was our hallucination rate in the last hour, by topic?",   # -> M3
    "What did the average answer cost in tokens and SAR yesterday?", # -> M2
    "Which prompt+model version produced the worst-rated answer?",   # -> M2/M4
    "How many users gave a thumbs-down, and on which intents?",      # -> M5
    "Is our answer-quality SLO in or out of error budget right now?",# -> M6
]

@pytest.mark.parametrize("question", BLIND_SPOTS)
def test_we_cannot_answer_yet(question):
    with pytest.raises(NotImplementedError):
        raise NotImplementedError(f"No signal exists for: {question}")
```

## Hands-on Lab 1 — Baseline the Blindness

| | |
|---|---|
| **Objective** | Stand up the Musaid stack, generate realistic bilingual traffic, and *prove* the service is un-observable by attempting to answer five operational questions; capture a cost/latency baseline for later comparison |
| **Duration** | 50 minutes |
| **Setup** | Docker + Compose, course repo cloned, `git checkout lab1-start`, `make up` (starts Musaid API + mock-LLM + Postgres) |

**Instructions & tasks**

1. *(5 min)* `make up`; confirm `GET /health` is 200 and send one Arabic and one English question via `/v1/ask`; read the raw JSON answer.
2. *(10 min)* Run the traffic generator `python tools/generate_traffic.py --n 300 --mix ar,en` (replays a realistic intent mix: ID renewal, appointments, violations, fees).
3. *(15 min)* Attempt each of the five operational questions from `test_blind_spots.py` using only what exists today (logs, `docker logs`). Record in `BASELINE.md` *why* each is unanswerable.
4. *(10 min)* Instrument the single cheapest signal: wrap `assistant.answer()` with a timer and a token counter (mock-LLM returns token counts); log latency_ms and total_tokens per request as JSON.
5. *(5 min)* Compute a crude baseline from those logs with `jq`: p50/p95 latency, mean tokens/request, estimated SAR/1k requests.
6. *(5 min)* Commit `chore: baseline latency/cost + documented blind spots`.

**Expected output**
```
$ python tools/generate_traffic.py --n 300 --mix ar,en
Sent 300 requests (168 ar / 132 en) across 6 intents. 0 errors.

$ jq -s 'add/length' logs/latency.jsonl        # mean latency_ms
612.4
$ jq -s '[.[].total_tokens]|add/length' logs/tokens.jsonl
1180.7
BASELINE.md: 5/5 operational questions currently UNANSWERABLE (documented)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `/v1/ask` returns 503 | Mock-LLM container not ready | `docker compose ps`; wait for `mock-llm` healthy; readiness gates traffic (M2/M6 topic) |
| Arabic text mojibake in logs | Non-UTF8 log handler | Force `ensure_ascii=false`; flag this — encoding bugs corrupt Arabic eval later |
| jq errors on token file | A request errored, wrote no token field | This *is* a blind spot — note that partial failures are invisible |
| Latency wildly variable | Mock-LLM injects jitter by design | Correct; motivates percentile thinking over averages |

**Instructor notes.** The emotional beat of this lab is the moment a pair confidently says "we can just grep the logs" and then discovers the logs do not contain model version, prompt version, retrieved context, or any quality signal. Let that land before Module 2. Fast finishers: have them sketch, on paper, the span tree they *wish* they had — you will build exactly it in Lab 2.

## Mini Exercises

**Quiz (5 questions)**
1. Which MLOps assumption fails hardest for an LLM API service? (a) deterministic output (b) fixed input schema (c) self-hosted infra (d) all of them → **d**.
2. Name the fourth observability pillar unique to LLMOps. → quality/evaluation scores.
3. A provider swaps model weights behind the same API name — which single trace attribute makes this detectable? → model_version tag.
4. Why is "reproduce the bug" harder for LLMs than classifiers? → non-determinism; you reproduce distributions, not single runs.
5. True/False: cost is a procurement concern, not an SLI. → **False** — token cost is a runtime SLI in LLMOps.

**Debugging exercise.** Give participants a green dashboard (latency flat, error rate ~0) alongside a rising complaint count. Ask: which pillar is missing, and what one signal would explain it? (Quality pillar; online faithfulness eval + model-version tag.)

**Design exercise.** Each pair draws the LLMOps reference architecture for Musaid from memory and marks where each of the nine failure modes (§2) would first become visible. Compare to the instructor's version.

**Discussion questions.**
- Your MLOps platform team says "we already have monitoring." What can they *not* answer about Musaid today, and which pillar closes the gap?
- Should answer quality be owned by data science, engineering, or a new ops role? What does your answer imply about who carries the pager?

## Case Study — The Silent Provider Upgrade

**Scenario.** "Khidmah", a national services assistant modelled on Musaid, serves 200k conversations/day. Over one weekend, average answer length rose 18% and "I don't have that information" responses fell by half — with zero deploys on the team's side. Complaints about *confidently wrong* procedural steps rose the following week.

**Business context.** The assistant is the front door to dozens of government procedures; a wrong step ("bring form X") wastes citizens' trips to service centres and erodes trust in digital government. The board asks a simple question the team cannot answer: "did something change, and was it us?"

**Technical challenge.** With no model-version tags, no online quality eval, and no captured inputs/outputs, the team cannot even confirm a change occurred, let alone attribute it.

**Constraints.** The provider will not confirm or roll back the silent update; the team cannot switch providers within the incident window; all user text is PDPL-protected and cannot be freely exported for offline analysis.

**Solution approach (facilitate, don't lecture).** Establish the four pillars retroactively: (1) tag every request with provider model version and prompt version (M2); (2) start sampling traces into an online faithfulness/refusal evaluator (M3); (3) pin the model to a specific version string where the provider allows it, and shadow-test the new version (M4); (4) stand up a quality SLO with a burn-rate alert so the *next* silent change pages someone in an hour, not a fortnight (M6). Everything the class builds this week is the postmortem's action list.

**Discussion questions.**
1. Which single pillar, added first, would have detected the change fastest?
2. How do you attribute a quality regression to the provider vs your own retrieval, without exporting raw PII?
3. What contractual/version-pinning ask should ops make of any LLM provider?
4. Write the one-paragraph board update you *could* give once the four pillars exist.

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Operational questions answerable | Observability | Baseline documented (0/5), target set (5/5 by course end) | `BASELINE.md` review |
| Latency baseline captured | Performance | p50/p95 recorded per intent | `jq` over latency logs |
| Cost baseline captured | Cost | Mean tokens/request + SAR/1k estimate recorded | token-log analysis |
| Failure modes enumerated | Observability | All 9 mapped to a signal | design exercise |
| Architecture recall | Understanding | Reference architecture reproduced unaided | paired sketch |

**Example baseline table (filled during lab):**

| Signal | Value at Lab 1 | Available? |
|---|---|---|
| p50 / p95 latency | 540 ms / 1,180 ms | ✅ (added in lab) |
| Mean tokens/request | 1,181 | ✅ (added in lab) |
| Hallucination rate | unknown | ❌ → M3 |
| Prompt/model version per request | not captured | ❌ → M2/M4 |
| User feedback rate | not captured | ❌ → M5 |

## Required Visuals and Training Assets

### Diagrams
1. **LLMOps reference architecture** — *Purpose:* anchor image for the whole course. *Elements:* request path (gateway→app→retriever→prompt→LLM→tools) with the observability plane (OTel Collector fanning out to Langfuse/Tempo/Prometheus/Loki) and Grafana/Alertmanager; feedback loop drawn back into datasets. *Style:* flat vector, plane-separated, English labels with Arabic subtitles.
2. **MLOps → LLMOps delta map** — *Purpose:* frame the whole module. *Elements:* two columns with arrows showing what carries over vs what is added (quality pillar, prompt lifecycle, online eval, provider resilience). *Style:* before/after split.
3. **Four pillars of LLM observability** — *Purpose:* memorable reference. *Elements:* four labelled columns (Traces/Metrics/Logs/Quality) each with the questions it answers and the Musaid example. *Style:* four-panel poster, printable A4.
4. **The LLMOps loop** — *Purpose:* show operations as a cycle. *Elements:* serve→observe→evaluate→learn→improve→roll out, with the module that owns each arc labelled. *Style:* circular flow.

### Images (screenshots)
1. **Green-dashboard-but-unhappy-users** — *why:* motivates the quality pillar; *content:* flat latency/error panels next to a rising complaint chart.
2. **Raw Musaid JSON answer with no metadata** — *why:* shows the blindness concretely; *content:* an answer body lacking model/prompt version and any score.
3. **`jq` baseline session** — *why:* expected-output reference; *content:* the latency/token computation from Lab 1.

### Simulations
1. **Silent-provider-swap** — *Setup:* mock-LLM has a `--persona verbose_overconfident` flag that mimics a model update. *Expected:* answers lengthen, refusals drop, no error/latency change. *Learning objective:* invisible-without-quality-pillar.
2. **Partial-failure invisibility** — *Setup:* 3% of requests error after the LLM call but before logging. *Expected:* token/latency stats silently exclude them. *Learning objective:* what you don't instrument, you cannot see.

### Interactive Activities
- **"Which pillar answers this?" card sort (12 min):** 15 operational-question cards sorted onto Traces/Metrics/Logs/Quality lanes; defend edge cases (cost = metric derived from trace).
- **Failure-mode-to-signal matching (10 min):** teams match the nine failure modes to the signal that catches each and the module that builds it.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `gov_services_kb/` | Synthetic KSA gov-service procedure docs (ID, passport, appointments, fees), AR+EN | Markdown | ~120 docs | Musaid RAG corpus, reused all modules |
| `intent_traffic.jsonl` | Course-generated realistic query mix, AR+EN | JSONL | 2,000 queries | Traffic generator for all labs |
| `eval_gold_v1.jsonl` | Curated Q→ideal-answer+context pairs | JSONL | 150 items | Reference set introduced here, used in M3/M4 |

### Demo Requirements
- **Instructor demo:** attempt live, on the projector, to answer "what did yesterday's average answer cost?" from raw logs — and fail — before naming the four pillars.
- **Student demo:** two pairs present their `BASELINE.md` blind-spot findings at end of Hour 3.
- **Expected outputs:** running Musaid stack; documented baseline; five blind spots articulated and mapped to future modules.

---

# Module 2 — Tracing and Logging for LLM Pipelines

## Module Overview

**Purpose.** A trace is the unit of truth for an LLM service. This module teaches participants to instrument the full Musaid request path — retrieval, prompt assembly, model call, tool calls — as a tree of spans carrying inputs, outputs, timing, tokens, cost, and version tags, using OpenTelemetry and the GenAI semantic conventions, exported to Langfuse for LLM-native inspection and to the metrics/logs backends for aggregation and correlation.

**Business relevance.** When a citizen reports a wrong answer, or the board asks why cost tripled, the answer must be one trace-lookup away. In regulated Saudi contexts the trace is also the audit record: which knowledge snapshot, which prompt version, which model produced this answer. Instrumentation is not optional telemetry — it is the operational and compliance substrate every later capability (eval, rollout, incident response) reads from.

**Industry use cases.**
- A support copilot where a single trace shows retrieval returned empty context, explaining a hallucination in seconds rather than hours.
- A bank assistant that must produce, per interaction, an immutable record of model+prompt+data version for a SAMA audit.
- A high-volume assistant where head-based sampling keeps trace cost bounded while always keeping errored and low-quality traces.

**Expected competencies.** Participants can instrument a RAG+tools pipeline with nested spans, apply GenAI semantic-convention attributes, capture tokens/cost/version safely, correlate structured logs to traces by trace-id, redact PII at the boundary, and configure sampling that never drops the traces that matter.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Instrument a RAG+tools request as a nested span tree with OpenTelemetry | LO1 |
| 2.2 | Apply GenAI semantic conventions and capture tokens, cost, and version tags | LO1 |
| 2.3 | Export traces to Langfuse and to an OTel backend without double-instrumenting | LO1 |
| 2.4 | Correlate structured logs to traces and redact PII at the boundary | LO1, LO6 |
| 2.5 | Configure sampling that preserves errored and low-quality traces | LO1, LO5 |

## Technical Content

### 1. Anatomy of an LLM trace

A trace represents one user request; spans represent operations within it, nested by causality. For a Musaid `answer()` call the ideal span tree is:

```
ask (root span)  ── attributes: session_id, lang, trace_id
├── retrieve         ── query, k, top_source_ids, n_chunks, retrieval_ms, score_of_top_chunk
├── build_prompt     ── prompt_name, prompt_version, template_tokens, context_tokens
├── llm.chat #1      ── gen_ai.request.model, gen_ai.usage.input_tokens/output_tokens,
│                        temperature, finish_reason, cost_sar, model_version, ttft_ms
├── tool.appointment_lookup ── tool_name, args_redacted, tool_ms, ok
└── llm.chat #2      ── (post-tool) tokens, cost, model_version
```

The discipline: **one span per meaningful operation**, each with the inputs and outputs needed to understand it in isolation, and timing that sums (with gaps) to the parent. The root span carries request-level identity (session, language, trace id). The LLM spans carry the GenAI-specific attributes. Everything downstream — evaluation, cost dashboards, incident debugging — reads this structure.

### 2. OpenTelemetry and the GenAI semantic conventions

Use OpenTelemetry as the vendor-neutral instrumentation API so you are not locked to one backend, and follow the **OTel GenAI semantic conventions** so attribute names are standard and dashboards are portable. Key conventions (2025-era `gen_ai.*` namespace):

| Attribute | Meaning |
|---|---|
| `gen_ai.system` | provider/system, e.g. `openai`, `anthropic`, `local` |
| `gen_ai.request.model` | requested model name |
| `gen_ai.response.model` | model that actually answered (catches silent swaps) |
| `gen_ai.request.temperature` | sampling temperature |
| `gen_ai.usage.input_tokens` / `output_tokens` | token counts |
| `gen_ai.response.finish_reason` | stop / length / tool_calls / content_filter |
| `gen_ai.operation.name` | chat / embeddings / tool |

To these, add operational extensions your platform standardises: `musaid.prompt.version`, `musaid.cost.sar`, `musaid.retrieval.top_score`, `musaid.answer.has_citations`. Standard names let Grafana panels and eval jobs work across services; custom names carry your business signals. Never invent a new name where a convention exists — portability is the point.

### 3. Two backends, one instrumentation

Musaid emits spans once (OTel SDK) and fans them out:

- **Langfuse** — the LLM-native view: it understands "generations", shows prompt/completion side by side, aggregates token cost, links prompt versions and evaluation scores to spans. This is where engineers *read* a trace. Use the OpenInference/OTel exporter so Langfuse ingests the same spans.
- **OTel Collector → Tempo / Prometheus / Loki** — the platform view: Tempo stores traces, Prometheus stores metrics derived from spans (latency histograms, token counters, cost), Loki stores correlated logs. This is where you *alert and aggregate*.

The rule: **instrument once, export twice.** Do not hand-roll Langfuse calls *and* OTel spans for the same operation — you get double counting and divergent data. Wrap the LLM client once; both exporters read the same spans.

### 4. What to capture — and what must never be logged

Capture generously on spans, but treat all user content as PDPL-protected personal data:

- **Always capture:** timings, token counts, cost, model/prompt/knowledge versions, finish reasons, retrieval scores and source ids, tool names and status, error types.
- **Capture with care (redaction/hashing):** the user query and the answer text — needed for debugging and eval, but must be redacted for PII (national id, phone, names) and access-controlled. Store a hash or a redacted form on the always-visible span; keep the full text in a restricted store keyed by trace id, with retention limits.
- **Never capture:** secrets/API keys, raw national ID / card numbers / full addresses, anything on the forbidden-field list, in any span, log, or metric label.
- **Never put high-cardinality values in metric labels** (trace id, session id, raw query) — they explode Prometheus. Cardinality lives in traces/logs, not metric dimensions.

### 5. Correlation and structured logging

Logs and traces must join on `trace_id`. Every log line Musaid emits binds the current trace/span id from the OTel context, so a Grafana user can pivot from a slow trace to its logs and back. Logs are structured JSON to stdout; the platform ships them. The `prediction`/answer event logs bucketed, non-PII fields only (decision, latency bucket, model version, has_citations) — never the raw answer at INFO. This is the same discipline as SDA-AIE-216's logging module, extended with trace correlation.

### 6. Sampling without losing what matters

At high volume you cannot store every trace's full payload. Use **tail-aware sampling**:

- Keep **100%** of errored traces, low-quality-scored traces, and a configurable set of flagged sessions.
- Keep a **head-based sample** (e.g., 10%) of normal traffic for baseline stats.
- Keep **metrics for 100%** of traffic regardless — sampling drops payloads, never counters. Latency/cost/error metrics are always complete; only the expensive full-payload traces are sampled.

Common mistakes: uniform random sampling that throws away the rare bad trace you most need; sampling metrics along with traces (breaking your rate/latency numbers); logging full answers at INFO and blowing up both cost and PDPL exposure; and putting the query string in a metric label.

## Code Examples

### Instrumenting the request path with OpenTelemetry

```python
# src/musaid/observability/tracing.py
"""Single instrumentation layer. Spans follow OTel GenAI conventions and
export to BOTH Langfuse and the OTel Collector. Instrument once, export twice.
"""
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode

tracer = trace.get_tracer("musaid.assistant")


def traced_answer(assistant, query):
    with tracer.start_as_current_span("ask") as root:
        root.set_attribute("musaid.lang", query.lang)
        root.set_attribute("session.id", query.session_id)   # not a metric label!
        try:
            with tracer.start_as_current_span("retrieve") as s:
                chunks = assistant.retriever.search(query.text, k=6, lang=query.lang)
                s.set_attribute("musaid.retrieval.k", 6)
                s.set_attribute("musaid.retrieval.n_chunks", len(chunks))
                s.set_attribute("musaid.retrieval.top_score",
                                round(chunks[0].score, 4) if chunks else 0.0)
                s.set_attribute("musaid.retrieval.source_ids",
                                [c.source_id for c in chunks])

            with tracer.start_as_current_span("build_prompt") as s:
                messages = assistant._build(query, chunks)
                s.set_attribute("musaid.prompt.name", assistant.prompt_name)
                s.set_attribute("musaid.prompt.version", assistant.prompt_version)

            completion = _traced_llm_call(assistant.llm, messages)
            root.set_attribute("gen_ai.response.model", completion.model_version)
            root.set_attribute("musaid.answer.has_citations", bool(chunks))
            root.set_status(Status(StatusCode.OK))
            return assistant._finalize(completion, chunks)
        except Exception as exc:
            root.record_exception(exc)              # errored traces are ALWAYS kept
            root.set_status(Status(StatusCode.ERROR, str(type(exc).__name__)))
            raise
```

### The LLM call span with GenAI conventions and cost

```python
# src/musaid/observability/tracing.py  (continued)
COST_PER_1K = {"input": 0.0025, "output": 0.010}   # SAR per 1k tokens (example tier)


def _traced_llm_call(llm, messages):
    with tracer.start_as_current_span("llm.chat") as s:
        s.set_attribute("gen_ai.system", llm.system)            # e.g. "anthropic"
        s.set_attribute("gen_ai.request.model", llm.model_name)
        s.set_attribute("gen_ai.request.temperature", llm.temperature)
        s.set_attribute("gen_ai.operation.name", "chat")

        completion = llm.chat(messages)             # provider call

        usage = completion.usage
        s.set_attribute("gen_ai.usage.input_tokens", usage.input_tokens)
        s.set_attribute("gen_ai.usage.output_tokens", usage.output_tokens)
        s.set_attribute("gen_ai.response.model", completion.model_version)
        s.set_attribute("gen_ai.response.finish_reason", completion.finish_reason)

        cost = (usage.input_tokens / 1000 * COST_PER_1K["input"]
                + usage.output_tokens / 1000 * COST_PER_1K["output"])
        s.set_attribute("musaid.cost.sar", round(cost, 5))
        # DO NOT set completion.text as a metric label; it lives on the span payload,
        # redacted, and is sampled — never in Prometheus.
        return completion
```

### Wiring exporters: Langfuse + OTel Collector

```python
# src/musaid/observability/setup.py
"""Configure ONE tracer provider with two span processors."""
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.sampling import ParentBasedTraceIdRatio
from langfuse.opentelemetry import LangfuseSpanProcessor   # LLM-native view


def configure_tracing(settings) -> None:
    # Head sample normal traffic at 10%; a tail processor (below) force-keeps
    # errored / low-quality traces regardless of this ratio.
    provider = TracerProvider(sampler=ParentBasedTraceIdRatio(0.10))
    provider.add_span_processor(KeepImportantTraces())          # tail rule: errors, low scores
    provider.add_span_processor(BatchSpanProcessor(
        OTLPSpanExporter(endpoint=settings.otel_collector_endpoint)))
    provider.add_span_processor(LangfuseSpanProcessor(
        public_key=settings.langfuse_public_key,
        secret_key=settings.langfuse_secret_key.get_secret_value()))
    trace.set_tracer_provider(provider)
```

### Trace-correlated structured logging

```python
# src/musaid/observability/logging_setup.py
"""JSON logs to stdout, bound to the active trace/span so Grafana can pivot
trace <-> logs. PII is masked; raw answers never logged at INFO."""
import structlog
from opentelemetry import trace

FORBIDDEN = {"national_id", "card_number", "phone", "full_name", "authorization"}


def _bind_trace(logger, method, event):
    ctx = trace.get_current_span().get_span_context()
    if ctx.is_valid:
        event["trace_id"] = format(ctx.trace_id, "032x")
        event["span_id"] = format(ctx.span_id, "016x")
    for k in list(event):
        if k.lower() in FORBIDDEN:
            event[k] = "***MASKED***"
    return event


def configure_logging(level="INFO"):
    structlog.configure(processors=[
        _bind_trace,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.JSONRenderer(),
    ])
```

## Hands-on Lab 2 — Instrument the Musaid Request Path

| | |
|---|---|
| **Objective** | Add OpenTelemetry tracing to the full RAG+tools path, export to Langfuse and the OTel Collector, capture tokens/cost/versions, correlate logs, and configure sampling that keeps every errored trace |
| **Duration** | 2 × 50 min (Day 1 H5 + Day 2 H1) |
| **Setup** | Lab 1 solution, `git checkout lab2-start`, `make up-observability` (adds Langfuse + OTel Collector + Prometheus + Loki + Grafana), `pip install opentelemetry-sdk langfuse structlog` |

**Part A tasks (50 min)**
1. Configure the tracer provider with both exporters; confirm one manual span appears in Langfuse (10 min).
2. Wrap `answer()` with the `ask` root span and child spans for `retrieve`, `build_prompt`, `llm.chat`, and any tool call (20 min).
3. Add GenAI-convention attributes + `musaid.cost.sar` on the LLM span; add prompt/model version tags (10 min).
4. Generate 100 requests; open one trace in Langfuse and confirm the full span tree with tokens and cost (10 min).

**Part B tasks (50 min)**
1. Add trace-correlated structured logging; pivot from a slow trace to its log lines in Grafana (15 min).
2. Configure sampling: 10% head sample but 100% of errored/low-score traces; prove it by injecting a 5% error and confirming all errors are kept (15 min).
3. Redaction drill: send a query containing a fake national id; confirm it is masked in logs and redacted on the span payload (10 min).
4. Commit `feat(obs): distributed tracing + cost/version tags + correlated logs` (10 min).

**Expected outputs**
```
Langfuse trace view: ask → retrieve(41ms) → build_prompt(3ms) → llm.chat(512ms, 1,180 tok, 0.0121 SAR, model=v3)
Injected 5% errors over 200 requests → 10/10 error traces retained (sampling kept 100%)
Redaction: query "my id is 1234567890" logged as "my id is ***MASKED***"
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Spans in Langfuse but not Tempo | Only one processor registered | Add the OTLP `BatchSpanProcessor` too; instrument once, export twice |
| Cost always 0 | Token usage not read from completion | Confirm mock-LLM returns usage; map input/output tokens explicitly |
| Prometheus cardinality warning | Query string used as a metric label | Move high-cardinality values to span attributes/logs only |
| Child spans detached from root | Not using `start_as_current_span` | Use current-span context so nesting propagates |
| Duplicate token counts | Hand-rolled Langfuse call + OTel span both firing | Remove the manual call; one instrumentation layer |

**Instructor notes.** The highest-value teachable moment is the sampling design: let one pair configure naive 10% uniform sampling, then show them the bad trace they most needed got dropped. Reuse Lab 2 traces as the input corpus for Lab 3's online evaluation — do not regenerate.

## Mini Exercises

**Quiz.** (1) Why export to both Langfuse and an OTel backend? (2) Which GenAI attribute catches a silent provider model swap? → `gen_ai.response.model`. (3) Name two values that must never be a Prometheus label. (4) What sampling rule protects debuggability? → always keep errored/low-quality traces. (5) Where does the full answer text live, and who can read it? → restricted store keyed by trace id, access-controlled, retention-limited.

**Debugging exercise.** Branch `sim-detached-spans`: retrieval and LLM spans appear as separate root traces instead of children. Participants diagnose the missing current-context propagation and fix nesting.

**Code-review exercise.** Review a PR that logs the full user query and answer at INFO, adds `query` as a metric label, and captures cost only on success. Three findings with PDPL and cardinality reasoning.

**Discussion.** Retention: how long may you keep raw prompts/answers for debugging under PDPL, and how do you reconcile that with the need to build eval datasets (M5)? Design the tiered-retention policy.

## Case Study — The Empty-Context Hallucination

**Scenario.** Musaid begins occasionally inventing a non-existent "unified services card" for certain Arabic queries about ID renewal. Complaints are sporadic and unreproducible on demand.

**Business context.** The invented procedure sends citizens to service centres for a document that does not exist. Leadership needs root cause within a day, and evidence for a fix, not a guess.

**Technical challenge.** With tracing now in place, an engineer filters Langfuse for the affected intent and low citation counts and finds the pattern in minutes: for a specific Arabic phrasing, the retriever returns **zero chunks** (a tokenisation/normalisation gap), so the prompt is built with empty context and the model free-associates.

**Constraints.** The fix must be validated without exposing raw citizen queries broadly; the root-cause evidence must be an auditable trace, not an anecdote.

**Solution approach.** The trace tree is the smoking gun: `retrieve` span shows `n_chunks=0` and `top_score=0.0` while `llm.chat` still produced a confident answer. Immediate mitigation: a guardrail that forces an "I don't have that information" response when `n_chunks=0` (a policy on the retrieval span). Durable fix: Arabic normalisation in the retriever, validated by re-running the affected traces. The whole investigation is possible only because §1's span tree captured retrieval scores and counts.

**Discussion questions.** (1) Which span attribute made the root cause obvious? (2) Why is "no context → refuse" a better default than trusting the model? (3) How would you alert on `n_chunks=0` rate proactively (foreshadows M3/M6)? (4) What is the auditable artefact you hand the review board?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Span coverage of request path | Observability | 100% of hops have a span | trace inspection |
| Version tags present | Observability | model+prompt version on 100% of traces | Langfuse filter |
| Cost captured per request | Cost | `musaid.cost.sar` on 100% of LLM spans | metric completeness |
| Errored-trace retention | Reliability | 100% kept under sampling | fault-injection check |
| Log↔trace correlation | Operability | 100% of logs carry trace_id | Grafana pivot |
| PII in traces/logs | Compliance | 0 against forbidden-field list | redaction drill |

**Example benchmark table:**

| Configuration | Traces w/ full tree | Cost captured | Errors kept | Trace overhead p99 |
|---|---|---|---|---|
| Lab 1 (none) | 0% | 0% | n/a | 0 ms |
| Lab 2 solution | 100% | 100% | 100% | +4 ms |

## Required Visuals and Training Assets

### Diagrams
1. **Musaid span tree** — *Purpose:* the mental model of a trace. *Elements:* the `ask` root with `retrieve`/`build_prompt`/`llm.chat`/`tool`/`llm.chat` children, each annotated with its key attributes and timing. *Style:* horizontal waterfall + attribute callouts.
2. **Instrument once, export twice** — *Elements:* one OTel SDK feeding Langfuse (LLM view) and the Collector→Tempo/Prometheus/Loki (platform view). *Style:* fan-out diagram.
3. **GenAI semantic-convention cheat sheet** — *Elements:* the `gen_ai.*` attribute table plus the Musaid custom extensions. *Style:* printable reference card.
4. **Sampling decision tree** — *Elements:* is it errored? low quality? flagged? → keep 100%; else head-sample 10%; metrics always 100%. *Style:* compact flowchart.

### Images
1. **Langfuse trace view screenshot** — *why:* target output of Lab 2; *content:* span tree with token/cost/version.
2. **Grafana trace↔logs pivot** — *why:* correlation payoff; *content:* a trace linked to its Loki log lines by trace id.
3. **Masked-PII log line** — *why:* proof of redaction; *content:* national id shown as `***MASKED***`.

### Simulations
1. **Detached-spans** — *Setup:* broken context propagation. *Expected:* orphan traces. *Objective:* nesting/context discipline.
2. **Cardinality explosion** — *Setup:* query string added as a metric label under load. *Expected:* Prometheus memory spike. *Objective:* labels vs span attributes.

### Interactive Activities
- **"Span or label?" sort (10 min):** 14 fields sorted into span-attribute / metric-label / never-capture lanes.
- **Trace-reading race (12 min):** given 5 Langfuse traces, teams find which one hallucinated and cite the attribute proving it.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `lab2_traces/` | Generated by Lab 2 instrumentation | OTLP/Langfuse export | ~300 traces | Input corpus for Lab 3 eval |
| `pii_probe_queries.jsonl` | Course-authored queries containing fake PII | JSONL | 20 | Redaction drill |

### Demo Requirements
- **Instructor demo:** open a hallucination trace live and read the root cause off the `retrieve` span in under 2 minutes.
- **Student demo:** one pair pivots trace→logs→trace in Grafana.
- **Expected outputs:** fully traced path, cost/version tags, correlated logs, sampling that keeps every error.

---

# Module 3 — Online Evaluation and Quality Monitoring

## Module Overview

**Purpose.** Traces tell you *what happened*; evaluation tells you whether it was *good*. This module teaches participants to score live Musaid traffic without ground-truth labels — reference-free evaluators, LLM-as-judge, RAG faithfulness and relevance, safety and format checks — running asynchronously on sampled traces, aggregating scores into the fourth pillar, and detecting quality drift before users do.

**Business relevance.** For a citizen-services assistant, "is it up" is table stakes; "is it *correct and grounded*" is the actual product. Offline evaluation on a static set cannot see tomorrow's questions or a silent provider regression. Online evaluation is the only mechanism that continuously answers "is Musaid still good, right now, on real traffic" — the signal leadership and auditors actually care about, and the trigger for every safe-rollout and incident decision later in the course.

**Industry use cases.**
- A support assistant that samples 5% of answers through a faithfulness judge and pages when groundedness drops on a specific product line.
- A bank copilot with a hard safety evaluator on 100% of outputs (block-worthy content) plus a sampled quality judge for tone and correctness.
- A multilingual assistant where Arabic and English answers are evaluated separately because quality can regress in one language only.

**Expected competencies.** Participants can choose evaluator types per requirement, implement an async online-eval worker that scores sampled traces, build reference-free and LLM-as-judge evaluators with calibration against human labels, attach scores to traces, aggregate them as time series, and monitor for quality drift and segment regressions.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Select evaluator types (deterministic, model-graded, human) per quality dimension | LO2 |
| 3.2 | Implement an async online-eval worker scoring sampled live traces | LO2, LO6 |
| 3.3 | Build RAG faithfulness/relevance and LLM-as-judge evaluators with calibration | LO2 |
| 3.4 | Attach scores to traces and aggregate them into quality time series | LO2, LO5 |
| 3.5 | Detect quality drift and per-segment regressions | LO2, LO5 |

## Technical Content

### 1. Offline vs online evaluation

Offline evaluation runs a fixed dataset through the system in CI or pre-release: reproducible, cheap, great for regression gating (used in M4 rollouts). Online evaluation scores *actual production traffic* continuously: it sees real distributions, novel questions, and silent regressions, but has no ground-truth labels and costs money/latency to run. You need both — offline as a gate, online as the living signal. This module builds online; M4 uses offline for rollout gating.

The core online-eval constraint: **no reference answer exists.** You cannot compute exact-match against a label because there is no label for "how do I renew my Iqama if I'm abroad" asked at 2am. So online evaluators are either **reference-free** (judge the answer against its own retrieved context and policy) or **model-graded** (an LLM judges the answer).

### 2. The evaluator taxonomy

| Evaluator type | How it works | Cost/latency | Best for |
|---|---|---|---|
| Deterministic/heuristic | Rules, regex, schema checks, `has_citations`, length, language-match | ~free, instant | Format, refusal, language, PII-leak, obvious failures |
| Statistical | Embedding similarity (answer↔context), toxicity classifier score | cheap | Relevance, safety pre-screen |
| Model-graded (LLM-as-judge) | A strong LLM scores faithfulness/relevance/helpfulness with a rubric | expensive, slow | Nuanced quality, faithfulness, tone |
| Human | Annotators label a small sample | slowest, gold | Calibration, ground truth for the flywheel (M5) |

Design principle: **run cheap evaluators on everything, expensive ones on a sample.** Deterministic safety/format/language checks run on 100% of traffic (they are fast and catch hard failures); LLM-as-judge faithfulness runs on a 5–10% sample plus 100% of already-flagged traces. Human labels are reserved for calibrating the judges and building datasets.

### 3. RAG-specific evaluators

Because Musaid is RAG-based, the highest-value evaluators score the retrieval-generation relationship (the RAGAS-style metric family):

- **Faithfulness / groundedness:** is every claim in the answer supported by the retrieved context? Low faithfulness = hallucination. Computed by an LLM judge decomposing the answer into claims and checking each against context.
- **Answer relevance:** does the answer address the question (independent of correctness)?
- **Context relevance / precision:** were the retrieved chunks actually relevant to the question? Catches retrieval failures (the M2 empty-context case).
- **Citation validity:** do cited sources actually support the answer?

These four, sampled continuously and trended, are the heart of Musaid's quality pillar. A faithfulness drop with flat context-relevance points at the model/prompt; a context-relevance drop points at retrieval.

### 4. LLM-as-judge: making it trustworthy

A judge LLM is itself non-deterministic, so treat it as a measurement instrument that must be **calibrated and controlled**:

- **Rubric prompts:** give the judge a specific rubric and a discrete scale (e.g., 1–5 or pass/fail with reasons), not "rate this 0–1". Ask for a reason before the score (chain-of-thought improves reliability).
- **Reference-guided where possible:** for sampled traffic that overlaps the gold set, provide the reference; for novel traffic, judge against retrieved context only.
- **Calibration:** periodically have humans label a sample the judge also scored; measure agreement (Cohen's kappa / correlation). If the judge disagrees with humans, fix the rubric before trusting the trend. A judge you have not calibrated is decoration.
- **Bias controls:** position bias, verbosity bias (judges favour longer answers), self-preference (a model judging its own family). Randomise, cap length in the rubric, and prefer a different model family as judge where feasible.
- **Cost control:** the judge is an LLM call per evaluated trace — sample, cache by answer hash, and use a smaller judge model where calibration allows.

### 5. The online-eval worker

Evaluation must not sit in the user's request path — it adds latency and cost and can fail. Run it **asynchronously**: the request emits its trace; a separate worker consumes sampled traces from a queue, runs the evaluators, and writes scores back onto the trace (Langfuse scores) and as metrics (Prometheus) for dashboards and alerts. This decoupling means eval can be slow, retried, and versioned without touching serving latency.

Scores become the fourth pillar: aggregated as time series (mean faithfulness/hour, refusal rate, safety-fail count), segmented by language, intent, prompt version, and model version — so you can see "faithfulness dropped only for Arabic ID-renewal on prompt v2".

### 6. Quality drift and alert-worthy signals

Quality monitoring is drift detection on scores:

- **Trend break:** faithfulness rolling mean drops below a threshold or shifts >Nσ from baseline.
- **Segment regression:** a metric fine overall but collapsing in one language/intent/version — averages hide these; always segment.
- **Distribution shift on inputs:** a surge of a new intent the system was not evaluated for (ties to M5's dataset gaps).

Common mistakes: trusting an uncalibrated judge; averaging across segments and missing a localized regression; running expensive eval synchronously in the request path; evaluating only English while Arabic silently degrades; treating a single low score as an incident instead of trending; and having no cheap deterministic layer so obvious failures burn judge budget.

## Code Examples

### Deterministic evaluators (run on 100% of traffic)

```python
# src/musaid/eval/deterministic.py
"""Cheap, fast, run on every answer. Catch hard failures before spending
judge budget. Each returns a score in [0,1] and a reason."""
from dataclasses import dataclass


@dataclass
class Score:
    name: str
    value: float
    reason: str


def language_match(answer_text: str, expected_lang: str) -> Score:
    detected = detect_lang(answer_text)
    ok = detected == expected_lang
    return Score("language_match", 1.0 if ok else 0.0,
                 f"expected {expected_lang}, got {detected}")


def grounded_or_refused(answer_text: str, n_chunks: int) -> Score:
    """The M2 lesson as a guardrail evaluator: if no context was retrieved,
    the answer MUST be a refusal, not a confident fabrication."""
    refused = is_refusal(answer_text)
    if n_chunks == 0 and not refused:
        return Score("grounded_or_refused", 0.0, "answered with empty context")
    return Score("grounded_or_refused", 1.0, "ok")


def pii_leak(answer_text: str) -> Score:
    hits = find_pii(answer_text)          # national id, card, phone patterns
    return Score("pii_leak", 0.0 if hits else 1.0,
                 f"leaked: {hits}" if hits else "clean")
```

### LLM-as-judge faithfulness (sampled)

```python
# src/musaid/eval/judge.py
"""Reference-free faithfulness: does the answer's every claim follow from the
retrieved context? Rubric + reason-before-score + discrete scale."""
import json

FAITHFULNESS_RUBRIC = """You are a strict evaluator of a government-services
assistant. Given the CONTEXT and the ANSWER, decide whether every factual claim
in the ANSWER is supported by the CONTEXT.

Return JSON: {"reason": "<one sentence>", "unsupported_claims": <int>,
"verdict": "faithful" | "partially_faithful" | "unfaithful"}.
Judge ONLY grounding, not style. Do not reward longer answers."""


def score_faithfulness(judge_llm, context: str, answer: str) -> dict:
    resp = judge_llm.chat([
        {"role": "system", "content": FAITHFULNESS_RUBRIC},
        {"role": "user", "content": f"CONTEXT:\n{context}\n\nANSWER:\n{answer}"},
    ], temperature=0.0)                    # judge is deterministic-ish
    out = json.loads(resp.text)
    value = {"faithful": 1.0, "partially_faithful": 0.5, "unfaithful": 0.0}[out["verdict"]]
    return {"name": "faithfulness", "value": value,
            "reason": out["reason"], "unsupported_claims": out["unsupported_claims"]}
```

### The async online-eval worker

```python
# src/musaid/eval/worker.py
"""Runs OUTSIDE the request path. Consumes sampled traces, evaluates,
writes scores back to Langfuse and Prometheus. Never adds serving latency."""
from prometheus_client import Histogram, Counter
from musaid.eval import deterministic as det
from musaid.eval.judge import score_faithfulness

FAITHFULNESS = Histogram("musaid_faithfulness", "faithfulness score",
                         labelnames=["lang", "intent", "prompt_version"])
SAFETY_FAIL = Counter("musaid_safety_fail_total", "hard safety failures",
                      labelnames=["lang", "intent"])


def evaluate_trace(trace, langfuse, judge_llm, sample_rate=0.10):
    ctx, answer = trace.context_text, trace.answer_text
    lang, intent, pv = trace.lang, trace.intent, trace.prompt_version

    # 1) deterministic layer on 100%
    for s in (det.language_match(answer, lang),
              det.grounded_or_refused(answer, trace.n_chunks),
              det.pii_leak(answer)):
        langfuse.score(trace_id=trace.id, name=s.name, value=s.value, comment=s.reason)
        if s.name == "pii_leak" and s.value == 0.0:
            SAFETY_FAIL.labels(lang, intent).inc()

    # 2) expensive judge on a sample OR if already flagged
    if trace.sampled(sample_rate) or trace.flagged:
        f = score_faithfulness(judge_llm, ctx, answer)
        langfuse.score(trace_id=trace.id, name="faithfulness",
                       value=f["value"], comment=f["reason"])
        FAITHFULNESS.labels(lang, intent, pv).observe(f["value"])
```

## Hands-on Lab 3 — Score Live Traffic

| | |
|---|---|
| **Objective** | Build the async online-eval worker: deterministic checks on 100% of Lab-2 traces plus sampled LLM-as-judge faithfulness; attach scores to traces; add a quality tile to Grafana; calibrate the judge against a small human-labelled set |
| **Duration** | 50 minutes |
| **Setup** | Lab 2 traces available, `git checkout lab3-start`, `pip install prometheus-client`, judge model in mock or real mode |

**Instructions & tasks**
1. *(10 min)* Implement the three deterministic evaluators; run over Lab-2 traces; confirm scores appear on traces in Langfuse.
2. *(15 min)* Implement `score_faithfulness` and wire the worker to sample 10% + all flagged; run over the corpus.
3. *(10 min)* Aggregate: expose `musaid_faithfulness` and `musaid_safety_fail_total`; build a Grafana panel of mean faithfulness by language.
4. *(10 min)* Calibrate: score the 30-item `human_labels.jsonl` with the judge; compute agreement; if kappa < 0.6, tighten the rubric and re-run.
5. *(5 min)* Commit `feat(eval): online eval worker + quality dashboard + judge calibration`.

**Expected outputs**
```
Deterministic scores on 300/300 traces. Judge scored 41 sampled + 8 flagged = 49.
Grafana: mean faithfulness  EN 0.94 | AR 0.88  (AR gap flagged for M4)
Judge calibration vs humans: Cohen's kappa 0.71 (acceptable)
Safety fails: 0
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Judge returns non-JSON | Rubric not strict on format | Enforce JSON, temperature 0, add a parse-retry |
| Faithfulness looks inflated | Verbosity bias / self-preference | Cap length in rubric; use different judge family; recalibrate |
| Eval adds serving latency | Worker running in request path | Move to async consumer; serving emits, worker scores |
| AR scores missing | Judge rubric English-only | Judge must handle Arabic context; test both languages |
| kappa low | Vague rubric | Add examples and a discrete scale; re-measure |

**Instructor notes.** The calibration step is what separates real LLMOps from theatre — do not let a pair trust a judge they have not measured against humans. The EN/AR faithfulness gap is a deliberate plant; it becomes the motivation for the prompt fix and shadow rollout in Lab 4.

## Mini Exercises

**Quiz.** (1) Why can't online eval use exact-match against labels? (2) Which two RAG evaluators separate a model problem from a retrieval problem? → faithfulness vs context-relevance. (3) Name two LLM-judge biases and a control for each. (4) Why run deterministic evaluators on 100% but the judge on a sample? (5) What makes a judge trustworthy? → calibration against human labels.

**Debugging exercise.** Overall faithfulness is 0.93 and steady, yet complaints rise. Branch `sim-segment-regression`: Arabic appointment-booking answers sit at 0.71. Participants must find it by segmenting — the lesson that averages hide regressions.

**Code-review exercise.** Review a PR that runs the judge synchronously in `answer()`, scores 100% with the expensive model, and uses a "rate 0-1" rubric. Three findings: latency/cost/decoupling, sampling, rubric rigor.

**Discussion.** Who owns the quality thresholds — where does "faithfulness must stay ≥ 0.90 for ID-renewal" come from, and what happens operationally when it breaches (ties to M6 SLOs)?

## Case Study — The Arabic Faithfulness Gap

**Scenario.** Musaid's overall quality dashboard is healthy, but the online-eval worker's segmented view shows Arabic faithfulness for ID-renewal at 0.79 vs 0.94 for English — a gap invisible in the aggregate.

**Business context.** Arabic is the primary language of most citizens; a quality gap in Arabic is a gap for the majority of real users, and a reputational risk for a national platform.

**Technical challenge.** Localise the cause: is it retrieval (Arabic chunks poorly matched), the prompt (English-centric instructions), or the model (weaker Arabic grounding)? Segmented scores plus traces make this tractable.

**Constraints.** The fix must be validated before promotion (no risky live change), and evaluation of Arabic content must respect PDPL.

**Solution approach.** Segmentation (M3) localises it to the prompt: the Arabic answers drift stylistically and add unsupported reassurance. Context-relevance is healthy (retrieval is fine), pointing at prompt/model. This hands off directly to M4: author a prompt v2 with stricter Arabic grounding instructions, shadow-test it against the same traffic, and compare faithfulness before promoting.

**Discussion questions.** (1) Which evaluator ruled out retrieval? (2) Why is segmentation the whole game here? (3) How do you set a per-segment quality bar without gaming? (4) What is the rollout gate that must pass before v2 ships (foreshadows M4)?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Deterministic coverage | Quality | 100% of traffic | worker logs |
| Judge sample rate | Quality/Cost | 5–10% + 100% flagged | worker config |
| Judge–human agreement | Quality | Cohen's kappa ≥ 0.6 | calibration set |
| Segmented quality panels | Observability | by lang/intent/version | Grafana |
| Eval added serving latency | Performance | 0 ms (async) | request-path timing |
| Safety-fail detection | Safety | 100% of hard failures caught | deterministic layer |

**Example benchmark table:**

| Segment | Faithfulness | Refusal-appropriate | Safety fails |
|---|---|---|---|
| EN / ID-renewal | 0.94 | 0.97 | 0 |
| AR / ID-renewal | 0.79 → (M4 target ≥ 0.90) | 0.88 | 0 |
| AR / appointments | 0.90 | 0.95 | 0 |

## Required Visuals and Training Assets

### Diagrams
1. **Evaluator taxonomy pyramid** — *Elements:* deterministic (100%) → statistical → LLM-judge (sampled) → human (calibration), width = volume, height = cost. *Style:* pyramid.
2. **RAG evaluator map** — *Elements:* question/context/answer triangle with faithfulness, answer-relevance, context-relevance, citation-validity as edges; which cause each isolates. *Style:* triangle diagram.
3. **Async eval architecture** — *Elements:* request path emits trace → queue → eval worker → scores back to Langfuse + Prometheus → Grafana; serving latency untouched. *Style:* flow with a clear async boundary.
4. **Judge calibration loop** — *Elements:* judge scores + human labels → agreement metric → rubric fix → re-measure. *Style:* loop.

### Images
1. **Segmented quality dashboard** — *why:* the segmentation lesson; *content:* EN vs AR faithfulness panels with the gap visible.
2. **Langfuse score attached to a trace** — *why:* target output; *content:* a faithfulness score + reason on a generation.
3. **Calibration scatter** — *why:* trust the judge; *content:* judge vs human scores with kappa.

### Simulations
1. **Segment-regression** — *Setup:* Arabic ID-renewal degraded. *Expected:* aggregate healthy, segment red. *Objective:* always segment.
2. **Uncalibrated-judge** — *Setup:* judge with verbosity bias. *Expected:* inflated scores vs humans. *Objective:* calibrate before trusting.

### Interactive Activities
- **Write-the-rubric (15 min):** teams draft a faithfulness rubric, swap, and try to "game" each other's with a verbose ungrounded answer; harden.
- **Segment hunt (10 min):** given a healthy aggregate, teams find the hidden regressed segment fastest.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `human_labels.jsonl` | Instructor-labelled sample of Lab-2 answers | JSONL | 30 | Judge calibration |
| `eval_gold_v1.jsonl` | From M1 | JSONL | 150 | Reference-guided judging |

### Demo Requirements
- **Instructor demo:** run the judge live on two answers (one grounded, one hallucinated) and show the scores + reasons; then reveal the calibration kappa.
- **Student demo:** one pair presents their segmented dashboard and the AR gap.
- **Expected outputs:** online-eval worker scoring traffic, calibrated judge, segmented quality dashboard.

---

# Module 4 — Prompt Registries and Version Management

## Module Overview

**Purpose.** In an LLM system the prompt is source code that ships changes to behaviour without a model retrain — and it is the most common cause of production regressions. This module treats prompts as versioned, governed artefacts: stored in a registry, linked to every trace and eval score, promoted through environments, and rolled out safely with shadow/canary comparisons and instant rollback.

**Business relevance.** A two-word prompt edit can degrade Arabic faithfulness (the M3 gap), leak an instruction, double latency, or change the assistant's willingness to refuse — with no code deploy and no model change. For a national platform, unversioned prompts editable by anyone are an audit and reliability liability. A prompt registry gives change control, attribution, and the ability to answer "which prompt produced this answer, who changed it, and did quality move".

**Industry use cases.**
- A support assistant where prompt changes go through review and canary like code, not a copy-paste into production.
- A bank copilot that must show auditors the exact prompt version behind any regulated response.
- A team A/B-testing two system prompts on live traffic, promoting the winner on measured faithfulness, not opinion.

**Expected competencies.** Participants can move prompts out of code into a registry, version and label them, link versions to traces and eval scores, gate promotion with offline eval, run shadow and canary rollouts comparing quality, and roll back instantly.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Externalise prompts into a versioned registry with labels and metadata | LO3 |
| 4.2 | Link prompt versions to traces and eval scores for attribution | LO3, LO1 |
| 4.3 | Gate prompt promotion with an offline eval regression suite | LO3, LO2 |
| 4.4 | Run shadow and canary rollouts comparing quality between versions | LO3 |
| 4.5 | Roll back a bad prompt/model version instantly and safely | LO3, LO4 |

## Technical Content

### 1. The prompt as a versioned artefact

A prompt hard-coded in Python has none of the properties production behaviour needs: no version, no author, no review, no link to the answers it produced, no way to roll back without a deploy. Treat it like the deployable it is:

- **Externalise** it from code into a registry (Langfuse prompt management, or a git-backed store) so changing it does not require a code release — but changing it is still governed.
- **Version** every change (immutable version numbers) with author, timestamp, and a changelog note.
- **Label** versions for environments: `production`, `staging`, `latest`. Code references a *label*, not a fixed version, so promotion is a label move, and rollback is moving the label back.
- **Parameterise** with typed variables (`{{query}}`, `{{context}}`, `{{lang}}`) so the template and the data stay separate and validatable.

The payoff: the prompt behind any answer is knowable and reversible, and prompt changes get the same discipline as code changes.

### 2. The prompt registry pattern

```
registry (Langfuse):
  prompt "citizen_assistant"
    ├── v1  (labels: —)          author: aisha  note: initial launch prompt
    ├── v2  (labels: staging)    author: omar   note: stricter Arabic grounding
    └── v3  (labels: production, latest) author: omar  note: v2 + refusal rule
```

At runtime Musaid fetches by label (`get_prompt("citizen_assistant", label="production")`), caches it with a short TTL, and tags every trace with the resolved version. The registry is the single source of truth; the app never contains prompt text. A background refresh picks up promotions without a redeploy, but a change to `production` is an audited, reviewed action — not an ad-hoc edit.

### 3. Linking prompts to traces and evaluation

The version tag from M2 (`musaid.prompt.version`) is what makes this module operational: every trace and every eval score (M3) carries the prompt version that produced it. That link enables:

- **Attribution:** "the faithfulness drop started exactly when v2 hit 20% of traffic".
- **Comparison:** aggregate eval scores *by prompt version* to compare v1 vs v2 on live traffic.
- **Regression detection:** a new version whose scores are worse is caught in the quality dashboard, segmented (the AR gap from M3 is diagnosed and fixed here).

Without the trace↔version link, prompt changes are unattributable and rollout is guesswork. With it, prompt management becomes measurable.

### 4. Offline eval as a promotion gate

Before a prompt version reaches live traffic at all, run it through an **offline regression suite** in CI: the gold set (`eval_gold_v1`) plus a growing set of past-incident cases (the empty-context query from M2, the Arabic ID-renewal cases from M3). The gate: the new version must not regress faithfulness/refusal on any segment beyond a tolerance, and must fix the case it claims to fix. This is the LLM analogue of a test suite — a prompt change with no offline eval is an unreviewed deploy to production behaviour.

### 5. Safe rollout: shadow and canary

Offline eval is necessary but not sufficient — live traffic differs. Two live-rollout patterns:

- **Shadow (mirror):** run the new version on a copy of live traffic *without serving its output to users*; evaluate both old and new offline-style on the same requests; compare. Zero user risk, real traffic. Ideal for prompts (cheap to double-run) — this is how the M3 Arabic fix is validated.
- **Canary:** serve the new version to a small % of real traffic (e.g., 5%), watch its segmented eval scores and latency/cost against the control, and ramp only if it holds — with automatic rollback on breach. Necessary when the change interacts with user behaviour (tone, follow-ups).

Model-version changes (provider or fine-tune) use the same machinery: pin the current model version, canary the new one, compare on the quality pillar, and keep the pin so a silent provider swap (M1) cannot bypass the gate.

### 6. Rollback and governance

- **Rollback is a label move:** `production → v2` reverts instantly, no deploy, no rebuild. Rehearse it; it is the fastest incident mitigation you have (M6).
- **Change control:** prompt edits go through review (a PR against the git-backed registry, or a registry approval workflow), with the offline gate required. No direct edits to the `production` label.
- **Audit:** who changed what prompt when, and the eval evidence for the promotion, is retained — the compliance record for a national service.

Common mistakes: prompts hard-coded and copy-pasted into prod; referencing a fixed version so promotions need deploys (or worse, referencing `latest` in production and getting surprise changes); promoting on vibes without eval; no shadow/canary so regressions hit 100% of users; no trace↔version link so nothing is attributable; and forgetting that a model swap needs the same rollout gate as a prompt.

## Code Examples

### Fetching prompts from the registry by label

```python
# src/musaid/service/prompts.py
"""Prompts live in the registry, never in code. Fetch by LABEL so promotion
is a label move and rollback is instant. Tag the resolved version on the trace."""
from functools import lru_cache
from opentelemetry import trace
from langfuse import Langfuse

lf = Langfuse()


def get_prompt(name: str, label: str = "production"):
    # short-TTL cache so promotions propagate within a minute, no redeploy
    prompt = lf.get_prompt(name, label=label, cache_ttl_seconds=60)
    span = trace.get_current_span()
    span.set_attribute("musaid.prompt.name", name)
    span.set_attribute("musaid.prompt.version", prompt.version)   # attribution!
    return prompt


def build_prompt(name, label, *, query, context, lang):
    prompt = get_prompt(name, label)
    return prompt.compile(query=query,
                          context="\n\n".join(c.text for c in context),
                          lang=lang)
```

### Offline eval promotion gate (CI)

```python
# tools/eval_gate.py
"""Runs in CI before a prompt version may be labelled 'staging'. Must not
regress any segment beyond tolerance and must fix its target case."""
import sys
from musaid.eval.judge import score_faithfulness

TOLERANCE = 0.02


def run_gate(candidate_version: str, gold_path: str, judge_llm) -> bool:
    gold = load_jsonl(gold_path)                 # includes past-incident cases
    baseline = load_scores("production")         # current prod version's scores
    regressions = []
    by_segment = {}
    for item in gold:
        answer = run_musaid(item["query"], prompt_version=candidate_version)
        f = score_faithfulness(judge_llm, item["context"], answer.text)
        by_segment.setdefault((item["lang"], item["intent"]), []).append(f["value"])

    for seg, scores in by_segment.items():
        new_mean = sum(scores) / len(scores)
        if new_mean < baseline[seg] - TOLERANCE:
            regressions.append((seg, baseline[seg], new_mean))

    if regressions:
        for seg, old, new in regressions:
            print(f"REGRESSION {seg}: {old:.3f} -> {new:.3f}")
        return False
    print(f"GATE PASSED for {candidate_version}")
    return True


if __name__ == "__main__":
    ok = run_gate(sys.argv[1], "eval_gold_v1.jsonl", get_judge())
    sys.exit(0 if ok else 1)                      # non-zero blocks promotion
```

### Shadow rollout comparing two versions on live traffic

```python
# src/musaid/rollout/shadow.py
"""Shadow: run candidate on mirrored live traffic WITHOUT serving it.
Evaluate both; compare by segment. Zero user risk."""
import asyncio
from musaid.eval.judge import score_faithfulness


async def handle_with_shadow(query, assistant, shadow_version, judge_llm, langfuse):
    # serve production to the user
    prod_answer = assistant.answer(query)                 # label="production"

    # shadow the candidate OUT OF BAND (not returned to user)
    async def run_shadow():
        cand = assistant.answer_with(query, prompt_label=shadow_version)
        f_prod = score_faithfulness(judge_llm, prod_answer.context, prod_answer.text)
        f_cand = score_faithfulness(judge_llm, cand.context, cand.text)
        langfuse.score(trace_id=prod_answer.trace_id, name="shadow_delta_faithfulness",
                       value=f_cand["value"] - f_prod["value"],
                       comment=f"{shadow_version} vs production")
    asyncio.create_task(run_shadow())                     # fire-and-forget
    return prod_answer                                     # user sees prod only
```

## Hands-on Lab 4 — Versioned Prompts and a Shadow Rollout

| | |
|---|---|
| **Objective** | Move Musaid's prompts into the registry, tag versions on traces, author a v2 fixing the M3 Arabic faithfulness gap, pass the offline eval gate, shadow-test v2 on live traffic, and promote it by label (with a rehearsed rollback) |
| **Duration** | 50 minutes |
| **Setup** | Lab 3 solution, `git checkout lab4-start`, Langfuse prompt management enabled |

**Instructions & tasks**
1. *(10 min)* Externalise the current prompt as `citizen_assistant` v1 in the registry; refactor code to `get_prompt(..., label="production")`; confirm `musaid.prompt.version` now tags traces.
2. *(10 min)* Author v2 with stricter Arabic grounding + explicit refusal-on-empty-context rule; save as a new version labelled `staging`.
3. *(10 min)* Run `tools/eval_gate.py v2` — it must fix the AR ID-renewal case and not regress EN; iterate the prompt until the gate passes.
4. *(10 min)* Shadow v2 on the live traffic generator; collect `shadow_delta_faithfulness`; confirm AR improves without EN regression.
5. *(5 min)* Promote: move the `production` label to v2; verify new traces carry v2. Then rehearse rollback: move `production` back to v1 and confirm instant revert.
6. *(5 min)* Commit `feat(prompts): registry + eval gate + shadow rollout of v2`.

**Expected outputs**
```
Gate: AR/ID-renewal 0.79 -> 0.91 (fixed), EN/ID-renewal 0.94 -> 0.94 (no regression). GATE PASSED
Shadow delta faithfulness (AR): +0.12 mean over 120 mirrored requests
Promote: production -> v2 (traces now tagged v2 within 60s, no redeploy)
Rollback drill: production -> v1 in <5s
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Promotion needs a redeploy | Code references a fixed version, not a label | Reference `label="production"`; cache with TTL |
| Traces still show v1 after promote | Cache TTL too long | Lower TTL; confirm background refresh |
| Gate passes but live regresses | Gold set unrepresentative | Add live-sampled and past-incident cases to gold |
| Shadow doubles user latency | Shadow run awaited in request path | Fire-and-forget; never block the user response |
| No attribution possible | Version tag missing on traces | Ensure `get_prompt` sets the span attribute |

**Instructor notes.** The label-move promotion and rollback is the "aha" of the module — do the rollback drill on the projector and time it; sub-five-seconds reversibility reframes how the room thinks about risk. The gate iterating until AR is fixed closes the loop opened in M3.

## Mini Exercises

**Quiz.** (1) Why reference a label, not a fixed version, in production? (2) What single tag links a regression to a prompt change? (3) Shadow vs canary — which serves the candidate to users? → canary. (4) What must the offline gate check beyond "did it improve"? → no regression on any segment. (5) How fast is prompt rollback and why? → instant, it's a label move, no deploy.

**Debugging exercise.** Branch `sim-latest-in-prod`: production references `latest`, so an untested edit reached 100% of users and dropped refusal rate. Participants diagnose the anti-pattern and switch to an approved label + gate.

**Code-review exercise.** Review a PR that hard-codes a "quick fix" prompt string in `answer()`, bypassing the registry "just for the incident". Findings: attribution loss, no rollback, no gate — and the correct fast path (label move).

**Discussion.** Prompt changes are behaviour changes with no code diff. Who reviews them, what evidence is required to promote, and how is the change audited for a national service?

## Case Study — The Two-Word Regression

**Scenario.** An engineer adds "be helpful and reassuring" to Musaid's system prompt to soften tone. Refusal-appropriateness drops from 0.96 to 0.82 over the next day: the assistant now reassures citizens with invented specifics rather than admitting uncertainty.

**Business context.** "Reassuring but wrong" is the worst failure for a services assistant — it maximises citizen trust in incorrect procedures. The change had no code review because it was "just a prompt".

**Technical challenge.** Detect, attribute, and revert fast; then prevent the class of change.

**Constraints.** The regression is subtle (quality, not errors); revert must not wait for a deploy; the fix must not re-break tone entirely.

**Solution approach.** The quality pillar (M3) flags the refusal-rate drop; the prompt-version tag (M4) attributes it to the exact version and author within minutes; rollback is a label move to the prior version (seconds). Prevention: route all prompt edits through the offline gate (which would have caught the refusal regression) and require review on the `production` label. A follow-up v-next tunes tone *and* passes the refusal gate via shadow.

**Discussion questions.** (1) Why did "just a prompt" bypass the safety net, and how do you close that? (2) Which signal detected it and which attributed it? (3) What is the fastest mitigation and why is it faster than a code rollback? (4) How do you keep the desired tone change without the refusal regression?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Prompts in registry (not code) | Governance | 100% | code grep for inline prompts |
| Trace↔version attribution | Observability | 100% of traces tagged | Langfuse filter |
| Promotion gate coverage | Quality | every version passes offline gate | CI logs |
| Rollback time | Reliability | < 60 s (label move) | rollback drill |
| Live rollout safety | Reliability | shadow/canary before 100% | rollout records |

**Example benchmark table:**

| Version | Gate result | Shadow AR faithfulness | Promoted | Rollback time |
|---|---|---|---|---|
| v1 | baseline | — | (initial) | — |
| v2 | passed | +0.12 vs v1 | yes | — |
| (drill) v1 | — | — | rollback | 4 s |

## Required Visuals and Training Assets

### Diagrams
1. **Prompt lifecycle** — *Elements:* author → offline gate → staging → shadow/canary → production label → (rollback arrow back). *Style:* pipeline with a prominent rollback loop.
2. **Registry + label model** — *Elements:* immutable versions with movable labels (production/staging/latest); code references labels. *Style:* version-stack diagram.
3. **Shadow vs canary** — *Elements:* shadow (mirrored, not served, both evaluated) vs canary (5% served, compared, auto-rollback). *Style:* two-panel.
4. **Attribution timeline** — *Elements:* eval score time series with a vertical marker at a promotion, showing the regression aligning to the version change. *Style:* annotated time series.

### Images
1. **Langfuse prompt versions screenshot** — *why:* target output; *content:* versions with labels, authors, notes.
2. **Eval-gate CI run** — *why:* gate-as-test; *content:* GATE PASSED / REGRESSION output.
3. **Rollback label move** — *why:* reversibility; *content:* production label moving back to v1.

### Simulations
1. **latest-in-prod** — *Setup:* production references `latest`. *Expected:* surprise regression at 100%. *Objective:* label discipline.
2. **ungated-promotion** — *Setup:* promote a version that regresses AR. *Expected:* dashboard catches it post-hoc. *Objective:* gate before promote.

### Interactive Activities
- **Promotion review board (12 min):** one pair presents evidence to promote v2; the rest act as change-approval board and decide.
- **Rollback race (8 min):** teams race to revert a bad prompt; fastest label-move wins.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `eval_gold_v1.jsonl` + incident cases | M1–M3 accumulated | JSONL | ~170 | Offline promotion gate |
| `prompt_versions/` | Course-authored v1/v2 templates | Jinja/text | 2 | Registry seeding |

### Demo Requirements
- **Instructor demo:** author v2, run the gate live, shadow it, promote by label, and roll back — end to end in under 8 minutes.
- **Student demo:** one pair shows their shadow delta and promotion decision.
- **Expected outputs:** registry-backed prompts, passing gate, shadow evidence, promoted v2 with rehearsed rollback.

---

# Module 5 — Feedback Loops and Data Flywheels

## Module Overview

**Purpose.** Production traffic is the best dataset an LLM service will ever have — if you capture it. This module teaches participants to turn live interactions and user reactions into a compounding asset: explicit and implicit feedback capture, routing low-quality traces to annotation queues, curating them into evaluation and fine-tuning datasets, and closing the loop back into prompt/model improvement — the data flywheel that makes Musaid better every week.

**Business relevance.** A national assistant that does not learn from its own traffic stagnates while user needs shift. The flywheel is how yesterday's failures become tomorrow's regression tests and improved answers, and how the eval gold set (M3/M4) grows to reflect real citizen questions rather than the launch team's guesses. Doing this under PDPL — capturing feedback and building datasets from personal data lawfully — is itself a core competency for Saudi operators.

**Industry use cases.**
- A support assistant whose thumbs-down answers auto-route to an annotation queue and become next month's eval cases.
- A bank copilot that mines implicit signals (user rephrased, abandoned, escalated to human) as negative feedback without asking.
- A team that grows its gold set weekly from curated production traces, so evaluation tracks reality.

**Expected competencies.** Participants can instrument explicit and implicit feedback, join it to traces, route low-score/negative traces to an annotation queue, curate PDPL-safe datasets, and design the flywheel that feeds M3 eval and M4 rollouts.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Capture explicit and implicit feedback and join it to traces | LO2, LO6 |
| 5.2 | Route low-quality/negative traces to an annotation queue | LO2, LO6 |
| 5.3 | Curate production traces into eval and training datasets, PDPL-safely | LO6 |
| 5.4 | Design the data flywheel feeding evaluation and rollout | LO6 |
| 5.5 | Measure feedback coverage and dataset growth as operational metrics | LO2, LO5 |

## Technical Content

### 1. Explicit vs implicit feedback

- **Explicit feedback** is what the user deliberately tells you: thumbs up/down, a star rating, a "report" button, a correction. High signal, low volume — most users never click. Design for it (a one-tap thumb on every answer) but never depend on it alone.
- **Implicit feedback** is inferred from behaviour: the user rephrased the same question (dissatisfaction), abandoned the session, copied the answer (satisfaction), followed a citation, or escalated to a human agent (failure). Lower signal-per-event but far higher volume — it covers the silent majority.

The design rule: **capture both, weight explicit higher, and never trust a single signal.** A thumbs-down plus a rephrase plus an escalation on the same trace is a strong negative; one ambiguous abandon is weak. Join every signal to its `trace_id` so feedback lands on the exact answer (and its prompt/model version) that caused it.

### 2. Instrumenting feedback

Feedback is a first-class score on the trace, exactly like an eval score (M3) — same store, same aggregation:

- The client sends `{trace_id, signal, value}` to a lightweight `/v1/feedback` endpoint; the service writes it as a Langfuse score (`user_feedback`) on that trace.
- Implicit signals are derived server-side: a session-level analyzer detects rephrases (high semantic similarity between consecutive queries), abandons (session ends after an answer with no follow-through), and escalations (handoff event), and writes them as scores too.
- Because feedback joins to the trace, it inherits all the trace's dimensions: you can now see thumbs-down *rate by intent, language, prompt version, and model version* — closing the loop to M4 attribution.

### 3. From feedback to annotation queue

Raw feedback is noisy; humans turn it into ground truth. The pipeline:

1. **Prioritise:** traces with negative feedback OR low eval scores (M3) OR both are candidates. Rank by impact (frequency of the intent × severity).
2. **Route to an annotation queue:** a review UI (Langfuse annotation queues) where a human sees the query, retrieved context, answer, and signals, and labels: correct/incorrect, the ideal answer, the failure category (hallucination / retrieval-miss / tone / refusal-wrong).
3. **Sample the good too:** queue a small share of positive/high-score traces so the dataset is not all-negative (evaluators and models need both classes).

Annotation is the human-in-the-loop that converts production noise into trustworthy labels — and those labels are what calibrate the judge (M3) and grow the gold set (M4).

### 4. Curating datasets — the flywheel's output

Annotated traces flow into versioned datasets, each with a purpose:

- **Evaluation datasets:** curated Q→ideal-answer+context cases that grow the gold set the M4 promotion gate runs against. Every fixed incident becomes a permanent regression test (the empty-context case, the AR gap, the two-word refusal regression).
- **Few-shot / prompt-improvement examples:** high-quality answers that seed better prompt instructions or in-context examples.
- **Fine-tuning datasets (optional):** if a component is fine-tuned (ties to SDA-AIE-215), curated preference pairs (good vs bad answer for the same query) feed preference optimisation.

Datasets are **versioned** (like prompts and models) so an eval result is reproducible against a known dataset version.

### 5. The data flywheel

```
   serve ──► traces (M2) ──► online eval scores (M3) ──┐
     ▲                                                 │
     │                          user + implicit feedback (M5)
     │                                                 ▼
   improved prompt/model  ◄── curated datasets ◄── annotation queue
   (M4 rollout, gated)         (eval + train)        (human labels)
```

Each turn of the wheel makes the next turn better: more traffic → more feedback → more labelled data → better eval + better prompts/models → better answers → more trust and traffic. The flywheel is the strategic reason LLMOps exists: it converts operation into improvement. The operational job is to keep every arc flowing and measured.

### 6. PDPL-safe feedback and data handling

User queries and answers are personal data. Building datasets from them lawfully:

- **Lawful basis and minimisation:** capture only what the purpose needs; separate the operational feedback (score + trace id) from the raw content, which stays access-controlled.
- **Redaction before dataset:** PII is stripped/pseudonymised when a trace is promoted into a shareable dataset; annotators see redacted content where possible.
- **Retention and consent:** raw content has a retention limit; datasets derived for eval are the durable artefact, not the raw logs. Respect deletion requests by keying content to identifiers you can purge.
- **Residency:** annotation and dataset storage stay within the sovereign boundary.

Common mistakes: relying on explicit feedback only (and concluding "users are happy" from silence); not joining feedback to traces (so it's unattributable); building an all-negative dataset; letting datasets rot un-versioned; skipping the human annotation step and training on noisy raw signals; and — the serious one — curating datasets from raw PII without redaction or lawful basis.

## Code Examples

### Feedback endpoint writing scores to traces

```python
# src/musaid/api/feedback.py
"""Feedback is a score on the trace — same store as eval scores.
The client sends the trace_id it received in the answer response headers."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from langfuse import Langfuse

router = APIRouter()
lf = Langfuse()


class Feedback(BaseModel):
    trace_id: str = Field(min_length=8)
    signal: str = Field(pattern="^(thumb_up|thumb_down|report|correction)$")
    correction_text: str | None = None       # optional user-provided ideal answer


@router.post("/v1/feedback")
def submit_feedback(fb: Feedback):
    value = {"thumb_up": 1.0, "thumb_down": 0.0,
             "report": 0.0, "correction": 0.0}[fb.signal]
    lf.score(trace_id=fb.trace_id, name="user_feedback",
             value=value, comment=fb.signal)
    if fb.correction_text:                     # gold candidate — redact before storing
        lf.score(trace_id=fb.trace_id, name="has_correction", value=1.0)
    return {"status": "recorded"}
```

### Deriving implicit feedback from sessions

```python
# src/musaid/feedback/implicit.py
"""Server-side signals for the silent majority. Written as scores too,
so implicit and explicit feedback aggregate together on the trace."""
from musaid.nlp import semantic_similarity


def analyze_session(session, langfuse):
    turns = session.turns                       # ordered (query, answer, trace_id)
    for i, turn in enumerate(turns):
        # rephrase: user re-asks a near-identical question next turn -> dissatisfaction
        if i + 1 < len(turns):
            sim = semantic_similarity(turn.query, turns[i + 1].query)
            if sim > 0.85:
                langfuse.score(trace_id=turn.trace_id, name="implicit_rephrase",
                               value=0.0, comment=f"sim={sim:.2f}")
        # escalation to a human agent after this answer -> strong negative
        if turn.followed_by_handoff:
            langfuse.score(trace_id=turn.trace_id, name="implicit_escalation",
                           value=0.0, comment="human handoff")
    # abandon: session ended right after an answer with no engagement
    if session.ended_after_answer and not session.any_positive_signal:
        langfuse.score(trace_id=turns[-1].trace_id, name="implicit_abandon",
                       value=0.0, comment="ended after answer")
```

### Routing to annotation and curating a dataset

```python
# tools/curate_dataset.py
"""Turn negative/low-score traces into annotation tasks, then curated,
REDACTED, versioned eval cases. PDPL: redact before the dataset."""
from musaid.privacy import redact_pii


def build_annotation_queue(langfuse, since, min_impact=5):
    traces = langfuse.get_traces(since=since)
    candidates = []
    for t in traces:
        neg = t.score("user_feedback", default=1.0) == 0.0
        low = t.score("faithfulness", default=1.0) < 0.7
        implicit = any(t.score(s, default=1.0) == 0.0
                       for s in ("implicit_rephrase", "implicit_escalation"))
        if neg or low or implicit:
            candidates.append((t, t.intent_frequency))
    # prioritise by impact; also sample 10% positives for balance
    candidates.sort(key=lambda c: c[1], reverse=True)
    for t, _ in candidates:
        langfuse.enqueue_annotation(trace_id=t.id, queue="quality_review")


def promote_to_eval_dataset(annotations, dataset="eval_gold", version="v2"):
    items = []
    for a in annotations:
        if a.label in ("incorrect", "corrected"):
            items.append({
                "query": redact_pii(a.query),            # PDPL: redact first
                "context": redact_pii(a.context),
                "ideal_answer": redact_pii(a.ideal_answer),
                "lang": a.lang, "intent": a.intent,
                "source_trace": a.trace_id, "failure_category": a.category,
            })
    save_versioned_dataset(dataset, version, items)        # immutable, versioned
    return len(items)
```

## Hands-on Lab 5 — Build the Flywheel

| | |
|---|---|
| **Objective** | Capture explicit + implicit feedback joined to traces, route low-score/negative traces to an annotation queue, annotate a batch, and export a redacted, versioned eval dataset that extends the M4 gold set |
| **Duration** | 50 minutes |
| **Setup** | Lab 4 solution, `git checkout lab5-start`, feedback-enabled traffic generator (simulates thumbs + rephrases + escalations) |

**Instructions & tasks**
1. *(10 min)* Implement `/v1/feedback`; run the feedback-enabled generator; confirm `user_feedback` scores land on the right traces and aggregate by intent.
2. *(10 min)* Implement two implicit signals (rephrase, escalation); verify they attach to traces and show a thumbs-down-rate-by-intent panel.
3. *(10 min)* Build the annotation queue from negative/low-score traces; annotate 10 items in the review UI (label + ideal answer + category).
4. *(10 min)* Export a redacted `eval_gold_v2` dataset; run a PII scan to prove no national ids/phones remain; confirm it is versioned.
5. *(5 min)* Close the loop: add one curated case to the M4 gate and show the gate now guards against that failure.
6. *(5 min)* Commit `feat(feedback): flywheel — feedback capture + annotation + curated eval set`.

**Expected outputs**
```
Feedback: 214 explicit (31 thumb_down) + 96 implicit signals joined to traces
Thumbs-down by intent: violations 14% (highest) -> prioritised for annotation
Annotated 10 -> eval_gold_v2 (+8 cases). PII scan: 0 leaks.
M4 gate now includes the 'violations fee' failure case
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Feedback not on trace | Client didn't return/echo trace_id | Return `X-Trace-Id`; client posts it back |
| Rephrase over-firing | Similarity threshold too low | Raise threshold; require same session |
| Queue all-negative | No positive sampling | Sample 10% positives for balance |
| PII in dataset | Redaction skipped on context | Redact query AND context AND ideal answer |
| Dataset not reproducible | Unversioned export | Version datasets immutably |

**Instructor notes.** The "silence is not satisfaction" point lands hardest when a pair sees implicit signals reveal dissatisfaction on an intent that had zero explicit thumbs-down. The loop-closing step (curated case → M4 gate) is the whole course in miniature — make sure every pair does it.

## Mini Exercises

**Quiz.** (1) Why never rely on explicit feedback alone? (2) Name two implicit negative signals. (3) What joins feedback to the prompt version that caused it? → trace_id. (4) Why sample positives into the annotation queue? (5) What must happen to a trace before it enters a shareable dataset? → PII redaction under PDPL.

**Debugging exercise.** Branch `sim-silence-bias`: explicit feedback shows 96% positive; implicit signals show 30% rephrase/escalation on one intent. Participants reconcile the contradiction and explain survivorship in explicit feedback.

**Code-review exercise.** Review a PR that builds a training set directly from raw traces (with PII), keyed by nothing, unversioned. Findings: PDPL redaction, lawful basis, versioning, deletion-support.

**Discussion.** Design the PDPL-compliant retention policy: how long do raw prompts live, when are they redacted into datasets, and how do you honour a citizen's deletion request across traces and datasets?

## Case Study — The Invisible Violations Problem

**Scenario.** Musaid's explicit feedback is 95% positive, yet the "traffic violations" intent has a 22% rephrase rate and frequent human escalations — users are quietly failing to get answers and giving up or escalating, without ever clicking thumbs-down.

**Business context.** Violations queries are high-volume and high-frustration; silent failure here drives call-centre load and citizen dissatisfaction that the happy explicit-feedback numbers completely mask.

**Technical challenge.** Surface the silent failure, find the cause, and feed it back into improvement.

**Constraints.** No new explicit signal will appear (users don't click); the fix must be validated (M4) and the data handled under PDPL.

**Solution approach.** Implicit signals (rephrase + escalation) expose the intent; annotation reveals the cause (retrieval returns outdated violation-fee documents); the curated cases become `eval_gold_v2` and the M4 gate; a knowledge refresh + prompt tweak is shadow-tested and promoted. The flywheel turned an invisible problem into a fixed, regression-tested capability.

**Discussion questions.** (1) Why did explicit feedback hide this? (2) Which implicit signal was most diagnostic? (3) How does this specific fix become permanent (regression-proof)? (4) What PDPL steps gate the raw traces before they became a dataset?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Feedback join rate | Feedback | 100% of feedback joined to a trace | score inspection |
| Implicit signal coverage | Feedback | ≥ 2 implicit signals live | session analyzer |
| Annotation throughput | Flywheel | ≥ 10 curated cases/session | queue export |
| Dataset PII leakage | Compliance | 0 in curated datasets | PII scan |
| Gold-set growth | Flywheel | eval set grows each cycle | dataset versions |

**Example benchmark table:**

| Signal | Volume | Reveals |
|---|---|---|
| Explicit thumbs-down | 31 / 300 | overt failures |
| Implicit rephrase | 42 / 300 | silent dissatisfaction |
| Implicit escalation | 18 / 300 | hard failures |
| Curated → eval_gold_v2 | +8 cases | permanent regression tests |

## Required Visuals and Training Assets

### Diagrams
1. **The data flywheel** — *Purpose:* strategic anchor. *Elements:* serve→trace→eval→feedback→annotation→dataset→improve, each arc labelled with its module. *Style:* circular, momentum arrows.
2. **Explicit vs implicit signal map** — *Elements:* signal types with volume vs signal-strength axes and how each maps to a score. *Style:* quadrant.
3. **Annotation pipeline** — *Elements:* prioritise → queue → human label → curate → versioned dataset, with a redaction gate. *Style:* pipeline with a PDPL gate icon.
4. **Feedback-on-trace** — *Elements:* one trace accumulating eval + explicit + implicit scores, inheriting prompt/model version. *Style:* trace with stacked scores.

### Images
1. **Thumbs-down-by-intent dashboard** — *why:* attribution; *content:* violations intent highest.
2. **Annotation UI** — *why:* the human-in-the-loop; *content:* query/context/answer/labels.
3. **PII scan clean report** — *why:* PDPL proof; *content:* 0 leaks on `eval_gold_v2`.

### Simulations
1. **silence-bias** — *Setup:* positive explicit, negative implicit. *Expected:* contradiction. *Objective:* silence ≠ satisfaction.
2. **all-negative-dataset** — *Setup:* queue only negatives. *Expected:* skewed evaluator. *Objective:* balance positives in.

### Interactive Activities
- **Signal design (12 min):** teams design three implicit signals for Musaid and rank them by reliability.
- **Annotate-a-batch (15 min):** pairs annotate 6 traces and reconcile disagreements — surfacing why calibration matters.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `feedback_traffic.jsonl` | Generator with simulated feedback | JSONL | 300 sessions | Lab 5 feedback |
| `eval_gold_v2.jsonl` | Curated in Lab 5 | JSONL | grows | Extends M4 gate |

### Demo Requirements
- **Instructor demo:** show implicit signals exposing a silent-failure intent the explicit numbers hid; curate one case into the gold set live.
- **Student demo:** one pair presents their `eval_gold_v2` growth and the loop-closing gate case.
- **Expected outputs:** feedback capture, annotation queue, redacted versioned dataset feeding M4.

---

# Module 6 — SLOs, Alerting, and Incident Response

## Module Overview

**Purpose.** Signals are useless unless they trigger the right action at the right time. This module teaches participants to define Service Level Indicators and Objectives for an LLM service — including the quality SLOs that only LLMOps has — compute error budgets, wire multi-window burn-rate alerts that page on real problems and stay quiet otherwise, and run AI-specific incidents with runbooks and blameless postmortems.

**Business relevance.** A national assistant needs a defensible answer to "how reliable is this, and who gets woken up when it isn't". SLOs turn vague reliability into a measurable contract; error budgets turn reliability into an engineering decision (ship vs stabilise); burn-rate alerts prevent both missed incidents and alert fatigue. AI-specific incidents — a hallucination spike, a provider outage, a prompt regression — need runbooks that ordinary APM playbooks do not cover.

**Industry use cases.**
- A services assistant with an availability SLO *and* a faithfulness SLO, each with its own error budget and alert.
- A bank copilot whose provider-outage runbook fails over to a backup model within the latency SLO.
- An on-call rotation that responds to a "hallucination-rate burn" alert with a defined mitigation ladder (rollback prompt, pin model, degrade to refuse).

**Expected competencies.** Participants can define SLIs/SLOs including quality, compute error budgets, implement multi-window multi-burn-rate alerts, build SLO dashboards, author AI-incident runbooks, and run and postmortem an incident.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Define SLIs and SLOs for an LLM service, including quality SLOs | LO5 |
| 6.2 | Compute error budgets and use them for ship/stabilise decisions | LO5, LO6 |
| 6.3 | Implement multi-window burn-rate alerts that avoid fatigue | LO5 |
| 6.4 | Build reliability dashboards for latency, cost, and quality | LO5 |
| 6.5 | Author runbooks and run/postmortem AI-specific incidents | LO4 |

## Technical Content

### 1. SLIs, SLOs, and error budgets for LLM services

- **SLI (indicator):** a measured ratio of good events to total, e.g., *proportion of requests answered in < 3s*, *proportion of answers with faithfulness ≥ 0.8*.
- **SLO (objective):** the target for an SLI over a window, e.g., *99% of requests < 3s over 30 days*; *95% of sampled answers faithfulness ≥ 0.8 over 7 days*.
- **Error budget:** `100% − SLO`. A 99% availability SLO grants a 1% budget — ~7.3 hours/30 days of "allowed" badness. The budget is a currency: spend it on shipping risk; when it's exhausted, freeze features and stabilise.

The LLMOps twist: alongside the classic **availability, latency, and error-rate** SLIs, you define **quality SLIs** built on the M3 eval scores — faithfulness, refusal-appropriateness, safety. This is the only operating model where "the service is up and fast but giving wrong answers" is a budget-burning SLO breach, not an invisible non-event.

### 2. Choosing Musaid's SLIs and SLOs

| SLI | Definition (good event) | Example SLO | Source |
|---|---|---|---|
| Availability | request returns a valid answer (not 5xx/timeout) | 99.5% / 30d | metrics (M2) |
| Latency | end-to-end < 3s (p95 target) | 95% < 3s / 30d | span timing (M2) |
| Faithfulness (quality) | sampled answer faithfulness ≥ 0.8 | 95% / 7d | eval scores (M3) |
| Safety | zero hard safety failures | 100% (any breach = incident) / 7d | deterministic eval (M3) |
| Cost | cost/request within budget band | 99% within band / 30d | cost metric (M2) |

Design principles: pick SLIs users actually feel; set SLOs from what the business needs, not 100% (perfection has no budget for change); measure quality SLOs on the *sampled, calibrated* eval stream, and be explicit that they are statistical. Safety is special — it is often a hard 100% with any breach paging immediately.

### 3. Burn-rate alerting without fatigue

Alerting naively on "SLI below SLO right now" either pages on every blip (fatigue) or too late (missed incident). The Google-SRE approach is **multi-window, multi-burn-rate**: alert on how fast you are *consuming the error budget*.

- **Burn rate** = how many times faster than sustainable you are spending budget. Burn rate 1 = you'll exactly exhaust the 30-day budget in 30 days; burn rate 14.4 = you'll exhaust it in ~2 days.
- **Fast-burn alert (page):** high burn (e.g., 14.4×) over a short window (1h) *and* a shorter window (5m) both breaching → a real, urgent problem. Pages the on-call.
- **Slow-burn alert (ticket):** moderate burn (e.g., 3×) over a long window (6h) → a chronic issue that needs attention but not at 3am. Creates a ticket.

The dual window (long + short) prevents flapping: the short window confirms the problem is still happening; the long window confirms it is significant. This is the difference between an alert system people trust and one they mute.

### 4. AI-specific incidents and runbooks

Classic runbooks cover "service down / latency high". LLM services add incident classes with their own mitigations:

| Incident | Detection | First mitigations (the ladder) |
|---|---|---|
| Hallucination/faithfulness burn | faithfulness SLO fast-burn | rollback prompt (M4 label move) → pin model version → degrade to stricter refusal → escalate |
| Provider outage / latency | availability/latency burn, provider 5xx | fail over to backup model/provider (M7) → shed load → status page |
| Cost blowout | cost SLO burn | cap max tokens → disable expensive path → alert owner |
| Prompt regression | quality burn aligned to a promotion | roll back prompt label (seconds) → open postmortem |
| Safety breach | any safety-eval fail | block output path → page security → preserve trace evidence |
| Retrieval failure | context-relevance drop, n_chunks=0 rate | refuse-on-empty guardrail → fix/rollback retriever |

A runbook per incident class states: how it's detected, the mitigation ladder (fastest-safest first), who to page, what evidence to preserve (the trace!), and the rollback lever. The fastest lever in the whole course is the M4 prompt label rollback — most quality incidents mitigate in seconds.

### 5. Dashboards and the on-call surface

The reliability dashboard is the on-call's home:

- **SLO panels:** current SLI vs SLO and remaining error budget (with burn-rate sparklines) for each SLO — availability, latency, faithfulness, safety, cost.
- **Golden signals:** request rate, error rate, latency percentiles, saturation.
- **LLM-specific:** token/cost trends, cache hit rate (M7), provider health, quality-by-segment (M3).
- **Drill-down:** every panel links to the traces behind it, so an alert leads to the exact bad examples in two clicks.

### 6. Blameless postmortems and the improvement loop

Every significant incident gets a blameless postmortem: timeline, impact, root cause, what detected it (and what should have detected it sooner), the mitigation, and durable action items — chief of which is *a regression test in the gold set* (M5) so the incident cannot silently recur. Postmortems feed the flywheel: the two-word-regression, the empty-context hallucination, and the Arabic gap all became permanent eval cases. This is the "optimize the operations lifecycle for continuous improvement" outcome made concrete.

Common mistakes: SLOs set to 100% (no budget for change); alerting on raw SLI not burn rate (fatigue or lateness); no quality SLO (the LLMOps blind spot); runbooks with no rollback lever; paging on non-actionable alerts; and postmortems that assign blame instead of producing a regression test.

## Code Examples

### Recording SLIs as Prometheus metrics

```python
# src/musaid/observability/slis.py
"""SLIs are ratios of good events to total. We emit counters the SLO
recording rules aggregate. Quality SLI comes from the async eval worker."""
from prometheus_client import Counter

REQUESTS = Counter("musaid_requests_total", "all requests", ["result"])   # ok|error
LATENCY_GOOD = Counter("musaid_latency_good_total", "requests under 3s")
LATENCY_TOTAL = Counter("musaid_latency_total", "requests measured for latency")
FAITHFUL_GOOD = Counter("musaid_faithful_good_total", "sampled answers >=0.8")
FAITHFUL_TOTAL = Counter("musaid_faithful_total", "sampled answers evaluated")


def record_request(ok: bool, latency_s: float):
    REQUESTS.labels("ok" if ok else "error").inc()
    LATENCY_TOTAL.inc()
    if latency_s < 3.0:
        LATENCY_GOOD.inc()


def record_faithfulness(value: float):           # called by the M3 worker
    FAITHFUL_TOTAL.inc()
    if value >= 0.8:
        FAITHFUL_GOOD.inc()
```

### SLO recording + burn-rate alert rules (Prometheus)

```yaml
# deploy/prometheus/slo_rules.yaml
groups:
  - name: musaid_slo
    rules:
      # SLI: latency good ratio over rolling windows
      - record: musaid:latency_sli:ratio_rate1h
        expr: sum(rate(musaid_latency_good_total[1h]))
              / sum(rate(musaid_latency_total[1h]))
      # Quality SLI: faithfulness good ratio
      - record: musaid:faithfulness_sli:ratio_rate1h
        expr: sum(rate(musaid_faithful_good_total[1h]))
              / sum(rate(musaid_faithful_total[1h]))

  - name: musaid_slo_alerts
    rules:
      # FAST BURN (page): 14.4x burn over 1h AND 5m for the 99% latency SLO
      - alert: MusaidLatencyFastBurn
        expr: |
          (1 - musaid:latency_sli:ratio_rate1h)  > (14.4 * 0.01)
          and
          (1 - musaid:latency_sli:ratio_rate5m)  > (14.4 * 0.01)
        for: 2m
        labels: {severity: page}
        annotations:
          summary: "Latency SLO fast burn — error budget draining in ~2 days"
          runbook: "runbooks/latency_provider.md"

      # QUALITY fast burn (page): faithfulness SLO (95%) burning fast
      - alert: MusaidFaithfulnessFastBurn
        expr: (1 - musaid:faithfulness_sli:ratio_rate1h) > (14.4 * 0.05)
        for: 5m
        labels: {severity: page}
        annotations:
          summary: "Faithfulness SLO fast burn — possible hallucination spike"
          runbook: "runbooks/hallucination_spike.md"
```

### An AI-incident runbook (excerpt)

```markdown
# runbooks/hallucination_spike.md
## Incident: Faithfulness SLO fast burn (hallucination spike)

### Detect / confirm
- Alert: MusaidFaithfulnessFastBurn. Confirm in Grafana "Quality" panel;
  drill to the lowest-faithfulness traces (link on panel).
- Segment: which lang/intent/prompt_version/model_version? (M3 dashboard)

### Mitigation ladder (fastest-safest first)
1. If burn aligns to a recent PROMPT promotion -> roll back the prompt label
   (M4): `production -> <prev>` (seconds). Confirm burn stops.
2. Else if `gen_ai.response.model` changed -> PIN model to last-good version.
3. Else if retrieval `n_chunks=0` rate is up -> enable refuse-on-empty guardrail.
4. If none isolate it -> raise stricter refusal threshold (degrade gracefully),
   page the model owner.

### Preserve evidence
- Tag the incident window; export the worst 20 traces (redacted) for postmortem.

### Exit
- Faithfulness back above SLO for 30 min. Open blameless postmortem within 24h;
  REQUIRED action item: add the failing cases to eval_gold (M5) as regression tests.
```

## Hands-on Lab 6 — SLO Dashboard, Burn-Rate Alerts, and an Incident

| | |
|---|---|
| **Objective** | Define Musaid's SLIs/SLOs, build an SLO+error-budget Grafana dashboard, wire multi-window burn-rate alerts, then run a hallucination-spike incident end to end with the runbook and write the postmortem |
| **Duration** | 2 × 50 min (Day 3 H4 + H5) |
| **Setup** | Lab 5 solution, `git checkout lab6-start`, Prometheus + Alertmanager + Grafana running |

**Part A tasks — SLO + alerts (50 min)**
1. Emit the SLI counters; add the SLO recording rules for latency and faithfulness (15 min).
2. Build a Grafana SLO panel: current SLI, SLO target, remaining error budget, burn-rate sparkline, per SLO (15 min).
3. Wire the fast-burn (page) and slow-burn (ticket) alerts to Alertmanager; route page→"on-call", ticket→"backlog" (10 min).
4. Validate the alert with a synthetic latency injection; confirm fast-burn fires and slow-burn stays quiet on a blip (10 min).

**Part B tasks — run the incident (50 min)**
1. Inject the incident: `make inject hallucination-spike` (flips prompt to a regressed version on 30% of traffic) (5 min).
2. Respond by the runbook: confirm the faithfulness fast-burn page, drill to worst traces, segment, and identify the aligned prompt promotion (15 min).
3. Mitigate: roll back the prompt label (M4); confirm the burn stops within minutes (10 min).
4. Preserve evidence; write `POSTMORTEM.md` (timeline, root cause, detection, mitigation, action items) with a REQUIRED regression-test item added to `eval_gold` (15 min).
5. Commit `feat(slo): SLO dashboard + burn-rate alerts + incident runbook + postmortem` (5 min).

**Expected outputs**
```
SLO dashboard: availability 99.6% (budget 80% left), latency 96% (budget 62% left),
               faithfulness 94.9% (budget 12% left — draining)
Fast-burn alert fired at T+4m; blip test: no false page
Incident: rolled back prompt label -> faithfulness recovered in 6m
POSTMORTEM.md written; +3 regression cases added to eval_gold
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Alert never fires | Threshold/window wrong | Recompute burn-rate math; verify recording rule outputs |
| Alert flaps | Single-window alert | Add the short confirmation window (multi-window) |
| Faithfulness SLI empty | Eval worker not feeding counters | Wire `record_faithfulness` from the M3 worker |
| Rollback didn't stop burn | Cause wasn't the prompt | Follow the ladder: pin model / refuse-on-empty next |
| Budget panel wrong | Window mismatch SLI vs SLO | Align rolling windows to the SLO period |

**Instructor notes.** Part B is the emotional peak of the course — a real page, a real drill, a real fix in minutes using the M4 lever. Insist the postmortem's top action item is a gold-set regression case; that is the loop closing. Keep the incident to one clear root cause the first time; run a second, ambiguous injection only for strong cohorts.

## Mini Exercises

**Quiz.** (1) What is an error budget and what decision does it drive? (2) Why burn-rate alerts over threshold alerts? (3) What quality SLO does only LLMOps have, and where does its data come from? (4) Why two windows in a burn-rate alert? (5) What is the mandatory action item of an AI-incident postmortem? → a gold-set regression test.

**Debugging exercise.** Branch `sim-alert-fatigue`: single-window alerts page 40×/day. Participants convert to multi-window multi-burn-rate and measure the drop to actionable pages only.

**Design exercise.** Each pair sets SLOs for Musaid's five SLIs with justification (why not 100%?), and computes the monthly error budget in minutes/answers for each.

**Discussion.** Who owns the faithfulness SLO, and when the budget is exhausted, who has authority to freeze prompt/model changes until it recovers?

## Case Study — The 3am Page That Should Not Have Happened

**Scenario.** A team wired an alert on "faithfulness < 0.9 right now". It paged the on-call 30+ times a night on normal sampling noise; the team muted it — and then missed a real hallucination spike because the alert was silenced.

**Business context.** Alert fatigue is a reliability risk in itself: the muted alert is the one that would have caught the real incident. For a national service, a missed hallucination spike is a public-trust event.

**Technical challenge.** Replace noise-driven alerting with budget-driven alerting that pages only on genuine, sustained burns.

**Constraints.** Faithfulness is a *sampled statistical* signal — instantaneous dips are expected; the alert must tolerate noise but catch sustained regression fast.

**Solution approach.** Define a faithfulness SLO (95%/7d) with an error budget; alert on multi-window burn rate (fast-burn 14.4× over 1h+5m pages; slow-burn 3× over 6h tickets). Noise no longer pages because a single-sample dip cannot sustain a 1h burn; a real regression sustains both windows and pages within minutes. The muted-alert failure becomes impossible.

**Discussion questions.** (1) Why is a sampled quality signal especially prone to threshold-alert fatigue? (2) How does the dual window separate noise from signal? (3) What's the right SLO window for a quality SLI and why? (4) How do you set page vs ticket severity boundaries?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| SLIs defined incl. quality | Reliability | ≥ 5 incl. faithfulness + safety | dashboard |
| Error-budget panels | Reliability | per-SLO, live | Grafana |
| Alert precision | Reliability | fast-burn pages only on real burns; 0 blip pages | injection test |
| Incident MTTR | Reliability | quality incident mitigated < 10 min | drill timing |
| Postmortem→regression | Improvement | every incident yields a gold case | postmortem review |

**Example benchmark table:**

| SLO | Target | Current SLI | Budget remaining | Alert |
|---|---|---|---|---|
| Availability | 99.5%/30d | 99.6% | 80% | quiet |
| Latency < 3s | 95%/30d | 96.1% | 62% | quiet |
| Faithfulness ≥ 0.8 | 95%/7d | 94.9% | 12% (draining) | slow-burn ticket |
| Safety | 100%/7d | 100% | full | quiet |

## Required Visuals and Training Assets

### Diagrams
1. **Error budget as a fuel gauge** — *Elements:* SLO, budget, burn-rate sparkline; ship-vs-stabilise decision at empty. *Style:* gauge + decision.
2. **Multi-window burn-rate alert** — *Elements:* long + short windows both breaching → page; only long → ticket; only short → nothing. *Style:* truth-table + timeline.
3. **AI-incident runbook ladder** — *Elements:* the mitigation ladder per incident class, fastest lever (prompt rollback) at top. *Style:* ladder.
4. **On-call dashboard layout** — *Elements:* SLO row, golden signals, LLM-specific, drill-to-trace. *Style:* dashboard wireframe.

### Images
1. **Grafana SLO/error-budget panel** — *why:* target output; *content:* four SLOs with budgets.
2. **Alertmanager fast-burn firing** — *why:* alert-to-runbook link; *content:* the page with runbook annotation.
3. **POSTMORTEM.md** — *why:* the improvement artefact; *content:* timeline + regression action item.

### Simulations
1. **hallucination-spike** — *Setup:* regressed prompt on 30% traffic. *Expected:* faithfulness burn → page → rollback. *Objective:* run the runbook.
2. **alert-fatigue** — *Setup:* threshold alert on noisy SLI. *Expected:* 40 pages/night. *Objective:* burn-rate conversion.

### Interactive Activities
- **SLO-setting workshop (15 min):** teams negotiate Musaid's SLOs with a "product owner" instructor and justify < 100%.
- **Tabletop incident (15 min):** instructor narrates an ambiguous incident; teams walk the runbook ladder aloud.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `slo_history.jsonl` | Pre-seeded SLI history | JSONL | 30d | Populate budget panels without waiting |
| `incident_injections/` | Fault-injection configs | YAML | 4 | Lab 6 + tabletop |

### Demo Requirements
- **Instructor demo:** trigger a fast-burn page live, drill to the worst traces, and mitigate by prompt rollback in under 6 minutes.
- **Student demo:** one pair presents their POSTMORTEM.md and the regression case it produced.
- **Expected outputs:** SLO dashboard, working burn-rate alerts, a run incident with postmortem and a new gold case.

---

# Module 7 — Reliability Engineering for AI Platforms

## Module Overview

**Purpose.** The final module hardens Musaid against the failures the previous modules learned to *see*. It teaches the resilience patterns that keep an LLM platform serving through provider outages, latency spikes, cost surges, and dependency failures: graceful degradation, fallbacks, timeouts and retry budgets, circuit breakers, semantic caching, load shedding, and multi-provider resilience — all governed by the SLOs from M6.

**Business relevance.** A national assistant sits on external, imperfect dependencies (LLM providers, vector DBs, tool APIs). Reliability engineering is what turns "the provider had an outage so we were down" into "the provider had an outage and citizens barely noticed". For a sovereign platform, provider independence and graceful degradation are also strategic: no single vendor can take down a national service, and cost is controlled by design.

**Industry use cases.**
- An assistant that fails over from a primary to a backup model within the latency SLO when the primary returns 5xx or slows.
- A high-traffic service where a semantic cache serves 35% of queries at near-zero cost and latency.
- A platform that sheds low-priority load and degrades to retrieval-only answers rather than collapsing under a spike.

**Expected competencies.** Participants can implement timeouts and retry budgets, circuit breakers, provider fallbacks, semantic caching, graceful degradation ladders, and load shedding, and can prove the service holds its SLOs under injected failure.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Implement timeouts, retry budgets, and circuit breakers around model/tool calls | LO5, LO6 |
| 7.2 | Design provider fallbacks and multi-provider resilience | LO5, LO6 |
| 7.3 | Implement semantic caching for cost and latency | LO6 |
| 7.4 | Design graceful-degradation ladders and load shedding | LO5, LO4 |
| 7.5 | Validate reliability against SLOs under injected failure | LO5 |

## Technical Content

### 1. Timeouts, retries, and retry budgets

Every external call (LLM, retriever, tool) needs a **timeout** — an un-bounded call is an outage waiting to happen; a slow provider must become a fast, handled failure, not a hung request. Above timeouts:

- **Retries** help with transient errors (429, 503, network blips) but must be bounded and backed off (exponential + jitter) or they amplify an outage into a self-inflicted DDoS.
- **A retry budget** caps retries as a fraction of total traffic (e.g., ≤ 10%). When the budget is exhausted (the dependency is genuinely down, not blipping), stop retrying and fail fast to the fallback. This is the single most important reliability control — naive "retry 3 times always" turns a provider hiccup into a cascading meltdown.
- **Idempotency:** only retry idempotent operations; a tool that books an appointment must not be retried blindly.

### 2. Circuit breakers

A circuit breaker stops calling a failing dependency so it can recover and so your service fails fast instead of piling up timeouts:

- **Closed:** calls flow; failures are counted.
- **Open:** after a failure threshold, calls are rejected immediately (fail fast to fallback) for a cool-down.
- **Half-open:** after cool-down, a trial call probes recovery; success closes the circuit, failure re-opens it.

For Musaid, a breaker on the primary LLM provider means a provider outage flips to the fallback model in milliseconds instead of every request eating the full timeout. Breakers per dependency (primary model, backup model, retriever, each tool) isolate failures so one bad tool cannot sink the whole service.

### 3. Provider fallbacks and multi-provider resilience

LLM providers fail, deprecate, rate-limit, and silently change. Resilience means not being hostage to one:

- **Fallback chain:** primary model → backup model (different provider or a self-hosted model) → degraded retrieval-only answer. Each step is cheaper/less capable but keeps the service *useful*.
- **Version pinning + canary (M4):** protects against silent changes; the fallback protects against outages.
- **Sovereign fallback:** a self-hosted open model within the national boundary as the last capable tier is both a reliability and a data-residency control.
- **Consistency of contract:** the fallback must honour the same output contract and safety guardrails; a fallback that bypasses safety is a new incident class.

The reliability goal: **degrade capability, never correctness or safety.** A backup model giving a simpler correct answer is fine; any model giving an ungrounded or unsafe answer is not.

### 4. Semantic caching

Many citizen queries are near-duplicates ("how do I renew my ID", "renew national id"). A **semantic cache** keys on the embedding of the query (and retrieved context), returning a stored answer for sufficiently similar, cache-safe queries:

- **Wins:** large cost and latency reduction (cache hits skip the LLM entirely), and load relief during spikes.
- **Risks:** staleness (cached answer outdated after a knowledge update — must invalidate on KB version change), over-broad matching (two similar-looking queries with different intent — tune the similarity threshold conservatively), and personalization/PDPL (never cache answers that depend on personal context; cache only general procedural answers).
- **Observability:** cache hit rate is a first-class metric (M6 dashboard); a cache serving stale answers is a quality incident, so cached answers are still sampled for eval.

### 5. Graceful degradation and load shedding

Under stress, a reliable service sheds and degrades rather than collapsing:

- **Degradation ladder:** full RAG+tools → RAG-only (skip slow tools) → cached/retrieval-only → static "service busy, try again / here is the official link" refusal. Each rung keeps citizens served with *something correct*.
- **Load shedding:** when saturated, reject or queue low-priority traffic (e.g., background/batch) to protect interactive users, returning 503 + Retry-After early rather than timing out everyone. Better to serve 90% well than 100% badly.
- **Prioritization:** interactive citizen queries > internal/batch; the shed decision is explicit and monitored.

### 6. Validating reliability against SLOs

Reliability patterns are only real if tested under failure. **Fault injection / chaos** proves them: kill the primary provider, inject latency, exhaust rate limits, corrupt retrieval — and confirm the SLOs (M6) hold: availability stays above target via fallback, latency stays bounded via timeouts+breaker, quality stays acceptable via degrade-not-fabricate. The capstone dashboard shows these holding under injected failure — the proof that Musaid is production-reliable.

Common mistakes: no timeouts (hung requests); unbounded retries (cascading outage); no circuit breaker (piling timeouts); single provider (hostage to one vendor); a fallback that skips safety; caching personalized/PII answers; caching without invalidation on KB change; degrading to fabrication instead of refusal; and never fault-testing so the "resilience" is theoretical.

## Code Examples

### Timeout, retry budget, and circuit breaker around the LLM

```python
# src/musaid/reliability/resilient_llm.py
"""Wraps the LLM client with a timeout, a bounded+jittered retry, a shared
retry budget, and a per-provider circuit breaker. Fails fast to a fallback."""
import random
import time
from musaid.reliability.circuit import CircuitBreaker
from musaid.reliability.budget import RetryBudget

breaker = CircuitBreaker(fail_threshold=5, cooldown_s=30)
retry_budget = RetryBudget(max_ratio=0.10)          # retries <= 10% of traffic


class ResilientLLM:
    def __init__(self, primary, fallback, timeout_s=8.0, max_retries=2):
        self.primary, self.fallback = primary, fallback
        self.timeout_s, self.max_retries = timeout_s, max_retries

    def chat(self, messages):
        if breaker.is_open():                       # provider known-bad: skip it
            return self._fallback(messages, reason="circuit_open")
        for attempt in range(self.max_retries + 1):
            try:
                completion = self.primary.chat(messages, timeout=self.timeout_s)
                breaker.record_success()
                return completion
            except (TimeoutError, ProviderError) as exc:
                breaker.record_failure()
                transient = isinstance(exc, TimeoutError) or exc.status in (429, 503)
                if transient and attempt < self.max_retries and retry_budget.allow():
                    time.sleep((2 ** attempt) * 0.2 + random.random() * 0.1)  # backoff+jitter
                    continue
                return self._fallback(messages, reason=type(exc).__name__)

    def _fallback(self, messages, reason):
        # Degrade capability, NEVER safety: fallback keeps the same guardrails.
        span_note(f"fallback:{reason}")
        return self.fallback.chat(messages, timeout=self.timeout_s)
```

### Semantic cache with invalidation

```python
# src/musaid/reliability/semantic_cache.py
"""Cache general procedural answers by query embedding. Never cache answers
that depend on personal context. Invalidate on knowledge-base version bump."""
from musaid.embeddings import embed
from prometheus_client import Counter

CACHE_HIT = Counter("musaid_cache_hits_total", "semantic cache hits")
CACHE_MISS = Counter("musaid_cache_miss_total", "semantic cache misses")
SIM_THRESHOLD = 0.93          # conservative: avoid over-broad matches


class SemanticCache:
    def __init__(self, store, kb_version: str):
        self.store, self.kb_version = store, kb_version

    def get(self, query: str, is_personalized: bool):
        if is_personalized:                       # PDPL + correctness: never cache
            return None
        vec = embed(query)
        hit = self.store.nearest(vec, kb_version=self.kb_version)  # scoped to KB version
        if hit and hit.similarity >= SIM_THRESHOLD:
            CACHE_HIT.inc()
            return hit.answer
        CACHE_MISS.inc()
        return None

    def put(self, query, answer, is_personalized):
        if not is_personalized:
            self.store.add(embed(query), answer, kb_version=self.kb_version)

    def invalidate_on_kb_change(self, new_version: str):
        # A KB update makes cached procedural answers potentially stale.
        self.store.drop_version(self.kb_version)
        self.kb_version = new_version
```

### The graceful-degradation ladder

```python
# src/musaid/reliability/degrade.py
"""Serve SOMETHING correct at every rung. Degrade capability, never safety."""
def answer_with_degradation(query, assistant, cache, health):
    # rung 0: cache (cheapest, fastest)
    cached = cache.get(query.text, query.is_personalized)
    if cached:
        return cached.mark(source="cache")
    # rung 1: full RAG + tools (normal)
    if health.tools_ok and health.llm_ok:
        return assistant.answer(query)
    # rung 2: RAG only (skip slow/failing tools)
    if health.llm_ok:
        return assistant.answer(query, use_tools=False).mark(degraded="no_tools")
    # rung 3: retrieval-only — return the official source, no generation
    chunks = assistant.retriever.search(query.text, k=3, lang=query.lang)
    if chunks:
        return official_source_reply(chunks).mark(degraded="retrieval_only")
    # rung 4: honest refusal with the official channel (never fabricate)
    return busy_refusal(query.lang).mark(degraded="refuse")
```

## Hands-on Lab 7 — Harden Musaid

| | |
|---|---|
| **Objective** | Add timeout+retry budget, a circuit breaker, a fallback model, a semantic cache, and a degradation ladder to Musaid, then prove — via fault injection — that the SLOs hold through a primary-provider outage |
| **Duration** | 50 minutes |
| **Setup** | Lab 6 solution, `git checkout lab7-start`, mock-LLM supports `--fail` and `--slow` flags; backup mock model available |

**Instructions & tasks**
1. *(10 min)* Wrap the LLM in `ResilientLLM` with timeout + bounded retry + retry budget; add the circuit breaker; add span notes for fallback events.
2. *(10 min)* Add the fallback model; inject a primary outage (`--fail 100%`) and confirm traffic flips to fallback within the latency SLO, breaker opens, availability holds.
3. *(10 min)* Add the semantic cache; replay traffic; measure hit rate and the cost/latency reduction; prove personalized queries are never cached.
4. *(10 min)* Add the degradation ladder; inject tool failure then LLM failure; confirm each rung serves a correct-or-refusing answer (never a fabrication).
5. *(5 min)* Validate against SLOs: run the fault scenario and confirm the M6 dashboard shows availability/latency/faithfulness holding.
6. *(5 min)* Commit `feat(reliability): fallback + breaker + retry budget + semantic cache + degradation`.

**Expected outputs**
```
Primary outage (--fail 100%): availability 99.4% held via fallback; breaker OPEN in 5 calls;
   p95 latency 2.7s (within 3s SLO); 0 hung requests
Semantic cache: 34% hit rate; mean cost/req 0.0121 -> 0.0081 SAR; personalized never cached
Degradation: tool-fail -> RAG-only; LLM-fail -> retrieval-only (official source); no fabrication
SLO dashboard under fault: all SLOs green
```

**Troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| Outage still causes timeouts pile-up | No circuit breaker / breaker threshold too high | Lower threshold; confirm open state skips primary |
| Retries worsen the outage | Unbounded retries | Add retry budget; fail fast when exhausted |
| Cache serves stale answers | No KB-version invalidation | Scope cache to KB version; invalidate on bump |
| Personalized answer cached | Missing is_personalized guard | Never cache personalized/PII-dependent answers |
| Fallback bypasses safety | Guardrails only on primary path | Apply the same guardrails to the fallback |

**Instructor notes.** The climax is injecting a full primary outage and watching the SLO dashboard stay green — this is the whole course paying off. Stress the "degrade capability, never safety/correctness" rule at rung 4: a busy refusal with the official link beats a confident fabrication every time.

## Mini Exercises

**Quiz.** (1) Why is a retry budget more important than the retry count? (2) Name the three circuit-breaker states. (3) What must a fallback never skip? → safety guardrails. (4) When must a semantic cache invalidate? → on knowledge-base version change (and never cache personalized). (5) What is the bottom rung of the degradation ladder and why not fabricate? → honest refusal with official channel; fabrication is the worst failure.

**Debugging exercise.** Branch `sim-retry-storm`: a provider blip plus unbounded retries turns 3% errors into 60% as retries pile on. Participants add a retry budget + breaker and watch the storm subside.

**Design exercise.** Each pair designs Musaid's full degradation ladder and marks which SLO each rung protects, and where safety is enforced at every rung.

**Discussion.** Sovereignty and reliability: argue for a self-hosted open model as the last fallback tier — what does it buy in outage resilience and data residency, and what does it cost?

## Case Study — The Provider Outage That Nobody Noticed

**Scenario.** Musaid's primary LLM provider has a 40-minute regional outage during morning peak. Citizens experience a brief, barely-perceptible slowdown; availability stays at 99.4%; no incident is declared beyond an informational note.

**Business context.** The same outage a year earlier (single-provider, no breaker, unbounded retries) took the assistant down for the full 40 minutes and generated headlines. The difference is entirely the reliability engineering built this module.

**Technical challenge.** Survive a total primary-provider outage within SLO, without a single-vendor dependency, while preserving safety and correctness.

**Constraints.** The fallback must stay within the sovereign boundary for sensitive traffic; degraded answers must remain correct/grounded; cost of running a hot fallback must be justified.

**Solution approach.** Circuit breaker opens within five failed calls and stops hammering the dead provider; traffic flips to a self-hosted sovereign fallback model within the latency SLO; the semantic cache absorbs a third of load at zero provider dependency; the degradation ladder means the worst case is a grounded retrieval-only answer, never a fabrication. The M6 dashboard shows the whole event as a small, bounded blip — with every SLO held.

**Discussion questions.** (1) Which single control prevented the cascade (retries piling up)? (2) Why does a sovereign self-hosted fallback matter beyond reliability? (3) How do you keep fallback answers grounded and safe? (4) What made this a non-incident where last year's was a crisis?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Availability under primary outage | Reliability | ≥ SLO (99.5%) via fallback | fault injection |
| Retry storm prevented | Reliability | error amplification bounded | retry-budget test |
| Circuit breaker trip time | Reliability | opens ≤ 5 failed calls | breaker test |
| Cache hit rate | Cost/Performance | ≥ 30% on repetitive traffic | cache metrics |
| Cost reduction from cache | Cost | measurable SAR/req drop | before/after |
| Degradation correctness | Safety | 0 fabrications at any rung | degrade test |

**Example benchmark table:**

| Scenario | Availability | p95 latency | Cost/req | Fabrications |
|---|---|---|---|---|
| Normal (no hardening) | 99.6% | 1.2s | 0.0121 SAR | 0 |
| Primary outage, no hardening | 41% | timeouts | n/a | spike |
| Primary outage, hardened | 99.4% | 2.7s | 0.0081 SAR | 0 |

## Required Visuals and Training Assets

### Diagrams
1. **Reliability pattern stack** — *Elements:* timeout → retry budget → circuit breaker → fallback chain → degradation ladder, each labelled with what it protects. *Style:* layered stack.
2. **Circuit breaker state machine** — *Elements:* closed/open/half-open with transitions. *Style:* state diagram.
3. **Fallback chain + degradation ladder** — *Elements:* primary → backup → retrieval-only → refuse, with safety enforced at every rung. *Style:* ladder with a safety rail.
4. **Cache flow** — *Elements:* query → embed → similarity check → hit/miss → KB-version invalidation. *Style:* flow.

### Images
1. **SLO dashboard green under injected outage** — *why:* the payoff; *content:* availability/latency/quality holding during a fault.
2. **Breaker-open span note** — *why:* observability of resilience; *content:* fallback event on a trace.
3. **Cache-hit-rate panel** — *why:* cost win; *content:* hit rate + cost reduction.

### Simulations
1. **primary-outage** — *Setup:* `--fail 100%` on primary. *Expected:* breaker opens, fallback serves, SLO holds. *Objective:* provider resilience.
2. **retry-storm** — *Setup:* blip + unbounded retries. *Expected:* amplification. *Objective:* retry budgets.

### Interactive Activities
- **Chaos game (15 min):** instructor injects a random failure; teams predict which control saves them and verify on the dashboard.
- **Ladder design (10 min):** teams design a degradation ladder for a *different* AI service and defend safety at each rung.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `repetitive_traffic.jsonl` | Near-duplicate queries | JSONL | 500 | Cache hit-rate lab |
| `fault_scenarios/` | Injection configs | YAML | 4 | Reliability validation |

### Demo Requirements
- **Instructor demo:** inject a full primary outage live and narrate the SLO dashboard staying green as the fallback takes over.
- **Student demo:** one pair shows their cache hit rate and degradation ladder behaviour under tool+LLM failure.
- **Expected outputs:** hardened Musaid holding SLOs under fault, semantic cache live, safe degradation proven.

---

# Final Capstone Project

## Title: Production Observability and Reliability Platform for Musaid

## Project Scenario

You are the on-call LLMOps engineer for **Musaid (مساعد)**, the bilingual citizen-services assistant of a national digital-government portal, serving hundreds of thousands of conversations a day in Arabic and English. The service already exists and is deployed. Your mandate for this capstone: make it **observable, evaluated, safely-changeable, self-improving, SLO-governed, and reliable** — and prove it with a single operations dashboard and an incident you can run on demand. Everything you built in Labs 1–7 is a component; the capstone is the integration plus a live demonstration that Musaid can be operated with confidence.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Distributed tracing (LO1):** the full RAG+tools path instrumented with OpenTelemetry + GenAI conventions; token/cost/model-version/prompt-version on every trace; exported to Langfuse and an OTel backend; correlated structured logs; sampling that keeps 100% of errored/low-quality traces; PII redacted.
2. **Online evaluation (LO2):** async eval worker scoring live traffic — deterministic checks on 100%, calibrated LLM-as-judge faithfulness on a sample; scores attached to traces and aggregated as a segmented quality pillar (by lang/intent/prompt/model version); judge–human agreement ≥ 0.6.
3. **Prompt/version management (LO3):** all prompts in a registry (none in code); versions labelled and tagged on traces; an offline eval promotion gate; at least one shadow or canary rollout with evidence; a rehearsed sub-60s label rollback.
4. **Feedback flywheel (LO2/LO6):** explicit + ≥ 2 implicit feedback signals joined to traces; an annotation queue; at least one curated, redacted, versioned eval dataset that extended the promotion gate.
5. **SLOs, alerting, incident response (LO5/LO4):** ≥ 5 SLIs including a quality SLO and a safety SLO; error-budget dashboard; multi-window burn-rate alerts (page + ticket); ≥ 1 AI-incident runbook; one run incident with a blameless `POSTMORTEM.md` whose action item added a gold-set regression case.
6. **Reliability engineering (LO5/LO6):** timeout + retry budget + circuit breaker; a fallback model; a semantic cache with invalidation; a graceful-degradation ladder; proof via fault injection that SLOs hold through a primary-provider outage with zero fabrications.
7. **Operations dashboard + docs (LO5/LO6):** one Grafana dashboard integrating latency, cost, quality-by-segment, SLO/error-budget, and reliability panels, each drilling to traces; a `RUNBOOKS.md`, and a `DECISIONS.md`.

**One extension (choose at least one):**
- Multi-provider routing with cost/quality-aware model selection and per-model SLOs
- Automated canary controller that promotes/rolls back a prompt on live eval scores without human action
- Cost-optimization pass: prompt-token reduction + cache tuning with a measured SAR/1k-request before/after
- Drift detector on input distribution that opens a dataset-gap ticket when a new intent surges
- Trace-based automated regression harness: nightly replay of the gold set against the current prod prompt/model

## Architecture (target state)

```
user ─► gateway ─► Musaid (traced: retrieve→prompt(registry)→resilient-LLM→tools) ─► answer
   │        │            │  spans (OTel/GenAI) ─► Collector ─► Langfuse / Tempo / Prometheus / Loki
   │        │            └─ resilient-LLM: timeout+retry-budget+breaker → fallback → degrade ladder
   │        └─ semantic cache (KB-versioned)                              │
   └─ /v1/feedback ─► scores ─► annotation queue ─► curated datasets ─────┤
 async eval worker ◄── sampled traces ── faithfulness/safety scores ──────┘
 Grafana: latency | cost | quality-by-segment | SLO/error-budget | reliability   (drill → traces)
 Alertmanager: fast-burn(page) + slow-burn(ticket) → runbooks → rollback lever (prompt label)
```

## Deliverables

1. Repository URL with full history and all Lab 1–7 components integrated
2. Live Grafana dashboard URL (or exported dashboard JSON + screenshots) with all panel groups
3. `RUNBOOKS.md` (≥ 2 AI-incident runbooks) + `POSTMORTEM.md` from a run incident
4. `DECISIONS.md`: five one-paragraph operations decisions with rationale (e.g., sampling strategy, quality-SLO target, fallback tier choice, cache scope, judge model)
5. 6-minute demo: open a trace end-to-end, show the quality pillar and a segment, trigger a burn-rate alert and mitigate by rollback, and inject a provider outage showing SLOs hold

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: traced path + cost/version tags (Labs 1–2) | End Day 1 | span tree in Langfuse |
| M-B: online eval + registry + shadow (Labs 3–4) | End Day 2 | calibrated judge + promoted v2 |
| M-C: flywheel + SLO/alerts + run incident (Labs 5–6) | Day 3 H5 | POSTMORTEM + gold case |
| M-D: reliability hardening + extension (Lab 7 + choice) | Day 4 H2 | SLOs hold under outage |
| M-E: integrated dashboard + demo | Day 4 H5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Tracing & instrumentation | 15 | Full path, GenAI conventions, cost/version tags, correlated logs, error-preserving sampling, PII-clean | Minor gaps (a hop untraced, cost only on success) | No span tree, no version tags, PII in traces |
| Online evaluation & quality pillar | 20 | Deterministic 100% + calibrated judge sampled; segmented; kappa ≥ 0.6; async | Judge uncalibrated or not segmented | Synchronous/absent eval; no quality signal |
| Prompt & version management | 15 | Registry, gate, shadow/canary evidence, sub-60s rollback, full attribution | Registry present; gate or rollout thin | Prompts in code; no attribution/rollback |
| Feedback flywheel | 10 | Explicit + implicit joined; annotation; redacted versioned dataset feeding the gate | Feedback captured but loop not closed | No implicit signals or no curated dataset |
| SLOs, alerting & incident response | 20 | ≥5 SLIs incl. quality+safety; burn-rate alerts; runbook; run incident + postmortem + regression case | SLOs present; alerts single-window or incident not run | No quality SLO; threshold alerts; no runbook |
| Reliability engineering | 15 | Timeout/budget/breaker/fallback/cache/degradation; SLOs proven under injected outage; 0 fabrications | Patterns present; not fault-validated | No breaker/fallback; cascades under failure |
| Dashboard, docs & demo | 5 | Integrated drill-to-trace dashboard; crisp demo; DECISIONS shows trade-off literacy | Works; docs/demo thin | Cannot operate own service in demo |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the live operations surface first* (dashboard, alert history, incident postmortem, trace drill-downs), demo second — the point of the course is that the running system speaks.
- Anti-pattern flags that cap a criterion at 70%: an uncalibrated judge trusted as truth; prompts hard-coded "for the incident"; threshold alerts dressed as SLOs; a fallback that skips safety; a cache without invalidation; a postmortem that assigns blame instead of producing a regression test.
- Verify one reliability claim live: inject a primary-provider outage and require the participant to show SLOs holding and zero fabrications.
- Verify one quality claim live: ask the participant to open the lowest-faithfulness trace of the day and explain the root cause from its spans.

## Bonus Tasks (for early finishers / distinction seekers)

1. Automated canary controller: promote/rollback a prompt purely on live eval scores, with a kill switch.
2. Cost-optimization report: measured SAR/1k-request before/after prompt-token trimming + cache tuning.
3. Multi-provider quality-aware router with per-provider SLOs and a sovereign fallback tier.
4. Nightly gold-set replay harness that opens a regression ticket automatically on any segment drop.
5. Load-test the hardened service and publish a reliability envelope (RPS vs latency vs SLO) under fault.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** Name the fourth observability pillar unique to LLMOps and its data source. → quality/eval scores from the online-eval worker.
**Q2.** Which GenAI trace attribute detects a silent provider model swap? → `gen_ai.response.model`.
**Q3.** Why must expensive LLM-as-judge eval run asynchronously? → it adds latency/cost and can fail; must not touch serving path.
**Q4.** Two values that must never be Prometheus labels? → query string / trace id / session id (any high-cardinality) — name two.
**Q5.** What makes an LLM judge trustworthy? → calibration against human labels (agreement ≥ threshold).
**Q6.** Which two RAG evaluators separate a model problem from a retrieval problem? → faithfulness vs context-relevance.
**Q7.** Why reference a label (not a fixed version) for the production prompt? → promotion/rollback becomes a label move, no redeploy.
**Q8.** Shadow vs canary — which serves the candidate to real users? → canary; shadow is mirrored and not served.
**Q9.** Fastest mitigation for a prompt-caused quality incident, and how fast? → roll back the prompt label, seconds.
**Q10.** Why never rely on explicit feedback alone? → most users never click; silence ≠ satisfaction; use implicit signals.
**Q11.** What joins a thumbs-down to the prompt/model version that caused it? → the trace_id.
**Q12.** What must happen to a trace before it enters a shareable dataset? → PII redaction under PDPL.
**Q13.** Define error budget and the decision it drives. → 100%−SLO; ship-more-risk vs freeze-and-stabilise.
**Q14.** Why burn-rate alerts over threshold alerts? → alert on budget consumption rate → catches real sustained issues, avoids fatigue.
**Q15.** Why two windows in a burn-rate alert? → long window = significance, short window = still-happening; together kill flapping.
**Q16.** Mandatory action item of an AI-incident postmortem? → add the failing case to the gold set as a regression test.
**Q17.** Why is a retry budget more important than the retry count? → it prevents retries amplifying an outage into a cascade.
**Q18.** Three circuit-breaker states? → closed, open, half-open.
**Q19.** What must a fallback model never skip? → the safety guardrails and output contract.
**Q20.** When must a semantic cache invalidate, and what must it never cache? → on KB-version change; never cache personalized/PII-dependent answers.

## Practical Assessments

**PA-1 (30 min, Day 2):** Given a service with traces but no quality signal and a reported bad answer, add a deterministic + judge evaluator, find and explain the failing segment. Scored on: instrumentation correctness (40%), segmentation/diagnosis (40%), calibration awareness (20%).

**PA-2 (30 min, Day 3):** Given a noisy threshold-alert config paging 40×/night and a real regression it missed, convert to a multi-window burn-rate SLO alert and prove it pages on the real burn but not on blips. Scored on: SLO/budget math (40%), alert design (40%), validation evidence (20%).

**PA-3:** Capstone (rubric above) — 40% of course grade. Labs completion + PA-1/PA-2 — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (7 labs) | 30% | checkpoint commits + expected outputs + dashboards |
| PA-1 + PA-2 | 20% | artefacts + diagnosis notes |
| Quiz | 10% | 10-question selection |
| Capstone | 40% | rubric, operations-surface-first |

Badge issuance (Expert operations badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero integrity flags (identical judge rubrics/datasets across repos are checked) **and** a demonstrated live incident mitigation.

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone course org repos; push checkpoint tags (`lab1-start` … `lab7-start`) and all `sim-*` / `fault_scenarios` branches
- [ ] Bring up and smoke-test the full stack: Musaid API + mock-LLM (+ backup) + Postgres + Langfuse + OTel Collector + Tempo + Prometheus + Loki + Grafana + Alertmanager
- [ ] Pre-seed realistic trace data, `slo_history.jsonl`, and feedback traffic so dashboards/budgets are populated on Day 1 without waiting
- [ ] Regenerate `eval_gold_v1`, `human_labels.jsonl`; verify judge calibration reaches kappa ≥ 0.6 on the reference machine
- [ ] Rehearse the live demos: hallucination-trace root-cause, prompt rollback, burn-rate page, primary-provider outage staying green
- [ ] Verify mock-LLM mode works fully offline; confirm the real-provider path and a spend cap for the eval/rollout labs only
- [ ] Print A4 posters: reference architecture, four pillars, evaluator pyramid, prompt lifecycle, burn-rate alert, reliability stack
- [ ] Confirm classroom network + data-residency posture (all trace/eval/annotation data stays within the sovereign boundary)

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + git + a GitHub account
- [ ] Docker Desktop (WSL2 on Windows) or Colima; verify `docker run hello-world` and `make up`
- [ ] VS Code + Python + Docker extensions (or preferred IDE)
- [ ] `pip install opentelemetry-sdk opentelemetry-exporter-otlp langfuse prometheus-client structlog fastapi uvicorn`
- [ ] `jq` binary; access to the course Langfuse/Grafana (URLs + keys distributed in class)
- [ ] Clone course repo; run `make doctor` (validates the stack and prints ✓/✗ per service)

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| Heavy local stack (many containers) slow on laptops | High | Shared classroom cluster fallback; pair on stronger machine; mock-LLM by default |
| Spans in Langfuse but not Tempo (or vice versa) | High | One tracer provider, two processors; check the M2 "export twice" pattern |
| LLM-as-judge cost/quota anxiety | Medium | Mock-judge mode for most labs; real judge only for calibration + rollout, with spend cap |
| Prometheus cardinality explosion | Medium | The M2 lesson: no high-cardinality metric labels; move to span attributes |
| Burn-rate alert math confusion | Medium | Provide the worked SLO spreadsheet; teach budget-in-minutes intuition first |
| Judge won't calibrate (low kappa) | Medium | Tighten rubric, add examples, discrete scale; it's a teaching moment, not a failure |
| Arabic encoding/normalisation bugs | Medium | Force UTF-8 end to end; flag early — it corrupts eval and retrieval silently |
| Reliability patterns "work" but untested | Low | Insist on fault injection; a resilience claim without a chaos test is not done |

## Timing Recommendations

- Protect Labs 3 (online eval) and 6 (SLO + incident) at full length; compress M1/M7 theory (both land through their labs) if behind.
- If a cohort is strong: run a second, ambiguous incident in Lab 6 and add the multi-provider router extension in the capstone.
- If a cohort is weak: pre-seed more trace/feedback data so labs start from populated dashboards; demo (rather than have each pair build) the judge calibration.
- Hard rule: the Day-4 capstone assembly must start on time and the primary-outage validation must be demonstrated by every team; cut discussion, not the SLO-holds proof.

## Discussion Prompts (use during transitions)

1. "Your dashboard is green and your users are unhappy — which pillar is missing, and whose job is it?"
2. "A two-word prompt edit degrades answers for millions with no code diff and no model change. What in your process would have caught it?"
3. "Which is worse for a citizen: the assistant saying 'I don't know', or confidently giving a wrong procedure — and does your service prefer the safer failure?"
4. "If the running system is the audit evidence, what does *your* Musaid testify about your operations maturity?"
5. "When the error budget is exhausted, who has the authority to freeze changes — and does that person carry the pager?"

## Wrap-up (Day 4 final 15 minutes)

- Map each mandatory capstone requirement to the module that taught it and the failure mode it defends against (one slide).
- Forward pointer: SDA-AIE-314 (Performance, Scalability & Cost) optimises the cost/latency surface this course made observable; SDA-AIE-390 (capstone) requires exactly this operational surface — traces, quality SLOs, incident runbooks — defended before the panel.
- Reinforce the through-line: LLMOps is the loop that turns *operating* a GenAI service into *continuously improving* it — traces to see, evaluation to judge, feedback to learn, versioning to change safely, SLOs to stay reliable.
- Collect: repo URLs, dashboard URLs/exports, POSTMORTEM.md, DECISIONS.md; issue badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.12, OpenTelemetry ≥ 1.25 with GenAI semantic conventions, Langfuse ≥ 2.x, pydantic v2, Prometheus/Grafana 2025-era releases. Treat all Musaid user content as PDPL-protected personal data; verify pinned versions and data-residency posture in the course lock file before each delivery.*







