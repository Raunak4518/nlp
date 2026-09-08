# POS Tagging Algorithms

## 1. Rule-Based POS Tagging
Early taggers used massive dictionaries and hand-written rules. 
- **Step 1**: Look up all possible tags for a word in the dictionary.
- **Step 2**: Apply rules to eliminate linguistically impossible tags.

**Example Rule**: If the preceding word is an article ("the"), then the current word cannot be a verb.
- "The **back**..." $\rightarrow$ "back" must be a noun or adjective, not a verb.

**Drawbacks**: Human languages are too complex. Building a complete set of rules that covers all exceptions is virtually impossible and doesn't scale to new languages.

---

## 2. Hidden Markov Models (HMM) for POS Tagging
In modern classical NLP, POS tagging is treated as a probabilistic sequence model. A **Hidden Markov Model (HMM)** is the mathematical standard for this.

In an HMM:
- The **observations** (the things we can actually see) are the words in the sentence.
- The **hidden states** (the things we want to infer) are the POS tags.

### The Two Probabilities of an HMM
An HMM calculates the most likely sequence of tags by combining two probabilities, which are learned by counting frequencies in a massive, human-labeled training corpus (like the Penn Treebank).

!!! abstract "Transition Probability $P(t_i \mid t_{i-1})$"
    The mathematical probability that tag $t_i$ follows tag $t_{i-1}$. 
    *(e.g., What is the probability that a NOUN follows a DET? Very high! What is the probability a VERB follows a DET? Very low!)*

!!! abstract "Emission Probability $P(w_i \mid t_i)$"
    The mathematical probability that tag $t_i$ generates word $w_i$. 
    *(e.g., Given that the tag is currently VERB, what is the probability the word is "back"?)*

### The Goal
For a sequence of words $W = w_1, w_2, ..., w_n$, we want to find the specific sequence of tags $T = t_1, t_2, ..., t_n$ that maximizes the following formula:
$$ \text{Score} = \prod_{i=1}^{n} P(w_i \mid t_i) \times P(t_i \mid t_{i-1}) $$

---

## 3. The Viterbi Algorithm

If a sentence has 10 words, and there are 30 possible POS tags, there are $30^{10}$ possible tag sequences. Calculating the probability for all of them to find the maximum is computationally impossible.

The **Viterbi Algorithm** is a classic dynamic programming algorithm that finds the most likely sequence of hidden states in an HMM in strict linear time $O(N \cdot |T|^2)$.

It works by processing the sequence left-to-right. At each step, for each possible tag, it calculates and remembers *only* the maximum probability path that led to that tag, permanently discarding all lower-probability paths. This prevents the exponential explosion of paths.

---

## 4. Scratch Implementation (Toy Viterbi Tagger)

Here is a functional Viterbi algorithm implemented in standard Python.

```python
def viterbi(obs, states, start_p, trans_p, emit_p):
    # V[t][y] will store the probability of the most likely path ending in state 'y' at time 't'
    V = [{}]
    # path[y] will store the actual sequence of states leading to state 'y'
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
            # Find the maximum probability path from the previous state (y0) to this state (y)
            (prob, state) = max(
                (V[t-1][y0] * trans_p[y0][y] * emit_p[y].get(obs[t], 0.0001), y0)
                for y0 in states
            )
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        path = newpath

    # Find the final most probable state at the end of the sequence
    (prob, state) = max((V[len(obs) - 1][y], y) for y in states)
    return (prob, path[state])
```

### Try It Yourself

??? question "Trace the Toy Model"
    ```python
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
    
    prob, sequence = viterbi(observations, states, start_probability, 
                             transition_probability, emission_probability)
    
    print(sequence) 
    # Output: ['NOUN', 'VERB', 'NOUN', 'NOUN'] 
    # (Notice the Viterbi algorithm successfully resolved the ambiguity of the word "saw" based on the transition probabilities!)
    ```

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Define Transition Probability and Emission Probability in the context of an HMM used for POS tagging. Write down the formulas.
> **Answer**: 
> - **Transition Probability** $P(t_i \mid t_{i-1})$ is the probability of moving from one tag to the next. It models the syntactic rules of the language (e.g., how likely is a Noun to follow an Adjective).
> - **Emission Probability** $P(w_i \mid t_i)$ is the probability that a given tag will generate a specific word. It models the lexical dictionary of the language (e.g., how likely is the NOUN tag to produce the word "apple").

**3-Mark Question**: Why is the Viterbi algorithm strictly necessary for HMM POS tagging?
> **Answer**: Because the number of possible tag sequences grows exponentially with the length of the sentence ($|Tags|^{Length}$), making a brute-force search impossible. Viterbi uses dynamic programming to discard sub-optimal paths at each timestep, reducing the algorithmic time complexity to a manageable linear time $O(N)$.

---

### Can You Explain This?
- [ ] I can write the formula for Transition Probability.
- [ ] I can write the formula for Emission Probability.
- [ ] I can explain what problem the Viterbi algorithm solves.
- [ ] I can explain the basic concept of dynamic programming as it applies to Viterbi.
