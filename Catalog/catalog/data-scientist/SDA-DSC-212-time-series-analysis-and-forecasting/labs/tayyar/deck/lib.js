const { C, F, W, H } = require("./theme");

// ---------------------------------------------------------------- primitives
function bg(slide, color) { slide.background = { color }; }

function titleSlideText(s, kicker, title, sub) {
  if (kicker) s.addText(kicker, { x: 0.9, y: 1.55, w: 11.5, h: 0.35, isTextBox: true,
    fontFace: F.body, fontSize: 13, color: C.gold, bold: true, charSpacing: 3 });
  s.addText(title, { x: 0.9, y: 1.95, w: 11.5, h: 1.9, isTextBox: true,
    fontFace: F.head, fontSize: 44, bold: true, color: C.paper, lineSpacing: 50 });
  if (sub) s.addText(sub, { x: 0.9, y: 3.95, w: 10.6, h: 1.2, isTextBox: true,
    fontFace: F.body, fontSize: 16, color: C.onDarkMut, lineSpacing: 24 });
}

// Standard light content slide: eyebrow + title, returns the content top (y).
function head(s, title, eyebrow, opts = {}) {
  const y = opts.y ?? 0.42;
  if (eyebrow) s.addText(eyebrow, { x: 0.62, y, w: 12.1, h: 0.28, isTextBox: true,
    fontFace: F.body, fontSize: 11.5, bold: true, color: C.teal, charSpacing: 2.5, margin: 0 });
  s.addText(title, { x: 0.62, y: y + (eyebrow ? 0.3 : 0), w: 12.1, h: 0.72, isTextBox: true,
    fontFace: F.head, fontSize: opts.size ?? 30, bold: true, color: C.ink, margin: 0 });
  return y + (eyebrow ? 0.3 : 0) + (opts.gap ?? 0.86);
}

function foot(s, left, right) {
  if (left) s.addText(left, { x: 0.62, y: 6.98, w: 8.5, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 9.5, color: C.muted, margin: 0 });
  if (right) s.addText(right, { x: 9.5, y: 6.98, w: 3.2, h: 0.3, isTextBox: true,
    fontFace: F.body, fontSize: 9.5, color: C.muted, align: "right", margin: 0 });
}

// numbered / iconic circle
function circle(s, x, y, d, fill, label, labelColor) {
  s.addShape("ellipse", { x, y, w: d, h: d, fill: { color: fill },
    line: { color: fill, width: 0 } });
  s.addText(label, { x, y, w: d, h: d, isTextBox: true, align: "center",
    valign: "middle", fontFace: F.body, fontSize: d > 0.5 ? 15 : 11, bold: true,
    color: labelColor || C.paper, margin: 0 });
}

// A tinted card. No edge stripes anywhere in this deck.
function card(s, x, y, w, h, fill) {
  s.addShape("roundRect", { x, y, w, h, rectRadius: 0.06,
    fill: { color: fill || C.paperAlt }, line: { color: fill || C.paperAlt, width: 0 } });
}

// bullet list helper
function bullets(s, items, x, y, w, h, opts = {}) {
  const runs = items.map((t, i) => {
    const o = { text: typeof t === "string" ? t : t.text, options: {
      bullet: { indent: 14 }, breakLine: i !== items.length - 1,
      paraSpaceAfter: opts.space ?? 7,
      fontSize: (typeof t === "object" && t.size) || opts.size || 14.5,
      color: (typeof t === "object" && t.color) || opts.color || C.ink,
      bold: typeof t === "object" && !!t.bold,
      indentLevel: (typeof t === "object" && t.lvl) || 0 } };
    return o;
  });
  s.addText(runs, { x, y, w, h, isTextBox: true, fontFace: F.body,
    valign: "top", margin: 0 });
}

// key/value "stat" callout
function stat(s, x, y, w, value, label, color) {
  s.addText(value, { x, y, w, h: 0.86, isTextBox: true, fontFace: F.head,
    fontSize: 40, bold: true, color: color || C.mid, margin: 0 });
  s.addText(label, { x, y: y + 0.84, w, h: 0.62, isTextBox: true, fontFace: F.body,
    fontSize: 11.5, color: C.muted, margin: 0, lineSpacing: 14 });
}

// table with the deck's house style
function table(s, rows, x, y, w, opts = {}) {
  const colW = opts.colW;
  s.addTable(rows, {
    x, y, w, colW,
    fontFace: F.body, fontSize: opts.size ?? 12, color: C.ink,
    border: { type: "solid", pt: 0.75, color: "D8E0E8" },
    fill: { color: C.paper },
    rowH: opts.rowH ?? 0.34, valign: "middle",
    margin: [4, 7, 4, 7],
    autoPage: false,
  });
}

function hrow(cells, fill) {
  return cells.map(t => ({ text: t, options: { bold: true, color: "FFFFFF",
    fill: { color: fill || C.deep }, fontSize: 11.5 } }));
}
function crow(cells, opts = {}) {
  return cells.map((t, i) => ({ text: String(t), options: {
    fontSize: opts.size ?? 11.5, bold: !!(opts.boldCols || []).includes(i),
    color: opts.color || C.ink, fill: { color: opts.fill || "FFFFFF" } } }));
}

// code block, monospaced on a dark card.
// The box height is DERIVED from the line count so text can never overflow it.
function code(s, lines, x, y, w, h, opts = {}) {
  const fs = opts.size ?? 11;
  const ls = fs * 1.42;                       // points per line
  // Count WRAPPED lines: a monospace glyph is ~0.60 em wide.
  const cpl = Math.max(8, Math.floor((w - 0.40) / (fs * 0.60 / 72)));
  const nWrapped = lines.reduce((n, l) => {
    const t = typeof l === "object" ? l.t : l;
    return n + Math.max(1, Math.ceil(t.length / cpl));
  }, 0);
  const need = (nWrapped * fs * 1.50) / 72 + 0.30;
  const H = Math.max(h || 0, need);
  s.addShape("roundRect", { x, y, w, h: H, rectRadius: 0.05,
    fill: { color: opts.dark || "0D2136" }, line: { color: "0D2136", width: 0 } });
  const runs = lines.map((l, i) => {
    const hi = typeof l === "object";
    return { text: hi ? l.t : l, options: {
      breakLine: i !== lines.length - 1, fontSize: fs,
      color: hi ? (l.c || C.gold) : "CFE3F5", bold: hi && !!l.b } };
  });
  s.addText(runs, { x: x + 0.18, y: y + 0.13, w: w - 0.34, h: H - 0.26,
    isTextBox: true, fontFace: F.mono, valign: "top", margin: 0, lineSpacing: ls });
  return y + H;                                // caller can stack below
}

// how tall a code block WILL be, without drawing it
code.height = (n, size = 11) => (n * size * 1.50) / 72 + 0.30;

// a "principle" pull-quote band on a light slide
function pull(s, text, x, y, w, h, color) {
  card(s, x, y, w, h, color || "E7EFF7");
  s.addText(text, { x: x + 0.3, y, w: w - 0.6, h, isTextBox: true, valign: "middle",
    fontFace: F.head, fontSize: 16, italic: true, color: C.deep, margin: 0, lineSpacing: 22 });
}

module.exports = { bg, head, foot, circle, card, bullets, stat, table, hrow, crow,
                   code, pull, titleSlideText, C, F, W, H };
