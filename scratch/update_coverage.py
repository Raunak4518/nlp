import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Parsing definition": "cfg-and-constituency.md",
    "Grammar": "cfg-and-constituency.md",
    "Context-Free Grammar (CFG)": "cfg-and-constituency.md",
    "Terminal": "cfg-and-constituency.md",
    "Non-terminal": "cfg-and-constituency.md",
    "Start symbol": "cfg-and-constituency.md",
    "Production rule": "cfg-and-constituency.md",
    "Derivation": "cfg-and-constituency.md",
    "Leftmost derivation": "cfg-and-constituency.md",
    "Rightmost derivation": "cfg-and-constituency.md",
    "Parse tree": "cfg-and-constituency.md",
    "Constituency parsing": "cfg-and-constituency.md",
    "Bracketing": "cfg-and-constituency.md",
    "Ambiguous grammar/sentence": "cfg-and-constituency.md",
    "Resolving ambiguity with grammar": "cfg-and-constituency.md",
    
    "Recursive-descent parsing": "parsing-algorithms.md",
    "Top-down parsing": "parsing-algorithms.md",
    "Bottom-up parsing": "parsing-algorithms.md",
    "CYK parsing": "parsing-algorithms.md",
    "Earley parsing concept": "parsing-algorithms.md",
    
    "Dependency parsing": "dependency-parsing.md",
    "Head/dependent": "dependency-parsing.md",
    "Dependency relations": "dependency-parsing.md",
    "Root node": "dependency-parsing.md",
    "CoNLL format": "dependency-parsing.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 11-parsing-and-grammar \| TBD \| PENDING \|"
    replacement = f"| {item} | 11-parsing-and-grammar | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
