# Parts of Speech

## 1. What Is Part-of-Speech Tagging?
Part-of-Speech (POS) tagging is the process of assigning a grammatical category (like noun, verb, adjective) to every single word in a text. It is a fundamental prerequisite for many downstream NLP tasks, including lemmatization, syntactic parsing, and named entity recognition.

---

## 2. The Core Word Classes
While different tagsets exist (like the famous Penn Treebank tagset which has 36 detailed tags), modern NLP often uses the Universal Dependencies (UD) tagset, which provides a simplified, cross-linguistic standard.

### Open Class Words
These classes constantly acquire new words as culture and technology evolve (e.g., "to google", "a selfie").
- **Noun (NOUN)**: A person, place, thing, or abstract idea (e.g., *cat*, *freedom*, *Google*).
- **Verb (VERB)**: An action, occurrence, or state of being (e.g., *run*, *is*, *happened*).
- **Adjective (ADJ)**: Modifies or describes a noun (e.g., *red*, *quick*, *tall*).
- **Adverb (ADV)**: Modifies a verb, adjective, or other adverb (e.g., *quickly*, *very*).

### Closed Class Words
These are structural/function words. It is extremely rare for a language to invent a new one.
- **Pronoun (PRON)**: Substitutes for a noun (e.g., *he*, *she*, *it*, *they*).
- **Determiner (DET)**: Precedes a noun to express reference or quantity (e.g., *the*, *a*, *an*, *this*, *every*).
- **Preposition / Adposition (ADP)**: Indicates relationship (often spatial/temporal) between a noun and another word (e.g., *in*, *on*, *before*).
- **Conjunction (CCONJ/SCONJ)**: Connects words, phrases, or clauses (e.g., *and*, *but*, *because*).
- **Numeral (NUM)**: Expresses a number (e.g., *one*, *123*).
- **Particle (PART)**: Function words that must be associated with another word to impart meaning (e.g., *not*, or the *to* in "to run").

---

## 3. POS Ambiguity
If every word had only one POS, tagging would just be a simple Python dictionary lookup. However, English is highly ambiguous. Many words belong to multiple POS categories depending entirely on their context.

### The "Back" Problem
Consider the word **"back"**:
| Usage | POS Tag | Sentence |
| :--- | :--- | :--- |
| **Noun** | NOUN | "My **back** hurts." |
| **Adverb** | ADV | "Go **back**." |
| **Verb** | VERB | "I will **back** the project." |
| **Adjective** | ADJ | "The **back** door." |

Because of this ambiguity, POS tagging cannot be done at the isolated word level; it must be treated as a **Sequence Labeling** problem where the mathematical probability of surrounding words and tags is used to resolve the ambiguity.

---

## 4. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Distinguish between Open Class and Closed Class words in linguistics. Provide two examples of POS categories for each class. Why are closed classes important for syntactic parsing?
> **Answer**: 
> - **Open Class** words easily accept new members as language evolves. They carry the primary semantic weight of a sentence. Examples: Nouns (e.g., "iPhone") and Verbs (e.g., "to tweet").
> - **Closed Class** words are a fixed, relatively small set of grammatical function words. Languages rarely invent new ones. Examples: Determiners (e.g., "the") and Prepositions (e.g., "under").
> - **Importance for Parsing**: Closed class words form the rigid grammatical skeleton of a sentence. Because their behavior is highly predictable, syntactic parsers rely heavily on them to determine phrase boundaries (e.g., a Determiner almost always signals the start of a Noun Phrase).

**2-Mark Question**: Provide a sentence where the word "saw" is used as a noun, and another where it is used as a verb.
> **Answer**: 
> - Noun: "I used a **saw** to cut the wood."
> - Verb: "I **saw** the man."

---

### Can You Explain This?
- [ ] I can list the 4 Open Class POS categories.
- [ ] I can list at least 3 Closed Class POS categories.
- [ ] I can explain why POS tagging requires analyzing the entire sequence rather than just isolated dictionary lookups.
