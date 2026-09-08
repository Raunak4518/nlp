import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Probability basics": "probability-basics.md",
    "Joint probability": "probability-basics.md",
    "Conditional probability": "probability-basics.md",
    "Marginal probability": "probability-basics.md",
    "Probability normalization": "probability-basics.md",
    "Probability numerical problems": "probability-basics.md",
    
    "Bayes theorem": "bayes-and-chain-rule.md",
    "Chain rule": "bayes-and-chain-rule.md",
    
    "Relative frequency": "maximum-likelihood-estimation.md",
    "Maximum Likelihood Estimation (MLE)": "maximum-likelihood-estimation.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 13-probability-foundations \| TBD \| PENDING \|"
    replacement = f"| {item} | 13-probability-foundations | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
