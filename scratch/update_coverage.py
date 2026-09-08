import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Data sparsity": "data-sparsity.md",
    "Vocabulary explosion V²/V³/Vⁿ": "data-sparsity.md",
    "Sparse count tables": "data-sparsity.md",
    
    "Unseen N-grams": "the-zero-probability-problem.md",
    "Zero probability": "the-zero-probability-problem.md",
    "Zero probability causing sentence probability = 0": "the-zero-probability-problem.md",
    "Unknown words": "the-zero-probability-problem.md",
    "Why smoothing is necessary": "the-zero-probability-problem.md",
}

for item, md_file in mapping.items():
    # Because of exponents in V²/V³/Vⁿ, we must use precise matching and escape correctly
    pattern = rf"\| {re.escape(item)} \| 15-sparsity-and-zero-probability-problem \| TBD \| PENDING \|"
    replacement = f"| {item} | 15-sparsity-and-zero-probability-problem | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
