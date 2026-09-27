// Design system for the SDA-AIE-311 "Agentic AI Systems Engineering" deck.
// Palette is content-informed: deep petrol + teal (operations / control systems),
// amber for "agency lives here" highlights, signal red for anti-patterns and attacks.
// Motif: rounded-square index badges (numbered tiles) repeated on every list, card and step.

const C = {
  ink:      '08312F',   // dominant dark — title, section, statement, code slides
  inkSoft:  '0E4744',
  teal:     '12706B',   // primary
  tealLite: '6FBFB5',   // secondary
  seafoam:  'D9EAE7',
  amber:    'E8A33D',   // accent — agency, highlights, "the one idea"
  amberLite:'FBF0DC',
  red:      'C4443A',   // anti-pattern / attack / failure
  redLite:  'F8E6E4',
  green:    '2F8F5B',   // pass / held
  greenLite:'E2F1E8',
  bg:       'F5F7F6',   // light slide ground
  card:     'FFFFFF',
  body:     '1A2B2A',
  muted:    '5C6E6C',
  line:     'D6DEDC',
  white:    'FFFFFF',
  codeBg:   '06282A',
  codeTint: '0C3B3D',
};

const F = {
  sans: 'Segoe UI',
  mono: 'Consolas',
};

// 13.333 x 7.5 canvas
const G = {
  W: 13.333,
  H: 7.5,
  ml: 0.62,           // left margin
  mr: 0.62,
  titleY: 0.46,
  ruleY: 1.18,
  bodyY: 1.46,
  bodyH: 5.42,
  footY: 7.02,
};

module.exports = { C, F, G };
