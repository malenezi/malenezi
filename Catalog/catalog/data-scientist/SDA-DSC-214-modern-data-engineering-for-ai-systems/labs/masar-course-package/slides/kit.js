const { P, F, W, H, M, fitFont, estLines, medallionChip, footer, darkBase, lightBase, slideTitle } = require("./lib.js");

function leadBlock(s, o, y, dark) {
  if (!o.lead) return y;
  const fs = 13.3, w = W - 2 * M - 0.4;
  const h = Math.max(0.4, estLines(o.lead, w, fs) * (fs * 1.30) / 72);
  s.addText(o.lead, { x: M, y, w, h, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: fs, italic: true, color: dark ? P.onDarkMut : P.muted, valign: "top" });
  return y + h + 0.14;
}

function fin(s, pres, o) { medallionChip(s, W - M - 0.63, 0.44, o.chip, !!o.dark); footer(s, pres, o.foot, !!o.dark); if (o.notes) s.addNotes(o.notes); return s; }

/* Icon-ish numbered/lettered disc */
function disc(s, x, y, label, color, textColor, size) {
  const d = size || 0.42;
  s.addShape("ellipse", { x, y, w: d, h: d, fill: { color }, line: { color, width: 0 } });
  s.addText(label, { x, y: y + 0.015, w: d, h: d, isTextBox: true, margin: 0, align: "center", valign: "middle",
    fontFace: F.body, fontSize: d > 0.5 ? 15 : 12.5, bold: true, color: textColor || "FFFFFF" });
}

/* ---------- 1. bullets: header + description rows with coloured discs ---------- */
function bullets(pres, o) {
  const s = o.dark ? darkBase(pres) : lightBase(pres);
  let y = slideTitle(s, o.title, o.kicker, o);
  y = leadBlock(s, o, y, !!o.dark);
  const n = o.items.length;
  const avail = H - y - (o.note ? 1.30 : 0.80);
  const rowH = Math.min(o.rowH || 1.0, avail / n);
  o.items.forEach((it, i) => {
    const yy = y + i * rowH;
    const c = it.color || [P.bronze, P.silver, P.gold, P.teal, P.alarm, P.ink2][i % 6];
    disc(s, M, yy + 0.04, it.n || String(i + 1), c, it.tc);
    s.addText(it.h, { x: M + 0.62, y: yy, w: W - 2 * M - 0.7, h: 0.3, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: 15, bold: true, color: o.dark ? P.onDark : P.ink });
    if (it.t) { const bw = W - 2 * M - 0.7, bh = rowH - 0.32;
      s.addText(it.t, { x: M + 0.62, y: yy + 0.29, w: bw, h: bh, isTextBox: true, margin: 0,
        fontFace: F.body, fontSize: fitFont(it.t, bw, bh, 12.5, 9.5), color: o.dark ? P.onDarkMut : P.body, valign: "top" }); }
  });
  if (o.note) s.addText(o.note, { x: M, y: H - 1.10, w: W - 2 * M, h: 0.55, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 12, italic: true, color: o.dark ? P.gold : P.bronze });
  return fin(s, pres, o);
}

/* ---------- 2. cards grid ---------- */
function cards(pres, o) {
  const s = o.dark ? darkBase(pres) : lightBase(pres);
  let y = slideTitle(s, o.title, o.kicker, o);
  y = leadBlock(s, o, y, !!o.dark);
  const cols = o.cols || 3;
  const rows = Math.ceil(o.cards.length / cols);
  const gap = 0.28;
  const cw = (W - 2 * M - gap * (cols - 1)) / cols;
  const availH = H - y - (o.note ? 1.34 : 0.80);
  const maxCh = (availH - gap * (rows - 1)) / rows;
  // size cards to their content: never clip, never leave a dead band
  let needCh = 0, commonBfs = 99;
  o.cards.forEach(c => {
    const inW = cw - 0.48;
    const hfs = c.hs || 14.5;
    const hH = Math.min(2, estLines(c.h, inW * 1.10, hfs)) * (hfs * 1.26) / 72;
    const bfs = c.ts || 12;
    const bH = estLines(c.t, inW, bfs) * (bfs * 1.24) / 72;
    needCh = Math.max(needCh, 0.2 + (c.n !== undefined ? 0.54 : 0) + hH + 0.1 + bH + 0.22);
  });
  const ch = Math.max(Math.min(o.cardH || 2.3, maxCh), Math.min(needCh, maxCh));
  const gridH = rows * ch + gap * (rows - 1);
  y += Math.max(0, (availH - gridH) * 0.20);      // balance the leftover whitespace
  o.cards.forEach(c => {                          // one fitted body size for the whole row
    const inW = cw - 0.48, hfs = c.hs || 14.5;
    const hH = Math.min(2, estLines(c.h, inW * 1.10, hfs)) * (hfs * 1.26) / 72;
    const bodyH = ch - 0.2 - (c.n !== undefined ? 0.54 : 0) - hH - 0.1 - 0.18;
    commonBfs = Math.min(commonBfs, fitFont(c.t, inW, bodyH, c.ts || 12, 10));
  });
  o.cards.forEach((c, i) => {
    const r = Math.floor(i / cols), col = i % cols;
    const x = M + col * (cw + gap), yy = y + r * (ch + gap);
    const accent = c.color || [P.bronze, P.silver, P.gold, P.teal, P.alarm, P.ink2][i % 6];
    s.addShape("roundRect", { x, y: yy, w: cw, h: ch, rectRadius: 0.06,
      fill: { color: o.dark ? P.ink2 : P.paper2 }, line: { color: o.dark ? P.ink2 : P.rule, width: 1 } });
    let ty = yy + 0.2;
    if (c.n !== undefined) { disc(s, x + 0.24, ty, c.n, accent, c.tc, 0.4); ty += 0.54; }
    const inW = cw - 0.48;
    const hfs = c.hs || 14.5;
    const hLines = Math.min(2, estLines(c.h, inW * 1.10, hfs));
    const hH = hLines * (hfs * 1.26) / 72;          // fixed 1- or 2-line title zone
    s.addText(c.h, { x: x + 0.24, y: ty, w: inW, h: hH, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: hfs, bold: true, color: c.n !== undefined ? (o.dark ? P.onDark : P.ink) : accent, valign: "top" });
    const bodyY = ty + hH + 0.1;
    const bodyH = yy + ch - bodyY - 0.18;
    s.addText(c.t, { x: x + 0.24, y: bodyY, w: inW, h: bodyH, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: commonBfs,
      color: o.dark ? P.onDarkMut : P.body, valign: "top" });
  });
  if (o.note) s.addText(o.note, { x: M, y: H - 1.10, w: W - 2 * M, h: 0.55, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 12, italic: true, color: o.dark ? P.gold : P.bronze });
  return fin(s, pres, o);
}

/* ---------- 3. table ---------- */
function table(pres, o) {
  const s = o.dark ? darkBase(pres) : lightBase(pres);
  let y = slideTitle(s, o.title, o.kicker, o);
  y = leadBlock(s, o, y, !!o.dark);
  const head = o.head.map(h => ({ text: h, options: { bold: true, color: "FFFFFF", fill: { color: o.headColor || P.ink }, fontSize: o.fs || 11.5 } }));
  const rows = o.rows.map((r, ri) => r.map((c, ci) => ({
    text: String(c),
    options: {
      fontSize: o.fs || 11.5, color: P.body, bold: ci === 0 && o.boldFirst !== false,
      fill: { color: ri % 2 ? "FFFFFF" : P.paper2 },
    },
  })));
  const availT = H - y - (o.note ? 1.24 : 0.86);
  const nRows = o.rows.length + 1;
  const rh = Math.max(o.rowH || 0.32, Math.min(o.maxRowH || 1.05, (availT / nRows) - 0.04));
  s.addTable([head, ...rows], {
    x: M, y, w: W - 2 * M, colW: o.widths, border: { type: "solid", color: P.rule, pt: 0.5 },
    fontFace: F.body, valign: "middle", rowH: rh, autoPage: false,
  });
  if (o.note) s.addText(o.note, { x: M, y: H - 1.10, w: W - 2 * M, h: 0.55, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 12, italic: true, color: P.bronze });
  return fin(s, pres, o);
}

/* ---------- 4. two-column comparison ---------- */
function twoCol(pres, o) {
  const s = o.dark ? darkBase(pres) : lightBase(pres);
  let y = slideTitle(s, o.title, o.kicker, o);
  y = leadBlock(s, o, y, !!o.dark);
  const gap = 0.34, cw = (W - 2 * M - gap) / 2;
  const availC = H - y - (o.note ? 1.34 : 0.80);
  let needC = 0;
  [o.left, o.right].forEach(col => {
    const lw = cw - 0.52, fs = col.fs || 12.5;
    const head = 0.2 + 0.4 + (col.sub ? estLines(col.sub, lw, 11.5) * 0.20 : 0) + 0.3;
    needC = Math.max(needC, head + estLines(col.items.join("\n"), lw - 0.18, fs) * (fs * 1.26) / 72 + col.items.length * 0.09 + 0.28);
  });
  const ch = Math.min(availC, Math.max(needC, 3.0));
  y += Math.max(0, (availC - ch) * 0.22);
  [o.left, o.right].forEach((col, i) => {
    const x = M + i * (cw + gap);
    const accent = col.color || (i ? P.teal : P.bronze);
    s.addShape("roundRect", { x, y, w: cw, h: ch, rectRadius: 0.06,
      fill: { color: o.dark ? P.ink2 : P.paper2 }, line: { color: o.dark ? P.ink2 : P.rule, width: 1 } });
    s.addText(col.h, { x: x + 0.26, y: y + 0.2, w: cw - 0.52, h: 0.4, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: 16, bold: true, color: accent });
    if (col.sub) s.addText(col.sub, { x: x + 0.26, y: y + 0.62, w: cw - 0.52, h: 0.36, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: 11.5, italic: true, color: o.dark ? P.onDarkMut : P.muted });
    const listY = y + (col.sub ? 1.02 : 0.7);
    const lw = cw - 0.52, lh = ch - (listY - y) - 0.22;
    const joined = col.items.join("\n");
    let lfs = fitFont(joined, lw - 0.18, lh - col.items.length * 0.11, col.fs || 12.5, 9.5);
    s.addText(col.items.map((t, j) => ({ text: t, options: { bullet: true, breakLine: j !== col.items.length - 1 } })), {
      x: x + 0.26, y: listY, w: lw, h: lh, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: lfs, color: o.dark ? P.onDarkMut : P.body, paraSpaceAfter: 6, valign: "top",
    });
  });
  if (o.note) s.addText(o.note, { x: M, y: H - 1.10, w: W - 2 * M, h: 0.55, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 12, italic: true, color: o.dark ? P.gold : P.bronze });
  return fin(s, pres, o);
}

/* ---------- 5. big stats ---------- */
function stat(pres, o) {
  const s = o.dark === false ? lightBase(pres) : darkBase(pres);
  const dark = o.dark !== false;
  let y = slideTitle(s, o.title, o.kicker, Object.assign({}, o, { dark }));
  y = leadBlock(s, o, y, !!o.dark);
  const n = o.stats.length, gap = 0.3;
  const cw = (W - 2 * M - gap * (n - 1)) / n;
  const bh = Math.min(2.5, H - y - 1.15);
  o.stats.forEach((st, i) => {
    const x = M + i * (cw + gap);
    const c = st.color || [P.gold, P.teal, P.bronze, P.silver][i % 4];
    s.addShape("roundRect", { x, y, w: cw, h: bh, rectRadius: 0.06,
      fill: { color: dark ? P.ink2 : P.paper2 }, line: { color: dark ? P.ink2 : P.rule, width: 1 } });
    s.addText(st.v, { x: x + 0.16, y: y + 0.28, w: cw - 0.32, h: 1.0, isTextBox: true, margin: 0, align: "center",
      fontFace: F.head, fontSize: st.vs || 44, bold: true, color: c });
    s.addText(st.l, { x: x + 0.2, y: y + 1.32, w: cw - 0.4, h: bh - 1.42, isTextBox: true, margin: 0, align: "center",
      fontFace: F.body, fontSize: 12, color: dark ? P.onDarkMut : P.body, valign: "top" });
  });
  if (o.note) s.addText(o.note, { x: M, y: y + bh + 0.28, w: W - 2 * M, h: 0.62, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 13.5, italic: true, color: dark ? P.gold : P.bronze });
  return fin(s, pres, Object.assign({}, o, { dark }));
}

/* ---------- 6. code + commentary ---------- */
function code(pres, o) {
  const s = lightBase(pres);
  let y = slideTitle(s, o.title, o.kicker, o);
  const hasPoints = o.points && o.points.length;
  const cw = hasPoints ? (W - 2 * M) * 0.6 : W - 2 * M;
  const ch = H - y - 0.8;
  s.addShape("roundRect", { x: M, y, w: cw, h: ch, rectRadius: 0.06, fill: { color: P.ink }, line: { color: P.ink, width: 1 } });
  if (o.lang) s.addText(o.lang, { x: M + cw - 1.3, y: y + 0.1, w: 1.1, h: 0.24, isTextBox: true, margin: 0, align: "right",
    fontFace: F.code, fontSize: 9, color: P.onDarkMut });
  s.addText(o.code, { x: M + 0.22, y: y + 0.2, w: cw - 0.44, h: ch - 0.36, isTextBox: true, margin: 0,
    fontFace: F.code, fontSize: o.fs || 10, color: "E8F0F3", valign: "top", lineSpacingMultiple: 1.06 });
  if (hasPoints) {
    const px = M + cw + 0.3, pw = W - M - px;
    let py = y + 0.04;
    o.points.forEach((p, i) => {
      const c = [P.bronze, P.teal, P.gold, P.alarm][i % 4];
      disc(s, px, py, String(i + 1), c, null, 0.34);
      s.addText(p, { x: px + 0.46, y: py - 0.03, w: pw - 0.5, h: 0.9, isTextBox: true, margin: 0,
        fontFace: F.body, fontSize: 12, color: P.body, valign: "top" });
      py += Math.max(0.62, Math.min(1.0, (ch - 0.1) / o.points.length));
    });
  }
  return fin(s, pres, o);
}

/* ---------- 7. native chart ---------- */
function chart(pres, o) {
  const s = lightBase(pres);
  let y = slideTitle(s, o.title, o.kicker, o);
  const hasSide = !!o.side;
  const cw = hasSide ? (W - 2 * M) * 0.62 : W - 2 * M;
  const ch = H - y - (o.takeaway ? 1.28 : 0.85);
  const base = {
    x: M, y, w: cw, h: ch,
    showTitle: false, showLegend: !!o.legend, legendPos: "b", legendFontSize: 10,
    chartColors: o.colors || [P.bronze, P.teal, P.gold, P.silver],
    catAxisLabelColor: P.muted, valAxisLabelColor: P.muted,
    catAxisLabelFontSize: 11, valAxisLabelFontSize: 10, catAxisLabelFontFace: F.body, valAxisLabelFontFace: F.body,
    valGridLine: { color: P.rule, size: 0.75 }, catGridLine: { style: "none" },
    showValue: o.showValue !== false, dataLabelPosition: o.labelPos || "outEnd",
    dataLabelFontSize: 10, dataLabelFontFace: F.body, dataLabelColor: P.body,
    dataLabelFormatCode: o.fmt || "#,##0.##", barGapWidthPct: 55,
  };
  s.addChart(o.type, o.data, Object.assign(base, o.opts || {}));
  if (hasSide) {
    const px = M + cw + 0.32, pw = W - M - px;
    const mono = String(o.side.h).indexOf("\n") >= 0;
    const hfs = mono ? 10.5 : 14.5;
    const hh = estLines(o.side.h, pw, hfs) * (hfs * 1.30) / 72 + 0.06;
    s.addText(o.side.h, { x: px, y: y + 0.05, w: pw, h: hh, isTextBox: true, margin: 0,
      fontFace: mono ? F.code : F.body, fontSize: hfs, bold: !mono, color: P.bronze, valign: "top" });
    const ly = y + 0.05 + hh + 0.14, lh = ch - (ly - y) - 0.08;
    const joined = o.side.items.join("\n");
    s.addText(o.side.items.map((t, j) => ({ text: t, options: { bullet: true, breakLine: j !== o.side.items.length - 1 } })), {
      x: px, y: ly, w: pw, h: lh, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: fitFont(joined, pw - 0.18, lh - o.side.items.length * 0.12, 12, 9),
      color: P.body, paraSpaceAfter: 7, valign: "top" });
  }
  if (o.takeaway) s.addText(o.takeaway, { x: M, y: H - 1.12, w: W - 2 * M, h: 0.56, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 13, italic: true, color: P.bronze });
  return fin(s, pres, o);
}

/* ---------- 8. horizontal flow ---------- */
function flow(pres, o) {
  const s = o.dark ? darkBase(pres) : lightBase(pres);
  let y = slideTitle(s, o.title, o.kicker, o);
  y = leadBlock(s, o, y, !!o.dark);
  const n = o.steps.length, arrow = 0.34;
  const bw = (W - 2 * M - arrow * (n - 1)) / n;
  const availS = H - y - (o.note ? 1.45 : 0.85);
  const bh = Math.min(o.stepH || 2.6, availS);
  y += Math.max(0, (availS - bh) * 0.34);
  o.steps.forEach((st, i) => {
    const x = M + i * (bw + arrow);
    const c = st.color || [P.bronze, P.silver, P.gold, P.teal, P.alarm][i % 5];
    s.addShape("roundRect", { x, y, w: bw, h: bh, rectRadius: 0.06,
      fill: { color: o.dark ? P.ink2 : P.paper2 }, line: { color: c, width: 1.5 } });
    s.addText(st.h, { x: x + 0.18, y: y + 0.22, w: bw - 0.36, h: 0.64, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: st.hs || 13.5, bold: true, color: c, valign: "top" });
    const sw = bw - 0.36, sh = bh - 1.06;
    s.addText(st.t, { x: x + 0.18, y: y + 0.88, w: sw, h: sh, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: fitFont(st.t, sw, sh, st.ts || 11.5, 8.5), color: o.dark ? P.onDarkMut : P.body, valign: "top" });
    if (i < n - 1) s.addShape("rightArrow", { x: x + bw + 0.05, y: y + bh / 2 - 0.11, w: arrow - 0.1, h: 0.22,
      fill: { color: o.dark ? P.onDarkMut : P.silver }, line: { color: o.dark ? P.onDarkMut : P.silver, width: 0 } });
  });
  if (o.note) s.addText(o.note, { x: M, y: y + bh + 0.36, w: W - 2 * M, h: 0.68, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 13, italic: true, color: o.dark ? P.gold : P.bronze, valign: "top" });
  return fin(s, pres, o);
}

/* ---------- 9. statement / quote ---------- */
function statement(pres, o) {
  const s = darkBase(pres);
  if (o.kicker) s.addText(o.kicker.toUpperCase(), { x: M, y: 1.5, w: W - 2 * M, h: 0.3, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 11, bold: true, charSpacing: 1.8, color: P.gold });
  s.addText(o.text, { x: M, y: o.kicker ? 1.95 : 2.1, w: W - 2 * M - 0.6, h: 2.6, isTextBox: true, margin: 0,
    fontFace: F.head, fontSize: o.size || 34, bold: true, color: P.onDark, valign: "top", lineSpacingMultiple: 1.12 });
  if (o.sub) s.addText(o.sub, { x: M, y: 4.85, w: W - 2 * M - 0.6, h: 1.2, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 15, color: P.onDarkMut, valign: "top" });
  return fin(s, pres, Object.assign({}, o, { dark: true }));
}

/* ---------- 10. section divider ---------- */
function divider(pres, o) {
  const s = darkBase(pres);
  s.addText(o.eyebrow || "", { x: M, y: 1.55, w: W - 2 * M, h: 0.3, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 11.5, bold: true, charSpacing: 2.2, color: P.gold });
  s.addText(o.title, { x: M, y: 1.95, w: (W - 2 * M) * 0.55, h: 1.5, isTextBox: true, margin: 0,
    fontFace: F.head, fontSize: 40, bold: true, color: P.onDark, valign: "top" });
  if (o.sub) s.addText(o.sub, { x: M, y: 3.5, w: (W - 2 * M) * 0.55, h: 1.5, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 14, color: P.onDarkMut, valign: "top" });
  if (o.items) {
    const x = M + (W - 2 * M) * 0.6, w = (W - 2 * M) * 0.4;
    let yy = 1.98;
    o.items.forEach((it, i) => {
      const c = [P.bronze, P.silver, P.gold, P.teal, P.alarm][i % 5];
      disc(s, x, yy, String(i + 1), c, null, 0.36);
      s.addText(it, { x: x + 0.5, y: yy - 0.03, w: w - 0.5, h: 0.6, isTextBox: true, margin: 0,
        fontFace: F.body, fontSize: 13, color: P.onDark, valign: "top" });
      yy += 0.72;
    });
  }
  return fin(s, pres, Object.assign({}, o, { dark: true }));
}

/* ---------- 11. medallion spine diagram ---------- */
function medallion(pres, o) {
  const s = lightBase(pres);
  let y = slideTitle(s, o.title, o.kicker, o);
  y = leadBlock(s, o, y, !!o.dark);
  const bands = [
    { n: "BRONZE", c: P.bronze, t: o.bronze },
    { n: "SILVER", c: P.silver, t: o.silver },
    { n: "GOLD",   c: P.gold,   t: o.gold },
  ];
  const srcW = 2.0, conW = 2.0, gap = 0.22;
  const bandX = M + srcW + gap, bandW = W - 2 * M - srcW - conW - 2 * gap;
  const bh = 1.15, tot = bh * 3 + 0.2 * 2;
  // sources
  s.addShape("roundRect", { x: M, y, w: srcW, h: tot, rectRadius: 0.06, fill: { color: P.paper2 }, line: { color: P.rule, width: 1 } });
  s.addText("SOURCES", { x: M + 0.14, y: y + 0.16, w: srcW - 0.28, h: 0.26, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 10.5, bold: true, charSpacing: 1.2, color: P.muted });
  s.addText((o.sources || []).map((t, i, a) => ({ text: t, options: { bullet: true, breakLine: i !== a.length - 1 } })), {
    x: M + 0.14, y: y + 0.5, w: srcW - 0.28, h: tot - 0.66, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 11, color: P.body, paraSpaceAfter: 6, valign: "top" });
  bands.forEach((b, i) => {
    const yy = y + i * (bh + 0.2);
    s.addShape("roundRect", { x: bandX, y: yy, w: bandW, h: bh, rectRadius: 0.06,
      fill: { color: P.paper2 }, line: { color: b.c, width: 1.75 } });
    s.addText(b.n, { x: bandX + 0.2, y: yy + 0.14, w: 1.5, h: 0.32, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: 13, bold: true, charSpacing: 1.4, color: b.c });
    s.addText(b.t.tables, { x: bandX + 1.75, y: yy + 0.12, w: bandW - 1.95, h: 0.34, isTextBox: true, margin: 0,
      fontFace: F.code, fontSize: 11, color: P.ink });
    const cwd = bandW - 0.4, cht = bh - 0.6;
    s.addText(b.t.contract, { x: bandX + 0.2, y: yy + 0.5, w: cwd, h: cht, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: fitFont(b.t.contract, cwd, cht, 11.5, 8.5), color: P.body, valign: "top" });
    if (i < 2) s.addShape("downArrow", { x: bandX + bandW / 2 - 0.11, y: yy + bh + 0.005, w: 0.22, h: 0.19,
      fill: { color: P.silver }, line: { color: P.silver, width: 0 } });
  });
  // consumers
  const cx = bandX + bandW + gap;
  [{ h: "BI · operations", t: o.bi, c: P.gold }, { h: "AI · ETA & demand", t: o.ai, c: P.teal }].forEach((c, i) => {
    const yy = y + i * (tot / 2 + 0.06);
    s.addShape("roundRect", { x: cx, y: yy, w: conW, h: tot / 2 - 0.06, rectRadius: 0.06,
      fill: { color: P.ink }, line: { color: P.ink, width: 1 } });
    s.addText(c.h, { x: cx + 0.16, y: yy + 0.16, w: conW - 0.32, h: 0.3, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: 12, bold: true, color: c.c });
    s.addText(c.t, { x: cx + 0.16, y: yy + 0.5, w: conW - 0.32, h: tot / 2 - 0.66, isTextBox: true, margin: 0,
      fontFace: F.code, fontSize: 9.5, color: P.onDarkMut, valign: "top" });
  });
  if (o.note) s.addText(o.note, { x: M, y: y + tot + 0.26, w: W - 2 * M, h: 0.8, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 13, italic: true, color: P.bronze, valign: "top" });
  return fin(s, pres, o);
}

/* ---------- 12. lab brief ---------- */
function lab(pres, o) {
  const s = lightBase(pres);
  let y = slideTitle(s, o.title, o.kicker || `Hands-on Lab ${o.id}`, Object.assign({}, o, { kickerColor: P.teal }));
  const metaW = 3.5;
  const bh = H - y - 0.8;
  s.addShape("roundRect", { x: M, y, w: metaW, h: bh, rectRadius: 0.06, fill: { color: P.ink }, line: { color: P.ink, width: 1 } });
  let my = y + 0.2;
  const mw = metaW - 0.4;
  (o.meta || []).forEach(m => {
    const vh = Math.max(0.24, estLines(m[1], mw, 11.5) * (11.5 * 1.28) / 72);
    s.addText(m[0].toUpperCase(), { x: M + 0.2, y: my, w: mw, h: 0.2, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: 9, bold: true, charSpacing: 1.2, color: P.gold });
    s.addText(m[1], { x: M + 0.2, y: my + 0.2, w: mw, h: vh, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: 11.5, color: P.onDark, valign: "top" });
    my += 0.2 + vh + 0.2;
  });
  const rx = M + metaW + 0.3, rw = W - M - rx;
  s.addText("What you will do", { x: rx, y: y + 0.02, w: rw, h: 0.3, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 14, bold: true, color: P.bronze });
  const tfs0 = fitFont(o.tasks.join("\n"), rw - 0.22, bh * 0.56 - o.tasks.length * 0.1, 12.5, 9.5);
  const tH = Math.min(bh * 0.62,
    estLines(o.tasks.join("\n"), rw - 0.28, tfs0) * (tfs0 * 1.26) / 72 + o.tasks.length * 0.09 + 0.1);
  s.addText(o.tasks.map((t, i, a) => ({ text: t, options: { bullet: { type: "number" }, breakLine: i !== a.length - 1 } })), {
    x: rx, y: y + 0.4, w: rw, h: tH, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: tfs0, color: P.body, paraSpaceAfter: 6, valign: "top" });
  const ay = y + 0.4 + tH + 0.1;
  s.addText("Acceptance criteria", { x: rx, y: ay, w: rw, h: 0.3, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 14, bold: true, color: P.teal });
  const aH = bh - (ay - y) - 0.4;
  s.addText(o.accept.map((t, i, a) => ({ text: t, options: { bullet: true, breakLine: i !== a.length - 1 } })), {
    x: rx, y: ay + 0.34, w: rw, h: aH, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: fitFont(o.accept.join("\n"), rw - 0.18, aH - o.accept.length * 0.1, 12, 9),
    color: P.body, paraSpaceAfter: 5, valign: "top" });
  return fin(s, pres, o);
}

module.exports = { bullets, cards, table, twoCol, stat, code, chart, flow, statement, divider, medallion, lab, disc };
