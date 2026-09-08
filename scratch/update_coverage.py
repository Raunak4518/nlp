import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Part-of-speech tagging": "parts-of-speech.md",
    "Noun": "parts-of-speech.md",
    "Verb": "parts-of-speech.md",
    "Adjective": "parts-of-speech.md",
    "Adverb": "parts-of-speech.md",
    "Pronoun": "parts-of-speech.md",
    "Determiner": "parts-of-speech.md",
    "Preposition": "parts-of-speech.md",
    "Conjunction": "parts-of-speech.md",
    "Interjection": "parts-of-speech.md",
    "Particle": "parts-of-speech.md",
    "Numeral": "parts-of-speech.md",
    "Punctuation tags": "parts-of-speech.md",
    "POS ambiguity": "parts-of-speech.md",
    
    "Sequence labeling": "sequence-labeling-fundamentals.md",
    "Sequence classification vs sequence labeling": "sequence-labeling-fundamentals.md",
    "BIO encoding": "sequence-labeling-fundamentals.md",
    "BILOU encoding": "sequence-labeling-fundamentals.md",
    
    "Rule-based POS tagger": "pos-tagging-algorithms.md",
    "HMM POS tagging": "pos-tagging-algorithms.md",
    "Viterbi algorithm": "pos-tagging-algorithms.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 08-pos-tagging-and-sequence-labeling \| TBD \| PENDING \|"
    replacement = f"| {item} | 08-pos-tagging-and-sequence-labeling | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
