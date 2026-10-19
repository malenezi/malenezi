# Rafeeq Mini: Advanced Agentic AI System 
## Haya BinYousef
A multi-agent customer support system built with strict security boundaries, deterministic routing, and highly observable telemetry.

**Training Center:** Developed as the final capstone project for the Advanced Agentic AI Systems Engineering program by [SDAIA Academy](https://github.com/SDAIAAcademy).

---

##  System Pipeline & Architecture

The system pipeline departs from standard LLM wrappers by implementing a highly compartmentalized **Router-Specialist Pattern**:

1. **Thin Supervisor (Router):** Acts as the primary orchestrator. It receives the user query, analyzes the intent, and delegates the task without holding any business logic or executing tools itself.
2. **OrdersAgent (Read-Only):** A specialized agent restricted to order tracking and status lookups. It operates with a `0` reflection compute budget to maximize speed.
3. **RefundAgent (Write-Access):** A high-stakes specialized agent handling financial transactions. It is constrained by:
   * **Bounded Reflection:** Allowed a maximum of `1` reflection loop to verify policy compliance.
   * **Human-in-the-Loop (HITL):** Hard-coded approval gate for any refund exceeding `500 SAR`.
4. **Tool Execution (MCP):** All database mocks and external tools are executed securely via the Model Context Protocol (MCP) over `stdio`.

##  Dataset Used

The project relies on **Synthetic Public Evaluation Data** (`data/public/eval_public.jsonl`). 
* The dataset consists of deterministic, pre-labeled cases designed to test functional routing accuracy and security edge cases.
* It includes synthetic customer profiles, policies, and adversarial prompts (e.g., prompt injection and boundary bypass attempts) to rigorously evaluate the system's defenses.

##  Results Achieved (Release Scorecard)

The system was evaluated against strict deterministic criteria, achieving perfect scores across all critical gates:

* **Functional Accuracy:** `100%` (Perfect intent routing and outcome generation).
* **Security Pass Rate:** `100%` (Successfully blocked all 8 standard adversarial attacks and the custom `L-SEC-01` learner threat).
* **Unauthorized Writes:** `0` (Zero cross-customer data leakage).
* **Performance Optimization:** Implemented a secure policy caching mechanism (keyed purely by `locale` and `category` to prevent data leakage), reducing policy retrieval latency from **~3.26ms down to ~0.26ms** (a >10x speedup).
* **Telemetry Privacy:** `100%` Trace Redaction. All Personally Identifiable Information (PII) is successfully stripped from the final `trace.jsonl` logs.
│   └── public/
│       └── eval_public.jsonl          # The synthetic dataset used for evaluation
├── trace.jsonl                        # Redacted, structured telemetry logs
├── LEARNING_PROGRESS.md               # Cumulative JSON logs of the 14 completed technical tasks
└── README.md                          # This documentation file
