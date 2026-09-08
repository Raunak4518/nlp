# Stemming

## 1. What Is It?
Stemming is a crude, heuristic process that chops off the ends of words in the hope of achieving the goal of reducing inflectional forms and sometimes derivationally related forms of a word to a common base form.

## 2. Rule-Based Suffix Stripping
Stemmers do not understand language, grammar, or parts of speech. They apply a cascading series of string-manipulation rules, primarily looking at the end of the word (suffixes).

### Common Suffix Rules
- If word ends in `sses`, remove `es` (caresses $\rightarrow$ caress).
- If word ends in `ies`, replace with `i` (ponies $\rightarrow$ poni).
- If word ends in `ss`, do nothing (caress $\rightarrow$ caress).
- If word ends in `s`, remove `s` (cats $\rightarrow$ cat).

### The Problem with Stemming
Because it relies purely on string manipulation, stemming often results in "stems" that are not actual dictionary words.
- *Example*: `organization` $\rightarrow$ `organ`
- *Example*: `university` $\rightarrow$ `univers`

## 3. Major Stemming Algorithms
There are several standard algorithms used in English NLP.

### Porter Stemmer
Developed by Martin Porter in 1980. It is the most common, gentle stemmer. It uses 5 phases of word reduction applied sequentially.
- *Example*: `running` $\rightarrow$ `run`

### Snowball Stemmer
Also developed by Martin Porter. It is an updated, slightly more aggressive version of the Porter Stemmer, designed to be faster and support multiple languages (French, German, etc.). It is sometimes called the "Porter2" stemmer.

### Lancaster Stemmer
A very aggressive stemmer developed at Lancaster University. It has over 120 rules. It often reduces words so drastically that they become completely unrecognizable, which can hurt human readability but sometimes aids in extremely sparse vector spaces.
- *Example*: `maximum` $\rightarrow$ `maxim`
- *Example*: `presumably` $\rightarrow$ `presum`

## 4. Scratch Implementation (Basic Suffix Stripper)
```python
def basic_stemmer(word: str) -> str:
    word = word.lower()
    
    # Simple cascading rules (similar to Porter step 1a)
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

# Manual Trace
print(basic_stemmer("ponies"))   # Output: poni
print(basic_stemmer("caresses")) # Output: caress
print(basic_stemmer("cats"))     # Output: cat
print(basic_stemmer("walking"))  # Output: walk
```

## 5. Exam Preparation
### Must Know
- Stemming produces chopped strings that are often not valid linguistic words.
- The Porter stemmer is the industry standard baseline.

### Likely Theory Question
**Question**: Why does stemming sometimes fail to improve Information Retrieval systems?
**Answer**: Stemming can suffer from **over-stemming** (where two words with different meanings are reduced to the same stem, e.g., "organization" and "organ") and **under-stemming** (where two words with the same meaning are not reduced to the same stem). Over-stemming decreases precision by returning irrelevant documents.
