// Shared design system for the SDA-DSC-214 deck.
const P = {
  ink:      "10202B",   // deep petrol slate  (dominant dark)
  ink2:     "1C333F",   // lighter slate for dark cards
  paper:    "FFFFFF",
  paper2:   "F4F6F7",   // light card ground
  rule:     "DDE3E6",
  body:     "2B3A42",
  muted:    "6B7C86",
  bronze:   "B0763A",
  silver:   "8E9AA3",
  gold:     "D4A537",
  teal:     "00A6A6",   // AI / serving accent
  alarm:    "D9503F",   // failure / incident
  onDark:   "FFFFFF",
  onDarkMut:"9FB3BE",
};
const F = { head: "Cambria", body: "Calibri", code: "Courier New" };
const W = 13.333, H = 7.5, M = 0.62;

// crude but reliable text-fit estimator (Calibri-ish metrics)
function fitFont(text, wIn, hIn, start, min) {
  const t = String(text || "");
  for (let fs = start; fs >= min; fs -= 0.5) {
    const cpl = Math.max(1, Math.floor((wIn * 72) / (fs * 0.50)));
    const lines = t.split("\n").reduce((a, seg) => a + Math.max(1, Math.ceil(seg.length / cpl)), 0);
    if (lines * (fs * 1.24) / 72 <= hIn) return fs;
  }
  return min;
}
function estLines(text, wIn, fs) {
  const cpl = Math.max(1, Math.floor((wIn * 72) / (fs * 0.50)));
  return String(text || "").split("\n").reduce((a, seg) => a + Math.max(1, Math.ceil(seg.length / cpl)), 0);
}

function medallionChip(slide, x, y, active, dark) {
  // motif: three small rounded squares = bronze / silver / gold
  const cols = [P.bronze, P.silver, P.gold];
  const names = ["B", "S", "G"];
  cols.forEach((c, i) => {
    const on = !active || active.includes(names[i]);
    slide.addShape("roundRect", {
      x: x + i * 0.22, y, w: 0.17, h: 0.17, rectRadius: 0.04,
      fill: { color: on ? c : (dark ? P.ink2 : P.rule) },
      line: { color: on ? c : (dark ? P.ink2 : P.rule), width: 0.5 },
    });
  });
}

function footer(slide, pres, left, dark) {
  slide.addText(left || "SDA-DSC-214 · Modern Data Engineering for AI Systems", {
    x: M, y: H - 0.46, w: 8.4, h: 0.28, isTextBox: true, margin: 0,
    fontFace: F.body, fontSize: 9, color: dark ? P.onDarkMut : P.muted,
  });
  slide.addText("SDAIA Academy", {
    x: W - M - 2.2, y: H - 0.46, w: 2.2, h: 0.28, isTextBox: true, margin: 0, align: "right",
    fontFace: F.body, fontSize: 9, color: dark ? P.onDarkMut : P.muted,
  });
}

// ---------- slide constructors ----------
function darkBase(pres) {
  const s = pres.addSlide();
  s.background = { color: P.ink };
  return s;
}
function lightBase(pres) {
  const s = pres.addSlide();
  s.background = { color: P.paper };
  return s;
}

function slideTitle(s, title, kicker, opts) {
  opts = opts || {};
  const dark = !!opts.dark;
  let y = 0.5;
  if (kicker) {
    s.addText(kicker.toUpperCase(), {
      x: M, y: 0.42, w: W - 2 * M - 1.2, h: 0.26, isTextBox: true, margin: 0,
      fontFace: F.body, fontSize: 10.5, bold: true, charSpacing: 1.6,
      color: opts.kickerColor || (dark ? P.gold : P.bronze),
    });
    y = 0.74;
  }
  const tw = W - 2 * M - 1.0;
  const tfs = opts.titleSize || 30;
  const tl = estLines(title, tw, tfs * 0.95);      // Cambria runs narrower than the estimator's default
  const th = opts.titleH || Math.max(0.62, tl * (tfs * 1.30) / 72 + 0.06);
  s.addText(title, {
    x: M, y, w: tw, h: th, isTextBox: true, margin: 0,
    fontFace: F.head, fontSize: tfs, bold: true,
    color: dark ? P.onDark : P.ink, valign: "top",
  });
  return y + th + 0.16;
}

module.exports = { P, F, W, H, M, fitFont, estLines, medallionChip, footer, darkBase, lightBase, slideTitle };
