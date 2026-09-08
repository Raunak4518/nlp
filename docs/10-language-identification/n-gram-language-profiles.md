# N-Gram Language Profiles

## 1. Character N-Grams
In the Tokenization module, we discussed word n-grams (sequences of words). For Language Identification, we use **character n-grams** (sequences of characters).

- **Text**: `_hello_` (using `_` to denote spaces)
- **Character 3-grams (trigrams)**: `_he`, `hel`, `ell`, `llo`, `lo_`

## 2. Language Profiles
Every language has a unique statistical signature of character n-grams.
- In English, `th_` and `_th` are incredibly common.
- In German, `sch` is very common.
- In Polish, `sz` and `cz` are common.

A **Language Profile** is simply a dictionary mapping character n-grams to their frequency of occurrence in a massive corpus of that language. To save memory, a profile usually only keeps the top 300 to 400 most frequent n-grams.

## 3. Classification via Similarity (Out-of-Place Measure)
To classify a new, unknown document:
1. Extract all character n-grams from the unknown document and sort them by frequency to create a **Document Profile**.
2. Compare the Document Profile against every known Language Profile.
3. The Language Profile that is most "similar" to the Document Profile wins.

### Out-of-Place (OoP) Distance Algorithm
This is the classic algorithm used by the famous *Cavnar and Trenkle (1994)* paper.
- For every n-gram in the Document Profile, find its rank (e.g., 5th most common).
- Find the rank of that same n-gram in the Language Profile (e.g., 8th most common).
- The distance for that n-gram is the absolute difference in ranks ($|5 - 8| = 3$).
- If the n-gram is not in the Language Profile at all, assign a maximum penalty distance.
- Sum the distances for all n-grams. The language with the **lowest total distance** is the predicted language.

## 4. Scratch Implementation (Language Profiler)
```python
from collections import defaultdict

def extract_character_ngrams(text: str, n: int = 3) -> list[str]:
    text = f" {text.lower()} " # Pad with spaces
    return [text[i:i+n] for i in range(len(text)-n+1)]

def build_profile(text: str, top_k: int = 10) -> dict[str, int]:
    ngrams = extract_character_ngrams(text)
    counts = defaultdict(int)
    for ng in ngrams:
        counts[ng] += 1
        
    # Sort by count descending, take top_k, assign rank (0 is most frequent)
    sorted_ngrams = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:top_k]
    return {ngram: rank for rank, (ngram, count) in enumerate(sorted_ngrams)}

def out_of_place_distance(doc_profile, lang_profile, max_penalty=50) -> int:
    total_distance = 0
    for ngram, doc_rank in doc_profile.items():
        if ngram in lang_profile:
            # Add difference in ranks
            total_distance += abs(doc_rank - lang_profile[ngram])
        else:
            # N-gram not found in language profile, add penalty
            total_distance += max_penalty
    return total_distance

# --- Trace ---
english_text = "the quick brown fox jumps over the lazy dog the the the"
french_text = "le renard brun rapide saute par dessus le chien paresseux le le"

profile_en = build_profile(english_text)
profile_fr = build_profile(french_text)

unknown_text = "the dog runs over the cat"
profile_unknown = build_profile(unknown_text)

dist_en = out_of_place_distance(profile_unknown, profile_en)
dist_fr = out_of_place_distance(profile_unknown, profile_fr)

print(f"Distance to English: {dist_en}")
print(f"Distance to French:  {dist_fr}")
# The script will output a lower distance for English, correctly identifying the language.
```

## 5. Exam Preparation
### Must Memorize
- LangID relies on **Character** N-Grams, not Word N-Grams.
- The Out-of-Place algorithm compares the **rank** of the n-grams, not their raw frequencies.

### Likely Practical Question
**Question**: An unknown document's top trigram is `_th`. In the English profile, `_th` is rank 2. In the German profile, `_th` is rank 200. What is the Out-of-Place distance for `_th` for both languages?
**Answer**: 
- English Distance: $|0 - 2| = 2$.
- German Distance: $|0 - 200| = 200$. 
The document is penalized heavily against German, steering the classification toward English.
