import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "NER definition": "ner-fundamentals.md",
    "PERSON": "ner-fundamentals.md",
    "LOCATION/LOC": "ner-fundamentals.md",
    "ORGANIZATION/ORG": "ner-fundamentals.md",
    "DATE": "ner-fundamentals.md",
    "MONEY": "ner-fundamentals.md",
    "PRODUCT": "ner-fundamentals.md",
    "EVENT": "ner-fundamentals.md",
    
    "BIO tagging for NER": "ner-tagging-and-evaluation.md",
    "Rule-based NER": "ner-tagging-and-evaluation.md",
    "NER evaluation": "ner-tagging-and-evaluation.md",
    
    "Entity linking concept": "entity-linking.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 09-named-entity-recognition \| TBD \| PENDING \|"
    replacement = f"| {item} | 09-named-entity-recognition | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
