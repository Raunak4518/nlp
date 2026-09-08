# Parts of Speech

## 1. What Is Part-of-Speech Tagging?
Part-of-Speech (POS) tagging is the process of assigning a grammatical category (like noun, verb, adjective) to each word in a text. It is a fundamental prerequisite for many downstream NLP tasks, including lemmatization, syntactic parsing, and named entity recognition.

## 2. The Core Word Classes
While different tagsets exist (like the Penn Treebank tagset which has 36 tags), the Universal Dependencies tagset uses a simplified, cross-linguistic set.

### Open Class Words
These classes constantly acquire new words as language evolves.
- **Noun (NOUN)**: A person, place, thing, or abstract idea (e.g., *cat*, *freedom*, *Google*).
- **Verb (VERB)**: An action, occurrence, or state of being (e.g., *run*, *is*, *happened*).
- **Adjective (ADJ)**: Modifies or describes a noun (e.g., *red*, *quick*, *tall*).
- **Adverb (ADV)**: Modifies a verb, adjective, or other adverb (e.g., *quickly*, *very*).

### Closed Class Words
These are structural words. It is extremely rare for a language to invent a new one.
- **Pronoun (PRON)**: Substitutes for a noun (e.g., *he*, *she*, *it*, *they*).
- **Determiner (DET)**: Precedes a noun to express reference or quantity (e.g., *the*, *a*, *an*, *this*, *every*).
- **Preposition / Adposition (ADP)**: Indicates relationship (often spatial/temporal) between a noun and another word (e.g., *in*, *on*, *before*).
- **Conjunction (CONJ/SCONJ/CCONJ)**: Connects words, phrases, or clauses (e.g., *and*, *but*, *because*).
- **Interjection (INTJ)**: Expresses emotion (e.g., *oh*, *wow*, *ouch*).
- **Numeral (NUM)**: Expresses a number (e.g., *one*, *123*).
- **Particle (PART)**: Function words that must be associated with another word to impart meaning (e.g., *not*, or the *to* in "to run").

### Punctuation Tags
Punctuation marks (like `.`, `,`, `!`) are usually assigned their own specific POS tags in NLP pipelines.

## 3. POS Ambiguity
If every word had only one POS, tagging would just be a dictionary lookup. However, English is highly ambiguous. Many words belong to multiple POS categories depending on their context.

- **"Back"**
  - Noun: "My **back** hurts."
  - Adverb: "Go **back**."
  - Verb: "I will **back** the project."
  - Adjective: "The **back** door."
- **"Saw"**
  - Verb: "I **saw** the man."
  - Noun: "I used a **saw** to cut the wood."

Because of this ambiguity, POS tagging cannot be done at the isolated word level; it must be treated as a **Sequence Labeling** problem where the surrounding context is used to resolve the ambiguity.

## 4. Exam Preparation
### Must Memorize
- The difference between Open Class (nouns, verbs, adjectives, adverbs) and Closed Class (prepositions, determiners, pronouns) words.

### Likely Theory Question
**Question**: Provide a sentence where the word "book" is used as a noun, and another where it is used as a verb. Why does this pose a problem for simple dictionary-based NLP systems?
**Answer**: 
- Noun: "I read a **book**."
- Verb: "I need to **book** a flight."
This poses a problem because a simple dictionary lookup cannot determine the grammatical role or semantic meaning of the word. The system must analyze the surrounding sequence (e.g., identifying that "to" precedes "book") to accurately assign the POS tag.
