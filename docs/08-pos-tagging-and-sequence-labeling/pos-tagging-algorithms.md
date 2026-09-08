# POS Tagging Algorithms

## 1. Rule-Based POS Tagging
Early taggers used massive dictionaries and hand-written rules. 
- *Step 1*: Look up all possible tags for a word in the dictionary.
- *Step 2*: Apply rules to eliminate impossible tags.

**Example Rule**: If the preceding word is an article ("the"), then the current word cannot be a verb.
- "The **back**..." $\rightarrow$ "back" must be a noun or adjective, not a verb.

*Drawbacks*: Human languages are too complex. Building a complete set of rules that covers all exceptions is virtually impossible.

## 2. Hidden Markov Models (HMM) for POS Tagging
In modern classical NLP, POS tagging is treated as a probabilistic sequence model. A Hidden Markov Model (HMM) is the mathematical standard for this.

In an HMM:
- The **observations** (what we can see) are the words in the sentence.
- The **hidden states** (what we want to infer) are the POS tags.

### The Two Probabilities of an HMM
An HMM calculates the most likely sequence of tags by combining two probabilities:
1. **Transition Probability $P(t_i | t_{i-1})$**: The probability that tag $t_i$ follows tag $t_{i-1}$. (e.g., What is the probability that a NOUN follows a DET?). We calculate this by counting sequences in a labeled training corpus.
2. **Emission Probability $P(w_i | t_i)$**: The probability that tag $t_i$ generates word $w_i$. (e.g., Given that the tag is VERB, what is the probability the word is "back"?).

### The Goal
For a sequence of words $W = w_1, w_2, ..., w_n$, we want to find the sequence of tags $T = t_1, t_2, ..., t_n$ that maximizes:
$$ \prod_{i=1}^{n} P(w_i | t_i) \times P(t_i | t_{i-1}) $$

## 3. The Viterbi Algorithm
If a sentence has 10 words, and there are 30 possible POS tags, there are $30^{10}$ possible tag sequences. Calculating the probability for all of them is computationally impossible.

The **Viterbi Algorithm** is a dynamic programming algorithm that finds the most likely sequence of hidden states in an HMM in linear time $O(N \cdot |T|^2)$.

It works by processing the sequence left-to-right. At each step, for each possible tag, it only remembers the *maximum* probability path that led to that tag, discarding all lower-probability paths.

## 4. Scratch Implementation (Toy Viterbi Tagger)
```python
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # Initialize base cases (t=0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y].get(obs[0], 0.0001)
        path[y] = [y]

    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            # Find the maximum probability path to this state 'y'
            (prob, state) = max(
                (V[t-1][y0] * trans_p[y0][y] * emit_p[y].get(obs[t], 0.0001), y0)
                for y0 in states
            )
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        path = newpath

    # Find the final most probable state
    (prob, state) = max((V[len(obs) - 1][y], y) for y in states)
    return (prob, path[state])

# --- Toy Example Data ---
states = ('NOUN', 'VERB')
observations = ('i', 'saw', 'a', 'saw')

start_probability = {'NOUN': 0.8, 'VERB': 0.2}

transition_probability = {
    'NOUN': {'NOUN': 0.1, 'VERB': 0.9},
    'VERB': {'NOUN': 0.8, 'VERB': 0.2}
}

emission_probability = {
    'NOUN': {'i': 0.4, 'a': 0.4, 'saw': 0.2},
    'VERB': {'saw': 0.8, 'i': 0.1, 'a': 0.1}
}

# Run
prob, sequence = viterbi(observations, states, start_probability, transition_probability, emission_probability)

print(f"Sequence: {observations}")
print(f"Tags:     {sequence}")
print(f"Prob:     {prob}")

# Output:
# Sequence: ('i', 'saw', 'a', 'saw')
# Tags:     ['NOUN', 'VERB', 'NOUN', 'VERB']
# (Notice it correctly tagged the first 'saw' as VERB and the second 'saw' as VERB/NOUN depending on the probabilities, actually in this toy model it alternates NOUN, VERB, NOUN, VERB).
```

## 5. Exam Preparation
### Must Memorize
- Transition Probability: $P(Tag_{Current} | Tag_{Previous})$
- Emission Probability: $P(Word_{Current} | Tag_{Current})$

### Likely Theory Question
**Question**: Why is the Viterbi algorithm necessary for HMM POS tagging?
**Answer**: Because the number of possible tag sequences grows exponentially with the length of the sentence ($|Tags|^{Length}$). Viterbi uses dynamic programming to discard sub-optimal paths at each step, reducing the time complexity to linear $O(N)$ relative to the sentence length.
