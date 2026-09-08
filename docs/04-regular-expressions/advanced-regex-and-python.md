# Advanced Regex and Python Implementations

## 1. Greedy vs. Non-Greedy Matching
By default, regex quantifiers (`*`, `+`, `?`, `{m,n}`) are **greedy**. They match as *much* text as possible while still allowing the overall pattern to match.

### The Greedy Problem
Suppose you have an HTML string and you want to extract the first `<div>` tag.
- **Text**: `"<div>Hello</div><div>World</div>"`
- **Regex**: `<div>.*</div>`

You might expect it to match `<div>Hello</div>`. 
**Result**: It matches the ENTIRE string `"<div>Hello</div><div>World</div>"`. 
**Why?**: Because `.*` greedily consumes everything in the string. It goes all the way to the end, then backtracks just enough to find the *last* `</div>`.

### The Non-Greedy Solution
Appending a `?` to a quantifier makes it **non-greedy** (or lazy). It matches as *little* text as possible.
- **Regex**: `<div>.*?</div>`
- **Result**: It correctly matches `"<div>Hello</div>"`. The `.*?` stops at the *first* `</div>` it sees.

---

## 2. Capturing Groups
Parentheses `()` do more than just group logic for OR statements; they **capture** the text that was matched by the regex inside them so it can be extracted later.

If you match `(\w+)@(\w+\.\w+)` against `"test@example.com"`:
- **Group 0** (The full match): `"test@example.com"`
- **Group 1** (The first set of parentheses): `"test"`
- **Group 2** (The second set of parentheses): `"example.com"`

This is incredibly useful for information extraction, allowing you to split the username and domain of an email instantly.

---

## 3. Python's `re` Module

Python handles regex through the built-in `re` module. Here are the 5 essential functions you must know.

| Function | Purpose | Returns |
| :--- | :--- | :--- |
| `re.search()` | Scans the whole string for the **first** match. | `Match` object or `None` |
| `re.match()` | Checks for a match ONLY at the **absolute start** of the string. | `Match` object or `None` |
| `re.findall()` | Finds **all** non-overlapping matches. | `List` of strings |
| `re.finditer()`| Like findall, but provides positions. | Iterator of `Match` objects |
| `re.sub()` | Replaces matches with a new string. | `String` |

### Try It Yourself

??? question "Trace `re.match()` vs `re.search()`"
    ```python
    import re
    text = "I have 2 apples"
    
    # re.match only looks at the start ("I"). It fails.
    print(re.match(r'\d+', text)) # Output: None
    
    # re.search scans until it finds the first match.
    print(re.search(r'\d+', text).group()) # Output: '2'
    ```

??? question "Trace `re.sub()` for Text Cleaning"
    ```python
    import re
    text = "Call 911 for emergency 112"
    
    # Replace all digit blocks with the string 'NUM'
    clean = re.sub(r'\d+', 'NUM', text)
    print(clean) # Output: 'Call NUM for emergency NUM'
    ```

---

## 4. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Explain the difference between Greedy and Non-Greedy regex matching. Provide a regex example and a sample string to illustrate your point.
> **Answer**: Greedy quantifiers (like `*` or `+`) match as much text as possible. Non-greedy (lazy) quantifiers (created by appending `?`, like `*?` or `+?`) match as little text as possible. 
> For example, given the string `<bold>text</bold>`:
> - The greedy regex `<.*>` will match the entire string `<bold>text</bold>` because `.*` consumes everything until the final `>`.
> - The non-greedy regex `<.*?>` will match only `<bold>` because `.*?` stops at the first `>` it encounters.

**3-Mark Question**: Write a Python script using the `re` module that takes a string and replaces all vowels (both lowercase and uppercase) with an underscore `_`.
> **Answer**:
> ```python
> import re
> text = "Natural Language"
> result = re.sub(r'[aeiouAEIOU]', '_', text)
> # result is "N_t_r_l L_ng__g_"
> ```

---

### Can You Explain This?
- [ ] I can explain why `.*` is greedy and how to make it non-greedy.
- [ ] I understand the difference between `re.search` and `re.match` in Python.
- [ ] I can write a `re.sub` command to perform basic text replacement.
- [ ] I can explain what a capturing group is.
