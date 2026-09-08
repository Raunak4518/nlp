# Regex Fundamentals

## 1. What Is It?
A Regular Expression (Regex) is a sequence of characters that specifies a search pattern in text. Originally developed in theoretical computer science to describe formal/regular languages, regex is now the standard engineering tool for text searching, validation, and tokenization.

---

## 2. Literal Characters
The simplest regex is a string of literal characters.
- **Regex**: `cat`
- **Matches**: "**cat**", "The **cat** sat", "s**cat**ter"

---

## 3. Metacharacters & Wildcards
Metacharacters have special meaning to the regex engine.

| Metacharacter | Name | Function | Example Regex | Matches |
| :--- | :--- | :--- | :--- | :--- |
| `.` | Wildcard | Matches *any* single character except a newline. | `c.t` | "cat", "cot", "cut", "c!t" |
| `\` | Escape | Removes the special meaning of a metacharacter. | `c\.t` | *Only* matches "c.t" |

---

## 4. Character Classes `[...]`
Matches exactly *one* character from a specified set.
- **Regex**: `c[aeiou]t` 
- **Matches**: "cat", "cot", "cut". (Does NOT match "cbt").

### Continuous Ranges
You can specify continuous sequences inside character classes using a hyphen `-`.
- `[a-z]`: Any single lowercase English letter.
- `[A-Z]`: Any single uppercase English letter.
- `[0-9]`: Any single digit from 0 to 9.
- `[a-zA-Z0-9]`: Any single alphanumeric character.

### Negated Classes `[^...]`
Placing a caret `^` immediately inside the bracket negates the entire set.
- **Regex**: `[^aeiou]`
- **Matches**: Any single character that is NOT a vowel.

---

## 5. Shorthand Character Classes
Because certain classes are used so frequently, regex provides backslash shortcuts.
Notice how the uppercase version is always the exact mathematical negation of the lowercase version.

| Shorthand | Meaning | Equivalent Bracket Syntax |
| :--- | :--- | :--- |
| `\d` | Any digit | `[0-9]` |
| `\D` | Any non-digit | `[^0-9]` |
| `\w` | Any word character (alphanumeric + underscore) | `[a-zA-Z0-9_]` |
| `\W` | Any non-word character | `[^a-zA-Z0-9_]` |
| `\s` | Any whitespace (space, tab, newline) | `[ \t\n\r\f\v]` |
| `\S` | Any non-whitespace character | `[^ \t\n\r\f\v]` |

---

## 6. Quantifiers
Quantifiers specify *how many times* the preceding character or group should be matched.

| Quantifier | Name | Meaning | Example Regex | Matches |
| :--- | :--- | :--- | :--- | :--- |
| `*` | Asterisk | 0 or more times | `ab*c` | "ac", "abc", "abbbc" |
| `+` | Plus | 1 or more times | `ab+c` | "abc", "abbbc" (NOT "ac") |
| `?` | Question | 0 or 1 time (optional) | `colou?r` | "color", "colour" |
| `{m,n}` | Range | Between $m$ and $n$ times inclusive | `a{2,4}` | "aa", "aaa", "aaaa" |

---

## 7. Anchors `^` and `$`
Anchors are unique: they do not match actual characters; they match *physical positions* in the string.
- **`^` (Start)**: Matches the absolute start of a string.
  - `^The` matches "The dog", but NOT "I saw The dog".
- **`$` (End)**: Matches the absolute end of a string.
  - `end$` matches "The end", but NOT "endless".

---

## 8. Grouping `()` and Alternation `|`
- **`|` (OR)**: Matches either the expression before or after it.
  - `cat|dog` matches "cat" or "dog".
- **`()` (Grouping)**: Applies operators to a whole sequence rather than a single character.
  - `(cat|dog)s` matches "cats" or "dogs". Without the parentheses, `cat|dogs` would match "cat" or "dogs".

---

## 9. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: What exactly does the regex `^[A-Z][a-z]+$` match? Break down each component.
> **Answer**: It strictly matches a string that consists of exactly one capitalized word, with no spaces or punctuation.
> 1. `^` ensures the match starts at the absolute beginning of the string.
> 2. `[A-Z]` matches exactly one uppercase letter.
> 3. `[a-z]+` matches one or more lowercase letters.
> 4. `$` ensures the string ends immediately after the lowercase letters.
> *Example Match*: "Hello"
> *Example Failures*: "Hello World" (contains space), "HELLO" (contains trailing uppercase letters).

> [!WARNING]
> **The Dual Use of the Caret `^`**
> A very common exam trap is testing if you know the difference between `^` inside brackets vs outside. 
> `^a` means "The string must *start* with 'a'". 
> `[^a]` means "Match any character that is *not* 'a'".

---

### Can You Explain This?
- [ ] I can list the definitions of `\w`, `\s`, and `\d` and their uppercase negations.
- [ ] I can explain the difference between the `*` and `+` quantifiers.
- [ ] I understand the difference between `^` as an anchor and `^` as a negation.
- [ ] I know why parentheses are necessary when using the `|` (OR) operator with suffixes.
