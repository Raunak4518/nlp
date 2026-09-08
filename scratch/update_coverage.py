import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Finite State Transducer (FST)": "finite-state-transducers.md",
    "Input/output transitions": "finite-state-transducers.md",
    "Morphological analysis": "finite-state-transducers.md",
    "Morphological generation": "finite-state-transducers.md",
    "FST-based morphological analyzer": "finite-state-transducers.md",
    "FST-based morphological generator": "finite-state-transducers.md",
    
    "Morphology definition": "morphology-fundamentals.md",
    "Morph": "morphology-fundamentals.md",
    "Morpheme": "morphology-fundamentals.md",
    "Root and stem": "morphology-fundamentals.md",
    "Affixes": "morphology-fundamentals.md",
    "Inflectional morphology": "morphology-fundamentals.md",
    "Derivational morphology": "morphology-fundamentals.md",
    "Inflection vs derivation": "morphology-fundamentals.md",
    "Number/tense/person/case/agreement": "morphology-fundamentals.md",
    "cat → cat + N + SG/PL style analysis": "morphology-fundamentals.md",
    "Verb morphology: walk/walked/walking": "morphology-fundamentals.md",
    "Plural rules: cat/cats, box/boxes": "morphology-fundamentals.md",
    "Irregular morphology: child/children, mouse/mice": "morphology-fundamentals.md",
    "Irregular verbs: go/went, be/was, have/had": "morphology-fundamentals.md",
    "Morphological ambiguity": "morphology-fundamentals.md",
}

for item, md_file in mapping.items():
    pattern = rf"\| {re.escape(item)} \| 06-finite-state-transducers-and-morphology \| TBD \| PENDING \|"
    replacement = f"| {item} | 06-finite-state-transducers-and-morphology | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
