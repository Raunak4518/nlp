# Master Project Specification: Complete NLP Study Website

You are an expert NLP educator, university-level curriculum designer, technical writer, software engineer, documentation architect, visualization designer, and exam-preparation specialist. Your task is to build a COMPLETE, EXTREMELY DETAILED, HIGH-QUALITY NLP STUDY MATERIAL WEBSITE from the two files already provided in this repository: 1. README.md 2. SYLLABUS.md

These files are the authoritative curriculum specification. IMPORTANT: DO NOT extract the syllabus from random notes. DO NOT infer the syllabus from unrelated files. DO NOT replace the syllabus with your own preferred NLP curriculum. DO NOT omit topics because they appear simple. DO NOT create shallow summaries. README.md and SYLLABUS.md define WHAT must be taught. Your job is to determine HOW deeply each item must be taught and to expand every syllabus item into rigorous study material.

The final result must function as a complete NLP examination preparation website that a student can use as their primary study resource. The student should be able to use it for:
- conceptual/theoretical questions
- mathematical questions
- numerical problems
- algorithm questions
- derivations
- implementation questions
- scratch coding questions
- practical NLP questions
- comparison questions
- viva/interview questions
- revision
- last-minute exam preparation

============================================================
PART 1 — FIRST UNDERSTAND THE INPUT FILES
============================================================
Before creating anything, carefully read:
- README.md
- SYLLABUS.md

Treat SYLLABUS.md as the authoritative list of topics. Treat README.md as the project-level specification, context, requirements, and any additional instructions.

Build an internal representation of the syllabus before writing study material.

For every syllabus item identify:
- major topic
- subtopic
- nested subtopic
- mathematical concepts
- algorithms
- formulas
- terminology
- implementation requirements
- likely numerical problems
- likely theoretical questions
- likely practical questions
- prerequisite concepts
- related concepts required to understand the topic

DO NOT modify the syllabus merely because you think another structure is better. You may reorganize it into folders and files for usability, but every syllabus item must remain represented.

============================================================
PART 2 — SYLLABUS COVERAGE IS ABSOLUTE
============================================================
EVERY item in SYLLABUS.md must appear somewhere in the generated study material. Nothing may be silently dropped.

Create a coverage mapping file: SOURCE-COVERAGE.md
It must contain a table such as:

| Syllabus Item | Major Topic Folder | Markdown File | Status |
|---|---|---|---|
| Topic X | 01-topic-x | concept.md | COMPLETE |
| Topic Y | 01-topic-x | numerical-problems.md | COMPLETE |

Every syllabus item must have a destination.

At the end of the project, perform a second coverage audit. If ANY syllabus item is missing:
1. identify it
2. create the required content
3. update SOURCE-COVERAGE.md
4. repeat the audit

Do not consider the project complete until every syllabus item is covered.

============================================================
PART 3 — FOLDER STRUCTURE
============================================================
Every MAJOR topic must have its own directory.
Every meaningful SUBTOPIC must have its own Markdown file.

Use a structure similar to:
docs/
├── index.md
├── syllabus.md
├── study-plan.md
├── exam-preparation.md
├── SOURCE-COVERAGE.md
│
├── 01-foundations/
│   ├── README.md
│   ├── introduction.md
│   ├── computational-linguistics.md
│   ├── inductive-bias.md
│   └── ...
│
├── 02-text-processing/
│   ├── README.md
│   ├── normalization.md
│   ├── tokenization.md
│   ├── sentence-segmentation.md
│   └── ...

IMPORTANT: Do not create absurdly tiny files. The goal is: HIGH GRANULARITY without RIDICULOUS FRAGMENTATION.

============================================================
PART 4 — README.md FOR EVERY MAJOR TOPIC
============================================================
Every major-topic folder MUST contain: README.md
The README should function as the landing page for that topic. It must contain:
1. What this topic is
2. Why it matters in NLP
3. What the student will learn
4. Prerequisites
5. Complete subtopic list
6. Recommended learning order
7. Mathematical difficulty
8. Implementation difficulty
9. Numerical-problem relevance
10. Exam importance
11. Common mistakes
12. Related topics
13. Links to every subtopic
14. Revision checklist
15. Implementation checklist
16. Numerical-practice checklist

============================================================
PART 5 — DEPTH REQUIREMENT FOR EVERY SUBTOPIC
============================================================
Every substantial subtopic Markdown file must be extremely well developed.
Use this structure whenever applicable:
# Topic Name
## 1. What Is It?
## 2. Intuition
## 3. Formal Definition
## 4. Why Does It Exist?
## 5. How Does It Work?
## 6. Mathematical Formulation
## 7. Worked Example
## 8. Numerical Example
## 9. Algorithm
## 10. Manual Trace
## 11. Scratch Implementation
## 12. Code Explanation
## 13. Visualization (Mermaid diagrams preferred)

============================================================
PART 6 — IMAGES & PART 7 — VISUAL EXPLANATIONS
============================================================
INCLUDE IMAGES WHEN THEY ACTUALLY IMPROVE UNDERSTANDING.
For difficult concepts, use the sequence:
TEXT → INTUITION → VISUAL → MATHEMATICS → EXAMPLE → IMPLEMENTATION

============================================================
PART 8 — EXTERNAL LEARNING LINKS & PART 9 — LINK QUALITY
============================================================
EVERY major topic MUST contain a "Further Learning" section.
Prefer official documentation, university course material, original papers, etc.
Explain why each link is worth opening and verify they are valid.

============================================================
PART 10 — EXAM PREPARATION & PART 11 — QUESTION BANK
============================================================
Every major topic MUST explicitly identify exam relevance (Must Know, Must Memorize, Must Be Able To Derive, etc.).
Create a substantial question bank for every major topic.

============================================================
PART 12 — COMPARISON TABLES & PART 13 — COMMON MISTAKES
============================================================
Create comparison tables for confusing concepts.
Include a "Common Mistakes" section.

============================================================
PART 14 — PREREQUISITE HANDLING & PART 15 — DO NOT TEACH THE WRONG THING
============================================================
Link to earlier syllabus items. Stay within the syllabus.

============================================================
PART 16 — CONSISTENT MATHEMATICAL NOTATION
============================================================
Use consistent notation (x=input, y=output, etc.).

============================================================
PART 17 — CODE QUALITY & PART 18 — NUMERICAL VERIFICATION
============================================================
Every code example must be runnable, valid, correct.
Verify numerical answers independently.

============================================================
PART 19 — WEBSITE & PART 20 — HOME PAGE
============================================================
Build a professional documentation website using MkDocs + Material for MkDocs.
Create an excellent homepage (index.md).

============================================================
PART 21 — SYLLABUS PAGE & PART 22 — STUDY DASHBOARD
============================================================
Create syllabus.md and study-plan.md to track progress.

============================================================
PART 23 — REVISION MATERIAL
============================================================
Every major topic must have a concise revision component.

============================================================
PART 24 — VISUAL QUALITY & PART 25 — SOURCE QUALITY
============================================================
Use short paragraphs, tables, diagrams, equations, callouts. Avoid giant walls of text.
Prefer authoritative sources.

============================================================
PART 26 — RESEARCH PAPER REFERENCES
============================================================
Include original papers when appropriate for major modern NLP methods.

============================================================
PART 27 — INTERNAL LINKING & PART 28 — LINK VALIDATION
============================================================
Create a dense but logical internal link network. Check all links.

============================================================
PART 29 — BUILD VALIDATION & PART 30 — DEPLOYMENT
============================================================
Run `mkdocs build --strict`. Fix all errors.
Deploy to GitHub Pages.

============================================================
PART 32 — CONTENT COMPLETENESS AUDIT & PART 33 — DEPTH AUDIT
============================================================
Audit for completeness and depth.

============================================================
PART 34 — ANTI-SHALLOW-CONTENT RULE
============================================================
DO NOT generate shallow content. Explain what, why, intuition, mechanism, mathematics, implementation, etc.

============================================================
PART 36 — FINAL PROJECT STRUCTURE
============================================================
Aim for a structure broadly resembling MkDocs format with a `docs/` folder.

============================================================
PART 37 — README.md & PART 38 — FINAL REPORT
============================================================
Root README.md explains the project. Provide a concise final report when finished.
