# Sequence Generation and Decoding Strategies

## 1. Autoregressive Generation
Language Models (whether classical N-gram models or modern Transformers like GPT-4) mathematically generate text **Autoregressively**.
This means they absolutely do not generate entire sentences all at once. They perform a strict loop called **Next-Token Prediction**:
1. Take the current context sequence (e.g., "The cat sat on the").
2. Mathematically predict the entire probability distribution for the *single* next word across the entire vocabulary.
3. Select a word from that distribution (e.g., "mat").
4. Append the selected word to the context sequence ("The cat sat on the mat").
5. Feed the *entire new sequence* back into the model to predict the next word.

The specific mathematical algorithm used to "select" the word in Step 3 is formally called the **Decoding Strategy**.

---

## 2. Greedy Decoding
The simplest, most computationally primitive decoding strategy is **Greedy Decoding**. At every single step, the model looks at the probability distribution and strictly, unconditionally selects the single word with the absolute highest probability ($\operatorname{argmax}$).

- **Pros**: Extremely fast. Requires almost zero computer memory.
- **Cons**: It frequently leads to highly repetitive, boring, or mathematically suboptimal sentences. By greedily choosing the mathematically best word *right now*, it will often trap itself in a "dead end" path where all subsequent future word choices have terrible probabilities, resulting in a low total sentence probability.

---

## 3. Random Sampling and Temperature
Instead of always blindly picking the #1 word, we can use **Random Sampling**. We mathematically roll a weighted 10,000-sided die based on the exact probability distribution. If "mat" has a 70% chance and "dog" has a 30% chance, we physically randomly pick "mat" 70% of the time. This makes the generated text much more creative and human-like.

We directly control this statistical randomness using a hyperparameter called **Temperature ($T$)**.
During decoding, we mathematically divide the raw pre-normalized neural network scores (logits) by the constant $T$ before running them through the Softmax function to calculate the final probabilities.

- **$T = 1.0$**: Normal, mathematically unaltered random sampling.
- **$T < 1.0$ (e.g., $0.1$)**: Low temperature. The math artificially inflates the probabilities of the top words, making the model much more deterministic and robotic. As $T \to 0$, the math becomes absolutely identical to Greedy Decoding.
- **$T > 1.0$ (e.g., $2.0$)**: High temperature. The mathematical distribution is artificially flattened, giving rare words a drastically higher chance of being selected. The text becomes highly creative, but at extremely high temperatures, it will degenerate into incoherent gibberish.

---

## 4. Beam Search
**Beam Search** is the industry-standard decoding strategy for tasks where we desperately want the mathematically optimal total sentence, but cannot afford the infinite compute time required to calculate every possible combination of words. It is heavily used in Google Translate and Siri.

Instead of keeping just 1 path alive (Greedy), Beam Search keeps track of the top $K$ most probable paths simultaneously. The hyperparameter $K$ is called the **Beam Width**.

### How it structurally works (Assuming Beam Width $K = 2$):
1. The model evaluates the first word. Instead of picking just the top word, it saves the top 2 words in memory (e.g., "The" and "A"). These are our 2 "Beams".
2. For the next step, it evaluates both beams simultaneously: "What comes after 'The'?" AND "What comes after 'A'?".
3. If the vocabulary has 10,000 words, the algorithm has now calculated the probabilities for 20,000 possible 2-word sequences.
4. It calculates the total sequence probability for all 20,000 options, sorts them mathematically, and immediately forcefully deletes (prunes) 19,998 of them, keeping only the top 2 overall sequences alive in memory.
5. It violently repeats this prune-and-expand loop until the `</s>` (End of Sequence) token is generated.

---

## 5. Scratch Implementation (Beam Search Concept)

```python
import math

def beam_search(start_token: str, vocab: list[str], get_prob_func, beam_width: int, max_length: int):
    """A conceptual implementation of the Beam Search algorithm."""
    
    # Store tuples of (Sequence_List, Log_Probability_Score)
    # We initialize it with the start token and a log probability of 0.0 (which is 100%)
    beams = [([start_token], 0.0)]
    
    for _ in range(max_length):
        all_candidates = []
        
        # 1. EXPAND every currently saved beam
        for seq, score in beams:
            if seq[-1] == "</s>": # If this specific beam is done, just keep it alive as is
                all_candidates.append((seq, score))
                continue
                
            # Try appending every single word in the vocabulary to this beam
            for word in vocab:
                # Get the log probability of 'word' given the 'seq' context
                prob = get_prob_func(seq, word) 
                new_seq = seq + [word]
                # In log space, we ADD probabilities to calculate total sequence score
                new_score = score + math.log(prob)
                all_candidates.append((new_seq, new_score))
                
        # 2. SORT all expanded candidates mathematically by score (highest first)
        ordered = sorted(all_candidates, key=lambda tup: tup[1], reverse=True)
        
        # 3. PRUNE: Violently delete everything except the top K beams!
        beams = ordered[:beam_width]
        
    # Return the absolutely best sequence found across all beams
    return beams[0]
```

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Mathematically and conceptually explain why Beam Search is heavily preferred over Greedy Decoding in production Machine Translation systems.
> **Answer**: In Machine Translation, the ultimate mathematical goal is to find the entire translated sequence with the highest overall joint probability. Greedy decoding only ever looks exactly one step ahead. It might greedily pick a word that is highly probable right now, but that specific word might force the rest of the sentence into a grammatically incorrect structure where all future words have extremely low probabilities, resulting in a terrible overall sentence score. 
> 
> Beam search dynamically looks at the *total sequence probability* and keeps $K$ alternative paths open in memory simultaneously. This allows the algorithm to safely sacrifice a short-term probability win on word 2 if it mathematically results in a much higher total sentence probability by word 10.

**2-Mark Question**: You are generating Python code using an LLM. You want the code to be as structurally accurate and deterministic as possible. Should you set the Temperature hyperparameter to $0.1$ or $1.5$? Why?
> **Answer**: You should set the Temperature to $0.1$. A low temperature mathematically inflates the probability of the most likely tokens, forcing the model to behave highly deterministically (approaching Greedy Decoding). This is ideal for code generation where factual accuracy is required. A temperature of $1.5$ flattens the distribution, injecting high randomness that will cause the model to hallucinate invalid syntax.

---

### Can You Explain This?
- [ ] I can explicitly define Autoregressive Generation.
- [ ] I can trace the Python loop of Beam Search, highlighting the "Expand, Sort, Prune" steps.
- [ ] I can explain mathematically why $T=0$ is identical to Greedy Decoding.
