import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace TBD and PENDING with the actual files for module 2
mapping = {
    "Data collection": "data-collection-and-splits.md",
    "Train/test split": "data-collection-and-splits.md",
    "Validation set": "data-collection-and-splits.md",
    "Data leakage": "data-collection-and-splits.md",
    "Model training": "data-collection-and-splits.md",
    "Model evaluation": "data-collection-and-splits.md",
    
    "Text cleaning": "text-cleaning-and-normalization.md",
    "Normalization": "text-cleaning-and-normalization.md",
    "Lowercasing / uppercasing": "text-cleaning-and-normalization.md",
    "Whitespace normalization": "text-cleaning-and-normalization.md",
    "Punctuation normalization": "text-cleaning-and-normalization.md",
    "Unicode normalization": "text-cleaning-and-normalization.md",
    "Numbers, URLs, emails, hashtags and mentions": "text-cleaning-and-normalization.md",
    "Special-character handling": "text-cleaning-and-normalization.md",
    
    "Vocabulary construction": "vocabulary-and-features.md",
    "Feature engineering": "vocabulary-and-features.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 02-nlp-pipeline-and-preprocessing \| TBD \| PENDING \|"
    replacement = f"| {item} | 02-nlp-pipeline-and-preprocessing | {md_file} | COMPLETE |"
    content = re.sub(pattern, replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
