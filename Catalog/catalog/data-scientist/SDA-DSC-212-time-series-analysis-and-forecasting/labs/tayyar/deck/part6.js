const L = require("./lib"); const { C, F } = L;

module.exports = function part6(pres, R, IMG) {
  const S = () => pres.addSlide();
  let s, y;
  const M = Object.fromEntries(R.m6.summary.map(d => [d.model, d]));
  const LG = M["LightGBM (direct)"], SN = M["Seasonal-naive"], Q = M["LightGBM (quantile q50)"];

  // ================================================== DAY 3 SECTION =======
  s = S(); L.bg(s, C.deep);
  s.addShape("ellipse", { x: 9.6, y: -2.2, w: 6.6, h: 6.6, fill: { color: C.mid },
    line: { width: 0 }, transparency: 58 });
  L.titleSlideText(s, "DAY 3 · HOURS 1–5", "Trust and Selection",
    "Two days of building produce candidate models. Today produces the only thing anyone outside the room will read: evidence that one of them deserves to run tomorrow afternoon.");
  [["MODULE 5", "Intervals and calibration (finish)", "LO5"],
   ["MODULE 6", "Backtesting and Forecast Evaluation", "LO4 · LO5"],
   ["MODULE 7", "Forecasting Case Study and Selection", "LO6"],
   ["CAPSTONE", "Tayyar — a backtested day-ahead service", "40%"]].forEach(([m, t, lo], i) => {
    const yy = 5.05 + i * 0.42;
    s.addText(m, { x: 0.9, y: yy, w: 1.5, h: 0.36, isTextBox: true, fontFace: F.mono,
      fontSize: 12.5, bold: true, color: C.gold, margin: 0, valign: "middle" });
    s.addText(t, { x: 2.5, y: yy, w: 5.5, h: 0.36, isTextBox: true, fontFace: F.body,
      fontSize: 13, color: C.sky, margin: 0, valign: "middle" });
    s.addText(lo, { x: 8.1, y: yy, w: 1.5, h: 0.36, isTextBox: true, fontFace: F.mono,
      fontSize: 12, color: C.onDarkMut, margin: 0, valign: "middle" });
  });
  s.addNotes("Day 3 afternoon is deliberately light on new theory so the backtest and capstone get uninterrupted build time. Guard that. Cut discussion, never build time.");

  // =========================================================== M6 TITLE ====
  s = S(); L.bg(s, C.paper);
  s.addShape("roundRect", { x: 0.62, y: 0.9, w: 12.1, h: 5.7, rectRadius: 0.08,
    fill: { color: C.paperAlt }, line: { width: 0 } });
  s.addText("MODULE 6  ·  DAY 3, HOURS 2–3  ·  LO4 · LO5 · LO6", { x: 1.1, y: 1.35, w: 8, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.teal, charSpacing: 2.5, margin: 0 });
  s.addText("Backtesting and\nForecast Evaluation", { x: 1.1, y: 1.7, w: 7.6, h: 1.5, isTextBox: true,
    fontFace: F.head, fontSize: 34, bold: true, color: C.ink, margin: 0, lineSpacing: 42 });
  s.addText("This is where “respect the arrow of time” stops being a principle and becomes a measurement protocol. The backtest report is this course's headline artefact — the deliverable a grid operator, a demand planner or a workforce planner actually commissions.",
    { x: 1.1, y: 3.3, w: 7.4, h: 1.2, isTextBox: true, fontFace: F.body, fontSize: 14,
      color: C.muted, margin: 0, lineSpacing: 20 });
  [["6.1", "Design rolling-origin and expanding-window backtests without temporal leakage"],
   ["6.2", "Select scale-appropriate point metrics and explain each one's failure mode"],
   ["6.3", "Evaluate probabilistic forecasts with pinball loss and empirical coverage"],
   ["6.4", "Compare models statistically with the Diebold-Mariano test"],
   ["6.5", "Assemble a reproducible backtest report driving a model-selection decision"]].forEach(([k, t], i) => {
    s.addText(k, { x: 1.1, y: 4.62 + i * 0.4, w: 0.55, h: 0.34, isTextBox: true, fontFace: F.body,
      fontSize: 11.5, bold: true, color: C.mid, margin: 0, valign: "middle" });
    s.addText(t, { x: 1.68, y: 4.62 + i * 0.4, w: 7.0, h: 0.34, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, color: C.ink, margin: 0, valign: "middle" });
  });
  L.card(s, 8.95, 2.55, 3.45, 2.35, "0D2136");
  s.addText("Why one split is not evidence", { x: 9.2, y: 2.72, w: 3.0, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 11.5, bold: true, color: C.gold, margin: 0 });
  s.addText("A single split estimates skill from ONE realisation of the future. Test-week luck flips rankings.\n\nA backtest repeats the evaluation over many origins and yields a distribution of skill, not a point estimate.",
    { x: 9.2, y: 3.08, w: 3.0, h: 1.7, isTextBox: true, fontFace: F.body, fontSize: 11,
      color: "CFE3F5", margin: 0, lineSpacing: 15 });
  s.addNotes("The real-world walkthrough for this module: a team celebrated a 0.3-point MAPE win, then a 90-origin backtest showed MASE 0.98 and Diebold-Mariano p = 0.41. The 'win' was noise — and the per-origin breakdown showed the ML model lost on every Eid week.");

  // ============================================ M6: SCHEME + METRICS ======
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Two schemes, five metrics, one protocol", "M6 · HOW TO MEASURE A FORECAST");
  s.addImage({ path: IMG("D3_rolling_origin.png"), x: 0.62, y: y - 0.1, w: 6.3, h: 2.55 });
  L.card(s, 7.2, y - 0.1, 5.52, 2.55, C.paperAlt);
  s.addText("The two rules that make it a backtest rather than theatre", { x: 7.45, y: y + 0.05,
    w: 5.0, h: 0.55, isTextBox: true, fontFace: F.body, fontSize: 12.5, bold: true, color: C.ink,
    margin: 0, lineSpacing: 17 });
  L.bullets(s, [
    { text: "REFIT at every origin. A fit-once loop scores points the model already trained on — the tell is MASE ≈ 0", bold: false },
    "Every feature at origin t uses only data ≤ t. Leave a GAP if any feature straddles the boundary",
    "Expanding when the process is stable and more data always helps; sliding when it drifts (a new industrial load, a tariff change)",
    "sktime's ExpandingWindowSplitter with strategy=\"refit\" does this correctly — hand-rolled loops are where leaks creep back in",
  ], 7.45, y + 0.66, 5.0, 1.8, { size: 10, space: 4 });
  L.table(s, [
    L.hrow(["Metric", "What it is", "Strength", "Fails when"]),
    L.crow(["MAE", "mean |y − ŷ|", "same units, robust", "not comparable across series of different scale"]),
    L.crow(["RMSE", "√ mean (y − ŷ)²", "penalises large misses", "dominated by outliers; scale-bound"], { fill: "F7FAFC" }),
    L.crow(["MAPE", "mean |y − ŷ| / |y|", "scale-free, intuitive", "explodes near zero; asymmetric — over-forecasts capped at 100%"], { fill: "FDF3E3" }),
    L.crow(["sMAPE", "symmetric percentage", "bounded", "still unstable near zero; awkward to interpret"], { fill: "F7FAFC" }),
    L.crow(["MASE", "MAE / MAE of seasonal-naive", "scale-free, symmetric, defined at zero", "needs a sensible baseline period m"], { fill: "EAF2EC", boldCols: [0] }),
    L.crow(["Pinball", "the quantile loss, averaged", "a PROPER score — rewards honest calibration", "only meaningful for a probabilistic forecast"], { fill: "F7FAFC" }),
  ], 0.62, y + 2.52, 12.1, { size: 9.5, rowH: 0.32, colW: [1.25, 2.5, 3.15, 5.2] });
  L.pull(s, "MASE < 1 beats the free seasonal-naive baseline · MASE = 1 ties it · MASE > 1 means you should have shipped the baseline. Always report MASE alongside a percentage metric — the percentage is what a planner feels, the MASE is what makes it comparable.",
    0.62, y + 4.9, 12.1, 0.78);
  s.addNotes("Run 'baseline first' (10 min): every pair hand-computes the seasonal-naive error for one day before touching a model. That single number is what everything else must beat, and computing it by hand makes MASE intuitive rather than formulaic.");

  // ========================================== M6: THE BACKTEST RESULT =====
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Sixty origins, refit at each — this is what evidence looks like",
    "M6 · THE TAYYAR BACKTEST", { size: 27 });
  s.addImage({ path: IMG("07_backtest.png"), x: 0.62, y: y - 0.05, w: 7.6, h: 2.77 });
  L.table(s, [
    L.hrow(["Model", "MASE", "MAE (MW)", "MAPE", "vs baseline"]),
    L.crow(["LightGBM, direct H = 24", LG.MASE.toFixed(3), LG.MAE.toFixed(0), LG["MAPE_%"].toFixed(2) + "%",
            "−" + (100 * (1 - LG.MAE / SN.MAE)).toFixed(0) + "% error"], { fill: "EAF2EC", boldCols: [0, 1] }),
    L.crow(["LightGBM quantile, q50", Q.MASE.toFixed(3), Q.MAE.toFixed(0), Q["MAPE_%"].toFixed(2) + "%",
            "−" + (100 * (1 - Q.MAE / SN.MAE)).toFixed(0) + "% error"], { fill: "F7FAFC" }),
    L.crow(["Seasonal-naive (free)", SN.MASE.toFixed(3), SN.MAE.toFixed(0), SN["MAPE_%"].toFixed(2) + "%",
            "the baseline"], { fill: "FDF3E3" }),
  ], 8.45, y - 0.05, 4.27, { size: 10.5, rowH: 0.42, colW: [1.42, 0.62, 0.8, 0.63, 0.8] });
  L.card(s, 8.45, y + 1.95, 4.27, 0.85, "E7EFF7");
  s.addText("Read the denominator. Seasonal-naive scores MASE 0.77, not 1.00, because the MASE scale is its in-sample error over a full year — including volatile summer — while these origins are autumn. Know what you divide by.",
    { x: 8.65, y: y + 1.95, w: 3.87, h: 0.85, isTextBox: true, valign: "middle", fontFace: F.body,
      fontSize: 9.5, color: C.deep, margin: 0, lineSpacing: 13 });
  s.addText("Is the difference real, or did it get lucky?", { x: 0.62, y: y + 2.95, w: 6.0, h: 0.35,
    isTextBox: true, fontFace: F.body, fontSize: 14, bold: true, color: C.ink, margin: 0 });
  const cB35 = L.code(s, [
    "d = |e_A| − |e_B|                     # the loss differential series",
    "lrv = Newey-West long-run variance of d (h−1 autocovariance lags)",
    "DM  = mean(d) / sqrt(lrv / n), then the Harvey-Leybourne-Newbold",
    "      small-sample correction",
    "",
    { t: "LightGBM vs seasonal-naive : DM = " + R.m6.dm_lgbm_vs_naive.dm_stat + "  p = 0.000  -> SIGNIFICANT", c: "6BCB77" },
    { t: "LightGBM vs quantile q50   : DM = " + R.m6.dm_lgbm_vs_q50.dm_stat + "  p = " + R.m6.dm_lgbm_vs_q50.p_value.toFixed(3) + "  -> NOT significant", c: "F2C14E" },
  ], 0.62, y + 3.3, 7.6, 0, { size: 9.5 });
  L.card(s, 8.45, y + 2.95, 4.27, 2.0, C.deep);
  s.addText("The decision rule", { x: 8.7, y: y + 3.1, w: 3.8, h: 0.3, isTextBox: true, fontFace: F.body,
    fontSize: 12, bold: true, color: C.gold, margin: 0 });
  s.addText("A non-significant Diebold-Mariano result tells you to ship the SIMPLER or CHEAPER model — you cannot distinguish them.\n\nHere the two LightGBM variants are statistically indistinguishable (p = " + R.m6.dm_lgbm_vs_q50.p_value.toFixed(3) + "), so the quantile model wins on grounds that have nothing to do with accuracy: it also produces the interval.",
    { x: 8.7, y: y + 3.45, w: 3.8, h: 1.45, isTextBox: true, fontFace: F.body, fontSize: 10.5,
      color: "CFE3F5", margin: 0, lineSpacing: 14.5 });
  s.addText("Statistical significance gates model promotion. A 0.1% MAE “win” that fails DM does not justify shipping the added complexity — and the per-origin breakdown is what tells you WHICH weeks the champion loses.",
    { x: 0.62, y: cB35 + 0.14, w: 7.6, h: 0.6, isTextBox: true, fontFace: F.body, fontSize: 11.5,
      italic: true, color: C.muted, margin: 0, lineSpacing: 15 });
  s.addNotes("Run 'significance debate' (15 min): show two models' per-origin errors, have the class predict the DM verdict by eye, then run it. They are wrong often enough to make the point permanently.");

  // ================================================= M6: LAB 6 ===========
  s = S(); L.bg(s, C.deep);
  s.addText("HANDS-ON LAB 6  ·  50 MINUTES  ·  THE COURSE'S HEADLINE DELIVERABLE", { x: 0.62,
    y: 0.5, w: 10, h: 0.3, isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true,
    color: C.gold, charSpacing: 2, margin: 0 });
  s.addText("The rolling-origin backtest report", { x: 0.62, y: 0.85, w: 9.5, h: 0.6, isTextBox: true,
    fontFace: F.head, fontSize: 29, bold: true, color: C.paper, margin: 0 });
  s.addText("git checkout lab6-start", { x: 10.3, y: 0.9, w: 2.4, h: 0.45, isTextBox: true,
    fontFace: F.mono, fontSize: 11, color: "6BCB77", align: "right", margin: 0, valign: "middle" });
  [["5", "The starter “backtests” by fitting once on all data and then scoring past points. Find the leak. Note it in BACKTEST.md."],
   ["12", "Configure the splitter: initial window 1 year, step 1 week, horizon 24 h. Run all four families. Confirm ≥ 50 origins."],
   ["10", "Aggregate per-origin errors: mean AND spread of MAE, MAPE, MASE. Every model reported relative to seasonal-naive."],
   ["8", "Add probabilistic scoring for the two interval models — mean pinball and empirical coverage across origins."],
   ["10", "Run Diebold-Mariano on the top two point models. Record the significance. Decide the champion and state the rule you applied."],
   ["5", "Write BACKTEST.md: table, DM verdict, champion, and the conditions under which the champion loses. Commit."]].forEach(([m, t], i) => {
    const yy = 1.7 + i * 0.68;
    L.circle(s, 0.62, yy + 0.05, 0.46, i === 0 ? C.bad : (i > 3 ? C.good : C.mid), m);
    s.addText(t, { x: 1.28, y: yy, w: 6.1, h: 0.6, isTextBox: true, fontFace: F.body,
      fontSize: 12, color: C.onDark, margin: 0, valign: "middle", lineSpacing: 15.5 });
  });
  L.code(s, [
    "$ python -m tayyar.eval.run_backtest",
    "Backtest: expanding window, 60 origins, fh=24h, refit each origin",
    "",
    "Model                MASE   MAE(MW)  MAPE   coverage  pinball",
    { t: "seasonal-naive       0.77    1244    4.12%     -        -", c: "CFE3F5" },
    { t: "ETS(A,Ad,A)          0.62     998    3.24%    0.87     221", c: "CFE3F5" },
    { t: "SARIMAX + temp       0.55     889    2.86%    0.90     198", c: "CFE3F5" },
    { t: "LightGBM + CQR       0.45     719    2.33%    0.90     181  <- champion", c: "6BCB77" },
    "",
    { t: "DM (LightGBM vs SARIMAX): dm=-6.75  p=0.000 -> significant", c: "F2C14E" },
    "Champion: LightGBM + CQR. Loses on Eid origins -> naive fallback.",
    "Wrote backtest_table.csv, error_by_origin.png, BACKTEST.md",
  ], 7.6, 1.7, 5.12, 0, { size: 8.8 });
  s.addText("Troubleshooting", { x: 7.6, y: 5.02, w: 5.12, h: 0.3, isTextBox: true, fontFace: F.body,
    fontSize: 12, bold: true, color: C.paper, margin: 0 });
  [["Every model MASE ≈ 0", "scored in-sample — use strategy=\"refit\""],
   ["MAPE = 4000% on one origin", "near-zero demand; prefer MASE"],
   ["Only three origins produced", "step too large or initial window too big"],
   ["Backtest runs for minutes", "expected — cache naive/ETS, parallelise folds"]].forEach(([a, b], i) => {
    s.addText(a, { x: 7.6, y: 5.34 + i * 0.4, w: 2.35, h: 0.36, isTextBox: true, fontFace: F.body,
      fontSize: 9.5, color: "F2A8A8", margin: 0, valign: "middle", lineSpacing: 12 });
    s.addText(b, { x: 10.02, y: 5.34 + i * 0.4, w: 2.7, h: 0.36, isTextBox: true, fontFace: F.body,
      fontSize: 9.5, color: "9DD9A8", margin: 0, valign: "middle", lineSpacing: 12 });
  });
  s.addText("The backtest is the product. Fixed splits, fixed seeds, pinned dependencies — that is what makes the report evidence rather than anecdote.",
    { x: 0.62, y: 5.85, w: 6.6, h: 0.7, isTextBox: true, fontFace: F.head, fontSize: 13.5,
      italic: true, color: C.sky, margin: 0, lineSpacing: 18 });
  s.addNotes("Run the shared leaderboard for this lab — MASE, coverage and pinball on a projector. The competitive element gets pairs to the finish line, and the leaderboard becomes the Module 7 discussion material.");

  return pres;
};
