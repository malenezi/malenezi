const L = require("./lib"); const { C, F } = L;

module.exports = function part4(pres, R, LK, IMG) {
  const S = () => pres.addSlide();
  let s, y;

  // =========================================================== M4 TITLE ====
  s = S(); L.bg(s, C.paper);
  s.addShape("roundRect", { x: 0.62, y: 0.9, w: 12.1, h: 5.7, rectRadius: 0.08,
    fill: { color: C.paperAlt }, line: { width: 0 } });
  s.addText("MODULE 4  ·  DAY 2, HOURS 3–4  ·  LO3 · LO4", { x: 1.1, y: 1.35, w: 8, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.teal, charSpacing: 2.5, margin: 0 });
  s.addText("Feature-Based\nML Forecasting", { x: 1.1, y: 1.7, w: 7.6, h: 1.5, isTextBox: true,
    fontFace: F.head, fontSize: 34, bold: true, color: C.ink, margin: 0, lineSpacing: 42 });
  s.addText("Reduce forecasting to supervised learning and a great deal becomes easy: nonlinear weather response, interactions, many covariates, many series. The catch — hammered throughout this module — is that every convenience of ML forecasting is also a fresh way to leak the future.",
    { x: 1.1, y: 3.3, w: 7.4, h: 1.2, isTextBox: true, fontFace: F.body, fontSize: 14,
      color: C.muted, margin: 0, lineSpacing: 20 });
  [["4.1", "Reduce a forecasting task to a supervised feature matrix without leakage"],
   ["4.2", "Engineer lag, rolling-window, calendar and Fourier features"],
   ["4.3", "Train and tune gradient-boosting models for forecasting"],
   ["4.4", "Choose recursive versus direct multi-step strategies"],
   ["4.5", "Interpret feature importance and compare against classical baselines"]].forEach(([k, t], i) => {
    s.addText(k, { x: 1.1, y: 4.62 + i * 0.4, w: 0.55, h: 0.34, isTextBox: true, fontFace: F.body,
      fontSize: 11.5, bold: true, color: C.mid, margin: 0, valign: "middle" });
    s.addText(t, { x: 1.68, y: 4.62 + i * 0.4, w: 7.0, h: 0.34, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, color: C.ink, margin: 0, valign: "middle" });
  });
  s.addImage({ path: IMG("D1_leakage_split.png"), x: 8.85, y: 2.55, w: 3.6, h: 1.36 });
  s.addText("THE ONLY SPLIT THAT MEANS ANYTHING", { x: 8.85, y: 2.2, w: 3.6, h: 0.28,
    isTextBox: true, fontFace: F.body, fontSize: 9.5, bold: true, color: C.bad, charSpacing: 1.5, margin: 0 });
  s.addNotes("Open this module by putting the leakage-smell poster on the wall and telling the room you will point at it every time a shuffle appears. Everything else in Module 4 is technique; this is ethics.");

  // ======================================== M4: THE FEATURE FAMILIES ======
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Five families, one rule", "M4 · LEAKAGE-SAFE FEATURE ENGINEERING");
  s.addText("Every feature must be computable at the forecast origin using only the past. That single rule generates all five families and rejects everything else.",
    { x: 0.62, y, w: 12.1, h: 0.35, isTextBox: true, fontFace: F.body, fontSize: 13.5,
      color: C.muted, margin: 0 });
  const fam = [
    ["Lags", "y at 1, 2, 3, 24, 25, 48, 168, 336 hours ago", "Choose them from the ACF, not from a guess", C.mid],
    ["Rolling windows", "mean · std · min · max over the past 24 h and 168 h", "The window must END before the target — .shift(1) first", C.bad],
    ["Calendar", "hour, day-of-week, month, is_weekend, Ramadan, Eid", "KSA weekend is Fri(4) + Sat(5) in pandas dayofweek", C.teal],
    ["Fourier terms", "k sin/cos pairs per period: 24, 168, 8766", "Encodes daily + weekly + annual jointly, in few columns", C.gold],
    ["Exogenous", "cooling and heating degrees, temp interactions", "Only if a FORECAST of it exists at origin time", C.good],
  ];
  fam.forEach(([n, d, note, col], i) => {
    const yy = y + 0.5 + i * 0.83;
    L.card(s, 0.62, yy, 6.55, 0.72, i % 2 ? C.paperAlt : "FFFFFF");
    s.addShape("roundRect", { x: 0.78, y: yy + 0.13, w: 0.2, h: 0.46, rectRadius: 0.03,
      fill: { color: col }, line: { width: 0 } });
    s.addText(n, { x: 1.1, y: yy + 0.05, w: 1.85, h: 0.32, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, bold: true, color: col, margin: 0, valign: "middle" });
    s.addText(d, { x: 1.1, y: yy + 0.35, w: 5.9, h: 0.3, isTextBox: true, fontFace: F.body,
      fontSize: 10.5, color: C.muted, margin: 0, valign: "middle" });
    s.addText(note, { x: 3.0, y: yy + 0.05, w: 4.0, h: 0.32, isTextBox: true, fontFace: F.body,
      fontSize: 10.5, color: C.ink, margin: 0, valign: "middle" });
  });
  L.code(s, [
    "def add_rolling_features(df, col, windows=(24, 168)):",
    { t: "    base = out[col].shift(1)        # <-- the leakage guard", c: "F2C14E", b: true },
    "    for w in windows:",
    { t: "        r = base.rolling(w, center=False)  # NEVER center=True", c: "F2C14E" },
    "        out[f\"{col}_rmean{w}\"] = r.mean()",
    "        out[f\"{col}_rstd{w}\"]  = r.std()",
    "",
    "def assert_no_leakage(df, target=\"demand_mw\"):",
    "    \"\"\"A. no feature correlates ~1.0 with the target",
    "       B. shuffling the FUTURE must not change any past feature\"\"\"",
    { t: "    ...  -> assert_no_leakage: PASS (44 features checked)", c: "6BCB77" },
  ], 7.45, y + 0.5, 5.27, 0, { size: 9 });
  L.card(s, 7.45, y + 3.42, 5.27, 1.5, "FBEEEC");
  s.addText("Trees cannot extrapolate", { x: 7.7, y: y + 3.55, w: 4.8, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 12, bold: true, color: C.bad, margin: 0 });
  s.addText("A gradient-boosted model can never forecast a demand higher than any it has seen. Mitigate by modelling a differenced or relative target so the level trend is handled outside the trees — or accept it and keep a classical model in the candidate set.",
    { x: 7.7, y: y + 3.88, w: 4.8, h: 1.0, isTextBox: true, fontFace: F.body, fontSize: 10.5,
      color: C.ink, margin: 0, lineSpacing: 14.5 });
  s.addNotes("Run 'what does this feature see?' (10 min): show eight candidate features one at a time, class votes leak or safe with thumbs. Include one genuinely ambiguous case — temperature — and let the argument happen.");

  // =============================== M4: RECURSIVE vs DIRECT + IMPORTANCE ===
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Twenty-four models, or one model twenty-four times?", "M4 · MULTI-STEP STRATEGY");
  L.card(s, 0.62, y, 5.9, 2.3, C.paperAlt);
  s.addText("RECURSIVE", { x: 0.88, y: y + 0.16, w: 2.4, h: 0.3, isTextBox: true, fontFace: F.body,
    fontSize: 12, bold: true, color: C.teal, margin: 0, charSpacing: 1.5 });
  s.addText("One model for one step. Feed its own predictions back in as lags.", { x: 0.88,
    y: y + 0.48, w: 5.35, h: 0.35, isTextBox: true, fontFace: F.body, fontSize: 12, color: C.ink, margin: 0 });
  L.bullets(s, [
    "Compact — a single model to train, tune and serve",
    "Errors compound: by h = 24 the lags are predictions of predictions",
    "Predicted lags have a different distribution from real lags",
  ], 0.88, y + 0.9, 5.35, 1.25, { size: 11.5, space: 4 });
  L.card(s, 6.82, y, 5.9, 2.3, "EAF2EC");
  s.addText("DIRECT  ·  what Tayyar uses", { x: 7.08, y: y + 0.16, w: 3.6, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 12, bold: true, color: C.good, margin: 0, charSpacing: 1.5 });
  s.addText("One model per horizon h, each trained on the target y shifted −h.", { x: 7.08,
    y: y + 0.48, w: 5.35, h: 0.35, isTextBox: true, fontFace: F.body, fontSize: 12, color: C.ink, margin: 0 });
  L.bullets(s, [
    "No compounding — h = 24 is predicted directly from origin features",
    "H models to train, and no guarantee of coherence across horizons",
    "At a 24-hour day-ahead horizon this is where recursive chains fall apart",
  ], 7.08, y + 0.9, 5.35, 1.25, { size: 11.5, space: 4 });
  const cB24 = L.code(s, [
    "class DirectLGBMForecaster:",
    "    def fit(self, X, y):",
    "        for h in range(1, self.horizon + 1):",
    { t: "            yh = y.shift(-h)          # the target is h steps AHEAD", c: "F2C14E" },
    "            ok = yh.notna() & X.notna().all(axis=1)",
    "            self.models_[h] = lgb.LGBMRegressor(**self.params)",
    "                                  .fit(X[ok], yh[ok])",
  ], 0.62, y + 2.5, 6.1, 0, { size: 9.5 });
  s.addText("Decision rule:  short horizons with strong autocorrelation → recursive.  Longer horizons, or any compounding risk → direct.",
    { x: 0.62, y: cB24 + 0.14, w: 6.1, h: 0.6, isTextBox: true, fontFace: F.body, fontSize: 11.5,
      italic: true, color: C.muted, margin: 0, lineSpacing: 15 });
  s.addImage({ path: IMG("04_feature_importance.png"), x: 6.9, y: y + 2.5, w: 5.82, h: 2.18 });
  s.addText("Importance is associational, never causal. “hour_of_day is 9% of the gain” is a description of the model, not a claim about the grid.",
    { x: 6.9, y: y + 4.75, w: 5.82, h: 0.5, isTextBox: true, fontFace: F.body, fontSize: 10.5,
      italic: true, color: C.muted, margin: 0, lineSpacing: 14 });
  s.addNotes("The importance-by-family roll-up is the useful version for a control room: rolling statistics 33%, lags 29%, Fourier terms 26%, calendar 7%, weather 5%. That is a sentence an engineer can act on.");

  // ======================================= M4: THE LEAKAGE DEMONSTRATION ==
  s = S(); L.bg(s, C.deep);
  s.addText("M4 · THE MEASUREMENT THAT MATTERS", { x: 0.62, y: 0.45, w: 8, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 11.5, bold: true, color: C.gold, charSpacing: 2.5, margin: 0 });
  s.addText("One model. One dataset. One target. Four evaluation designs.", { x: 0.62, y: 0.8,
    w: 11.5, h: 0.6, isTextBox: true, fontFace: F.head, fontSize: 29, bold: true, color: C.paper, margin: 0 });
  s.addImage({ path: IMG("08_leakage.png"), x: 0.62, y: 1.55, w: 7.55, h: 3.51 });
  const rows = [
    ["A", "Shuffle split + leaky features", LK.A_shuffle_plus_leaky_features, "A centred rolling window and a \"known\" exogenous value that is not. This is the number that gets a model promoted.", "F2A8A8"],
    ["B", "Shuffle split, clean features", LK.B_shuffle_clean_features, "The split alone still leaks: test hours sit between training hours.", "F2C14E"],
    ["C", "Time-ordered split, clean", LK.C_time_split_clean, "Honest, but a single split is a sample of one.", "E8D9A0"],
    ["D", "Rolling-origin backtest", LK.D_rolling_origin_clean, "Eight origins, refit at each. This is the only number you could defend.", "9DD9A8"],
  ];
  rows.forEach(([k, t, v, d, col], i) => {
    const yy = 1.55 + i * 0.95;
    L.circle(s, 8.5, yy + 0.1, 0.42, i === 3 ? C.good : (i === 0 ? C.bad : C.warn), k);
    s.addText(t, { x: 9.05, y: yy, w: 2.7, h: 0.32, isTextBox: true, fontFace: F.body,
      fontSize: 12, bold: true, color: C.paper, margin: 0, valign: "middle" });
    s.addText(v.toFixed(2) + "%", { x: 11.7, y: yy, w: 1.05, h: 0.32, isTextBox: true, align: "right",
      fontFace: F.head, fontSize: 16, bold: true, color: col, margin: 0, valign: "middle" });
    s.addText(d, { x: 9.05, y: yy + 0.34, w: 3.7, h: 0.62, isTextBox: true, fontFace: F.body,
      fontSize: 10, color: C.onDarkMut, margin: 0, lineSpacing: 13.5 });
  });
  L.card(s, 0.62, 5.45, 12.1, 1.35, "12365A");
  s.addText("The leaked design reports a model that is 2.3× more accurate than the same model actually is. Nothing in the code errored. Nothing in the notebook looked wrong. The only defence is a measurement protocol that makes it structurally impossible — which is Module 6.",
    { x: 0.95, y: 5.45, w: 11.44, h: 1.35, isTextBox: true, valign: "middle", fontFace: F.head,
      fontSize: 15, italic: true, color: C.paper, margin: 0, lineSpacing: 22 });
  s.addNotes("This is the single most important slide in the course. Do not rush it. Ask the room which of the four numbers they have personally reported in a project. Then ask what would have caught it. Practical Assessment 2 is exactly this exercise, unassisted.");

  // ================================================== M4: LAB 4 ===========
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Build the forecaster — and find the two planted leaks first", "M4 · HANDS-ON LAB 4  ·  50 MINUTES");
  L.card(s, 0.62, y, 6.1, 4.15, C.paperAlt);
  s.addText("git checkout lab4-start", { x: 0.88, y: y + 0.15, w: 5.6, h: 0.3, isTextBox: true,
    fontFace: F.mono, fontSize: 11, color: C.good, margin: 0 });
  [["5", "The starter ships a train_test_split(shuffle=True) AND a centred rolling feature. Find both before writing any new code. Record them in LEAKS.md."],
   ["12", "Build lags (chosen from the Lab 2 ACF), rolling windows with .shift(1), calendar flags, and Fourier terms for daily + weekly. Verify with assert_no_leakage."],
   ["12", "Direct targets for H = 24. Split BY TIME — last 28 days is test. Train one LightGBM per horizon."],
   ["8", "Forecast the test window day by day. Compute MAE and MAPE. Overlay the actuals and the Lab 3 SARIMAX baseline."],
   ["8", "Build the feature-importance table and interpret the top five aloud."],
   ["5", "Commit: feat(models): leakage-safe LightGBM direct forecaster"]].forEach(([m, t], i) => {
    const yy = y + 0.55 + i * 0.6;
    L.circle(s, 0.88, yy + 0.05, 0.42, i === 0 ? C.bad : C.mid, m);
    s.addText(t, { x: 1.42, y: yy, w: 5.1, h: 0.55, isTextBox: true, fontFace: F.body,
      fontSize: 10.5, color: C.ink, margin: 0, valign: "middle", lineSpacing: 14 });
  });
  L.code(s, [
    "$ python -m tayyar.models.run_lgbm",
    { t: "Leak check: PASS (44 features, none reference t or the future)", c: "6BCB77" },
    "Direct H=24 trained (24 models) in 11.4s",
    { t: "Test (28d, hourly)  LightGBM: MAE=719 MW  MAPE=2.33%", c: "CFE3F5" },
    { t: "Baseline compare    seasonal-naive: MAE=1244 MW  MAPE=4.12%", c: "CFE3F5" },
    "Top features: demand_lag3, d_cos1, roll_mean_168, hour, roll_mean_24",
    "By family: rolling 33% | lags 29% | fourier 26% | calendar 7% | weather 5%",
    "Wrote forecast_lgbm.png, importance.png, LEAKS.md",
  ], 7.0, y, 5.72, 0, { size: 8.6 });
  s.addText("Troubleshooting", { x: 7.0, y: y + 2.12, w: 5.72, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 12.5, bold: true, color: C.ink, margin: 0 });
  L.table(s, [
    L.hrow(["Symptom", "Cause"], C.bad),
    L.crow(["MAPE suspiciously below 0.7%", "a leak survives — re-run assert_no_leakage"], { fill: "FBEEEC" }),
    L.crow(["Model under-forecasts a heat spike", "trees cannot extrapolate — model a differenced target"]),
    L.crow(["Most rows dropped, tiny training set", "long lags create leading NaNs; expected"], { fill: "F7FAFC" }),
    L.crow(["Weekend flag on wrong days", "KSA weekend is Fri(4) / Sat(5), Mon = 0"]),
  ], 7.0, y + 2.48, 5.72, { size: 9, rowH: 0.32, colW: [2.4, 3.32] });
  L.card(s, 0.62, y + 4.42, 12.1, 0.68, "FDF3E3");
  s.addText("Protect this lab's full 50 minutes. It and Lab 6 are the two most overrun-prone sessions in the course — and they carry the two ideas the whole course exists to teach.",
    { x: 0.9, y: y + 4.42, w: 11.54, h: 0.68, isTextBox: true, valign: "middle", fontFace: F.body,
      fontSize: 12.5, italic: true, color: C.warn, margin: 0 });
  s.addNotes("Run this as a race: first pair to find both leaks and name them precisely wins. It converts a dry debugging task into the moment they will remember six months later.");

  return pres;
};
