# Advanced Regex and Python implementations

## 1. Greedy vs Non-Greedy Matching
By default, regex quantifiers (`*`, `+`, `?`, `{m,n}`) are **greedy**. They match as *much* text as possible.

### The Greedy Problem
Suppose you have HTML text: `<div>Hello</div><div>World</div>`
And you want to extract `<div>Hello</div>`.
You write the regex: `<div>.*</div>`
- **Result**: It matches the ENTIRE string `<div>Hello</div><div>World</div>` because `.*` greedily consumes everything until the *last* `</div>`.

### The Non-Greedy Solution
Appending a `?` to a quantifier makes it **non-greedy** (lazy). It matches as *little* text as possible.
- Regex: `<div>.*?</div>`
- **Result**: It correctly matches `<div>Hello</div>` and `<div>World</div>` separately.

## 2. Capturing Groups
Parentheses `()` do more than just group logic; they **capture** the text that was matched by the regex inside them so it can be extracted later.

If you match `(\w+)@(\w+\.\w+)` against "test@example.com":
- Group 0 (the full match): "test@example.com"
- Group 1: "test"
- Group 2: "example.com"

## 3. Python `re` Module Functions
Python handles regex through the built-in `re` module.

### `re.search(pattern, string)`
Scans through a string, looking for the **first location** where the pattern produces a match. Returns a Match object or `None`.
```python
import re
match = re.search(r'\d+', 'I have 2 apples and 3 bananas')
print(match.group()) # Output: '2'
```

### `re.match(pattern, string)`
Only looks for a match at the **absolute beginning** of the string.
```python
match1 = re.match(r'\d+', '2 apples') # Matches '2'
match2 = re.match(r'\d+', 'I have 2') # Returns None
```

### `re.findall(pattern, string)`
Finds **all** non-overlapping matches and returns them as a list of strings.
```python
print(re.findall(r'\d+', 'I have 2 apples and 3 bananas')) 
# Output: ['2', '3']
```

### `re.finditer(pattern, string)`
Like `findall`, but returns an iterator of Match objects, allowing you to get the span (start and end indices) of each match.
```python
for m in re.finditer(r'\d+', 'A 2 B 3'):
    print(f"Found {m.group()} at {m.span()}")
```

### `re.sub(pattern, repl, string)`
Replaces occurrences of the pattern with the replacement string. Extremely useful for text cleaning.
```python
clean = re.sub(r'\d+', 'NUM', 'Call 911 for emergency 112')
print(clean) # Output: 'Call NUM for emergency NUM'
```

### `re.split(pattern, string)`
Splits the string by the occurrences of the pattern.
```python
parts = re.split(r'\s*,\s*', 'apple, banana , cherry')
print(parts) # Output: ['apple', 'banana', 'cherry']
```

## 4. Exam Preparation
### Must Be Able To Calculate
Know the difference in output between `.*` and `.*?`.

### Likely Practical Question
**Question**: Write a Python script using the `re` module that replaces all vowels in a string with an underscore `_`.
**Answer**:
```python
import re
text = "Natural Language Processing"
result = re.sub(r'[aeiouAEIOU]', '_', text)
```
