import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Bag of Words": "bag-of-words.md",
    "Count vector": "bag-of-words.md",
    "Binary word features": "bag-of-words.md",
    
    "Term Frequency (TF)": "tf-idf.md",
    "Document Frequency (DF)": "tf-idf.md",
    "Inverse Document Frequency (IDF)": "tf-idf.md",
    "TF-IDF": "tf-idf.md",
    "TF-IDF numerical calculation": "tf-idf.md",
    
    "Vector normalization": "cosine-similarity.md",
    "Cosine similarity": "cosine-similarity.md",
    "Cosine similarity numerical problems": "cosine-similarity.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 12-tf-idf-and-vector-semantics \| TBD \| PENDING \|"
    replacement = f"| {item} | 12-tf-idf-and-vector-semantics | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
