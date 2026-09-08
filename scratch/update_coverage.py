import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Language identification definition": "language-identification-fundamentals.md",
    "Unknown language handling": "language-identification-fundamentals.md",
    
    "Character n-gram language model": "n-gram-language-profiles.md",
    "Language profiles": "n-gram-language-profiles.md",
    "Likelihood/similarity-based classification": "n-gram-language-profiles.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 10-language-identification \| TBD \| PENDING \|"
    replacement = f"| {item} | 10-language-identification | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
