import os
import re

# 1. Create docs directory
os.makedirs('docs', exist_ok=True)

# 2. Create requirements.txt
with open('requirements.txt', 'w', encoding='utf-8') as f:
    f.write("mkdocs-material\npymdown-extensions\n")

# 3. Create mkdocs.yml
mkdocs_yaml = """site_name: NLP Study Guide
site_description: A comprehensive study material website for Natural Language Processing
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - toc.integrate
    - search.suggest
    - search.highlight
    - content.code.copy
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - admonition
  - pymdownx.details
  - attr_list
  - md_in_html

extra_javascript:
  - javascripts/mathjax.js
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
"""
with open('mkdocs.yml', 'w', encoding='utf-8') as f:
    f.write(mkdocs_yaml)

# 4. Create javascripts directory for mathjax config
os.makedirs('docs/javascripts', exist_ok=True)
mathjax_js = """window.MathJax = {
  tex: {
    inlineMath: [["\\\\(", "\\\\)"]],
    displayMath: [["\\\\[", "\\\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};
"""
with open('docs/javascripts/mathjax.js', 'w', encoding='utf-8') as f:
    f.write(mathjax_js)


# 5. Create SOURCE-COVERAGE.md by parsing SYLLABUS.md
with open('SYLLABUS.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

coverage_lines = [
    "# Source Coverage Map",
    "",
    "| Syllabus Item | Major Topic Folder | Markdown File | Status |",
    "|---|---|---|---|"
]

current_folder = ""

for line in lines:
    line = line.strip()
    if line.startswith("## "):
        # e.g. "## 1. NLP Fundamentals"
        match = re.match(r'## (\d+)\. (.*)', line)
        if match:
            num = match.group(1).zfill(2)
            name = match.group(2).lower().replace(" ", "-").replace("&", "and").replace(",", "")
            current_folder = f"{num}-{name}"
    elif line.startswith("- "):
        item = line[2:]
        coverage_lines.append(f"| {item} | {current_folder} | TBD | PENDING |")

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write("\\n".join(coverage_lines) + "\\n")

# 6. Create initial root docs
index_md = """# Welcome to the NLP Study Guide

This is a comprehensive, exam-oriented study material website for Natural Language Processing.

## What This Website Contains
- Deep theoretical explanations
- Mathematical formulations and derivations
- Numerical problems with worked solutions
- Scratch implementations of core algorithms in Python
- Exam preparation questions and notes

## How to Use It
1. Use the [Syllabus](syllabus.md) page to see the full list of topics.
2. Track your progress on the [Study Dashboard](study-plan.md).
3. Prepare for tests using the [Exam Preparation](exam-preparation.md) guide.

[**START LEARNING**](01-nlp-fundamentals/README.md)
"""
with open('docs/index.md', 'w', encoding='utf-8') as f:
    f.write(index_md)

with open('docs/syllabus.md', 'w', encoding='utf-8') as f:
    f.write("# Full Syllabus\\n\\n(Generated from `SYLLABUS.md`)\\n")
    
with open('docs/study-plan.md', 'w', encoding='utf-8') as f:
    f.write("# Study Dashboard\\n\\nTrack your progress here.\\n")
    
with open('docs/exam-preparation.md', 'w', encoding='utf-8') as f:
    f.write("# Exam Preparation\\n\\nReview questions and typical exam traps.\\n")
