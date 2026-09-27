const L = require("./lib"); const { C, F } = L;

module.exports = function part3(pres, R, IMG) {
  const S = () => pres.addSlide();
  let s, y;

  // =========================================================== M2 TITLE ====
  s = S(); L.bg(s, C.paper);
  s.addShape("roundRect", { x: 0.62, y: 0.9, w: 12.1, h: 5.7, rectRadius: 0.08,
    fill: { color: C.paperAlt }, line: { width: 0 } });
  s.addText("MODULE 2  ·  DAY 1, HOURS 4–5  ·  LO1 · LO2", { x: 1.1, y: 1.35, w: 8, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.teal, charSpacing: 2.5, margin: 0 });
  s.addText("Stationarity and\nAutocorrelation", { x: 1.1, y: 1.7, w: 7.6, h: 1.5, isTextBox: true,
    fontFace: F.head, fontSize: 34, bold: true, color: C.ink, margin: 0, lineSpacing: 42 });
  s.addText("Classical models assume stationarity. Diagnose it, transform to it, then read autocorrelation to fingerprint the model. Mistaking a trend for a stationary mean is the single most expensive analytical error in demand and economic forecasting.",
    { x: 1.1, y: 3.3, w: 7.4, h: 1.05, isTextBox: true, fontFace: F.body, fontSize: 14,
      color: C.muted, margin: 0, lineSpacing: 20 });
  [["2.1", "Define weak stationarity and identify sources of non-stationarity"],
   ["2.2", "Apply and reconcile ADF and KPSS tests"],
   ["2.3", "Apply regular and seasonal differencing to achieve stationarity"],
   ["2.4", "Compute and interpret ACF and PACF"],
   ["2.5", "Translate ACF/PACF signatures into candidate ARIMA orders"]].forEach(([k, t], i) => {
    s.addText(k, { x: 1.1, y: 4.5 + i * 0.4, w: 0.55, h: 0.34, isTextBox: true, fontFace: F.body,
      fontSize: 11.5, bold: true, color: C.mid, margin: 0, valign: "middle" });
    s.addText(t, { x: 1.68, y: 4.5 + i * 0.4, w: 7.0, h: 0.34, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, color: C.ink, margin: 0, valign: "middle" });
  });
  L.card(s, 8.95, 2.4, 3.45, 2.85, "0D2136");
  s.addText("Weak stationarity", { x: 9.2, y: 2.55, w: 3.0, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 12, bold: true, color: C.gold, margin: 0 });
  s.addText("Three things constant over time:", { x: 9.2, y: 2.88, w: 3.0, h: 0.28,
    isTextBox: true, fontFace: F.body, fontSize: 11, color: C.onDarkMut, margin: 0 });
  ["the mean", "the variance", "the autocovariance at each lag k\n(depends on the gap, not the position)"].forEach((t, i) => {
    s.addText("▪  " + t, { x: 9.2, y: 3.2 + i * 0.42, w: 3.0, h: 0.4, isTextBox: true,
      fontFace: F.body, fontSize: 10.5, color: "CFE3F5", margin: 0, lineSpacing: 13 });
  });
  s.addText("ARIMA estimates ONE parameter set and assumes it holds throughout.",
    { x: 9.2, y: 4.65, w: 3.0, h: 0.5, isTextBox: true, fontFace: F.body, fontSize: 10.5,
      italic: true, color: C.sky, margin: 0, lineSpacing: 14 });
  s.addNotes("Tayyar has all three sources of non-stationarity: a growth trend, multi-period seasonality, and summer-amplified variance. Fix order matters: stabilise variance first (the log from Module 1), then difference.");

  // ==================================================== M2: ADF vs KPSS ====
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Two tests, opposite nulls — and the disagreement is the information",
    "M2 · TESTING STATIONARITY", { size: 27 });
  s.addImage({ path: IMG("D2_adf_kpss.png"), x: 0.62, y: y - 0.05, w: 6.9, h: 4.0 });
  L.code(s, [
    "adf_stat, adf_p, *_ = adfuller(s, autolag=\"AIC\")",
    "kpss_stat, kpss_p, *_ = kpss(s, regression=\"c\", nlags=\"auto\")",
    "",
    { t: "adf_stationary  = adf_p  < 0.05   # reject the unit root", c: "6BCB77" },
    { t: "kpss_stationary = kpss_p > 0.05   # fail to reject stationarity", c: "6BCB77" },
    "",
    "verdict, action = RECONCILE[(adf_stationary, kpss_stationary)]",
  ], 7.75, y - 0.05, 4.97, 0, { size: 9.5 });
  s.addText("What Tayyar reports", { x: 7.75, y: y + 1.85, w: 4.97, h: 0.32, isTextBox: true,
    fontFace: F.body, fontSize: 12.5, bold: true, color: C.ink, margin: 0 });
  L.table(s, [
    L.hrow(["Series", "ADF p", "KPSS p", "Verdict"]),
    L.crow(["log(demand), level", R.m2.trace[0].adf_p, R.m2.trace[0].kpss_p, "difference-stationary"], { fill: "FDF3E3" }),
    L.crow(["after D = 1, m = 24", R.m2.trace[1].adf_p.toFixed(2), R.m2.trace[1].kpss_p, "stationary"], { fill: "EAF2EC" }),
  ], 7.75, y + 2.2, 4.97, { size: 10.5, rowH: 0.34, colW: [1.75, 0.85, 0.95, 1.42] });
  L.card(s, 7.75, y + 3.4, 4.97, 1.55, C.paperAlt);
  s.addText("The result that surprises people", { x: 7.98, y: y + 3.52, w: 4.5, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.warn, margin: 0 });
  s.addText("One SEASONAL difference at lag 24 was enough. No regular difference was needed at all: D = 1, d = 0. Difference as little as possible — over-differencing injects artificial negative autocorrelation and inflates variance.",
    { x: 7.98, y: y + 3.85, w: 4.5, h: 1.05, isTextBox: true, fontFace: F.body, fontSize: 11,
      color: C.ink, margin: 0, lineSpacing: 15 });
  s.addText("Mistakes to plant and catch:  reading ADF's null backwards (\"p > 0.05 so it's stationary\") · differencing before stabilising variance · reading the ACF of a non-stationary series and calling its slow decay a high AR order.",
    { x: 0.62, y: y + 4.1, w: 6.9, h: 0.85, isTextBox: true, fontFace: F.body, fontSize: 11,
      color: C.muted, margin: 0, lineSpacing: 15 });
  s.addNotes("Run the verdict-reconciliation drill here (10 min): call out p-value pairs and have the room say the reconciled verdict aloud. Quiz them cold — the nulls being backwards is the single most common error on Day 1.");

  // ============================================ M2: ACF/PACF FINGERPRINT ===
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "The correlogram is a fingerprint, not a decoration", "M2 · READING ACF AND PACF");
  s.addImage({ path: IMG("D7_fingerprint.png"), x: 1.35, y: y - 0.1, w: 10.6, h: 3.85 });
  L.table(s, [
    L.hrow(["ACF", "PACF", "Read as", "In practice"]),
    L.crow(["tails off (geometric decay)", "cuts off after lag p", "AR(p)", "PACF gives the order"]),
    L.crow(["cuts off after lag q", "tails off", "MA(q)", "ACF gives the order"], { fill: "F7FAFC" }),
    L.crow(["tails off", "tails off", "ARMA(p, q)", "use AICc / BIC to choose"]),
    L.crow(["slow, near-linear decay", "large spike at lag 1", "NOT stationary", "difference before reading further"], { fill: "FDF3E3", color: C.warn }),
    L.crow(["spikes at m, 2m, 3m …", "spike at lag m", "seasonal terms", "set P, Q and m"], { fill: "F7FAFC" }),
  ], 0.62, y + 3.88, 12.1, { size: 10.5, rowH: 0.3, colW: [3.1, 2.6, 2.4, 4.0] });
  s.addText("“Cuts off” means it drops inside the ±1.96/√n band. Default lags = 20 never reaches lag 24 — set lags ≥ 2m or the seasonal spike is invisible.",
    { x: 0.62, y: y + 5.85, w: 12.1, h: 0.35, isTextBox: true, fontFace: F.body, fontSize: 11,
      italic: true, color: C.muted, margin: 0 });
  s.addNotes("Run the ACF/PACF speed round: six anonymised correlogram pairs, 30 seconds each, teams call the model class and order. It is the fastest way to make the fingerprint table stick.");

  // ==================================== M2: LAB 2 + Tayyar correlograms ====
  s = S(); L.bg(s, C.deep);
  s.addText("HANDS-ON LAB 2  ·  50 MINUTES  ·  PAIRS", { x: 0.62, y: 0.55, w: 8, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.gold, charSpacing: 2.5, margin: 0 });
  s.addText("The stationarity report", { x: 0.62, y: 0.9, w: 9.5, h: 0.6, isTextBox: true,
    fontFace: F.head, fontSize: 29, bold: true, color: C.paper, margin: 0 });
  s.addText("git checkout lab2-start", { x: 10.3, y: 0.95, w: 2.4, h: 0.45, isTextBox: true,
    fontFace: F.mono, fontSize: 11, color: "6BCB77", align: "right", margin: 0, valign: "middle" });
  [["8", "Run stationarity_report on raw log-demand. Interpret ADF and KPSS TOGETHER. Record the verdict and predict the differencing needed."],
   ["10", "choose_differencing(m=24) — seasonal FIRST, then regular. Re-run the report to confirm stationarity was actually reached."],
   ["10", "Plot before and after. Check the lag-1 ACF for the over-differencing signature (strongly negative, < −0.5). Reduce d if you see it."],
   ["12", "ACF/PACF with lags ≥ 60. Annotate the seasonal spike at lag 24. Read candidate (p, q) and seasonal (P, Q)."],
   ["10", "Write STATIONARITY.md: verdict, chosen (d, D), and 2–3 candidate SARIMA orders with justification. Commit."]].forEach(([m, t], i) => {
    const yy = 1.8 + i * 0.83;
    L.circle(s, 0.62, yy + 0.1, 0.48, i < 2 ? C.mid : C.teal, m);
    s.addText(t, { x: 1.3, y: yy, w: 5.9, h: 0.75, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, color: C.onDark, margin: 0, valign: "middle", lineSpacing: 16 });
  });
  s.addImage({ path: IMG("03_acf_pacf.png"), x: 7.5, y: 1.62, w: 5.25, h: 2.94 });
  L.code(s, [
    "$ python -m tayyar.analysis.run_stationarity",
    { t: "Raw log-demand : ADF p=0.026  KPSS p=0.01", c: "F2C14E" },
    { t: "                 -> difference-stationary", c: "F2C14E" },
    "Suggested       : seasonal first, m=24",
    { t: "After D=1, d=0 : ADF p=0.00  KPSS p=0.10 -> stationary", c: "6BCB77" },
    "ACF/PACF        : PACF cuts near lag 2-5; ACF spike at 24",
    "Candidates      : SARIMA(2,0,1)(1,1,1)[24]",
    "                  SARIMA(1,0,2)(0,1,1)[24]",
    "Wrote acf_pacf.png, STATIONARITY.md",
  ], 7.5, 4.72, 5.25, 0, { size: 9 });
  s.addText("Debugging branch  sim-overdiff  differences twice where once suffices. Diagnose it from the lag-1 ACF near −0.6, then fix it.",
    { x: 0.62, y: 6.1, w: 6.6, h: 0.6, isTextBox: true, fontFace: F.body, fontSize: 11.5,
      italic: true, color: C.sky, margin: 0, lineSpacing: 15 });
  s.addNotes("Watch for pairs who difference until ADF is happy and stop thinking. Ask them to look at the lag-1 ACF. Also warn about the statsmodels 'p-value greater than 0.1' KPSS warning — it is expected, and means p > 0.1.");

  // ================================================== DAY 2 SECTION ========
  s = S(); L.bg(s, C.deep);
  s.addShape("ellipse", { x: 10.7, y: 4.4, w: 4.6, h: 4.6, fill: { color: C.teal },
    line: { width: 0 }, transparency: 68 });
  L.titleSlideText(s, "DAY 2 · HOURS 1–5", "Building Forecasts",
    "Three model families, in the order a practitioner should try them: the free baseline, the classical models a control room will accept, and the feature-based ML model that wins when the covariates are rich.");
  [["MODULE 3", "ARIMA and Exponential Smoothing", "LO2 · LO3"],
   ["MODULE 4", "Feature-Based ML Forecasting", "LO3 · LO4"],
   ["MODULE 5", "Probabilistic Forecasts and Intervals (starts)", "LO5"]].forEach(([m, t, lo], i) => {
    const yy = 5.15 + i * 0.42;
    s.addText(m, { x: 0.9, y: yy, w: 1.5, h: 0.36, isTextBox: true, fontFace: F.mono,
      fontSize: 12.5, bold: true, color: C.gold, margin: 0, valign: "middle" });
    s.addText(t, { x: 2.5, y: yy, w: 5.5, h: 0.36, isTextBox: true, fontFace: F.body,
      fontSize: 13, color: C.sky, margin: 0, valign: "middle" });
    s.addText(lo, { x: 8.1, y: yy, w: 1.5, h: 0.36, isTextBox: true, fontFace: F.mono,
      fontSize: 12, color: C.onDarkMut, margin: 0, valign: "middle" });
  });
  s.addNotes("Pair rotation today: put a strong-statistics participant with a strong-ML participant. The M3 to M4 bridge is exactly where that skill transfer pays off.");

  // =========================================================== M3 TITLE ====
  s = S(); L.bg(s, C.paper);
  s.addShape("roundRect", { x: 0.62, y: 0.9, w: 12.1, h: 5.7, rectRadius: 0.08,
    fill: { color: C.paperAlt }, line: { width: 0 } });
  s.addText("MODULE 3  ·  DAY 2, HOURS 1–2  ·  LO2 · LO3", { x: 1.1, y: 1.35, w: 8, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.teal, charSpacing: 2.5, margin: 0 });
  s.addText("ARIMA and\nExponential Smoothing", { x: 1.1, y: 1.7, w: 7.6, h: 1.5, isTextBox: true,
    fontFace: F.head, fontSize: 34, bold: true, color: C.ink, margin: 0, lineSpacing: 42 });
  s.addText("The classical families remain the model to beat in regulated and safety-critical settings — because they can be explained. “The forecast rose because the level term updated and the summer seasonal factor kicked in” is accepted by a control-room engineer. “The gradient boosting said so” is not.",
    { x: 1.1, y: 3.3, w: 7.4, h: 1.2, isTextBox: true, fontFace: F.body, fontSize: 14,
      color: C.muted, margin: 0, lineSpacing: 20 });
  [["3.1", "Specify and fit ARIMA/SARIMA models with justified orders"],
   ["3.2", "Incorporate exogenous regressors with SARIMAX"],
   ["3.3", "Select an exponential-smoothing / ETS specification from the taxonomy"],
   ["3.4", "Diagnose model adequacy from residuals"],
   ["3.5", "Compare ARIMA and ETS and choose per situation"]].forEach(([k, t], i) => {
    s.addText(k, { x: 1.1, y: 4.62 + i * 0.4, w: 0.55, h: 0.34, isTextBox: true, fontFace: F.body,
      fontSize: 11.5, bold: true, color: C.mid, margin: 0, valign: "middle" });
    s.addText(t, { x: 1.68, y: 4.62 + i * 0.4, w: 7.0, h: 0.34, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, color: C.ink, margin: 0, valign: "middle" });
  });
  L.card(s, 8.95, 2.4, 3.45, 2.75, "0D2136");
  s.addText("SARIMA(p, d, q)(P, D, Q)ₘ", { x: 9.2, y: 2.58, w: 3.0, h: 0.32, isTextBox: true,
    fontFace: F.mono, fontSize: 12.5, bold: true, color: C.gold, margin: 0 });
  [["AR(p)", "y depends on its own p past values"],
   ["I(d)", "d differences to reach stationarity"],
   ["MA(q)", "y depends on the last q shocks"],
   ["(P,D,Q)ₘ", "the same three, at the seasonal period m"]].forEach(([k, v], i) => {
    s.addText(k, { x: 9.2, y: 3.02 + i * 0.5, w: 0.95, h: 0.44, isTextBox: true, fontFace: F.mono,
      fontSize: 10.5, bold: true, color: "6BCB77", margin: 0, valign: "middle" });
    s.addText(v, { x: 10.2, y: 3.02 + i * 0.5, w: 2.05, h: 0.44, isTextBox: true, fontFace: F.body,
      fontSize: 10, color: "CFE3F5", margin: 0, valign: "middle", lineSpacing: 13 });
  });
  s.addNotes("Flag the practical constraint early: m = 24 (let alone 168) makes the state space large and estimation slow. Practitioners model a daily-aggregated series with m = 7 and leave sub-daily structure to the ML route. That wall is deliberate and teachable.");

  // ============================== M3: the m=24 wall, order selection, ETS ==
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Where classical methods strain — and what to do about it", "M3 · ORDER SELECTION AND THE m = 24 WALL");
  L.card(s, 0.62, y, 3.9, 2.15, "FBEEEC");
  s.addText("The wall", { x: 0.88, y: y + 0.16, w: 3.4, h: 0.3, isTextBox: true, fontFace: F.body,
    fontSize: 12, bold: true, color: C.bad, margin: 0 });
  s.addText("auto_arima with m = 24 on 26,000 hourly points runs for minutes and may never converge. This is not a bug in your code.",
    { x: 0.88, y: y + 0.5, w: 3.4, h: 0.9, isTextBox: true, fontFace: F.body, fontSize: 12,
      color: C.ink, margin: 0, lineSpacing: 16 });
  s.addText("→  Model the DAILY series with m = 7.\n→  Leave sub-daily structure to Module 4.",
    { x: 0.88, y: y + 1.42, w: 3.4, h: 0.62, isTextBox: true, fontFace: F.body, fontSize: 11.5,
      bold: true, color: C.bad, margin: 0, lineSpacing: 16 });
  L.card(s, 4.72, y, 3.9, 2.15, C.paperAlt);
  s.addText("Order selection", { x: 4.98, y: y + 0.16, w: 3.4, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 12, bold: true, color: C.mid, margin: 0 });
  L.bullets(s, [
    "AR order from the PACF cut-off, MA from the ACF",
    "Minimise AICc (small samples) or BIC (parsimony)",
    "auto_arima proposes; the analyst disposes",
    "NEVER compare AIC across different d — different targets",
  ], 4.98, y + 0.5, 3.4, 1.55, { size: 11.5, space: 5 });
  L.card(s, 8.82, y, 3.9, 2.15, C.paperAlt);
  s.addText("ETS taxonomy", { x: 9.08, y: y + 0.16, w: 3.4, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 12, bold: true, color: C.teal, margin: 0 });
  s.addText("(Error, Trend, Seasonal), each ∈ {None, Additive, Multiplicative}", { x: 9.08,
    y: y + 0.5, w: 3.4, h: 0.5, isTextBox: true, fontFace: F.body, fontSize: 11.5,
    color: C.ink, margin: 0, lineSpacing: 15 });
  s.addText("SES → level only, flat forecast\nHolt → + trend  (damp it)\nHolt-Winters → + seasonality",
    { x: 9.08, y: y + 1.02, w: 3.4, h: 0.65, isTextBox: true, fontFace: F.mono, fontSize: 10.5,
      color: C.mid, margin: 0, lineSpacing: 15 });
  s.addText("Damped trend is almost always the safer production choice.", { x: 9.08, y: y + 1.72,
    w: 3.4, h: 0.35, isTextBox: true, fontFace: F.body, fontSize: 11, bold: true, italic: true,
    color: C.teal, margin: 0, lineSpacing: 14 });

  s.addText("Exogenous regressors must be known at forecast time", { x: 0.62, y: y + 2.28,
    w: 6.0, h: 0.32, isTextBox: true, fontFace: F.body, fontSize: 13, bold: true, color: C.ink, margin: 0 });
  const cB20 = L.code(s, [
    "def make_exog(df):",
    "    out[\"cdd\"] = np.clip(df[\"temp_c\"] - 21.0, 0, None)  # cooling",
    "    out[\"hdd\"] = np.clip(14.0 - df[\"temp_c\"], 0, None)",
    "    for c in (\"is_weekend\", \"is_ramadan\", \"is_eid\"):",
    "        out[c] = df[c].astype(int)",
    "",
    "res = fit_sarimax(y, exog, order=(2,1,1),",
    "                  seasonal_order=(1,1,1,7))",
    "fc  = res.get_forecast(steps=28, exog=exog_future)",
    { t: "                                  # exog_future is REQUIRED", c: "F2C14E" },
  ], 0.62, y + 2.7, 6.0, 0, { size: 8.6 });
  L.card(s, 0.62, cB20 + 0.14, 6.0, 0.8, "FDF3E3");
  s.addText("Temperature qualifies only because a day-ahead weather forecast exists. Use the FORECAST, not the realised value — otherwise you have built a leak that looks like skill.",
    { x: 0.86, y: cB20 + 0.14, w: 5.52, h: 0.8, isTextBox: true, valign: "middle", fontFace: F.body,
      fontSize: 11.5, color: C.warn, margin: 0, lineSpacing: 15.5 });

  s.addText("Residual diagnostics are mandatory, not optional", { x: 6.9, y: y + 2.28, w: 5.8,
    h: 0.32, isTextBox: true, fontFace: F.body, fontSize: 13, bold: true, color: C.ink, margin: 0 });
  L.bullets(s, [
    "Ljung-Box: H₀ = residuals independent. p < 0.05 means autocorrelation remains and the model is under-specified — raise an order",
    "Residual mean ≈ 0 (no bias) and roughly constant variance (the transform worked)",
    "Approximate normality — matters for INTERVAL validity more than for the point forecast",
    "An un-diagnosed auto_arima result is a liability, not a model",
  ], 6.9, y + 2.68, 5.8, 1.75, { size: 12 });
  L.card(s, 6.9, cB20 + 0.14, 5.82, 0.8, "E7EFF7");
  s.addText("On Tayyar's daily-max series the fitted SARIMAX still shows Ljung-Box p ≈ 0.00 — structure remains. Say so out loud: this is what an honest diagnostic looks like, and it is why the ML route exists.",
    { x: 7.14, y: cB20 + 0.14, w: 5.34, h: 0.8, isTextBox: true, valign: "middle", fontFace: F.body,
      fontSize: 11.5, color: C.deep, margin: 0, lineSpacing: 15.5 });
  s.addNotes("Do not hide the failing Ljung-Box. Participants trust a course that shows its own model failing a test it taught. Explain that a daily-max series compresses away the sub-daily structure that would satisfy the diagnostic.");

  // ============================================= M3: RESULTS + LAB 3 ======
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Does the temperature regressor actually pay for itself?", "M3 · LAB 3 AND THE ANSWER IT PRODUCES");
  L.table(s, [
    L.hrow(["Model (daily peak, 28-day hold-out)", "MAE (MW)", "MAPE", "MASE", "Bias (MW)", "Verdict"]),
    L.crow(["SARIMAX + temperature + calendar", R.m3.sarimax.MAE.toFixed(0), R.m3.sarimax["MAPE_%"].toFixed(2) + "%",
            R.m3.sarimax.MASE.toFixed(3), "+" + R.m3.sarimax.bias.toFixed(0), "best point accuracy"],
           { fill: "EAF2EC", boldCols: [0, 3] }),
    L.crow(["SARIMA, no exogenous regressors", R.m3.sarima_no_exog.MAE.toFixed(0), R.m3.sarima_no_exog["MAPE_%"].toFixed(2) + "%",
            R.m3.sarima_no_exog.MASE.toFixed(3), "+" + R.m3.sarima_no_exog.bias.toFixed(0), "temperature is worth ≈ 20 MW of MAE"]),
    L.crow(["ETS(A, Ad, A) — damped trend", R.m3.ets.MAE.toFixed(0), R.m3.ets["MAPE_%"].toFixed(2) + "%",
            R.m3.ets.MASE.toFixed(3), "+" + R.m3.ets.bias.toFixed(0), "no covariates, fits in seconds"], { fill: "F7FAFC" }),
    L.crow(["Seasonal-naive (the free baseline)", R.m3.seasonal_naive.MAE.toFixed(0), R.m3.seasonal_naive["MAPE_%"].toFixed(2) + "%",
            R.m3.seasonal_naive.MASE.toFixed(3), "+" + R.m3.seasonal_naive.bias.toFixed(0), "what everything must beat"], { fill: "FDF3E3" }),
  ], 0.62, y, 12.1, { size: 11.5, rowH: 0.38, colW: [4.1, 1.35, 1.15, 1.1, 1.3, 3.1] });
  s.addText("Read the bias column, not only the error column. The no-exogenous model drifts +142 MW high; adding temperature pulls that to +37 MW. A biased forecast is a systematic reserve error every single day.",
    { x: 0.62, y: y + 2.1, w: 12.1, h: 0.4, isTextBox: true, fontFace: F.body, fontSize: 12,
      italic: true, color: C.muted, margin: 0 });

  L.card(s, 0.62, y + 2.65, 6.0, 3.0, C.deep);
  s.addText("LAB 3  ·  50 min  ·  git checkout lab3-start", { x: 0.9, y: y + 2.82, w: 5.4, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11, bold: true, color: C.gold, margin: 0 });
  s.addText("Classical baselines: SARIMAX and ETS", { x: 0.9, y: y + 3.12, w: 5.4, h: 0.38,
    isTextBox: true, fontFace: F.head, fontSize: 17, bold: true, color: C.paper, margin: 0 });
  L.bullets(s, [
    "5′  Aggregate to daily; build the exog frame from ksa_calendar.csv; hold out the last 28 days",
    "12′  Select the SARIMA order at m = 7; confirm Ljung-Box; raise the order and refit if it fails",
    "10′  Fit ETS with damped trend; read the smoothing parameters from the summary",
    "10′  Forecast 28 days both ways with 90% intervals; SARIMAX needs the FUTURE exog rows",
    "8′  Compute MAE / MAPE / MASE and coverage; run plot_diagnostics",
    "5′  Commit the baselines",
  ], 0.9, y + 3.55, 5.42, 2.0, { size: 11, color: C.onDark, space: 4 });
  s.addText("Watch for", { x: 6.95, y: y + 2.65, w: 5.75, h: 0.32, isTextBox: true,
    fontFace: F.body, fontSize: 13, bold: true, color: C.ink, margin: 0 });
  L.table(s, [
    L.hrow(["Symptom", "What it really is"], C.teal),
    L.crow(["auto_arima runs for minutes", "m = 24 on hourly — switch to the daily series, m = 7"]),
    L.crow(["Ljung-Box p < 0.05", "under-specified; raise an order and refit"], { fill: "F7FAFC" }),
    L.crow(["Forecast diverges to absurd values", "un-damped Holt trend — set damped_trend=True"]),
    L.crow(["get_forecast raises on exog", "supply exactly `steps` rows of future regressors"], { fill: "F7FAFC" }),
    L.crow(["Multiplicative ETS fails", "the series contains a zero (a sensor dropout)"]),
  ], 6.95, y + 3.0, 5.77, { size: 10.5, rowH: 0.33, colW: [2.35, 3.42] });
  s.addNotes("The interactive here is 'explain it to the control room' (10 min): each participant writes ONE sentence explaining the SARIMAX forecast to a non-statistician, then reads it aloud. Ruthlessly cut any sentence containing the word 'parameter'.");

  return pres;
};
