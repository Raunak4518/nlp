# Algorithm Cheat Sheet

This page provides a rapid overview of the most critical algorithms tested in the NLP syllabus.

## Core NLP Algorithms

### Byte Pair Encoding (BPE)
| Property | Description |
| :--- | :--- |
| **Purpose** | Tokenizes text into subwords to handle Out-Of-Vocabulary (OOV) words and reduce vocabulary size. |
| **Input** | Raw text corpus. |
| **Output** | A vocabulary of subword tokens and a set of merge rules. |
| **Core Idea** | Treat every character as a token. Iteratively find the most frequent adjacent pair of tokens and merge them into a single new token. Repeat $k$ times. |
| **Complexity** | $O(N \log N)$ using a priority queue. |

### Minimum Edit Distance
| Property | Description |
| :--- | :--- |
| **Purpose** | Measures the minimum number of operations (insert, delete, substitute) required to transform one string into another. Used in spell correction. |
| **Input** | String A, String B. |
| **Output** | An integer representing the minimum distance. |
| **Core Idea** | Dynamic programming. Build an $N \times M$ matrix where `D[i,j]` is the edit distance between the first $i$ chars of A and $j$ chars of B. |
| **Complexity** | Time: $O(N \times M)$. Space: $O(N \times M)$ (or $O(\min(N,M))$ if optimized). |

### The Viterbi Algorithm
| Property | Description |
| :--- | :--- |
| **Purpose** | Finds the most likely sequence of hidden states (e.g., POS tags) given an observed sequence of words in an HMM. |
| **Input** | Observed sequence (words), Transition matrix, Emission matrix. |
| **Output** | The single most probable path of hidden states. |
| **Core Idea** | Dynamic programming. At each timestep, for each state, calculate the max probability of arriving there. Store a backpointer to the best previous state. |
| **Complexity** | Time: $O(T \times K^2)$ where $T$ is sequence length and $K$ is number of states. |

### CKY (Cocke-Kasami-Younger) Parsing
| Property | Description |
| :--- | :--- |
| **Purpose** | Determines if a sentence is grammatically valid according to a Context-Free Grammar (CFG), and generates its parse trees. |
| **Input** | Sentence, CFG in Chomsky Normal Form (CNF). |
| **Output** | A parse tree (or a boolean indicating if parsing failed). |
| **Core Idea** | Dynamic programming. Build a 2D upper-triangular table. Combine smaller valid spans into larger valid spans until the entire sentence forms the root symbol $S$. |
| **Complexity** | Time: $O(N^3 \times |G|)$ where $N$ is sentence length and $|G|$ is grammar size. |

### Beam Search
| Property | Description |
| :--- | :--- |
| **Purpose** | A decoding algorithm for sequence generation (like Machine Translation) that approximates the mathematically optimal sequence. |
| **Input** | Autoregressive model, start token, Beam Width $K$. |
| **Output** | The best generated sequence. |
| **Core Idea** | Maintain the top $K$ most probable partial sequences at all times. Expand all $K$ paths by 1 token, score all resulting paths, and prune back down to the top $K$. |
| **Complexity** | Time: $O(T \times K \times V)$ where $T$ is max length, $K$ is beam width, $V$ is vocab size. |

### Kneser-Ney Smoothing
| Property | Description |
| :--- | :--- |
| **Purpose** | Estimates probabilities of n-grams, especially unseen ones, better than any other classical method. |
| **Input** | N-gram counts from a corpus. |
| **Output** | Smoothed probability distribution. |
| **Core Idea** | "Absolute Discounting" (subtract a fixed value $d$ from all counts) plus "Continuation Probability" (a lower-order backoff based on how many *different* contexts a word appears in). |
| **Complexity** | $O(1)$ at inference if precomputed. |
