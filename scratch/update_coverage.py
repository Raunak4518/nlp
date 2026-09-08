import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Laplace / Add-one smoothing": "laplace-smoothing.md",
    "Laplace formula": "laplace-smoothing.md",
    "Why +1 is added": "laplace-smoothing.md",
    "Why denominator becomes +V": "laplace-smoothing.md",
    "Seen-event probability after Laplace": "laplace-smoothing.md",
    "Unseen-event probability after Laplace": "laplace-smoothing.md",
    "Laplace limitations": "laplace-smoothing.md",
    "Implement Laplace smoothing from scratch": "laplace-smoothing.md",
    
    "Add-k smoothing": "add-k-smoothing.md",
    "Add-k formula": "add-k-smoothing.md",
    "Choosing k": "add-k-smoothing.md",
    "Grid search for k": "add-k-smoothing.md",
    "Validation-set selection of k": "add-k-smoothing.md",
    "Implement Add-k from scratch": "add-k-smoothing.md",
    "Add-k numerical problems": "add-k-smoothing.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 16-laplace-and-add-k-smoothing \| TBD \| PENDING \|"
    replacement = f"| {item} | 16-laplace-and-add-k-smoothing | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
