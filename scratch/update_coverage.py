import re

with open('SOURCE-COVERAGE.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace TBD and PENDING with the actual files for module 5
mapping = {
    "Finite State Automaton definition": "fsa-fundamentals.md",
    "Formal tuple M=(Q,Σ,δ,q0,F)": "fsa-fundamentals.md",
    "States": "fsa-fundamentals.md",
    "Alphabet": "fsa-fundamentals.md",
    "Initial state": "fsa-fundamentals.md",
    "Accepting/final states": "fsa-fundamentals.md",
    "Transition function": "fsa-fundamentals.md",
    "Regex → automaton concept": "fsa-fundamentals.md",
    
    "DFA definition": "dfa.md",
    "DFA transition table": "dfa.md",
    "DFA state-diagram construction": "dfa.md",
    "DFA string acceptance": "dfa.md",
    "Implement a generic DFA recognizer from scratch": "dfa.md",
    
    "NFA definition": "nfa.md",
    "NFA multiple transitions": "nfa.md",
    "Epsilon transitions": "nfa.md",
    "NFA string acceptance": "nfa.md",
    "DFA vs NFA": "nfa.md",
    "Implement an NFA recognizer from scratch": "nfa.md",
}

for item, md_file in mapping.items():
    # Use re.escape on the item directly to handle weird chars safely
    pattern = rf"\| {re.escape(item)} \| 05-finite-state-automata \| TBD \| PENDING \|"
    replacement = f"| {item} | 05-finite-state-automata | {md_file} | COMPLETE |"
    content = re.sub(pattern, lambda m: replacement, content)

with open('SOURCE-COVERAGE.md', 'w', encoding='utf-8') as f:
    f.write(content)
