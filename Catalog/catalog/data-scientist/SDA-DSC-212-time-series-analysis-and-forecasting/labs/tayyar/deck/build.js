const pptxgen = require("pptxgenjs");
const fs = require("fs"), path = require("path");
const ROOT = path.resolve(__dirname, "..");
const R  = JSON.parse(fs.readFileSync(path.join(ROOT, "reference_results.json"), "utf8"));
const LK = JSON.parse(fs.readFileSync(path.join(ROOT, "leak_results.json"), "utf8"));
const IMG = f => path.join(ROOT, "figures", f);

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";               // 13.333 x 7.5
pres.author = "SDAIA Academy";
pres.company = "Saudi Data and Artificial Intelligence Authority";
pres.title = "SDA-DSC-212 — Time Series Analysis and Forecasting";
pres.subject = "Instructor training deck, 3 days / 15 hours";

require("./part1")(pres, R, IMG);
require("./part2")(pres, R, IMG);
require("./part3")(pres, R, IMG);
require("./part4")(pres, R, LK, IMG);
require("./part5")(pres, R, IMG);
require("./part6")(pres, R, IMG);
require("./part7")(pres, R, IMG);
require("./part8")(pres, R, IMG);

const out = path.join(ROOT, "SDA-DSC-212_Time_Series_Training_Deck.pptx");
pres.writeFile({ fileName: out }).then(() => console.log("wrote", out));
