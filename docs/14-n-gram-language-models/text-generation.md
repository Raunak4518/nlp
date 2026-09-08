# Text Generation and Boundaries

## 1. Start and End Markers
In the previous section, we calculated the probability of a Bigram sequence starting with "I":
$$ P(\text{"I am"}) = P(\text{"I"}) \times P(\text{"am"} \mid \text{"I"}) $$

**The Problem**: Where did the first word "I" mathematically come from? In a strict $P(w_i \mid w_{i-1})$ bigram model, every word must be conditioned on a previous word. The first word has no preceding context.

To solve this, we inject artificial **Boundary Tokens** into our training data *before* calculating any counts.
- `<s>`: Start of sentence marker.
- `</s>`: End of sentence marker.

The raw string `"I am Sam"` is modified to: `["<s>", "I", "am", "Sam", "</s>"]`.

Now, we can properly calculate the conditional probability of the sentence *starting* with "I":
$$ P(\text{"I"} \mid \text{"<s>"}) $$

And we can calculate the probability of the sentence terminating *after* "Sam":
$$ P(\text{"</s>"} \mid \text{"Sam"}) $$

---

## 2. Next-Word Prediction (Greedy Search)
To predict the next word in an autocomplete system, we mathematically calculate $P(w_{next} \mid w_{current})$ for *every single word* in our vocabulary database, and return the word that yields the highest probability score. 

This technique of always picking the mathematically "safest" option is known as the **argmax** function:
$$ w_{next} = \text{argmax}_{w \in V} P(w \mid w_{current}) $$

---

## 3. Unknown Tokens (`<UNK>`)
If a user types a word that was completely absent from the training corpus (e.g., "Zorplox"), the system will crash because that word has no row in the vocabulary matrix.

To handle this elegantly, we designate an `<UNK>` (Unknown) token. During the training phase, any word that appears very rarely (e.g., only 1 time in the entire corpus) is permanently replaced with the `<UNK>` token. 

This brilliantly forces the mathematical model to learn the probability of transitioning *into* and *out of* unknown words, allowing the system to process Out-Of-Vocabulary (OOV) inputs in production without crashing.

---

## 4. Scratch Implementation (Bigram Generator)

Here is a functional Python script demonstrating how to count bigrams from a tiny corpus and use them to probabilistically generate novel sentences.

```python
import random
from collections import defaultdict

class BigramModel:
    def __init__(self):
        # Maps (w1) -> {w2: count}
        self.counts = defaultdict(lambda: defaultdict(int))
        self.vocab = set()

    def train(self, sentences: list[str]):
        for sentence in sentences:
            # 1. Add boundary markers
            tokens = ["<s>"] + sentence.lower().split() + ["</s>"]
            
            # 2. Count bigrams
            for i in range(len(tokens) - 1):
                w1, w2 = tokens[i], tokens[i+1]
                self.counts[w1][w2] += 1
                self.vocab.add(w1)
                self.vocab.add(w2)

    def generate(self) -> str:
        current_word = "<s>"
        sentence = []

        while True:
            # Get possible next words and their raw counts
            next_word_counts = self.counts[current_word]
            
            # Failsafe if we hit a dead end (shouldn't happen with proper </s> logic)
            if not next_word_counts:
                break

            # Separate words and their frequency weights
            words = list(next_word_counts.keys())
            weights = list(next_word_counts.values())

            # Choose the next word randomly, weighted by its probability.
            # (If we used argmax() here, it would always generate the exact same sentence!)
            current_word = random.choices(words, weights=weights, k=1)[0]

            if current_word == "</s>":
                break
                
            sentence.append(current_word)

        return " ".join(sentence)
```

### Try It Yourself

??? question "Trace the Generator"
    ```python
    corpus = [
        "I am Sam",
        "Sam I am",
        "I do not like green eggs and ham"
    ]
    
    model = BigramModel()
    model.train(corpus)
    
    # Generate 3 novel sentences using probability distributions
    for i in range(3):
        print(f"Generated: {model.generate()}")
        
    # Example Output:
    # Generated: I do not like green eggs and ham
    # Generated: Sam I am Sam I do not like green eggs and ham
    # Generated: I am Sam I am Sam
    ```

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Write out the full Chain Rule expansion to calculate the probability of the sentence "I am Sam", assuming a Bigram Model and the use of explicit Start and End boundary markers.
> **Answer**: 
> $$ P(\text{Sentence}) = P(\text{"I"} \mid \text{"<s>"}) \times P(\text{"am"} \mid \text{"I"}) \times P(\text{"Sam"} \mid \text{"am"}) \times P(\text{"</s>"} \mid \text{"Sam"}) $$

**2-Mark Question**: In text generation, why is weighted random sampling (like Python's `random.choices`) often preferred over simply using `argmax()` to pick the most probable next word?
> **Answer**: If we always use `argmax()` to pick the mathematically most probable next word (Greedy Search), the model becomes completely deterministic. Given the same starting word, it will enter a loop and generate the exact same "safest" string of text every single time, severely limiting creativity. By sampling randomly based on the underlying probability distribution, we allow the model to generate diverse, novel sentences.

---

### Can You Explain This?
- [ ] I can explain the mathematical necessity of the `<s>` marker.
- [ ] I can define what an Out-Of-Vocabulary (OOV) word is.
- [ ] I can explain how the `<UNK>` token prevents system crashes.
