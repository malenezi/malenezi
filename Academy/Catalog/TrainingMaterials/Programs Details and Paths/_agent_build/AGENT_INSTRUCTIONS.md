# INSTRUCTOR_PACKAGE.md Build Instructions (SDAIA Academy)

You are building ONE comprehensive, instructor-ready training package as a single Markdown file. Match the **exact structure, depth, and tone** of the reference template:
`AI Engineer Track/Software Engineering Practices for AI Systems/INSTRUCTOR_PACKAGE.md` (≈2,500 lines).

## Absolute rules
1. **Authoritative facts only.** Cover Page, Course Description, Learning Outcomes, Topics, Tools, Assessment, Prerequisites, Duration, Stackability MUST come from the module's block in `SOURCE_REFERENCE.md`. Do NOT invent catalog facts. If a catalog field is absent, write **"Not specified"** (do not fabricate).
2. **Pedagogical content may be authored.** Technical explanations, code examples, labs, exercises, case studies, benchmarks, visuals lists, quizzes, and instructor notes are expert instructional content you write to be realistic, correct, and specific to THIS module's topics. Keep it technically accurate and current (2025-era tooling).
3. **One evolving artefact ("golden thread").** Like the template's fraud-service, invent ONE realistic project/dataset this course builds across all modules, ideally with a Saudi/SDAIA-relevant context. Reuse it in every lab and the capstone.
4. **Length & depth:** target 2,300–2,800 lines. Every module needs real code blocks (```python / ```bash / ```yaml), tables, and concrete numbers.
5. **Bilingual touches:** H1 = English title, H2 = Arabic title (from SOURCE_REFERENCE). Cover page includes Arabic Title row. Body content in English; code/identifiers in English.
6. **Module count = number of Topics** in the source block (usually 6–7). One module per topic, in order. If 7 topics, make 7 modules.

## Required file structure (in order)
```
# <English Title>
## <Arabic Title>

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page
| Field | Details |   ← table: Course Title, Arabic Title, Code, Level, Duration ("N days × 5 learning hours = **NN hours**"),
                        Audience, Prerequisites, Assessment, Stackability, Tools & Platforms

## Course Description   ← 2 paragraphs: what it is + the golden-thread artefact

## Learning Outcomes    ← numbered LO1..LOn, bold, from source outcomes

---

# Course Delivery Plan
## Day-by-Day Schedule   ← table: Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day  (rows = Days from source)
## Hour-by-Hour Breakdown
### Day N — <theme>      ← one table per day: Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab  (5 hours/day)
## Instructor Guidance Notes (Delivery Plan Level)   ← 6–8 bullets incl. golden thread, pacing, pairing, environment, language, prayer/break scheduling, assessment logistics

---

# Module N — <Title from topic>   (repeat for every topic)
## Module Overview          ← 2 short paras
## Learning Objectives (mapped)  ← bullets mapped to LOs (e.g. "→ LO2")
## Technical Content
### 1..6 numbered subsections with real explanation, principles, best practices, common mistakes, real-world example
## Code Examples            ← 2–4 substantial, correct, commented code blocks with realistic file paths
## Hands-on Lab N — <name>  ← objective, steps, starter/solution checkpoints, expected outputs, acceptance criteria
## Mini Exercises           ← 3–5 short tasks
## Case Study — <realistic titled scenario>
## Benchmarks and Evaluation ← concrete metrics/targets table
## Required Visuals and Training Assets
### Diagrams / Images / Simulations / Interactive Activities / Datasets / Demo Requirements

---

# Final Capstone Project
## Title / Project Scenario / Requirements / Architecture (target state) / Deliverables / Milestones /
## Grading Rubric (100 points) ← table / Assessment Criteria Notes for Instructors / Bonus Tasks

# Assessment Package
## Quiz Bank (20 questions) / Practical Assessments / Evaluation Criteria Summary

# Instructor Guide
## Preparation Checklist (T-minus 1 week) / Software Installation Checklist / Common Student Issues & Troubleshooting /
## Timing Recommendations / Discussion Prompts / Wrap-up
```

## Output mechanics
- Write the file to the EXACT path given in your task.
- Because the file is long, build it incrementally: `Write` the file through the Delivery Plan + Module 1, then `Edit` to append each subsequent section. This avoids truncation.
- Do NOT leave any `<!-- CONTINUE -->` markers in the final file.
- When done, report: final line count (`wc -l`) and confirm no CONTINUE marker remains.
