import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace TBD and PENDING with the actual files for module 1
mapping = {
    "What is Natural Language Processing": "what-is-nlp.md",
    "Natural vs programming language": "what-is-nlp.md",
    "NLP vs AI vs ML vs Deep Learning": "what-is-nlp.md",
    "Computational linguistics": "what-is-nlp.md",
    
    "Why natural language is difficult": "challenges-in-nlp.md",
    "Ambiguity": "challenges-in-nlp.md",
    "Context and variability": "challenges-in-nlp.md",
    "Spoken vs written language": "challenges-in-nlp.md",
    "Filler words and disfluencies": "challenges-in-nlp.md",
    
    "Training, validation, testing and inference": "machine-learning-foundations.md",
    "Inductive bias": "machine-learning-foundations.md",
    
    "NLP tasks: language modeling": "core-nlp-tasks.md",
    "Text classification": "core-nlp-tasks.md",
    "Sequence labeling/tagging": "core-nlp-tasks.md",
    "Sequence generation": "core-nlp-tasks.md",
    
    "Machine translation": "nlp-applications.md",
    "Speech recognition": "nlp-applications.md",
    "Text-to-speech": "nlp-applications.md",
    "Summarization": "nlp-applications.md",
    "Speaker identification": "nlp-applications.md",
    "Sentiment analysis": "nlp-applications.md",
    "Chatbots": "nlp-applications.md",
    "Code assistants": "nlp-applications.md",
    "NLP applications and pipeline overview": "nlp-applications.md",
}

for item, md_file in mapping.items():
    # Example line: | What is Natural Language Processing | 01-nlp-fundamentals | TBD | PENDING |
    pattern = rf"\| {re.escape(item)} \| 01-nlp-fundamentals \| TBD \| PENDING \|"
    replacement = f"| {item} | 01-nlp-fundamentals | {md_file} | COMPLETE |"
    content = re.sub(pattern, replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
