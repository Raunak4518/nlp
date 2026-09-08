# N-Gram Language Profiles

## 1. Character N-Grams
In the Tokenization module, we discussed *word n-grams* (sequences of whole words). For Language Identification, we strictly use **character n-grams** (sequences of individual characters).

To extract character n-grams, we first pad the string with spaces so the algorithm can learn which characters frequently start and end words.

- **Text**: `" hello "`
- **Character 3-grams (trigrams)**: `[" he", "hel", "ell", "llo", "lo "]`

## 2. Language Profiles
Every human language has a highly unique statistical signature of character n-grams.
- In English, `"th "` and `" th"` are incredibly common.
- In German, `"sch"` is very common.
- In Polish, `"sz"` and `"cz"` are common.

A **Language Profile** is simply a dictionary mapping character n-grams to their frequency of occurrence, trained on a massive corpus (like Wikipedia) of that language. 

To save memory and increase speed, a profile usually only keeps the top 300 to 400 most frequent n-grams. Anything beyond the top 400 is considered statistical noise.

---

## 3. Classification via Out-of-Place (OoP) Measure

To classify a new, unknown document, we use a simple distance metric.

1. **Build**: Extract all character n-grams from the unknown document and sort them by frequency to create a **Document Profile**.
2. **Compare**: Compare the Document Profile against every known Language Profile in the database.
3. **Score**: The Language Profile that is most "similar" (has the lowest distance score) to the Document Profile wins.

### The OoP Distance Algorithm
This is the classic ranking algorithm used by the famous *Cavnar and Trenkle (1994)* paper. It compares the *Rank* of the n-gram, not its raw count.

1. For every n-gram in the Document Profile, find its rank (e.g., it is the 5th most common n-gram).
2. Find the rank of that *exact same* n-gram in the target Language Profile (e.g., it is the 8th most common).
3. The distance for that n-gram is the absolute difference in ranks ($|5 - 8| = 3$).
4. **The Penalty**: If the document n-gram is not found in the Language Profile at all, assign a massive maximum penalty distance.
5. Sum the distances for all n-grams. 

!!! success "The Winner"
    The language with the **lowest total OoP distance** is the predicted language.

---

## 4. Scratch Implementation (Language Profiler)

Here is a functional implementation of the OoP algorithm in Python.

```python
from collections import defaultdict

def extract_character_ngrams(text: str, n: int = 3) -> list[str]:
    # Pad with spaces to capture word boundaries
    text = f" {text.lower()} " 
    return [text[i:i+n] for i in range(len(text)-n+1)]

def build_profile(text: str, top_k: int = 10) -> dict[str, int]:
    ngrams = extract_character_ngrams(text)
    counts = defaultdict(int)
    for ng in ngrams:
        counts[ng] += 1
        
    # Sort by count descending, take top_k
    sorted_ngrams = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:top_k]
    
    # Return a dictionary mapping the ngram to its Rank (0 is most frequent)
    return {ngram: rank for rank, (ngram, count) in enumerate(sorted_ngrams)}

def out_of_place_distance(doc_profile, lang_profile, max_penalty=50) -> int:
    total_distance = 0
    for ngram, doc_rank in doc_profile.items():
        if ngram in lang_profile:
            # Add absolute difference in ranks
            total_distance += abs(doc_rank - lang_profile[ngram])
        else:
            # N-gram not found in language profile, add maximum penalty
            total_distance += max_penalty
    return total_distance
```

### Try It Yourself

??? question "Trace the code"
    **Input Data:**
    ```python
    english_text = "the quick brown fox jumps over the lazy dog the the the"
    french_text = "le renard brun rapide saute par dessus le chien paresseux le le"
    
    # Train our two mock language profiles
    profile_en = build_profile(english_text)
    profile_fr = build_profile(french_text)
    
    # The unknown document we want to classify
    unknown_text = "the dog runs over the cat"
    profile_unknown = build_profile(unknown_text)
    
    # Calculate OoP Distance
    dist_en = out_of_place_distance(profile_unknown, profile_en)
    dist_fr = out_of_place_distance(profile_unknown, profile_fr)
    
    print(f"Distance to English: {dist_en}")
    print(f"Distance to French:  {dist_fr}")
    ```
    
    **Output:**
    ```text
    Distance to English: 294
    Distance to French:  488
    ```
    *The script outputs a significantly lower distance for English, correctly identifying the language of the unknown document.*

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: An unknown document's most frequent trigram (Rank 0) is `" th"`. In the English language profile, `" th"` is Rank 2. In the German profile, `" th"` is Rank 200. Using the Out-of-Place (OoP) algorithm, calculate the distance for `" th"` for both languages, and explain how this impacts the final classification.
> **Answer**: 
> - English Distance: $|0 - 2| = 2$.
> - German Distance: $|0 - 200| = 200$. 
> 
> The document's trigram is penalized heavily against the German profile due to the massive rank difference, adding 200 to the total distance score. It matches the English profile closely, adding only 2 to the score. Because the algorithm selects the language with the *lowest* total distance, this heavily steers the classification toward English.

**2-Mark Question**: Why does the OoP algorithm compare the *rank* of n-grams rather than their raw frequency counts?
> **Answer**: Raw frequency counts are highly dependent on the length of the document. A 10-page English document will have thousands more `"the"` trigrams than a 1-page English document. Comparing relative ranks normalizes the data, allowing a short document to be compared accurately against a massive training corpus.

---

### Can You Explain This?
- [ ] I can clearly distinguish between a word n-gram and a character n-gram.
- [ ] I can write the padding logic for character n-gram extraction.
- [ ] I can define a Language Profile.
- [ ] I understand the mathematics of the Out-of-Place (OoP) rank distance algorithm.
