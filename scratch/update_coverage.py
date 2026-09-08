import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace TBD and PENDING with the actual files for module 4
mapping = {
    "Regex fundamentals": "regex-fundamentals.md",
    "Literal characters": "regex-fundamentals.md",
    "Wildcard .": "regex-fundamentals.md",
    "Character classes []": "regex-fundamentals.md",
    "Ranges [a-z], [A-Z], [0-9]": "regex-fundamentals.md",
    "Negated classes [^...]": "regex-fundamentals.md",
    "Quantifier *": "regex-fundamentals.md",
    "Quantifier +": "regex-fundamentals.md",
    "Quantifier ?": "regex-fundamentals.md",
    "{m,n} repetition": "regex-fundamentals.md",
    "Grouping ()": "regex-fundamentals.md",
    "Alternation |": "regex-fundamentals.md",
    "Start/end anchors ^ and $": "regex-fundamentals.md",
    "Escaping special characters": "regex-fundamentals.md",
    "\\d / \\D": "regex-fundamentals.md",
    "\\w / \\W": "regex-fundamentals.md",
    "\\s / \\S": "regex-fundamentals.md",
    
    "Greedy matching": "advanced-regex-and-python.md",
    "Non-greedy matching": "advanced-regex-and-python.md",
    "search()": "advanced-regex-and-python.md",
    "match()": "advanced-regex-and-python.md",
    "findall()": "advanced-regex-and-python.md",
    "finditer()": "advanced-regex-and-python.md",
    "sub() / substitution": "advanced-regex-and-python.md",
    "split()": "advanced-regex-and-python.md",
    "Capturing groups": "advanced-regex-and-python.md",
    
    "Regex for email extraction": "regex-applications.md",
    "Regex for URL extraction": "regex-applications.md",
    "Regex for phone/date/number extraction": "regex-applications.md",
    "Regex for sentence boundaries": "regex-applications.md",
    "Regex and finite automata relationship": "regex-applications.md",
}

for item, md_file in mapping.items():
    # Handle the fact that some items have backslashes that need double escaping
    pattern = rf"\| {re.escape(item)} \| 04-regular-expressions \| TBD \| PENDING \|"
    replacement = f"| {item} | 04-regular-expressions | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
