const L = require("./lib"); const { C, F } = L;

module.exports = function part7(pres, R, IMG) {
  const S = () => pres.addSlide();
  let s, y;

  // =========================================================== M7 TITLE ====
  s = S(); L.bg(s, C.paper);
  s.addShape("roundRect", { x: 0.62, y: 0.9, w: 12.1, h: 5.7, rectRadius: 0.08,
    fill: { color: C.paperAlt }, line: { width: 0 } });
  s.addText("MODULE 7  ·  DAY 3, HOUR 4  ·  LO6 (INTEGRATES LO1–LO5)", { x: 1.1, y: 1.35, w: 8.5,
    h: 0.3, isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.teal,
    charSpacing: 2.5, margin: 0 });
  s.addText("Forecasting Case Study\nand Model Selection", { x: 1.1, y: 1.7, w: 7.6, h: 1.5,
    isTextBox: true, fontFace: F.head, fontSize: 34, bold: true, color: C.ink, margin: 0, lineSpacing: 42 });
  s.addText("The output of this module is not a model. It is a recommendation with evidence — and its own stated limits. Model selection is a function of the use case, not a leaderboard.",
    { x: 1.1, y: 3.3, w: 7.4, h: 1.0, isTextBox: true, fontFace: F.body, fontSize: 14,
      color: C.muted, margin: 0, lineSpacing: 20 });
  [["7.1", "Integrate decomposition, models, intervals and backtesting into one reproducible pipeline"],
   ["7.2", "Select a model family under multi-dimensional real-world constraints"],
   ["7.3", "Weigh accuracy against explainability, latency, compute and maintenance cost"],
   ["7.4", "Defend a recommendation from backtest and significance evidence"],
   ["7.5", "Communicate a forecast and its uncertainty to non-technical decision-makers"]].forEach(([k, t], i) => {
    s.addText(k, { x: 1.1, y: 4.45 + i * 0.42, w: 0.55, h: 0.36, isTextBox: true, fontFace: F.body,
      fontSize: 11.5, bold: true, color: C.mid, margin: 0, valign: "middle" });
    s.addText(t, { x: 1.68, y: 4.45 + i * 0.42, w: 7.2, h: 0.36, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, color: C.ink, margin: 0, valign: "middle" });
  });
  s.addImage({ path: IMG("D5_tradeoff_radar.png"), x: 9.0, y: 1.5, w: 3.4, h: 3.2 });
  s.addNotes("The walkthrough: a unit ran a bake-off, LightGBM won on MASE, promoted full stop. Two months later a control-room engineer refused to act on a forecast he could not interrogate during an unusual load event, and the team fell back to spreadsheets. The failure was not the model — it was a selection that weighted accuracy 100% and explainability 0%.");

  // ============================================ M7: TRADE-OFF SPACE ======
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "No row dominates", "M7 · THE MODEL-FAMILY TRADE-OFF SPACE");
  L.table(s, [
    L.hrow(["Family", "Accuracy", "Explainability", "Interval quality", "Compute / latency", "Maintenance", "Best when"]),
    L.crow(["Seasonal-naive", "low", "total", "none (add conformal)", "trivial", "none",
            "a baseline, or a stable calendar-driven series"], { fill: "FDF3E3" }),
    L.crow(["ETS", "medium", "high", "analytic, decent", "very fast", "low (automated)",
            "many series, no covariates, interpretability needed"]),
    L.crow(["SARIMAX", "medium-high", "high — a component story", "analytic, native", "moderate (slow at large m)", "medium",
            "covariates plus explainability required"], { fill: "F7FAFC" }),
    L.crow(["LightGBM + CQR", "high", "medium — importance only", "calibrated and sharp", "fast to train, needs a feature store", "higher (a pipeline)",
            "rich covariates, scale, nonlinear interactions"], { fill: "EAF2EC", boldCols: [0] }),
  ], 0.62, y, 12.1, { size: 10, rowH: 0.46, colW: [1.75, 1.35, 2.0, 1.75, 1.9, 1.5, 1.85] });
  s.addText("Six constraints that override accuracy", { x: 0.62, y: y + 2.62, w: 6.0, h: 0.35,
    isTextBox: true, fontFace: F.body, fontSize: 14, bold: true, color: C.ink, margin: 0 });
  const cons = [
    ["Deadline / latency", "An afternoon publication window caps fit + forecast time — this alone rules out refitting a large-m SARIMA per origin at serve time."],
    ["Explainability", "Regulatory or control-room acceptance can require a component story, promoting SARIMAX or ETS at a real accuracy cost."],
    ["Cost asymmetry", "If under-forecasting is far costlier, selection should optimise a quantile or asymmetric loss — not symmetric MAE."],
    ["Maintenance", "A feature pipeline is a standing liability. A thin accuracy gain loses on total cost of ownership."],
    ["Serve-time data", "A covariate model needs FUTURE covariates. No temperature forecast, no SARIMAX-with-temperature."],
    ["Adoption", "The winning model is the one people will actually use during an unusual event at 02:00."],
  ];
  cons.forEach(([k, v], i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const x = 0.62 + col * 6.3, yy = y + 3.0 + row * 0.92;
    L.card(s, x, yy, 5.95, 0.84, i === 5 ? "E7EFF7" : C.paperAlt);
    s.addText(k, { x: x + 0.22, y: yy + 0.07, w: 5.5, h: 0.26, isTextBox: true, fontFace: F.body,
      fontSize: 12, bold: true, color: i === 5 ? C.deep : C.mid, margin: 0 });
    s.addText(v, { x: x + 0.22, y: yy + 0.32, w: 5.5, h: 0.52, isTextBox: true, fontFace: F.body,
      fontSize: 10, color: C.ink, margin: 0, lineSpacing: 13 });
  });
  s.addNotes("Ask the room which constraint they have personally seen override a model choice. Nearly everyone names either the deadline or the explainability one, and that shared experience is what makes the decision record feel necessary rather than bureaucratic.");

  // ==================================== M7: SCENARIOS + DECISION RECORD ==
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Same series, same backtest, three different champions", "M7 · CONSTRAINT-DRIVEN SELECTION");
  const sc = [
    ["A", "Regulator", "0.3 / 0.4 / 0.2 / 0.1", "SARIMAX + temperature", "explainability + deadline", C.mid,
     "The published number must be defensible component by component. LightGBM is disqualified on serve-time feature-store dependency."],
    ["B", "Internal dispatch", "0.6 / 0.1 / 0.2 / 0.1", "LightGBM + CQR", "accuracy, DM-significant", C.good,
     "MASE 0.45, significantly better than the runner-up. Nobody outside the team reads the number."],
    ["C", "Four operating areas", "0.3 / 0.1 / 0.2 / 0.4", "Global LightGBM or ETS", "maintenance", C.teal,
     "Four hand-tuned models is four standing liabilities. A 0.2% accuracy loss buys three fewer models to maintain."],
  ];
  sc.forEach(([k, name, w, champ, dec, col, why], i) => {
    const x = 0.62 + i * 4.13;
    L.card(s, x, y, 3.85, 3.4, C.paperAlt);
    s.addShape("roundRect", { x, y, w: 3.85, h: 0.75, rectRadius: 0.06, fill: { color: col }, line: { width: 0 } });
    s.addText("SCENARIO " + k, { x: x + 0.25, y: y + 0.07, w: 3.3, h: 0.26, isTextBox: true,
      fontFace: F.body, fontSize: 9.5, bold: true, color: "FFE8B0", charSpacing: 2, margin: 0 });
    s.addText(name, { x: x + 0.25, y: y + 0.32, w: 3.3, h: 0.36, isTextBox: true, fontFace: F.head,
      fontSize: 17, bold: true, color: C.paper, margin: 0 });
    s.addText("weights  acc / explain / latency / maint", { x: x + 0.25, y: y + 0.88, w: 3.35, h: 0.24,
      isTextBox: true, fontFace: F.body, fontSize: 9, color: C.muted, margin: 0 });
    s.addText(w, { x: x + 0.25, y: y + 1.1, w: 3.35, h: 0.3, isTextBox: true, fontFace: F.mono,
      fontSize: 12, bold: true, color: col, margin: 0 });
    s.addText("CHAMPION", { x: x + 0.25, y: y + 1.5, w: 3.35, h: 0.24, isTextBox: true, fontFace: F.body,
      fontSize: 9, bold: true, color: C.muted, charSpacing: 1.5, margin: 0 });
    s.addText(champ, { x: x + 0.25, y: y + 1.72, w: 3.35, h: 0.36, isTextBox: true, fontFace: F.head,
      fontSize: 14.5, bold: true, color: C.ink, margin: 0 });
    s.addText("Decisive constraint:  " + dec, { x: x + 0.25, y: y + 2.12, w: 3.35, h: 0.34, isTextBox: true,
      fontFace: F.body, fontSize: 10.5, bold: true, color: col, margin: 0, lineSpacing: 14 });
    s.addText(why, { x: x + 0.25, y: y + 2.5, w: 3.35, h: 0.85, isTextBox: true, fontFace: F.body,
      fontSize: 10.5, color: C.ink, margin: 0, lineSpacing: 14 });
  });
  s.addText("A decision record is six things, and none of them is a leaderboard position", { x: 0.62,
    y: y + 3.54, w: 12.1, h: 0.35, isTextBox: true, fontFace: F.body, fontSize: 14, bold: true,
    color: C.ink, margin: 0 });
  ["the decision and its cost function", "the candidates and the constraints applied",
   "the stated weights", "the recommendation with its DM evidence",
   "the FLIP-CONDITIONS — what would have to change", "the monitoring contract and the fallback"]
    .forEach((t, i) => {
      const x = 0.62 + (i % 3) * 4.13, yy = y + 3.86 + Math.floor(i / 3) * 0.54;
      L.circle(s, x, yy, 0.36, i >= 4 ? C.gold : C.deep, String(i + 1), i >= 4 ? C.ink : C.paper);
      s.addText(t, { x: x + 0.5, y: yy - 0.02, w: 3.5, h: 0.4, isTextBox: true, fontFace: F.body,
        fontSize: 11.5, color: C.ink, margin: 0, valign: "middle" });
    });
  L.card(s, 0.62, y + 4.98, 12.1, 0.74, "FDF3E3");
  s.addText("A recommendation includes its own limits. State where the model loses and what you monitor — that candour is what earns adoption. A report that names the Eid weeks and ships a fallback should score above a silent, marginally sharper submission.",
    { x: 0.9, y: y + 4.98, w: 11.54, h: 0.74, isTextBox: true, valign: "middle", fontFace: F.body,
      fontSize: 12, italic: true, color: C.warn, margin: 0 });
  s.addNotes("Lab 7 is exactly this slide, done by the participants with their own backtest numbers. If a cohort is running behind, reduce it to two scenarios and demo the third — but never drop the decision record.");

  // ================================ M7: COMMUNICATING + THE RESERVE BRIEF =
  s = S(); L.bg(s, C.deep);
  s.addText("M7 · COMMUNICATING THE FORECAST", { x: 0.62, y: 0.45, w: 8, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 11.5, bold: true, color: C.gold, charSpacing: 2.5, margin: 0 });
  s.addText("Lead with the decision, not the model", { x: 0.62, y: 0.8, w: 11.5, h: 0.6,
    isTextBox: true, fontFace: F.head, fontSize: 29, bold: true, color: C.paper, margin: 0 });
  L.card(s, 0.62, 1.65, 5.85, 2.05, "3A1F26");
  s.addText("WHAT NOT TO SEND", { x: 0.88, y: 1.8, w: 5.3, h: 0.28, isTextBox: true, fontFace: F.body,
    fontSize: 10, bold: true, color: "F2A8A8", charSpacing: 1.5, margin: 0 });
  s.addText("“The p95 is 52,400 MW. MASE is 0.45 and marginal coverage is 0.90 on the held-out window.”",
    { x: 0.88, y: 2.12, w: 5.3, h: 0.8, isTextBox: true, fontFace: F.mono, fontSize: 12,
      color: "F2C9C9", margin: 0, lineSpacing: 18 });
  s.addText("Every number is correct. Not one of them is a decision.", { x: 0.88, y: 3.05, w: 5.3,
    h: 0.5, isTextBox: true, fontFace: F.body, fontSize: 11.5, italic: true, color: "F2A8A8",
    margin: 0, lineSpacing: 15 });
  L.card(s, 6.85, 1.65, 5.85, 2.05, "17352A");
  s.addText("WHAT TO SEND", { x: 7.11, y: 1.8, w: 5.3, h: 0.28, isTextBox: true, fontFace: F.body,
    fontSize: 10, bold: true, color: "9DD9A8", charSpacing: 1.5, margin: 0 });
  s.addText("“Set spinning reserve to 52,400 MW. Expected peak is 49,900 MW at 15:00; the 2,500 MW gap is the honest uncertainty and it is widest on hot days. This covers all but about 5% of afternoons.”",
    { x: 7.11, y: 2.12, w: 5.3, h: 1.35, isTextBox: true, fontFace: F.body, fontSize: 12.5,
      color: "D6EFDC", margin: 0, lineSpacing: 18 });
  L.code(s, [
    "RESERVE BRIEF — Tayyar day-ahead load forecast",
    "Issued 2023-11-14 14:00 for the 24 hours beginning 2023-11-15 00:00",
    "",
    { t: "  Expected peak demand          41,850 MW at 15:00", c: "CFE3F5" },
    { t: "  90% upper bound (p95)         43,470 MW", c: "CFE3F5" },
    { t: "  Recommended spinning reserve   1,620 MW", c: "6BCB77" },
    "      = the p95 peak minus the expected peak: what we would need",
    "        if tomorrow lands at the top of the interval.",
    "",
    { t: "  Confidence: over the last 60 backtested days this interval", c: "CFE3F5" },
    { t: "  contained the actual demand 90% of the time (target 90%).", c: "CFE3F5" },
    "",
    { t: "  Where this forecast is weakest: Eid weeks, and summer", c: "F2C14E" },
    { t: "  afternoons where conditional coverage falls to 0.85.", c: "F2C14E" },
    { t: "  Fallback: the seasonal-naive forecast, which handles the", c: "F2C14E" },
    { t: "  holiday shift correctly. Monitored weekly on MASE + coverage.", c: "F2C14E" },
  ], 0.62, 3.8, 7.9, 0, { size: 8.4 });
  s.addText("Four rules", { x: 8.75, y: 3.9, w: 3.97, h: 0.3, isTextBox: true, fontFace: F.body,
    fontSize: 12.5, bold: true, color: C.gold, margin: 0 });
  L.bullets(s, [
    "Lead with the decision, not the model",
    "Show the interval as risk, not as hedging — its width IS the honest uncertainty, and narrowing it dishonestly costs load-shedding",
    "Name the known weaknesses and the fallback. Trust survives the first miss only if you predicted it",
    "Feature importance is a story, never a causal claim",
  ], 8.75, 4.22, 3.97, 2.5, { size: 11, color: C.onDark, space: 5 });
  s.addNotes("Run the communication drill (10 min): give them the jargon version on the left and have them rewrite it in two decision-language sentences. Read the best one aloud. Then ask a participant to play the control-room engineer and push back.");

  return pres;
};
