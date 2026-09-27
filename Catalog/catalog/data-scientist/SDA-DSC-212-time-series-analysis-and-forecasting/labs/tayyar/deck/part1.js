const L = require("./lib"); const { C, F } = L;

module.exports = function part1(pres, R, IMG) {
  const S = () => pres.addSlide();

  // ============================================================ 1. TITLE ====
  let s = S(); L.bg(s, C.deep);
  s.addShape("ellipse", { x: 9.1, y: -1.5, w: 6.4, h: 6.4, fill: { color: C.mid },
    line: { width: 0 }, transparency: 55 });
  s.addShape("ellipse", { x: 10.9, y: 3.1, w: 4.2, h: 4.2, fill: { color: C.teal },
    line: { width: 0 }, transparency: 65 });
  s.addText("SDAIA ACADEMY  ·  DATA SCIENTIST TRACK  ·  SDA-DSC-212", {
    x: 0.9, y: 0.85, w: 11.5, h: 0.34, isTextBox: true, fontFace: F.body,
    fontSize: 12, bold: true, color: C.gold, charSpacing: 3 });
  s.addText("Time Series Analysis\nand Forecasting", { x: 0.9, y: 1.7, w: 8.6, h: 2.1,
    isTextBox: true, fontFace: F.head, fontSize: 46, bold: true, color: C.paper,
    lineSpacing: 54 });
  s.addText("تحليل السلاسل الزمنية والتنبؤ", { x: 0.9, y: 3.75, w: 8.6, h: 0.55,
    isTextBox: true, fontFace: "Arial", fontSize: 22, color: C.sky });
  s.addText("Respect the arrow of time — so every accuracy number you report\nwould survive contact with the future.",
    { x: 0.9, y: 4.5, w: 8.4, h: 0.9, isTextBox: true, fontFace: F.head,
      fontSize: 15, italic: true, color: C.onDarkMut, lineSpacing: 22 });
  const meta = [["Level", "Specialist"], ["Duration", "3 days × 5 hours = 15 hours"],
                ["Audience", "Data scientists & analysts working with temporal data"],
                ["Prerequisites", "SDA-DSC-111 · SDA-DSC-211 recommended"],
                ["Assessment", "Forecasting project with backtest report"]];
  meta.forEach(([k, v], i) => {
    s.addText(k.toUpperCase(), { x: 0.9, y: 5.55 + i * 0.3, w: 1.55, h: 0.28, isTextBox: true,
      fontFace: F.body, fontSize: 9, bold: true, color: C.gold, margin: 0, valign: "middle" });
    s.addText(v, { x: 2.5, y: 5.55 + i * 0.3, w: 7.4, h: 0.28, isTextBox: true,
      fontFace: F.body, fontSize: 10.5, color: C.onDark, margin: 0, valign: "middle" });
  });
  s.addNotes("Welcome. Set the frame in one sentence before anything else: this course is not 'more machine learning, but on dates'. It is a discipline about one thing — never letting the future touch the past. Everything for three days advances one artefact, a national load-forecasting service called Tayyar.");

  // ============================================ 2. THE FORECAST THAT LIED ====
  s = S(); L.bg(s, C.paper);
  let y = L.head(s, "A model that was right until it mattered", "OPENING · WHY THIS COURSE EXISTS");
  L.card(s, 0.62, y, 5.9, 3.55, "FBEEEC");
  s.addText("What the report said", { x: 0.92, y: y + 0.22, w: 5.3, h: 0.34, isTextBox: true,
    fontFace: F.body, fontSize: 12, bold: true, color: C.bad, margin: 0, charSpacing: 1.5 });
  L.bullets(s, [
    "A gradient-boosted model scored 0.6% MAPE in validation",
    "It beat the incumbent by a wide margin on every chart",
    "It was promoted to production the following week",
    "Live accuracy collapsed to roughly 4% within days",
  ], 0.92, y + 0.68, 5.3, 2.7, { size: 13.5, color: C.ink });
  L.card(s, 6.82, y, 5.9, 3.55, "EAF2EC");
  s.addText("What had actually happened", { x: 7.12, y: y + 0.22, w: 5.3, h: 0.34, isTextBox: true,
    fontFace: F.body, fontSize: 12, bold: true, color: C.good, margin: 0, charSpacing: 1.5 });
  L.bullets(s, [
    "A rolling-mean feature used a CENTRED window",
    "\"The average of the past 24 hours\" silently contained the target hour",
    "One .shift(1) fixed it — honest accuracy rose to 2.1%",
    "Worse on paper. Real in production.",
  ], 7.12, y + 0.68, 5.3, 2.7, { size: 13.5, color: C.ink });
  L.pull(s, "This failure has a thousand faces and one cause: information from the future reached a model that will never have it. Detecting, preventing and measuring that is the entire content of the next three days.",
    0.62, y + 3.85, 12.1, 1.15);
  s.addNotes("Tell this as a story, not a slide. Ask the room: has anyone shipped a model whose live accuracy did not match its validation accuracy? Almost every hand goes up. Then name the mechanism. Do NOT yet explain what .shift(1) does — Module 4 earns that. Right now they only need to believe the problem is real.");

  // =================================== 3. WHY TIME SERIES BREAKS ORDINARY ML =
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Order is the signal", "HOUR 1 · WHAT MAKES A TIME SERIES DIFFERENT");
  s.addText("An ordinary supervised-learning row is exchangeable — shuffle the dataset and nothing is lost. A time series is the opposite. Three consequences follow, and each of them bites anyone who treats a series like a normal table.",
    { x: 0.62, y, w: 12.1, h: 0.62, isTextBox: true, fontFace: F.body, fontSize: 14,
      color: C.muted, margin: 0, lineSpacing: 20 });
  const three = [
    ["1", "Autocorrelation", "Today is correlated with yesterday. Observations are not independent, so error bars, CV folds and significance tests computed under an i.i.d. assumption are simply wrong.", C.mid],
    ["2", "Temporal leakage", "Any information from the future — a random-split test point, a global mean, a peeking feature — inflates measured accuracy and evaporates in production. This is THE recurring failure of the field.", C.bad],
    ["3", "Non-stationarity", "Mean, variance and seasonal shape drift. A model trained on last year's level will confidently forecast a level that no longer exists.", C.teal],
  ];
  three.forEach(([n, t, d, col], i) => {
    const x = 0.62 + i * 4.13;
    L.card(s, x, y + 0.8, 3.85, 3.35, C.paperAlt);
    L.circle(s, x + 0.28, y + 1.05, 0.55, col, n);
    s.addText(t, { x: x + 0.28, y: y + 1.75, w: 3.3, h: 0.4, isTextBox: true,
      fontFace: F.head, fontSize: 17, bold: true, color: col, margin: 0 });
    s.addText(d, { x: x + 0.28, y: y + 2.2, w: 3.3, h: 1.8, isTextBox: true,
      fontFace: F.body, fontSize: 12.5, color: C.ink, margin: 0, lineSpacing: 17 });
  });
  L.pull(s, "The one non-negotiable rule of this course: every feature, every split, every scaler must be computable using only data that existed at the forecast origin.",
    0.62, y + 4.35, 12.1, 0.85, "FDF3E3");
  s.addNotes("Land 'exchangeable' with a physical demo: shuffle a deck of cards and ask whether anything was lost, then shuffle a sentence's words. The three consequences are the spine of the whole course — Module 2 attacks autocorrelation and non-stationarity, Modules 4 and 6 attack leakage.");

  // ======================================================== 4. THE THREAD ====
  s = S(); L.bg(s, C.deep);
  s.addText("THE GOLDEN THREAD", { x: 0.62, y: 0.55, w: 6, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 11.5, bold: true, color: C.gold, charSpacing: 2.5, margin: 0 });
  s.addText("Tayyar (تيّار)", { x: 0.62, y: 0.88, w: 7, h: 0.75, isTextBox: true,
    fontFace: F.head, fontSize: 34, bold: true, color: C.paper, margin: 0 });
  s.addText("A national day-ahead load-forecasting service for the Central Operating Area of the Saudi grid. Three years of hourly demand, and one series that carries every lesson in this course.",
    { x: 0.62, y: 1.72, w: 6.1, h: 1.25, isTextBox: true, fontFace: F.body, fontSize: 14,
      color: C.onDarkMut, margin: 0, lineSpacing: 20 });
  const props = [
    ["Growth trend", "economic expansion, ≈ +3% a year"],
    ["Daily cycle", "air-conditioning load, period 24"],
    ["Weekly rhythm", "the Friday–Saturday weekend dip"],
    ["Annual peak", "a fierce Riyadh summer, 47 °C afternoons"],
    ["Calendar shocks", "Ramadan, the two Eids, National Day"],
    ["Structural break", "a large industrial customer connects"],
  ];
  props.forEach(([k, v], i) => {
    const yy = 3.05 + i * 0.62;
    L.circle(s, 0.62, yy, 0.34, C.teal, "✓");
    s.addText(k, { x: 1.08, y: yy - 0.02, w: 2.0, h: 0.38, isTextBox: true,
      fontFace: F.body, fontSize: 13, bold: true, color: C.paper, margin: 0, valign: "middle" });
    s.addText(v, { x: 3.05, y: yy - 0.02, w: 3.7, h: 0.38, isTextBox: true,
      fontFace: F.body, fontSize: 12.5, color: C.onDarkMut, margin: 0, valign: "middle" });
  });
  s.addImage({ path: IMG("01_series_overview.png"), x: 7.0, y: 1.0, w: 5.85, h: 3.65 });
  L.card(s, 7.0, 4.95, 5.85, 1.75, "12365A");
  s.addText("The decision the service exists to answer", { x: 7.28, y: 5.1, w: 5.3, h: 0.32,
    isTextBox: true, fontFace: F.body, fontSize: 11, bold: true, color: C.gold, margin: 0 });
  s.addText("“At 14:00 today, how much generation capacity should the operator prepare for each hour tomorrow?”",
    { x: 7.28, y: 5.45, w: 5.3, h: 1.05, isTextBox: true, fontFace: F.head, fontSize: 14.5,
      italic: true, color: C.paper, margin: 0, lineSpacing: 20 });
  L.foot(s, "", "");
  s.addNotes("Emphasise that this is operational, not statistical. A 1% day-ahead error on a 55,000 MW peak is about 550 MW — a mid-size gas turbine held spinning for nothing, or missing when needed. Every lab advances THIS service; nobody builds a throwaway airline-passengers model.");

  // ================================================== 5. LEARNING OUTCOMES ==
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "What you will be able to do on Thursday", "COURSE LEARNING OUTCOMES");
  const los = [
    ["LO1", "Analyse trend, seasonality and autocorrelation structure in time series", "M1 · M2"],
    ["LO2", "Develop classical forecasting models including ARIMA and exponential smoothing", "M3"],
    ["LO3", "Implement ML and gradient-boosting approaches with engineered temporal features", "M4"],
    ["LO4", "Design backtesting frameworks with proper time-based validation", "M6"],
    ["LO5", "Evaluate forecasts using scale-appropriate accuracy and uncertainty metrics", "M5 · M6"],
    ["LO6", "Compare model families to select the right approach per use case", "M7"],
  ];
  los.forEach(([k, t, m], i) => {
    const yy = y + i * 0.79;
    L.card(s, 0.62, yy, 12.1, 0.68, i % 2 ? C.paperAlt : "FFFFFF");
    s.addShape("roundRect", { x: 0.78, y: yy + 0.13, w: 0.78, h: 0.42, rectRadius: 0.05,
      fill: { color: C.mid }, line: { width: 0 } });
    s.addText(k, { x: 0.78, y: yy + 0.13, w: 0.78, h: 0.42, isTextBox: true, align: "center",
      valign: "middle", fontFace: F.body, fontSize: 12.5, bold: true, color: C.paper, margin: 0 });
    s.addText(t, { x: 1.75, y: yy, w: 9.1, h: 0.68, isTextBox: true, valign: "middle",
      fontFace: F.body, fontSize: 14, color: C.ink, margin: 0 });
    s.addText(m, { x: 11.0, y: yy, w: 1.55, h: 0.68, isTextBox: true, valign: "middle",
      align: "right", fontFace: F.body, fontSize: 11.5, bold: true, color: C.teal, margin: 0 });
  });
  s.addText("Assessed by: 7 lab checkpoints (30%) · two practical assessments (20%) · a 10-question quiz (10%) · the capstone backtest report (40%).",
    { x: 0.62, y: y + 5.0, w: 12.1, h: 0.4, isTextBox: true, fontFace: F.body, fontSize: 12,
      color: C.muted, margin: 0 });
  s.addNotes("Read LO4 and LO5 aloud slowly — those two are what distinguish this course from a modelling tutorial. Point out that LO2 and LO3 are only half the grade between them; the evidence is the other half.");

  // ================================================= 6. THREE-DAY MAP =======
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Three days, one deliverable", "DELIVERY PLAN");
  const days = [
    ["DAY 1", "Seeing the signal", C.mid, "M1  Structure & decomposition\nM2  Stationarity & autocorrelation",
     "50% theory / 50% lab", "Clean hourly series + decomposition panel + stationarity report"],
    ["DAY 2", "Building forecasts", C.teal, "M3  ARIMA & exponential smoothing\nM4  Feature-based ML forecasting\nM5  Probabilistic forecasting (start)",
     "45% theory / 55% lab", "SARIMAX, ETS and a LightGBM forecaster, all producing 24 h forecasts"],
    ["DAY 3", "Trust and selection", C.deep, "M5  Intervals & calibration\nM6  Backtesting & evaluation\nM7  Case study + capstone",
     "35% theory / 65% lab", "Rolling-origin backtest report, calibrated intervals, model decision"],
  ];
  days.forEach(([d, t, col, mods, mix, deliv], i) => {
    const x = 0.62 + i * 4.13;
    L.card(s, x, y, 3.85, 4.62, C.paperAlt);
    s.addShape("roundRect", { x, y, w: 3.85, h: 0.92, rectRadius: 0.06,
      fill: { color: col }, line: { width: 0 } });
    s.addText(d, { x: x + 0.28, y: y + 0.1, w: 3.3, h: 0.3, isTextBox: true, fontFace: F.body,
      fontSize: 10.5, bold: true, color: C.gold, margin: 0, charSpacing: 2 });
    s.addText(t, { x: x + 0.28, y: y + 0.38, w: 3.3, h: 0.45, isTextBox: true, fontFace: F.head,
      fontSize: 19, bold: true, color: C.paper, margin: 0 });
    s.addText(mods, { x: x + 0.28, y: y + 1.12, w: 3.3, h: 1.35, isTextBox: true,
      fontFace: F.body, fontSize: 12.5, color: C.ink, margin: 0, lineSpacing: 19 });
    s.addText(mix, { x: x + 0.28, y: y + 2.55, w: 3.3, h: 0.3, isTextBox: true,
      fontFace: F.body, fontSize: 11, bold: true, color: col, margin: 0 });
    s.addText("END OF DAY", { x: x + 0.28, y: y + 3.0, w: 3.3, h: 0.25, isTextBox: true,
      fontFace: F.body, fontSize: 9, bold: true, color: C.muted, margin: 0, charSpacing: 1.5 });
    s.addText(deliv, { x: x + 0.28, y: y + 3.25, w: 3.3, h: 1.15, isTextBox: true,
      fontFace: F.body, fontSize: 12, color: C.ink, margin: 0, lineSpacing: 17 });
  });
  L.foot(s, "Each hour = 50 minutes of instruction + 10 minutes buffer. The long break is scheduled around Dhuhr.", "SDA-DSC-212");
  s.addNotes("Point at Day 3 and say plainly: the backtest report is the deliverable and the thesis made visible. If a cohort falls behind, compress Module 6 theory — never the backtest lab.");

  // ================================================ 7. DAY 1 SECTION ========
  s = S(); L.bg(s, C.deep);
  s.addShape("ellipse", { x: 10.3, y: 4.2, w: 5.0, h: 5.0, fill: { color: C.mid },
    line: { width: 0 }, transparency: 60 });
  L.titleSlideText(s, "DAY 1 · HOURS 1–5", "Seeing the Signal",
    "Before anyone fits a model, they must see the series. Module 1 teaches what a series is made of; Module 2 teaches how to test whether a classical model may touch it.");
  [["MODULE 1", "Time-Series Structure and Decomposition", "LO1"],
   ["MODULE 2", "Stationarity and Autocorrelation", "LO1 · LO2"]].forEach(([m, t, lo], i) => {
    const yy = 5.35 + i * 0.42;
    s.addText(m, { x: 0.9, y: yy, w: 1.5, h: 0.36, isTextBox: true, fontFace: F.mono,
      fontSize: 12.5, bold: true, color: C.gold, margin: 0, valign: "middle" });
    s.addText(t, { x: 2.5, y: yy, w: 6.2, h: 0.36, isTextBox: true, fontFace: F.body,
      fontSize: 13, color: C.sky, margin: 0, valign: "middle" });
    s.addText(lo, { x: 8.8, y: yy, w: 1.5, h: 0.36, isTextBox: true, fontFace: F.mono,
      fontSize: 12, color: C.onDarkMut, margin: 0, valign: "middle" });
  });
  s.addNotes("Day 1 has no forecasting in it at all, and that is deliberate. Say so — participants who expect to fit a model in hour 2 need to know why they are not going to.");

  return pres;
};
