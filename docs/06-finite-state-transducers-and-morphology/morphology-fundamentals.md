# Morphology Fundamentals

## 1. What Is Morphology?
Morphology is the study of the internal structure of words and how they are formed. Just as syntax dictates how words combine to form sentences, morphology dictates how smaller units combine to form words.

## 2. Morphs and Morphemes
- **Morpheme**: The smallest meaning-bearing unit in a language. (An abstract concept).
- **Morph**: The physical realization (the actual spelling/sounds) of a morpheme.

For example, the word "unbelievable" has three morphemes:
1. `un-` (meaning "not")
2. `believe` (the core action)
3. `-able` (meaning "capable of being")

## 3. Roots, Stems, and Affixes
- **Root**: The primary lexical unit of a word, carrying the most significant aspects of semantic content. It cannot be reduced further (e.g., "believe").
- **Stem**: The root plus any derivational affixes, to which inflectional affixes are added.
- **Affixes**: Bound morphemes that attach to roots/stems. They include:
  - **Prefixes**: Attach to the front (e.g., **un**happy).
  - **Suffixes**: Attach to the end (e.g., happi**ness**).
  - **Infixes**: Inserted inside the root (rare in English, common in Tagalog).

## 4. Inflectional vs Derivational Morphology

### Inflectional Morphology
Modifies a word to express different grammatical categories (like tense, mood, person, number, case) **without** changing its core meaning or part of speech.
- *Examples*:
  - **Number**: cat $\rightarrow$ cats
  - **Tense**: walk $\rightarrow$ walked
  - **Person/Agreement**: I run $\rightarrow$ He runs

### Derivational Morphology
Creates an entirely **new word** with a new meaning, often changing the part of speech.
- *Examples*:
  - **Verb $\rightarrow$ Noun**: compute $\rightarrow$ computer
  - **Adjective $\rightarrow$ Adverb**: quick $\rightarrow$ quickly
  - **Noun $\rightarrow$ Adjective**: magic $\rightarrow$ magical

## 5. English Morphological Rules
English morphology is relatively simple compared to languages like Russian or Turkish, but it has many exceptions.

### Regular Noun Plurals
- Default rule: Add `-s` (cat $\rightarrow$ cats).
- Ends in s, z, x, ch, sh: Add `-es` (box $\rightarrow$ boxes).
- Ends in consonant + y: Change y to i, add `-es` (city $\rightarrow$ cities).

### Regular Verb Tenses
- Present Participle: Add `-ing` (walk $\rightarrow$ walking).
- Past Tense: Add `-ed` (walk $\rightarrow$ walked).

### Irregular Morphology
English is heavily influenced by Old English and Germanic roots, leaving many words highly irregular. They do not follow the standard suffix rules.
- **Nouns**: child $\rightarrow$ children, mouse $\rightarrow$ mice, sheep $\rightarrow$ sheep.
- **Verbs**: go $\rightarrow$ went, be $\rightarrow$ was/were, have $\rightarrow$ had.

## 6. Morphological Analysis
The NLP task of breaking down a surface word into its constituent morphemes.
Standard output format usually looks like: `word + PartOfSpeech + Features`

- `cats` $\rightarrow$ `cat + N + PL` (Noun, Plural)
- `walked` $\rightarrow$ `walk + V + PAST` (Verb, Past Tense)
- `geese` $\rightarrow$ `goose + N + PL`

## 7. Morphological Ambiguity
A single surface form can map to multiple morphological analyses.
- **"leaves"**: 
  - `leaf + N + PL` (The leaves on the tree).
  - `leave + V + 3SG` (He leaves the house).
Context is required to resolve this ambiguity, typically through Part-of-Speech tagging.

## 8. Exam Preparation
### Must Memorize
- The exact distinction between Inflectional (changes grammar, keeps POS) and Derivational (changes core meaning/POS) morphology.

### Likely Theory Question
**Question**: Analyze the word "antidisestablishmentarianism" into its stem and affixes. Is the process of adding "ism" inflectional or derivational?
**Answer**: 
- Root: `establish`
- Affixes: `anti-`, `dis-`, `-ment`, `-arian`, `-ism`.
- Adding `-ism` to "antidisestablishmentarian" is **derivational** because it creates a new noun denoting a belief system or movement from an adjective/noun, fundamentally changing the semantic category.
