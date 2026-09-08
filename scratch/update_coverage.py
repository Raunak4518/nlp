import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace TBD and PENDING with the actual files for module 3
mapping = {
    "Definition and purpose of tokenization": "tokenization-fundamentals.md",
    "Character units": "tokenization-fundamentals.md",
    "Word units": "tokenization-fundamentals.md",
    "Sentence units": "tokenization-fundamentals.md",
    "Paragraph/document/corpus": "tokenization-fundamentals.md",
    "Character tokenization": "tokenization-fundamentals.md",
    "Word tokenization": "tokenization-fundamentals.md",
    "Subword tokenization": "tokenization-fundamentals.md",
    "Unknown-token handling (<UNK>)": "tokenization-fundamentals.md",
    
    "Sentence segmentation": "sentence-segmentation.md",
    "Sentence boundary markers": "sentence-segmentation.md",
    "Handling abbreviations such as Dr./Mr./Mrs.": "sentence-segmentation.md",
    
    "Whitespace tokenization": "tokenization-algorithms.md",
    "Punctuation tokenization": "tokenization-algorithms.md",
    "Regex-based tokenization": "tokenization-algorithms.md",
    "N-gram tokenization": "tokenization-algorithms.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 03-tokenization \| TBD \| PENDING \|"
    replacement = f"| {item} | 03-tokenization | {md_file} | COMPLETE |"
    content = re.sub(pattern, replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
