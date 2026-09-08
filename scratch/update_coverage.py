import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Stemming definition": "stemming.md",
    "Rule-based stemming": "stemming.md",
    "Suffix stripping": "stemming.md",
    "Porter Stemmer concept": "stemming.md",
    "Snowball Stemmer concept": "stemming.md",
    "Lancaster Stemmer concept": "stemming.md",
    
    "Lemmatization definition": "lemmatization.md",
    "Dictionary-based lemmatization": "lemmatization.md",
    "Rule-based lemmatization": "lemmatization.md",
    "POS-aware lemmatization": "lemmatization.md",
    "Irregular lemma examples": "lemmatization.md",
    
    "Stemming vs lemmatization": "stemming-vs-lemmatization.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 07-stemming-and-lemmatization \| TBD \| PENDING \|"
    replacement = f"| {item} | 07-stemming-and-lemmatization | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
