const { P, F, W, H, M, footer, darkBase, medallionChip } = require("./lib.js");

module.exports = function (pres, K) {
  // ---------- 1. TITLE ----------
  {
    const s = darkBase(pres);
    s.addText("SDAIA ACADEMY  ·  SPECIALIST TRACK  ·  SDA-DSC-214", {
      x: M, y: 1.35, w: W - 2 * M, h: 0.3, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: 11.5, bold: true, charSpacing: 2.4, color: P.gold });
    s.addText("Modern Data Engineering\nfor AI Systems", {
      x: M, y: 1.85, w: W - 2 * M - 1.2, h: 2.0, isTextBox: true, margin: 0,
      fontFace: F.head, fontSize: 46, bold: true, color: P.onDark, lineSpacingMultiple: 1.02 });
    s.addText("Building the trustworthy data platform behind Masar (مسار) — the national smart-mobility system", {
      x: M, y: 3.95, w: W - 2 * M - 1.6, h: 0.6, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: 15.5, color: P.onDarkMut });
    [["5 days", "25 learning hours"], ["8 modules", "8 hands-on labs"], ["1 capstone", "Masar Mini-Lakehouse"]]
      .forEach((c, i) => {
        const x = M + i * 3.5;
        s.addText(c[0], { x, y: 4.95, w: 3.2, h: 0.42, isTextBox: true, margin: 0,
          fontFace: F.head, fontSize: 22, bold: true, color: [P.bronze, P.silver, P.gold][i] });
        s.addText(c[1], { x, y: 5.38, w: 3.2, h: 0.3, isTextBox: true, margin: 0,
          fontFace: F.body, fontSize: 12, color: P.onDarkMut });
      });
    s.addText("PySpark · Delta Lake · dbt · Kafka · Great Expectations", {
      x: M, y: 6.25, w: W - 2 * M, h: 0.3, isTextBox: true, margin: 0,
      fontFace: F.code, fontSize: 11.5, color: P.teal });
    medallionChip(s, W - M - 0.63, 1.36, null, true);
    footer(s, pres, "Instructor deck · v1.0", true);
    s.addNotes("Open by naming the course promise: by Friday every participant owns a working, tested, governed Lakehouse feeding both an AI model and a BI dashboard. Do not open with tool names. Open with the Masar platform.");
  }

  // ---------- 2. THE QUESTION ----------
  K.statement(pres, {
    kicker: "The question behind every slide in this deck",
    text: "“What happens to Masar’s AI system\nif this part of the data platform fails?”",
    size: 33,
    sub: "This course is not about learning five tools. It is about engineering ONE trustworthy data product for AI.\nEvery concept, every lab, every case study answers the same question. Ask it out loud at each transition.",
    notes: "This slide is the spine of the whole delivery. Return to it at every module boundary. If a participant can answer this question for each layer of the platform by Friday, the course worked.",
  });

  // ---------- 3. COURSE AT A GLANCE ----------
  K.table(pres, {
    kicker: "Course profile", title: "SDA-DSC-214 at a glance",
    head: ["Field", "Details"],
    widths: [2.9, 9.19],
    rowH: 0.42, fs: 12,
    rows: [
      ["Arabic title", "هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي"],
      ["Level / duration", "Specialist · 5 days × 5 learning hours = 25 hours"],
      ["Audience", "Data engineers, data scientists, systems and AI architects, data-infrastructure leads"],
      ["Prerequisites", "SDA-FND-104 · SDA-FND-103"],
      ["Assessment", "8 labs (30%) · 2 practical assessments (20%) · quiz (10%) · Mini-Lakehouse capstone (40%)"],
      ["Stackability", "Data-engineering badge · anchors the Data Engineering for AI specialisation · next: SDA-DSC-215 / SDA-DSC-313"],
      ["Tools", "PySpark 3.5 · Delta Lake 3.2 · dbt 1.7 · Kafka (single broker) · Great Expectations 0.18 · Redis"],
    ],
    note: "All code, table names and identifiers remain in English — Saudi enterprise convention; mixed-language identifiers break SQL tooling.",
  });

  // ---------- 4. LEARNING OUTCOMES ----------
  K.cards(pres, {
    kicker: "Learning outcomes", title: "What you will be able to do by Thursday evening",
    cols: 4, cardH: 1.95, cards: [
      { n: "1", h: "Compare architectures", t: "Warehouse, lake and Lakehouse across real use cases — and say which one a workload belongs in.", color: P.bronze },
      { n: "2", h: "Explain decoupling", t: "Compute–storage separation and its impact on cost, elasticity and scale.", color: P.bronze },
      { n: "3", h: "Design ELT pipelines", t: "Incremental, idempotent transformations suited to modern cloud data platforms.", color: P.silver },
      { n: "4", h: "Implement Delta Lake", t: "ACID transactions, schema enforcement, MERGE, time travel, maintenance.", color: P.silver },
      { n: "5", h: "Develop streaming ingestion", t: "Event-driven patterns with exactly-once semantics and event-time correctness.", color: P.teal },
      { n: "6", h: "Apply quality & governance", t: "Expectations, observability signals, PII classification and PDPL controls.", color: P.teal },
      { n: "7", h: "Build a Mini-Lakehouse", t: "The whole medallion, orchestrated as one idempotent, recoverable DAG.", color: P.gold },
      { n: "8", h: "Serve AI and BI", t: "Point-in-time-correct features and a conformed star schema from one governed gold layer.", color: P.gold },
    ],
    note: "LO1–LO8 are the assessment map: every rubric criterion and every quiz item traces back to one of these eight.",
  });

  // ---------- 5. GOLDEN THREAD ----------
  K.medallion(pres, {
    kicker: "The golden thread", title: "Masar (مسار) — one platform, evolved for five days",
    lead: "Never a throwaway dataset. Every lab adds a component to the same Lakehouse, so the capstone is assembly, not a new build.",
    sources: ["trips CSV (batch)", "drivers / vehicles", "payments", "zones + weather", "GPS via Kafka (stream)"],
    bronze: { tables: "bronze.trips · bronze.gps_events · bronze.drivers", contract: "Append-only, as-received schema, never mutated. Carries _ingested_at, _source_file, _batch_id." },
    silver: { tables: "silver.trips · silver.vehicle_positions", contract: "One row per trip_id. Enforced schema + CHECK constraints. Quality-gated. Conformed units and timezone." },
    gold:   { tables: "gold.fact_trip · gold.eta_features · gold.zone_hourly_demand", contract: "Business-modelled, documented grain. Feature table is point-in-time correct. PDPL-safe at the boundary." },
    bi: "gold.fact_trip\ngold.dim_driver\ngold.dim_zone\ngold.dim_date\n→ ops dashboard",
    ai: "gold.eta_features\n→ offline training\n→ Redis online store\nmasar:features:zone:*",
    note: "One source of truth, two contracts. The analyst's “trips per zone” and the model's “zone demand feature” cannot silently disagree — because they are derived from the same silver.",
  });

  // ---------- 6. FIVE-DAY MAP ----------
  K.table(pres, {
    kicker: "Delivery plan", title: "Five days, five deliverables",
    head: ["Day", "Theme", "Modules", "Theory / Lab", "Deliverable at end of day"],
    widths: [0.75, 2.35, 2.6, 1.25, 5.14], rowH: 0.62, fs: 11.5,
    rows: [
      ["Day 1", "Foundations and economics", "M1 Evolution · M2 Compute–storage", "55 / 45", "Architecture decision record + a cost and elasticity model for Masar"],
      ["Day 2", "Pipelines — ETL to ELT", "M3 ETL vs ELT", "40 / 60", "ELT pipeline: raw trips landed and transformed to a conformed silver.trips"],
      ["Day 3", "The Lakehouse table", "M4 Delta Lake and ACID", "35 / 65", "Delta silver.trips with constraints, MERGE upserts, time travel, OPTIMIZE/VACUUM"],
      ["Day 4", "Real-time and trust", "M5 Streaming · M6 Quality and governance", "40 / 60", "Structured-Streaming GPS ingestion + a Great Expectations quality gate"],
      ["Day 5", "Build and serve", "M7 Mini-Lakehouse · M8 Serving · Capstone", "25 / 75", "End-to-end Mini-Lakehouse feeding an AI feature table and a BI star schema"],
    ],
    note: "Each “hour” is 50 minutes of instruction plus a 10-minute buffer. Schedule the long break around Dhuhr; Day 5 afternoon is deliberately build-heavy.",
  });

  // ---------- 7. HOW YOU ARE ASSESSED ----------
  K.chart(pres, {
    kicker: "Assessment", title: "How the 100 points are earned",
    type: pres.ChartType.doughnut, legend: true, showValue: false,
    colors: [P.bronze, P.silver, P.teal, P.gold],
    data: [{ name: "Weighting", labels: ["Labs (8)", "Practical assessments", "Quiz", "Capstone"], values: [30, 20, 10, 40] }],
    opts: { holeSize: 55, showPercent: false, showValue: true, dataLabelFormatCode: '0"%"', dataLabelColor: "FFFFFF", dataLabelFontSize: 13, dataLabelFontBold: true },
    side: { h: "Graded from the platform first", items: [
      "Evidence order: the running platform and repository, then the demo — the point of the course is that the platform speaks for itself.",
      "Pass ≥ 70. Distinction ≥ 90. Extensions add up to +5 (capped at 100) only if mandatory scope is ≥ 80.",
      "Anti-pattern flags cap a criterion at 70%: feature leakage, non-idempotent gold, VACUUM RETAIN 0, alert-only quality gate, raw rider IDs in BI output, streaming without a dedicated checkpoint.",
      "Badge issuance also requires zero academic-integrity flags and no PDPL red flags.",
    ] },
    takeaway: "PA-1 (Delta recovery, Day 3) · PA-2 (streaming exactly-once, Day 4) · PA-3 (feature-leakage audit, Day 5).",
  });

  // ---------- 8. ENVIRONMENT ----------
  K.cards(pres, {
    kicker: "Before we start", title: "Your environment for the week",
    cols: 3, cardH: 2.5, cards: [
      { h: "Primary path", t: "Local Spark 3.5 + delta-spark 3.2 on Java 17, plus a single-broker Kafka and Redis via docker compose. Run `make doctor` — it validates every dependency and prints a ✓/✗ table.", color: P.bronze },
      { h: "Fallback path", t: "A hosted notebook: Databricks Community Edition, or Colab with pyspark and delta installed. Verified the week before delivery. The streaming lab needs Kafka — images are pre-pulled.", color: P.silver },
      { h: "The starter repo", t: "Clone it once. Checkpoint tags (`lab1-start` … `lab8-start`) let anyone fast-forward to any lab's starting state without losing the day.", color: P.teal },
      { h: "The data", t: "A seeded synthetic Masar generator — trips CSV, GPS NDJSON, drivers, vehicles, zones, payments, weather — with defects deliberately injected and documented.", color: P.gold },
      { h: "Pairs, rotated daily", t: "Pair a strong-SQL participant with a strong-Python/Spark participant. ELT rewards one background, streaming the other; the skill transfer is the point.", color: P.bronze },
      { h: "Language rule", t: "Delivery in English or Arabic. All code, table names, column names and commit messages stay in English — production convention in Saudi enterprise environments.", color: P.silver },
    ],
    note: "Environment failures are the single biggest risk to Day 1. Send LAB_00_Environment_Setup.md two days before the course and staff the first hour with a floater.",
  });
};
