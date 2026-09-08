import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Linear interpolation": "linear-interpolation.md",
    "Unigram + bigram + trigram interpolation": "linear-interpolation.md",
    "Interpolation weights λ": "linear-interpolation.md",
    "λ1 + λ2 + λ3 = 1": "linear-interpolation.md",
    "Fixed interpolation": "linear-interpolation.md",
    "Interpolation vs backoff": "linear-interpolation.md",
    
    "Deleted interpolation": "estimating-weights.md",
    "Estimating interpolation weights": "estimating-weights.md",
    "Held-out data": "estimating-weights.md",
    "Interpolation numerical problems": "estimating-weights.md",
}

for item, md_file in mapping.items():
    # Due to encoding issues (e.g. lambda weights?), I should be careful. 
    # I noticed in the previous read of the syllabus they were rendered as `?` or `?1 + ?2 + ?3 = 1`.
    # Let's write a python script to do this safely. Wait, my update_coverage.py handles exact match. Let me check what is in SOURCE-COVERAGE.md for those symbols.
    pass

# I will write the python script to read lines, replace if it contains the topic name, and write back.
