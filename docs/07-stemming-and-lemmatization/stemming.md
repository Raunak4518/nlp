# Stemming

## 1. What Is It?
Stemming is a crude, heuristic process that chops off the ends of words in the hope of achieving the goal of reducing inflectional forms and sometimes derivationally related forms of a word to a common base form.

## 2. Rule-Based Suffix Stripping
Stemmers do not understand language, grammar, context, or parts of speech. They apply a cascading series of raw string-manipulation rules, primarily looking at the end of the word (suffixes).

### Common Suffix Rules
- If word ends in `sses`, remove `es` (caresses $\rightarrow$ caress).
- If word ends in `ies`, replace with `i` (ponies $\rightarrow$ poni).
- If word ends in `ss`, do nothing (caress $\rightarrow$ caress).
- If word ends in `s`, remove `s` (cats $\rightarrow$ cat).

### The Problem with Stemming
Because it relies purely on string manipulation rather than linguistic knowledge, stemming frequently results in "stems" that are not actual dictionary words.

| Original Word | Stemmed Result | Problem |
| :--- | :--- | :--- |
| `organization` | `organ` | **Over-stemming**: Two different concepts reduced to the same stem. |
| `university` | `univers` | Not a valid English word. |
| `alumnus` / `alumni` | `alumnus` / `alumni` | **Under-stemming**: Plural/Singular fail to resolve to the same stem. |

---

## 3. Major Stemming Algorithms
There are several standard algorithms used in English NLP.

### Porter Stemmer
Developed by Martin Porter in 1980. It is the most common, gentle stemmer used in the industry. It uses 5 phases of word reduction applied sequentially.
- *Example*: `running` $\rightarrow$ `run`

### Snowball Stemmer
Also developed by Martin Porter. It is an updated, slightly more aggressive version of the Porter Stemmer, designed to be faster and support multiple languages (French, German, etc.). It is sometimes called the "Porter2" stemmer.

### Lancaster Stemmer
A very aggressive stemmer developed at Lancaster University. It has over 120 rules. It often reduces words so drastically that they become completely unrecognizable.
- *Example*: `maximum` $\rightarrow$ `maxim`
- *Example*: `presumably` $\rightarrow$ `presum`

---

## 4. Scratch Implementation (Basic Suffix Stripper)

Here is a Python implementation of the very first step (Step 1a) of the Porter Stemmer.

```python
def basic_stemmer(word: str) -> str:
    word = word.lower()
    
    # Simple cascading rules 
    if word.endswith("sses"):
        return word[:-2]
    if word.endswith("ies"):
        return word[:-3] + "i"
    if word.endswith("ss"):
        return word
    if word.endswith("s"):
        return word[:-1]
    if word.endswith("ing"):
        return word[:-3]
    if word.endswith("ed"):
        return word[:-2]
        
    return word
```

### Try It Yourself

??? question "Trace the code on these inputs"
    **Input:** `["ponies", "caresses", "cats", "walking"]`
    
    **Output:**
    ```python
    print(basic_stemmer("ponies"))   # Output: poni
    print(basic_stemmer("caresses")) # Output: caress
    print(basic_stemmer("cats"))     # Output: cat
    print(basic_stemmer("walking"))  # Output: walk
    ```
    *Notice how `poni` is not a valid English word. This is standard behavior for a stemmer.*

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Define Over-stemming and Under-stemming. How do they affect the performance of an Information Retrieval system?
> **Answer**: 
> - **Over-stemming** occurs when two words with completely different semantic meanings are chopped down to the identical stem (e.g., `organization` and `organ` both becoming `organ`). This hurts **precision**, because a search for "musical organs" will incorrectly return documents about "business organizations".
> - **Under-stemming** occurs when two words that share the same semantic meaning are NOT reduced to the same stem (e.g., `alumnus` and `alumni`). This hurts **recall**, because a search for "university alumni" will fail to return documents containing the word "alumnus".

---

### Can You Explain This?
- [ ] I can explain why a stemmed word is often not a dictionary word.
- [ ] I can name the most famous stemming algorithm.
- [ ] I can explain the difference between over-stemming and under-stemming.
