/*
 * Renderer for the SDA-AIE-311 "Agentic AI Systems Engineering" instructor deck.
 * Consumes deck/content/*.json (ordered) and writes one .pptx.
 *
 *   node render.js content/*.json -o out/deck.pptx
 *
 * Every slide type is declarative; content authors never touch layout.
 */
const PptxGenJS = require('pptxgenjs');
const fs = require('fs');
const path = require('path');
const { C, F, G } = require('./theme');

// ---------------------------------------------------------------- utilities
const txt = (s) => (s === undefined || s === null ? '' : String(s));
const clamp = (n, lo, hi) => Math.max(lo, Math.min(hi, n));

function fit(items, { base, min, per }) {
  // shrink type as content grows, never below `min`
  return clamp(base - Math.max(0, items - per) * 1.05, min, base);
}

const WARN = [];
function warn(msg) { WARN.push(msg); }

// ------------------------------------------------------------------ chrome
function newSlide(pres, dark) {
  const s = pres.addSlide();
  s.background = { color: dark ? C.ink : C.bg };
  return s;
}

function footer(s, ctx, dark) {
  const col = dark ? '6E8F8C' : C.muted;
  s.addText(txt(ctx.footLeft || 'SDA-AIE-311 · Agentic AI Systems Engineering · SDAIA Academy'), {
    x: G.ml, y: G.footY, w: 8.2, h: 0.3, isTextBox: true,
    fontFace: F.sans, fontSize: 9, color: col, align: 'left', margin: 0,
  });
  s.addText(txt(ctx.pageLabel || ''), {
    x: G.W - G.mr - 3.2, y: G.footY, w: 3.2, h: 0.3, isTextBox: true,
    fontFace: F.sans, fontSize: 9, color: col, align: 'right', margin: 0,
  });
}

// module chip — the repeated motif, top right of every content slide
function chip(s, label, dark) {
  if (!label) return;
  s.addShape('roundRect', {
    x: G.W - G.mr - 1.12, y: G.titleY - 0.04, w: 1.12, h: 0.42,
    rectRadius: 0.08,
    fill: { color: dark ? C.inkSoft : C.seafoam },
    line: { color: dark ? '1B5C58' : C.tealLite, width: 1 },
  });
  s.addText(txt(label), {
    x: G.W - G.mr - 1.12, y: G.titleY - 0.04, w: 1.12, h: 0.42, isTextBox: true,
    fontFace: F.sans, fontSize: 11, bold: true, color: dark ? C.tealLite : C.teal,
    align: 'center', valign: 'middle', margin: 0,
  });
}

function heading(s, d, dark) {
  const hasKicker = !!d.kicker;
  if (hasKicker) {
    s.addText(txt(d.kicker).toUpperCase(), {
      x: G.ml, y: G.titleY - 0.10, w: 10.2, h: 0.26, isTextBox: true,
      fontFace: F.sans, fontSize: 10.5, bold: true, charSpacing: 1.6,
      color: dark ? C.tealLite : C.teal, margin: 0,
    });
  }
  const ty = hasKicker ? G.titleY + 0.20 : G.titleY;
  const t = txt(d.title);
  const tw = G.W - G.ml - G.mr - 1.3;
  // shrink until the title fits two lines, then lay the rule under its real height
  let size = 30;
  const cpl = (fsz) => Math.floor(tw / (0.70 * fsz / 72));  // Segoe UI Semibold avg advance
  while (size > 21 && Math.ceil(t.length / cpl(size)) > 2) size -= 1.5;
  const lines = Math.max(1, Math.ceil(t.length / cpl(size)));
  const th = lines * (size * 1.22 / 72);
  s.addText(t, {
    x: G.ml, y: ty, w: tw, h: th, isTextBox: true,
    fontFace: F.sans, fontSize: size, bold: true,
    color: dark ? C.white : C.ink, margin: 0, valign: 'top', lineSpacingMultiple: 0.98,
  });
  const ry = Math.max(hasKicker ? G.ruleY + 0.14 : G.ruleY, ty + th + 0.10);
  let after = ry + 0.30;
  if (d.title_ar) {
    // one-line titles leave room beside the rule; two-line titles push Arabic below it
    const below = lines > 1 || t.length > cpl(size) * 0.58;
    s.addText(txt(d.title_ar), {
      x: G.W - G.mr - 5.0, y: below ? ry + 0.08 : ry - 0.34, w: 5.0, h: 0.3, isTextBox: true,
      fontFace: F.sans, fontSize: 13, color: dark ? C.tealLite : C.muted,
      align: 'right', rtlMode: true, margin: 0,
    });
    if (below) after = ry + 0.46;
  }
  s.addShape('rect', { x: G.ml, y: ry, w: 0.9, h: 0.045, fill: { color: C.amber } });
  s.addShape('rect', { x: G.ml + 0.9, y: ry, w: G.W - G.ml - G.mr - 0.9, h: 0.045,
    fill: { color: dark ? '17514E' : C.line } });
  return after;
}

// numbered rounded-square badge — the motif
function badge(s, x, y, label, opts = {}) {
  const sz = opts.size || 0.30;
  s.addShape('roundRect', {
    x, y, w: sz, h: sz, rectRadius: 0.06,
    fill: { color: opts.fill || C.teal },
    line: { color: opts.fill || C.teal, width: 0 },
  });
  s.addText(txt(label), {
    x, y, w: sz, h: sz, isTextBox: true,
    fontFace: F.sans, fontSize: opts.fontSize || 11.5, bold: true,
    color: opts.color || C.white, align: 'center', valign: 'middle', margin: 0,
  });
}

function notes(s, d) { if (d.notes) s.addNotes(txt(d.notes)); }

// --------------------------------------------------------------- primitives
function bulletList(s, items, box, opts = {}) {
  const n = items.length;
  const fs = opts.fontSize || fit(n, { base: 16.5, min: 11.5, per: 5 });
  const gap = box.h / Math.max(n, 1);
  const badgeSize = clamp(gap * 0.42, 0.22, 0.32);
  items.forEach((raw, i) => {
    const item = typeof raw === 'string' ? { text: raw } : raw;
    const y = box.y + i * gap;
    const kind = item.kind || 'default';
    const fillMap = { default: C.teal, bad: C.red, good: C.green, key: C.amber };
    badge(s, box.x, y + 0.06, item.label || String(i + 1), {
      size: badgeSize, fill: fillMap[kind] || C.teal,
      fontSize: clamp(badgeSize * 36, 8, 12),
      color: kind === 'key' ? C.ink : C.white,
    });
    const tx = box.x + badgeSize + 0.20;
    const parts = [];
    if (item.lead) parts.push({ text: txt(item.lead) + '  ', options: { bold: true, color: opts.dark ? C.white : C.ink } });
    parts.push({ text: txt(item.text), options: { color: opts.dark ? 'CFE0DE' : C.body } });
    s.addText(parts, {
      x: tx, y, w: box.w - (badgeSize + 0.20), h: gap - 0.04, isTextBox: true,
      fontFace: F.sans, fontSize: fs, margin: 0, valign: 'top', lineSpacingMultiple: 1.02,
    });
    if (txt(item.text).length > 210) warn(`long bullet (${txt(item.text).length} chars): ${txt(item.text).slice(0, 50)}…`);
  });
}

function panel(s, box, opts = {}) {
  s.addShape('roundRect', {
    x: box.x, y: box.y, w: box.w, h: box.h, rectRadius: 0.04,
    fill: { color: opts.fill || C.card },
    line: { color: opts.line || C.line, width: 1 },
  });
}

function panelTitle(s, box, title, color) {
  s.addShape('rect', { x: box.x, y: box.y, w: box.w, h: 0.44, fill: { color: color || C.teal } });
  s.addText(txt(title), {
    x: box.x + 0.16, y: box.y, w: box.w - 0.32, h: 0.44, isTextBox: true,
    fontFace: F.sans, fontSize: 12.5, bold: true, color: C.white, valign: 'middle', margin: 0,
  });
}

// ------------------------------------------------------------- slide types
const R = {};

R.title = (pres, d, ctx) => {
  const s = newSlide(pres, true);
  s.addShape('rect', { x: 0, y: 0, w: 0.22, h: G.H, fill: { color: C.teal } });
  s.addShape('roundRect', { x: 9.4, y: 1.05, w: 3.4, h: 3.4, rectRadius: 0.2,
    fill: { color: C.inkSoft }, line: { color: '1B5C58', width: 1 } });
  ['reason', 'act', 'observe', 'decide'].forEach((lab, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    badge(s, 9.78 + col * 1.62, 1.45 + row * 1.42, String(i + 1), { size: 0.34, fill: i === 3 ? C.amber : C.teal, color: i === 3 ? C.ink : C.white });
    s.addText(lab, { x: 9.78 + col * 1.62, y: 1.85 + row * 1.42, w: 1.5, h: 0.3, isTextBox: true,
      fontFace: F.sans, fontSize: 11, color: C.tealLite, margin: 0 });
  });
  s.addText(txt(d.eyebrow || 'SDAIA Academy · Capacity Building Sector'), {
    x: 0.8, y: 1.25, w: 8.2, h: 0.3, isTextBox: true, fontFace: F.sans, fontSize: 12,
    bold: true, charSpacing: 1.6, color: C.tealLite, margin: 0 });
  s.addText(txt(d.title), {
    x: 0.8, y: 1.72, w: 8.4, h: 1.5, isTextBox: true, fontFace: F.sans, fontSize: 44,
    bold: true, color: C.white, margin: 0, lineSpacingMultiple: 0.95 });
  s.addText(txt(d.title_ar), {
    x: 0.8, y: 3.22, w: 8.4, h: 0.6, isTextBox: true, fontFace: F.sans, fontSize: 26,
    color: C.tealLite, margin: 0, rtlMode: true, align: 'left' });
  s.addShape('rect', { x: 0.8, y: 4.02, w: 1.3, h: 0.05, fill: { color: C.amber } });
  s.addText(txt(d.subtitle), {
    x: 0.8, y: 4.28, w: 8.2, h: 0.8, isTextBox: true, fontFace: F.sans, fontSize: 15,
    color: 'AFC9C6', margin: 0, lineSpacingMultiple: 1.1 });
  (d.meta || []).forEach((m, i) => {
    s.addText([{ text: txt(m.k).toUpperCase() + '\n', options: { fontSize: 9, color: '7EA5A2', bold: true, charSpacing: 1.2 } },
               { text: txt(m.v), options: { fontSize: 13, color: C.white, bold: true } }], {
      x: 0.8 + i * 2.12, y: 5.55, w: 2.05, h: 0.72, isTextBox: true, fontFace: F.sans, margin: 0 });
  });
  notes(s, d);
  return s;
};

R.section = (pres, d, ctx) => {
  const s = newSlide(pres, true);
  s.addShape('rect', { x: 0, y: 0, w: 0.22, h: G.H, fill: { color: C.amber } });
  s.addText(txt(d.kicker || ''), {
    x: 0.9, y: 2.0, w: 9.5, h: 0.34, isTextBox: true, fontFace: F.sans, fontSize: 12.5,
    bold: true, charSpacing: 1.8, color: C.tealLite, margin: 0 });
  const bigT = txt(d.big || '');
  const bigSize = bigT.length <= 1 ? 112 : bigT.length === 2 ? 76 : bigT.length === 3 ? 58 : 44;
  s.addText(bigT, {
    x: 9.55, y: 1.55, w: 3.2, h: 2.2, isTextBox: true, fontFace: F.sans, fontSize: bigSize,
    bold: true, color: C.inkSoft, align: 'right', margin: 0 });
  s.addText(txt(d.title), {
    x: 0.9, y: 2.42, w: 9.2, h: 1.2, isTextBox: true, fontFace: F.sans, fontSize: 38,
    bold: true, color: C.white, margin: 0, lineSpacingMultiple: 0.98 });
  if (d.title_ar) s.addText(txt(d.title_ar), {
    x: 0.9, y: 3.62, w: 9.2, h: 0.5, isTextBox: true, fontFace: F.sans, fontSize: 20,
    color: C.tealLite, margin: 0, rtlMode: true, align: 'left' });
  s.addShape('rect', { x: 0.9, y: 4.28, w: 1.3, h: 0.05, fill: { color: C.amber } });
  if (d.subtitle) s.addText(txt(d.subtitle), {
    x: 0.9, y: 4.52, w: 8.6, h: 0.9, isTextBox: true, fontFace: F.sans, fontSize: 15,
    color: 'AFC9C6', margin: 0, lineSpacingMultiple: 1.12 });
  (d.items || []).forEach((it, i) => {
    badge(s, 0.9 + i * 3.0, 5.72, String(i + 1), { size: 0.28, fill: C.teal });
    s.addText(txt(it), { x: 1.26 + i * 3.0, y: 5.70, w: 2.6, h: 0.6, isTextBox: true,
      fontFace: F.sans, fontSize: 11.5, color: 'CFE0DE', margin: 0 });
  });
  notes(s, d);
  return s;
};

R.bullets = (pres, d, ctx) => {
  const s = newSlide(pres, false);
  const y0 = heading(s, d, false);
  chip(s, d.module, false);
  const hasAside = !!(d.aside && d.aside.body);
  const w = hasAside ? 7.9 : G.W - G.ml - G.mr;
  if (d.intro) {
    s.addText(txt(d.intro), { x: G.ml, y: y0, w, h: 0.52, isTextBox: true,
      fontFace: F.sans, fontSize: 14, italic: true, color: C.muted, margin: 0 });
  }
  const by = y0 + (d.intro ? 0.62 : 0.08);
  bulletList(s, d.bullets || [], { x: G.ml, y: by, w, h: G.footY - by - 0.22 });
  if (hasAside) {
    const ax = G.ml + 8.2, aw = G.W - G.mr - ax;
    const box = { x: ax, y: y0 + 0.04, w: aw, h: G.footY - y0 - 0.30 };
    panel(s, box, { fill: d.aside.tone === 'warn' ? C.redLite : d.aside.tone === 'key' ? C.amberLite : C.seafoam,
      line: d.aside.tone === 'warn' ? 'EFC9C5' : d.aside.tone === 'key' ? 'F0DDB8' : C.tealLite });
    s.addText(txt(d.aside.title || 'Note'), {
      x: box.x + 0.22, y: box.y + 0.22, w: box.w - 0.44, h: 0.3, isTextBox: true,
      fontFace: F.sans, fontSize: 11, bold: true, charSpacing: 1.2,
      color: d.aside.tone === 'warn' ? C.red : C.teal, margin: 0 });
    s.addText(txt(d.aside.body), {
      x: box.x + 0.22, y: box.y + 0.58, w: box.w - 0.44, h: box.h - 0.8, isTextBox: true,
      fontFace: F.sans, fontSize: 12.5, color: C.body, margin: 0, lineSpacingMultiple: 1.08 });
  }
  footer(s, ctx, false); notes(s, d);
  return s;
};

R.two_col = (pres, d, ctx) => {
  const s = newSlide(pres, false);
  const y0 = heading(s, d, false);
  chip(s, d.module, false);
  const gap = 0.34, w = (G.W - G.ml - G.mr - gap) / 2, h = G.footY - y0 - 0.24;
  [[d.left, G.ml, d.left_tone], [d.right, G.ml + w + gap, d.right_tone]].forEach(([col, x, tone]) => {
    if (!col) return;
    const box = { x, y: y0 + 0.04, w, h };
    const head = tone === 'bad' ? C.red : tone === 'good' ? C.green : C.teal;
    panel(s, box, { fill: C.card, line: C.line });
    panelTitle(s, box, col.title, head);
    if (col.subtitle) s.addText(txt(col.subtitle), {
      x: box.x + 0.18, y: box.y + 0.52, w: box.w - 0.36, h: 0.34, isTextBox: true,
      fontFace: F.sans, fontSize: 11.5, italic: true, color: C.muted, margin: 0 });
    const iy = box.y + (col.subtitle ? 0.94 : 0.62);
    bulletList(s, col.items || [], { x: box.x + 0.18, y: iy, w: box.w - 0.36, h: box.y + box.h - iy - 0.18 },
      { fontSize: col.items && col.items.length > 5 ? 12.5 : 13.5 });
  });
  footer(s, ctx, false); notes(s, d);
  return s;
};

R.cards = (pres, d, ctx) => {
  const s = newSlide(pres, false);
  const y0 = heading(s, d, false);
  chip(s, d.module, false);
  const cards = d.cards || [];
  const n = cards.length;
  const cols = n <= 3 ? n : n <= 4 ? 2 : 3;
  const rows = Math.ceil(n / cols);
  const gap = 0.30;
  const w = (G.W - G.ml - G.mr - gap * (cols - 1)) / cols;
  const availH = G.footY - y0 - 0.28;
  const h = (availH - gap * (rows - 1)) / rows;
  cards.forEach((c, i) => {
    const col = i % cols, row = Math.floor(i / cols);
    const x = G.ml + col * (w + gap), y = y0 + 0.06 + row * (h + gap);
    const tone = c.tone || 'default';
    const accent = tone === 'bad' ? C.red : tone === 'good' ? C.green : tone === 'key' ? C.amber : C.teal;
    panel(s, { x, y, w, h }, { fill: C.card, line: C.line });
    s.addShape('rect', { x, y, w: 0.06, h, fill: { color: accent } });
    badge(s, x + 0.24, y + 0.24, c.label || String(i + 1), { size: 0.32, fill: accent, color: tone === 'key' ? C.ink : C.white });
    s.addText(txt(c.title), {
      x: x + 0.66, y: y + 0.22, w: w - 0.88, h: 0.4, isTextBox: true,
      fontFace: F.sans, fontSize: 14, bold: true, color: C.ink, margin: 0, valign: 'middle' });
    s.addText(txt(c.body), {
      x: x + 0.26, y: y + 0.72, w: w - 0.52, h: h - 0.92, isTextBox: true,
      fontFace: F.sans, fontSize: n > 4 ? 11.5 : 12.5, color: C.body, margin: 0, lineSpacingMultiple: 1.06 });
  });
  footer(s, ctx, false); notes(s, d);
  return s;
};

R.table = (pres, d, ctx) => {
  const s = newSlide(pres, false);
  const y0 = heading(s, d, false);
  chip(s, d.module, false);
  const headers = d.headers || [];
  const rows = d.rows || [];
  const head = headers.map((hd) => ({
    text: txt(hd), options: { bold: true, color: C.white, fill: { color: C.teal }, fontSize: 11.5, valign: 'middle' },
  }));
  const body = rows.map((r, ri) => r.map((cell, ci) => {
    const v = txt(cell);
    const tone = /^!bad /.test(v) ? 'bad' : /^!good /.test(v) ? 'good' : /^!key /.test(v) ? 'key' : null;
    const clean = v.replace(/^!(bad|good|key) /, '');
    return {
      text: clean,
      options: {
        fontSize: rows.length > 8 ? 10 : 11,
        color: tone === 'bad' ? C.red : tone === 'good' ? C.green : C.body,
        bold: ci === 0 || !!tone,
        fill: { color: ri % 2 ? 'FFFFFF' : 'EEF3F2' },
        valign: 'middle',
      },
    };
  }));
  s.addTable([head, ...body], {
    x: G.ml, y: y0 + 0.06, w: G.W - G.ml - G.mr,
    colW: d.colW || undefined,
    border: { type: 'solid', color: C.line, pt: 0.5 },
    fontFace: F.sans, autoPage: false,
    rowH: Math.min(0.46, (G.footY - y0 - 0.4) / Math.max(rows.length + 1, 1)),
  });
  if (d.footnote) s.addText(txt(d.footnote), {
    x: G.ml, y: G.footY - 0.34, w: G.W - G.ml - G.mr, h: 0.3, isTextBox: true,
    fontFace: F.sans, fontSize: 10.5, italic: true, color: C.muted, margin: 0 });
  footer(s, ctx, false); notes(s, d);
  if (rows.length > 11) warn(`table with ${rows.length} rows: ${d.title}`);
  return s;
};

R.code = (pres, d, ctx) => {
  const s = newSlide(pres, true);
  const y0 = heading(s, d, true);
  chip(s, d.module, true);
  const hasCall = (d.callouts || []).length > 0;
  const cw = hasCall ? 8.35 : G.W - G.ml - G.mr;
  const box = { x: G.ml, y: y0 + 0.04, w: cw, h: G.footY - y0 - 0.30 };
  s.addShape('roundRect', { x: box.x, y: box.y, w: box.w, h: box.h, rectRadius: 0.03,
    fill: { color: C.codeBg }, line: { color: '17514E', width: 1 } });
  if (d.filename) {
    s.addShape('rect', { x: box.x, y: box.y, w: box.w, h: 0.34, fill: { color: C.codeTint } });
    s.addText(txt(d.filename), { x: box.x + 0.18, y: box.y, w: box.w - 0.36, h: 0.34, isTextBox: true,
      fontFace: F.mono, fontSize: 10.5, color: C.tealLite, valign: 'middle', margin: 0 });
  }
  const lines = txt(d.code).replace(/\t/g, '    ').split('\n');
  const maxw = Math.max(...lines.map((l) => l.length), 1);
  const fsByLines = clamp(( box.h - 0.5) / Math.max(lines.length, 1) * 52, 8, 13.5);
  const fsByCols = clamp((box.w - 0.44) / maxw * 143, 7.5, 13.5);
  const fs = Math.min(fsByLines, fsByCols);
  const paras = lines.map((l) => {
    const isComment = /^\s*#/.test(l);
    const anti = /ANTI-PATTERN|SMELL/.test(l);
    const teach = /TEACHING POINT|<--|<-- /.test(l);
    return { text: l || ' ', options: {
      color: anti ? 'F0938C' : teach ? C.amber : isComment ? '7FA8A5' : 'DCEAE8',
      bold: anti || teach,
    } };
  });
  s.addText(paras, {
    x: box.x + 0.22, y: box.y + (d.filename ? 0.44 : 0.18), w: box.w - 0.44,
    h: box.h - (d.filename ? 0.60 : 0.34), isTextBox: true,
    fontFace: F.mono, fontSize: fs, margin: 0, lineSpacingMultiple: 0.98, valign: 'top',
  });
  if (hasCall) {
    const ax = G.ml + 8.62, aw = G.W - G.mr - ax;
    const items = d.callouts.map((c, i) => (typeof c === 'string' ? { text: c } : c));
    bulletList(s, items, { x: ax, y: box.y + 0.06, w: aw, h: box.h - 0.12 }, { dark: true, fontSize: 12 });
  }
  footer(s, ctx, true); notes(s, d);
  if (lines.length > 26) warn(`code slide with ${lines.length} lines: ${d.title}`);
  return s;
};

R.statement = (pres, d, ctx) => {
  const s = newSlide(pres, true);
  s.addShape('rect', { x: 0, y: 0, w: G.W, h: 0.12, fill: { color: C.amber } });
  if (d.kicker) s.addText(txt(d.kicker).toUpperCase(), {
    x: 1.3, y: 1.9, w: 10.7, h: 0.3, isTextBox: true, fontFace: F.sans, fontSize: 11.5,
    bold: true, charSpacing: 1.8, color: C.tealLite, margin: 0, align: 'center' });
  const t = txt(d.statement);
  s.addText(t, {
    x: 1.2, y: 2.4, w: 10.9, h: 2.2, isTextBox: true, fontFace: F.sans,
    fontSize: t.length > 150 ? 24 : t.length > 90 ? 29 : 34, bold: true,
    color: C.white, align: 'center', valign: 'middle', margin: 0, lineSpacingMultiple: 1.05 });
  if (d.statement_ar) s.addText(txt(d.statement_ar), {
    x: 1.2, y: 4.62, w: 10.9, h: 0.6, isTextBox: true, fontFace: F.sans, fontSize: 17,
    color: C.tealLite, align: 'center', rtlMode: true, margin: 0 });
  if (d.attribution) s.addText(txt(d.attribution), {
    x: 1.2, y: 5.45, w: 10.9, h: 0.4, isTextBox: true, fontFace: F.sans, fontSize: 13,
    color: '8FB3B0', align: 'center', margin: 0 });
  notes(s, d);
  return s;
};

R.flow = (pres, d, ctx) => {
  const s = newSlide(pres, false);
  const y0 = heading(s, d, false);
  chip(s, d.module, false);
  const rows = d.rows || [];
  const availH = G.footY - y0 - (d.caption ? 0.72 : 0.30);
  const n_ = Math.max(rows.length, 1);
  const rowH = Math.min(1.12, (availH - 0.28 * (n_ - 1) - 0.14) / n_);
  rows.forEach((row, ri) => {
    const steps = row.steps || row;
    const label = row.label;
    const y = y0 + 0.14 + ri * (rowH + 0.28);
    const xs = G.ml + (label ? 1.5 : 0);
    if (label) s.addText(txt(label), {
      x: G.ml, y, w: 1.36, h: rowH, isTextBox: true, fontFace: F.sans, fontSize: 11.5,
      bold: true, color: C.teal, valign: 'middle', margin: 0 });
    const n = steps.length;
    const totalW = G.W - G.mr - xs;
    const arrow = 0.34;
    const w = (totalW - arrow * (n - 1)) / n;
    steps.forEach((raw, i) => {
      const st = typeof raw === 'string' ? { text: raw } : raw;
      const tone = st.tone || 'default';
      const fill = tone === 'bad' ? C.redLite : tone === 'good' ? C.greenLite : tone === 'key' ? C.amberLite : C.card;
      const line = tone === 'bad' ? C.red : tone === 'good' ? C.green : tone === 'key' ? C.amber : C.tealLite;
      const x = xs + i * (w + arrow);
      s.addShape('roundRect', { x, y, w, h: rowH, rectRadius: 0.06,
        fill: { color: fill }, line: { color: line, width: 1.25 } });
      const body = [];
      body.push({ text: txt(st.text), options: { bold: true, fontSize: w < 1.7 ? 10.5 : 12, color: C.ink } });
      if (st.sub) body.push({ text: '\n' + txt(st.sub), options: { fontSize: 9.5, color: C.muted, bold: false } });
      s.addText(body, { x: x + 0.08, y, w: w - 0.16, h: rowH, isTextBox: true,
        fontFace: F.sans, align: 'center', valign: 'middle', margin: 0, lineSpacingMultiple: 1.0 });
      if (i < n - 1) s.addText('→', {
        x: x + w, y, w: arrow, h: rowH, isTextBox: true, fontFace: F.sans, fontSize: 16,
        color: C.teal, align: 'center', valign: 'middle', margin: 0 });
    });
  });
  if (d.caption) s.addText(txt(d.caption), {
    x: G.ml, y: G.footY - 0.42, w: G.W - G.ml - G.mr, h: 0.34, isTextBox: true,
    fontFace: F.sans, fontSize: 11.5, italic: true, color: C.muted, margin: 0 });
  footer(s, ctx, false); notes(s, d);
  return s;
};

R.lab = (pres, d, ctx) => {
  const s = newSlide(pres, false);
  const y0 = heading(s, { ...d, kicker: d.kicker || 'Hands-on lab' }, false);
  chip(s, d.module, false);
  const metaBox = { x: G.ml, y: y0 + 0.04, w: G.W - G.ml - G.mr, h: 0.72 };
  panel(s, metaBox, { fill: C.seafoam, line: C.tealLite });
  const metas = [['Objective', d.objective], ['Duration', d.duration], ['Setup', d.setup]];
  const mw = metaBox.w / 3;
  metas.forEach(([k, v], i) => {
    s.addText([{ text: txt(k).toUpperCase() + '\n', options: { fontSize: 9, bold: true, color: C.teal, charSpacing: 1.1 } },
               { text: txt(v), options: { fontSize: 11, color: C.body } }], {
      x: metaBox.x + 0.2 + i * mw, y: metaBox.y + 0.08, w: mw - 0.3, h: 0.58, isTextBox: true,
      fontFace: F.sans, margin: 0, lineSpacingMultiple: 1.02 });
  });
  const ty = metaBox.y + metaBox.h + 0.22;
  const leftW = 7.4;
  s.addText('TASKS', { x: G.ml, y: ty, w: leftW, h: 0.28, isTextBox: true,
    fontFace: F.sans, fontSize: 10, bold: true, charSpacing: 1.4, color: C.teal, margin: 0 });
  bulletList(s, (d.tasks || []).map((t, i) => (typeof t === 'string' ? { text: t } : t)),
    { x: G.ml, y: ty + 0.32, w: leftW, h: G.footY - ty - 0.62 }, { fontSize: 12.5 });
  const rx = G.ml + leftW + 0.34, rw = G.W - G.mr - rx;
  const rbox = { x: rx, y: ty, w: rw, h: G.footY - ty - 0.28 };
  panel(s, rbox, { fill: C.ink, line: C.ink });
  s.addText('EXPECTED OUTPUT', { x: rbox.x + 0.2, y: rbox.y + 0.16, w: rbox.w - 0.4, h: 0.26, isTextBox: true,
    fontFace: F.sans, fontSize: 9.5, bold: true, charSpacing: 1.3, color: C.tealLite, margin: 0 });
  s.addText(txt(d.expected), { x: rbox.x + 0.2, y: rbox.y + 0.48, w: rbox.w - 0.4, h: rbox.h - 1.16, isTextBox: true,
    fontFace: F.mono, fontSize: 10, color: 'DCEAE8', margin: 0, lineSpacingMultiple: 1.04 });
  if (d.commit) s.addText('commit: ' + txt(d.commit), {
    x: rbox.x + 0.2, y: rbox.y + rbox.h - 0.56, w: rbox.w - 0.4, h: 0.4, isTextBox: true,
    fontFace: F.mono, fontSize: 9.5, color: C.amber, margin: 0 });
  footer(s, ctx, false); notes(s, d);
  return s;
};

R.case = (pres, d, ctx) => {
  const s = newSlide(pres, false);
  const y0 = heading(s, { ...d, kicker: d.kicker || 'Case study' }, false);
  chip(s, d.module, false);
  const parts = [
    ['Scenario', d.scenario, C.teal],
    ['What went wrong', d.challenge, C.red],
    ['The fix', d.solution, C.green],
  ].filter((p) => p[1]);
  const gap = 0.28;
  const w = (G.W - G.ml - G.mr - gap * (parts.length - 1)) / parts.length;
  const h = (d.questions && d.questions.length) ? 3.0 : G.footY - y0 - 0.3;
  parts.forEach(([k, v, col], i) => {
    const x = G.ml + i * (w + gap);
    panel(s, { x, y: y0 + 0.06, w, h }, { fill: C.card, line: C.line });
    panelTitle(s, { x, y: y0 + 0.06, w, h }, k, col);
    s.addText(txt(v), { x: x + 0.2, y: y0 + 0.62, w: w - 0.4, h: h - 0.72, isTextBox: true,
      fontFace: F.sans, fontSize: 12, color: C.body, margin: 0, lineSpacingMultiple: 1.06 });
  });
  if (d.questions && d.questions.length) {
    const qy = y0 + 0.06 + h + 0.26;
    s.addText('DISCUSSION', { x: G.ml, y: qy, w: 3, h: 0.26, isTextBox: true,
      fontFace: F.sans, fontSize: 10, bold: true, charSpacing: 1.4, color: C.teal, margin: 0 });
    bulletList(s, d.questions.map((q) => ({ text: q })),
      { x: G.ml, y: qy + 0.3, w: G.W - G.ml - G.mr, h: G.footY - qy - 0.5 }, { fontSize: 12 });
  }
  footer(s, ctx, false); notes(s, d);
  return s;
};

R.metrics = (pres, d, ctx) => {
  const s = newSlide(pres, false);
  const y0 = heading(s, d, false);
  chip(s, d.module, false);
  const tiles = d.tiles || [];
  if (tiles.length) {
    const gap = 0.26;
    const w = (G.W - G.ml - G.mr - gap * (tiles.length - 1)) / tiles.length;
    tiles.forEach((t, i) => {
      const x = G.ml + i * (w + gap);
      panel(s, { x, y: y0 + 0.06, w, h: 1.42 }, { fill: C.card, line: C.line });
      s.addShape('rect', { x, y: y0 + 0.06, w, h: 0.06, fill: { color: t.tone === 'bad' ? C.red : t.tone === 'good' ? C.green : C.teal } });
      s.addText(txt(t.value), { x: x + 0.12, y: y0 + 0.24, w: w - 0.24, h: 0.66, isTextBox: true,
        fontFace: F.sans, fontSize: 27, bold: true, color: C.ink, align: 'center', margin: 0 });
      s.addText(txt(t.label), { x: x + 0.12, y: y0 + 0.92, w: w - 0.24, h: 0.48, isTextBox: true,
        fontFace: F.sans, fontSize: 10.5, color: C.muted, align: 'center', margin: 0, lineSpacingMultiple: 1.0 });
    });
  }
  const ty = y0 + (tiles.length ? 1.72 : 0.06);
  if (d.headers) {
    const head = d.headers.map((hd) => ({ text: txt(hd), options: { bold: true, color: C.white, fill: { color: C.teal }, fontSize: 11 } }));
    const body = (d.rows || []).map((r, ri) => r.map((c, ci) => ({
      text: txt(c).replace(/^!(bad|good|key) /, ''),
      options: { fontSize: 10.5, bold: ci === 0, color: /^!bad /.test(txt(c)) ? C.red : /^!good /.test(txt(c)) ? C.green : C.body,
        fill: { color: ri % 2 ? 'FFFFFF' : 'EEF3F2' } },
    })));
    s.addTable([head, ...body], { x: G.ml, y: ty, w: G.W - G.ml - G.mr,
      border: { type: 'solid', color: C.line, pt: 0.5 }, fontFace: F.sans,
      rowH: Math.min(0.42, (G.footY - ty - 0.3) / Math.max((d.rows || []).length + 1, 1)) });
  }
  footer(s, ctx, false); notes(s, d);
  return s;
};

R.checklist = (pres, d, ctx) => {
  const s = newSlide(pres, false);
  const y0 = heading(s, d, false);
  chip(s, d.module, false);
  const items = d.items || [];
  const cols = items.length > 7 ? 2 : 1;
  const rows = Math.ceil(items.length / cols);
  const w = (G.W - G.ml - G.mr - (cols - 1) * 0.4) / cols;
  const gap = (G.footY - y0 - 0.3) / rows;
  items.forEach((raw, i) => {
    const it = typeof raw === 'string' ? { text: raw } : raw;
    const col = Math.floor(i / rows), row = i % rows;
    const x = G.ml + col * (w + 0.4), y = y0 + 0.1 + row * gap;
    const ok = it.state !== 'no';
    s.addShape('roundRect', { x, y, w: 0.28, h: 0.28, rectRadius: 0.05,
      fill: { color: ok ? C.greenLite : C.redLite }, line: { color: ok ? C.green : C.red, width: 1 } });
    s.addText(ok ? '✓' : '✗', { x, y, w: 0.28, h: 0.28, isTextBox: true,
      fontFace: F.sans, fontSize: 12, bold: true, color: ok ? C.green : C.red, align: 'center', valign: 'middle', margin: 0 });
    s.addText([{ text: txt(it.lead ? it.lead + '  ' : ''), options: { bold: true, color: C.ink } },
               { text: txt(it.text), options: { color: C.body } }], {
      x: x + 0.42, y: y - 0.03, w: w - 0.46, h: gap - 0.04, isTextBox: true,
      fontFace: F.sans, fontSize: fit(rows, { base: 14, min: 11, per: 6 }), margin: 0 });
  });
  footer(s, ctx, false); notes(s, d);
  return s;
};

R.closing = (pres, d, ctx) => {
  const s = newSlide(pres, true);
  s.addShape('rect', { x: 0, y: 0, w: 0.22, h: G.H, fill: { color: C.amber } });
  s.addText(txt(d.title), { x: 1.0, y: 1.7, w: 11, h: 1.0, isTextBox: true,
    fontFace: F.sans, fontSize: 36, bold: true, color: C.white, margin: 0 });
  if (d.title_ar) s.addText(txt(d.title_ar), { x: 1.0, y: 2.72, w: 11, h: 0.5, isTextBox: true,
    fontFace: F.sans, fontSize: 19, color: C.tealLite, margin: 0, rtlMode: true, align: 'left' });
  (d.points || []).forEach((p, i) => {
    badge(s, 1.0, 3.62 + i * 0.62, String(i + 1), { size: 0.32, fill: C.teal });
    s.addText(txt(p), { x: 1.48, y: 3.58 + i * 0.62, w: 10.6, h: 0.56, isTextBox: true,
      fontFace: F.sans, fontSize: 14.5, color: 'CFE0DE', margin: 0 });
  });
  notes(s, d);
  return s;
};

// ------------------------------------------------------------------- build
function build(files, out) {
  const pres = new PptxGenJS();
  pres.layout = 'LAYOUT_WIDE';
  pres.author = 'SDAIA Academy';
  pres.company = 'Saudi Data and AI Authority';
  pres.title = 'Agentic AI Systems Engineering (SDA-AIE-311)';

  let count = 0;
  const ctx = {};
  for (const f of files) {
    const doc = JSON.parse(fs.readFileSync(f, 'utf8'));
    const slides = doc.slides || doc;
    for (const d of slides) {
      const fn = R[d.type];
      if (!fn) { warn(`unknown slide type "${d.type}" in ${path.basename(f)}`); continue; }
      count += 1;
      ctx.pageLabel = (d.module ? d.module + ' · ' : '') + 'Slide ' + count;
      try { fn(pres, d, ctx); }
      catch (e) { warn(`render error on slide ${count} (${d.type}, "${d.title || d.statement || ''}"): ${e.message}`); }
    }
  }
  fs.mkdirSync(path.dirname(out), { recursive: true });
  return pres.writeFile({ fileName: out }).then(() => {
    console.log(`slides: ${count}`);
    console.log(`written: ${out}`);
    if (WARN.length) {
      console.log(`\nwarnings (${WARN.length}):`);
      WARN.slice(0, 40).forEach((w) => console.log('  - ' + w));
    }
  });
}

const argv = process.argv.slice(2);
const oi = argv.indexOf('-o');
const out = oi >= 0 ? argv[oi + 1] : 'out/deck.pptx';
const files = (oi >= 0 ? argv.slice(0, oi) : argv).sort();
if (!files.length) { console.error('usage: node render.js content/*.json -o out/deck.pptx'); process.exit(1); }
build(files, out);
