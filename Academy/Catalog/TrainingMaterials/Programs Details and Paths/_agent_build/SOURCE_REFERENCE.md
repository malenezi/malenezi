# SDAIA Module Catalog — Authoritative Source Reference

Source: SDAIA_Academy_Module_Catalog_v2.xlsx (Module Catalog sheet). Use ONLY these facts for cover pages, descriptions, outcomes, topics, tools, assessment. Mark anything not present as "Not specified".


---

## SDA-AIE-214 — Building Retrieval-Augmented Generation Systems

**AR Title:** بناء أنظمة التوليد المعزز بالاسترجاع
**Track:** AI Engineer
مهندس الذكاء الاصطناعي
**Level:** Specialist / متخصص
**Days:** 4  |  **Hours:** 20

**Description (EN):** A deep, practical module on grounding LLMs in enterprise knowledge. Participants build the full RAG pipeline — ingestion, chunking, embedding, vector retrieval, reranking, and generation — and evaluate answer faithfulness systematically. The module covers advanced patterns including hybrid search and multi-document reasoning for production-grade assistants.

**Target Audience:** GenAI engineers building knowledge assistants and enterprise search

**Prerequisites:** SDA-AIE-213

**Learning Outcomes (Bloom-aligned):** • Design end-to-end RAG architectures for enterprise knowledge bases
• Implement ingestion, chunking, and embedding pipelines for heterogeneous documents
• Develop retrieval stacks combining vector, keyword, and hybrid search with reranking
• Evaluate RAG quality using faithfulness, relevance, and answer-correctness metrics
• Optimize retrieval parameters, context construction, and citation grounding
• Validate systems against hallucination and stale-knowledge failure modes

**Topics:** 1. RAG architecture and when to use it versus fine-tuning
2. Document ingestion, parsing, and chunking strategies
3. Embeddings and vector databases
4. Hybrid retrieval and reranking
5. Context construction and citation grounding
6. RAG evaluation frameworks
7. Advanced patterns: multi-hop, agentic RAG
8. Production RAG project

**Tools & Platforms:** Vector DBs (Qdrant/pgvector), LangChain/LlamaIndex, RAGAS, rerankers

**Assessment:** Labs; enterprise RAG project with evaluation

**Next Module(s):** SDA-AIE-311

**Stackability:** RAG badge; prerequisite for Agentic AI Systems Engineering.

---

## SDA-AIE-215 — Fine-Tuning and Adapting Foundation Models

**AR Title:** الضبط الدقيق وتكييف النماذج الأساسية
**Track:** AI Engineer
مهندس الذكاء الاصطناعي
**Level:** Specialist / متخصص
**Days:** 3  |  **Hours:** 15

**Description (EN):** A specialist module on customising foundation models efficiently. Participants prepare instruction datasets, apply parameter-efficient fine-tuning (LoRA/QLoRA), align models with preference optimisation, and quantise them for deployment. The module gives engineers a decision framework for when to prompt, retrieve, or fine-tune.

**Target Audience:** GenAI engineers customising models for domain tasks

**Prerequisites:** SDA-AIE-112; SDA-AIE-213 recommended

**Learning Outcomes (Bloom-aligned):** • Compare prompting, RAG, and fine-tuning strategies for a given requirement
• Design high-quality instruction and preference datasets
• Implement parameter-efficient fine-tuning using LoRA and QLoRA
• Apply quantisation techniques to reduce model footprint
• Evaluate fine-tuned models against baselines with rigorous benchmarks
• Validate adapted models for regression, safety, and domain fitness

**Topics:** 1. Adaptation strategy: prompt vs RAG vs fine-tune
2. Instruction dataset design and curation
3. PEFT methods: LoRA, QLoRA, adapters
4. Preference alignment (DPO) overview
5. Quantisation and efficient inference
6. Evaluation and regression testing of tuned models

**Tools & Platforms:** Hugging Face PEFT/TRL, bitsandbytes, Axolotl, lm-eval-harness

**Assessment:** Labs; domain fine-tuning project

**Next Module(s):** SDA-AIE-311 / SDA-AIE-312

**Stackability:** Model-adaptation badge; elective within GenAI Engineering specialisation.

---

## SDA-AIE-216 — MLOps: Model Deployment and Automation

**AR Title:** عمليات تعلم الآلة: نشر النماذج والأتمتة
**Track:** AI Engineer
مهندس الذكاء الاصطناعي
**Level:** Specialist / متخصص
**Days:** 5  |  **Hours:** 25

**Description (EN):** A comprehensive module on operationalising machine learning. Participants build reproducible training pipelines, register and version models and data, deploy scalable serving endpoints, and automate retraining with monitoring for drift. The module establishes the MLOps backbone that Expert-level reliability and LLMOps modules extend.

**Target Audience:** AI engineers responsible for production ML systems

**Prerequisites:** SDA-AIE-113; SDA-AIE-111

**Learning Outcomes (Bloom-aligned):** • Design end-to-end MLOps architectures spanning training, serving, and monitoring
• Implement reproducible pipelines with data and model versioning
• Deploy models as scalable, containerised inference services
• Develop automated retraining and CI/CD/CT workflows
• Implement monitoring for data drift, concept drift, and performance decay
• Evaluate deployment strategies including canary, blue-green, and shadow releases

**Topics:** 1. MLOps maturity model and system architecture
2. Experiment tracking and model registry
3. Data versioning and feature stores
4. Pipeline orchestration and automation
5. Model serving: batch, online, streaming
6. Drift detection and monitoring
7. Release strategies and rollback
8. MLOps platform project

**Tools & Platforms:** MLflow, DVC, Airflow/Prefect, Docker, Kubernetes basics, Evidently

**Assessment:** Labs; deployed pipeline project

**Next Module(s):** SDA-AIE-312

**Stackability:** MLOps badge; prerequisite for LLMOps and reliability modules.

---

## SDA-AIE-311 — Agentic AI Systems Engineering

**AR Title:** هندسة أنظمة الذكاء الاصطناعي الوكيلي
**Track:** AI Engineer
مهندس الذكاء الاصطناعي
**Level:** Expert / خبير
**Days:** 5  |  **Hours:** 25

**Description (EN):** An expert module on designing, building, securing, and operating enterprise agentic systems that plan, reason, use tools, and manage memory across multi-step workflows. Participants implement ReAct, Plan-and-Execute, and Reflection patterns, orchestrate multi-agent architectures, integrate tools via the Model Context Protocol, and harden agents with guardrails and red-team testing. The module culminates in deploying a production-grade agentic system in a simulated enterprise environment.

**Target Audience:** Senior AI engineers, AI architects, technical leads

**Prerequisites:** SDA-AIE-214

**Learning Outcomes (Bloom-aligned):** • Design agentic architectures with planning, reasoning, tool use, and memory
• Implement ReAct, Plan-and-Execute, and Reflection patterns in working agents
• Develop multi-agent systems with orchestration, delegation, and task routing
• Integrate tools and enterprise APIs using the Model Context Protocol
• Design state management and short/long-term memory with vector stores
• Implement automated guardrails and red-team agents against attacks
• Optimize agent performance, cost, and reliability with tracing and monitoring
• Validate a deployed agentic system in a simulated enterprise environment

**Topics:** 1. Agentic system architectures and components
2. Planning and reasoning patterns: ReAct, Plan-and-Execute, Reflection
3. Tool use, function calling, and MCP integration
4. Memory and state management with vector databases
5. Single-agent versus multi-agent architectures
6. Hierarchical delegation and agent orchestration
7. Flow engineering over prompt engineering
8. Guardrails, security, and adversarial testing
9. Observability, cost optimisation, and monitoring
10. Capstone: enterprise agentic system deployment

**Tools & Platforms:** LangGraph, MCP, vector DBs, agent-tracing platforms (LangSmith), guardrails frameworks

**Assessment:** Labs; security report; deployed agent capstone

**Next Module(s):** SDA-AIE-313 / SDA-AIE-390

**Stackability:** Flagship Expert badge; anchors the GenAI Engineering specialisation. Derived from the existing Advanced Agentic AI Systems programme.

---

## SDA-AIE-312 — LLMOps and Production AI Observability

**AR Title:** عمليات النماذج اللغوية ومراقبة الذكاء الاصطناعي الإنتاجي
**Track:** AI Engineer
مهندس الذكاء الاصطناعي
**Level:** Expert / خبير
**Days:** 4  |  **Hours:** 20

**Description (EN):** An expert module on operating LLM and generative-AI workloads in production. Participants implement tracing, quality monitoring, feedback loops, and incident response for AI services, extending MLOps discipline to non-deterministic systems. The module covers evaluation-in-production, prompt/version management, and reliability engineering for AI platforms.

**Target Audience:** Engineers operating GenAI services at scale

**Prerequisites:** SDA-AIE-216; SDA-AIE-213

**Learning Outcomes (Bloom-aligned):** • Design observability architectures for LLM applications with distributed tracing
• Implement online evaluation, quality scoring, and user-feedback loops
• Develop prompt and model version-management workflows with safe rollouts
• Analyze production incidents in AI systems and build response runbooks
• Implement SLOs, alerting, and reliability dashboards for AI services
• Optimize the operations lifecycle for continuous improvement of deployed LLM systems

**Topics:** 1. From MLOps to LLMOps: what changes
2. Tracing and logging for LLM pipelines
3. Online evaluation and quality monitoring
4. Prompt registries and version management
5. Feedback loops and data flywheels
6. SLOs, alerting, and incident response
7. Reliability engineering for AI platforms

**Tools & Platforms:** LangSmith/Langfuse, OpenTelemetry, Grafana, evaluation pipelines

**Assessment:** Labs; observability dashboard project

**Next Module(s):** SDA-AIE-314 / SDA-AIE-390

**Stackability:** Expert operations badge; part of the MLOps & Reliability specialisation.

---

## SDA-AIE-313 — AI Security, Guardrails and Red Teaming

**AR Title:** أمن الذكاء الاصطناعي والحواجز الوقائية والفريق الأحمر
**Track:** AI Engineer
مهندس الذكاء الاصطناعي
**Level:** Expert / خبير
**Days:** 3  |  **Hours:** 15

**Description (EN):** An expert module on securing AI systems against adversarial threats. Participants analyse attack surfaces including prompt injection, jailbreaks, data poisoning, and model extraction, then design layered defences with guardrails, filtering, and access controls. Structured red-team exercises teach systematic security validation of LLM and agentic applications.

**Target Audience:** Senior engineers, security specialists, AI platform owners

**Prerequisites:** SDA-AIE-213; SDA-AIE-311 recommended

**Learning Outcomes (Bloom-aligned):** • Analyze AI attack surfaces using OWASP LLM Top-10 and threat modelling
• Evaluate systems against prompt injection, jailbreak, and data-exfiltration attacks
• Design layered guardrail architectures for inputs, outputs, and tools
• Implement content filtering, PII protection, and policy enforcement
• Conduct structured red-team exercises against LLM and agentic applications
• Develop security test suites and reporting aligned with governance requirements

**Topics:** 1. AI threat landscape and OWASP LLM Top-10
2. Prompt injection and jailbreak techniques
3. Data poisoning and supply-chain risks
4. Guardrail architecture and policy enforcement
5. Red-teaming methodology and tooling
6. Security evaluation and reporting
7. Compliance alignment with national frameworks

**Tools & Platforms:** Garak/PyRIT, guardrails frameworks, NeMo Guardrails, threat-modelling templates

**Assessment:** Red-team exercise; security assessment report

**Next Module(s):** SDA-AIE-390

**Stackability:** Security badge; required for AI Engineer Expert certificate.

---

## SDA-AIE-314 — AI Performance, Scalability and Cost Optimization

**AR Title:** أداء الذكاء الاصطناعي وقابلية التوسع وتحسين التكلفة
**Track:** AI Engineer
مهندس الذكاء الاصطناعي
**Level:** Expert / خبير
**Days:** 3  |  **Hours:** 15

**Description (EN):** An expert module on engineering AI systems that are fast, scalable, and economical. Participants profile inference workloads, apply batching, caching, quantisation, and routing strategies, and design autoscaling serving infrastructure. The module builds the FinOps discipline to run national-scale AI services within budget.

**Target Audience:** Senior engineers and platform architects

**Prerequisites:** SDA-AIE-216

**Learning Outcomes (Bloom-aligned):** • Analyze latency, throughput, and cost profiles of AI inference workloads
• Implement batching, caching, and streaming optimisations for model serving
• Apply quantisation, distillation, and model-routing to cut serving costs
• Design autoscaling GPU infrastructure for variable demand
• Evaluate build-versus-buy and model-tier trade-offs with TCO analysis
• Develop cost-monitoring dashboards and optimisation playbooks

**Topics:** 1. Performance profiling of inference workloads
2. Serving optimisation: batching, caching, streaming
3. Model compression: quantisation and distillation
4. Model routing and cascade architectures
5. GPU infrastructure and autoscaling
6. AI FinOps: cost monitoring and TCO
7. Optimisation project on a live workload

**Tools & Platforms:** vLLM, TensorRT/ONNX Runtime, Kubernetes autoscaling, cost dashboards

**Assessment:** Optimisation project with before/after benchmark

**Next Module(s):** SDA-AIE-390

**Stackability:** Optimisation badge; part of the MLOps & Reliability specialisation.

---

## SDA-AIE-315 — Enterprise AI Solution Architecture

**AR Title:** معمارية حلول الذكاء الاصطناعي المؤسسية
**Track:** AI Engineer
مهندس الذكاء الاصطناعي
**Level:** Expert / خبير
**Days:** 3  |  **Hours:** 15

**Description (EN):** An expert module that elevates engineers to solution architects. Participants translate business requirements into end-to-end AI architectures, select platforms and integration patterns, and produce architecture documentation and decision records. Case-based design reviews cover real government and enterprise AI scenarios.

**Target Audience:** Senior engineers moving into architecture and technical leadership

**Prerequisites:** SDA-AIE-216; SDA-AIE-213

**Learning Outcomes (Bloom-aligned):** • Translate business requirements into candidate AI solution architectures
• Design integration patterns connecting AI services to enterprise systems
• Evaluate platform, cloud, and sovereignty options against constraints
• Design for security, compliance, and data residency from the outset
• Develop architecture decision records and reference documentation
• Defend architectural choices in structured design reviews

**Topics:** 1. AI solution architecture lifecycle
2. Reference architectures: RAG, agents, ML platforms
3. Enterprise integration and API strategy
4. Cloud, on-premise, and sovereignty considerations
5. Non-functional requirements: security, scale, compliance
6. Architecture documentation and ADRs
7. Design-review simulations on real scenarios

**Tools & Platforms:** Architecture canvases, C4 modelling, cloud reference architectures

**Assessment:** Architecture design package; peer design review

**Next Module(s):** SDA-AIE-390

**Stackability:** Architecture badge; elective for Expert certificate; on-ramp to future AI Solution Architect track.

---

## SDA-AIE-390 — AI Engineering Capstone: Production GenAI System

**AR Title:** مشروع التخرج: نظام ذكاء توليدي إنتاجي
**Track:** AI Engineer
مهندس الذكاء الاصطناعي
**Level:** Expert / خبير
**Days:** 5  |  **Hours:** 25

**Description (EN):** The integrative capstone of the AI Engineer pathway. Teams scope, design, build, secure, and deploy a complete generative-AI system — combining RAG or agents, MLOps automation, observability, and guardrails — for a realistic enterprise brief. Work is assessed through a production demo, security review, and architecture defence before an expert panel.

**Target Audience:** Candidates completing the AI Engineer Expert certificate

**Prerequisites:** SDA-AIE-311 + SDA-AIE-312 + SDA-AIE-313 (or equivalent portfolio)

**Learning Outcomes (Bloom-aligned):** • Design a complete production architecture for an enterprise GenAI use case
• Implement an integrated system combining retrieval, agents, and serving infrastructure
• Develop automated evaluation, monitoring, and guardrail layers
• Validate the system through security testing and load benchmarks
• Optimize cost and performance against defined service objectives
• Defend design decisions and results before a technical panel

**Topics:** 1. Project scoping and requirements engineering
2. System design and architecture review
3. Sprint-based build with mentor checkpoints
4. Evaluation, security, and performance hardening
5. Deployment and operations readiness
6. Final demo, documentation, and panel defence

**Tools & Platforms:** Full track toolchain as selected by teams

**Assessment:** Deployed system; documentation package; panel defence

**Next Module(s):** —

**Stackability:** Completes the AI Engineer Expert (Professional) Certificate.

---

## SDA-DSC-111 — Statistical Foundations for Data Science

**AR Title:** الأسس الإحصائية لعلم البيانات
**Track:** Data Scientist
عالم البيانات
**Level:** Practitioner / ممارس
**Days:** 4  |  **Hours:** 20

**Description (EN):** A rigorous, applied grounding in the statistics that underpin trustworthy data science. Participants master probability, distributions, estimation, hypothesis testing, and regression, applying each concept computationally in Python. The module builds the inferential judgement needed to draw valid conclusions from data.

**Target Audience:** Analysts, graduates, and engineers entering data science

**Prerequisites:** SDA-FND-103; SDA-FND-104 recommended

**Learning Outcomes (Bloom-aligned):** • Apply probability rules and distributions to model real-world uncertainty
• Analyze sampling variability using confidence intervals and standard errors
• Implement hypothesis tests and interpret p-values and effect sizes correctly
• Develop linear and logistic regression models and diagnose their assumptions
• Evaluate statistical claims for common fallacies and misuse
• Simulate statistical processes computationally to validate analytical results

**Topics:** 1. Probability and common distributions
2. Descriptive statistics and sampling
3. Estimation and confidence intervals
4. Hypothesis testing and effect sizes
5. Correlation, causation, and confounding
6. Linear and logistic regression
7. Simulation and resampling methods

**Tools & Platforms:** Python, SciPy, statsmodels, Jupyter

**Assessment:** Labs; statistical analysis project

**Next Module(s):** SDA-DSC-112 / SDA-AIE-111

**Stackability:** Core statistics badge; required for all Specialist Data Scientist modules.

---

## SDA-DSC-112 — Data Visualization and Storytelling

**AR Title:** تصور البيانات وسرد القصص
**Track:** Data Scientist
عالم البيانات
**Level:** Practitioner / ممارس
**Days:** 3  |  **Hours:** 15

**Description (EN):** A craft-focused module on turning analysis into influence. Participants apply perception science to design honest, compelling visualisations, build interactive dashboards, and structure data narratives for executive audiences. The module closes the last mile between analytical work and organisational decisions.

**Target Audience:** Data scientists, analysts, BI professionals

**Prerequisites:** SDA-FND-104

**Learning Outcomes (Bloom-aligned):** • Apply visual-perception principles to select effective chart types
• Design clear, honest visualisations that avoid distortion and clutter
• Develop interactive dashboards for self-service exploration
• Construct data narratives structured around audience and decision
• Evaluate visualisations through critique and iterative refinement
• Present analytical findings persuasively to executive stakeholders

**Topics:** 1. Perception science and visual encoding
2. Chart selection and design principles
3. Colour, annotation, and decluttering
4. Interactive dashboards and BI tools
5. Data storytelling structure and flow
6. Executive communication and presentation lab

**Tools & Platforms:** Plotly, Power BI/Tableau, Matplotlib/Seaborn

**Assessment:** Dashboard project; storytelling presentation

**Next Module(s):** SDA-DSC-211

**Stackability:** Communication badge; required for Data Scientist Practitioner certificate.

---

## SDA-DSC-211 — Advanced Machine Learning Methods

**AR Title:** أساليب تعلم الآلة المتقدمة
**Track:** Data Scientist
عالم البيانات
**Level:** Specialist / متخصص
**Days:** 4  |  **Hours:** 20

**Description (EN):** A specialist module that deepens modelling skill beyond the foundations. Participants master gradient-boosting frameworks, imbalanced and cost-sensitive learning, model interpretability with SHAP, and rigorous validation design. The emphasis is on winning reliable performance on messy, real-world tabular problems.

**Target Audience:** Data scientists progressing to specialist modelling roles

**Prerequisites:** SDA-AIE-111 (cross-listed); SDA-DSC-111

**Learning Outcomes (Bloom-aligned):** • Develop high-performance models with XGBoost and LightGBM
• Design validation schemes that respect leakage, grouping, and time order
• Apply techniques for imbalanced, noisy, and cost-sensitive problems
• Analyze model behaviour using SHAP and permutation importance
• Optimize feature pipelines and model ensembles for tabular data
• Evaluate models for stability, calibration, and business impact

**Topics:** 1. Gradient boosting deep dive
2. Validation design and leakage prevention
3. Imbalanced and cost-sensitive learning
4. Model interpretability: SHAP and beyond
5. Calibration and uncertainty estimates
6. Ensembling and stacking strategies
7. Applied modelling challenge

**Tools & Platforms:** XGBoost, LightGBM, SHAP, scikit-learn, Optuna

**Assessment:** Modelling challenge; interpretability report

**Next Module(s):** SDA-DSC-212 / SDA-DSC-213

**Stackability:** Advanced ML badge; core of the Data Scientist Specialist certificate.

---

## SDA-DSC-212 — Time Series Analysis and Forecasting

**AR Title:** تحليل السلاسل الزمنية والتنبؤ
**Track:** Data Scientist
عالم البيانات
**Level:** Specialist / متخصص
**Days:** 3  |  **Hours:** 15

**Description (EN):** A specialist module on modelling data that evolves over time. Participants decompose series, build statistical and ML-based forecasting models, and evaluate them with time-aware backtesting. Applications include demand planning, workforce projections, and economic indicators relevant to national programmes.

**Target Audience:** Data scientists and analysts working with temporal data

**Prerequisites:** SDA-DSC-111; SDA-DSC-211 recommended

**Learning Outcomes (Bloom-aligned):** • Analyze trend, seasonality, and autocorrelation structure in time series
• Develop classical forecasting models including ARIMA and exponential smoothing
• Implement ML and gradient-boosting approaches with engineered temporal features
• Design backtesting frameworks with proper time-based validation
• Evaluate forecasts using scale-appropriate accuracy and uncertainty metrics
• Compare model families to select the right approach per use case

**Topics:** 1. Time-series structure and decomposition
2. Stationarity and autocorrelation
3. ARIMA and exponential smoothing
4. Feature-based ML forecasting
5. Probabilistic forecasts and intervals
6. Backtesting and forecast evaluation
7. Forecasting case study

**Tools & Platforms:** statsmodels, Prophet, sktime, LightGBM

**Assessment:** Forecasting project with backtest report

**Next Module(s):** SDA-DSC-311

**Stackability:** Forecasting badge; part of Analytics & Experimentation specialisation.

---

## SDA-DSC-213 — Experimentation, A/B Testing and Causal Inference

**AR Title:** التجريب واختبارات A/B والاستدلال السببي
**Track:** Data Scientist
عالم البيانات
**Level:** Specialist / متخصص
**Days:** 4  |  **Hours:** 20

**Description (EN):** A specialist module on answering "what actually works" with data. Participants design and analyse randomised experiments, compute power and sample sizes, and apply causal-inference methods — matching, difference-in-differences, and instrumental variables — when experiments are impossible. The module turns data scientists into trusted advisors on policy and product decisions.

**Target Audience:** Data scientists supporting product, policy, and programme decisions

**Prerequisites:** SDA-DSC-111

**Learning Outcomes (Bloom-aligned):** • Design randomised experiments with valid randomisation units and guardrail metrics
• Compute statistical power, sample sizes, and minimum detectable effects
• Analyze experiment results with correct variance estimation and multiple-testing control
• Apply quasi-experimental methods including matching and difference-in-differences
• Evaluate causal claims from observational data using DAG-based reasoning
• Communicate experimental evidence and uncertainty to decision-makers

**Topics:** 1. Causal thinking and potential outcomes
2. Experiment design and randomisation
3. Power analysis and sample sizing
4. Analysis pitfalls: peeking, multiple testing
5. Quasi-experiments: matching, DiD, IV
6. Causal graphs and confounding
7. Experimentation case study

**Tools & Platforms:** statsmodels, DoWhy/EconML, experiment simulators

**Assessment:** Experiment design and analysis project

**Next Module(s):** SDA-DSC-311

**Stackability:** Causal badge; core of Analytics & Experimentation specialisation.

---

## SDA-DSC-214 — Modern Data Engineering for AI Systems

**AR Title:** هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي
**Track:** Data Scientist
عالم البيانات
**Level:** Specialist / متخصص
**Days:** 5  |  **Hours:** 25

**Description (EN):** A comprehensive module on building modern, scalable, production-ready data architectures that feed AI and analytics. Participants trace the evolution from warehouses and lakes to the Lakehouse, master Delta Lake with ACID transactions and compute-storage separation, and work with ELT, streaming, data quality, and governance. A hands-on build of a local Mini-Lakehouse with Delta Lake and PySpark anchors the learning.

**Target Audience:** Data engineers, data scientists, systems and AI architects, data-infrastructure leads

**Prerequisites:** SDA-FND-104; SDA-FND-103

**Learning Outcomes (Bloom-aligned):** • Compare data warehouses, data lakes, and Lakehouse architectures across use cases
• Explain compute-storage separation and its impact on cost, elasticity, and scale
• Design ELT pipelines suited to modern cloud data environments
• Implement Delta Lake tables with ACID transactions and schema enforcement
• Develop streaming and event-driven ingestion patterns for real-time data
• Apply data-quality, observability, and governance controls across pipelines
• Build a working Mini-Lakehouse with Delta Lake and PySpark
• Connect Lakehouse components to AI, reporting, and analytics consumers

**Topics:** 1. Evolution of data architecture: warehouse, lake, Lakehouse
2. Compute-storage separation and cloud economics
3. ETL versus ELT in modern stacks
4. Delta Lake and ACID transactions
5. Streaming data and event-driven architectures
6. Data quality, observability, and governance
7. Hands-on: building a Mini-Lakehouse
8. Serving data to AI and BI workloads

**Tools & Platforms:** PySpark, Delta Lake, dbt, Kafka basics, Great Expectations

**Assessment:** Labs; Mini-Lakehouse build project

**Next Module(s):** SDA-DSC-215 / SDA-DSC-313

**Stackability:** Data-engineering badge; anchors the Data Engineering for AI specialisation. Derived from the existing Modern Data Engineering programme.

---

## SDA-DSC-215 — Big Data Analytics with Spark

**AR Title:** تحليلات البيانات الضخمة باستخدام Spark
**Track:** Data Scientist
عالم البيانات
**Level:** Specialist / متخصص
**Days:** 3  |  **Hours:** 15

**Description (EN):** A specialist module on analysing datasets too large for a single machine. Participants master distributed computing concepts, write performant Spark transformations and SQL, and tune jobs through partitioning and caching. The module scales every prior analytics skill to enterprise data volumes.

**Target Audience:** Data scientists and engineers working with large-scale data

**Prerequisites:** SDA-DSC-214 or equivalent Spark exposure

**Learning Outcomes (Bloom-aligned):** • Explain distributed execution: partitions, shuffles, and lazy evaluation
• Develop analytical workloads with Spark DataFrames and Spark SQL
• Optimize job performance through partitioning, caching, and join strategies
• Implement scalable feature-engineering and ML pipelines with Spark MLlib
• Analyze query plans to diagnose and resolve performance bottlenecks
• Design batch analytics workflows on Lakehouse storage

**Topics:** 1. Distributed computing fundamentals
2. Spark DataFrames and Spark SQL
3. Shuffles, partitioning, and caching
4. Performance tuning and query plans
5. Spark MLlib pipelines at scale
6. Big-data analytics project

**Tools & Platforms:** PySpark, Spark SQL, MLlib, Delta Lake

**Assessment:** Labs; large-scale analytics project

**Next Module(s):** SDA-DSC-313

**Stackability:** Big-data badge; part of the Data Engineering for AI specialisation.

---

## SDA-DSC-311 — Decision Science and Optimization Modeling

**AR Title:** علم القرار ونمذجة التحسين
**Track:** Data Scientist
عالم البيانات
**Level:** Expert / خبير
**Days:** 3  |  **Hours:** 15

**Description (EN):** An expert module that moves from predicting outcomes to prescribing actions. Participants formulate linear and integer optimisation models, run simulations under uncertainty, and combine ML predictions with optimisation to recommend optimal decisions. Applications span resource allocation, scheduling, and policy planning.

**Target Audience:** Senior data scientists supporting operational and strategic decisions

**Prerequisites:** SDA-DSC-211; SDA-DSC-213 recommended

**Learning Outcomes (Bloom-aligned):** • Formulate business problems as linear and integer optimisation models
• Implement optimisation solutions using modern solver frameworks
• Design simulations to evaluate decisions under uncertainty
• Integrate ML predictions into prescriptive decision pipelines
• Analyze trade-offs with sensitivity and scenario analysis
• Evaluate decision-support systems for robustness and adoption

**Topics:** 1. From predictive to prescriptive analytics
2. Linear and integer programming
3. Solver frameworks and model building
4. Monte Carlo simulation
5. Predict-then-optimise pipelines
6. Sensitivity and scenario analysis
7. Decision-science case project

**Tools & Platforms:** PuLP/OR-Tools, SimPy, pandas

**Assessment:** Optimisation project with decision memo

**Next Module(s):** SDA-DSC-390

**Stackability:** Decision-science badge; Expert elective.

---

## SDA-DSC-312 — GenAI-Augmented Data Science Workflows

**AR Title:** سير عمل علم البيانات المعزز بالذكاء التوليدي
**Track:** Data Scientist
عالم البيانات
**Level:** Expert / خبير
**Days:** 3  |  **Hours:** 15

**Description (EN):** An expert module on multiplying data-science productivity with generative AI. Participants use LLMs for code generation, automated EDA, synthetic data, and unstructured-text analysis, while building reproducible, verifiable workflows. The module defines the professional standard for responsible AI-assisted analysis.

**Target Audience:** Experienced data scientists modernising their workflow

**Prerequisites:** SDA-DSC-211; SDA-FND-102

**Learning Outcomes (Bloom-aligned):** • Integrate AI coding assistants into analysis workflows with verification discipline
• Apply LLMs to extract structure and insight from unstructured text data
• Develop synthetic-data strategies for augmentation and privacy protection
• Design reproducible, version-controlled analysis pipelines with AI assistance
• Evaluate AI-generated analytical artefacts for correctness and bias
• Implement agent-assisted automation for recurring analytics tasks

**Topics:** 1. AI-assisted coding and analysis patterns
2. LLMs for text analytics and feature extraction
3. Synthetic data generation and privacy
4. Reproducibility and verification discipline
5. Automating recurring analytics with agents
6. Responsible use and quality assurance

**Tools & Platforms:** AI coding assistants, LLM APIs, Git, notebook-to-pipeline tooling

**Assessment:** Augmented-workflow project with verification report

**Next Module(s):** SDA-DSC-390

**Stackability:** GenAI-workflow badge; Expert elective bridging to AI Engineer track.

---

## SDA-DSC-313 — Real-Time and Streaming Data Analytics

**AR Title:** التحليلات اللحظية وتدفقات البيانات
**Track:** Data Scientist
عالم البيانات
**Level:** Expert / خبير
**Days:** 3  |  **Hours:** 15

**Description (EN):** An expert module on analytics that cannot wait for batch jobs. Participants build streaming pipelines with Kafka and Spark Structured Streaming, implement windowed aggregations and real-time feature computation, and serve live metrics and alerts. The module completes the modern data stack for real-time AI applications.

**Target Audience:** Senior data scientists and engineers building real-time products

**Prerequisites:** SDA-DSC-214; SDA-DSC-215 recommended

**Learning Outcomes (Bloom-aligned):** • Design streaming architectures with appropriate delivery and consistency guarantees
• Implement event ingestion and processing with Kafka and Structured Streaming
• Develop windowed aggregations, joins, and stateful stream computations
• Build real-time feature pipelines serving online ML models
• Implement live dashboards, alerting, and anomaly detection on streams
• Evaluate latency, throughput, and correctness trade-offs in streaming systems

**Topics:** 1. Streaming architecture and event-driven design
2. Kafka fundamentals and event modelling
3. Spark Structured Streaming
4. Windowing, watermarks, and state
5. Real-time features for online ML
6. Live monitoring and anomaly detection
7. Streaming analytics project

**Tools & Platforms:** Kafka, Spark Structured Streaming, Delta Live patterns, Grafana

**Assessment:** Streaming pipeline project

**Next Module(s):** SDA-DSC-390

**Stackability:** Streaming badge; completes the Data Engineering for AI specialisation.

---

## SDA-DSC-390 — Data Science Capstone: From Data to Decision

**AR Title:** مشروع التخرج: من البيانات إلى القرار
**Track:** Data Scientist
عالم البيانات
**Level:** Expert / خبير
**Days:** 5  |  **Hours:** 25

**Description (EN):** The integrative capstone of the Data Scientist pathway. Teams take an ambiguous organisational question through framing, data engineering, modelling, validation, and a decision-ready recommendation, defended before an expert panel. The project produces a portfolio-grade artefact demonstrating end-to-end professional competence.

**Target Audience:** Candidates completing the Data Scientist Expert certificate

**Prerequisites:** SDA-DSC-211 + SDA-DSC-213 + SDA-DSC-214 (or equivalent portfolio)

**Learning Outcomes (Bloom-aligned):** • Frame an ambiguous organisational question as a tractable analytical problem
• Design and build the data pipeline supporting the analysis
• Develop and validate models with rigorous, leakage-free methodology
• Analyze results for robustness, fairness, and practical significance
• Construct a decision-ready recommendation with quantified uncertainty
• Defend methodology and findings before a technical panel

**Topics:** 1. Problem framing and scoping workshop
2. Data acquisition and pipeline build
3. Modelling and validation sprints
4. Robustness, fairness, and sensitivity checks
5. Decision memo and visual narrative
6. Final presentation and panel defence

**Tools & Platforms:** Full track toolchain as selected by teams

**Assessment:** Portfolio project; decision memo; panel defence

**Next Module(s):** —

**Stackability:** Completes the Data Scientist Expert (Professional) Certificate.