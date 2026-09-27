const L = require("./lib"); const { C, F } = L;

module.exports = function part5(pres, R, IMG) {
  const S = () => pres.addSlide();
  let s, y;
  const cond = Object.fromEntries(R.m5.conditional.map(d => [d.group, d]));
  const condB = Object.fromEntries(R.m5.conditional_before.map(d => [d.group, d]));

  // =========================================================== M5 TITLE ====
  s = S(); L.bg(s, C.paper);
  s.addShape("roundRect", { x: 0.62, y: 0.9, w: 12.1, h: 5.7, rectRadius: 0.08,
    fill: { color: C.paperAlt }, line: { width: 0 } });
  s.addText("MODULE 5  ·  DAY 2 HOUR 5 → DAY 3 HOUR 1  ·  LO5", { x: 1.1, y: 1.35, w: 8, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.teal, charSpacing: 2.5, margin: 0 });
  s.addText("Probabilistic Forecasts\nand Intervals", { x: 1.1, y: 1.7, w: 7.6, h: 1.5, isTextBox: true,
    fontFace: F.head, fontSize: 34, bold: true, color: C.ink, margin: 0, lineSpacing: 42 });
  s.addText("A point forecast is a lie by omission. Two forecasts can share a mean of 50,000 MW while one is near-certain and the other spans ±8,000 MW — completely different reserve decisions. Forecast the distribution, and let the decision pick the quantile it needs.",
    { x: 1.1, y: 3.3, w: 7.4, h: 1.2, isTextBox: true, fontFace: F.body, fontSize: 14,
      color: C.muted, margin: 0, lineSpacing: 20 });
  [["5.1", "Frame decisions as quantile problems, not mean problems"],
   ["5.2", "Produce prediction intervals from classical and ML models"],
   ["5.3", "Train quantile models with the pinball loss"],
   ["5.4", "Apply split-conformal prediction for distribution-free coverage"],
   ["5.5", "Evaluate on coverage, sharpness and pinball — and diagnose miscalibration"]].forEach(([k, t], i) => {
    s.addText(k, { x: 1.1, y: 4.62 + i * 0.4, w: 0.55, h: 0.34, isTextBox: true, fontFace: F.body,
      fontSize: 11.5, bold: true, color: C.mid, margin: 0, valign: "middle" });
    s.addText(t, { x: 1.68, y: 4.62 + i * 0.4, w: 7.0, h: 0.34, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, color: C.ink, margin: 0, valign: "middle" });
  });
  L.card(s, 8.95, 2.55, 3.45, 2.4, "0D2136");
  s.addText("The module ethic", { x: 9.2, y: 2.72, w: 3.0, h: 0.3, isTextBox: true, fontFace: F.body,
    fontSize: 11.5, bold: true, color: C.gold, margin: 0 });
  s.addText("Report uncertainty —\nand then prove it is honest.", { x: 9.2, y: 3.05, w: 3.0, h: 0.7,
    isTextBox: true, fontFace: F.head, fontSize: 15, italic: true, color: C.paper, margin: 0, lineSpacing: 21 });
  s.addText("The reserve margin is sized off the UPPER bound of the day-ahead forecast, not the mean. The interval is not a caveat attached to the product. The interval IS the product.",
    { x: 9.2, y: 3.85, w: 3.0, h: 1.0, isTextBox: true, fontFace: F.body, fontSize: 11,
      color: "CFE3F5", margin: 0, lineSpacing: 15 });
  s.addNotes("Open with the two-forecasts-same-mean example on the whiteboard before any slide content. Ask which one the control room should act on. The answer — 'you cannot tell from the mean' — is the module in one line.");

  // ============================================= M5: PINBALL + CI vs PI ===
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "The loss that produces a quantile", "M5 · PINBALL LOSS AND THE TWO KINDS OF INTERVAL");
  s.addImage({ path: IMG("D4_pinball.png"), x: 0.62, y: y - 0.05, w: 5.9, h: 3.49 });
  L.card(s, 6.8, y - 0.05, 5.92, 1.65, "FBEEEC");
  s.addText("Confidence interval", { x: 7.05, y: y + 0.08, w: 5.4, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 12.5, bold: true, color: C.bad, margin: 0 });
  s.addText("Uncertainty about a PARAMETER — where the mean level sits. Narrower. Almost never what a forecast decision needs, and shipping one where a prediction interval belongs is the most common interval bug in production.",
    { x: 7.05, y: y + 0.42, w: 5.4, h: 1.1, isTextBox: true, fontFace: F.body, fontSize: 12,
      color: C.ink, margin: 0, lineSpacing: 16 });
  L.card(s, 6.8, y + 1.78, 5.92, 1.66, "EAF2EC");
  s.addText("Prediction interval", { x: 7.05, y: y + 1.91, w: 5.4, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 12.5, bold: true, color: C.good, margin: 0 });
  s.addText("Uncertainty about a future OBSERVATION — parameter uncertainty plus irreducible noise. Always wider. This is what forecasting wants, every time.",
    { x: 7.05, y: y + 2.25, w: 5.4, h: 0.8, isTextBox: true, fontFace: F.body, fontSize: 12,
      color: C.ink, margin: 0, lineSpacing: 16 });
  s.addText("Classical models give these analytically — but on the assumption of constant variance. Tayyar's summer heteroskedasticity breaks exactly that assumption.",
    { x: 7.05, y: y + 3.0, w: 5.4, h: 0.4, isTextBox: true, fontFace: F.body, fontSize: 10.5,
      italic: true, color: C.muted, margin: 0, lineSpacing: 14 });
  const cB28 = L.code(s, [
    "def pinball_loss(y_true, q_pred, tau):",
    "    d = np.asarray(y_true) - np.asarray(q_pred)",
    { t: "    return np.mean(np.maximum(tau * d, (tau - 1) * d))", c: "6BCB77" },
    "",
    "# LightGBM fits it directly, one model per quantile:",
    "lgb.LGBMRegressor(objective=\"quantile\", alpha=0.95)",
    "",
    { t: "out[qcols] = np.sort(out[qcols].to_numpy(), axis=1)  # de-cross q95 < q50", c: "F2C14E" },
  ], 0.62, y + 3.42, 12.1, 0, { size: 9.5 });
  s.addText("Independently-fitted quantile models can cross — a predicted q95 below the q50 is an incoherent distribution. Repair by sorting per row, or fit with a monotone constraint. Never by ignoring it.",
    { x: 0.62, y: cB28 + 0.08, w: 12.1, h: 0.45, isTextBox: true, fontFace: F.body, fontSize: 10,
      italic: true, color: C.muted, margin: 0, lineSpacing: 15 });
  s.addNotes("Run the elicitation drill (10 min): three decisions — reserve margin, SKU stocking, staff roster — each with a stated cost asymmetry. Teams name the quantile each decision should consume and defend it. Nobody picks the mean twice.");

  // ==================================================== M5: CONFORMAL =====
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Coverage you can actually promise", "M5 · SPLIT-CONFORMAL PREDICTION AND CQR");
  const steps = [
    ["1", "Split", "Hold out a calibration window the model never trained on — respecting time.", C.mid],
    ["2", "Score", "On calibration, compute the nonconformity score. For CQR that is max(lo − y, y − hi): how far the truth fell OUTSIDE the band.", C.teal],
    ["3", "Quantile", "Take q̂ = the ⌈(n+1)(1−α)⌉-th smallest score. The finite-sample correction is the +1.", C.gold],
    ["4", "Widen", "Ship [lo − q̂, hi + q̂]. Marginal coverage ≥ 1 − α is then guaranteed under exchangeability.", C.good],
  ];
  steps.forEach(([n, t, d, col], i) => {
    const x = 0.62 + i * 3.09;
    L.card(s, x, y, 2.85, 2.15, C.paperAlt);
    L.circle(s, x + 0.25, y + 0.22, 0.5, col, n);
    s.addText(t, { x: x + 0.85, y: y + 0.28, w: 1.85, h: 0.38, isTextBox: true, fontFace: F.head,
      fontSize: 16, bold: true, color: col, margin: 0, valign: "middle" });
    s.addText(d, { x: x + 0.25, y: y + 0.85, w: 2.35, h: 1.2, isTextBox: true, fontFace: F.body,
      fontSize: 11, color: C.ink, margin: 0, lineSpacing: 15 });
    if (i < 3) s.addText("→", { x: x + 2.87, y: y + 0.85, w: 0.2, h: 0.4, isTextBox: true,
      fontFace: F.body, fontSize: 16, bold: true, color: C.muted, margin: 0, align: "center" });
  });
  const cB29 = L.code(s, [
    "def conformal_quantile(scores, alpha=0.10):",
    "    n = len(scores)",
    { t: "    k = int(np.ceil((n + 1) * (1 - alpha)))   # the finite-sample +1", c: "F2C14E" },
    "    return float(np.sort(scores)[min(max(k, 1), n) - 1])",
    "",
    "class CQR:",
    "    def calibrate(self, y_cal, lo_cal, hi_cal):",
    { t: "        self.qhat_ = conformal_quantile(", c: "6BCB77" },
    { t: "            np.maximum(lo_cal - y_cal, y_cal - hi_cal))", c: "6BCB77" },
    "    def interval(self, lo, hi):",
    "        return lo - self.qhat_, hi + self.qhat_",
  ], 0.62, y + 2.35, 6.1, 0, { size: 9.5 });
  L.card(s, 6.9, y + 2.35, 5.82, 2.4, "FDF3E3");
  s.addText("What conformal does NOT give you", { x: 7.15, y: y + 2.5, w: 5.3, h: 0.32, isTextBox: true,
    fontFace: F.body, fontSize: 12.5, bold: true, color: C.warn, margin: 0 });
  L.bullets(s, [
    "CONDITIONAL coverage. The guarantee is marginal — 90% on average across all hours",
    "Protection when exchangeability fails. Calibrating on July and testing in December over-covers, because the residuals are not exchangeable across regimes",
    "A pass on monitoring. Coverage drifts; recalibrate on a rolling recent window and persist q̂ with the model",
  ], 7.15, y + 2.82, 5.3, 1.85, { size: 11, space: 5 });
  s.addText("For strongly autocorrelated series use adaptive conformal (ACI) or EnbPI, which update q̂ online as coverage errors accumulate.",
    { x: 0.62, y: cB29 + 0.14, w: 12.1, h: 0.45, isTextBox: true, fontFace: F.body, fontSize: 11.5,
      italic: true, color: C.muted, margin: 0 });
  s.addNotes("Make the exchangeability point concretely: we deliberately calibrate on October and test on November-December. If you calibrate on peak summer and test in winter the interval over-covers to 0.99 and is useless. That is a real failure mode, not a footnote.");

  // ============================ M5: THE CONDITIONAL-COVERAGE RESULT =======
  s = S(); L.bg(s, C.deep);
  s.addText("M5 · THE RESULT THAT CHANGES A DECISION", { x: 0.62, y: 0.45, w: 8, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 11.5, bold: true, color: C.gold, charSpacing: 2.5, margin: 0 });
  s.addText("90% on average can hide 85% on the afternoons that matter", { x: 0.62, y: 0.8, w: 11.8,
    h: 0.6, isTextBox: true, fontFace: F.head, fontSize: 28, bold: true, color: C.paper, margin: 0 });
  s.addImage({ path: IMG("06_coverage.png"), x: 0.62, y: 1.55, w: 6.35, h: 3.26 });
  L.table(s, [
    L.hrow(["", "Coverage", "Mean width", "Verdict"], C.mid),
    [{ text: "Quantile model only", options: { fontSize: 11, bold: true, color: C.ink } },
     { text: R.m5.coverage_before_on_test.toFixed(3), options: { fontSize: 11, color: C.bad, bold: true } },
     { text: R.m5.mean_width_before.toFixed(0) + " MW", options: { fontSize: 11 } },
     { text: "under-covers by 11 points", options: { fontSize: 11, color: C.bad } }],
    [{ text: "  └ peak hours 12:00–18:00", options: { fontSize: 10.5, color: C.muted } },
     { text: condB["12:00-18:00 (peak)"].coverage.toFixed(3), options: { fontSize: 11, color: C.bad, bold: true } },
     { text: condB["12:00-18:00 (peak)"].mean_width.toFixed(0) + " MW", options: { fontSize: 10.5 } },
     { text: "worst exactly where it matters", options: { fontSize: 10.5, color: C.bad } }],
    [{ text: "After CQR calibration", options: { fontSize: 11, bold: true, color: C.ink, fill: { color: "EAF2EC" } } },
     { text: R.m5.coverage_calibrated.toFixed(3), options: { fontSize: 11, bold: true, color: C.good, fill: { color: "EAF2EC" } } },
     { text: R.m5.mean_width_after.toFixed(0) + " MW", options: { fontSize: 11, fill: { color: "EAF2EC" } } },
     { text: "hits nominal 90%", options: { fontSize: 11, color: C.good, fill: { color: "EAF2EC" } } }],
    [{ text: "  └ peak hours 12:00–18:00", options: { fontSize: 10.5, color: C.muted, fill: { color: "FDF3E3" } } },
     { text: cond["12:00-18:00 (peak)"].coverage.toFixed(3), options: { fontSize: 11, bold: true, color: C.warn, fill: { color: "FDF3E3" } } },
     { text: cond["12:00-18:00 (peak)"].mean_width.toFixed(0) + " MW", options: { fontSize: 10.5, fill: { color: "FDF3E3" } } },
     { text: "STILL 5 points short", options: { fontSize: 10.5, color: C.warn, bold: true, fill: { color: "FDF3E3" } } }],
    [{ text: "  └ all other hours", options: { fontSize: 10.5, color: C.muted } },
     { text: cond["other hours"].coverage.toFixed(3), options: { fontSize: 11, color: C.good } },
     { text: cond["other hours"].mean_width.toFixed(0) + " MW", options: { fontSize: 10.5 } },
     { text: "over-covers, subsidising the peak", options: { fontSize: 10.5, color: C.muted } }],
  ], 7.3, 1.55, 5.42, { size: 11, rowH: 0.42, colW: [1.95, 0.95, 1.02, 1.5] });
  L.card(s, 7.3, 4.5, 5.42, 2.1, "12365A");
  s.addText("What you tell operations", { x: 7.55, y: 4.65, w: 4.9, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 11.5, bold: true, color: C.gold, margin: 0 });
  s.addText("“The 90% interval holds 90% of the time overall, and 85% of the time on summer afternoons — the hours you actually size reserve for. Here is the adaptive-conformal fix, and here is the margin to add until it ships.”",
    { x: 7.55, y: 4.98, w: 4.9, h: 1.5, isTextBox: true, fontFace: F.head, fontSize: 13,
      italic: true, color: C.paper, margin: 0, lineSpacing: 19 });
  s.addText("Report marginal AND conditional coverage. Ship both, or ship neither.", { x: 0.62,
    y: 5.0, w: 6.35, h: 0.35, isTextBox: true, fontFace: F.body, fontSize: 13, bold: true,
    color: C.gold, margin: 0 });
  L.bullets(s, [
    "Coverage is the FIRST metric to drift when a model goes stale — before point error degrades",
    "Among calibrated methods, the sharper interval wins. Among un-calibrated ones, sharpness is meaningless",
    "Winkler / interval score combines both: width plus a penalty for every miss",
  ], 0.62, 5.4, 6.35, 1.25, { size: 11, color: C.onDark, space: 4 });
  s.addNotes("Run the 'coverage courtroom' (15 min): one pair defends their interval's 90% claim, another cross-examines using the held-out conditional numbers. It teaches the difference between marginal and conditional better than any slide can.");

  // ================================================= M5: LAB 5 ============
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Calibrated day-ahead intervals", "M5 · HANDS-ON LAB 5  ·  50 MINUTES  ·  SPANS DAY 2 → DAY 3");
  s.addImage({ path: IMG("05_interval.png"), x: 0.62, y, w: 5.35, h: 2.49 });
  s.addText("The band is not decoration — it is the number operations sizes reserve from.",
    { x: 0.62, y: y + 2.55, w: 6.35, h: 0.3, isTextBox: true, fontFace: F.body, fontSize: 10.5,
      italic: true, color: C.muted, margin: 0 });
  L.card(s, 7.25, y, 5.47, 3.0, C.deep);
  s.addText("git checkout lab5-start", { x: 7.5, y: y + 0.15, w: 5.0, h: 0.28, isTextBox: true,
    fontFace: F.mono, fontSize: 10.5, color: "6BCB77", margin: 0 });
  [["5", "The starter reports a CONFIDENCE interval and estimates coverage on the training set. Find both bugs."],
   ["10", "Reuse the Lab 4 features. Split train / calibration / test by time. Fit quantiles τ ∈ {0.05, 0.50, 0.95}. Repair crossing."],
   ["10", "Coverage and mean width of the raw band on test. Expect it BELOW 90%."],
   ["10", "Calibrate with CQR on the held-out window; re-apply; coverage should snap to ≈ 0.90."],
   ["10", "Add the analytic SARIMAX interval. Build the method × coverage × width × pinball table. Plot all three over one hot week."],
   ["5", "Recommend one method in INTERVALS.md and commit."]].forEach(([m, t], i) => {
    const yy = y + 0.44 + i * 0.42;
    L.circle(s, 7.5, yy + 0.01, 0.36, i === 0 ? C.bad : C.teal, m);
    s.addText(t, { x: 7.98, y: yy - 0.02, w: 4.55, h: 0.42, isTextBox: true, fontFace: F.body,
      fontSize: 9.2, color: C.onDark, margin: 0, valign: "middle", lineSpacing: 11.5 });
  });
  const cB31 = L.code(s, [
    "$ python -m tayyar.models.run_intervals",
    "Test window: 61 days hourly | calibration: the 31 days before it",
    { t: "LGBM quantile raw  : coverage=0.786  width=2418 MW  pinball=190", c: "F2A8A8" },
    { t: "LGBM quantile + CQR: coverage=0.902  width=3235 MW  pinball=181", c: "6BCB77" },
    { t: "                     q-hat = 409 MW  (the calibration correction)", c: "6BCB77" },
    "Conditional (12:00-18:00): 0.845   <- report this, always",
    "Recommendation: CQR — the only method reaching nominal coverage;",
    "                flag the peak-hour gap and propose ACI as the fix",
    "Wrote intervals_hotweek.png, coverage_table.csv, INTERVALS.md",
  ], 0.62, y + 3.05, 12.1, 0, { size: 8.4 });
  L.card(s, 0.62, cB31 + 0.10, 12.1, 0.58, "FBEEEC");
  s.addText("Troubleshooting:  coverage ≈ 1.0 with a huge width → alpha confused (0.10 is the tail, not 0.90) · q95 < q50 → crossing, sort the row · CQR barely changes anything → you calibrated on the training set · coverage fine but the decision still fails on hot days → marginal, not conditional.",
    { x: 0.9, y: cB31 + 0.10, w: 11.54, h: 0.58, isTextBox: true, valign: "middle", fontFace: F.body,
      fontSize: 10.5, color: C.bad, margin: 0, lineSpacing: 14 });
  s.addNotes("This lab is deliberately split across the day boundary. End Day 2 after task 3 — with the room holding an interval that visibly under-covers. They will think about it overnight, and the CQR fix on Day 3 morning lands much harder.");

  return pres;
};
