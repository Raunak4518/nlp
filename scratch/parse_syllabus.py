import re

raw_text = """
1. NLP Fundamentals
14/24 complete

What is Natural Language Processing
NOTES

Natural vs programming language
EXPAND

Why natural language is difficult
EXPAND

Ambiguity
EXPAND

Context and variability
EXPAND

Spoken vs written language
NOTES

Filler words and disfluencies
NOTES

NLP vs AI vs ML vs Deep Learning
EXPAND

Computational linguistics
EXPAND

Training, validation, testing and inference
EXPAND

Inductive bias
NOTES

NLP tasks: language modeling
NOTES

Text classification
NOTES

Sequence labeling/tagging
NOTES

Sequence generation
NOTES

Machine translation
NOTES

Speech recognition
NOTES

Text-to-speech
NOTES

Summarization
NOTES

Speaker identification
NOTES

Sentiment analysis
NOTES

Chatbots
NOTES

Code assistants
NOTES

NLP applications and pipeline overview
NOTES
2. NLP Pipeline & Preprocessing
0/16 complete

Data collection
NOTES

Train/test split
NOTES

Validation set
EXPAND

Data leakage
EXPAND

Text cleaning
EXPAND

Normalization
NOTES

Lowercasing / uppercasing
NOTES

Whitespace normalization
EXPAND

Punctuation normalization
EXPAND

Unicode normalization
EXPAND

Numbers, URLs, emails, hashtags and mentions
EXPAND

Special-character handling
EXPAND

Vocabulary construction
NOTES

Feature engineering
NOTES

Model training
NOTES

Model evaluation
NOTES
3. Tokenization
0/16 complete

Definition and purpose of tokenization
NOTES

Character units
NOTES

Word units
NOTES

Sentence units
NOTES

Paragraph/document/corpus
NOTES

Whitespace tokenization
SCRATCH

Punctuation tokenization
SCRATCH

Regex-based tokenization
SCRATCH

Sentence segmentation
SCRATCH

Sentence boundary markers
NOTES

Handling abbreviations such as Dr./Mr./Mrs.
EXPAND

Character tokenization
SCRATCH

Word tokenization
SCRATCH

Subword tokenization
EXPAND

N-gram tokenization
SCRATCH

Unknown-token handling (<UNK>)
EXPAND
4. Regular Expressions
0/31 complete

Regex fundamentals
SCRATCH

Literal characters
SCRATCH

Wildcard .
SCRATCH

Character classes []
SCRATCH

Ranges [a-z], [A-Z], [0-9]
SCRATCH

Negated classes [^...]
SCRATCH

Quantifier *
SCRATCH

Quantifier +
SCRATCH

Quantifier ?
SCRATCH

{m,n} repetition
SCRATCH

Grouping ()
SCRATCH

Alternation |
SCRATCH

Start/end anchors ^ and $
SCRATCH

Escaping special characters
SCRATCH

\d / \D
SCRATCH

\w / \W
SCRATCH

\s / \S
SCRATCH

Greedy matching
SCRATCH

Non-greedy matching
SCRATCH

search()
SCRATCH

match()
SCRATCH

findall()
SCRATCH

finditer()
SCRATCH

sub() / substitution
SCRATCH

split()
SCRATCH

Capturing groups
SCRATCH

Regex for email extraction
SCRATCH

Regex for URL extraction
SCRATCH

Regex for phone/date/number extraction
SCRATCH

Regex for sentence boundaries
SCRATCH

Regex and finite automata relationship
EXPAND
5. Finite State Automata
0/19 complete

Finite State Automaton definition
NOTES

Formal tuple M=(Q,Σ,δ,q0,F)
EXPAND

States
NOTES

Alphabet
NOTES

Initial state
NOTES

Accepting/final states
NOTES

Transition function
NOTES

DFA definition
NOTES

DFA transition table
NOTES

DFA state-diagram construction
SCRATCH

DFA string acceptance
SCRATCH

NFA definition
NOTES

NFA multiple transitions
NOTES

Epsilon transitions
NOTES

NFA string acceptance
SCRATCH

DFA vs NFA
NOTES

Regex → automaton concept
EXPAND

Implement a generic DFA recognizer from scratch
SCRATCH

Implement an NFA recognizer from scratch
SCRATCH
6. Finite State Transducers & Morphology
0/21 complete

Finite State Transducer (FST)
NOTES

Input/output transitions
NOTES

Morphology definition
NOTES

Morph
NOTES

Morpheme
NOTES

Root and stem
NOTES

Affixes
NOTES

Inflectional morphology
NOTES

Derivational morphology
NOTES

Inflection vs derivation
NOTES

Number/tense/person/case/agreement
EXPAND

Morphological analysis
NOTES

Morphological generation
NOTES

cat → cat + N + SG/PL style analysis
SCRATCH

Verb morphology: walk/walked/walking
SCRATCH

Plural rules: cat/cats, box/boxes
SCRATCH

Irregular morphology: child/children, mouse/mice
SCRATCH

Irregular verbs: go/went, be/was, have/had
SCRATCH

Morphological ambiguity
EXPAND

FST-based morphological analyzer
SCRATCH

FST-based morphological generator
SCRATCH
7. Stemming & Lemmatization
0/12 complete

Stemming definition
NOTES

Rule-based stemming
SCRATCH

Suffix stripping
SCRATCH

Porter Stemmer concept
EXPAND

Snowball Stemmer concept
EXPAND

Lancaster Stemmer concept
EXPAND

Lemmatization definition
NOTES

Dictionary-based lemmatization
SCRATCH

Rule-based lemmatization
SCRATCH

POS-aware lemmatization
EXPAND

Stemming vs lemmatization
NOTES

Irregular lemma examples
EXPAND
8. POS Tagging & Sequence Labeling
0/21 complete

Part-of-speech tagging
NOTES

Noun
NOTES

Verb
NOTES

Adjective
NOTES

Adverb
NOTES

Pronoun
NOTES

Determiner
NOTES

Preposition
NOTES

Conjunction
NOTES

Interjection
NOTES

Particle
EXPAND

Numeral
EXPAND

Punctuation tags
NOTES

POS ambiguity
EXPAND

Rule-based POS tagger
SCRATCH

Sequence labeling
NOTES

Sequence classification vs sequence labeling
EXPAND

BIO encoding
SCRATCH

BILOU encoding
EXPAND

HMM POS tagging
SCRATCH

Viterbi algorithm
SCRATCH
9. Named Entity Recognition
0/12 complete

NER definition
NOTES

PERSON
NOTES

LOCATION/LOC
NOTES

ORGANIZATION/ORG
NOTES

DATE
NOTES

MONEY
NOTES

PRODUCT
NOTES

EVENT
NOTES

BIO tagging for NER
SCRATCH

Rule-based NER
SCRATCH

NER evaluation
EXPAND

Entity linking concept
EXPAND
10. Language Identification
0/5 complete

Language identification definition
NOTES

Character n-gram language model
SCRATCH

Language profiles
SCRATCH

Likelihood/similarity-based classification
SCRATCH

Unknown language handling
EXPAND
11. Parsing & Grammar
0/26 complete

Parsing definition
NOTES

Grammar
NOTES

Context-Free Grammar (CFG)
NOTES

Terminal
NOTES

Non-terminal
NOTES

Start symbol
NOTES

Production rule
NOTES

Derivation
EXPAND

Leftmost derivation
EXPAND

Rightmost derivation
EXPAND

Parse tree
NOTES

Constituency parsing
NOTES

Bracketing
NOTES

Ambiguous grammar/sentence
NOTES

Resolving ambiguity with grammar
NOTES

Recursive-descent parsing
SCRATCH

Top-down parsing
EXPAND

Bottom-up parsing
EXPAND

CYK parsing
SCRATCH

Earley parsing concept
EXPAND

Dependency parsing
EXPAND

Head/dependent
EXPAND

Dependency relations
EXPAND

Root node
EXPAND

CoNLL format
NOTES

CoNLL columns and representation
SCRATCH
12. TF-IDF & Vector Representations
0/11 complete

Bag of Words
EXPAND

Count vector
SCRATCH

Binary word features
EXPAND

Term Frequency (TF)
SCRATCH

Document Frequency (DF)
SCRATCH

Inverse Document Frequency (IDF)
SCRATCH

TF-IDF
SCRATCH

TF-IDF numerical calculation
NUMERICAL

Vector normalization
EXPAND

Cosine similarity
SCRATCH

Cosine similarity numerical problems
NUMERICAL
13. Probability Foundations
0/10 complete

Probability basics
EXPAND

Joint probability
EXPAND

Conditional probability
NOTES

Marginal probability
EXPAND

Bayes theorem
EXPAND

Chain rule
NOTES

Relative frequency
NOTES

Maximum Likelihood Estimation (MLE)
NOTES

Probability normalization
EXPAND

Probability numerical problems
NUMERICAL
14. N-gram Language Models
0/21 complete

Language model definition
NOTES

Next-token prediction
NOTES

Unigram
NOTES

Bigram
NOTES

Trigram
NOTES

4-gram / general N-gram
NOTES

Word N-grams
SCRATCH

Character N-grams
SCRATCH

N-gram count generation
SCRATCH

Number of n-grams = N-n+1
NUMERICAL

Vocabulary size
NOTES

<s> start marker
NOTES

</s> end marker
NOTES

<UNK> unknown token
EXPAND

MLE unigram probability
SCRATCH

MLE bigram probability
SCRATCH

MLE trigram probability
SCRATCH

Sentence probability
SCRATCH

Next-word prediction using argmax
SCRATCH

Random sentence generation
SCRATCH

N-gram probability numericals
NUMERICAL
15. Sparsity & Zero-Probability Problem
0/8 complete

Data sparsity
NOTES

Unseen N-grams
NOTES

Zero probability
NOTES

Zero probability causing sentence probability = 0
NOTES

Vocabulary explosion V²/V³/Vⁿ
EXPAND

Unknown words
EXPAND

Why smoothing is necessary
NOTES

Sparse count tables
EXPAND
16. Laplace & Add-k Smoothing
0/15 complete

Laplace / Add-one smoothing
NOTES

Laplace formula
NOTES

Why +1 is added
EXPAND

Why denominator becomes +V
EXPAND

Seen-event probability after Laplace
NUMERICAL

Unseen-event probability after Laplace
NUMERICAL

Laplace limitations
EXPAND

Implement Laplace smoothing from scratch
SCRATCH

Add-k smoothing
NOTES

Add-k formula
NOTES

Choosing k
NOTES

Grid search for k
NOTES

Validation-set selection of k
EXPAND

Implement Add-k from scratch
SCRATCH

Add-k numerical problems
NUMERICAL
17. Interpolation
0/10 complete

Linear interpolation
NOTES

Unigram + bigram + trigram interpolation
NOTES

Interpolation weights λ
NOTES

λ1 + λ2 + λ3 = 1
NOTES

Fixed interpolation
EXPAND

Deleted interpolation
NOTES

Estimating interpolation weights
SCRATCH

Held-out data
NOTES

Interpolation numerical problems
NUMERICAL

Interpolation vs backoff
EXPAND
18. Good-Turing Smoothing
0/12 complete

Good-Turing intuition
NOTES

Frequency of frequencies
NOTES

N1, N2, N3, ...
NOTES

Adjusted count c*
NOTES

c* = (c+1)N(c+1)/N(c)
NOTES

Probability of unseen events
NOTES

Good-Turing numerical calculations
NUMERICAL

Good-Turing regression
NOTES

log N_c = a + b log c concept
NOTES

Fit regression for Good-Turing
SCRATCH

Good-Turing implementation from scratch
SCRATCH

Limitations of raw Good-Turing
EXPAND
19. Witten-Bell Smoothing
0/7 complete

Witten-Bell intuition
NOTES

Observed tokens N
NOTES

Observed types T
NOTES

Seen vs unseen events
NOTES

Witten-Bell probability
NOTES

Witten-Bell numerical problems
NUMERICAL

Implement Witten-Bell from scratch
SCRATCH
20. Backoff & Discounting
0/18 complete

Backoff concept
NOTES

Trigram → bigram → unigram
NOTES

Seen vs unseen N-gram handling
NOTES

Discounting
NOTES

Absolute discounting
NOTES

C* = C-D
NOTES

Estimating discount D
NOTES

Backoff probability
NOTES

Katz backoff
NOTES

Katz discounted probability
NOTES

Katz backoff weight
NOTES

Katz numerical problems
NUMERICAL

Implement Katz backoff from scratch
SCRATCH

Stupid backoff
NOTES

Stupid backoff implementation
SCRATCH

Backoff vs interpolation
EXPAND

Absolute discounting implementation
SCRATCH

Absolute discounting numerical problems
NUMERICAL
21. Kneser-Ney Smoothing
0/13 complete

Why Kneser-Ney exists
NOTES

Continuation probability
NOTES

Context diversity
NOTES

Continuation count
NOTES

Bigram Kneser-Ney
NOTES

Interpolated Kneser-Ney
NOTES

Recursive Kneser-Ney
NOTES

Absolute discounting inside Kneser-Ney
NOTES

Higher-order Kneser-Ney
NOTES

Kneser-Ney numerical problems
NUMERICAL

Implement bigram Kneser-Ney from scratch
SCRATCH

Implement interpolated Kneser-Ney
SCRATCH

Implement recursive Kneser-Ney
SCRATCH
22. Zipf's Law & Frequency Distributions
0/7 complete

Zipf's law
NOTES

Rank-frequency relationship
NOTES

Power-law distribution
NOTES

Frequency ∝ 1/rank
NOTES

Log-log representation
NOTES

Zipf numerical problems
NUMERICAL

Connection to vocabulary and sparsity
EXPAND
23. Perplexity & Language Model Evaluation
0/9 complete

Log probability
EXPAND

Cross entropy
EXPAND

Perplexity definition
ADDED

PP = P(W)^(-1/N)
ADDED

Perplexity from log probabilities
SCRATCH

Why zero probability breaks perplexity
EXPAND

Compare two language models by perplexity
NUMERICAL

Intrinsic evaluation
EXPAND

Extrinsic evaluation
EXPAND
24. Byte Pair Encoding (BPE)
0/16 complete

Why subword tokenization is needed
NOTES

Character-level starting representation
NOTES

Word-level vs subword-level representation
NOTES

BPE algorithm
NOTES

Count adjacent symbol pairs
NOTES

Find most frequent pair
NOTES

Merge most frequent pair
NOTES

Update vocabulary
NOTES

Repeat merges
NOTES

Stopping condition
NOTES

BPE numerical/manual problems
NUMERICAL

Implement pair counting from scratch
SCRATCH

Implement pair merging from scratch
SCRATCH

Implement complete BPE trainer from scratch
SCRATCH

BPE vs WordPiece
EXPAND

BPE vs Unigram LM
EXPAND
25. Text Classification
0/16 complete

Text classification
NOTES

Spam/not-spam example
EXPAND

Count/BOW features
EXPAND

TF-IDF features
EXPAND

Naive Bayes
ADDED

Multinomial Naive Bayes
ADDED

Laplace smoothing in Naive Bayes
ADDED

Naive Bayes from scratch
SCRATCH

Logistic regression concept
ADDED

Confusion matrix
EXPAND

TP/TN/FP/FN
EXPAND

Accuracy
EXPAND

Precision
EXPAND

Recall
EXPAND

F1 score
EXPAND

Macro-F1 vs Micro-F1
EXPAND
26. Sentiment Analysis
0/6 complete

Sentiment analysis
NOTES

Positive/negative classification
NOTES

Lexicon-based sentiment
ADDED

Lexicon classifier from scratch
SCRATCH

Naive Bayes sentiment classifier
ADDED

Sentiment evaluation
EXPAND
27. Sequence Generation
0/7 complete

Autoregressive generation
NOTES

Next-token prediction
NOTES

Greedy decoding
EXPAND

Random sampling
EXPAND

Temperature
ADDED

Beam search
ADDED

Beam search from scratch
SCRATCH
28. Machine Translation & Speech
0/11 complete

Machine translation
NOTES

Source and target language
EXPAND

Rule-based translation concept
ADDED

Statistical machine translation concept
ADDED

Neural machine translation concept
ADDED

Sequence-to-sequence concept
ADDED

Automatic speech recognition
NOTES

Speech → text
NOTES

Text → speech
NOTES

Speaker identification
NOTES

Phonetics/phonemes
ADDED
29. Summarization, QA & Information Extraction
0/10 complete

Extractive summarization
NOTES

Sentence scoring
ADDED

Sentence scoring implementation
SCRATCH

Abstractive summarization concept
ADDED

Question answering
NOTES

Retrieval-based QA
ADDED

Generative QA
ADDED

Information extraction
EXPAND

Relation extraction
ADDED

Entity linking
ADDED
30. Evaluation & Metrics
0/10 complete

Language-model evaluation
EXPAND

Perplexity
ADDED

Classification accuracy
EXPAND

Precision
EXPAND

Recall
EXPAND

F1
EXPAND

Sequence-labeling token accuracy
EXPAND

Entity-level NER precision/recall/F1
EXPAND

BLEU concept
ADDED

ROUGE concept
ADDED
31. Final Scratch-Implementation Projects
0/20 complete

Complete tokenizer without NLP libraries
SCRATCH

Complete regex tokenizer
SCRATCH

Complete DFA/NFA recognizer
SCRATCH

Complete morphology FST
SCRATCH

Complete POS tagger
SCRATCH

Complete CFG parser
SCRATCH

Complete TF-IDF engine
SCRATCH

Complete N-gram language model
SCRATCH

Sentence probability calculator
SCRATCH

Next-token predictor
SCRATCH

Perplexity calculator
SCRATCH

Laplace + Add-k framework
SCRATCH

Good-Turing implementation
SCRATCH

Witten-Bell implementation
SCRATCH

Katz backoff implementation
SCRATCH

Absolute discounting implementation
SCRATCH

Kneser-Ney implementation
SCRATCH

BPE tokenizer trainer
SCRATCH

Naive Bayes classifier
SCRATCH

HMM + Viterbi sequence tagger
SCRATCH
"""

lines = raw_text.splitlines()

syllabus = ["# NLP Syllabus\n"]

current_major_id = None
current_sub_idx = 1

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    
    # Check if it's a major topic
    m = re.match(r'^(\d+)\.\s+(.*)$', line)
    if m:
        current_major_id = m.group(1)
        major_name = m.group(2)
        syllabus.append(f"## {current_major_id}. {major_name}")
        current_sub_idx = 1
        continue
    
    # Check if it's "x/y complete"
    if "complete" in line and "/" in line:
        continue
        
    # Check if it's one of the tags like NOTES, EXPAND, SCRATCH, NUMERICAL, ADDED
    if line in ["NOTES", "EXPAND", "SCRATCH", "NUMERICAL", "ADDED"]:
        continue
        
    if current_major_id:
        syllabus.append(f"### {current_major_id}.{current_sub_idx} {line}")
        current_sub_idx += 1

with open("SYLLABUS.md", "w", encoding="utf-8") as f:
    f.write("\n".join(syllabus))
