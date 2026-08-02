# AthkaX Workbooks — Completion & Flag Report
**Date:** 2026-07-12 · **Scope:** 37 program workbooks in `Program Files (AthkaX)`

## What was populated (all 37 workbooks)

**نموذج التأهيل (Qualification Form):** bilingual title (row 4) + 7 multiple-choice questions per program testing *prerequisite* knowledge appropriate to each course level (based on each instructor package's Prerequisites chain; general workforce readiness for Level-0 and Foundation programs). Each question: Arabic + English text, 2 minutes, 1 mark, 4 options, exactly one correct answer (marked TRUE in columns أ–د).

**الاختبار القبلي / الاختبار البعدي (Pre-Test / Post-Test):** bilingual title + 7 multiple-choice questions per program on *core course content*. Pre- and post-test use identical items (standard practice for measuring learning gain).

**Question evidence sources:**
- 27 programs (all AIE, DSC-111→215, all FND): converted from the 20-item Quiz Banks in each course's `INSTRUCTOR_PACKAGE.md`, with the bank's answer as the correct option.
- 10 programs (DSC-311, 312, 313, 390 + all 6 Level-0): **no instructor package exists** — questions generated from each workbook's own bilingual description/objectives/topics. Review these first.

**Metadata updates (تفاصيل الحدث / معلومات الحدث):**
- العدد المستهدف = 25 (propagated from SDA-AIE-311, the only workbook that had it).
- الدورات → «يوجد» and نموذج التأهيل → «يوجد» (tabs now contain content to be reflected on the platform).

## ⚠ Not yet written — file locked

- **SDA-AIE-111 – Applied Machine Learning Foundations.xlsx** was open in Excel and could not be saved. A fully populated copy is staged; close the file and ask me to retry (or see the copy provided in chat).

## 🚩 Flagged — left empty, insufficient evidence

| Field | Location | Why flagged |
|---|---|---|
| صورة الحدث | معلومات الحدث, row 3 | Template says image is provided by email — no image in folder. |
| شروط التسجيل | معلومات الحدث, row 9 | Registration conditions are a policy decision; no source document found. |
| تواريخ/أوقات التسجيل والحدث | معلومات الحدث, rows 13–20 | Scheduling data; only SDA-AIE-311 has partial dates (reg. 25/05/2026 → 14/06/2026, entered by you; times and event dates still missing there too). |
| فريق الحدث (رئيس، مدربون، مساعدون) | فريق الحدث | Real staff names required; team must also log in to the platform first. |
| الدورات (درجة النجاح، معايير الحضور، الوزن، التواريخ) | الدورات sheet | Platform-fixed values per the sheet's own note; no evidence for pass grade/weights. |
| المجموعات (أسماء الشعب، الأعداد، التواريخ) | المجموعات | Cohort/section planning data not derivable from course materials. |
| نموذج التسجيل (أسئلة التسجيل) | نموذج التسجيل | Registration questions (residency, employment…) are policy items; تفاصيل الحدث flag left at «لايوجد». |

## 🚩 Flagged — pre-existing inconsistencies (not changed)

1. **الفئة المستهدفة = «ممارس»** in all 37 workbooks, but the cell's dropdown only allows «مبتدئ، مختص، خبير، عالم». Existing value kept; decide whether the platform accepts «ممارس» or map it (likely «مختص»).
2. **Naming mismatch:** workbook SDA-AIE-112 is titled *Deep Learning Foundations* while its source folder is *Deep Learning Essentials with PyTorch*; catalog says أسس التعلم العميق. Content was matched correctly, but titles should be unified.
3. **DSC-215** workbook is *Big Data Analytics* vs. source folder *Big Data Analytics with Spark* — same note as above.
4. **Excel lock file** `~$SDA-AIE-111 …xlsx` sits in the AI Engineer Track folder; delete it after closing Excel.
5. **الشهادة = «لايوجد»** in all workbooks while الاستبانة إلزامية للحصول على الشهادة = «لا» — consistent, but confirm no certificate is intended for accredited SDAIA programs.

## Consistency guarantees verified programmatically

37/37 files re-scanned after writing (36 written + 1 staged): every assessment sheet has 7 questions, bilingual text, valid dropdown values («اختيار من متعدد»), 4 unique options, exactly one correct answer per question, pre = post, target = 25, flags = «يوجد». Options beginning with "=" (formula-symbol questions) stored as literal text so Excel won't parse them as formulas. All original formatting, merged cells, and data validations preserved.
