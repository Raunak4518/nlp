# Text Generation and Boundaries

## 1. Start and End Markers
In the previous section, we calculated the Bigram probability $P(\text{"I am"}) = P(\text{"I"}) \times P(\text{"am"} | \text{"I"})$.
But there is a problem: where did the first word "I" come from? It has no preceding context.

To solve this, we inject artificial boundary tokens into our training data before calculating counts.
- `<s>`: Start of sentence marker.
- `</s>`: End of sentence marker.

"I am Sam" becomes: `<s> I am Sam </s>`.

Now, we can properly calculate the probability of the sentence starting with "I":
$P(\text{"I"} | \text{"<s>"})$

And we can calculate the probability of the sentence ending after "Sam":
$P(\text{"</s>"} | \text{"Sam"})$

## 2. Next-Word Prediction
To predict the next word in an autocomplete system, we calculate $P(w_i | w_{i-1})$ for every single word in the vocabulary $V$, and return the word that yields the highest probability. 

This is known as the **argmax** function:
$$ w_{next} = \text{argmax}_{w \in V} P(w | w_{i-1}) $$

## 3. Unknown Tokens (`<UNK>`)
If a user types a word that was not in the training corpus, the system will crash because that word is not in the vocabulary matrix.

To handle this, we designate an `<UNK>` (Unknown) token. During training, any word that appears very rarely (e.g., only 1 time) is replaced with `<UNK>`. This forces the model to learn the probability of transitioning into and out of unknown words.

## 4. Scratch Implementation (Bigram Generator)

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
            # Add boundary markers
            tokens = ["<s>"] + sentence.lower().split() + ["</s>"]
            
            # Count bigrams
            for i in range(len(tokens) - 1):
                w1, w2 = tokens[i], tokens[i+1]
                self.counts[w1][w2] += 1
                self.vocab.add(w1)
                self.vocab.add(w2)

    def generate(self) -> str:
        current_word = "<s>"
        sentence = []

        while True:
            # Get possible next words and their counts
            next_word_counts = self.counts[current_word]
            
            # If we hit a dead end (shouldn't happen with </s>)
            if not next_word_counts:
                break

            # Convert counts to probabilities for weighted random choice
            words = list(next_word_counts.keys())
            weights = list(next_word_counts.values())

            # Choose the next word randomly based on its probability weight
            # (If we used argmax here instead of random, it would always generate the exact same sentence)
            current_word = random.choices(words, weights=weights, k=1)[0]

            if current_word == "</s>":
                break
                
            sentence.append(current_word)

        return " ".join(sentence)

# --- Trace ---
corpus = [
    "I am Sam",
    "Sam I am",
    "I do not like green eggs and ham"
]

model = BigramModel()
model.train(corpus)

# Generate 5 random sentences
for i in range(5):
    print(f"Generated: {model.generate()}")
    
# Example Outputs:
# Generated: I do not like green eggs and ham
# Generated: Sam I am Sam I do not like green eggs and ham
# Generated: I am Sam I am Sam
```

## 5. Exam Preparation
### Must Know
- `<s>` is required so that the first word of a sentence has a conditional context in an n-gram model.

### Likely Theory Question
**Question**: In the scratch implementation above, the `generate()` function uses `random.choices(weights)` instead of `argmax()`. Why?
**Answer**: If we always used `argmax()` to pick the mathematically most probable next word, the model would be deterministic. It would enter a loop and generate the exact same "safest" string of text every single time. By sampling randomly based on the probability distribution, we allow the model to generate diverse, novel sentences.
