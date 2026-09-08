# Lemmatization

## 1. What Is It?
Lemmatization is the proper, linguistic process of determining the **lemma** (dictionary base form) of a word based on its intended meaning. Unlike stemming, lemmatization guarantees that the resulting word is a valid word found in the language.

## 2. The Core Difference from Stemming
Lemmatization requires **morphological analysis** and **vocabulary/dictionary lookups**. It does not blindly chop off suffixes.
- *Stemming*: `better` $\rightarrow$ `better`
- *Lemmatization*: `better` $\rightarrow$ `good`

## 3. Approaches to Lemmatization

### Dictionary-Based Lemmatization
The system looks up the surface word in a massive predefined dictionary (like WordNet).
- Look up `was`. Dictionary maps `was` to `be`.

### Rule-Based Lemmatization
Similar to the morphological FSTs discussed in the previous module. The system uses grammatical rules to reverse-engineer the lemma.
- If the word is a noun ending in `s`, strip `s` and check if the result is in the dictionary.

### POS-Aware Lemmatization (The Standard)
Because words can be ambiguous, lemmatization **must** be aware of the Part-of-Speech (POS) of the word in context.
- **Example: "leaves"**
  - If POS is Noun: `leaves` $\rightarrow$ `leaf`
  - If POS is Verb: `leaves` $\rightarrow$ `leave`

Without POS tagging first, a lemmatizer is forced to guess, which often results in errors.

## 4. Irregular Lemma Examples
Lemmatization shines with highly irregular morphology that stemmers completely fail at:
- `am`, `is`, `are`, `was`, `were` $\rightarrow$ `be`
- `mice` $\rightarrow$ `mouse`
- `geese` $\rightarrow$ `goose`
- `worst` $\rightarrow$ `bad`

## 5. Scratch Implementation (Dictionary & POS Lemmatizer)
```python
def pos_aware_lemmatizer(word: str, pos: str) -> str:
    # A mock dictionary combining irregulars and base forms
    lemma_dict = {
        'V': {
            'is': 'be', 'are': 'be', 'was': 'be', 'were': 'be',
            'leaves': 'leave', 'went': 'go', 'running': 'run'
        },
        'N': {
            'leaves': 'leaf', 'mice': 'mouse', 'children': 'child',
            'ponies': 'pony', 'cats': 'cat'
        },
        'ADJ': {
            'better': 'good', 'worst': 'bad'
        }
    }
    
    # 1. Check if word exists in our POS-specific dictionary
    if pos in lemma_dict and word in lemma_dict[pos]:
        return lemma_dict[pos][word]
        
    # 2. Fallback rule: If it's a plural noun ending in 's', strip it
    if pos == 'N' and word.endswith('s'):
        return word[:-1]
        
    # 3. Default: return the word as-is
    return word

# Manual Trace
print(pos_aware_lemmatizer("leaves", "V"))   # Output: leave
print(pos_aware_lemmatizer("leaves", "N"))   # Output: leaf
print(pos_aware_lemmatizer("better", "ADJ")) # Output: good
print(pos_aware_lemmatizer("cats", "N"))     # Output: cat
```

## 6. Exam Preparation
### Must Know
- Lemmatization requires a dictionary/lexicon and Part-of-Speech context.
- A lemma is always a valid dictionary word.

### Likely Theory Question
**Question**: Why is POS tagging considered a prerequisite step for accurate lemmatization? Give an example.
**Answer**: Many surface word forms belong to multiple parts of speech, and their lemma depends entirely on which part of speech is intended. For example, the word "saw" can be a verb (past tense of "see" $\rightarrow$ lemma: "see") or a noun (a tool for cutting $\rightarrow$ lemma: "saw"). Without knowing the POS, the lemmatizer cannot determine the correct base form.
