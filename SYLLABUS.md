# NLP Syllabus

## 1. NLP Fundamentals
### 1.1 What is Natural Language Processing
### 1.2 Natural vs programming language
### 1.3 Why natural language is difficult
### 1.4 Ambiguity
### 1.5 Context and variability
### 1.6 Spoken vs written language
### 1.7 Filler words and disfluencies
### 1.8 NLP vs AI vs ML vs Deep Learning
### 1.9 Computational linguistics
### 1.10 Training, validation, testing and inference
### 1.11 Inductive bias
### 1.12 NLP tasks: language modeling
### 1.13 Text classification
### 1.14 Sequence labeling/tagging
### 1.15 Sequence generation
### 1.16 Machine translation
### 1.17 Speech recognition
### 1.18 Text-to-speech
### 1.19 Summarization
### 1.20 Speaker identification
### 1.21 Sentiment analysis
### 1.22 Chatbots
### 1.23 Code assistants
### 1.24 NLP applications and pipeline overview
## 2. NLP Pipeline & Preprocessing
### 2.1 Data collection
### 2.2 Train/test split
### 2.3 Validation set
### 2.4 Data leakage
### 2.5 Text cleaning
### 2.6 Normalization
### 2.7 Lowercasing / uppercasing
### 2.8 Whitespace normalization
### 2.9 Punctuation normalization
### 2.10 Unicode normalization
### 2.11 Numbers, URLs, emails, hashtags and mentions
### 2.12 Special-character handling
### 2.13 Vocabulary construction
### 2.14 Feature engineering
### 2.15 Model training
### 2.16 Model evaluation
## 3. Tokenization
### 3.1 Definition and purpose of tokenization
### 3.2 Character units
### 3.3 Word units
### 3.4 Sentence units
### 3.5 Paragraph/document/corpus
### 3.6 Whitespace tokenization
### 3.7 Punctuation tokenization
### 3.8 Regex-based tokenization
### 3.9 Sentence segmentation
### 3.10 Sentence boundary markers
### 3.11 Handling abbreviations such as Dr./Mr./Mrs.
### 3.12 Character tokenization
### 3.13 Word tokenization
### 3.14 Subword tokenization
### 3.15 N-gram tokenization
### 3.16 Unknown-token handling (<UNK>)
## 4. Regular Expressions
### 4.1 Regex fundamentals
### 4.2 Literal characters
### 4.3 Wildcard .
### 4.4 Character classes []
### 4.5 Ranges [a-z], [A-Z], [0-9]
### 4.6 Negated classes [^...]
### 4.7 Quantifier *
### 4.8 Quantifier +
### 4.9 Quantifier ?
### 4.10 {m,n} repetition
### 4.11 Grouping ()
### 4.12 Alternation |
### 4.13 Start/end anchors ^ and $
### 4.14 Escaping special characters
### 4.15 \d / \D
### 4.16 \w / \W
### 4.17 \s / \S
### 4.18 Greedy matching
### 4.19 Non-greedy matching
### 4.20 search()
### 4.21 match()
### 4.22 findall()
### 4.23 finditer()
### 4.24 sub() / substitution
### 4.25 split()
### 4.26 Capturing groups
### 4.27 Regex for email extraction
### 4.28 Regex for URL extraction
### 4.29 Regex for phone/date/number extraction
### 4.30 Regex for sentence boundaries
### 4.31 Regex and finite automata relationship
## 5. Finite State Automata
### 5.1 Finite State Automaton definition
### 5.2 Formal tuple M=(Q,Σ,δ,q0,F)
### 5.3 States
### 5.4 Alphabet
### 5.5 Initial state
### 5.6 Accepting/final states
### 5.7 Transition function
### 5.8 DFA definition
### 5.9 DFA transition table
### 5.10 DFA state-diagram construction
### 5.11 DFA string acceptance
### 5.12 NFA definition
### 5.13 NFA multiple transitions
### 5.14 Epsilon transitions
### 5.15 NFA string acceptance
### 5.16 DFA vs NFA
### 5.17 Regex → automaton concept
### 5.18 Implement a generic DFA recognizer from scratch
### 5.19 Implement an NFA recognizer from scratch
## 6. Finite State Transducers & Morphology
### 6.1 Finite State Transducer (FST)
### 6.2 Input/output transitions
### 6.3 Morphology definition
### 6.4 Morph
### 6.5 Morpheme
### 6.6 Root and stem
### 6.7 Affixes
### 6.8 Inflectional morphology
### 6.9 Derivational morphology
### 6.10 Inflection vs derivation
### 6.11 Number/tense/person/case/agreement
### 6.12 Morphological analysis
### 6.13 Morphological generation
### 6.14 cat → cat + N + SG/PL style analysis
### 6.15 Verb morphology: walk/walked/walking
### 6.16 Plural rules: cat/cats, box/boxes
### 6.17 Irregular morphology: child/children, mouse/mice
### 6.18 Irregular verbs: go/went, be/was, have/had
### 6.19 Morphological ambiguity
### 6.20 FST-based morphological analyzer
### 6.21 FST-based morphological generator
## 7. Stemming & Lemmatization
### 7.1 Stemming definition
### 7.2 Rule-based stemming
### 7.3 Suffix stripping
### 7.4 Porter Stemmer concept
### 7.5 Snowball Stemmer concept
### 7.6 Lancaster Stemmer concept
### 7.7 Lemmatization definition
### 7.8 Dictionary-based lemmatization
### 7.9 Rule-based lemmatization
### 7.10 POS-aware lemmatization
### 7.11 Stemming vs lemmatization
### 7.12 Irregular lemma examples
## 8. POS Tagging & Sequence Labeling
### 8.1 Part-of-speech tagging
### 8.2 Noun
### 8.3 Verb
### 8.4 Adjective
### 8.5 Adverb
### 8.6 Pronoun
### 8.7 Determiner
### 8.8 Preposition
### 8.9 Conjunction
### 8.10 Interjection
### 8.11 Particle
### 8.12 Numeral
### 8.13 Punctuation tags
### 8.14 POS ambiguity
### 8.15 Rule-based POS tagger
### 8.16 Sequence labeling
### 8.17 Sequence classification vs sequence labeling
### 8.18 BIO encoding
### 8.19 BILOU encoding
### 8.20 HMM POS tagging
### 8.21 Viterbi algorithm
## 9. Named Entity Recognition
### 9.1 NER definition
### 9.2 PERSON
### 9.3 LOCATION/LOC
### 9.4 ORGANIZATION/ORG
### 9.5 DATE
### 9.6 MONEY
### 9.7 PRODUCT
### 9.8 EVENT
### 9.9 BIO tagging for NER
### 9.10 Rule-based NER
### 9.11 NER evaluation
### 9.12 Entity linking concept
## 10. Language Identification
### 10.1 Language identification definition
### 10.2 Character n-gram language model
### 10.3 Language profiles
### 10.4 Likelihood/similarity-based classification
### 10.5 Unknown language handling
## 11. Parsing & Grammar
### 11.1 Parsing definition
### 11.2 Grammar
### 11.3 Context-Free Grammar (CFG)
### 11.4 Terminal
### 11.5 Non-terminal
### 11.6 Start symbol
### 11.7 Production rule
### 11.8 Derivation
### 11.9 Leftmost derivation
### 11.10 Rightmost derivation
### 11.11 Parse tree
### 11.12 Constituency parsing
### 11.13 Bracketing
### 11.14 Ambiguous grammar/sentence
### 11.15 Resolving ambiguity with grammar
### 11.16 Recursive-descent parsing
### 11.17 Top-down parsing
### 11.18 Bottom-up parsing
### 11.19 CYK parsing
### 11.20 Earley parsing concept
### 11.21 Dependency parsing
### 11.22 Head/dependent
### 11.23 Dependency relations
### 11.24 Root node
### 11.25 CoNLL format
### 11.26 CoNLL columns and representation
## 12. TF-IDF & Vector Representations
### 12.1 Bag of Words
### 12.2 Count vector
### 12.3 Binary word features
### 12.4 Term Frequency (TF)
### 12.5 Document Frequency (DF)
### 12.6 Inverse Document Frequency (IDF)
### 12.7 TF-IDF
### 12.8 TF-IDF numerical calculation
### 12.9 Vector normalization
### 12.10 Cosine similarity
### 12.11 Cosine similarity numerical problems
## 13. Probability Foundations
### 13.1 Probability basics
### 13.2 Joint probability
### 13.3 Conditional probability
### 13.4 Marginal probability
### 13.5 Bayes theorem
### 13.6 Chain rule
### 13.7 Relative frequency
### 13.8 Maximum Likelihood Estimation (MLE)
### 13.9 Probability normalization
### 13.10 Probability numerical problems
## 14. N-gram Language Models
### 14.1 Language model definition
### 14.2 Next-token prediction
### 14.3 Unigram
### 14.4 Bigram
### 14.5 Trigram
### 14.6 4-gram / general N-gram
### 14.7 Word N-grams
### 14.8 Character N-grams
### 14.9 N-gram count generation
### 14.10 Number of n-grams = N-n+1
### 14.11 Vocabulary size
### 14.12 <s> start marker
### 14.13 </s> end marker
### 14.14 <UNK> unknown token
### 14.15 MLE unigram probability
### 14.16 MLE bigram probability
### 14.17 MLE trigram probability
### 14.18 Sentence probability
### 14.19 Next-word prediction using argmax
### 14.20 Random sentence generation
### 14.21 N-gram probability numericals
## 15. Sparsity & Zero-Probability Problem
### 15.1 Data sparsity
### 15.2 Unseen N-grams
### 15.3 Zero probability
### 15.4 Zero probability causing sentence probability = 0
### 15.5 Vocabulary explosion V²/V³/Vⁿ
### 15.6 Unknown words
### 15.7 Why smoothing is necessary
### 15.8 Sparse count tables
## 16. Laplace & Add-k Smoothing
### 16.1 Laplace / Add-one smoothing
### 16.2 Laplace formula
### 16.3 Why +1 is added
### 16.4 Why denominator becomes +V
### 16.5 Seen-event probability after Laplace
### 16.6 Unseen-event probability after Laplace
### 16.7 Laplace limitations
### 16.8 Implement Laplace smoothing from scratch
### 16.9 Add-k smoothing
### 16.10 Add-k formula
### 16.11 Choosing k
### 16.12 Grid search for k
### 16.13 Validation-set selection of k
### 16.14 Implement Add-k from scratch
### 16.15 Add-k numerical problems
## 17. Interpolation
### 17.1 Linear interpolation
### 17.2 Unigram + bigram + trigram interpolation
### 17.3 Interpolation weights λ
### 17.4 λ1 + λ2 + λ3 = 1
### 17.5 Fixed interpolation
### 17.6 Deleted interpolation
### 17.7 Estimating interpolation weights
### 17.8 Held-out data
### 17.9 Interpolation numerical problems
### 17.10 Interpolation vs backoff
## 18. Good-Turing Smoothing
### 18.1 Good-Turing intuition
### 18.2 Frequency of frequencies
### 18.3 N1, N2, N3, ...
### 18.4 Adjusted count c*
### 18.5 c* = (c+1)N(c+1)/N(c)
### 18.6 Probability of unseen events
### 18.7 Good-Turing numerical calculations
### 18.8 Good-Turing regression
### 18.9 log N_c = a + b log c concept
### 18.10 Fit regression for Good-Turing
### 18.11 Good-Turing implementation from scratch
### 18.12 Limitations of raw Good-Turing
## 19. Witten-Bell Smoothing
### 19.1 Witten-Bell intuition
### 19.2 Observed tokens N
### 19.3 Observed types T
### 19.4 Seen vs unseen events
### 19.5 Witten-Bell probability
### 19.6 Witten-Bell numerical problems
### 19.7 Implement Witten-Bell from scratch
## 20. Backoff & Discounting
### 20.1 Backoff concept
### 20.2 Trigram → bigram → unigram
### 20.3 Seen vs unseen N-gram handling
### 20.4 Discounting
### 20.5 Absolute discounting
### 20.6 C* = C-D
### 20.7 Estimating discount D
### 20.8 Backoff probability
### 20.9 Katz backoff
### 20.10 Katz discounted probability
### 20.11 Katz backoff weight
### 20.12 Katz numerical problems
### 20.13 Implement Katz backoff from scratch
### 20.14 Stupid backoff
### 20.15 Stupid backoff implementation
### 20.16 Backoff vs interpolation
### 20.17 Absolute discounting implementation
### 20.18 Absolute discounting numerical problems
## 21. Kneser-Ney Smoothing
### 21.1 Why Kneser-Ney exists
### 21.2 Continuation probability
### 21.3 Context diversity
### 21.4 Continuation count
### 21.5 Bigram Kneser-Ney
### 21.6 Interpolated Kneser-Ney
### 21.7 Recursive Kneser-Ney
### 21.8 Absolute discounting inside Kneser-Ney
### 21.9 Higher-order Kneser-Ney
### 21.10 Kneser-Ney numerical problems
### 21.11 Implement bigram Kneser-Ney from scratch
### 21.12 Implement interpolated Kneser-Ney
### 21.13 Implement recursive Kneser-Ney
## 22. Zipf's Law & Frequency Distributions
### 22.1 Zipf's law
### 22.2 Rank-frequency relationship
### 22.3 Power-law distribution
### 22.4 Frequency ∝ 1/rank
### 22.5 Log-log representation
### 22.6 Zipf numerical problems
### 22.7 Connection to vocabulary and sparsity
## 23. Perplexity & Language Model Evaluation
### 23.1 Log probability
### 23.2 Cross entropy
### 23.3 Perplexity definition
### 23.4 PP = P(W)^(-1/N)
### 23.5 Perplexity from log probabilities
### 23.6 Why zero probability breaks perplexity
### 23.7 Compare two language models by perplexity
### 23.8 Intrinsic evaluation
### 23.9 Extrinsic evaluation
## 24. Byte Pair Encoding (BPE)
### 24.1 Why subword tokenization is needed
### 24.2 Character-level starting representation
### 24.3 Word-level vs subword-level representation
### 24.4 BPE algorithm
### 24.5 Count adjacent symbol pairs
### 24.6 Find most frequent pair
### 24.7 Merge most frequent pair
### 24.8 Update vocabulary
### 24.9 Repeat merges
### 24.10 Stopping condition
### 24.11 BPE numerical/manual problems
### 24.12 Implement pair counting from scratch
### 24.13 Implement pair merging from scratch
### 24.14 Implement complete BPE trainer from scratch
### 24.15 BPE vs WordPiece
### 24.16 BPE vs Unigram LM
## 25. Text Classification
### 25.1 Text classification
### 25.2 Spam/not-spam example
### 25.3 Count/BOW features
### 25.4 TF-IDF features
### 25.5 Naive Bayes
### 25.6 Multinomial Naive Bayes
### 25.7 Laplace smoothing in Naive Bayes
### 25.8 Naive Bayes from scratch
### 25.9 Logistic regression concept
### 25.10 Confusion matrix
### 25.11 TP/TN/FP/FN
### 25.12 Accuracy
### 25.13 Precision
### 25.14 Recall
### 25.15 F1 score
### 25.16 Macro-F1 vs Micro-F1
## 26. Sentiment Analysis
### 26.1 Sentiment analysis
### 26.2 Positive/negative classification
### 26.3 Lexicon-based sentiment
### 26.4 Lexicon classifier from scratch
### 26.5 Naive Bayes sentiment classifier
### 26.6 Sentiment evaluation
## 27. Sequence Generation
### 27.1 Autoregressive generation
### 27.2 Next-token prediction
### 27.3 Greedy decoding
### 27.4 Random sampling
### 27.5 Temperature
### 27.6 Beam search
### 27.7 Beam search from scratch
## 28. Machine Translation & Speech
### 28.1 Machine translation
### 28.2 Source and target language
### 28.3 Rule-based translation concept
### 28.4 Statistical machine translation concept
### 28.5 Neural machine translation concept
### 28.6 Sequence-to-sequence concept
### 28.7 Automatic speech recognition
### 28.8 Speech → text
### 28.9 Text → speech
### 28.10 Speaker identification
### 28.11 Phonetics/phonemes
## 29. Summarization, QA & Information Extraction
### 29.1 Extractive summarization
### 29.2 Sentence scoring
### 29.3 Sentence scoring implementation
### 29.4 Abstractive summarization concept
### 29.5 Question answering
### 29.6 Retrieval-based QA
### 29.7 Generative QA
### 29.8 Information extraction
### 29.9 Relation extraction
### 29.10 Entity linking
## 30. Evaluation & Metrics
### 30.1 Language-model evaluation
### 30.2 Perplexity
### 30.3 Classification accuracy
### 30.4 Precision
### 30.5 Recall
### 30.6 F1
### 30.7 Sequence-labeling token accuracy
### 30.8 Entity-level NER precision/recall/F1
### 30.9 BLEU concept
### 30.10 ROUGE concept
## 31. Final Scratch-Implementation Projects
### 31.1 Complete tokenizer without NLP libraries
### 31.2 Complete regex tokenizer
### 31.3 Complete DFA/NFA recognizer
### 31.4 Complete morphology FST
### 31.5 Complete POS tagger
### 31.6 Complete CFG parser
### 31.7 Complete TF-IDF engine
### 31.8 Complete N-gram language model
### 31.9 Sentence probability calculator
### 31.10 Next-token predictor
### 31.11 Perplexity calculator
### 31.12 Laplace + Add-k framework
### 31.13 Good-Turing implementation
### 31.14 Witten-Bell implementation
### 31.15 Katz backoff implementation
### 31.16 Absolute discounting implementation
### 31.17 Kneser-Ney implementation
### 31.18 BPE tokenizer trainer
### 31.19 Naive Bayes classifier
### 31.20 HMM + Viterbi sequence tagger