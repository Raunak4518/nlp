# Summarization

## 1. Extractive Summarization
**Extractive Summarization** functions exactly like a human using a highlighter pen on a textbook. The algorithmic pipeline reads a long document, mathematically evaluates the "importance" of every single sentence, and physically "extracts" the top $N$ highest-scoring sentences verbatim to form the summary. 
*Critically, it does not mathematically generate any new text.*

### Sentence Scoring Algorithm
To scientifically determine which sentences are "important", the algorithm assigns a numerical score to each sentence based entirely on the specific words it contains. The most common classical method uses **TF-IDF** (Covered in Module 12).
1. Calculate the standard TF-IDF score for every unique word in the document.
2. For each sentence, sum the TF-IDF scores of all the words present in that sentence.
3. **Normalize** by dividing that sum by the physical length of the sentence (to mathematically prevent the algorithm from just blindly picking the longest sentences).
4. Rank all the sentences by their normalized score descending, and output the top 3.

---

## 2. Abstractive Summarization
**Abstractive Summarization** functions like a human reading a textbook, closing it, and explaining the concepts to a friend. The algorithm mathematically compresses the semantic meaning of the document and generates an *entirely new*, structurally shorter text that captures the core concepts, frequently hallucinating brand new words and phrasing that never physically appeared in the original document.

Abstractive summarization relies heavily on **Neural Seq2Seq models** (like BART, T5, or GPT-4). It is fundamentally orders of magnitude harder than Extractive Summarization. The model must not only maintain grammatical fluency while generating new text, but it must rigorously avoid "hallucinating" false facts that contradict the source text.

---

## 3. Scratch Implementation (Extractive Sentence Scoring)

Here is a simple, highly effective Python implementation of a TF-IDF Extractive Summarizer.

```python
def score_sentences(text: str, word_scores: dict[str, float]) -> list[str]:
    """Extracts the top 2 most important sentences using TF-IDF word scores."""
    
    # 1. Simple sentence tokenizer (splitting by periods)
    sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 5]
    
    sentence_scores = []
    
    # 2. Score every sentence
    for sentence in sentences:
        words = sentence.lower().split()
        
        # Calculate raw sum of TF-IDF scores
        score = sum(word_scores.get(word, 0.0) for word in words)
        
        # 3. NORMALIZE by length to calculate "density of importance"
        normalized_score = score / len(words) 
        
        sentence_scores.append((sentence, normalized_score))
        
    # 4. Sort strictly by normalized score descending
    sentence_scores.sort(key=lambda x: x[1], reverse=True)
    
    # 5. Return the text of the top 2 sentences
    return [s[0] for s in sentence_scores[:2]]

# --- Code Trace ---
text = "The quick brown fox jumps over the lazy dog. The sun is shining. The fox is very quick and brown. It is a nice day."

# Assume these TF-IDF scores were calculated across a large Wikipedia corpus
tf_idf_scores = {
    "fox": 5.0,
    "quick": 4.0,
    "brown": 3.0,
    "sun": 1.0,
    "dog": 2.0
}

summary = score_sentences(text, tf_idf_scores)

print("Extractive Summary:")
for s in summary:
    print(f"- {s}.")

# Output:
# Extractive Summary:
# - The fox is very quick and brown.
# - The quick brown fox jumps over the lazy dog.
```

---

## 4. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You are designing an Extractive Summarization system using TF-IDF sentence scoring. Why is mathematically normalizing the sentence score by the sentence length absolutely critical for the performance of the algorithm?
> **Answer**: If an extractive algorithm simply sums the raw TF-IDF scores of all the words in a sentence, it will naturally and unfairly favor extremely long, rambling sentences simply because they contain more physical words and therefore accumulate more total score. 
> 
> Normalizing the score by mathematically dividing the total sum by the word count calculates the average "density" of importance per word. This strictly allows short, highly-informative, densely packed sentences to properly outrank long, diluted sentences, resulting in a much more concise and useful summary.

**2-Mark Question**: Explain the fundamental difference between how Extractive and Abstractive summarizers construct their final output.
> **Answer**: Extractive summarizers algorithmically select and physically copy/paste the most important existing sentences directly from the source text verbatim. Abstractive summarizers use Seq2Seq language models to generate entirely new sentences from scratch that summarize the semantic meaning of the source text, often using completely novel vocabulary.

---

### Can You Explain This?
- [ ] I can explicitly define the difference between Extractive and Abstractive summarization.
- [ ] I can trace the Python loop for an extractive sentence scorer.
- [ ] I can explicitly define why we divide the total score by the `len(words)` in the implementation.
