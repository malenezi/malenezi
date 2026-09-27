const pptxgen = require("pptxgenjs");
const K = require("./kit.js");

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";           // 13.333 x 7.5
pres.author = "SDAIA Academy";
pres.company = "Saudi Data and AI Authority";
pres.title = "SDA-DSC-214 — Modern Data Engineering for AI Systems";
pres.subject = "Instructor deck — 5 days, 8 modules, Masar Mini-Lakehouse capstone";

["c0_intro", "c1_day1", "c2_day2", "c3_day3", "c4_day4", "c5_incident", "c6_day5", "c7_close"]
  .forEach(m => require("./" + m + ".js")(pres, K));

const out = "/home/claude/SDA-DSC-214/slides/SDA-DSC-214_Modern_Data_Engineering_for_AI_Systems.pptx";
pres.writeFile({ fileName: out }).then(() => console.log("written:", out));
