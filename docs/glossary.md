# Global NLP Glossary

This dictionary provides quick definitions and intuitive explanations for the most critical NLP terminology used across this textbook. 

---

### A
- **Abstractive Summarization**  
  **Definition**: Generating a new, concise summary that may use words not found in the original document.  
  **Intuition**: Like a human writing a book report in their own words.  

- **Acoustic Model**  
  **Definition**: In speech recognition, the model that maps audio waveforms to phonemes.  
  **Intuition**: The "ear" of the speech recognition system.  

- **Add-k Smoothing**  
  **Definition**: A technique to solve the zero-probability problem by adding a fractional constant $k$ to all n-gram counts.  
  **Intuition**: Don't just give unseen words zero probability; assume you saw everything at least a tiny fraction of a time.  

- **Autoregressive Generation**  
  **Definition**: A modeling paradigm where the model predicts the next token in a sequence based on the previously generated tokens.  
  **Intuition**: Writing a sentence one word at a time, looking back at what you've written so far.

---

### B
- **Bag of Words (BoW)**  
  **Definition**: A representation of text that counts the frequency of words but completely ignores their order or grammar.  
  **Intuition**: Dumping all the words of a sentence into a bag; you know what's in there, but you don't know how they were arranged.  

- **Beam Search**  
  **Definition**: A decoding algorithm that maintains the top $K$ most probable sequences at each step to find a mathematically optimal output sequence.  
  **Intuition**: Instead of blindly picking the best next step (Greedy), keeping your options open to avoid walking into a dead end.

- **Bilingual Evaluation Understudy (BLEU)**  
  **Definition**: A metric used to evaluate Machine Translation by measuring n-gram overlap between machine output and human references.  
  **Intuition**: Grading a translation based on how many "chunks" of words perfectly match the human's answer key.

- **Byte Pair Encoding (BPE)**  
  **Definition**: A subword tokenization algorithm that iteratively merges the most frequent pairs of characters.  
  **Intuition**: Treating common syllables as their own letters to shrink the vocabulary size and handle unknown words.

---

### C
- **Context-Free Grammar (CFG)**  
  **Definition**: A set of recursive rules (e.g., $S \rightarrow NP \ VP$) used to generate and parse the syntactic structure of sentences.  
  **Intuition**: The mathematical rules of sentence diagramming.

- **Cosine Similarity**  
  **Definition**: A metric that calculates the cosine of the angle between two vectors to determine their similarity, ignoring magnitude.  
  **Intuition**: Checking if two arrows point in the exact same direction, regardless of how long the arrows are.

---

### D
- **Dependency Parsing**  
  **Definition**: Analyzing the grammatical structure of a sentence by establishing direct binary relationships (dependencies) between "head" words and "dependent" words.  
  **Intuition**: Drawing arrows from verbs to their subjects and objects to show who did what to whom.

---

### E
- **Entity Linking**  
  **Definition**: Disambiguating a named entity identified in text by linking it to a specific unique identifier in a knowledge base (e.g., Wikipedia).  
  **Intuition**: Knowing that the "Apple" in the sentence refers specifically to `Apple_Inc` and not the fruit.

- **Extractive Summarization**  
  **Definition**: Creating a summary by selecting and copying the most important existing sentences directly from the source text.  
  **Intuition**: Using a highlighter pen on a textbook.

---

### F
- **Finite State Automaton (FSA)**  
  **Definition**: A theoretical machine consisting of states and transitions used to recognize patterns in text (the math behind regular expressions).  
  **Intuition**: A subway turnstile that changes state based on whether you push or insert a coin.

- **Finite State Transducer (FST)**  
  **Definition**: An FSA that not only accepts/rejects input but outputs a transformed sequence.  
  **Intuition**: A machine that translates plural words into singular ones on the fly.

---

### G
- **Good-Turing Smoothing**  
  **Definition**: A method for estimating the probability of unseen n-grams by looking at the frequency of n-grams that occurred exactly once.  
  **Intuition**: "The probability of seeing something completely new is roughly equal to the fraction of things I have only seen exactly once so far."

- **Greedy Decoding**  
  **Definition**: Always selecting the single token with the highest immediate probability during autoregressive generation.  
  **Intuition**: Making the best short-term choice without looking ahead.

---

### H
- **Hidden Markov Model (HMM)**  
  **Definition**: A statistical model where the system being modeled is assumed to be a Markov process with unobservable ("hidden") states.  
  **Intuition**: Trying to guess the weather (hidden) just by looking at whether a person is carrying an umbrella (observed).

---

### K
- **Kneser-Ney Smoothing**  
  **Definition**: An advanced smoothing algorithm that relies on Absolute Discounting and the "continuation probability" of a word.  
  **Intuition**: A word should be considered likely in a novel context only if it naturally appears after many *different* types of words, not just because it has a high absolute frequency.

---

### L
- **Lemmatization**  
  **Definition**: Reducing a word to its proper dictionary base form (lemma) using vocabulary and morphological analysis.  
  **Intuition**: Knowing that "better" maps to "good" because you actually checked the dictionary.

- **Log Probability**  
  **Definition**: The logarithm of a probability. Used to prevent arithmetic underflow when multiplying many tiny fractions.  
  **Intuition**: Adding negative numbers instead of multiplying tiny decimals so the computer's memory doesn't break.

---

### N
- **Named Entity Recognition (NER)**  
  **Definition**: The task of identifying and classifying proper nouns (people, organizations, locations) in a text.  
  **Intuition**: Scanning a document to highlight all the names and places.

- **Noisy Channel Model**  
  **Definition**: A framework that treats tasks like spell-correction, translation, and speech recognition as recovering an original intended message that was corrupted by "noise".  
  **Intuition**: You meant to type "the", the keyboard added noise and produced "teh", and the model uses Bayes' theorem to figure out what you meant.

---

### O
- **Out-of-Vocabulary (OOV)**  
  **Definition**: A token that appears during testing or deployment that was not present in the model's training dictionary.  
  **Intuition**: A word the model has literally never seen before.

---

### P
- **Perplexity**  
  **Definition**: The standard evaluation metric for language models. The inverse probability of the test set, normalized by the number of words.  
  **Intuition**: How "surprised" the model is by the actual next word in a sentence. Lower perplexity means the model is less surprised (better).

- **Phoneme**  
  **Definition**: The smallest distinct unit of sound in a language.  
  **Intuition**: The "c" in cat and the "k" in kite are the exact same phoneme (/k/).

- **Precision**  
  **Definition**: The percentage of positive predictions made by the model that were actually correct. ($TP / (TP + FP)$).  
  **Intuition**: "Out of all the emails you threw in the spam folder, how many were actually spam?"

---

### R
- **Recall**  
  **Definition**: The percentage of actual positive instances the model successfully found. ($TP / (TP + FN)$).  
  **Intuition**: "Out of all the spam emails that actually exist, how many did you catch?"

- **Recall-Oriented Understudy for Gisting Evaluation (ROUGE)**  
  **Definition**: A metric used to evaluate summarization by measuring n-gram recall against a human reference.  
  **Intuition**: Did the machine summary capture all the important concepts the human summary had?

---

### S
- **Sequence-to-Sequence (Seq2Seq)**  
  **Definition**: A neural network architecture comprising an Encoder and a Decoder, designed to transform an input sequence into a different output sequence.  
  **Intuition**: The underlying architecture for Machine Translation and Summarization.

- **Stemming**  
  **Definition**: Reducing a word to its base form by blindly chopping off the end of the word using a heuristic rule set (like the Porter Stemmer).  
  **Intuition**: Chopping the "ing" off "running" to get "run" (fast, but sometimes chops off too much).

---

### T
- **Term Frequency-Inverse Document Frequency (TF-IDF)**  
  **Definition**: A numerical statistic that reflects how important a word is to a document within a larger corpus.  
  **Intuition**: A word is important if it appears many times in *this* document, but rarely in the *rest* of the library.

---

### V
- **Viterbi Algorithm**  
  **Definition**: A dynamic programming algorithm used to find the most likely sequence of hidden states (the Viterbi path) in an HMM.  
  **Intuition**: Efficiently finding the best path through a maze without having to explore every single dead end.

---

### Z
- **Zipf's Law**  
  **Definition**: An empirical law stating that the frequency of any word is inversely proportional to its rank in the frequency table. ($f \propto 1/r$).  
  **Intuition**: A tiny handful of words (like "the") account for the vast majority of all text, while most words appear only once.
