# Cosine Similarity & Vector Mathematics

## 1. Comparing Documents
Once documents are mathematically vectorized (using BoW or TF-IDF), we frequently need to measure how similar they are. This is exactly how Search Engines rank documents against your search query (your query is treated as a tiny document).

We could try to measure **Euclidean Distance** (the straight-line physical distance between the two points in multi-dimensional space). 

**The Problem**: Euclidean distance catastrophically fails for text because document length skews the distance. A 5,000-word article about "cats" will have massive term frequencies compared to a 10-word tweet about "cats", putting them extremely far apart in physical space, even though they share the exact same semantic topic.

---

## 2. Cosine Similarity
Instead of measuring the distance between the two points, we measure the **angle** between the two vectors originating from the zero origin. 
- If two vectors point in the exact same direction, the angle is 0. $\cos(0) = 1.0$ (Identical semantic distribution).
- If two vectors are orthogonal (perpendicular), they share absolutely no terms. The angle is 90 degrees. $\cos(90) = 0.0$ (Completely dissimilar).

Because text vectors (TF-IDF/BoW) cannot have negative values (you cannot have a word appear -5 times in a document), the angle will always be between 0 and 90 degrees, meaning Cosine Similarity for text is strictly bound between `0.0` and `1.0`.

---

## 3. The Cosine Similarity Formula
The cosine of the angle between two vectors $\vec{v}$ and $\vec{w}$ is mathematically defined as the **dot product** of the vectors divided by the product of their **magnitudes** (lengths).

$$ \text{Cosine Similarity} = \frac{\vec{v} \cdot \vec{w}}{|\vec{v}| |\vec{w}|} $$

### The Dot Product
Multiply the corresponding elements of both vectors together, and sum the results.
$$ \vec{v} \cdot \vec{w} = \sum_{i=1}^{n} v_i \times w_i $$

### The Magnitude (L2 Norm)
The square root of the sum of the squared elements of the vector.
$$ |\vec{v}| = \sqrt{\sum_{i=1}^{n} (v_i)^2} $$

---

## 4. Numerical Problem Walkthrough

**Problem**: Find the cosine similarity between Document 1 and Document 2 given the following Term Frequency vectors.
- **Vocabulary ($V$)** $= [\text{apple}, \text{banana}, \text{cherry}]$
- **$D_1$** $= [2, 1, 0]$
- **$D_2$** $= [1, 1, 1]$

**Step 1: Calculate Dot Product**
$$ D_1 \cdot D_2 = (2 \times 1) + (1 \times 1) + (0 \times 1) = 2 + 1 + 0 = 3 $$

**Step 2: Calculate Magnitudes**
$$ |D_1| = \sqrt{2^2 + 1^2 + 0^2} = \sqrt{4 + 1 + 0} = \sqrt{5} \approx 2.236 $$
$$ |D_2| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{1 + 1 + 1} = \sqrt{3} \approx 1.732 $$

**Step 3: Calculate Cosine Similarity**
$$ \text{Similarity} = \frac{3}{\sqrt{5} \times \sqrt{3}} = \frac{3}{\sqrt{15}} = \frac{3}{3.873} \approx 0.774 $$

*(A similarity of 0.774 means these two documents are fairly similar).*

---

## 5. Vector Normalization
If you mathematically **normalize** your vectors to have a length/magnitude of exactly $1.0$ before comparing them (by dividing every element in the vector by the vector's magnitude), the denominator of the cosine similarity equation becomes $1 \times 1 = 1$. 

In this scenario, the Cosine Similarity equation simplifies to just the Dot Product. This is highly computationally efficient and is the standard practice in all modern NLP and deep learning libraries (like PyTorch).

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Document A and Document B share zero words in common. Prove mathematically what their cosine similarity will be and explain why.
> **Answer**: Their cosine similarity is $0.0$. Because they share absolutely no words, at least one vector will have a $0$ at every index where the other has a non-zero value. 
> 
> When calculating the dot product numerator $\sum (v_i \times w_i)$, every single multiplication will involve a zero (e.g., $5 \times 0$ or $0 \times 2$), resulting in a final dot product of $0$. A numerator of $0$ makes the entire similarity equation $0.0$, proving that the vectors are orthogonal (perpendicular).

**3-Mark Question**: Why is Cosine Similarity preferred over Euclidean Distance for comparing text documents?
> **Answer**: Euclidean Distance measures the absolute geometric distance between two points, meaning it is heavily skewed by document length. A short tweet and a massive book about the same topic will have a huge Euclidean distance because their raw term frequencies are vastly different in scale. Cosine Similarity measures the *angle* of the vectors regardless of their length, successfully capturing the semantic overlap between documents of different sizes.

---

### Can You Explain This?
- [ ] I can write the full formula for Cosine Similarity from memory.
- [ ] I can calculate a Dot Product by hand.
- [ ] I can calculate the Magnitude (L2 Norm) of a vector by hand.
- [ ] I can explain what a vector normalized to a length of 1.0 does to the Cosine formula.
