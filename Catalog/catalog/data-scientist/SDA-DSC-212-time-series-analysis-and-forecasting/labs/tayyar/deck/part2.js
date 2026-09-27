const L = require("./lib"); const { C, F } = L;

module.exports = function part2(pres, R, IMG) {
  const S = () => pres.addSlide();
  let s, y;

  // ======================================================= M1 TITLE ========
  s = S(); L.bg(s, C.paper);
  L.card(s, 0, 0, 13.333, 7.5, "FFFFFF");
  s.addShape("roundRect", { x: 0.62, y: 0.9, w: 12.1, h: 5.7, rectRadius: 0.08,
    fill: { color: C.paperAlt }, line: { width: 0 } });
  s.addText("MODULE 1  ·  DAY 1, HOURS 2–3  ·  LO1", { x: 1.1, y: 1.35, w: 8, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.teal,
    charSpacing: 2.5, margin: 0 });
  s.addText("Time-Series Structure\nand Decomposition", { x: 1.1, y: 1.7, w: 7.6, h: 1.5,
    isTextBox: true, fontFace: F.head, fontSize: 34, bold: true, color: C.ink,
    margin: 0, lineSpacing: 42 });
  s.addText("Before anyone fits a model, they must see the series. Decomposition is both a diagnostic — what structure exists? — and a modelling strategy: forecast the parts, recombine.",
    { x: 1.1, y: 3.3, w: 7.4, h: 1.0, isTextBox: true, fontFace: F.body, fontSize: 14,
      color: C.muted, margin: 0, lineSpacing: 20 });
  const o1 = [["1.1", "Construct a correct, gap-free DatetimeIndex with explicit frequency and timezone"],
              ["1.2", "Distinguish trend, seasonal and remainder; choose additive vs multiplicative"],
              ["1.3", "Apply STL and classical decomposition, including multiple seasonalities"],
              ["1.4", "Resample and aggregate without introducing temporal artefacts"],
              ["1.5", "Read a decomposition to specify what a downstream model must capture"]];
  o1.forEach(([k, t], i) => {
    s.addText(k, { x: 1.1, y: 4.45 + i * 0.4, w: 0.55, h: 0.34, isTextBox: true,
      fontFace: F.body, fontSize: 11.5, bold: true, color: C.mid, margin: 0, valign: "middle" });
    s.addText(t, { x: 1.68, y: 4.45 + i * 0.4, w: 7.0, h: 0.34, isTextBox: true,
      fontFace: F.body, fontSize: 12.5, color: C.ink, margin: 0, valign: "middle" });
  });
  s.addImage({ path: IMG("D6_pipeline.png"), x: 8.85, y: 2.6, w: 3.55, h: 0.81 });
  s.addText("Where this module sits in the pipeline you will build", { x: 8.85, y: 2.25,
    w: 3.6, h: 0.3, isTextBox: true, fontFace: F.body, fontSize: 10, color: C.muted, margin: 0 });
  s.addNotes("Business relevance in one line: a demand planner who cannot separate 'sales are trending up' from 'it is simply summer' will over-order every June and blame the model. Decomposition is the shared vocabulary between the data scientist and the decision-maker.");

  // ============================================ M1: THE ADDITIVE MODEL =====
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Every series is three things at once", "M1 · THE ADDITIVE MODEL");
  L.card(s, 0.62, y, 5.75, 2.05, "0D2136");
  s.addText([
    { text: "y", options: { fontSize: 26, color: "FFFFFF", bold: true } },
    { text: "t", options: { fontSize: 14, color: "FFFFFF", subscript: true } },
    { text: "  =  ", options: { fontSize: 26, color: C.onDarkMut } },
    { text: "T", options: { fontSize: 26, color: "F08A5D", bold: true } },
    { text: "t", options: { fontSize: 14, color: "F08A5D", subscript: true } },
    { text: "  +  ", options: { fontSize: 26, color: C.onDarkMut } },
    { text: "S", options: { fontSize: 26, color: "6BCB77", bold: true } },
    { text: "t", options: { fontSize: 14, color: "6BCB77", subscript: true } },
    { text: "  +  ", options: { fontSize: 26, color: C.onDarkMut } },
    { text: "R", options: { fontSize: 26, color: "8FB8DE", bold: true } },
    { text: "t", options: { fontSize: 14, color: "8FB8DE", subscript: true } },
  ], { x: 0.95, y: y + 0.28, w: 5.1, h: 0.6, isTextBox: true, fontFace: F.head, margin: 0 });
  s.addText([
    { text: "trend", options: { color: "F08A5D", bold: true, fontSize: 12 } },
    { text: "   the long-run level\n", options: { color: C.onDarkMut, fontSize: 12, breakLine: true } },
    { text: "seasonality", options: { color: "6BCB77", bold: true, fontSize: 12 } },
    { text: "   the repeating pattern of known period\n", options: { color: C.onDarkMut, fontSize: 12, breakLine: true } },
    { text: "remainder", options: { color: "8FB8DE", bold: true, fontSize: 12 } },
    { text: "   what neither explains — where a covariate hides", options: { color: C.onDarkMut, fontSize: 12 } },
  ], { x: 0.95, y: y + 0.95, w: 5.1, h: 0.95, isTextBox: true, fontFace: F.body,
       margin: 0, lineSpacing: 18 });
  L.card(s, 0.62, y + 2.25, 5.75, 2.35, C.paperAlt);
  s.addText("Multiplicative when the swing grows with the level", { x: 0.95, y: y + 2.42,
    w: 5.1, h: 0.32, isTextBox: true, fontFace: F.body, fontSize: 12.5, bold: true,
    color: C.ink, margin: 0 });
  s.addText("y = T × S × R    ⟺    log y = log T + log S + log R", { x: 0.95, y: y + 2.78,
    w: 5.1, h: 0.32, isTextBox: true, fontFace: F.mono, fontSize: 12, color: C.mid, margin: 0 });
  s.addText("Decide on evidence, not on taste: correlate the per-cycle level with the per-cycle amplitude. On Tayyar that correlation is " +
    R.m1.transform.level_swing_corr + ", so the series is modelled multiplicatively — as log(demand).",
    { x: 0.95, y: y + 3.2, w: 5.1, h: 1.15, isTextBox: true, fontFace: F.body, fontSize: 12.5,
      color: C.ink, margin: 0, lineSpacing: 18 });
  s.addImage({ path: IMG("02_mstl_panel.png"), x: 6.7, y: y - 0.1, w: 6.02, h: 4.57 });
  s.addText("MSTL on log(demand), summer 2023 — the observed line separated into trend, the daily and weekly seasonal components, and the remainder.",
    { x: 6.7, y: y + 4.52, w: 6.02, h: 0.45, isTextBox: true, fontFace: F.body, fontSize: 9.5,
      color: C.muted, margin: 0, lineSpacing: 14 });
  L.foot(s, "Zero or negative values must be inspected before any log transform — a sensor dropout will silently produce NaN.", "M1");
  s.addNotes("Demonstrate live: plot the summer week and the winter week from the previous figure on the same axis. The amplitude difference is the whole argument for multiplicative. Then show that the level/swing correlation makes it a measurement rather than an opinion.");

  // ==================================== M1: SEASONAL STRENGTH + RESULTS ====
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Decomposition is a measurement, not a picture", "M1 · SEASONAL AND TREND STRENGTH");
  L.card(s, 0.62, y, 5.5, 1.55, "0D2136");
  s.addText("Fₛ  =  1  −  Var(R) / Var(S + R)\nFₜ  =  1  −  Var(R) / Var(T + R)",
    { x: 0.9, y: y + 0.2, w: 4.95, h: 0.6, isTextBox: true, fontFace: F.mono, fontSize: 12,
      color: "CFE3F5", margin: 0, lineSpacing: 18 });
  s.addText("Hyndman's strength measures, both in [0, 1]. Near 1 means the component dominates what a model must capture; near 0 means you can ignore it.",
    { x: 0.9, y: y + 0.82, w: 4.95, h: 0.62, isTextBox: true, fontFace: F.body, fontSize: 11,
      color: C.onDarkMut, margin: 0, lineSpacing: 15 });
  const st = [["Daily (m = 24)", R.m1.strength.seasonal_24, "The air-conditioning cycle. The dominant structure — any model that misses it is not a candidate.", C.mid],
              ["Weekly (m = 168)", R.m1.strength.seasonal_168, "The Friday–Saturday weekend dip. Real, but secondary — a calendar feature can carry it.", C.teal],
              ["Trend", R.m1.strength.trend, "Economic growth plus a step change when a large industrial customer connected.", C.gold]];
  st.forEach(([k, v, d, col], i) => {
    const yy = y + 1.8 + i * 1.05;
    L.card(s, 0.62, yy, 5.5, 0.92, C.paperAlt);
    s.addText(String(v.toFixed(2)), { x: 0.85, y: yy + 0.06, w: 1.05, h: 0.8, isTextBox: true,
      fontFace: F.head, fontSize: 30, bold: true, color: col, margin: 0, valign: "middle" });
    s.addText(k, { x: 2.0, y: yy + 0.08, w: 3.9, h: 0.3, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, bold: true, color: C.ink, margin: 0 });
    s.addText(d, { x: 2.0, y: yy + 0.36, w: 3.9, h: 0.5, isTextBox: true, fontFace: F.body,
      fontSize: 10.5, color: C.muted, margin: 0, lineSpacing: 13.5 });
  });
  s.addImage({ path: IMG("09_calendar.png"), x: 6.45, y: y + 0.1, w: 6.3, h: 2.66 });
  s.addText("What the remainder is telling you", { x: 6.45, y: y + 2.95, w: 6.3, h: 0.32,
    isTextBox: true, fontFace: F.body, fontSize: 12.5, bold: true, color: C.ink, margin: 0 });
  L.bullets(s, [
    "The evening peak shifts later through Ramadan — a fasting-and-Iftar pattern no fixed 24-hour seasonal shape can absorb",
    "Eid produces a deep multi-day trough that looks, to a naive model, exactly like a weekend that will not end",
    "A summer heatwave shows up as remainder, not seasonality — that is the signature of a missing covariate: temperature",
  ], 6.45, y + 3.3, 6.3, 1.6, { size: 12.5 });
  s.addNotes("The card-sort activity fits here (10 min): give pairs cards reading temperature, hour-of-day, Ramadan, economic growth, sensor noise, and have them sort into seasonal component / trend / exogenous covariate / remainder. The argument about temperature is the productive one.");

  // ============================================== M1: THE asfreq LESSON ====
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "The one line that turns a silent gap into a visible one", "M1 · INDEXING, FREQUENCY AND GAPS");
  L.code(s, [
    "df = pd.read_csv(path, parse_dates=[\"timestamp\"])",
    "df = df.drop_duplicates(subset=\"timestamp\", keep=\"last\")   # 19 duplicates",
    "df = df.sort_values(\"timestamp\").set_index(\"timestamp\")",
    "df.index = df.index.tz_localize(\"Asia/Riyadh\",",
    "                  ambiguous=\"infer\", nonexistent=\"shift_forward\")",
    { t: "df = df.asfreq(\"h\")        # <- the line that reveals the gaps", c: "F2C14E", b: true },
    "",
    "df.loc[df[\"demand_mw\"] == 0, \"demand_mw\"] = pd.NA   # sensor dropouts",
    "assert df.index.is_monotonic_increasing and df.index.is_unique",
    { t: "assert df.index.freq is not None    # frequency must be DECLARED", c: "6BCB77" },
  ], 0.62, y, 7.4, 0, { size: 11 });
  L.card(s, 8.25, y, 4.47, 2.9, "0D2136");
  s.addText("What the cleaned load reports", { x: 8.5, y: y + 0.18, w: 4.0, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.gold, margin: 0 });
  const rep = [["rows in the raw file", R.m1.rows_raw.toLocaleString()],
               ["rows after asfreq(\"h\")", R.m1.rows_clean.toLocaleString()],
               ["missing hours materialised", String(R.m1.missing)],
               ["longest single gap", R.m1.longest_gap_h + " hours"],
               ["short gaps interpolated", String(R.m1.imputed)]];
  rep.forEach(([k, v], i) => {
    s.addText(k, { x: 8.5, y: y + 0.62 + i * 0.4, w: 2.75, h: 0.34, isTextBox: true,
      fontFace: F.body, fontSize: 11, color: C.onDarkMut, margin: 0, valign: "middle" });
    s.addText(v, { x: 11.25, y: y + 0.62 + i * 0.4, w: 1.25, h: 0.34, isTextBox: true,
      align: "right", fontFace: F.mono, fontSize: 12, bold: true, color: "6BCB77",
      margin: 0, valign: "middle" });
  });
  L.pull(s, "The raw file contains 26,235 rows and the clean series contains 26,280. The missing hours were never in the file — absent, not null. Skip asfreq and every seasonal index downstream is quietly misaligned, and the STL seasonal shape smears.",
    0.62, y + 3.05, 12.1, 0.95, "FDF3E3");
  s.addText("Common mistakes this slide prevents", { x: 0.62, y: y + 4.18, w: 5.9, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 12.5, bold: true, color: C.ink, margin: 0 });
  L.bullets(s, [
    "Resampling with .sum() where the question needs .mean() — the trend inflates 24×",
    "Using period = 12 for the daily cycle of an hourly series (it is 24 — observations per cycle)",
    "Log-transforming a series containing a zero from a sensor dropout",
  ], 0.62, y + 4.48, 6.0, 1.15, { size: 11.5 });
  s.addText("Instructor demo", { x: 6.9, y: y + 4.15, w: 5.8, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 12.5, bold: true, color: C.bad, margin: 0 });
  L.bullets(s, [
    "Load and decompose live in under 8 minutes",
    "Deliberately SKIP asfreq once; show the seasonal shape smear on branch sim-gap",
    "Then fix it — the fix is one line, and that is the point",
  ], 6.9, y + 4.48, 5.8, 1.15, { size: 11.5, color: C.ink });
  s.addNotes("Let a pair discover the silent row loss themselves — do not pre-warn them. It is the highest-value teachable moment on Day 1. sim-gap removes 48 hours of telemetry without a marker.");

  // ================================================== M1: LAB 1 ============
  s = S(); L.bg(s, C.deep);
  s.addText("HANDS-ON LAB 1  ·  50 MINUTES  ·  PAIRS", { x: 0.62, y: 0.55, w: 8, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 11.5, bold: true, color: C.gold,
    charSpacing: 2.5, margin: 0 });
  s.addText("Load, index and decompose the Tayyar series", { x: 0.62, y: 0.9, w: 9.5, h: 0.65,
    isTextBox: true, fontFace: F.head, fontSize: 29, bold: true, color: C.paper, margin: 0 });
  s.addText("git checkout lab1-start", { x: 10.3, y: 0.95, w: 2.4, h: 0.45, isTextBox: true,
    fontFace: F.mono, fontSize: 11, color: "6BCB77", align: "right", margin: 0, valign: "middle" });
  const t1 = [["5", "Load the raw CSV. Confirm the duplicate and out-of-order timestamps. Note the row count BEFORE cleaning."],
              ["10", "Implement load_demand: de-duplicate, sort, localise to Asia/Riyadh, asfreq(\"h\"). Report gap rows and the longest gap."],
              ["10", "Impute gaps ≤ 3 h by time interpolation; flag longer gaps. Plot one summer week and one winter week; describe each in a sentence."],
              ["10", "Decide additive vs multiplicative with additive_or_multiplicative. Justify from the amplitude plot. Log-transform if multiplicative."],
              ["10", "Run MSTL for daily + weekly seasonality. Compute seasonal_strength for each. Produce the four-panel figure."],
              ["5", "Write three bullets in FINDINGS.md: dominant seasonality, trend direction, remainder behaviour. Commit."]];
  t1.forEach(([m, t], i) => {
    const yy = 1.85 + i * 0.72;
    L.circle(s, 0.62, yy + 0.06, 0.48, i < 2 ? C.mid : C.teal, m);
    s.addText(t, { x: 1.3, y: yy, w: 6.5, h: 0.62, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, color: C.onDark, margin: 0, valign: "middle", lineSpacing: 16 });
  });
  L.code(s, [
    "$ python -m tayyar.analysis.run_decompose",
    "",
    { t: "Loaded 26,280 hourly rows | 71 missing hours materialised", c: "CFE3F5" },
    { t: "        (longest gap: 5h)", c: "CFE3F5" },
    { t: "Imputed 66 short gaps; 1 long gap (5h) flagged", c: "CFE3F5" },
    { t: "Transform: multiplicative (level/swing corr = 0.94)", c: "F2C14E" },
    { t: "        -> modelling log(demand)", c: "F2C14E" },
    { t: "Seasonal strength  daily=0.97  weekly=0.61", c: "6BCB77" },
    { t: "Trend strength 0.97 | growth +3.4% then +5.5% YoY", c: "6BCB77" },
    "Wrote decomposition_panel.png, FINDINGS.md",
  ], 8.15, 1.85, 4.57, 0, { size: 9.5 });
  s.addText("EXPECTED OUTPUT", { x: 8.15, y: 1.5, w: 4.5, h: 0.28, isTextBox: true,
    fontFace: F.body, fontSize: 10, bold: true, color: C.gold, charSpacing: 2, margin: 0 });
  s.addText("Troubleshooting", { x: 8.15, y: 4.62, w: 4.5, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 12, bold: true, color: C.paper, margin: 0 });
  const tr = [["Index not monotonic in STL", "drop_duplicates + sort before set_index"],
              ["ValueError: freq not set", "you skipped asfreq(\"h\")"],
              ["NaNs after log transform", "a zero demand — inspect the dropout first"],
              ["Seasonal component looks flat", "wrong period: hourly daily cycle = 24, not 12"]];
  tr.forEach(([a, b], i) => {
    s.addText(a, { x: 8.15, y: 4.95 + i * 0.42, w: 2.3, h: 0.4, isTextBox: true,
      fontFace: F.body, fontSize: 9.5, color: "F2A8A8", margin: 0, valign: "middle", lineSpacing: 12 });
    s.addText(b, { x: 10.5, y: 4.95 + i * 0.42, w: 2.25, h: 0.4, isTextBox: true,
      fontFace: F.body, fontSize: 9.5, color: "9DD9A8", margin: 0, valign: "middle", lineSpacing: 12 });
  });
  s.addText("Fast finishers: overlay the annual seasonal shape for 2021 against 2023 and observe the deepening summer peak — the motivation for STL's evolving seasonality.",
    { x: 0.62, y: 6.35, w: 7.2, h: 0.6, isTextBox: true, fontFace: F.body, fontSize: 11,
      italic: true, color: C.sky, margin: 0, lineSpacing: 15 });
  s.addNotes("Circulate. The pairs who skip task 1 and go straight to the clean loader are the ones who will not understand why asfreq matters — let them hit it, then ask them to count their rows.");

  // ============================================ M1 CASE + CHECKPOINT ======
  s = S(); L.bg(s, C.paper);
  y = L.head(s, "Demand planning at a national grid operator", "M1 · CASE STUDY  ·  FACILITATE, DON'T LECTURE");
  L.card(s, 0.62, y, 6.05, 4.55, C.paperAlt);
  s.addText("The situation", { x: 0.9, y: y + 0.2, w: 5.5, h: 0.32, isTextBox: true,
    fontFace: F.body, fontSize: 12.5, bold: true, color: C.mid, margin: 0 });
  s.addText("“Shabakah”, the operations-planning unit of a national grid operator, must publish a day-ahead load forecast every afternoon. Reserve margins — how much spare generation to keep spinning — are sized off that forecast.",
    { x: 0.9, y: y + 0.55, w: 5.5, h: 1.0, isTextBox: true, fontFace: F.body, fontSize: 12.5,
      color: C.ink, margin: 0, lineSpacing: 17 });
  L.card(s, 0.9, y + 1.65, 5.5, 0.95, "FDF3E3");
  s.addText("A 1% day-ahead error on a 55,000 MW peak is about 550 MW — a mid-size gas turbine held in reserve for nothing, or missing when needed.",
    { x: 1.12, y: y + 1.65, w: 5.06, h: 0.95, isTextBox: true, valign: "middle",
      fontFace: F.head, fontSize: 12.5, italic: true, color: C.warn, margin: 0, lineSpacing: 17 });
  s.addText("Constraints that shape every later decision", { x: 0.9, y: y + 2.78, w: 5.5, h: 0.3,
    isTextBox: true, fontFace: F.body, fontSize: 12.5, bold: true, color: C.mid, margin: 0 });
  L.bullets(s, [
    "Hourly telemetry with occasional sensor gaps",
    "A strict afternoon publication deadline — the pipeline must run in minutes",
    "The forecast must be explainable to control-room engineers who distrust black boxes",
    "Friday–Saturday weekend and Hijri holidays handled correctly",
  ], 0.9, y + 3.12, 5.5, 1.35, { size: 12 });
  s.addText("Discussion questions", { x: 7.0, y, w: 5.7, h: 0.34, isTextBox: true,
    fontFace: F.body, fontSize: 13, bold: true, color: C.ink, margin: 0 });
  const dq = ["Why might daily-max and daily-mean forecasts need different models?",
              "Which structure should be a model component, and which an exogenous covariate?",
              "How would you detect that this year's summer seasonality is deepening rather than a one-off heatwave?",
              "What is the cost asymmetry of over- versus under-forecasting here — and how should it shape evaluation?"];
  dq.forEach((q, i) => {
    const yy = y + 0.42 + i * 1.02;
    L.circle(s, 7.0, yy + 0.08, 0.4, C.deep, String(i + 1));
    s.addText(q, { x: 7.58, y: yy, w: 5.14, h: 0.9, isTextBox: true, fontFace: F.body,
      fontSize: 12.5, color: C.ink, margin: 0, valign: "top", lineSpacing: 17 });
  });
  L.card(s, 7.0, y + 4.35, 5.72, 0.85, "E7EFF7");
  s.addText("Checkpoint before Module 2: every pair should hold a tz-aware hourly series with a declared frequency, a documented gap policy, and an MSTL panel with reported strengths.",
    { x: 7.24, y: y + 4.35, w: 5.24, h: 0.85, isTextBox: true, valign: "middle",
      fontFace: F.body, fontSize: 11.5, color: C.deep, margin: 0, lineSpacing: 15.5 });
  s.addNotes("Question 4 is the one to protect time for — it plants Module 6. Under-forecasting risks load-shedding, a headline; over-forecasting burns fuel, merely expensive. Symmetric MAE does not know that.");

  return pres;
};
