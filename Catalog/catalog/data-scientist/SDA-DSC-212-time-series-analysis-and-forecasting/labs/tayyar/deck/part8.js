const L = require("./lib"); const { C, F } = L;

module.exports = function part8(pres, R, IMG) {
  const S = () => pres.addSlide();
  let s, y;

  // ================================================= CAPSTONE SECTION =====
  s = S(); L.bg(s, C.deep);
  s.addShape("ellipse", { x: -2.0, y: -1.8, w: 6.0, h: 6.0, fill: { color: C.teal },
    line: { width: 0 }, transparency: 62 });
  L.titleSlideText(s, "FINAL CAPSTONE PROJECT · 40% OF THE COURSE GRADE",
    "Tayyar — a backtested\nday-ahead forecasting service",
    "The operations-planning unit has asked for a production-ready day-ahead pipeline for the Central Operating Area, plus a backtest report it can put in front of the regulator and the control room.");
  s.addText("The repository IS the evidence: a stranger should clone it, run one command, and reproduce every number in your report.",
    { x: 0.9, y: 5.55, w: 10.5, h: 0.8, isTextBox: true, fontFace: F.head, fontSize: 16,
      italic: true, color: C.gold, margin: 0, lineSpacing: 22 });
  s.addNotes("Everything they built in Labs 1 to 7 is a component. The capstone is the integration plus one extension of their own.");

  // ================================================ CAPSTONE REQUIREMENTS =
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Seven mandatory requirements, one extension", "CAPSTONE · SCOPE");
  const req = [
    ["1", "Clean, reproducible pipeline", "LO1", "A src/tayyar package running end to end from a committed config. Fixed splits and seeds, pinned dependencies, one command regenerates every reported number."],
    ["2", "Decomposition & diagnostics", "LO1", "tz-aware hourly index with explicit frequency and gap policy. MSTL with reported daily and weekly strengths. Stationarity report with (d, D) justified."],
    ["3", "At least three model families", "LO2 LO3", "Seasonal-naive baseline, one classical model (SARIMAX with temperature, or ETS), one feature-based ML model. All leakage-safe and reproducible."],
    ["4", "Calibrated probabilistic forecast", "LO5", "A 90% day-ahead interval with empirical coverage in 0.88–0.92 on the held-out window. Coverage reported marginally AND by hour-of-day."],
    ["5", "Rolling-origin backtest", "LO4", "≥ 50 origins, refit each origin, 24 h horizon, no leakage. MASE, a % metric, coverage and pinball per model, with a per-origin breakdown flagging Eid and heatwave weeks."],
    ["6", "Model-selection decision", "LO6", "DECISION_RECORD.md: one production model recommended with a Diebold-Mariano test over the runner-up, stated constraints and weights, flip-conditions, a fallback, and a monitoring contract."],
    ["7", "Report & communication", "LO5 LO6", "BACKTEST_REPORT.md an operator would accept — the table, the decision, the known limits — plus a decision-language reserve brief with no unexplained jargon."],
  ];
  req.forEach(([n, t, lo, d], i) => {
    const yy = y + i * 0.7;
    L.card(s, 0.62, yy, 8.7, 0.64, i % 2 ? C.paperAlt : "FFFFFF");
    L.circle(s, 0.78, yy + 0.11, 0.42, i < 3 ? C.mid : (i < 5 ? C.teal : C.deep), n);
    s.addText(t, { x: 1.32, y: yy + 0.04, w: 2.6, h: 0.3, isTextBox: true, fontFace: F.body,
      fontSize: 12, bold: true, color: C.ink, margin: 0 });
    s.addText(lo, { x: 1.32, y: yy + 0.33, w: 2.6, h: 0.26, isTextBox: true, fontFace: F.body,
      fontSize: 9.5, bold: true, color: C.teal, margin: 0 });
    s.addText(d, { x: 3.95, y: yy + 0.02, w: 5.25, h: 0.6, isTextBox: true, fontFace: F.body,
      fontSize: 9.5, color: C.muted, margin: 0, valign: "middle", lineSpacing: 12.5 });
  });
  L.card(s, 9.6, y, 3.12, 5.05, C.deep);
  s.addText("CHOOSE ONE EXTENSION", { x: 9.85, y: y + 0.15, w: 2.7, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 10, bold: true, color: C.gold, charSpacing: 1.5, margin: 0 });
  ["Multi-area global model across all four operating areas, backtested per area",
   "Adaptive conformal (ACI / EnbPI) — show improved CONDITIONAL summer-afternoon coverage",
   "Weather-uncertainty propagation: widen the interval for temperature-forecast error",
   "Automated retraining trigger, with a test proving it fires on injected drift",
   "Champion / challenger harness that continuously re-evaluates against the incumbent"]
    .forEach((t, i) => {
      s.addText("▪  " + t, { x: 9.85, y: y + 0.55 + i * 0.9, w: 2.7, h: 0.85, isTextBox: true,
        fontFace: F.body, fontSize: 10, color: "CFE3F5", margin: 0, lineSpacing: 13.5 });
    });
  L.card(s, 0.62, y + 5.05, 8.7, 0.6, "FDF3E3");
  s.addText("The extension adds up to +5 bonus, capped at 100, and only if mandatory scope scores ≥ 80. Pass ≥ 70. Distinction ≥ 90.",
    { x: 0.88, y: y + 5.05, w: 8.2, h: 0.6, isTextBox: true, valign: "middle", fontFace: F.body,
      fontSize: 11.5, bold: true, color: C.warn, margin: 0 });
  s.addNotes("Read requirement 4's coverage band aloud and mean it — 0.88 to 0.92 is a gate, not guidance. It is the single requirement most submissions miss, because they calibrate on the wrong window.");

  // ============================================= CAPSTONE RUBRIC + GATES ==
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "How it is graded — and what caps a criterion at 70%", "CAPSTONE · RUBRIC AND ANTI-PATTERN FLAGS");
  L.table(s, [
    L.hrow(["Criterion", "Wt", "90–100%", "< 70%"]),
    L.crow(["Data, index & decomposition", "12", "Correct tz-aware frequency, gap policy, MSTL with justified strengths and transform", "Broken index, silent gaps, wrong period"]),
    L.crow(["Stationarity & modelling rigour", "15", "ADF + KPSS reconciled, minimal differencing, ≥ 3 families all leak-safe and diagnosed", "Leakage present, no baseline, or invalid AIC comparisons"], { fill: "F7FAFC" }),
    L.crow(["Feature engineering (leakage-safe)", "15", "assert_no_leakage PASS; lags from the ACF; .shift(1) rolling; Hijri calendar correct", "Shuffle split or centred window survives; future exog used"]),
    L.crow(["Probabilistic calibration", "15", "Coverage 0.88–0.92 marginal AND conditional; CQR justified; sharpest at target", "Confidence where a prediction interval belongs; coverage off target"], { fill: "F7FAFC" }),
    L.crow(["Backtesting validity", "18", "≥ 50 origins, refit each, no leak, MASE + coverage + pinball + breakdown", "Fit-once or in-sample scoring; a single split; no baseline"], { fill: "EAF2EC", boldCols: [1] }),
    L.crow(["Model selection & evidence", "15", "DM-significant choice, weights stated, flip-conditions + fallback + monitoring", "Lowest-MAE pick with no significance test and no stated limits"]),
    L.crow(["Report, brief & reproducibility", "10", "One-command reproduction; decision-language brief; auditor-ready", "Irreproducible; jargon-only; numbers not regenerable"], { fill: "F7FAFC" }),
  ], 0.62, y, 12.1, { size: 8.8, rowH: 0.42, colW: [2.5, 0.5, 4.85, 4.25] });
  s.addText("Anti-pattern flags — any one of these caps its criterion at 70%", { x: 0.62, y: y + 3.78,
    w: 12.1, h: 0.35, isTextBox: true, fontFace: F.body, fontSize: 13.5, bold: true, color: C.bad, margin: 0 });
  const flags = ["train_test_split(shuffle=True), anywhere", "a centred rolling feature",
    "a \"backtest\" that scores in-sample", "MAPE reported without MASE or a baseline",
    "a champion declared on a sub-1% gap with no Diebold-Mariano test",
    "a confidence interval where a prediction interval is required"];
  flags.forEach((t, i) => {
    const x = 0.62 + (i % 3) * 4.13, yy = y + 4.13 + Math.floor(i / 3) * 0.55;
    L.card(s, x, yy, 3.9, 0.52, "FBEEEC");
    s.addText("✕   " + t, { x: x + 0.18, y: yy, w: 3.6, h: 0.52, isTextBox: true, valign: "middle",
      fontFace: F.body, fontSize: 10.5, color: C.bad, margin: 0, lineSpacing: 13 });
  });
  L.card(s, 0.62, y + 5.3, 12.1, 0.62, "E7EFF7");
  s.addText("Grade from the repository and its reproducibility FIRST — clone it, run the one command, check the numbers regenerate — then the demo. Verify one calibration claim live: ask for empirical coverage on the held-out window, broken down by hour-of-day.",
    { x: 0.88, y: y + 5.3, w: 11.54, h: 0.62, isTextBox: true, valign: "middle", fontFace: F.body,
      fontSize: 11, italic: true, color: C.deep, margin: 0 });
  s.addNotes("Reward candour explicitly. A submission that names where the model loses and ships a fallback should outscore a silent, marginally sharper one. Say this to the room before they start, so it changes what they build.");

  // ============================================== MILESTONES + ASSESSMENT =
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Milestones, gates and the rest of the grade", "ASSESSMENT PACKAGE");
  s.addText("Capstone milestones", { x: 0.62, y, w: 6.0, h: 0.32, isTextBox: true, fontFace: F.body,
    fontSize: 13.5, bold: true, color: C.ink, margin: 0 });
  const ms = [["M-A", "Clean series + decomposition + stationarity report", "End Day 1", "index / gaps / strengths spot-check"],
              ["M-B", "Classical + ML models producing 24 h forecasts", "End Day 2", "leak check PASS; forecast vs actual plotted"],
              ["M-C", "Calibrated 90% interval", "Day 3 H1", "coverage 0.88–0.92 on the held-out window"],
              ["M-D", "Rolling-origin backtest + DM selection", "Day 3 H3", "≥ 50 origins, no leak, champion chosen"],
              ["M-E", "Decision record + extension + demo", "Day 3 H5", "rubric scoring"]];
  ms.forEach(([k, t, d, g], i) => {
    const yy = y + 0.4 + i * 0.82;
    L.card(s, 0.62, yy, 6.0, 0.74, i % 2 ? C.paperAlt : "FFFFFF");
    s.addShape("roundRect", { x: 0.78, y: yy + 0.16, w: 0.62, h: 0.42, rectRadius: 0.05,
      fill: { color: i === 4 ? C.deep : C.mid }, line: { width: 0 } });
    s.addText(k, { x: 0.78, y: yy + 0.16, w: 0.62, h: 0.42, isTextBox: true, align: "center",
      valign: "middle", fontFace: F.body, fontSize: 10.5, bold: true, color: C.paper, margin: 0 });
    s.addText(t, { x: 1.52, y: yy + 0.06, w: 3.55, h: 0.32, isTextBox: true, fontFace: F.body,
      fontSize: 11.5, bold: true, color: C.ink, margin: 0 });
    s.addText("GATE:  " + g, { x: 1.52, y: yy + 0.37, w: 3.55, h: 0.3, isTextBox: true, fontFace: F.body,
      fontSize: 9.5, color: C.muted, margin: 0 });
    s.addText(d, { x: 5.15, y: yy, w: 1.32, h: 0.74, isTextBox: true, align: "right", valign: "middle",
      fontFace: F.body, fontSize: 10.5, bold: true, color: C.teal, margin: 0 });
  });
  s.addText("The rest of the grade", { x: 6.9, y, w: 5.8, h: 0.32, isTextBox: true, fontFace: F.body,
    fontSize: 13.5, bold: true, color: C.ink, margin: 0 });
  const comp = [["Lab completion (7 labs)", 30, C.mid, "checkpoint commits + expected outputs"],
                ["PA-1 + PA-2", 20, C.teal, "artefacts + diagnosis notes"],
                ["Quiz (10 of 20 questions)", 10, C.gold, "15 minutes, closed book"],
                ["Capstone", 40, C.deep, "rubric, repository-first"]];
  comp.forEach(([t, w, col, ev], i) => {
    const yy = y + 0.4 + i * 0.82;
    L.card(s, 6.9, yy, 5.82, 0.74, C.paperAlt);
    s.addText(String(w) + "%", { x: 7.1, y: yy, w: 0.95, h: 0.74, isTextBox: true, valign: "middle",
      fontFace: F.head, fontSize: 22, bold: true, color: col, margin: 0 });
    s.addText(t, { x: 8.15, y: yy + 0.07, w: 4.4, h: 0.3, isTextBox: true, fontFace: F.body,
      fontSize: 12, bold: true, color: C.ink, margin: 0 });
    s.addText(ev, { x: 8.15, y: yy + 0.37, w: 4.4, h: 0.3, isTextBox: true, fontFace: F.body,
      fontSize: 10, color: C.muted, margin: 0 });
  });
  L.card(s, 6.9, y + 3.68, 5.82, 1.0, "FDF3E3");
  s.addText("PA-1 (Day 1, 30 min): clean a messy CSV and fix a broken decompose script.\nPA-2 (Day 2, 30 min): a notebook reports 0.6% MAPE. Find and fix BOTH planted leaks, then report the honest post-fix accuracy.",
    { x: 7.14, y: y + 3.68, w: 5.34, h: 1.0, isTextBox: true, valign: "middle", fontFace: F.body,
      fontSize: 10.5, color: C.warn, margin: 0, lineSpacing: 14 });
  L.card(s, 0.62, y + 4.85, 12.1, 0.72, C.deep);
  s.addText("Forecasting badge requires ≥ 70 overall AND capstone ≥ 70 AND zero academic-integrity flags. Identical backtest tables or decision records across repositories are checked — the backtest must reproduce from each repository's own config.",
    { x: 0.9, y: y + 4.85, w: 11.54, h: 0.72, isTextBox: true, valign: "middle", fontFace: F.body,
      fontSize: 11.5, color: C.onDark, margin: 0 });
  s.addNotes("Collect repository URLs at the END of Day 3 Hour 4, not Hour 5 — that gives you the gap to spot-check backtest results before the demos begin.");

  // ================================================== WRAP-UP ============
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Every capstone requirement traces to a module", "WRAP-UP · DAY 3, FINAL 15 MINUTES");
  s.addImage({ path: IMG("D6_pipeline.png"), x: 1.35, y: y - 0.12, w: 10.6, h: 2.41 });
  const map = [["Decomposition", "M1"], ["Stationarity", "M2"], ["Classical models", "M3"],
               ["Leakage-safe features", "M4"], ["Calibrated intervals", "M5"],
               ["Rolling-origin backtest", "M6"], ["Selection & decision record", "M7"]];
  map.forEach(([t, m], i) => {
    const x = 0.62 + i * 1.75;
    L.card(s, x, y + 2.42, 1.6, 0.82, C.paperAlt);
    s.addText(m, { x, y: y + 2.5, w: 1.6, h: 0.3, isTextBox: true, align: "center", fontFace: F.body,
      fontSize: 11, bold: true, color: C.teal, margin: 0 });
    s.addText(t, { x: x + 0.12, y: y + 2.78, w: 1.36, h: 0.42, isTextBox: true, align: "center",
      fontFace: F.body, fontSize: 9.5, color: C.ink, margin: 0, lineSpacing: 12 });
  });
  L.pull(s, "Respect the arrow of time, so every reported accuracy number would survive contact with the future. The leakage-safe features, the time-aware backtest and the calibrated intervals are three faces of that one discipline.",
    0.62, y + 3.42, 12.1, 0.98);
  s.addText("Where this goes next", { x: 0.62, y: y + 4.58, w: 6.0, h: 0.32, isTextBox: true,
    fontFace: F.body, fontSize: 13, bold: true, color: C.ink, margin: 0 });
  L.bullets(s, [
    "SDA-DSC-311 builds directly on this pipeline",
    "SDA-DSC-213 Experimentation & Causal Inference is the sibling skill — what actually WORKS, which forecasting alone cannot answer",
    "The Forecasting badge is issued within 5 working days of collecting the repositories",
  ], 0.62, y + 4.82, 6.0, 1.15, { size: 10.5, space: 3 });
  s.addText("Collect before anyone leaves", { x: 6.9, y: y + 4.58, w: 5.8, h: 0.32, isTextBox: true,
    fontFace: F.body, fontSize: 13, bold: true, color: C.bad, margin: 0 });
  L.bullets(s, [
    "Repository URLs", "BACKTEST_REPORT.md", "DECISION_RECORD.md", "BENCHMARKS.md filled from their own runs",
  ], 6.9, y + 4.82, 5.8, 1.15, { size: 10.5, space: 3 });
  s.addNotes("Close on the thesis one last time, then the forward pointer. The five discussion prompts in the instructor guide are good material if you finish early — prompt 5 in particular: 'if the repository is the audit evidence for an accuracy claim, what does YOUR current backtest testify?'");

  // ================================================== CLOSING ============
  s = S(); L.bg(s, C.deep);
  s.addShape("ellipse", { x: 8.6, y: -2.0, w: 7.4, h: 7.4, fill: { color: C.mid },
    line: { width: 0 }, transparency: 60 });
  s.addText("SDA-DSC-212", { x: 0.9, y: 2.0, w: 8, h: 0.35, isTextBox: true, fontFace: F.body,
    fontSize: 12, bold: true, color: C.gold, charSpacing: 3 });
  s.addText("A forecast's accuracy claim\nmust survive contact\nwith the future.", { x: 0.9, y: 2.5,
    w: 9.5, h: 2.3, isTextBox: true, fontFace: F.head, fontSize: 38, bold: true, color: C.paper,
    lineSpacing: 50 });
  s.addText("The backtest is that survival, made auditable.", { x: 0.9, y: 4.9, w: 9.5, h: 0.5,
    isTextBox: true, fontFace: F.head, fontSize: 18, italic: true, color: C.sky });
  s.addText("SDAIA Academy  ·  Capacity Building Sector  ·  Data Scientist Track",
    { x: 0.9, y: 6.35, w: 9.5, h: 0.35, isTextBox: true, fontFace: F.body, fontSize: 12,
      color: C.onDarkMut });
  s.addNotes("Thank the room, then hand back the one thing they take away: not a model, a protocol.");

  return pres;
};
