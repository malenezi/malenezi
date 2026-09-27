const { P } = require("./lib.js");

module.exports = function (pres, K) {
  K.divider(pres, { eyebrow: "SIGNATURE CASE STUDY · CS-11 · 90 MINUTES", title: "The Masar National\nMobility Data Incident",
    sub: "Teams investigate the Lakehouse and reconstruct what happened. Facilitator releases evidence in six stages. Nobody is told the answer.",
    items: ["08:00 — the page", "The evidence pack, P1–P6", "The chain", "Five conclusions", "Remediation and the blameless review"],
    notes: "Run this at the start of Day 5, before Module 7. It is the emotional peak of the course and it retro-justifies every control taught on Days 3 and 4. Budget 90 minutes and do not compress it below 60." });

  K.statement(pres, { kicker: "08:00, Thursday", size: 32,
    text: "Demand-forecasting accuracy has\ndeteriorated by 18% overnight.\n\nThe BI dashboard looks completely normal.",
    sub: "Trip counts: normal. Revenue: normal. Freshness: green. Volume: green. Schema validation: passing.\nEvery quality check you built yesterday is passing right now.\n\nYou have 60 minutes. What do you look at first?",
    notes: "Read this slide out loud and then stop talking. Let the silence do the work. Take the first three suggestions from the room and write them on the board without judging them — you will return to them in the debrief." });

  K.cards(pres, { kicker: "CS-11 · evidence pack", title: "Six evidence packets, released one at a time",
    lead: "Do not hand out all six. Release the next packet only when a team asks a question it would answer.",
    cols: 3, cardH: 2.45, cards: [
      { n: "P1", h: "Model monitoring chart", t: "Hourly ETA-model MAE for 14 days. Flat, then a step change at 05:00 on 5 June. No gradual drift — a cliff.", color: P.alarm },
      { n: "P2", h: "The BI dashboard", t: "Trips per zone, revenue, utilisation, cancellations — all normal for a Thursday. This is the packet that makes teams doubt themselves.", color: P.silver },
      { n: "P3", h: "Delta commit history", t: "DESCRIBE HISTORY on bronze.gps_events and silver.vehicle_positions. Steady commits, no failures. Version 808 is the last before 05:00.", color: P.bronze },
      { n: "P4", h: "The schema diff", t: "bronze.gps_events schema at v807 versus v812. IDENTICAL — same columns, types and nullability. Nothing to report.", color: P.gold },
      { n: "P5", h: "Producer release notes", t: "Telemetry agent 2.5.0, rolled out to 62% of vehicles overnight. Bullet four: “telemetry now reported in SI base units.”", color: P.teal },
      { n: "P6", h: "Feature distributions", t: "Histograms of rolling_avg_speed_10m before and after. Not shifted — BIMODAL. Two populations, one about 3.6× lower.", color: P.alarm },
    ],
    note: "Fixture: data/fixtures/incident_speed_unit/gps_2026-06-05_v250.ndjson — the decisive query is one GROUP BY away, but teams rarely reach for it before P5." });

  K.flow(pres, { kicker: "CS-11 · the chain", title: "How a passing pipeline produced a failing model", dark: true,
    stepH: 2.5, steps: [
      { h: "1 · Producer changed", t: "Telemetry agent 2.5.0 emits speed in metres per second. The field is still called speed_kmh. The type is still double.", color: P.alarm },
      { h: "2 · Validation passed", t: "Schema enforcement compares NAMES and TYPES. Both unchanged. The batch is accepted, correctly, by a control working exactly as designed.", color: P.gold },
      { h: "3 · Silver continued", t: "Dedup, conform, gate — all pass. Range checks on speed were set wide enough to admit both populations. Every row is individually plausible.", color: P.silver },
      { h: "4 · Feature corrupted", t: "rolling_avg_speed_10m now averages two incompatible units together. The number is precise, stable, and meaningless.", color: P.bronze },
      { h: "5 · AI degraded", t: "The ETA feature distribution shifts. Predictions degrade 18%. BI never touches speed, so BI shows nothing at all.", color: P.alarm },
    ],
    note: "Notice where the failure is NOT: there is no bug, no outage, no failed job, no rejected row, no red alert. Every component did its job. The platform was operationally perfect and analytically fatal." });

  K.bullets(pres, { kicker: "CS-11 · the five conclusions", title: "What teams must reach on their own",
    rowH: 0.94, items: [
      { n: "1", h: "Schema validation cannot detect semantic change", t: "It compares names and types. A unit change is a change of MEANING inside an unchanged type. No type system you have will catch it.", color: P.alarm },
      { n: "2", h: "BI did not expose the failure because BI does not use the field", t: "Dashboards report counts and revenue. Speed appears nowhere. A green dashboard is evidence about the dashboard, not about the platform.", color: P.silver },
      { n: "3", h: "AI was disproportionately affected", t: "Models consume derived, aggregated features that silently blend populations. BI reads facts; AI reads statistics — and statistics hide the very heterogeneity that broke it.", color: P.teal },
      { n: "4", h: "Observability must include FEATURE DISTRIBUTIONS", t: "Freshness, volume and schema were all green. Only distribution drift on rolling_avg_speed_10m — segmented by producer_version — would have fired.", color: P.gold },
      { n: "5", h: "Data contracts must specify semantics and units, not merely types", t: "speed_kmh: double is not a contract. speed_kmh: double, unit=km/h, range 0–180, producer_version pinned — that is a contract.", color: P.bronze },
    ] });

  K.chart(pres, { kicker: "CS-11 · the decisive query", title: "One GROUP BY ends the investigation",
    type: pres.ChartType.bar, showValue: true, labelPos: "outEnd",
    colors: [P.teal, P.alarm],
    data: [{ name: "Mean speed_kmh in the same hour", labels: ["producer_version 2.4.0", "producer_version 2.5.0"], values: [35.45, 9.85] }],
    opts: { valAxisMaxVal: 45, barGapWidthPct: 120 },
    side: { h: "SELECT producer_version,\n       avg(speed_kmh)\n  FROM bronze.gps_events\n WHERE ts >= '2026-06-05'\n GROUP BY producer_version", items: [
      "3.60× — and 3.6 is what you get when kilometres per hour are read as metres per second.",
      "The ratio IS the diagnosis. Nothing else in a mobility platform produces exactly that factor.",
      "producer_version was in bronze all along, carried by the landing job as part of the payload — because bronze landed the data AS RECEIVED.",
      "This is the return on the CS-09 rule: if landing had normalised units before persistence, this evidence would not exist.",
    ] },
    takeaway: "The independent confirmation: reconcile against metered distance ÷ duration from silver.trips, which never touched the telemetry unit." });

  K.cards(pres, { kicker: "CS-11 · remediation", title: "Four controls, each with a done-test",
    cols: 4, cardH: 3.05, cards: [
      { n: "1", h: "Roll back and pin", t: "RESTORE silver.vehicle_positions and the derived features TO VERSION AS OF 808 — the last trusted commit. Pin the model to that version BEFORE restoring, so the training set stays reproducible.\n\nDone-test: the ETA MAE returns to baseline on a replayed hour.", color: P.teal },
      { n: "2", h: "Unit-aware data contract", t: "The contract declares unit, valid range and expected producer versions per field. A batch from an undeclared producer version is quarantined, not promoted.\n\nDone-test: replaying the 2.5.0 batch is now blocked at the gate.", color: P.bronze },
      { n: "3", h: "Segmented drift monitor", t: "PSI or KS on rolling_avg_speed_10m, computed per producer_version, not just in aggregate — aggregate drift on a bimodal split can look mild.\n\nDone-test: the monitor fires on the historical batch.", color: P.gold },
      { n: "4", h: "Producer-version gate", t: "An unknown producer_version is an event that requires a human decision before its data reaches silver.\n\nDone-test: a synthetic 2.6.0 batch halts promotion and raises exactly one proportionate alert.", color: P.alarm },
    ],
    note: "Close with the blameless post-incident review template in labs/case_studies/CS-11. The producer team did nothing wrong — they improved consistency and documented it. The contract was the missing artefact." });

  K.statement(pres, { kicker: "CS-11 · the sentence to leave with", size: 33,
    text: "A type says what shape a value has.\nA contract says what a value means.\n\nAI consumes meaning.",
    sub: "Every control on Days 3 and 4 protects shape. Only two things protect meaning: a contract that states units and provenance,\nand a monitor that watches the distribution of what your model actually consumes.",
    notes: "Write the last line on the whiteboard and leave it there for the rest of Day 5. Capstone teams will point at it during their demos." });
};
