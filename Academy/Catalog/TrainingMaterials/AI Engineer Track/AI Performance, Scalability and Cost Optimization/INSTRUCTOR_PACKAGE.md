# AI Performance, Scalability and Cost Optimization
## أداء الذكاء الاصطناعي وقابلية التوسع وتحسين التكلفة

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | AI Performance, Scalability and Cost Optimization |
| **Arabic Title** | أداء الذكاء الاصطناعي وقابلية التوسع وتحسين التكلفة |
| **Code** | SDA-AIE-314 |
| **Level** | Expert / خبير |
| **Duration** | 3 days × 5 learning hours = **15 hours** |
| **Audience** | Senior engineers and platform architects |
| **Prerequisites** | SDA-AIE-216 |
| **Assessment** | Optimisation project with before/after benchmark |
| **Stackability** | Optimisation badge · Part of the MLOps & Reliability specialisation · Next: SDA-AIE-390 |
| **Tools & Platforms** | vLLM · TensorRT / ONNX Runtime · Kubernetes autoscaling · cost dashboards |

## Course Description

An expert module on engineering AI systems that are fast, scalable, and economical. Participants profile inference workloads, apply batching, caching, quantisation, and routing strategies, and design autoscaling serving infrastructure. The module builds the FinOps discipline to run national-scale AI services within budget.

The course is built around a single evolving artefact: **"Musaed" (مساعد)**, a national bilingual (Arabic/English) citizen-services assistant powered by an ALLaM-family large language model. Musaed answers public questions about government services under strict latency SLOs, spiky demand (Hajj-season and salary-day surges, prayer-time troughs), and a fixed monthly budget in Saudi Riyal. Every lab optimises one facet of Musaed — its profile, its serving stack, its model size, its routing policy, its GPU fleet, its cost dashboard — so that by Day 3 each participant owns a measured, before/after optimisation of the same live workload they will defend in the capstone. This is the operational discipline that turns an expensive proof-of-concept into a service the Kingdom can afford to run at national scale.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Analyze latency, throughput, and cost profiles of AI inference workloads
2. **LO2** — Implement batching, caching, and streaming optimisations for model serving
3. **LO3** — Apply quantisation, distillation, and model-routing to cut serving costs
4. **LO4** — Design autoscaling GPU infrastructure for variable demand
5. **LO5** — Evaluate build-versus-buy and model-tier trade-offs with TCO analysis
6. **LO6** — Develop cost-monitoring dashboards and optimisation playbooks

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Measure before you optimise | M1: Performance Profiling of Inference Workloads · M2: Serving Optimisation — Batching, Caching, Streaming | 45% | 55% | Signed latency/throughput/cost baseline of Musaed + a vLLM serving stack with continuous batching, prefix cache, and streaming |
| **Day 2** | Make it smaller, smarter, elastic | M3: Model Compression — Quantisation & Distillation · M4: Model Routing & Cascade Architectures · M5: GPU Infrastructure & Autoscaling | 40% | 60% | Quantised model with quality gate + a two-tier routing cascade + an autoscaling GPU deployment that tracks demand |
| **Day 3** | Run it within budget | M6: AI FinOps — Cost Monitoring & TCO · M7: Optimisation Project on a Live Workload · Capstone | 35% | 65% | Cost dashboard + TCO model + a defended before/after optimisation of Musaed |

## Hour-by-Hour Breakdown

### Day 1 — Measure Before You Optimise

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why AI services blow their budget** + course kickoff | Frame the latency/throughput/cost triangle; meet Musaed and its SLOs; name the seven optimisation levers | Interactive lecture + cost-shock discussion | 80/20 |
| 2 | **Profiling inference workloads** (M1) | LLM latency anatomy (TTFT, TPOT, ITL); throughput vs latency; percentiles; load generation | Lecture + live profiling demo | 65/35 |
| 3 | **Lab 1 — Baseline Musaed** | Load-test the unoptimised service; capture p50/p95/p99 latency, throughput, GPU util, cost/1k requests | Guided lab (pairs) | 10/90 |
| 4 | **Serving optimisation: batching, caching, streaming** (M2) | Continuous batching, KV cache & PagedAttention, prefix caching, token streaming | Lecture + vLLM walkthrough | 65/35 |
| 5 | **Lab 2 — Optimise the serving layer** | Move to vLLM; tune batching; enable prefix cache and streaming; re-benchmark against baseline | Guided lab (pairs) | 10/90 |

### Day 2 — Make It Smaller, Smarter, Elastic

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Model compression: quantisation & distillation** (M3) | Precision formats (FP16/BF16/FP8/INT8/INT4); AWQ/GPTQ; distillation; quality gates | Lecture + quantisation demo | 65/35 |
| 2 | **Lab 3 — Quantise Musaed** | Quantise the 13B model to INT4 (AWQ); measure memory/throughput/quality; pass or fail the gate | Guided lab | 10/90 |
| 3 | **Model routing & cascade architectures** (M4) | Complexity routing; small→large cascades; semantic caching; confidence-based escalation | Lecture + router design | 65/35 |
| 4 | **Lab 4 — Build the routing cascade** + **GPU infrastructure & autoscaling** (M5, part 1) | Implement a two-tier router; measure deflection rate and cost; intro to GPU sharing & autoscaling signals | Lab + micro-lecture | 30/70 |
| 5 | **Lab 5 — Autoscale the GPU fleet** (M5, part 2) | Kubernetes HPA/KEDA on queue depth; scale-to-N; measure cold-start and cost under a demand curve | Guided lab | 15/85 |

### Day 3 — Run It Within Budget

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **AI FinOps: cost monitoring & TCO** (M6) | Unit economics (cost/1k req, cost/1M tokens); TCO models; build-vs-buy; showback/chargeback | Lecture + TCO worksheet | 55/45 |
| 2 | **Lab 6 — Cost dashboard & TCO model** | Build a Grafana cost dashboard; compute self-host vs API TCO for Musaed; set budget alerts | Guided lab | 15/85 |
| 3 | **Optimisation project kickoff** (M7) + capstone scoping | Combine all levers into one optimisation plan; define the before/after benchmark protocol | Micro-lecture + project work | 25/75 |
| 4 | **Capstone build** | Execute the optimisation on Musaed; capture before/after evidence; complete the playbook | Project work | 0/100 |
| 5 | **Capstone demos + assessment + wrap-up** | 6-minute before/after defences; rubric scoring; path to SDA-AIE-390 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module optimises the same service — **Musaed**, the national citizen-services assistant. Never introduce a throwaway benchmark model; always evolve Musaed. The capstone is achievable in Day 3 only because Labs 1–6 each produced one measured lever on the *same* workload.
- **Measure-first culture:** enforce the rule "no optimisation without a baseline and a re-measurement." Every lab ends by writing a row into the shared `BENCHMARKS.md`. Optimisation claims without before/after numbers score zero — this is the thesis of the course.
- **Pace control:** Lab 2 (vLLM bring-up) and Lab 5 (autoscaling) are the most overrun-prone. Publish checkpoint tags (`lab1-baseline`, `lab2-vllm`, `lab3-awq`, `lab4-router`, `lab5-hpa`, `lab6-finops`) and a pre-warmed model cache so stragglers can fast-forward.
- **Pairing:** rotate pairs each day; pair a strong-infrastructure participant (Kubernetes/GPU) with a strong-ML participant (quantisation/quality). The skill transfer across that seam is the point of an Expert module.
- **GPU environment strategy:** primary = a shared classroom GPU pool (A100 80GB or L40S per pair) via the SDAIA training cluster; fallback = a single shared inference endpoint plus a CPU-only "quality-only" path for participants without a GPU seat. Verify quota and driver versions the week before; GPU scarcity is the #1 delivery risk.
- **Language:** deliver in English or Arabic; keep all code, identifiers, dashboards, and commit messages in English (production convention — mixed-language metric labels break Grafana queries and PromQL). Musaed's *content* is bilingual; its *operational tooling* is English.
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Use the trough in Musaed's own demand curve (prayer-time dip) as a teaching artefact when discussing autoscaling.
- **Assessment logistics:** collect each pair's `BENCHMARKS.md` and dashboard URL at the end of Day 3 Hour 4; rubric scoring happens live during Hour 5 before/after defences. Verify one claimed speed-up on the projector to deter number-fabrication.

---

# Module 1 — Performance Profiling of Inference Workloads

## Module Overview

**Purpose.** You cannot optimise what you have not measured, and most teams optimise the wrong thing because they measure the wrong number — average latency instead of tail latency, throughput at zero load instead of at the SLO, or GPU cost per hour instead of cost per served request. This module teaches participants to build a rigorous, reproducible performance and cost baseline of an LLM inference workload: the vocabulary (TTFT, TPOT, ITL, throughput, goodput), the measurement discipline (percentiles, warm-up, closed vs open loop), and the translation of latency and utilisation into Riyal.

**Business relevance.** A national assistant like Musaed answers millions of citizen queries. A 200 ms regression in time-to-first-token, multiplied across two million daily sessions, is felt by the public and shows up in abandonment metrics; a 15% drop in GPU efficiency is felt by the Treasury. In regulated and sovereign Saudi contexts, capacity planning and cost accountability are governance requirements, not engineering niceties — the baseline this module produces is the evidence every later optimisation is judged against.

**Industry use cases.**
- A government contact-centre assistant must hold TTFT p95 ≤ 800 ms during the salary-day surge, or citizens abandon the chat and flood the human call centre.
- A bank's document-analysis LLM is billed internally per team; without a per-request cost baseline, chargeback is impossible and the platform runs at a loss.
- A ministry procuring GPU capacity for a Hajj-season peak must know the true requests-per-GPU figure, or it over-provisions by 3× and wastes public funds.

**Expected competencies.** After this module a participant can instrument an inference service, generate representative load, report latency by percentile with correct methodology, compute throughput and GPU utilisation, and convert all of it into cost-per-1,000-requests and cost-per-million-tokens for Musaed.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Decompose LLM request latency into TTFT, TPOT, and end-to-end components | LO1 |
| 1.2 | Generate representative load and report latency by percentile with correct methodology | LO1 |
| 1.3 | Measure throughput, goodput, and GPU utilisation under increasing concurrency | LO1 |
| 1.4 | Convert latency, utilisation, and GPU price into cost-per-request and cost-per-token | LO1, LO5 |
| 1.5 | Produce a signed, reproducible baseline that later optimisations are measured against | LO1, LO6 |

## Technical Content

### 1. The latency–throughput–cost triangle

Every serving decision trades off three quantities, and you can rarely improve one without spending another:

- **Latency** — how fast a single user is served. For LLMs this is not one number.
- **Throughput** — how many requests (or tokens) the system serves per second across all users.
- **Cost** — the Riyal spent per unit of useful work, almost always dominated by GPU-hours.

The classic trap: raising batch size increases throughput (good, cheaper per token) but also raises per-request latency (bad). The engineer's job is not to maximise one corner but to find the operating point that meets the **latency SLO at the lowest cost**. Every module in this course moves Musaed around this triangle deliberately, with numbers.

### 2. Anatomy of LLM inference latency

Unlike a classifier that returns one score, an autoregressive LLM streams tokens, so latency has structure. Teach these four terms explicitly and never let participants collapse them into "latency":

| Term | Definition | What dominates it |
|---|---|---|
| **TTFT** (time to first token) | From request arrival to the first output token | The *prefill* phase: encoding the whole prompt in parallel; grows with prompt length and queue wait |
| **TPOT** (time per output token) | Average time to generate each subsequent token | The *decode* phase: one forward pass per token; dominated by memory bandwidth, not compute |
| **ITL** (inter-token latency) | The gap between two streamed tokens as the user perceives it | TPOT plus scheduling jitter |
| **E2E latency** | Total time to the last token | ≈ TTFT + (output_tokens − 1) × TPOT |

The two-phase structure (compute-bound **prefill**, memory-bandwidth-bound **decode**) is the single most important idea in LLM performance. It explains why long prompts hurt TTFT, why long answers hurt E2E through TPOT, and why the optimisations in later modules (batching helps decode throughput; caching skips prefill; quantisation shrinks the memory traffic that bounds decode) each target a *specific* phase.

### 3. Percentiles, warm-up, and honest measurement

Averages lie. For a service with a TTFT SLO, the p95 and p99 are the numbers citizens actually feel — the tail is where abandonment lives.

- **Report percentiles, not means.** A p50 of 300 ms with a p99 of 6 s is a broken service that a mean of 450 ms would hide.
- **Warm up first.** The first requests pay CUDA-graph capture, weight paging, and JIT costs. Discard a warm-up window (e.g., first 30 s) before recording.
- **Open loop vs closed loop.** A *closed-loop* generator (fixed number of clients, each waiting for a reply before sending the next) measures the system's natural throughput but hides queueing under overload. An *open-loop* generator (fixed arrival rate, independent of replies) reveals how latency explodes past the knee. Report which you used; they answer different questions.
- **Goodput, not just throughput.** Goodput = requests per second **that also met the SLO**. A system doing 400 req/s at p95 = 5 s (SLO 800 ms) has high throughput and near-zero goodput. Optimise goodput.

### 4. Throughput, concurrency, and the latency knee

Sweep concurrency and plot latency against throughput. You will always see the same shape:

- At low load, latency is flat and throughput rises linearly — you are paying for idle GPU.
- Near saturation, throughput plateaus while latency rises steeply — the **knee**.
- Past the knee, queues grow unbounded; latency diverges while throughput barely moves.

The right operating point sits just *below* the knee: maximum throughput while p95 still meets the SLO. Autoscaling (Module 5) exists to keep the system there as demand moves. Finding Musaed's knee is the core measurement of Lab 1.

### 5. From utilisation to Riyal: unit economics

The number executives care about is not milliseconds; it is **cost per 1,000 requests** (and its cousin, cost per 1M tokens). Derive it from first principles:

```
cost_per_1k_requests = (GPU_hourly_cost × num_GPUs) / (requests_per_second × 3600) × 1000
```

Worked example for baseline Musaed on one A100 80GB at an assumed sovereign-cloud rate of USD 2.20/hr (≈ SAR 8.25/hr):
- Baseline throughput at SLO: 22 req/s (single-request, no batching)
- cost/1k req = 8.25 / (22 × 3600) × 1000 = **SAR 0.104 per 1,000 requests**
- But GPU utilisation is only 31% — you are paying for a mostly-idle A100. Module 2 will lift throughput to ~140 req/s at the same SLO, cutting cost/1k by ~6×.

**GPU utilisation is a cost signal, not a vanity metric.** Low utilisation at high spend is money on fire; the baseline must record it. Note also that `nvidia-smi` "GPU-Util" is misleading for LLMs — it reports whether *any* kernel is running, not whether the GPU is doing useful FLOPs. Prefer memory-bandwidth utilisation and achieved tokens/s per GPU.

### 6. Common mistakes & production considerations

**Common mistakes (each appears in the Lab 1 starter harness deliberately)**
1. Reporting mean latency and hiding a catastrophic p99 tail.
2. No warm-up window — the first cold requests poison the numbers.
3. Closed-loop load at fixed 1 concurrency, then claiming "the system does 22 req/s" (it does 22 req/s *at that concurrency*, not at its knee).
4. Measuring TTFT but ignoring TPOT, so a fast-first-token but slow-streaming model looks great and reads terribly.
5. Quoting `nvidia-smi` utilisation as proof of efficiency.
6. Benchmarking with a fixed 32-token prompt when real Musaed prompts average 220 tokens — unrepresentative load produces unrepresentative conclusions.

**Production considerations**
- Baseline with **representative** traffic: real prompt-length and output-length distributions, real bilingual mix (Arabic tokenises to more tokens per word than English — this shifts TPOT cost).
- Capture the full context of a baseline: model version, quantisation, GPU type, vLLM version, batch settings, and the exact load profile. A baseline without its configuration is not reproducible and therefore worthless.
- Establish the baseline **once**, sign it (commit the numbers and the config), and treat regressions against it as incidents. Every later module re-runs the identical harness.

## Code Examples

### A representative load generator with correct percentile reporting

```python
# tools/loadgen.py
"""Open-loop load generator for Musaed. Sends requests at a fixed arrival
rate (Poisson) regardless of replies, so we can see the latency knee.
Reports TTFT and E2E by percentile after a warm-up window.
"""
import asyncio
import random
import time
from dataclasses import dataclass, field

import httpx
import numpy as np

ENDPOINT = "http://localhost:8000/v1/chat/completions"


@dataclass
class Sample:
    ttft_ms: float
    e2e_ms: float
    output_tokens: int
    ok: bool


@dataclass
class Results:
    samples: list[Sample] = field(default_factory=list)


async def one_request(client: httpx.AsyncClient, prompt: str, out: Results) -> None:
    """Stream a chat completion; record TTFT (first chunk) and E2E (last)."""
    body = {
        "model": "musaed",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 256,
        "stream": True,
    }
    t0 = time.perf_counter()
    ttft = None
    tokens = 0
    try:
        async with client.stream("POST", ENDPOINT, json=body, timeout=30) as r:
            async for line in r.aiter_lines():
                if not line.startswith("data:") or line.endswith("[DONE]"):
                    continue
                if ttft is None:
                    ttft = (time.perf_counter() - t0) * 1000  # first token arrived
                tokens += 1
        e2e = (time.perf_counter() - t0) * 1000
        out.samples.append(Sample(ttft, e2e, tokens, ok=True))
    except Exception:
        out.samples.append(Sample(0, 0, 0, ok=False))


async def run(rate_rps: float, duration_s: int, prompts: list[str]) -> Results:
    out = Results()
    async with httpx.AsyncClient() as client:
        tasks: list[asyncio.Task] = []
        deadline = time.perf_counter() + duration_s
        while time.perf_counter() < deadline:
            prompt = random.choice(prompts)
            tasks.append(asyncio.create_task(one_request(client, prompt, out)))
            # Poisson arrivals: inter-arrival ~ Exponential(rate)
            await asyncio.sleep(random.expovariate(rate_rps))
        await asyncio.gather(*tasks)
    return out


def report(out: Results, warmup_s: int = 30) -> None:
    ok = [s for s in out.samples if s.ok]
    ttft = np.array([s.ttft_ms for s in ok])
    e2e = np.array([s.e2e_ms for s in ok])
    def pct(a, p): return float(np.percentile(a, p)) if len(a) else float("nan")
    print(f"requests_ok={len(ok)}  errors={len(out.samples) - len(ok)}")
    print(f"TTFT  p50={pct(ttft,50):.0f}  p95={pct(ttft,95):.0f}  p99={pct(ttft,99):.0f} ms")
    print(f"E2E   p50={pct(e2e,50):.0f}  p95={pct(e2e,95):.0f}  p99={pct(e2e,99):.0f} ms")


if __name__ == "__main__":
    corpus = [l.strip() for l in open("data/musaed_prompts.txt", encoding="utf-8")]
    results = asyncio.run(run(rate_rps=40, duration_s=120, prompts=corpus))
    report(results)  # NOTE: production harness discards the first warmup_s of samples
```

### Turning the measurement into unit cost

```python
# tools/cost.py
"""Convert a benchmark result into the numbers executives read:
cost per 1k requests and cost per 1M tokens. All money in SAR.
"""
from dataclasses import dataclass

USD_TO_SAR = 3.75


@dataclass(frozen=True)
class GpuPrice:
    name: str
    usd_per_hour: float

    @property
    def sar_per_hour(self) -> float:
        return self.usd_per_hour * USD_TO_SAR


A100_80GB = GpuPrice("A100-80GB", 2.20)
H100_80GB = GpuPrice("H100-80GB", 3.90)
L40S = GpuPrice("L40S", 1.10)


def unit_costs(gpu: GpuPrice, num_gpus: int, req_per_s: float,
               avg_output_tokens: float, avg_input_tokens: float) -> dict:
    sar_per_s = gpu.sar_per_hour * num_gpus / 3600
    cost_per_1k_req = sar_per_s / req_per_s * 1000
    tokens_per_s = req_per_s * (avg_output_tokens + avg_input_tokens)
    cost_per_1m_tokens = sar_per_s / tokens_per_s * 1_000_000
    return {
        "gpu": gpu.name,
        "num_gpus": num_gpus,
        "req_per_s": round(req_per_s, 1),
        "sar_per_1k_requests": round(cost_per_1k_req, 4),
        "sar_per_1m_tokens": round(cost_per_1m_tokens, 2),
        "gpu_sar_per_hour": round(gpu.sar_per_hour, 2),
    }


if __name__ == "__main__":
    # Baseline Musaed: single A100, no batching, 22 req/s at SLO
    print(unit_costs(A100_80GB, num_gpus=1, req_per_s=22,
                     avg_output_tokens=256, avg_input_tokens=220))
    # -> sar_per_1k_requests ≈ 0.104 ; utilisation ~31% (recorded separately)
```

## Hands-on Lab 1 — Baseline Musaed

| | |
|---|---|
| **Objective** | Produce a signed, reproducible performance and cost baseline of the unoptimised Musaed service: TTFT/E2E percentiles, the throughput knee, GPU utilisation, and cost per 1,000 requests |
| **Duration** | 50 minutes |
| **Setup** | One GPU seat (A100 80GB or L40S), `git checkout lab1-baseline`, model cache pre-warmed, `pip install httpx numpy` |

**Instructions & tasks**

1. *(5 min)* Start the baseline service (`make serve-baseline` — a naive single-request HuggingFace `transformers` server, deliberately unbatched) and confirm `/health`.
2. *(10 min)* Run the load generator at a low rate (`--rate 5 --duration 90`); record warm vs cold behaviour and confirm your warm-up window discards the cold tail.
3. *(15 min)* Sweep the rate: 5, 10, 20, 30, 40 req/s. For each, capture TTFT p95, E2E p95, achieved req/s, and `nvidia-smi` memory-bandwidth utilisation. Find the **knee** — the highest rate where TTFT p95 ≤ 800 ms.
4. *(10 min)* Compute cost/1k requests and cost/1M tokens at the knee using `tools/cost.py` with the A100 price.
5. *(5 min)* Write the baseline row into `BENCHMARKS.md` (table below) and record the full config (model, GPU, server version, load profile).
6. *(5 min)* Commit: `bench: signed baseline for Musaed on A100 (unbatched)`.

**Expected output**
```
$ python tools/loadgen.py --rate 20 --duration 120
requests_ok=2287  errors=0
TTFT  p50=210  p95=640  p99=910 ms
E2E   p50=3120  p95=4980  p99=6240 ms
knee ≈ 22 req/s (TTFT p95 just under 800 ms); GPU mem-bw util ≈ 31%
cost ≈ SAR 0.104 / 1k requests  (single A100, unbatched)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| p99 wildly above p95 on first run | Cold start not discarded | Increase warm-up window; re-run |
| Throughput caps at ~1 req/s regardless of rate | Baseline server processes requests serially (by design) | This *is* the finding — it motivates Module 2's batching |
| GPU-Util reads 100% but tokens/s is low | `nvidia-smi` util is misleading for LLMs | Report achieved tokens/s and mem-bandwidth util instead |
| Arabic prompts slower than English | More tokens per word in Arabic tokenisation | Note it; keep the bilingual mix representative |

**Instructor notes.** The emotional beat of Lab 1 is the serial baseline: participants watch a 40 req/s arrival rate pile into a queue while the GPU sits at 31% useful utilisation. Do not fix it — that is Module 2. Have each pair announce their knee and cost/1k; write them on the shared leaderboard. The spread across pairs (same hardware, different load profiles) is itself a lesson in measurement discipline.

## Mini Exercises

**Quiz (5 questions)**
1. Which phase of LLM inference is compute-bound, and which is memory-bandwidth-bound? → prefill is compute-bound; decode is memory-bandwidth-bound.
2. A service reports mean latency 450 ms and meets its "sub-500 ms" target. Why might it still be failing users? → the mean hides the tail; p99 could be seconds.
3. Define goodput and explain how it differs from throughput. → requests/s that also met the SLO; throughput counts all completions regardless of SLO.
4. Why is open-loop load generation better for finding the knee than closed-loop? → open loop keeps arriving at a fixed rate, exposing unbounded queueing past saturation.
5. Write the formula for cost per 1,000 requests from GPU hourly cost and req/s. → (gpu_sar_per_hour × num_gpus) / (req_per_s × 3600) × 1000.

**Debugging exercise.** Give participants a benchmark script that computes latency as `mean(all_samples)` including a 20 s cold start and using closed-loop concurrency=1. Ask them to identify all three methodology errors and fix them.

**Calculation exercise.** Musaed runs on 4× A100 at 2.20 USD/hr, serving 160 req/s at the SLO, average 220 in + 256 out tokens. Compute cost/1k requests and cost/1M tokens. Then compute the same on 3× H100 at 3.90 USD/hr serving 300 req/s and argue which is cheaper per unit work.

**Discussion questions.**
- Your product manager wants "the latency number" for the SLA. Which single number do you give, and what do you insist on adding? (a percentile at a stated load, plus the phase breakdown)
- Arabic responses cost more per answer than English ones at equal word count. Is that a bug, a billing question, or both?

## Case Study — The Salary-Day Surge at a National Services Portal

**Scenario.** "Khadamati", a government citizen-services portal, launched an LLM assistant (an earlier incarnation of Musaed) that tested beautifully in the lab at 300 ms average latency. On the 27th of the month — salary day — traffic tripled within an hour and TTFT p95 climbed to 9 seconds; citizens abandoned the chat and the human call centre received 40,000 extra calls.

**Business context.** The lab benchmark used closed-loop concurrency=4 and reported a mean; it never found the knee, which sat at 24 req/s. Salary-day peak was 90 req/s. The service was three times past its knee with no autoscaling and no goodput metric.

**Technical challenge.** Reconstruct the true performance envelope, define an SLO in terms of a percentile at a stated load, and identify the cheapest lever to move the knee before next salary day.

**Constraints.** Two weeks to the next salary day; a fixed GPU budget increase of at most 50%; the model artefact may not be changed this cycle (a retrain needs risk sign-off); bilingual traffic must keep equal quality.

**Solution approach (facilitate, don't lecture).** (1) Rebuild the benchmark open-loop with representative prompts; publish the real knee. (2) Redefine the SLO as "TTFT p95 ≤ 800 ms at 90 req/s". (3) Recognise that a 50% GPU increase alone cannot close a 3.7× gap — serving optimisation (Module 2) must come first, then autoscaling (Module 5). (4) Instrument goodput so the next incident is visible in seconds, not from the call-centre.

**Discussion questions.**
1. Why did the lab benchmark give false confidence, and what one change would have exposed the risk?
2. Rank the available levers (more GPUs, batching, caching, smaller model, autoscaling) by cost-effectiveness for a two-week deadline.
3. What is the right SLO statement, and who must sign off on it?
4. How would a goodput dashboard have changed the incident timeline?

## Benchmarks and Evaluation

| Metric | Category | Target for the baseline | How measured |
|---|---|---|---|
| TTFT p95 | Latency | Recorded (SLO reference: ≤ 800 ms) | `loadgen.py` open-loop at the knee |
| E2E p95 | Latency | Recorded (SLO reference: ≤ 4 s for 256 tokens) | `loadgen.py` |
| Throughput knee | Throughput | Highest req/s with TTFT p95 ≤ 800 ms | rate sweep |
| GPU memory-bandwidth utilisation | Efficiency | Recorded (baseline typically low) | DCGM / `nvidia-smi dmon` |
| Cost per 1k requests | Cost | Recorded | `cost.py` at the knee |
| Baseline reproducibility | Rigour | Config committed with numbers | `BENCHMARKS.md` + git SHA |

**Example benchmark table (filled during lab):**

| Configuration | TTFT p95 | E2E p95 | Knee (req/s) | Mem-bw util | SAR / 1k req |
|---|---|---|---|---|---|
| Baseline (transformers, unbatched, A100) | 640 ms | 4,980 ms | 22 | 31% | 0.104 |
| *(targets for Module 2)* | ≤ 800 ms | ≤ 4,000 ms | ~140 | > 70% | ~0.017 |

## Required Visuals and Training Assets

### Diagrams
1. **The latency–throughput–cost triangle** — *Purpose:* anchor image for the whole course. *Elements:* a triangle with the three quantities at the corners, an operating point that moves; annotations showing "batching pushes toward throughput/cost, away from latency". *Style:* flat vector, English labels with Arabic subtitles.
2. **LLM latency anatomy timeline** — *Purpose:* make TTFT/TPOT/ITL concrete. *Elements:* a horizontal time axis from request arrival to last token; prefill block, then a series of decode ticks; TTFT and TPOT bracketed. *Style:* annotated timeline.
3. **The latency knee curve** — *Purpose:* teach the operating point. *Elements:* latency vs throughput curve with flat region, knee, and divergence; SLO line; the safe operating point marked. *Style:* labelled line chart.

### Images (screenshots)
1. **`loadgen.py` percentile output** — *why:* expected-output reference; *content:* the TTFT/E2E percentile block exactly as in the lab.
2. **DCGM/`nvidia-smi dmon` during a rate sweep** — *why:* shows utilisation vs achieved tokens/s divergence; *content:* GPU-util near 100% while tokens/s is modest.
3. **The shared leaderboard** — *why:* social proof of measurement discipline; *content:* each pair's knee and cost/1k.

### Simulations
1. **The serial-baseline pile-up** — *Setup:* the unbatched server under 40 req/s open loop. *Expected behaviour:* queue grows unbounded, E2E p99 diverges while GPU util stays ~31%. *Learning objective:* throughput is a system property, not a GPU property.
2. **The misleading mean** — *Setup:* a synthetic latency distribution with a fat tail. *Expected behaviour:* mean looks fine, p99 is 10× worse. *Learning objective:* always report percentiles.

### Interactive Activities
- **"Guess the knee" (10 min):** show a latency-vs-load curve with the axis labels hidden; pairs place the operating point, then reveal.
- **Unit-cost relay (10 min):** each pair converts a different (GPU, req/s) pair into cost/1k on the whiteboard; the class assembles a price ladder.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `musaed_prompts.txt` | Synthetic bilingual citizen queries (government-services domain, Arabic + English, realistic length distribution) | text (one prompt per line) | 5,000 prompts | Representative load for all labs |
| `musaed_traffic_profile.csv` | Synthetic 24-hour arrival-rate curve with salary-day and prayer-time features | CSV | 1,440 rows (per-minute) | Load shaping; reused in autoscaling (M5) |
| `baseline_signed.json` | Produced by reference solution | JSON | small | The signed baseline all optimisations are measured against |

### Demo Requirements
- **Instructor demo:** live rate sweep on the projector, calling out the knee as TTFT p95 crosses 800 ms; convert to cost/1k in real time.
- **Student demo:** one volunteer pair presents their knee and the config that produced it; the class challenges one methodology choice.
- **Expected outputs:** a committed baseline row, the config alongside it, and a screenshot of the percentile output.

---

# Module 2 — Serving Optimisation: Batching, Caching, Streaming

## Module Overview

**Purpose.** The baseline from Module 1 wastes most of the GPU because it serves one request at a time and re-computes everything from scratch. This module teaches the three highest-leverage serving optimisations that require no change to the model itself: **continuous batching** (fill the GPU with concurrent requests), **caching** (never re-compute what you have already computed — KV cache, PagedAttention, prefix cache, semantic cache), and **streaming** (return the first token immediately so perceived latency collapses). Applied together on Musaed, these lift throughput roughly 6× at the same SLO — the single largest cost win in the course, and the reason it comes first.

**Business relevance.** For a national assistant, serving-layer efficiency is the difference between running on 20 GPUs and running on 120. Continuous batching alone can raise GPU utilisation from ~30% to ~75%, and that ratio maps directly onto the monthly GPU bill. Streaming, meanwhile, changes the *perceived* speed citizens experience without changing total compute — a rare optimisation that improves experience and cost accounting simultaneously.

**Industry use cases.**
- A chat assistant with bursty traffic uses continuous batching so a request arriving mid-generation joins the running batch instead of waiting for it to finish.
- A RAG assistant whose prompts all begin with the same 1,500-token system preamble uses prefix caching to skip re-encoding it on every call, cutting TTFT by more than half.
- A customer-support bot with many repeated questions uses a semantic cache to answer common queries in single-digit milliseconds at near-zero GPU cost.

**Expected competencies.** After this module a participant can deploy Musaed on vLLM, explain PagedAttention and continuous batching, tune batching and KV-cache memory for a target SLO, enable prefix and semantic caching, serve tokens by streaming, and re-benchmark to prove the improvement against the signed baseline.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Explain continuous batching and PagedAttention and why they raise GPU utilisation | LO2 |
| 2.2 | Deploy an LLM on vLLM and tune batching / KV-cache memory for an SLO | LO2 |
| 2.3 | Apply prefix caching and semantic caching to skip redundant computation | LO2 |
| 2.4 | Implement token streaming and measure its effect on perceived latency | LO2 |
| 2.5 | Re-benchmark against the baseline and quantify the throughput and cost gain | LO2, LO1 |

## Technical Content

### 1. Why the baseline wastes the GPU

The Module 1 baseline processes requests serially: each request runs prefill, then decodes token-by-token to completion, and only then does the next request start. During the decode phase — which dominates wall-clock time — the GPU is memory-bandwidth-bound and its compute units sit mostly idle. Worse, requests that arrive during a generation must wait in a queue. The result is the pile-up participants observed in Lab 1: 31% useful utilisation while a queue grows. The fix is not a faster GPU; it is **keeping many requests in flight at once** so the idle compute is filled.

### 2. Static vs continuous (in-flight) batching

- **Static batching** collects N requests, runs them together, and returns when *all* finish. Its fatal flaw for LLMs: requests have different output lengths, so the whole batch waits for the slowest, and the batch cannot admit new arrivals until it drains. Short requests suffer head-of-line blocking behind long ones.
- **Continuous (in-flight) batching** — the vLLM default — schedules at the *token* level. Every decode step, the scheduler assembles a batch from all active requests; a request that finishes leaves immediately and its slot is filled by a waiting request in the very next step. There is no waiting for the batch to drain. This is the single most important serving optimisation for LLMs and typically delivers a 3–5× throughput gain over static batching at equal latency.

Teach the mental model: continuous batching turns "N sequential generations" into "one wide, continuously-refilled generation" that keeps the GPU's matrix units busy every step.

### 3. The KV cache and PagedAttention

During decode, the model must attend to every previous token, so it caches each token's key/value tensors — the **KV cache**. This cache is large (it grows with sequence length × layers × heads) and it is the real constraint on how many requests fit on a GPU: you run out of KV-cache memory long before you run out of compute.

Naive serving pre-allocates a contiguous KV buffer for each request's *maximum* possible length, wasting 60–80% of it (most answers are far shorter than max_tokens). **PagedAttention** (vLLM's core innovation) fixes this by treating KV memory like virtual memory in an operating system: the cache is split into fixed-size *blocks* allocated on demand, so memory is used only for tokens actually generated, and fragmentation nearly disappears. The practical payoff: 2–4× more concurrent requests on the same GPU, which is 2–4× more throughput.

`--gpu-memory-utilization` controls how much VRAM vLLM claims for weights + KV cache; higher values allow bigger batches but leave less headroom. This is a key tuning knob in Lab 2.

### 4. Prefix caching: skip the prompt you already encoded

Many Musaed requests share a long, identical prefix — a bilingual system prompt, safety instructions, and a fixed policy preamble (often 1,000–2,000 tokens). Without caching, every request re-runs prefill on that shared text, paying the TTFT cost each time. **Prefix caching** (also called automatic prefix caching or prompt caching) stores the KV cache of the shared prefix and reuses it across requests, so only the unique user turn needs prefill.

For Musaed, whose 1,500-token system preamble is identical on every call, prefix caching cuts TTFT by roughly half and frees prefill compute for real work. Enable with vLLM `--enable-prefix-caching`. The win scales with how long and how shared the prefix is — measure it.

### 5. Streaming and semantic caching

- **Streaming** returns tokens as they are generated (Server-Sent Events). It does not change total compute or E2E-to-last-token, but it collapses *perceived* latency: the user sees text at TTFT (~300 ms) instead of waiting for the full answer (~4 s). For a chat assistant this is transformational and effectively free. Always stream interactive LLM responses.
- **Semantic caching** goes further than prefix caching: it caches whole *answers* keyed by the *meaning* of the question (an embedding lookup with a similarity threshold). When a citizen asks "How do I renew my iqama?" and thousands of others ask the same thing in different words, the first answer is served from the model and the rest from the cache in single-digit milliseconds at near-zero GPU cost. The risk is a false-positive cache hit returning a subtly wrong answer, so the similarity threshold and a per-domain freshness policy must be tuned and monitored. Semantic caching is the bridge to Module 4's routing.

### 6. Common mistakes & production considerations

**Common mistakes**
1. Leaving `max_num_seqs` / batch limits at defaults, so the GPU never fills.
2. Setting `--gpu-memory-utilization` so high that a long-context request triggers KV-cache preemption and latency spikes.
3. Enabling prefix caching but then randomising the system prompt per request (timestamps, request IDs in the preamble) — defeating the cache.
4. Semantic cache with a loose threshold that returns confidently wrong answers.
5. Claiming a speed-up without re-running the *identical* Module 1 harness — apples to oranges.
6. Streaming enabled on the server but the client waits for the full body, throwing away the perceived-latency win.

**Production considerations**
- Continuous batching improves throughput but can raise *per-request* TTFT under load (a request may wait a scheduling step). Tune batch limits to protect the TTFT SLO, not to maximise raw throughput.
- Cache correctness is a governance concern: for a government assistant, a stale or mismatched cached answer can be a compliance issue. Version the cache with the model and the knowledge base; invalidate on update.
- Measure the win the honest way: re-run the exact Module 1 load profile and compare rows in the same `BENCHMARKS.md`.

## Code Examples

### Serving Musaed on vLLM with batching, prefix cache, and streaming

```bash
# scripts/serve_vllm.sh
# Musaed on vLLM: continuous batching + PagedAttention are ON by default.
# We explicitly enable prefix caching and tune KV-cache memory for the SLO.
python -m vllm.entrypoints.openai.api_server \
  --model /models/allam-13b-instruct \
  --served-model-name musaed \
  --dtype bfloat16 \
  --gpu-memory-utilization 0.90 \      # weights + KV cache share 90% of VRAM
  --max-num-seqs 256 \                 # max concurrent sequences in a batch
  --max-model-len 4096 \               # context budget; caps KV per request
  --enable-prefix-caching \            # reuse the shared bilingual system prompt
  --enable-chunked-prefill \           # interleave long prefills with decode -> smoother TTFT
  --port 8000
# Serves an OpenAI-compatible API at /v1/chat/completions with stream=True support.
```

### A semantic cache in front of the model

```python
# src/musaed/serving/semantic_cache.py
"""Answer-level cache keyed by question meaning. A hit avoids the GPU entirely.
Threshold and TTL are governance-sensitive: too loose -> wrong answers served.
"""
from __future__ import annotations
import time
from dataclasses import dataclass

import numpy as np


@dataclass
class Entry:
    embedding: np.ndarray
    answer: str
    model_version: str
    created_at: float


class SemanticCache:
    def __init__(self, embed_fn, threshold: float = 0.93, ttl_s: int = 3600):
        self._embed = embed_fn            # question -> unit-norm vector
        self._threshold = threshold       # cosine similarity to count as a hit
        self._ttl = ttl_s
        self._entries: list[Entry] = []

    def get(self, question: str, model_version: str) -> str | None:
        q = self._embed(question)
        now = time.time()
        best, best_sim = None, -1.0
        for e in self._entries:
            if now - e.created_at > self._ttl or e.model_version != model_version:
                continue                  # stale or wrong model version -> ignore
            sim = float(q @ e.embedding)  # both unit-norm -> dot == cosine
            if sim > best_sim:
                best, best_sim = e, sim
        if best is not None and best_sim >= self._threshold:
            return best.answer            # CACHE HIT: no GPU call
        return None

    def put(self, question: str, answer: str, model_version: str) -> None:
        self._entries.append(
            Entry(self._embed(question), answer, model_version, time.time()))
```

### Streaming client that records perceived latency

```python
# tools/stream_client.py
"""Demonstrates that streaming collapses PERCEIVED latency: TTFT ~300 ms
even though the full answer takes ~4 s. Compare to a non-streaming call.
"""
import time
import httpx

body = {"model": "musaed", "stream": True, "max_tokens": 256,
        "messages": [{"role": "user", "content": "كيف أجدد الإقامة؟"}]}

t0 = time.perf_counter()
first = None
with httpx.stream("POST", "http://localhost:8000/v1/chat/completions",
                  json=body, timeout=30) as r:
    for line in r.iter_lines():
        if line.startswith("data:") and not line.endswith("[DONE]"):
            if first is None:
                first = time.perf_counter() - t0
                print(f"first token visible to user at {first*1000:.0f} ms")
print(f"full answer at {(time.perf_counter()-t0)*1000:.0f} ms "
      f"(user was already reading since {first*1000:.0f} ms)")
```

## Hands-on Lab 2 — Optimise the Serving Layer

| | |
|---|---|
| **Objective** | Move Musaed from the unbatched baseline to a tuned vLLM stack with continuous batching, prefix caching, and streaming; re-run the Lab 1 harness and prove the throughput and cost gain |
| **Duration** | 2 × 50 min (Day 1 H5 + carry-over) or 1 × 50 min for strong cohorts |
| **Setup** | Lab 1 baseline row committed, `git checkout lab2-vllm`, GPU seat, `pip install vllm` (or pre-built image), model cached at `/models/allam-13b-instruct` |

**Instructions & tasks**
1. *(10 min)* Launch vLLM with `scripts/serve_vllm.sh` (defaults on). Re-run the **identical** Lab 1 load profile at the old knee rate; observe throughput headroom.
2. *(10 min)* Sweep `--max-num-seqs` (32, 128, 256) and `--gpu-memory-utilization` (0.85, 0.90, 0.95). Find the new knee where TTFT p95 ≤ 800 ms; watch for KV-cache preemption warnings at the high end.
3. *(10 min)* Enable `--enable-prefix-caching`; confirm the shared 1,500-token system prompt is cached and measure the TTFT drop.
4. *(10 min)* Enable streaming in the client; record first-token-visible vs full-answer time. Put a `SemanticCache` in front for a set of repeated FAQ prompts and measure hit-rate and cost impact.
5. *(5 min)* Compute the new cost/1k requests and write the optimised row into `BENCHMARKS.md` beside the baseline.
6. *(5 min)* Commit: `perf(serve): vLLM continuous batching + prefix cache + streaming (6x throughput)`.

**Expected output**
```
$ python tools/loadgen.py --rate 130 --duration 120   # same harness as Lab 1
TTFT  p50=180  p95=760  p99=980 ms
E2E   p50=2400 p95=3900 p99=4700 ms
new knee ≈ 140 req/s ; GPU mem-bw util ≈ 74%
prefix cache: TTFT p95 640 -> 300 ms on shared-preamble prompts
cost ≈ SAR 0.017 / 1k requests  (down from 0.104 baseline -> ~6x cheaper)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Throughput barely improves | `max_num_seqs` still tiny or KV cache too small | Raise `--max-num-seqs`; raise `--gpu-memory-utilization` toward 0.9 |
| Latency spikes intermittently | KV-cache preemption at high mem-util | Lower `--gpu-memory-utilization` or `--max-model-len` |
| Prefix cache shows no gain | System prompt varies per request | Remove per-request tokens (timestamps/IDs) from the preamble |
| Semantic cache returns wrong answer | Threshold too low | Raise threshold; add model-version + TTL guard (already in code) |

**Instructor notes.** The payoff moment is the side-by-side `BENCHMARKS.md`: same hardware, same load profile, ~6× cheaper. Insist that participants re-run the *identical* harness — a pair that changes the prompt set and reports a bigger number has committed the cardinal sin of the course. Fast finishers: measure how the win shrinks when the shared prefix is removed, to internalise *why* prefix caching helped.

## Mini Exercises

**Quiz (5 questions)**
1. Why does continuous batching beat static batching for LLMs? → token-level scheduling; finished requests leave immediately and new ones join without draining the batch, eliminating head-of-line blocking.
2. What resource, not compute, usually limits how many requests fit on a GPU? → KV-cache memory.
3. What problem does PagedAttention solve? → KV-cache fragmentation/over-allocation; it allocates cache in on-demand blocks, fitting 2–4× more requests.
4. When does prefix caching help most? → when a long prefix is identical across many requests (shared system prompt).
5. Does streaming reduce total compute? → no; it reduces *perceived* latency by delivering the first token early.

**Debugging exercise.** A pair reports "prefix caching gave us nothing." Their preamble embeds `Current time: {now}`. Explain the miss and fix it.

**Design exercise.** Musaed's traffic is 35% repeated FAQ questions. Design a two-layer cache (semantic answer cache + prefix cache) and estimate the GPU-cost reduction if the semantic cache achieves a 30% hit rate at near-zero cost per hit.

**Discussion questions.**
- Continuous batching can raise per-request TTFT under load. How do you set batch limits to protect the SLO rather than chase raw throughput?
- For a government assistant, what governance controls must wrap a semantic cache before you dare enable it?

## Case Study — The RAG Assistant That Paid for Its Preamble Twice a Second

**Scenario.** "Dalil", a ministry RAG assistant, prepends a 1,800-token bilingual system prompt (policy, safety, formatting rules) to every request. At 120 req/s it re-encoded that preamble 120 times a second, burning prefill compute and pushing TTFT p95 to 1.9 s — over its 800 ms SLO — while paying for a second GPU it did not truly need.

**Business context.** The preamble was 88% of the average prompt's tokens. Prefill on the preamble alone consumed the majority of GPU time. The team's proposed fix was "buy more GPUs".

**Technical challenge.** Cut TTFT under the SLO and reclaim a GPU without touching the model or the preamble content.

**Constraints.** The preamble cannot be shortened (legal sign-off); the knowledge base updates nightly; answers must remain grounded and current.

**Solution approach (facilitate, don't lecture).** (1) Enable prefix caching so the 1,800-token preamble is encoded once and reused — TTFT p95 falls from 1.9 s to 700 ms. (2) Add chunked prefill to smooth TTFT under bursts. (3) Add a semantic answer cache for the top-200 repeated questions, invalidated on the nightly KB update, cutting GPU load 25%. (4) Re-benchmark: one GPU retired, SLO met.

**Discussion questions.**
1. Why is "buy more GPUs" the wrong first move here?
2. How does the nightly KB update constrain the semantic cache design?
3. What single log field would let you monitor prefix-cache hit rate in production?
4. If the preamble contained a per-request timestamp, what would you change?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Throughput knee | Throughput | ≥ 6× baseline at same SLO (~140 req/s) | re-run Lab 1 harness |
| GPU mem-bandwidth utilisation | Efficiency | > 70% | DCGM |
| TTFT p95 with prefix cache | Latency | ≤ 400 ms on shared-preamble prompts | `loadgen.py` |
| Semantic cache hit rate | Efficiency | ≥ 25% on FAQ-heavy traffic | cache counters |
| Cost per 1k requests | Cost | ~SAR 0.017 (≈ 6× cheaper) | `cost.py` |
| Perceived first-token time (streaming) | UX | ≤ 350 ms | `stream_client.py` |

**Example benchmark table (filled during lab):**

| Configuration | Knee (req/s) | TTFT p95 | Mem-bw util | SAR / 1k req |
|---|---|---|---|---|
| Baseline (unbatched) | 22 | 640 ms | 31% | 0.104 |
| vLLM continuous batching | 120 | 780 ms | 71% | 0.019 |
| + prefix cache + streaming | 140 | 300 ms* | 74% | 0.017 |

\* on shared-preamble prompts

## Required Visuals and Training Assets

### Diagrams
1. **Static vs continuous batching** — *Purpose:* the module's core idea. *Elements:* two timelines; static batch waits for the slowest to drain, continuous batch refills slots every step; idle GPU shaded. *Style:* before/after split panel.
2. **PagedAttention memory blocks** — *Purpose:* explain the KV-cache win. *Elements:* contiguous over-allocated buffers vs on-demand blocks; freed blocks recycled. *Style:* OS-virtual-memory analogy diagram.
3. **Prefix cache reuse** — *Purpose:* motivate shared-prompt caching. *Elements:* many requests sharing one cached preamble KV block, only the unique turn re-encoded. *Style:* fan-in diagram.

### Images (screenshots)
1. **vLLM startup log** — *why:* confirms batching/prefix-cache flags; *content:* the served-model line and KV-cache block count.
2. **Before/after `BENCHMARKS.md` diff** — *why:* the honest comparison; *content:* baseline row beside vLLM row on the same harness.
3. **Streaming vs non-streaming timeline** — *why:* perceived-latency win; *content:* first-token-visible marker far left of full-answer marker.

### Simulations
1. **KV-cache preemption** — *Setup:* `--gpu-memory-utilization 0.97` under long-context load. *Expected behaviour:* preemption warnings, latency spikes. *Learning objective:* headroom matters; the highest mem-util is not the best.
2. **Prefix-cache defeat** — *Setup:* inject a timestamp into the preamble. *Expected behaviour:* prefix-cache hit rate collapses to ~0. *Learning objective:* cache keys must be stable.

### Interactive Activities
- **Batch-slot game (10 min):** participants physically play requests joining/leaving a continuous batch each "tick"; contrast with static batching where all wait.
- **Cache-or-compute sort (10 min):** cards of request types (identical FAQ, unique long-form, sensitive personal) sorted into semantic-cache / prefix-cache / always-compute buckets with a rationale.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `musaed_faq_prompts.txt` | Synthetic repeated citizen FAQs with paraphrases | text | 200 canonical × 20 paraphrases | Semantic-cache hit-rate measurement |
| `musaed_system_prompt.txt` | The fixed 1,500-token bilingual preamble | text | ~1,500 tokens | Prefix-cache demonstration |

### Demo Requirements
- **Instructor demo:** launch vLLM, re-run the baseline harness live, and show the throughput jump on the same axes as Module 1.
- **Student demo:** a pair shows their streaming client — first token on screen while the answer is still generating.
- **Expected outputs:** the optimised `BENCHMARKS.md` row, a prefix-cache TTFT drop, and a non-zero semantic-cache hit rate.

---

# Module 3 — Model Compression: Quantisation and Distillation

## Module Overview

**Purpose.** Serving optimisation filled the GPU; compression shrinks what has to fit in it. This module teaches participants to reduce a model's memory and compute footprint without unacceptable quality loss: **quantisation** (representing weights and activations in fewer bits — FP16→INT8→INT4) and **distillation** (training a small "student" model to imitate a large "teacher"). Quantising Musaed's 13B model to INT4 roughly quarters its weight memory, letting it run on a smaller GPU or fit far more KV cache, while a distilled 3B student can handle the easy majority of traffic. The discipline that separates an Expert from an amateur is the **quality gate**: no compression ships without a measured quality comparison against the full-precision baseline.

**Business relevance.** Weight memory is destiny for GPU choice. A 13B model in BF16 needs ~26 GB just for weights, forcing an 80 GB-class GPU; the same model in INT4 needs ~7 GB and runs comfortably on a 24 GB L40S or even an A10, which can be a third of the hourly cost. For a national deployment, choosing the right precision is a multi-million-Riyal decision. But quality regressions in a government assistant are a public-trust risk — hence the gate.

**Industry use cases.**
- A bank quantises a 70B model to INT4 to fit a single GPU instead of a two-GPU tensor-parallel setup, halving serving cost.
- A telecom distils its large intent-classification LLM into a 1B student that runs on CPU at the edge for offline retail kiosks.
- A ministry ships an FP8 version of its assistant on H100s, gaining throughput from native FP8 tensor cores with negligible quality loss.

**Expected competencies.** After this module a participant can choose a precision format for a hardware target, quantise Musaed with AWQ/GPTQ, explain distillation and when to use it, run a rigorous quality gate (task accuracy + regression + bilingual quality), and decide whether the compressed model ships.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Compare precision formats (FP16/BF16/FP8/INT8/INT4) by memory, speed, and quality | LO3 |
| 3.2 | Quantise an LLM with AWQ/GPTQ and measure memory and throughput gains | LO3 |
| 3.3 | Explain knowledge distillation and when a small student beats a quantised teacher | LO3 |
| 3.4 | Design and run a quality gate that a compressed model must pass to ship | LO3, LO1 |
| 3.5 | Recommend a precision/model choice for a given GPU and budget | LO3, LO5 |

## Technical Content

### 1. Why fewer bits means less cost

An LLM's parameters are numbers. Store each in 16 bits (BF16) and a 13B model needs ~26 GB; store each in 4 bits (INT4) and it needs ~7 GB. Two things follow:

- **Memory:** the model fits on a cheaper, smaller GPU, or leaves far more room for KV cache (more concurrent requests → more throughput → lower cost per request).
- **Speed:** decode is memory-bandwidth-bound (Module 1). Fewer bits per weight means fewer bytes moved per token, so decode gets faster — often 1.5–2× on the same GPU. Compression is thus a *latency* optimisation as well as a memory one.

The catch is quality: fewer bits means coarser numbers, and past a point the model degrades. The art is finding the lowest precision that still passes the gate.

### 2. Precision formats and where each fits

| Format | Bits | Weight mem (13B) | Typical use | Quality risk |
|---|---|---|---|---|
| **FP32** | 32 | ~52 GB | training only | none (baseline) |
| **FP16 / BF16** | 16 | ~26 GB | standard serving default | negligible |
| **FP8** | 8 | ~13 GB | H100/L40S native tensor cores | very low |
| **INT8** | 8 | ~13 GB | broad GPU support (SmoothQuant) | low |
| **INT4** | 4 | ~7 GB | max compression (AWQ/GPTQ) | low–moderate, must gate |

Guidance to teach: default to BF16; move to FP8 on Hopper/Ada GPUs for a nearly-free win; go INT4 when memory or cost pressure is real and the gate passes. INT4 is where quality risk becomes material — never ship it ungated.

### 3. Post-training quantisation: AWQ and GPTQ

**Post-training quantisation (PTQ)** compresses an already-trained model without retraining — fast, cheap, and the default path. Two methods dominate:

- **GPTQ** quantises layer by layer, using a small calibration dataset and second-order (Hessian) information to choose quantised values that minimise output error. Strong at INT4, widely supported.
- **AWQ (Activation-aware Weight Quantisation)** observes that a small fraction of weights (those multiplying large activations) matter disproportionately, and protects them while quantising the rest aggressively. Often better quality at INT4 and faster to apply. AWQ is the course default for Musaed.

Both need a **calibration set** — a few hundred representative samples (for Musaed: bilingual citizen queries, so the quantisation "sees" Arabic). Calibrating on English-only text and then serving Arabic is a classic mistake that shows up as Arabic-specific degradation. **Quantisation-aware training (QAT)**, which simulates quantisation *during* training for the best quality, exists but is expensive; teach it as the option of last resort when PTQ fails the gate.

### 4. Knowledge distillation

Quantisation shrinks the *representation* of a fixed model; **distillation** trains a *different, smaller* model. A large **teacher** (the 13B Musaed) generates outputs — either final answers or full probability distributions ("soft labels") — and a small **student** (e.g., 3B) is trained to imitate them. The student learns the teacher's behaviour on the target domain far better than training from scratch would allow.

When to distil rather than quantise:
- You need a model *much* smaller than quantisation can reach (e.g., a 1–3B model for edge or CPU).
- You have a well-defined task distribution (Musaed's government-services domain) so the student need not be a generalist.
- You can afford a training run and have teacher-generated data.

In practice the two combine: distil to a smaller student, then quantise the student. And distillation feeds Module 4 directly — the small student becomes the cheap first tier of the routing cascade.

### 5. The quality gate: the non-negotiable

No compressed model ships without passing a gate that compares it to the full-precision baseline on:

- **Task quality:** domain accuracy on a held-out Musaed evaluation set (e.g., answer-correctness judged by an LLM-as-judge or human labels), reported as absolute score and delta vs baseline.
- **Bilingual parity:** Arabic and English scored separately — compression often hurts the lower-resource language more.
- **Regression / behavioural checks:** safety refusals still fire; formatting rules hold; no new hallucination on a fixed probe set.
- **Performance:** the memory, throughput, and cost gains that justified the compression, measured on the same harness.

Define the pass threshold *before* quantising (e.g., "≤ 1.5 point drop in answer-correctness, no safety regression, Arabic delta ≤ English delta + 1 point"). A gate defined after seeing the numbers is not a gate. If INT4 fails, step up to INT8 or FP8; document the decision.

### 6. Common mistakes & production considerations

**Common mistakes**
1. Calibrating quantisation on English-only data, then degrading on Arabic.
2. Reporting a speed-up but never measuring quality — "it's 2× faster and probably fine".
3. Defining the quality threshold after seeing results.
4. Distilling on teacher outputs that were themselves wrong (garbage-in) with no filtering.
5. Comparing INT4 throughput on one GPU against BF16 on another — confounded benchmark.
6. Forgetting that quantisation can change safety behaviour (a compressed model may refuse less reliably).

**Production considerations**
- Version the quantised artefact with its method, bit-width, calibration set, and gate results — this is audit evidence.
- Re-run the gate whenever the base model or knowledge base changes; compression quality is not a one-time property.
- Match precision to hardware: FP8 is nearly free on H100/L40S but unsupported on older GPUs; INT4 (AWQ) runs broadly. The right answer depends on the fleet you actually have (Module 5).

## Code Examples

### Quantising Musaed to INT4 with AWQ, calibrated on bilingual data

```python
# scripts/quantize_awq.py
"""AWQ INT4 quantisation of the 13B Musaed model.
Calibration MUST include Arabic + English, or Arabic quality suffers.
"""
from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

MODEL = "/models/allam-13b-instruct"
OUT = "/models/allam-13b-awq-int4"

model = AutoAWQForCausalLM.from_pretrained(MODEL, safetensors=True)
tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)

# Bilingual calibration set: ~512 representative citizen queries (AR + EN).
calib = [l.strip() for l in open("data/calibration_bilingual.txt", encoding="utf-8")]

quant_config = {
    "zero_point": True,
    "q_group_size": 128,   # granularity: smaller groups -> better quality, larger files
    "w_bit": 4,            # INT4 weights
    "version": "GEMM",
}
model.quantize(tok, quant_config=quant_config, calib_data=calib)
model.save_quantized(OUT)
tok.save_pretrained(OUT)
print(f"Saved AWQ-INT4 model to {OUT}")
# Serve it: vLLM --model /models/allam-13b-awq-int4 --quantization awq
```

### The quality gate

```python
# eval/quality_gate.py
"""A compressed model ships only if it passes this gate vs the FP baseline.
Thresholds are defined BEFORE running. Arabic and English scored separately.
"""
from dataclasses import dataclass


@dataclass
class GateResult:
    metric: str
    baseline: float
    candidate: float

    @property
    def delta(self) -> float:
        return self.candidate - self.baseline


# --- thresholds fixed in advance ---
MAX_DROP = 1.5            # points of answer-correctness allowed
MAX_LANG_GAP = 1.0       # Arabic may drop at most 1 pt more than English
SAFETY_MUST_HOLD = True  # zero new safety regressions


def evaluate(gate: dict[str, GateResult], safety_regressions: int) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    ok = True
    for name in ("correctness_en", "correctness_ar"):
        if -gate[name].delta > MAX_DROP:
            ok = False
            reasons.append(f"{name} dropped {-gate[name].delta:.2f} > {MAX_DROP}")
    lang_gap = (-gate["correctness_ar"].delta) - (-gate["correctness_en"].delta)
    if lang_gap > MAX_LANG_GAP:
        ok = False
        reasons.append(f"Arabic degraded {lang_gap:.2f} pt more than English")
    if SAFETY_MUST_HOLD and safety_regressions > 0:
        ok = False
        reasons.append(f"{safety_regressions} safety regressions")
    return ok, reasons


if __name__ == "__main__":
    results = {
        "correctness_en": GateResult("correctness_en", 82.4, 81.6),
        "correctness_ar": GateResult("correctness_ar", 79.1, 77.9),
    }
    passed, why = evaluate(results, safety_regressions=0)
    print("GATE:", "PASS" if passed else "FAIL", why)
```

## Hands-on Lab 3 — Quantise Musaed

| | |
|---|---|
| **Objective** | Quantise the 13B Musaed model to INT4 with AWQ, measure the memory/throughput/cost gains on the standard harness, run the quality gate, and decide whether it ships |
| **Duration** | 50 minutes |
| **Setup** | `git checkout lab3-awq`, GPU seat, `pip install autoawq vllm`, bilingual calibration and eval sets provided, FP16 baseline quality scores from the solution repo |

**Instructions & tasks**
1. *(10 min)* Quantise with `scripts/quantize_awq.py` (a pre-baked artefact is provided as fallback if time-constrained). Record weight memory before/after (~26 GB → ~7 GB).
2. *(10 min)* Serve the INT4 model on vLLM (`--quantization awq`); re-run the standard load harness. Record the new knee, mem-bw util, and decode tokens/s vs the BF16 vLLM row from Lab 2.
3. *(10 min)* Run `eval/quality_gate.py` against the FP16 baseline: answer-correctness EN and AR, safety probe set. Record the deltas.
4. *(10 min)* Make the call: does INT4 pass? If it fails on Arabic, re-quantise INT8 (provided) and compare. Write the decision and evidence.
5. *(5 min)* Compute cost/1k on a smaller GPU (L40S) now that the model fits; write the row.
6. *(5 min)* Commit: `perf(model): AWQ-INT4 with bilingual gate (fits L40S, -55% cost)`.

**Expected output**
```
weight memory: 26.1 GB (BF16) -> 7.2 GB (INT4 AWQ)
decode: 41 tok/s -> 68 tok/s per request ; knee 140 -> 165 req/s (A100)
GATE: PASS  correctness_en 82.4->81.6 (-0.8)  correctness_ar 79.1->77.9 (-1.2)
now fits L40S (24GB): cost ≈ SAR 0.008 / 1k req  (vs 0.017 on A100 BF16)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Arabic quality drops far more than English | English-only calibration | Re-calibrate with the bilingual set |
| Quantised model slower than expected | Kernel/GPU mismatch for the quant format | Confirm vLLM `--quantization awq` and a supported GPU |
| Gate fails INT4 | Too aggressive for this model | Step up to INT8/FP8; document the trade |
| Out-of-memory during quantisation | AWQ needs headroom | Use the provided pre-quantised artefact or a bigger calibration GPU |

**Instructor notes.** The teachable tension is memory vs quality: participants *want* INT4's cost win but must respect the gate. Seed one pair's cohort with an English-only calibration so the Arabic regression appears — then debug it publicly. This is the module's thesis: compression is a quality-governed decision, not a free lunch.

## Mini Exercises

**Quiz (5 questions)**
1. Why does quantisation speed up decode, not just save memory? → decode is memory-bandwidth-bound; fewer bits per weight = fewer bytes moved per token.
2. What does AWQ protect that plain rounding does not? → the salient weights that multiply large activations.
3. Why must the calibration set be bilingual for Musaed? → otherwise Arabic (unseen during calibration) degrades.
4. When would you distil rather than quantise? → when you need a model much smaller than quantisation reaches, on a defined domain.
5. Why define the quality-gate threshold before quantising? → a threshold chosen after seeing results is not an objective gate.

**Calculation exercise.** A 13B model needs ~2 bytes/param in BF16. Compute weight memory in BF16, INT8, and INT4, and state the smallest GPU class each fits given ~40% KV/overhead headroom.

**Design exercise.** Sketch a distillation plan to produce a 3B Musaed student: teacher, data source, filtering of teacher errors, and the gate the student must pass to become the cheap tier in Module 4's cascade.

**Discussion questions.**
- Compression can weaken safety refusals. How does that change the gate for a government assistant?
- FP8 is "nearly free" on H100 but unsupported on your older A100 fleet. How does your hardware inventory change the precision decision?

## Case Study — The INT4 Assistant That Forgot Its Arabic

**Scenario.** A team quantised a bilingual assistant to INT4 to cut cost, calibrated (out of habit) on an English instruction dataset, and shipped after checking English quality only. Arabic answer-correctness quietly fell 6 points; complaints rose from Arabic-first citizens two weeks later.

**Business context.** The cost win was real (55% cheaper) but the quality regression was invisible to a monolingual gate. For a national service, degraded Arabic is a public-trust failure, not a metric wobble.

**Technical challenge.** Recover Arabic quality while keeping most of the cost win.

**Constraints.** The cost target must hold within 10%; a full QAT run is too slow for the release window; the base model is fixed this cycle.

**Solution approach (facilitate, don't lecture).** (1) Re-calibrate AWQ on a bilingual set — Arabic recovers ~4 of the 6 points. (2) For the residual, raise the most sensitive layers to INT8 (mixed precision), recovering the rest at a small memory cost. (3) Institute a bilingual, safety-inclusive gate as a mandatory CI step so no future compression ships monolingually. (4) Re-benchmark: cost target held, Arabic within threshold.

**Discussion questions.**
1. What single process change would have prevented the incident?
2. Why did an English-only gate give false confidence?
3. When is mixed-precision worth its extra complexity?
4. How do you make a bilingual quality gate a hard release requirement?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Weight memory | Efficiency | ≤ 8 GB (INT4) | model file / GPU memory report |
| Decode tokens/s per request | Latency | ≥ 1.5× BF16 | harness |
| Answer-correctness delta (EN & AR) | Quality | within gate threshold (≤ 1.5 pt drop) | quality gate |
| Bilingual parity | Quality | Arabic delta ≤ English delta + 1 pt | quality gate |
| Safety regressions | Quality | 0 | safety probe set |
| Cost per 1k requests | Cost | further reduced by fitting a smaller GPU | `cost.py` |

**Example benchmark table (filled during lab):**

| Model | Precision | Weight mem | Fits GPU | Correctness EN/AR | SAR / 1k req |
|---|---|---|---|---|---|
| Musaed 13B | BF16 | 26.1 GB | A100 80GB | 82.4 / 79.1 | 0.017 |
| Musaed 13B | INT4 AWQ | 7.2 GB | L40S 24GB | 81.6 / 77.9 | 0.008 |
| Musaed 13B | INT8 | 13.3 GB | A100 / L40S | 82.2 / 78.9 | 0.011 |

## Required Visuals and Training Assets

### Diagrams
1. **Precision ladder** — *Purpose:* map bits to memory, speed, quality. *Elements:* FP32→BF16→FP8→INT8→INT4 rungs with memory and quality-risk annotations; the "gate line" below which you must test. *Style:* vertical ladder.
2. **AWQ salient-weight protection** — *Purpose:* explain why AWQ beats naive rounding. *Elements:* weight matrix with a few highlighted salient columns kept precise, rest quantised. *Style:* matrix heatmap.
3. **Quantise vs distil decision tree** — *Purpose:* choose the right tool. *Elements:* branches on target size, domain breadth, training budget. *Style:* decision tree.

### Images (screenshots)
1. **GPU memory before/after quantisation** — *why:* the memory win made visible; *content:* `nvidia-smi` showing 26 GB → 7 GB.
2. **Quality-gate output** — *why:* the ship/no-ship decision; *content:* PASS/FAIL with per-language deltas.
3. **Mixed-precision layer config** — *why:* the Arabic-recovery fix; *content:* the layer→precision map.

### Simulations
1. **Monolingual-calibration regression** — *Setup:* calibrate on English only. *Expected behaviour:* Arabic correctness drops sharply while English holds. *Learning objective:* calibration must match serving distribution.
2. **Over-aggressive INT4** — *Setup:* quantise a small model to INT4 with tiny group size. *Expected behaviour:* gibberish/gate failure. *Learning objective:* there is a floor; the gate catches it.

### Interactive Activities
- **Set-the-gate workshop (15 min):** pairs write the pass/fail thresholds for Musaed *before* seeing any numbers, then defend them.
- **Precision auction (10 min):** given a GPU budget, teams "buy" precision/quality trade-offs and justify the choice.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `calibration_bilingual.txt` | Synthetic AR+EN citizen queries | text | 512 samples | AWQ/GPTQ calibration |
| `musaed_eval.jsonl` | Held-out Q/A with reference answers, AR+EN, safety probes | JSONL | 400 items | Quality gate |
| `allam-13b-awq-int4/` | Pre-quantised artefact (fallback) | safetensors | ~7 GB | Time-boxed labs |

### Demo Requirements
- **Instructor demo:** quantise a small model live (or load the artefact), show the memory drop and run the gate on the projector.
- **Student demo:** a pair presents their ship/no-ship decision with the per-language deltas.
- **Expected outputs:** a quantised artefact, a recorded gate result, and a cost row on a smaller GPU.

---

# Module 4 — Model Routing and Cascade Architectures

## Module Overview

**Purpose.** Not every citizen question needs the 13B model. "What are the working hours?" and "Explain the appeal process for a rejected visa application, citing the relevant regulation" cost the same on a single big model — which is wasteful. This module teaches participants to route each request to the cheapest model that can answer it well: **complexity routing** (a fast classifier picks a tier), **cascades** (try a small model first, escalate only if its confidence is low), and **semantic caching as tier zero**. Done right on Musaed, routing sends the easy majority to a small/cheap model and reserves the expensive model for the hard minority, cutting blended cost 40–60% while holding quality.

**Business relevance.** Traffic to a national assistant is heavily skewed: a large share is repeated, simple FAQ. Paying flagship-model prices for a question a 1B model answers perfectly is pure waste multiplied by millions of requests. Routing is the lever with the best cost-per-engineering-day ratio once serving and compression are done, and it composes with everything before it (the distilled/quantised student from Module 3 becomes the cheap tier here).

**Industry use cases.**
- A support platform routes FAQ to a semantic cache, routine queries to a 3B model, and complex reasoning to a 70B model — one blended endpoint, three cost tiers.
- A coding assistant sends autocomplete to a tiny fast model and "explain this bug" to a large one.
- A document service uses a cascade: a cheap model drafts, and only low-confidence drafts are re-run by the expensive model (verify-and-escalate).

**Expected competencies.** After this module a participant can design a multi-tier routing policy, implement a complexity router and a confidence-based cascade, measure deflection rate and blended cost, guard quality with an escalation policy, and reason about the accuracy/cost frontier.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Design a multi-tier serving topology (cache → small → large) for a workload | LO3, LO5 |
| 4.2 | Implement a complexity/intent router that assigns requests to tiers | LO3 |
| 4.3 | Implement a confidence-based cascade with an escalation policy | LO3 |
| 4.4 | Measure deflection rate, escalation rate, and blended cost | LO3, LO1 |
| 4.5 | Evaluate routing on the quality/cost frontier and tune the threshold | LO3, LO5 |

## Technical Content

### 1. The insight: match model cost to request difficulty

A single-model deployment charges the same for every request regardless of difficulty. But requests are not equally hard, and models are not equally expensive. If you can *cheaply* estimate difficulty and route accordingly, you pay flagship prices only for flagship-hard requests. The economics are compelling because traffic is skewed: when 70% of requests are easy, moving them to a model that is 10× cheaper cuts blended cost dramatically even if the remaining 30% still use the expensive model.

Three routing patterns, from simplest to smartest:
- **Semantic cache (tier 0):** identical/paraphrased repeats answered with no model at all (Module 2).
- **Complexity routing (predict then route):** a fast classifier reads the request and picks a tier *before* generating.
- **Cascade (generate then verify):** the cheap model answers first; a confidence signal decides whether to accept or escalate to the expensive model.

### 2. Complexity routing

A lightweight router — a small classifier, an embedding-based scorer, or even a rules+heuristics layer — labels each incoming request with a difficulty/intent class and maps it to a tier. Signals it can use: prompt length, presence of reasoning keywords ("compare", "explain why", "cite"), detected intent (FAQ lookup vs multi-step reasoning), and required tools (retrieval, calculation).

Trade-off: routing must be *much* cheaper than the models it routes between, or it eats its own savings. A 20-ms embedding classifier deciding between a 3B and a 13B model is a good ratio; calling a 13B model to decide whether to call a 13B model is not. The router itself is on the latency critical path, so keep it fast.

The failure mode is **mis-routing**: sending a hard question to the small model, which answers confidently but wrongly. Complexity routing alone has no safety net for this — which is why cascades exist.

### 3. Cascades: generate-then-verify with escalation

A cascade tries the cheap model first and escalates only when needed. The core question is: *how do you know the cheap answer is good enough?* Options for the confidence signal:

- **Model self-confidence:** token log-probabilities / sequence likelihood; low confidence → escalate. Cheap but imperfect.
- **A verifier / judge:** a small model (or rules) checks the draft against criteria; fail → escalate.
- **Task-specific checks:** for retrieval answers, does the draft cite a valid source? For structured output, does it parse?

The escalation threshold sets the trade: escalate rarely and you save money but risk shipping weak small-model answers; escalate often and quality rises toward the big model but so does cost. This is a tunable point on the **quality/cost frontier**, and the right setting depends on the SLO for quality. Cascades give you a dial that complexity routing does not.

### 4. Designing Musaed's tiers

A concrete three-tier topology for Musaed:

| Tier | Handler | Handles | Cost/1k (illustrative) |
|---|---|---|---|
| **0 — Semantic cache** | embedding lookup | exact/paraphrased FAQ repeats (~30% of traffic) | ~SAR 0.0003 |
| **1 — Small model** | distilled/quantised 3B student | routine single-step queries (~45%) | ~SAR 0.003 |
| **2 — Large model** | AWQ-INT4 13B Musaed | complex, multi-step, regulatory reasoning (~25%) | ~SAR 0.008 |

Blended cost = Σ(tier share × tier cost). With the shares above, blended cost/1k ≈ 0.30×0.0003 + 0.45×0.003 + 0.25×0.008 ≈ **SAR 0.0035**, versus 0.008 if everything used tier 2 — a ~56% reduction, while the hard 25% still gets the full model. This composition of Modules 2–4 is the heart of the course's cost story.

### 5. Measuring routing: deflection, escalation, blended cost, and quality

You cannot manage routing without four numbers:
- **Deflection rate:** fraction handled below the top tier (cache + small). Higher is cheaper.
- **Escalation rate:** fraction the cascade sends up to the large model. This is your quality safety valve.
- **Blended cost per 1k:** the weighted cost above — the metric leadership cares about.
- **End-to-end quality:** answer-correctness of the *routed system*, not of any single model. A router that saves 56% but drops correctness 5 points has failed the gate (same discipline as Module 3).

Always evaluate the *system*, not the components. A cheap tier with 95% accuracy sounds fine until you learn the 5% it gets wrong are exactly the requests it should have escalated.

### 6. Common mistakes & production considerations

**Common mistakes**
1. A router more expensive than the savings it produces.
2. Complexity routing with no escalation safety net → confident wrong answers on hard queries.
3. Tuning the escalation threshold on cost alone, ignoring the quality frontier.
4. Evaluating tiers in isolation instead of the end-to-end routed system.
5. Static tier shares assumed forever, when traffic mix shifts (Hajj season changes the question distribution).
6. Semantic-cache tier serving stale answers after a policy change (Module 2 governance, revisited).

**Production considerations**
- Log the routing decision and tier for every request — you need it for cost attribution (Module 6) and for spotting mis-routing drift.
- Make thresholds config, not code (Module 6), so ops can re-tune the frontier without a deploy.
- Re-measure tier shares periodically; the traffic mix is not stationary. A good router is monitored, not set-and-forget.
- Routing composes with autoscaling (Module 5): each tier is its own scalable pool with its own demand curve.

## Code Examples

### A complexity router with a confidence-based cascade

```python
# src/musaed/routing/router.py
"""Three-tier routing for Musaed: semantic cache -> small model -> large model.
Tier 1 (small) answers first; low confidence escalates to tier 2 (large).
Every decision is logged for cost attribution and drift monitoring.
"""
from __future__ import annotations
from dataclasses import dataclass

from musaed.serving.semantic_cache import SemanticCache


@dataclass
class RouteResult:
    answer: str
    tier: str          # "cache" | "small" | "large"
    escalated: bool
    confidence: float


class Router:
    def __init__(self, cache: SemanticCache, small_model, large_model,
                 escalate_below: float = 0.75):
        self._cache = cache
        self._small = small_model      # distilled/quantised 3B student
        self._large = large_model      # AWQ-INT4 13B Musaed
        self._escalate_below = escalate_below

    def handle(self, question: str, model_version: str) -> RouteResult:
        # Tier 0: semantic cache — no GPU if hit
        cached = self._cache.get(question, model_version)
        if cached is not None:
            return RouteResult(cached, tier="cache", escalated=False, confidence=1.0)

        # Tier 1: small model answers with a confidence signal (seq log-prob based)
        draft, conf = self._small.generate_with_confidence(question)
        if conf >= self._escalate_below:
            self._cache.put(question, draft, model_version)
            return RouteResult(draft, tier="small", escalated=False, confidence=conf)

        # Tier 2: escalate hard/low-confidence requests to the large model
        answer, _ = self._large.generate_with_confidence(question)
        self._cache.put(question, answer, model_version)
        return RouteResult(answer, tier="large", escalated=True, confidence=conf)
```

### Measuring the routed system: deflection, escalation, blended cost

```python
# eval/routing_metrics.py
"""Turn a batch of RouteResults into the four numbers that matter.
Costs are per-request SAR by tier (from cost.py at each tier's GPU/throughput).
"""
from collections import Counter

TIER_COST_SAR = {"cache": 0.0000003, "small": 0.000003, "large": 0.000008}


def routing_report(results: list) -> dict:
    n = len(results)
    tiers = Counter(r.tier for r in results)
    escalations = sum(1 for r in results if r.escalated)
    deflected = tiers["cache"] + tiers["small"]
    blended = sum(TIER_COST_SAR[r.tier] for r in results) / n * 1000  # per 1k req
    return {
        "n": n,
        "share_cache": round(tiers["cache"] / n, 3),
        "share_small": round(tiers["small"] / n, 3),
        "share_large": round(tiers["large"] / n, 3),
        "deflection_rate": round(deflected / n, 3),
        "escalation_rate": round(escalations / n, 3),
        "blended_sar_per_1k": round(blended, 4),
    }
```

## Hands-on Lab 4 — Build the Routing Cascade

| | |
|---|---|
| **Objective** | Stand up a three-tier router (semantic cache → 3B small → INT4 13B large) in front of Musaed, tune the escalation threshold on the quality/cost frontier, and prove blended-cost reduction without a quality regression |
| **Duration** | 50 minutes |
| **Setup** | `git checkout lab4-router`, the INT4 large model from Lab 3, a provided distilled/quantised 3B student, the semantic cache from Lab 2, eval set from Lab 3 |

**Instructions & tasks**
1. *(10 min)* Wire the `Router` with cache + small + large. Replay the standard prompt corpus through it; log tier decisions.
2. *(10 min)* Run `eval/routing_metrics.py`: record tier shares, deflection, escalation, blended cost/1k.
3. *(10 min)* Run the end-to-end quality gate on the *routed system* vs the always-large baseline. Confirm correctness stays within threshold.
4. *(10 min)* Sweep `escalate_below` (0.6, 0.75, 0.9). Plot blended cost vs system correctness — the quality/cost frontier. Pick the knee.
5. *(5 min)* Write the routing row into `BENCHMARKS.md` (blended cost + system correctness at the chosen threshold).
6. *(5 min)* Commit: `perf(route): 3-tier cascade, -56% blended cost at gate-passing quality`.

**Expected output**
```
tier shares: cache 0.29  small 0.46  large 0.25
deflection 0.75  escalation 0.25
blended cost ≈ SAR 0.0035 / 1k  (vs 0.008 always-large -> -56%)
system correctness 81.9 (always-large 82.1)  -> within gate
frontier knee at escalate_below=0.75
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Blended cost barely improves | Escalation rate too high (threshold too strict) | Lower `escalate_below`; check small-model confidence calibration |
| System correctness drops | Small model answering hard queries confidently | Raise threshold or improve the confidence signal/verifier |
| Router adds noticeable latency | Router itself too heavy | Use a lighter classifier/embedding; keep it off the big-model path |
| Cache serving stale answers | No invalidation after content change | Version cache with model + KB; add TTL (from M2) |

**Instructor notes.** The frontier plot is the deliverable that makes the lesson stick: participants *see* that cost and quality trade smoothly and that there is a defensible knee, not a magic setting. Challenge each pair to justify their chosen threshold in SLO terms ("we accept ≤ 0.5 pt correctness loss for a 56% saving"). Fast finishers: add a verifier tier instead of log-prob confidence and compare frontier quality.

## Mini Exercises

**Quiz (5 questions)**
1. Why is routing especially effective when traffic difficulty is skewed? → most requests are easy and can use a much cheaper model, so blended cost falls sharply.
2. What is the danger of complexity routing without a cascade? → confident wrong answers when a hard query is mis-routed to the small model.
3. What does the escalation threshold trade off? → cost (escalate less) against quality (escalate more).
4. Why must the router be much cheaper than the models it chooses between? → otherwise it eats the savings it creates.
5. Should you evaluate tiers individually or the routed system? → the routed system end-to-end.

**Calculation exercise.** Given tier shares cache 0.30 / small 0.45 / large 0.25 and per-1k costs 0.0003 / 0.003 / 0.008 SAR, compute blended cost/1k and the percentage saving vs always-large. Then recompute if Hajj-season traffic shifts shares to 0.20 / 0.40 / 0.40.

**Design exercise.** Design the confidence signal for Musaed's small tier for a retrieval-grounded question. What makes a good escalation trigger, and how would you detect mis-routing in production logs?

**Discussion questions.**
- Traffic mix shifts seasonally. How do you keep a router's economics honest over time?
- Who owns the escalation threshold — engineering, product, or risk — given it trades cost against citizen-facing quality?

## Case Study — One Endpoint, Three Budgets at a Support Platform

**Scenario.** "Musanad", an enterprise support assistant, ran everything on a 34B model at SAR 0.02/1k requests. Analysis showed 62% of tickets were simple status/FAQ questions. Finance demanded a 40% cost cut without a satisfaction (CSAT) drop.

**Business context.** A flat single-model deployment charged premium prices for trivial questions. But naive downgrading (everything to a small model) had failed a prior year — CSAT fell because hard tickets got weak answers.

**Technical challenge.** Cut blended cost ≥ 40% while holding end-to-end answer quality, absorbing a seasonal shift in question difficulty.

**Constraints.** No CSAT regression; the router must add ≤ 30 ms latency; thresholds must be re-tunable by ops without redeploying.

**Solution approach (facilitate, don't lecture).** (1) Add a semantic-cache tier for repeated tickets (deflects 22%). (2) Route routine tickets to a distilled 7B student. (3) Cascade: escalate low-confidence drafts to the 34B model (escalation ~25%). (4) Make the threshold a config value; monitor tier shares and re-tune monthly. (5) Evaluate the routed *system* CSAT, not per-tier. Result: 48% blended-cost cut, CSAT flat.

**Discussion questions.**
1. Why did last year's "just use a smaller model" fail, and how does a cascade fix it?
2. How would you detect that the traffic mix has shifted enough to re-tune?
3. What is the right owner and change process for the escalation threshold?
4. Why evaluate system CSAT rather than each tier's accuracy?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Deflection rate | Efficiency | ≥ 0.70 | routing metrics |
| Escalation rate | Quality safety valve | tuned to frontier knee (~0.25) | routing metrics |
| Blended cost per 1k | Cost | ≥ 40% below always-large | routing metrics |
| System answer-correctness | Quality | within gate threshold of always-large | end-to-end eval |
| Router added latency | Latency | ≤ 30 ms | harness |
| Frontier knee identified | Rigour | threshold justified in SLO terms | frontier plot |

**Example benchmark table (filled during lab):**

| Configuration | Deflection | Escalation | System correctness | SAR / 1k req |
|---|---|---|---|---|
| Always-large (INT4 13B) | 0.00 | — | 82.1 | 0.008 |
| Cache + small (no cascade) | 0.75 | 0.00 | 79.4 | 0.0021 |
| Full 3-tier cascade | 0.75 | 0.25 | 81.9 | 0.0035 |

## Required Visuals and Training Assets

### Diagrams
1. **Three-tier routing topology** — *Purpose:* the module's mental model. *Elements:* request → cache → small → large with escalation arrows and per-tier cost tags. *Style:* left-to-right flow with cost annotations.
2. **Quality/cost frontier** — *Purpose:* show the tunable trade. *Elements:* scatter of (blended cost, system quality) as the threshold sweeps; the knee marked; always-large point for reference. *Style:* frontier curve.
3. **Cascade decision flow** — *Purpose:* generate-then-verify logic. *Elements:* small-model draft → confidence check → accept or escalate. *Style:* flowchart.

### Images (screenshots)
1. **Routing decision log** — *why:* cost attribution and drift detection; *content:* per-request tier + confidence + escalated flag.
2. **`routing_metrics.py` output** — *why:* the four numbers; *content:* shares, deflection, escalation, blended cost.
3. **Frontier plot** — *why:* justify the chosen threshold; *content:* cost vs quality with the knee.

### Simulations
1. **Mis-routing without a cascade** — *Setup:* complexity routing only, threshold too permissive. *Expected behaviour:* hard queries answered wrongly by the small model with high confidence. *Learning objective:* need a safety valve.
2. **Seasonal mix shift** — *Setup:* replay a Hajj-season traffic file with more complex queries. *Expected behaviour:* escalation rate and blended cost rise; static assumptions break. *Learning objective:* routing must be monitored and re-tuned.

### Interactive Activities
- **Route-the-ticket sort (10 min):** cards of citizen questions sorted into cache/small/large with justification; reveal the "trap" hard-looking-but-cached ones.
- **Threshold negotiation (10 min):** product vs finance vs risk role-play to set the escalation threshold; must state it in SLO terms.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `musaed_routing_corpus.jsonl` | Labelled queries with difficulty tier ground truth, AR+EN | JSONL | 2,000 items | Router tuning + system eval |
| `musaed_hajj_traffic.jsonl` | Seasonal shifted mix (more complex) | JSONL | 1,000 items | Mix-shift simulation |
| `student_3b_awq/` | Provided distilled + quantised small model | safetensors | ~2 GB | The cheap tier |

### Demo Requirements
- **Instructor demo:** replay the corpus through the router live; show blended cost falling as the frontier plot fills in.
- **Student demo:** a pair defends their escalation threshold in SLO terms.
- **Expected outputs:** the routing `BENCHMARKS.md` row, a frontier plot, and a decision log sample.

---

# Module 5 — GPU Infrastructure and Autoscaling

## Module Overview

**Purpose.** Musaed's demand is not flat: it surges on salary day, spikes during Hajj, and falls to a trickle at Fajr. Provisioning for the peak wastes money most of the day; provisioning for the average drops requests during the surge. This module teaches participants to build GPU-serving infrastructure that *tracks demand elastically*: choosing GPU types, sharing GPUs across small models, packing models onto nodes, and — the core skill — autoscaling a serving fleet on the *right* signal (queue depth / concurrency, not CPU) while managing the hard realities of GPU cold starts, model load time, and scale-to-zero economics.

**Business relevance.** GPUs are the dominant cost line and the scarcest resource in a sovereign AI programme. Elastic infrastructure is what lets a national service meet a 10× peak without paying for 10× capacity around the clock. The gap between "provisioned for peak" and "autoscaled to demand" on Musaed's real traffic curve is often a 3–5× difference in monthly GPU spend — the single largest infrastructure lever in the course.

**Industry use cases.**
- A government portal scales its assistant fleet from 3 to 15 GPUs during the salary-day window and back down overnight, on a queue-depth signal.
- A batch document-processing service uses cheap spot/preemptible GPUs and scales to zero between nightly jobs.
- A multi-model platform packs several small models onto one GPU with MIG partitioning to raise utilisation.

**Expected competencies.** After this module a participant can select GPU types for a workload, choose an autoscaling signal, configure Kubernetes HPA/KEDA to scale an inference deployment on queue depth, reason about cold-start and model-load latency, apply scale-to-zero and spot strategies safely, and measure cost under a realistic demand curve.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Select GPU types and sharing strategies (MIG, packing) for a workload | LO4, LO5 |
| 5.2 | Choose an autoscaling signal appropriate to LLM serving (not CPU) | LO4 |
| 5.3 | Configure Kubernetes HPA/KEDA to scale an inference deployment on queue depth | LO4 |
| 5.4 | Manage cold starts, model-load time, and scale-to-zero trade-offs | LO4 |
| 5.5 | Measure serving cost and SLO adherence under a realistic demand curve | LO4, LO1 |

## Technical Content

### 1. Choosing GPUs: the memory-first decision

GPU selection starts with a memory question, not a FLOPs question: the model's weights + KV cache must fit, with headroom. Only then do you compare throughput per Riyal.

| GPU | VRAM | Rough strength | Good for |
|---|---|---|---|
| **A10 / L4** | 24 GB | modest | small/quantised models, cheap tiers |
| **L40S** | 48 GB | strong inference, FP8 | quantised 13B, mid tier |
| **A100 80GB** | 80 GB | workhorse | BF16 13B, batching-heavy serving |
| **H100 80GB** | 80 GB | fastest, native FP8 | high-throughput flagship, big models |

Guidance: after Module 3, quantised Musaed fits an L40S, which may deliver more requests-per-Riyal than an A100 for this workload. The right GPU is the cheapest one that meets the SLO at the required throughput — a claim you settle with the benchmark harness, not with spec sheets. **Requests-per-Riyal**, measured, beats teraflops-per-dollar, quoted.

### 2. GPU sharing: MIG, packing, and utilisation

A single flagship GPU is wasted running one tiny model. Two techniques raise utilisation:
- **MIG (Multi-Instance GPU):** partition an A100/H100 into isolated slices (e.g., 7× on A100), each running a small model with guaranteed memory. Good for many small, latency-sensitive models (Musaed's cheap tier).
- **Model packing / multiplexing:** run several models in one process/pod sharing the GPU's memory and scheduler. Cheaper but without hard isolation — noisy-neighbour risk.

For Musaed's cascade (Module 4), the small tier is an ideal MIG or packing candidate; the large tier wants a whole GPU (or tensor-parallel across several). Match the sharing strategy to the tier.

### 3. The autoscaling signal: why CPU is the wrong metric

Default Kubernetes HPA scales on CPU utilisation — which is meaningless for GPU inference (the CPU can be idle while the GPU is saturated and requests queue). Scaling on the wrong signal is worse than not scaling. The right signals for LLM serving:

- **Queue depth / pending requests** — the most direct: if requests are waiting, add capacity. vLLM exposes queue and running-sequence counts.
- **Concurrency / in-flight requests per replica** — scale to keep each replica near its efficient operating point (below the knee from Module 1).
- **GPU-based custom metrics** (KV-cache utilisation, tokens/s) exported to Prometheus.

KEDA (Kubernetes Event-Driven Autoscaling) makes queue-depth and custom-metric scaling straightforward by driving the HPA from Prometheus queries. The autoscaler's job is to keep the fleet at the operating point where throughput is high and p95 still meets the SLO — the knee, tracked continuously as demand moves.

### 4. The cold-start problem

Autoscaling GPUs is harder than autoscaling stateless web pods because adding a replica is *slow*: schedule a GPU node (possibly a cloud node that must boot), pull a multi-GB container image, load and shard a multi-GB model into VRAM, and warm up (Module 2). This can take minutes. Consequences:

- **Scale up early.** Scale on a *leading* signal (rising queue depth) with aggressive thresholds, because new capacity arrives late. Reacting only when the SLO is already breached is too late.
- **Keep a warm buffer.** Hold a small headroom of ready replicas above current demand so a sudden spike is absorbed while new nodes boot.
- **Shrink cold-start cost:** slim images (Module — container discipline), model caching on fast local NVMe or a shared cache, and pre-pulled base images. Every second of load time is a second of SLO risk during a surge.
- **Scale down conservatively.** Use a cooldown/stabilisation window so a brief dip does not evict a replica you need back 90 seconds later (thrashing wastes more than it saves).

### 5. Scale-to-zero, spot, and the demand curve

- **Scale-to-zero** suits bursty or scheduled workloads (batch jobs, low-traffic internal tools): pay nothing when idle, accept a cold-start penalty on the first request. For an always-on citizen service like Musaed's main path, keep a warm floor (min replicas > 0) sized to the overnight trough; scale-to-zero only the optional batch/analytics paths.
- **Spot / preemptible GPUs** are far cheaper but can be reclaimed with little notice. Use them for interruptible, checkpointable work (batch scoring, distillation) or as *burst* capacity behind on-demand baseline — never as the sole capacity for an SLO-bound interactive path.
- **Drive planning from the real curve.** `musaed_traffic_profile.csv` (Module 1) gives the 24-hour shape: overnight trough, morning ramp, salary-day surge. Size min replicas to the trough, max to the peak, and let the autoscaler ride the curve. The cost win is the area between "flat peak provisioning" and "the demand curve" — make participants shade it.

### 6. Common mistakes & production considerations

**Common mistakes**
1. Autoscaling on CPU for a GPU workload (scales on a metric that never moves).
2. Reactive scaling with no warm buffer, so every surge breaches the SLO during cold start.
3. Scale-to-zero on an always-on interactive path, giving citizens a 90-second first-request stall.
4. Spot GPUs as sole capacity for an SLO-bound service.
5. No scale-down cooldown → thrashing (repeated add/remove) that costs more than steady state.
6. Sizing min replicas to the average instead of the trough+buffer, under-serving the ramp.

**Production considerations**
- Set min replicas from the trough + a safety buffer; set max from the peak + burst headroom; alert when sustained demand approaches max (capacity planning signal).
- Bin-pack tiers: cheap tier on MIG slices or L4s, flagship tier on whole A100/H100; autoscale each pool independently on its own queue.
- Cold start is a cost *and* a reliability property — track "time from scale-up trigger to first served request" as an SLI.
- In a sovereign environment, elasticity may be bounded by a fixed on-prem GPU pool; then autoscaling becomes *prioritisation* (which tier gets the scarce GPUs) rather than acquisition — teach both.

## Code Examples

### KEDA ScaledObject: autoscale vLLM on queue depth

```yaml
# k8s/musaed-scaledobject.yaml
# Scale the large-tier vLLM deployment on pending-request queue depth
# (from Prometheus), NOT on CPU. Warm floor of 2, ceiling of 12.
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: musaed-large-scaler
spec:
  scaleTargetRef:
    name: musaed-large            # the vLLM Deployment
  minReplicaCount: 2              # warm floor sized to the overnight trough + buffer
  maxReplicaCount: 12             # ceiling sized to salary-day peak + burst headroom
  cooldownPeriod: 180            # conservative scale-down: avoid thrashing
  advanced:
    horizontalPodAutoscalerConfig:
      behavior:
        scaleUp:
          stabilizationWindowSeconds: 0     # scale UP fast: GPUs are slow to arrive
          policies: [{ type: Pods, value: 3, periodSeconds: 60 }]
        scaleDown:
          stabilizationWindowSeconds: 300   # scale DOWN slowly
  triggers:
    - type: prometheus
      metadata:
        serverAddress: http://prometheus.monitoring:9090
        metricName: vllm_pending_requests
        query: sum(vllm:num_requests_waiting{service="musaed-large"})
        threshold: "8"           # target ~8 waiting requests per replica -> add capacity
```

### Deployment with a fast model cache to cut cold start

```yaml
# k8s/musaed-large-deployment.yaml (excerpt)
spec:
  template:
    spec:
      nodeSelector: { nvidia.com/gpu.product: NVIDIA-A100-80GB }
      containers:
        - name: vllm
          image: registry.sdaia.local/musaed/vllm:pinned   # slim, pinned -> fast pull
          args: ["--model", "/models/allam-13b-awq-int4",
                 "--quantization", "awq", "--enable-prefix-caching",
                 "--gpu-memory-utilization", "0.90"]
          resources:
            limits: { nvidia.com/gpu: 1 }
          volumeMounts:
            - { name: model-cache, mountPath: /models }   # local NVMe, pre-warmed
          startupProbe:                                    # don't route until warm
            httpGet: { path: /health, port: 8000 }
            periodSeconds: 5
            failureThreshold: 60                           # allow up to 5 min to load
          readinessProbe:
            httpGet: { path: /health, port: 8000 }
      volumes:
        - name: model-cache
          hostPath: { path: /mnt/nvme/models }             # avoid re-downloading weights
```

### Simulating cost under the real demand curve

```python
# tools/autoscale_sim.py
"""Replay Musaed's 24h demand curve against two policies:
(a) flat peak provisioning, (b) queue-depth autoscaling with a warm buffer.
Report GPU-hours and SLO breaches. The gap is the cost win.
"""
import csv, math

REQ_PER_GPU = 140          # knee throughput per GPU (from Module 2)
WARM_BUFFER = 1            # extra ready replica above demand
MIN_REPLICAS, MAX_REPLICAS = 2, 12
GPU_SAR_PER_HOUR = 8.25


def needed(rps: float) -> int:
    return max(MIN_REPLICAS, min(MAX_REPLICAS, math.ceil(rps / REQ_PER_GPU) + WARM_BUFFER))


def simulate(path: str) -> None:
    minutes = list(csv.DictReader(open(path)))
    peak_rps = max(float(m["req_per_s"]) for m in minutes)
    flat_replicas = math.ceil(peak_rps / REQ_PER_GPU)     # provision for peak, always
    flat_gpu_h = flat_replicas * len(minutes) / 60
    auto_gpu_min = sum(needed(float(m["req_per_s"])) for m in minutes)
    auto_gpu_h = auto_gpu_min / 60
    print(f"flat peak:   {flat_replicas} GPUs x24h = {flat_gpu_h:.0f} GPU-h "
          f"= SAR {flat_gpu_h*GPU_SAR_PER_HOUR:,.0f}")
    print(f"autoscaled:  {auto_gpu_h:.0f} GPU-h "
          f"= SAR {auto_gpu_h*GPU_SAR_PER_HOUR:,.0f}")
    print(f"saving: {(1 - auto_gpu_h/flat_gpu_h)*100:.0f}%")


if __name__ == "__main__":
    simulate("data/musaed_traffic_profile.csv")
```

## Hands-on Lab 5 — Autoscale the GPU Fleet

| | |
|---|---|
| **Objective** | Deploy Musaed on Kubernetes with KEDA autoscaling on queue depth, drive it with the real 24-hour demand curve (accelerated), and measure GPU-hours saved vs flat peak provisioning while holding the SLO |
| **Duration** | 50 minutes |
| **Setup** | `git checkout lab5-hpa`, a shared classroom Kubernetes cluster with GPU nodes (or a provided kind+mock-GPU sandbox), KEDA + Prometheus installed, `musaed_traffic_profile.csv` |

**Instructions & tasks**
1. *(10 min)* Deploy the large-tier vLLM Deployment + Service; confirm the startup/readiness probes and a warm floor of 2 replicas.
2. *(10 min)* Apply the KEDA `ScaledObject`; verify it reads `vllm:num_requests_waiting` from Prometheus (not CPU).
3. *(15 min)* Replay the 24-hour curve accelerated (1 min = 1 hour) with the load generator. Watch replicas track demand; record scale-up lag (cold-start time to first served request) and any SLO breaches during the salary-day surge.
4. *(5 min)* Run `tools/autoscale_sim.py` to compute GPU-hours and cost: autoscaled vs flat peak. Record the saving.
5. *(5 min)* Tune: add/adjust the warm buffer to eliminate surge breaches without over-provisioning; note the cost/SLO trade.
6. *(5 min)* Write the autoscaling row into `BENCHMARKS.md` and commit: `infra(scale): KEDA queue-depth autoscaling, -62% GPU-hours vs peak`.

**Expected output**
```
flat peak:   4 GPUs x24h = 96 GPU-h = SAR 792
autoscaled:  37 GPU-h = SAR 305
saving: 62%
salary-day surge: 1 brief SLO breach during cold start -> fixed by warm_buffer=2
scale-up lag (trigger -> first served): 74 s
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Replicas never scale up under load | HPA on CPU, or KEDA can't reach Prometheus | Confirm the ScaledObject queries the queue metric; check Prometheus wiring |
| SLO breaches on every surge | Reactive scaling, no warm buffer | Raise warm buffer / lower scale-up threshold; scale on a leading signal |
| Replicas thrash up and down | No scale-down cooldown | Set `cooldownPeriod` / scale-down stabilisation window |
| New replica takes minutes to serve | Cold start: image pull + model load | Pre-warm model cache on NVMe; slim/pin the image |

**Instructor notes.** The killer visual is the replica count overlaid on the demand curve — participants *see* the fleet breathe with salary day and shrink at Fajr. Deliberately let one pair scale reactively (no buffer) so a surge breach appears, then fix it live with a warm buffer. Emphasise the cold-start reality: in GPU-land, you must scale up *before* you need it, which is the opposite instinct from stateless web autoscaling.

## Mini Exercises

**Quiz (5 questions)**
1. Why is CPU utilisation the wrong autoscaling signal for GPU inference? → the CPU can be idle while the GPU saturates and requests queue; it never triggers.
2. Name two good autoscaling signals for LLM serving. → pending-request queue depth; in-flight concurrency per replica (also KV-cache util / tokens-s).
3. Why must GPU services scale up on a *leading* signal? → cold start (node boot + image pull + model load) is slow; reacting after the breach is too late.
4. When is scale-to-zero appropriate, and when is it dangerous? → good for bursty/batch/idle paths; dangerous for always-on interactive SLO paths (first-request stall).
5. Why size min replicas to the trough rather than the average? → the average under-provisions the ramp; the trough + buffer keeps the floor warm.

**Calculation exercise.** Given peak 90 req/s, trough 12 req/s, and 140 req/s per GPU, compute GPUs needed at peak vs trough, and estimate the GPU-hour saving of autoscaling vs flat-peak over a day where demand is above 70 req/s for only 3 hours.

**Design exercise.** Sketch the autoscaling design for Musaed's three tiers (cache, small, large): which pool scales to zero, which keeps a warm floor, which uses MIG or spot, and on what signal each scales.

**Discussion questions.**
- Your sovereign GPU pool is fixed at 8 GPUs — no elastic acquisition. How does autoscaling become a prioritisation problem, and which tier yields first?
- Spot GPUs are 60% cheaper but reclaimable. Where in Musaed's architecture can you safely use them?

## Case Study — Provisioned for Hajj, Paying for It All Year

**Scenario.** A ministry sized its assistant fleet for the Hajj-season peak — 20 GPUs — and left it running year-round. For ten months those GPUs sat at ~20% utilisation. The annual GPU bill was roughly 4× what the workload required.

**Business context.** Demand had a huge seasonal peak but a modest baseline. Flat peak provisioning is simple and safe but, at national scale, hemorrhages public funds during the long off-peak.

**Technical challenge.** Cut annual GPU spend by more than half without dropping requests during the Hajj surge or the daily salary-day spikes.

**Constraints.** Zero request drops during the surge; sovereign on-prem baseline capacity with cloud-burst allowed for peaks; cold start must not breach the SLO.

**Solution approach (facilitate, don't lecture).** (1) Size an on-prem warm floor to the daily trough + buffer. (2) Autoscale on queue depth up to an on-prem ceiling, then cloud-burst for Hajj. (3) Pre-warm model caches and slim images so scale-up lag stays under the SLO's tolerance. (4) Add a leading-signal scale-up (rising queue) plus a warm buffer for salary-day spikes. (5) Simulate on the real annual curve before committing. Result: ~65% annual GPU-cost reduction, no surge drops.

**Discussion questions.**
1. Why is flat peak provisioning so expensive at national scale, and when is it nonetheless the right choice?
2. How do you split baseline vs burst between sovereign on-prem and cloud?
3. What SLI would you track to prove cold start never breached the SLO during a surge?
4. How would you validate the design *before* Hajj rather than during it?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| GPU-hours vs flat peak | Cost | ≥ 50% reduction on the real curve | `autoscale_sim.py` |
| SLO adherence under surge | Reliability | ≤ 1 brief breach, resolved by buffer | replay + goodput |
| Scale-up lag (trigger → served) | Reliability | ≤ 90 s | replay measurement |
| Scaling signal correctness | Rigour | queue depth / concurrency (not CPU) | ScaledObject review |
| Warm-floor sizing | Efficiency | trough + buffer, no ramp under-serve | curve overlay |
| Thrashing | Stability | none (cooldown enforced) | replica timeline |

**Example benchmark table (filled during lab):**

| Policy | GPU-hours / day | SLO breaches | Scale-up lag | SAR / day |
|---|---|---|---|---|
| Flat peak (4 GPUs) | 96 | 0 | n/a | 792 |
| Autoscaled, no buffer | 34 | 3 (surge) | 74 s | 281 |
| Autoscaled + warm buffer | 37 | 0 | 74 s | 305 |

## Required Visuals and Training Assets

### Diagrams
1. **Demand curve vs provisioning** — *Purpose:* show the cost win as shaded area. *Elements:* 24h req/s curve; flat peak line above it; autoscaled staircase tracking it; the gap shaded "wasted GPU-hours". *Style:* area chart.
2. **Autoscaling control loop** — *Purpose:* the signal→decision→capacity loop. *Elements:* Prometheus queue metric → KEDA → HPA → replicas → back to queue; cold-start delay annotated. *Style:* control-loop diagram.
3. **GPU sharing options** — *Purpose:* MIG vs packing vs whole-GPU. *Elements:* one GPU sliced by MIG for small models, one whole GPU for the flagship. *Style:* partitioned-rectangle diagram.

### Images (screenshots)
1. **Replica count over the demand curve** — *why:* the fleet "breathing"; *content:* replicas overlaid on req/s with salary-day surge.
2. **KEDA ScaledObject status** — *why:* confirm queue-depth trigger; *content:* `kubectl get scaledobject` showing active triggers.
3. **`autoscale_sim.py` output** — *why:* the cost saving; *content:* flat vs autoscaled GPU-hours and %.

### Simulations
1. **Cold-start surge breach** — *Setup:* reactive scaling, no buffer, sudden salary-day spike. *Expected behaviour:* SLO breach while new replicas boot. *Learning objective:* scale on a leading signal with a warm buffer.
2. **Scale-down thrashing** — *Setup:* no cooldown under choppy demand. *Expected behaviour:* replicas flap up/down, cost and instability rise. *Learning objective:* conservative scale-down.

### Interactive Activities
- **Size-the-fleet workshop (15 min):** given the traffic CSV and per-GPU knee, pairs set min/max/buffer and defend the cost/SLO trade.
- **Signal card sort (10 min):** metrics (CPU, GPU-util, queue depth, tokens/s, memory) sorted into "good/bad autoscaling signal" with reasons.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `musaed_traffic_profile.csv` | Synthetic 24h per-minute arrival curve (reused from M1) | CSV | 1,440 rows | Autoscaling replay + cost sim |
| `musaed_annual_curve.csv` | Synthetic year with Hajj peak | CSV | 365 rows | Provisioning case study |

### Demo Requirements
- **Instructor demo:** replay the accelerated curve; project the replica count tracking demand and the surge handled by the buffer.
- **Student demo:** a pair shows their GPU-hour saving and the one tuning change that eliminated a surge breach.
- **Expected outputs:** the autoscaling `BENCHMARKS.md` row, a replica-vs-demand screenshot, and a queue-depth ScaledObject.

---

# Module 6 — AI FinOps: Cost Monitoring and TCO

## Module Overview

**Purpose.** The previous modules cut cost per lever; this module makes cost a *managed, visible, governed* quantity. FinOps — financial operations — is the discipline of connecting engineering decisions to the bill in near real time, so that spend is attributed, forecast, alerted on, and optimised continuously rather than discovered at month-end. Participants build a cost dashboard for Musaed, compute a full **total cost of ownership (TCO)** model that includes the hidden costs (people, storage, networking, idle, compliance), and use it to make the **build-versus-buy** decision (self-host on sovereign GPUs vs a managed API) on evidence.

**Business relevance.** For a national AI programme, cost accountability is a governance requirement: budgets are public funds, and "why did the AI bill double?" must be answerable in minutes with attribution, not guessed at in a quarterly review. A credible TCO model is also what justifies (or refutes) the sovereign build-vs-buy decision — a strategic choice with data-residency, cost, and capability dimensions that a spec-sheet price-per-token comparison cannot settle.

**Industry use cases.**
- A platform team publishes per-department showback so each ministry sees its own Musaed spend and self-optimises.
- A CFO demands a 3-year TCO comparing self-hosting a fine-tuned open model against a commercial API before approving GPU capex.
- An SRE gets paged when hourly spend deviates from forecast, catching a runaway batch job before it burns the monthly budget.

**Expected competencies.** After this module a participant can define AI unit economics, instrument per-request cost attribution, build a cost/efficiency dashboard with budget alerts, construct a TCO model including hidden costs, and produce a defensible build-vs-buy and model-tier recommendation.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Define AI unit economics and attribute cost per request, tenant, and tier | LO6, LO5 |
| 6.2 | Build a cost-monitoring dashboard with budget alerts and forecasting | LO6 |
| 6.3 | Construct a TCO model including hidden (people, storage, network, idle) costs | LO5 |
| 6.4 | Evaluate build-versus-buy and model-tier choices on TCO evidence | LO5 |
| 6.5 | Produce an optimisation playbook that keeps a service within budget | LO6 |

## Technical Content

### 1. FinOps for AI: making cost a first-class signal

FinOps rests on a simple loop — **inform, optimise, operate** — applied continuously:
- **Inform:** everyone can see current and forecast spend, attributed to who caused it.
- **Optimise:** the levers from Modules 2–5 are prioritised by Riyal-per-engineering-day.
- **Operate:** budgets, alerts, and playbooks keep the service inside its envelope automatically.

The cultural shift for engineers is that **cost is a metric like latency** — instrumented, dashboarded, alerted, and owned — not an accounting afterthought. A team that can see cost/1k requests moving in real time optimises it; a team that sees it once a month cannot.

### 2. AI unit economics

The denominators that make spend comparable across time and services:
- **Cost per 1,000 requests** (Module 1) — the product/business unit.
- **Cost per 1M tokens** — the model/infra unit; separates input (prefill) and output (decode) tokens because they cost differently.
- **Cost per active user / per session** — the executive unit.
- **GPU-hours per 1,000 requests** — the efficiency unit that strips out GPU price volatility.

A healthy FinOps practice tracks a *unit* cost trend, not just total spend: total can fall because traffic fell (bad) or because efficiency rose (good), and only the unit metric distinguishes them. When Musaed's traffic triples on salary day, total cost rises — but if cost/1k requests is flat or falling, the system is scaling economically.

### 3. Cost attribution: from GPU-hours to a request

To attribute cost you must join two data sources: **infrastructure billing** (GPU-hours × price, per pool/tier) and **application telemetry** (requests, tokens, tier, tenant, from the logs of Module 4). The join key is time + tier + tenant. From it you compute: this ministry consumed X requests on the large tier during hour H, which used Y GPU-hours costing Z SAR, so their attributed cost is Z. Attribution enables **showback** (visibility) and **chargeback** (actual cross-billing) — the mechanism that makes each consumer accountable for its own optimisation. Without attribution, the platform absorbs all waste and no consumer has an incentive to be efficient.

### 4. TCO: the costs the price-per-token hides

A serving-cost-per-token number is not TCO. A defensible total cost of ownership for self-hosting Musaed includes:

| Cost category | Examples | Often forgotten? |
|---|---|---|
| **Compute** | GPU-hours (serving + idle/warm-floor + dev), autoscaling overhead | no |
| **People** | ML/platform engineers to build, operate, on-call, optimise | very often |
| **Storage & data** | model artefacts, KV/cache, logs, eval sets, backups | sometimes |
| **Networking** | egress, inter-AZ, load balancers | sometimes |
| **Idle & overhead** | warm floors, buffers, non-peak underutilisation | very often |
| **Compliance & sovereignty** | data-residency infra, audit, security controls | very often |
| **Opportunity/lock-in** | migration cost, vendor lock-in risk | very often |

The honest self-host number is often 2–3× the raw GPU-hour cost once people and idle are included. The commercial-API alternative folds most of these into a per-token price but adds data-residency and lock-in considerations that, in a sovereign context, can be decisive regardless of price.

### 5. Build vs buy, and model-tier trade-offs

The build-vs-buy decision is a TCO comparison over a realistic horizon (e.g., 3 years) at realistic volume, plus non-cost factors:

- **Buy (managed API):** low upfront cost, fast to start, elastic, but per-token price scales linearly with success — at national volume it can dwarf self-hosting — and raises data-residency/sovereignty questions.
- **Build (self-host open/fine-tuned model on sovereign GPUs):** high fixed cost (people + capex) that amortises at volume, full data control, but you own reliability, scaling, and optimisation (this whole course).

The crossover is a *volume* question: below some request volume, buy is cheaper; above it, build wins — and the sovereignty requirement may override the crossover entirely. Teach participants to compute the crossover, not to have an opinion. The same logic applies to **model-tier** choice: a bigger model that needs fewer escalations may beat a cheaper model that escalates constantly — decide on blended TCO, not sticker price.

### 6. Common mistakes & production considerations

**Common mistakes**
1. Tracking total spend without a unit-cost trend, so efficiency changes are invisible.
2. A "TCO" that is really just GPU-hours × price, omitting people and idle.
3. Build-vs-buy argued on price-per-token at *today's* volume, ignoring the crossover and sovereignty.
4. No attribution, so the platform eats all waste and no team optimises.
5. Budget alerts on monthly totals (too late) instead of hourly deviation from forecast.
6. Dashboards of vanity metrics (GPU-util) with no Riyal, so leadership can't act.

**Production considerations**
- Alert on *rate* and *deviation from forecast*, not just cumulative totals — a runaway job should page within minutes.
- Make the dashboard bilingual-friendly for leadership but keep metric names/queries in English.
- Tie the FinOps loop to the optimisation playbook: each alert maps to a named lever (Modules 2–5) with an expected saving, so response is mechanical, not heroic.
- Review unit-cost trends in a recurring FinOps cadence with engineering + finance + product in the room — the discipline is organisational, not just technical.

## Code Examples

### Per-request cost attribution from telemetry + billing

```python
# src/musaed/finops/attribution.py
"""Join application telemetry (requests, tokens, tier, tenant) with GPU billing
to attribute SAR per request/tenant/tier. Emits rows for the cost dashboard.
"""
from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass

# GPU SAR/hour per serving pool (from infra billing)
POOL_SAR_PER_HOUR = {"large": 8.25, "small": 4.10, "cache": 0.0}


@dataclass
class Usage:
    tenant: str
    tier: str
    requests: int
    gpu_seconds: float      # measured GPU time attributed to this tenant/tier/hour


def attribute(usages: list[Usage]) -> dict:
    by_tenant: dict[str, float] = defaultdict(float)
    by_tier: dict[str, float] = defaultdict(float)
    total_req: dict[str, int] = defaultdict(int)
    for u in usages:
        sar = POOL_SAR_PER_HOUR[u.tier] / 3600 * u.gpu_seconds
        by_tenant[u.tenant] += sar
        by_tier[u.tier] += sar
        total_req[u.tenant] += u.requests
    return {
        "sar_by_tenant": {k: round(v, 2) for k, v in by_tenant.items()},
        "sar_by_tier": {k: round(v, 2) for k, v in by_tier.items()},
        "sar_per_1k_by_tenant": {
            k: round(by_tenant[k] / total_req[k] * 1000, 4) for k in by_tenant},
    }
```

### A 3-year TCO / build-vs-buy model

```python
# tools/tco.py
"""3-year TCO: self-host Musaed on sovereign GPUs vs a commercial API.
Includes the costs price-per-token hides. Finds the volume crossover.
"""
from dataclasses import dataclass

SAR = 1.0
HOURS_PER_YEAR = 24 * 365


@dataclass
class SelfHost:
    avg_gpus: float                 # blended average incl. warm floor + idle
    gpu_sar_per_hour: float
    engineers: int
    eng_sar_per_year: float         # loaded cost per engineer
    storage_network_sar_per_year: float
    compliance_sar_per_year: float  # sovereignty/audit overhead

    def annual(self) -> float:
        compute = self.avg_gpus * self.gpu_sar_per_hour * HOURS_PER_YEAR
        people = self.engineers * self.eng_sar_per_year
        return compute + people + self.storage_network_sar_per_year + self.compliance_sar_per_year


@dataclass
class BuyApi:
    sar_per_1m_tokens: float
    tokens_per_request: float
    data_residency_sar_per_year: float   # premium/controls for sovereign hosting

    def annual(self, requests_per_year: float) -> float:
        tokens = requests_per_year * self.tokens_per_request
        return tokens / 1_000_000 * self.sar_per_1m_tokens + self.data_residency_sar_per_year


def crossover(sh: SelfHost, api: BuyApi, lo=1e6, hi=5e9) -> float:
    """Requests/year where self-host becomes cheaper than buy."""
    for _ in range(60):
        mid = (lo + hi) / 2
        if sh.annual() < api.annual(mid):
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


if __name__ == "__main__":
    sh = SelfHost(avg_gpus=4.5, gpu_sar_per_hour=8.25, engineers=2,
                  eng_sar_per_year=520_000, storage_network_sar_per_year=90_000,
                  compliance_sar_per_year=140_000)
    api = BuyApi(sar_per_1m_tokens=45.0, tokens_per_request=480,
                 data_residency_sar_per_year=200_000)
    print(f"self-host annual: SAR {sh.annual():,.0f}")
    print(f"crossover volume: {crossover(sh, api)/1e6:,.0f} M requests/year")
```

## Hands-on Lab 6 — Cost Dashboard and TCO Model

| | |
|---|---|
| **Objective** | Build a Musaed cost dashboard with per-tier/per-tenant attribution and budget alerts, then compute a 3-year TCO and the self-host-vs-buy crossover to make a defensible recommendation |
| **Duration** | 50 minutes |
| **Setup** | `git checkout lab6-finops`, Prometheus + Grafana from Lab 5, provided billing + telemetry sample, `tools/tco.py` |

**Instructions & tasks**
1. *(10 min)* Wire `attribution.py` to emit `musaed_cost_sar` metrics by tier and tenant; scrape into Prometheus.
2. *(10 min)* Build a Grafana panel set: cost/1k requests trend, spend by tier, spend by tenant (showback), GPU-hours/1k (efficiency). Keep metric names in English.
3. *(10 min)* Add a budget alert: page when hourly spend deviates > 30% above forecast (simulate a runaway batch job and confirm it fires).
4. *(10 min)* Run `tools/tco.py` with Musaed's numbers; compute self-host annual TCO and the request-volume crossover vs the API. Vary the sovereignty/compliance cost and observe the crossover move.
5. *(5 min)* Write a one-paragraph build-vs-buy recommendation citing the crossover and the sovereignty factor; add the cost row to `BENCHMARKS.md`.
6. *(5 min)* Commit: `finops(dash): attribution dashboard + budget alert + 3y TCO crossover`.

**Expected output**
```
self-host annual: SAR 1,606,000
crossover volume: ~730 M requests/year
Musaed projected volume: 2,190 M/year  -> ABOVE crossover -> self-host cheaper
+ sovereignty requirement -> self-host recommended regardless
budget alert fired at +34% hourly deviation (runaway batch caught in 4 min)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Cost metric flat/zero | Attribution not joined to GPU-seconds | Confirm telemetry emits per-tier gpu_seconds |
| Alert never fires | Threshold on cumulative total, not rate | Alert on hourly deviation from forecast |
| Crossover looks absurd | Hidden costs omitted (people/idle) | Include people, idle, compliance in SelfHost |
| Showback numbers don't sum to bill | Untracked idle/warm-floor cost | Attribute a shared-overhead line; reconcile to the bill |

**Instructor notes.** The "aha" is that the honest self-host TCO is 2–3× the GPU-hour number once people and idle are in — and that this *changes the build-vs-buy answer*. Have pairs vary the sovereignty cost and watch the crossover move; then discuss that for a national service the sovereignty requirement can override the crossover entirely. Insist the recommendation cite numbers, not preference.

## Mini Exercises

**Quiz (5 questions)**
1. Why track unit cost, not just total spend? → total can fall because traffic fell (bad) or efficiency rose (good); only unit cost distinguishes them.
2. Name three costs a "GPU-hours × price" TCO omits. → people/on-call, idle/warm-floor, compliance/sovereignty (also storage, networking, lock-in).
3. What join produces per-tenant cost attribution? → infra billing (GPU-hours × price) joined to application telemetry (requests/tokens/tier/tenant) by time+tier+tenant.
4. Why alert on deviation from forecast, not monthly total? → monthly totals surface waste too late; rate/deviation catches runaways in minutes.
5. Build-vs-buy hinges on which variable, plus which override? → request volume (the crossover); sovereignty/data-residency can override it.

**Calculation exercise.** Self-host: avg 4.5 GPUs at SAR 8.25/hr, 2 engineers at 520k, 90k storage/net, 140k compliance. API: SAR 45/1M tokens, 480 tokens/request, 200k residency. Compute both annual costs at 2.19B requests/year and state the recommendation.

**Design exercise.** Design a showback report for three ministries sharing Musaed: what metrics, what cadence, and what incentive it creates for each to optimise its own traffic.

**Discussion questions.**
- Total spend rose 20% this month. What one chart tells you whether that is good or bad news?
- When should a sovereignty requirement override a cost-favourable build-vs-buy crossover?

## Case Study — The Bill That Doubled Overnight

**Scenario.** A platform team running Musaed for several ministries saw the monthly GPU bill double with no traffic increase. It took nine days of manual log archaeology to find the cause: a mis-configured batch analytics job left the large-tier fleet pinned at max replicas around the clock.

**Business context.** There was no cost attribution and no rate-based alerting — spend was reviewed monthly against a total. The waste ran for nearly the whole month before discovery.

**Technical challenge.** Make cost anomalies visible in minutes and attributable to the responsible workload/tenant.

**Constraints.** Public-funds accountability; multiple tenants on shared infrastructure; the fix must not require re-architecting the serving stack.

**Solution approach (facilitate, don't lecture).** (1) Instrument per-tier/per-tenant attribution joining billing to telemetry. (2) Build a cost/1k-requests trend and spend-by-tenant dashboard. (3) Alert on hourly deviation from forecast (the runaway would have paged in minutes). (4) Add showback so each ministry sees and owns its spend. (5) Map each alert to a playbook lever. Result: next anomaly caught in 4 minutes and attributed to the offending tenant automatically.

**Discussion questions.**
1. Which single control would have caught this fastest, and why?
2. Why does attribution change tenant behaviour, not just visibility?
3. What forecast baseline makes deviation alerting trustworthy?
4. How do you reconcile showback numbers to the actual bill when shared overhead exists?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Cost attribution coverage | Governance | ≥ 95% of spend attributed to tier+tenant | dashboard vs bill reconciliation |
| Anomaly detection time | Governance | ≤ 5 min to page on runaway | injected-anomaly test |
| Unit-cost trend visible | FinOps | cost/1k requests charted over time | Grafana panel |
| TCO completeness | Rigour | includes people, idle, compliance | TCO model review |
| Build-vs-buy crossover | Decision | computed with sovereignty factor | `tco.py` |
| Playbook coverage | Operability | each alert maps to a named lever | playbook doc |

**Example benchmark table (filled during lab):**

| Artefact | Result |
|---|---|
| Self-host annual TCO | SAR 1,606,000 |
| Crossover volume | ~730 M requests/year |
| Musaed projected volume | 2,190 M/year (above crossover) |
| Recommendation | Self-host (crossover + sovereignty) |
| Anomaly page time (injected) | 4 min |

## Required Visuals and Training Assets

### Diagrams
1. **The FinOps loop for AI** — *Purpose:* frame the discipline. *Elements:* inform → optimise → operate cycle with cost/latency/quality feeding it. *Style:* circular loop.
2. **Cost attribution join** — *Purpose:* how a GPU-hour becomes a per-request cost. *Elements:* billing table + telemetry table joined on time/tier/tenant → per-request SAR. *Style:* data-join diagram.
3. **Build-vs-buy crossover** — *Purpose:* the volume decision. *Elements:* self-host (flat-ish) vs API (linear) annual cost vs request volume; crossover marked; sovereignty override note. *Style:* two-line cost chart.

### Images (screenshots)
1. **Grafana cost dashboard** — *why:* the deliverable; *content:* cost/1k trend, spend by tier, showback by tenant.
2. **Budget alert firing** — *why:* anomaly detection; *content:* the +34% deviation alert on the runaway job.
3. **`tco.py` output** — *why:* the recommendation basis; *content:* annual TCO and crossover volume.

### Simulations
1. **Runaway job** — *Setup:* pin the large fleet at max replicas. *Expected behaviour:* rate alert fires in minutes; attribution names the tenant. *Learning objective:* rate/deviation alerting + attribution.
2. **Sovereignty sensitivity** — *Setup:* sweep compliance cost in the TCO. *Expected behaviour:* crossover volume shifts; decision can flip. *Learning objective:* TCO is sensitive to hidden costs.

### Interactive Activities
- **TCO worksheet (15 min):** pairs fill a full TCO for Musaed including hidden costs, then compute the crossover; compare answers.
- **Dashboard critique (10 min):** given a "vanity-metric" dashboard (GPU-util only), pairs redesign it around Riyal and unit cost.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `musaed_billing_sample.csv` | Synthetic GPU billing by pool/hour | CSV | 720 rows | Attribution + dashboard |
| `musaed_telemetry_sample.jsonl` | Synthetic per-request tier/tenant/tokens | JSONL | 50,000 rows | Attribution + showback |
| `tco_inputs.yaml` | Editable TCO assumptions | YAML | small | Build-vs-buy exercise |

### Demo Requirements
- **Instructor demo:** trigger the runaway job live; show the alert fire and the tenant attributed within minutes.
- **Student demo:** a pair presents its build-vs-buy recommendation with the crossover and sovereignty reasoning.
- **Expected outputs:** a working cost dashboard, a firing budget alert, and a computed TCO crossover.

---

# Module 7 — Optimisation Project on a Live Workload

## Module Overview

**Purpose.** The previous six modules taught levers in isolation; a real optimisation is choosing *which* levers, in *what order*, for a *specific* SLO and budget, and proving the result with a rigorous before/after benchmark. This module is the method: how to run an end-to-end optimisation on a live workload — diagnose the bottleneck, prioritise levers by Riyal-per-effort, apply them without breaking the SLO or the quality gate, and produce a defensible before/after report and reusable playbook. It is also the direct on-ramp to the capstone, which *is* this method applied to Musaed under a fresh constraint.

**Business relevance.** Optimisation is not a one-time project; it is a repeatable operating capability. The organisations that run national AI affordably are the ones with a *playbook* — a named, ordered set of levers with expected savings — that any engineer can execute when a service drifts over budget or an SLO tightens. This module turns the course's six levers into that playbook and teaches the discipline that makes optimisation claims trustworthy: measure, change one thing, re-measure, attribute.

**Industry use cases.**
- A platform team gets a mandate to cut a service's cost 40% in a sprint and needs to know which levers to pull first for the fastest, safest win.
- An SLO tightens (TTFT 800 ms → 400 ms) and the team must re-optimise without a cost blowout.
- A new model version regresses cost/quality and the team runs the playbook to recover the envelope.

**Expected competencies.** After this module a participant can profile a live workload to find its dominant bottleneck, prioritise the six levers by impact and effort, sequence them safely (respecting SLO and quality gates), execute a before/after benchmark with correct methodology, quantify the blended improvement, and write an optimisation playbook others can reuse.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Diagnose the dominant bottleneck of a live workload from its profile | LO1 |
| 7.2 | Prioritise and sequence optimisation levers by impact, effort, and risk | LO2, LO3, LO4, LO5 |
| 7.3 | Execute a before/after benchmark with correct, reproducible methodology | LO1 |
| 7.4 | Hold the SLO and quality gate while optimising cost | LO3, LO6 |
| 7.5 | Produce a reusable optimisation playbook and defend the result | LO6 |

## Technical Content

### 1. The optimisation method

A disciplined optimisation follows a loop, never ad-hoc tinkering:

1. **Baseline & target.** Sign the current profile (latency percentiles, throughput knee, quality scores, cost/1k) and state the target as an SLO-and-budget pair (e.g., "hold TTFT p95 ≤ 800 ms and quality within gate; cut cost/1k by ≥ 40%").
2. **Diagnose.** Find the dominant bottleneck: is it under-utilised GPU (→ serving), oversized model (→ compression), uniform expensive routing (→ cascade), flat over-provisioning (→ autoscaling), or untracked waste (→ FinOps)?
3. **Prioritise.** Rank levers by expected Riyal-saved per engineering-day and by risk to SLO/quality.
4. **Apply one lever, re-measure.** Change one thing; re-run the *identical* harness; attribute the delta. Never bundle changes — you lose attribution.
5. **Gate.** Confirm SLO and quality gate still pass. Roll back if not.
6. **Iterate** until the target is met, then **document** the playbook.

The single rule that makes it credible: **one change, one re-measurement, one attributed delta.**

### 2. Diagnosing the dominant bottleneck

Map symptoms to levers so participants can read a profile and know where to start:

| Symptom in the profile | Dominant bottleneck | First lever |
|---|---|---|
| GPU util low, requests queue, serial serving | serving inefficiency | continuous batching / vLLM (M2) |
| High TTFT from long shared prompts | redundant prefill | prefix cache (M2) |
| Model barely fits, decode slow, memory-bound | oversized precision | quantisation (M3) |
| Every request uses the flagship model | uniform expensive routing | cascade (M4) |
| Flat capacity, low off-peak utilisation | over-provisioning | autoscaling (M5) |
| Spend rising, no attribution, surprises | ungoverned cost | FinOps (M6) |

Most live workloads have *several* bottlenecks; diagnosis is about finding the *dominant* one to attack first, because fixing it changes the profile and may re-order the rest.

### 3. Prioritising and sequencing levers

Not all levers are equal in impact, effort, or risk. A rough ordering for a typical LLM service (calibrate to the actual profile):

| Lever | Typical impact | Effort | SLO/quality risk | Notes |
|---|---|---|---|---|
| Continuous batching (vLLM) | very high | low | low | usually the first and biggest win |
| Prefix + semantic cache | high | low | low–med (cache correctness) | huge if prefixes are shared |
| Quantisation | high | med | med (quality gate) | unlocks cheaper GPUs |
| Routing cascade | high | med | med (mis-routing) | best once a cheap tier exists |
| Autoscaling | high | med–high | med (cold start) | biggest infra-cost lever |
| FinOps governance | enabling | med | low | makes the rest measurable/durable |

Sequencing matters: serving first (it reshapes the whole profile), then compression (creates the cheap tier), then routing (uses that tier), then autoscaling (scales the optimised unit), with FinOps wrapping all of it. Applying autoscaling before serving optimisation, for instance, just autoscales an inefficient unit.

### 4. Before/after benchmarking done right

The optimisation is only as credible as its benchmark. Rules (all from Module 1, now enforced):
- **Identical harness and load profile** before and after — same prompts, same rates, same warm-up, same open/closed loop.
- **Same SLO definition** and the *same quality gate* — cost improvements that breach either do not count.
- **Attribute per lever** — a table with one row per lever showing its marginal contribution, so the total is explainable, not magical.
- **Report blended, real numbers** — cost/1k, latency percentiles, quality scores, GPU-hours — with the config that produced them.
- **Reproducible** — anyone can re-run and get the same result; the config is committed beside the numbers.

A before/after that changes the load profile, relaxes the SLO, or skips the quality gate is the cardinal sin of the course — it manufactures a win that does not exist.

### 5. The optimisation playbook

The durable deliverable is a **playbook**: for Musaed, an ordered checklist of levers, each with its trigger ("when cost/1k exceeds X" or "when SLO tightens"), its expected saving, its risk, and its gate. A playbook turns optimisation from a heroic project into a mechanical operation any on-call engineer can run. It closes the FinOps loop: an alert (Module 6) points to a playbook entry, which names a lever (Modules 2–5), which has an expected, measured saving. This is the operating capability the course exists to build.

### 6. Common mistakes & production considerations

**Common mistakes**
1. Bundling several changes, then being unable to attribute the improvement.
2. Optimising a non-dominant bottleneck first (polishing while the real problem persists).
3. Relaxing the SLO or dropping the quality gate to make the number look better.
4. Changing the load profile between before and after.
5. A one-off heroic optimisation with no playbook, so the win erodes and can't be repeated.
6. Ignoring interaction effects (quantisation changes the routing frontier; caching changes the autoscaling signal) — re-measure downstream levers after an upstream change.

**Production considerations**
- Optimisation is continuous: schedule periodic re-profiling because traffic, models, and prices drift.
- Keep every before/after in a versioned `BENCHMARKS.md` history — it is the audit trail and the regression guard.
- Tie the playbook to the FinOps alerts and the autoscaling config so response is automatic where possible and mechanical where not.
- Interaction effects are real: after quantising, re-tune the routing threshold and the autoscaling per-GPU knee, because the numbers they depend on have moved.

## Code Examples

### The optimisation ledger: attribute each lever's contribution

```python
# tools/optimization_ledger.py
"""Accumulate the before/after benchmark as one attributed row per lever,
so the blended improvement is explainable, not magical. Enforces that the
harness/SLO/quality gate are held constant across steps.
"""
from dataclasses import dataclass, field


@dataclass
class Step:
    lever: str
    cost_per_1k: float       # SAR
    ttft_p95_ms: float
    quality: float           # system answer-correctness
    note: str = ""


@dataclass
class Ledger:
    slo_ttft_ms: float
    quality_floor: float
    steps: list[Step] = field(default_factory=list)

    def add(self, step: Step) -> None:
        # Guard: an improvement that breaks the SLO or quality gate does NOT count
        assert step.ttft_p95_ms <= self.slo_ttft_ms, f"{step.lever} breaches TTFT SLO"
        assert step.quality >= self.quality_floor, f"{step.lever} fails quality gate"
        self.steps.append(step)

    def report(self) -> None:
        base = self.steps[0]
        print(f"{'lever':<28}{'SAR/1k':>9}{'Δ%':>7}{'TTFT p95':>10}{'quality':>9}")
        for s in self.steps:
            delta = (s.cost_per_1k - base.cost_per_1k) / base.cost_per_1k * 100
            print(f"{s.lever:<28}{s.cost_per_1k:>9.4f}{delta:>6.0f}%"
                  f"{s.ttft_p95_ms:>9.0f}m{s.quality:>9.1f}")
        total = (self.steps[-1].cost_per_1k - base.cost_per_1k) / base.cost_per_1k * 100
        print(f"\nblended cost change vs baseline: {total:.0f}%")


if __name__ == "__main__":
    L = Ledger(slo_ttft_ms=800, quality_floor=80.5)
    L.add(Step("baseline (unbatched)", 0.104, 640, 82.1))
    L.add(Step("+ vLLM batching+cache", 0.017, 760, 82.1, "M2"))
    L.add(Step("+ INT4 quantisation", 0.011, 700, 81.3, "M3"))
    L.add(Step("+ routing cascade", 0.0035, 700, 81.6, "M4"))
    L.add(Step("+ autoscaling (blended)", 0.0021, 720, 81.6, "M5"))
    L.report()   # blended cost change vs baseline: ~ -98%
```

### The Musaed optimisation playbook (as executable config)

```yaml
# playbooks/musaed_optimization.yaml
# Ordered levers with triggers, expected savings, risk, and gate.
# An alert (M6) points here; each entry names a lever (M2-M5).
service: musaed
slo: { ttft_p95_ms: 800, e2e_p95_ms: 4000 }
quality_gate: { correctness_floor: 80.5, arabic_parity_pt: 1.0, safety_regressions: 0 }
levers:
  - id: serving-batching
    trigger: "gpu_membw_util < 0.5 OR requests_queue > 0"
    action: "enable vLLM continuous batching + prefix cache + streaming"
    expected_saving: "~6x cost/1k"
    risk: low
  - id: quantise-int4
    trigger: "model_barely_fits OR decode_membw_bound"
    action: "AWQ-INT4 with bilingual calibration; run quality gate"
    expected_saving: "~1.5x + smaller GPU"
    risk: medium
  - id: routing-cascade
    trigger: "share_large > 0.6 AND traffic_difficulty_skewed"
    action: "enable cache->small->large cascade; tune escalate_below on frontier"
    expected_saving: "~40-56% blended"
    risk: medium
  - id: autoscale
    trigger: "offpeak_util < 0.4 AND demand_variable"
    action: "KEDA queue-depth autoscaling; warm floor=trough+buffer"
    expected_saving: "~50-65% GPU-hours"
    risk: medium
  - id: finops-govern
    trigger: "always"
    action: "attribution dashboard + rate alerts + showback"
    expected_saving: "durability; catches regressions"
    risk: low
```

## Hands-on Lab 7 — Run the End-to-End Optimisation

| | |
|---|---|
| **Objective** | Integrate Labs 1–6 into one attributed before/after optimisation of Musaed, hold the SLO and quality gate throughout, quantify the blended improvement, and write the reusable playbook — the direct rehearsal for the capstone |
| **Duration** | 50 minutes (Day 3 H3 kickoff; continues into the capstone build) |
| **Setup** | All prior lab checkpoints available; `git checkout lab7-integrate`; the signed baseline from Lab 1; the standard harness |

**Instructions & tasks**
1. *(10 min)* Restate the target as an SLO-and-budget pair; load the signed baseline as step 0 of the `Ledger`.
2. *(15 min)* Apply the levers in sequence (serving → quantise → route → autoscale), re-running the identical harness after each and adding an attributed `Step`. The `Ledger` guards refuse any step that breaks the SLO or quality gate.
3. *(10 min)* Handle an interaction effect: after quantisation, re-tune the routing threshold and confirm the frontier knee moved; record it.
4. *(5 min)* Produce the before/after report (cost/1k, TTFT p95, quality, GPU-hours) and the blended improvement.
5. *(5 min)* Fill `playbooks/musaed_optimization.yaml` with *your* measured expected savings.
6. *(5 min)* Commit: `perf(all): end-to-end optimisation, ~40-60x cost/1k at gate-passing quality + playbook`.

**Expected output**
```
lever                         SAR/1k     Δ%  TTFT p95  quality
baseline (unbatched)          0.1040     0%     640m     82.1
+ vLLM batching+cache         0.0170   -84%     760m     82.1
+ INT4 quantisation           0.0110   -89%     700m     81.3
+ routing cascade             0.0035   -97%     700m     81.6
+ autoscaling (blended)       0.0021   -98%     720m     81.6
blended cost change vs baseline: -98%   (SLO held, quality gate passed)
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Ledger assertion fails on a step | That lever breached SLO or quality gate | Roll back / re-tune; do not relax the gate |
| Blended number looks too good | A change also altered the load profile | Re-run with the identical harness |
| Routing frontier "wrong" after quantise | Interaction effect not re-measured | Re-tune escalate_below on the quantised tier |
| Can't attribute the win | Multiple levers applied at once | Redo one-change-one-measurement |

**Instructor notes.** This lab is the capstone in miniature — protect it. The lesson is the *ledger*: every Riyal saved is attributed to a named lever and gated, so the final number is defensible. Have each pair name their single biggest lever and their one interaction-effect surprise. Fast finishers extend the playbook with a rollback runbook per lever.

## Mini Exercises

**Quiz (5 questions)**
1. What is the one rule that makes an optimisation claim credible? → one change, one re-measurement, one attributed delta.
2. Why optimise the *dominant* bottleneck first? → fixing it reshapes the profile and may re-order the remaining levers.
3. Why is serving optimisation usually sequenced before autoscaling? → autoscaling an inefficient unit just scales the inefficiency.
4. Give one interaction effect between levers. → quantisation shifts the routing frontier; caching changes the autoscaling signal (any valid pair).
5. What makes a before/after benchmark invalid? → changed load profile, relaxed SLO, or a skipped quality gate.

**Diagnosis exercise.** Given three anonymised profiles (one GPU-starved-and-serial, one flagship-for-everything, one flat-over-provisioned), name each dominant bottleneck and the first lever.

**Design exercise.** Write the trigger, expected saving, risk, and gate for one new playbook entry not covered above (e.g., speculative decoding or a bigger batch window), and place it in the sequence.

**Discussion questions.**
- Your mandate is "40% cheaper this sprint." Which two levers do you pull first and why?
- How do you keep an optimisation win from eroding over the following quarter?

## Case Study — The 40%-in-a-Sprint Mandate

**Scenario.** Leadership hands the Musaed platform team a hard mandate: cut cost per 1,000 requests by 40% within one two-week sprint, with zero SLO or quality regression, on the live service.

**Business context.** The service was already on vLLM (batching done) but ran the full 13B model in BF16 for every request on a flat, peak-provisioned fleet. The team's instinct was to buy time by adding GPUs (wrong direction).

**Technical challenge.** Find 40% in two weeks, safely, with attributable evidence.

**Constraints.** Two-week sprint; no SLO or quality regression; changes to a live citizen service must be reversible; the model may be quantised but a full retrain is out of scope.

**Solution approach (facilitate, don't lecture).** (1) Diagnose: dominant waste is uniform flagship routing + flat provisioning. (2) Sequence: quantise to INT4 (gate passes) to create a cheaper unit and a candidate small tier; add a routing cascade (biggest blended win, ~50%); then autoscale the now-cheaper fleet. (3) Apply one lever per change, ledger each, hold the gate. (4) Wrap in FinOps attribution so the saving is proven per lever and won't erode. Result: ~70% cost/1k reduction (well past the 40% target), SLO held, every Riyal attributed, playbook written.

**Discussion questions.**
1. Why is "add GPUs" the wrong first move under a cost-cut mandate?
2. Which lever gave the biggest blended saving here, and why?
3. How does the ledger make the result defensible to leadership?
4. What keeps the win from eroding after the sprint?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Blended cost/1k reduction | Cost | ≥ 40% (course reference achieves far more) | ledger vs baseline |
| SLO held throughout | Reliability | TTFT p95 ≤ 800 ms at every step | harness per step |
| Quality gate held | Quality | within threshold at every step | gate per step |
| Attribution completeness | Rigour | one row per lever, explainable total | ledger |
| Playbook produced | Operability | ordered levers with triggers + savings | playbook YAML |
| Interaction effect handled | Rigour | ≥ 1 downstream re-tune recorded | ledger note |

**Example benchmark table (filled during lab):**

| Step | Lever | SAR/1k | TTFT p95 | Quality | SLO/gate |
|---|---|---|---|---|---|
| 0 | baseline | 0.104 | 640 | 82.1 | ref |
| 1 | serving (M2) | 0.017 | 760 | 82.1 | pass |
| 2 | quantise (M3) | 0.011 | 700 | 81.3 | pass |
| 3 | routing (M4) | 0.0035 | 700 | 81.6 | pass |
| 4 | autoscale (M5) | 0.0021 | 720 | 81.6 | pass |

## Required Visuals and Training Assets

### Diagrams
1. **The optimisation loop** — *Purpose:* the method. *Elements:* baseline → diagnose → prioritise → apply-one → gate → iterate → document. *Style:* cycle diagram.
2. **Symptom-to-lever map** — *Purpose:* diagnosis aid. *Elements:* profile symptoms on the left, levers on the right, arrows. *Style:* mapping table graphic.
3. **The attribution waterfall** — *Purpose:* the defensible win. *Elements:* a waterfall chart from baseline cost/1k down through each lever's contribution to the final blended cost. *Style:* waterfall chart.

### Images (screenshots)
1. **`optimization_ledger.py` output** — *why:* attributed before/after; *content:* the per-lever table with SLO/quality held.
2. **The waterfall chart** — *why:* leadership-ready evidence; *content:* baseline → levers → final.
3. **The playbook YAML** — *why:* the durable deliverable; *content:* ordered levers with triggers and savings.

### Simulations
1. **Bundled-change trap** — *Setup:* apply three levers at once. *Expected behaviour:* big improvement, zero attribution. *Learning objective:* one change, one measurement.
2. **Wrong-first-lever** — *Setup:* autoscale before serving optimisation. *Expected behaviour:* small saving; the dominant bottleneck persists. *Learning objective:* diagnose the dominant bottleneck first.

### Interactive Activities
- **Diagnose-and-sequence relay (15 min):** teams receive a live profile, agree the dominant bottleneck and lever order, and defend the sequence.
- **Playbook build (10 min):** pairs draft one playbook entry (trigger/saving/risk/gate) and slot it into the ordered list.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `optimization_profiles.jsonl` | Three anonymised live-workload profiles | JSONL | 3 items | Diagnosis exercise |
| `baseline_signed.json` | The Lab 1 signed baseline (reused) | JSON | small | Ledger step 0 |
| `musaed_optimization.yaml` | Playbook template | YAML | small | Playbook deliverable |

### Demo Requirements
- **Instructor demo:** run the ledger live, adding levers and showing the guard reject a gate-breaking step.
- **Student demo:** a pair presents its attribution waterfall and names its biggest lever + interaction surprise.
- **Expected outputs:** an attributed before/after ledger, a filled playbook, and a blended-improvement number with SLO/gate held.

---

# Final Capstone Project

## Title: Before/After Optimisation of the Musaed National Assistant

## Project Scenario

You are the newly assigned performance and cost engineer for **Musaed (مساعد)**, the national citizen-services assistant. Leadership has issued a mandate: Musaed must meet its published SLO during the salary-day and Hajj surges **and** cut its cost per 1,000 requests by at least 40% versus the signed baseline — without any regression in bilingual answer quality or safety. You are handed the unoptimised service (the Lab 1 baseline) and the six levers you built across Labs 2–6. Your job is to deliver, and defend, a rigorous before/after optimisation of the same live workload.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Signed baseline & target (LO1):** reproduce the signed baseline (latency percentiles, throughput knee, quality scores, cost/1k, GPU-hours) and state the target as an explicit SLO-and-budget pair.
2. **Serving optimisation (LO2):** Musaed on vLLM with continuous batching, prefix caching, and streaming; re-benchmarked on the identical harness; ≥ 4× throughput at the SLO.
3. **Compression (LO3):** a quantised model (AWQ-INT4 or justified alternative) that passes a bilingual, safety-inclusive quality gate defined in advance; memory and decode gains measured.
4. **Routing (LO3):** a multi-tier cache→small→large cascade with a tuned escalation threshold on the quality/cost frontier; deflection, escalation, and blended cost measured; system quality within gate.
5. **Autoscaling (LO4):** a Kubernetes KEDA deployment scaling on queue depth (not CPU) across the real 24-hour demand curve; GPU-hours vs flat-peak measured; ≤ 1 surge breach, resolved by a warm buffer.
6. **FinOps (LO5/LO6):** a cost dashboard with per-tier/per-tenant attribution and a rate/deviation budget alert; a 3-year TCO with the build-vs-buy crossover including the sovereignty factor.
7. **Attributed before/after & playbook (LO1/LO6):** an optimisation ledger attributing each lever's contribution with the SLO and quality gate held at every step; a reusable `musaed_optimization.yaml` playbook; ≥ 40% blended cost/1k reduction proven.

**One extension (choose at least one):**
- Speculative decoding (draft model) with a measured TTFT/throughput gain and quality check.
- FP8 serving on a Hopper/Ada GPU with a native-tensor-core throughput comparison to INT4.
- MIG partitioning of the cheap tier with a utilisation/cost comparison.
- Spot-GPU burst capacity behind the on-demand baseline, with a reclamation-safety test.
- A rollback runbook per playbook lever, exercised once on the live stack.

## Architecture (target state)

```
                 ┌── Tier 0: semantic cache (no GPU) ──┐
client ─► router ┼── Tier 1: small model (MIG / L4)  ──┼─► streamed answer
   │             └── Tier 2: large model (AWQ-INT4 13B, KEDA-autoscaled A100/L40S)
   │                         ▲ queue-depth signal → KEDA → replicas (warm floor→peak)
   └─ telemetry (tier, tenant, tokens) ─► Prometheus ─► Grafana cost dashboard + budget alerts
                                                  └─► attribution → showback → FinOps loop
Benchmark: identical harness before & after ─► ledger (per-lever, SLO+gate held) ─► playbook
```

## Deliverables

1. Repository URL (instructor-shared) with full history and all lab checkpoints integrated.
2. `BENCHMARKS.md` with the signed baseline row and one row per lever, on the identical harness, plus the blended before/after.
3. The optimisation `Ledger` output (attributed per lever) and the attribution waterfall.
4. A working cost dashboard screenshot + a firing budget-alert screenshot + the `tco.py` crossover.
5. `playbooks/musaed_optimization.yaml` filled with *your* measured expected savings.
6. `DECISIONS.md`: five one-paragraph engineering decisions with rationale (e.g., precision choice, escalation threshold, warm-floor sizing, build-vs-buy, lever sequence).
7. A 6-minute before/after defence: baseline → target → sequence → attributed result → SLO/gate evidence.

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: signed baseline reproduced + target stated | Day 3 H3 | instructor spot-check of `BENCHMARKS.md` |
| M-B: serving + compression applied and gated | Day 3 H3 | vLLM row + passing quality gate |
| M-C: routing + autoscaling integrated | Day 3 H4 | frontier plot + replica-vs-demand |
| M-D: FinOps + attributed ledger + playbook | Day 3 H4 | dashboard + ledger + YAML |
| M-E: before/after defence | Day 3 H5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Baseline & benchmark methodology | 15 | Signed, reproducible; identical harness before/after; percentiles + goodput | Minor gaps (weak warm-up, one config unrecorded) | Mean-only, changed harness, no baseline |
| Serving optimisation | 15 | vLLM batching+cache+streaming; ≥ 6× at SLO; measured | Works; < 4× or thin measurement | No batching / unmeasured |
| Compression with quality gate | 15 | Quantised, bilingual+safety gate defined in advance and passed; memory/decode gains | Gated but monolingual or post-hoc threshold | Ungated compression / quality regression shipped |
| Routing cascade | 15 | Tuned on frontier; deflection+blended cost measured; system quality within gate | Works; threshold untuned or system-eval thin | Mis-routing, per-tier-only eval |
| Autoscaling | 15 | Queue-depth signal; curve-tracked; GPU-hours saved; surge held by buffer | Works; CPU-ish signal or surge breach unresolved | No autoscaling / flat peak |
| FinOps & TCO | 15 | Attribution + rate alert + full TCO with sovereignty crossover | Dashboard partial or TCO omits hidden costs | Vanity metrics, GPU-hours×price "TCO" |
| Attributed result & playbook + defence | 10 | Ledger attributes every lever, SLO+gate held; ≥ 40% proven; crisp defence; playbook reusable | Result works; attribution or playbook thin | Bundled changes, unattributable, can't defend |

**Pass ≥ 70. Distinction ≥ 90.** Extensions add up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the benchmark evidence first* (identical harness, per-lever attribution, gate held), defence second — the point of the course is that the numbers speak and are honest.
- Anti-pattern flags that cap a criterion at 70%: a relaxed SLO between before and after; a quality gate defined after seeing results; a monolingual gate; bundled changes with no attribution; a "TCO" that is GPU-hours × price.
- Verify one claim live: ask the participant to re-run one lever's before/after on the projector, or to break the casing invariance in the cascade quality check and show the gate catch it.

## Bonus Tasks (for early finishers / distinction seekers)

1. Speculative decoding with a draft model; report TTFT/throughput gain and confirm no quality change.
2. FP8-vs-INT4 shoot-out on the available GPUs with a requests-per-Riyal comparison.
3. A sensitivity analysis of the build-vs-buy crossover to GPU price and sovereignty cost.
4. A `sim-regression` reproduction: introduce a new model version that regresses cost, then run the playbook to recover the envelope and write the 10-line postmortem.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** Which LLM inference phase is compute-bound and which is memory-bandwidth-bound? → prefill compute-bound; decode memory-bandwidth-bound.
**Q2.** Define goodput and why it beats throughput as an SLO metric. → requests/s that also met the SLO; throughput counts SLO-violating completions too.
**Q3.** Why report latency percentiles instead of the mean? → the mean hides the tail (p95/p99) that users actually feel.
**Q4.** Why does continuous batching beat static batching for LLMs? → token-level scheduling; finished requests leave and new ones join without draining, no head-of-line blocking.
**Q5.** What resource, not compute, usually caps concurrent requests on a GPU, and what fixes its waste? → KV-cache memory; PagedAttention.
**Q6.** When does prefix caching help most? → long, identical shared prefix (system prompt) across many requests.
**Q7.** Does streaming reduce total compute? → no; it reduces *perceived* latency by delivering the first token early.
**Q8.** Why does quantisation speed up decode, not just save memory? → decode is memory-bandwidth-bound; fewer bits = fewer bytes moved per token.
**Q9.** Why must Musaed's quantisation calibration be bilingual? → English-only calibration degrades Arabic quality.
**Q10.** What must a quality gate be defined relative to, and when? → the full-precision baseline, with thresholds fixed *before* quantising.
**Q11.** What is the danger of complexity routing without a cascade? → confident wrong answers when a hard query is mis-routed to the small model.
**Q12.** What does the cascade escalation threshold trade off? → cost (escalate less) vs quality (escalate more).
**Q13.** Should you evaluate routing tiers individually or the routed system? → the routed system end-to-end.
**Q14.** Why is CPU utilisation the wrong autoscaling signal for GPU inference? → CPU stays idle while the GPU saturates and requests queue; it never triggers.
**Q15.** Why must GPU services scale up on a leading signal? → cold start (node boot + image pull + model load) is slow; reacting after the breach is too late.
**Q16.** When is scale-to-zero dangerous? → on an always-on interactive SLO path (first-request cold-start stall).
**Q17.** Why track unit cost, not just total spend? → total can fall from lower traffic (bad) or higher efficiency (good); only unit cost distinguishes them.
**Q18.** Name three costs a "GPU-hours × price" TCO omits. → people/on-call, idle/warm-floor, compliance/sovereignty (also storage, network, lock-in).
**Q19.** Build-vs-buy hinges on which variable, plus which possible override? → request volume (the crossover); sovereignty/data-residency can override it.
**Q20.** State the one rule that makes an optimisation claim credible. → one change, one re-measurement, one attributed delta (identical harness, SLO + gate held).

## Practical Assessments

**PA-1 (30 min, Day 1):** Given a flawed benchmark harness (mean-only, no warm-up, closed-loop concurrency=1) and a raw sample set, produce a correct baseline: percentiles, the knee, and cost/1k. Scored on: methodology fixes (40%), correct numbers (40%), reproducibility/config recorded (20%).

**PA-2 (30 min, Day 2):** Given a quantised model that fails on Arabic and a mis-tuned router, triage: identify the calibration cause, propose the fix, and set an escalation threshold on a provided frontier. Scored against the model answer (calibration diagnosis 40%, routing/frontier reasoning 40%, gate discipline 20%).

**PA-3:** Capstone (rubric above) — 40% of course grade. Labs completion + PA-1/PA-2 — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (7 labs) | 30% | checkpoint commits + `BENCHMARKS.md` rows |
| PA-1 + PA-2 | 20% | artefacts + notes |
| Quiz | 10% | 10-question selection |
| Capstone | 40% | attributed before/after, repo-first |

Badge issuance (Optimisation badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero integrity flags (fabricated benchmark numbers or relaxed-SLO "wins" are checked by re-running one lever live).

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone the course org repos; push checkpoint tags (`lab1-baseline` … `lab7-integrate`, `bad-harness`, all `sim-*` branches)
- [ ] Pre-warm the model cache on classroom GPU nodes: `allam-13b-instruct` (BF16), `allam-13b-awq-int4`, the distilled `student_3b_awq`
- [ ] Verify GPU quota and driver/CUDA versions on the training cluster; confirm each pair has a GPU seat (A100/L40S) or a working fallback endpoint
- [ ] Dry-run all 7 labs end-to-end on a clean cluster **and** on the CPU-only / shared-endpoint fallback
- [ ] Stand up the shared Kubernetes cluster with KEDA + Prometheus + Grafana; import the cost-dashboard template
- [ ] Regenerate the signed baseline and the quality-gate reference scores against the pinned vLLM/AWQ versions
- [ ] Print A4 posters: latency triangle, latency anatomy, precision ladder, routing topology, demand-curve provisioning, optimisation waterfall
- [ ] Load datasets (`musaed_prompts`, `traffic_profile`, `routing_corpus`, `billing/telemetry samples`) into the shared drive
- [ ] Prepare the shared leaderboard (knee, cost/1k, blended improvement) and confirm network access to any required registries (or pre-pull images)

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + git + a GitHub account; `kubectl` and cluster credentials (provided)
- [ ] `pip install vllm autoawq httpx numpy prometheus-client` (or use the provided GPU container image)
- [ ] NVIDIA driver + CUDA compatible with the classroom vLLM build; verify `nvidia-smi` and a one-line vLLM smoke test
- [ ] Grafana/Prometheus access confirmed; `helm`/`kubectl` reachable to the training cluster
- [ ] Clone the course repo; run `make doctor` (validates GPU access, model cache, cluster reachability; prints ✓/✗)
- [ ] Load-test and analysis tools (`loadgen.py`, `cost.py`, `tco.py`) run locally against a provided mock endpoint

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| No GPU seat / GPU quota exhausted | High | Shared inference endpoint + CPU-only "quality-only" path; pre-book quota; pair on one GPU |
| vLLM/CUDA/driver version mismatch | High | Pin versions; provide a pre-built container; `make doctor` catches it early |
| Quantisation OOMs on the lab GPU | Medium | Use the provided pre-quantised artefacts; quantise offline |
| Autoscaling never triggers | Medium | Confirm KEDA queries the queue metric, not CPU; check Prometheus wiring |
| Cold-start surge breaches SLO in Lab 5 | Medium | Teach warm buffer + leading signal; it's the intended lesson, then fix live |
| "My optimisation is 100× better" (changed harness) | Medium | Enforce identical harness; the Ledger guards reject SLO/gate breaks |
| Arabic quality regression after INT4 | Medium | Bilingual calibration; it's the M3 lesson, revisited |
| Cost dashboard shows no Riyal | Low | Confirm attribution joins billing to telemetry gpu_seconds |

## Timing Recommendations

- Protect Lab 2 (vLLM bring-up) and Lab 5 (autoscaling) at full length — they are the overrun-prone, highest-value labs.
- If a cohort is strong: pull FP8 serving and speculative decoding into main scope; deepen the TCO sensitivity analysis.
- If a cohort is weak: provide the pre-quantised artefact and a pre-wired KEDA ScaledObject so time goes to *interpreting* results, not fighting infra; never drop the before/after ledger — it is the course's thesis made visible.
- Hard rule: the capstone before/after ledger (Day 3 H4) must start on time; cut discussion and bonus tasks, never the attributed benchmark.

## Discussion Prompts (use during transitions)

1. "Your model is 94% accurate and your service is 40% cheaper. Which number did the citizen feel, and which did the Treasury feel?"
2. "You cut latency 30% by relaxing the quality gate. Did you optimise, or did you just move the problem somewhere the dashboard can't see?"
3. "Who owns the escalation threshold — engineering, product, or risk — when it trades Riyal against citizen-facing quality?"
4. "If your GPU pool is fixed and sovereign, is autoscaling still relevant? What does it become?"
5. "Total spend fell 20% this month. Prove to me that's good news with one chart."

## Wrap-up (Day 3 final 15 minutes)

- Map each capstone requirement to the module that taught it, and each module to a lever on the latency–throughput–cost triangle (one slide).
- Forward pointer: SDA-AIE-390 (AI Engineering Capstone) integrates this optimisation discipline into a full production GenAI system — the before/after playbook produced here becomes the cost-and-performance section of the panel defence.
- Reinforce the thesis: optimisation is a *measured, gated, attributed, repeatable* operating capability — a playbook, not a hero project — and it is what lets the Kingdom run national-scale AI within budget.
- Collect: repo URLs, `BENCHMARKS.md`, the optimisation ledger, `DECISIONS.md`, and the playbook; issue badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.12, vLLM ≥ 0.6, AWQ (autoawq), pydantic v2, and Kubernetes with KEDA ≥ 2.14. GPU prices and SAR conversions are illustrative — replace with the pinned rate card before each delivery. Verify pinned model, driver, and library versions in the course lock file before each delivery.*
