# Sequence Generation and Decoding Strategies

## 1. Autoregressive Generation
Language Models (whether N-gram models or Transformers like GPT-4) generate text **Autoregressively**.
This means they do not generate entire sentences at once. They perform **Next-Token Prediction**:
1. Take the current sequence (e.g., "The cat sat on the").
2. Predict the probabilities for the *single* next word.
3. Select a word (e.g., "mat").
4. Append it to the sequence ("The cat sat on the mat").
5. Feed the *entire new sequence* back into the model to predict the next word.

The algorithm used to "select" the word in Step 3 is called the **Decoding Strategy**.

## 2. Greedy Decoding
The simplest decoding strategy is **Greedy Decoding**. At every step, the model looks at the probability distribution and strictly selects the single word with the highest probability ($argmax$).

- *Pros*: Extremely fast.
- *Cons*: It often leads to repetitive, boring, or mathematically suboptimal sentences. By greedily choosing the best word *right now*, it might trap itself in a path where all future word choices have terrible probabilities.

## 3. Random Sampling and Temperature
Instead of always picking the #1 word, we can use **Random Sampling**. We roll a weighted die based on the probability distribution. If "mat" has a 70% chance and "dog" has a 30% chance, we literally randomly pick "mat" 70% of the time. This makes the text much more creative and human-like.

We control this randomness using a parameter called **Temperature ($T$)**.
During decoding, we divide the pre-normalized scores (logits) by $T$ before calculating the probabilities.
- **$T = 1.0$**: Normal random sampling.
- **$T < 1.0$ (e.g., 0.1)**: Low temperature. The probabilities of the top words are artificially inflated, making the model more deterministic and robotic. As $T \rightarrow 0$, it becomes identical to Greedy Decoding.
- **$T > 1.0$ (e.g., 2.0)**: High temperature. The probabilities are flattened, giving rare words a much higher chance of being selected. The text becomes highly creative, but often turns into incoherent gibberish.

## 4. Beam Search
**Beam Search** is the industry standard for tasks where we want the mathematically optimal sentence, but cannot afford to calculate every possible combination of words (which would take infinite time). It is heavily used in Machine Translation.

Instead of keeping just 1 path (Greedy), Beam Search keeps track of the top $K$ most probable paths at the same time. $K$ is called the **Beam Width**.

### How it works (Beam Width = 2):
1. The model predicts the first word. Instead of picking just the top word, it saves the top 2 words (e.g., "The" and "A").
2. For the next step, it asks the model: "What comes after 'The'?" AND "What comes after 'A'?".
3. If the vocabulary has 10,000 words, it now has 20,000 possible 2-word sequences.
4. It calculates the total sequence probability for all 20,000 options, sorts them, and immediately throws away 19,998 of them, keeping only the top 2 overall sequences.
5. It repeats this until the `</s>` (End of Sequence) token is generated.

## 5. Scratch Implementation (Beam Search Concept)
```python
import math

def beam_search(start_token: str, vocab: list[str], get_prob_func, beam_width: int, max_length: int):
    # Store tuples of (Sequence_List, Log_Probability_Score)
    beams = [([start_token], 0.0)]
    
    for _ in range(max_length):
        all_candidates = []
        
        # Expand every currently saved beam
        for seq, score in beams:
            if seq[-1] == "</s>": # If this beam is done, just keep it
                all_candidates.append((seq, score))
                continue
                
            # Try appending every word in the vocabulary
            for word in vocab:
                # Get the log probability of 'word' given the 'seq' context
                prob = get_prob_func(seq, word) 
                new_seq = seq + [word]
                new_score = score + math.log(prob)
                all_candidates.append((new_seq, new_score))
                
        # Sort all expanded candidates by score (highest first)
        ordered = sorted(all_candidates, key=lambda tup: tup[1], reverse=True)
        
        # Prune: Keep only the top K beams!
        beams = ordered[:beam_width]
        
    # Return the best sequence found
    return beams[0]
```

## 6. Exam Preparation
### Must Memorize
- Autoregressive means generating one token at a time and feeding it back into the model.
- High Temperature ($T>1$) = More random/creative. Low Temperature ($T<1$) = More deterministic/greedy.
- Beam Search keeps the top $K$ paths alive to avoid local optimum traps.

### Likely Theory Question
**Question**: Why is Beam Search preferred over Greedy Decoding in Machine Translation?
**Answer**: In Machine Translation, the goal is to find the sentence with the highest overall probability. Greedy decoding only looks one step ahead. It might pick a word that is highly probable right now, but forces the rest of the sentence into a grammatically incorrect structure with very low probability. Beam search looks at the total sequence probability and keeps $K$ alternative paths open, allowing it to sacrifice a short-term probability win for a much higher total sentence probability.
