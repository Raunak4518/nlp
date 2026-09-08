import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Language model definition": "language-models-and-ngrams.md",
    "Next-token prediction": "language-models-and-ngrams.md",
    "Unigram": "language-models-and-ngrams.md",
    "Bigram": "language-models-and-ngrams.md",
    "Trigram": "language-models-and-ngrams.md",
    "4-gram / general N-gram": "language-models-and-ngrams.md",
    "Word N-grams": "language-models-and-ngrams.md",
    "Character N-grams": "language-models-and-ngrams.md",
    "Number of n-grams = N-n+1": "language-models-and-ngrams.md",
    "Vocabulary size": "language-models-and-ngrams.md",
    
    "N-gram count generation": "n-gram-probabilities.md",
    "MLE unigram probability": "n-gram-probabilities.md",
    "MLE bigram probability": "n-gram-probabilities.md",
    "MLE trigram probability": "n-gram-probabilities.md",
    "Sentence probability": "n-gram-probabilities.md",
    "N-gram probability numericals": "n-gram-probabilities.md",
    
    "<s> start marker": "text-generation.md",
    "</s> end marker": "text-generation.md",
    "<UNK> unknown token": "text-generation.md",
    "Next-word prediction using argmax": "text-generation.md",
    "Random sentence generation": "text-generation.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 14-n-gram-language-models \| TBD \| PENDING \|"
    replacement = f"| {item} | 14-n-gram-language-models | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
