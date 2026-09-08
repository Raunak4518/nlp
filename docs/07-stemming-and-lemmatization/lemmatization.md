# Lemmatization

## 1. What Is It?
Lemmatization is the proper, linguistic process of determining the **lemma** (the dictionary base form) of a word based on its intended meaning. Unlike stemming, lemmatization guarantees that the resulting word is a valid, real word found in the language.

## 2. The Core Difference from Stemming
Lemmatization requires **morphological analysis** and **vocabulary/dictionary lookups**. It does not blindly chop off suffixes.

| Word | Stemming Output | Lemmatization Output |
| :--- | :--- | :--- |
| `better` | `better` | `good` |
| `was` | `wa` | `be` |
| `mice` | `mice` | `mouse` |

## 3. Approaches to Lemmatization

### Dictionary-Based Lemmatization
The system looks up the surface word in a massive, predefined lexical database (like WordNet).
- The system encounters `geese`. It searches the dictionary, which explicitly maps `geese` back to the lemma `goose`.

### Rule-Based Lemmatization
Similar to the morphological FSTs discussed in the previous module. The system uses grammatical rules to reverse-engineer the lemma.
- **Rule**: If the word is a noun ending in `s`, strip `s` and check if the resulting string exists in the dictionary. If yes, that is the lemma.

---

## 4. POS-Aware Lemmatization (The Standard)
Because words can be deeply ambiguous, accurate lemmatization **must** be aware of the Part-of-Speech (POS) of the word in its specific context.

### The Ambiguity Problem
Take the word **"leaves"**.
- If the POS is **Noun** (e.g., "The leaves fell"): `leaves` $\rightarrow$ `leaf`
- If the POS is **Verb** (e.g., "He leaves now"): `leaves` $\rightarrow$ `leave`

Without running a Part-of-Speech tagger *before* the lemmatizer, the lemmatizer is forced to guess, which severely degrades accuracy.

---

## 5. Scratch Implementation (Dictionary & POS Lemmatizer)

Here is a simple mock implementation showing how a lemmatizer uses both a dictionary of irregulars and POS tags to resolve ambiguity.

```python
def pos_aware_lemmatizer(word: str, pos: str) -> str:
    word = word.lower()
    
    # A mock dictionary combining irregulars and base forms
    lemma_dict = {
        'V': { # Verbs
            'is': 'be', 'are': 'be', 'was': 'be', 'were': 'be',
            'leaves': 'leave', 'went': 'go', 'running': 'run'
        },
        'N': { # Nouns
            'leaves': 'leaf', 'mice': 'mouse', 'children': 'child',
            'ponies': 'pony', 'cats': 'cat'
        },
        'ADJ': { # Adjectives
            'better': 'good', 'worst': 'bad'
        }
    }
    
    # 1. Check if word exists in our POS-specific dictionary
    if pos in lemma_dict and word in lemma_dict[pos]:
        return lemma_dict[pos][word]
        
    # 2. Fallback rule: If it's a regular plural noun ending in 's', strip it
    if pos == 'N' and word.endswith('s'):
        return word[:-1]
        
    # 3. Default: return the word as-is (assuming it's already a lemma)
    return word
```

### Try It Yourself

??? question "Trace the code on these inputs"
    **Output:**
    ```python
    print(pos_aware_lemmatizer("leaves", "V"))   # Output: leave
    print(pos_aware_lemmatizer("leaves", "N"))   # Output: leaf
    print(pos_aware_lemmatizer("better", "ADJ")) # Output: good
    print(pos_aware_lemmatizer("cats", "N"))     # Output: cat
    ```

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Why is Part-of-Speech (POS) tagging considered a strict prerequisite step for accurate lemmatization? Give a concrete example to justify your answer.
> **Answer**: Many surface word forms belong to multiple parts of speech, and their lemma depends entirely on which part of speech is intended in context. Without knowing the POS, the lemmatizer cannot resolve this ambiguity. 
> For example, the word **"saw"** can be:
> 1. A verb (past tense of "see"). Its lemma is **"see"**.
> 2. A noun (a tool for cutting). Its lemma is **"saw"**.
> By running a POS tagger first, the lemmatizer knows which dictionary lookup path to take, ensuring it returns the linguistically correct base form.

---

### Can You Explain This?
- [ ] I can explain why lemmatizers require massive dictionaries (like WordNet).
- [ ] I can list three highly irregular English words that stemmers fail on but lemmatizers handle perfectly.
- [ ] I understand the dependency pipeline (Why POS tagging must happen *before* lemmatization).
