# Cosine Similarity & Vector Mathematics

## 1. Comparing Documents
Once documents are vectorized (using BoW or TF-IDF), we often need to measure how similar they are. This is how search engines rank documents against a query.

We could measure Euclidean distance (the straight-line distance between the two points in multi-dimensional space). However, Euclidean distance fails for text because document length skews the distance. A 1,000-word article about "cats" will have massive term frequencies compared to a 10-word tweet about "cats", putting them very far apart in space, even though they share the exact same topic.

## 2. Cosine Similarity
Instead of measuring the distance between the points, we measure the **angle** between the two vectors originating from zero. 
- If two vectors point in the exact same direction, the angle is 0. $\cos(0) = 1.0$ (Identical).
- If two vectors are orthogonal (perpendicular), they share no terms. The angle is 90 degrees. $\cos(90) = 0.0$ (Completely dissimilar).

Because text vectors (TF-IDF/BoW) cannot have negative values (you can't have a word appear -5 times), cosine similarity for text is always between `0.0` and `1.0`.

## 3. The Cosine Similarity Formula
The cosine of the angle between two vectors $\vec{v}$ and $\vec{w}$ is the dot product of the vectors divided by the product of their magnitudes (lengths).

$$ \text{Cosine Similarity} = \frac{\vec{v} \cdot \vec{w}}{|\vec{v}| |\vec{w}|} $$

### The Dot Product
Multiply the corresponding elements of both vectors and sum them up.
$$ \vec{v} \cdot \vec{w} = \sum_{i=1}^{n} v_i \times w_i $$

### The Magnitude (L2 Norm)
The square root of the sum of the squared elements of the vector.
$$ |\vec{v}| = \sqrt{\sum_{i=1}^{n} (v_i)^2} $$

## 4. Numerical Problem Walkthrough

**Problem**: Find the cosine similarity between Document 1 and Document 2 given the following TF vectors.
- $V = [\text{apple}, \text{banana}, \text{cherry}]$
- $D_1 = [2, 1, 0]$
- $D_2 = [1, 1, 1]$

**Step 1: Calculate Dot Product**
$$ D_1 \cdot D_2 = (2 \times 1) + (1 \times 1) + (0 \times 1) = 2 + 1 + 0 = 3 $$

**Step 2: Calculate Magnitudes**
$$ |D_1| = \sqrt{2^2 + 1^2 + 0^2} = \sqrt{4 + 1 + 0} = \sqrt{5} \approx 2.236 $$
$$ |D_2| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{1 + 1 + 1} = \sqrt{3} \approx 1.732 $$

**Step 3: Calculate Cosine Similarity**
$$ \text{Similarity} = \frac{3}{\sqrt{5} \times \sqrt{3}} = \frac{3}{\sqrt{15}} = \frac{3}{3.873} \approx 0.774 $$

## 5. Vector Normalization
If you **normalize** your vectors to have a length/magnitude of 1.0 before comparing them (by dividing every element by the magnitude), the denominator of the cosine similarity equation becomes $1 \times 1 = 1$. 

In this case, the Cosine Similarity is simply equal to the Dot Product. This is highly computationally efficient and is the standard practice in NLP and deep learning.

## 6. Exam Preparation
### Must Memorize
- The formulas for Dot Product and Magnitude.
- Cosine similarity measures the *angle* between vectors, making it immune to differences in document length.

### Likely Practical Question
**Question**: Document A and Document B share zero words in common. What is their cosine similarity and why?
**Answer**: Their cosine similarity is $0.0$. Because they share no words, at least one vector will have a $0$ at every index where the other has a value. When calculating the dot product $\sum (v_i \times w_i)$, every multiplication will involve a zero, resulting in a dot product of $0$, which makes the entire similarity equation $0$.
