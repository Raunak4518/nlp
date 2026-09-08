# 27. Sequence Generation

## 1. What this topic is
This module explains how a Language Model actually generates text, covering the autoregressive loop and the Decoding Strategies (Greedy, Sampling, Beam Search) used to pick the next word.

## 2. Why it matters in NLP
Training a language model gives you a probability distribution. Decoding is how you actually *use* that distribution to write a story, translate a sentence, or summarize a document. The choice of decoding strategy completely changes the behavior of the model.

## 3. What the student will learn
- The concept of Autoregressive Next-Token Prediction.
- Why Greedy Decoding is fast but suboptimal.
- How Temperature scaling controls the randomness of sampling.
- How Beam Search maintains $K$ parallel paths to optimize total sequence probability.
- How to implement a basic Beam Search loop.

## 4. Prerequisites
- [14. N-gram Language Models](../14-n-gram-language-models/README.md)

## 5. Complete subtopic list
- [Sequence Generation and Decoding Strategies](decoding-strategies.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★☆☆☆ (Low - The math is mostly just summing log probabilities, but tracking the Beams conceptually can be slightly confusing).

## 8. Implementation difficulty
★★★☆☆ (Medium - Writing a bug-free Beam Search with proper pruning is a classic whiteboard interview question).

## 9. Numerical-problem relevance
**High**. Tracing a Beam Search tree on paper given a set of probabilities is a very common exam question.

## 10. Exam importance
**Medium-High**.

## 11. Common mistakes
- Thinking that Beam Search is guaranteed to find the absolute mathematically optimal sentence. It does not (only an exhaustive search of all possible combinations does that). Beam search is an *approximation* algorithm.
- Thinking that $T=0$ means completely random. $T=0$ means completely deterministic (Greedy). Higher temperature means more random.

## 12. Related topics
- [28. Machine Translation & Speech](../28-machine-translation-and-speech/README.md) (Beam search is the core decoding algorithm for MT).

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand how changing the Temperature affects the probability distribution.
- [ ] Explain the trade-off between Beam Width and computation time.

## 15. Implementation checklist
- [ ] Read through the Beam Search python concept code and understand the sorting and pruning steps.

## 16. Numerical-practice checklist
- [ ] Draw a Beam Search tree with $K=2$ for 3 timesteps.
