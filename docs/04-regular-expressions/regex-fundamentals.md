# Regex Fundamentals

## 1. What Is It?
A Regular Expression (Regex) is a sequence of characters that specifies a search pattern in text. Originally developed in theoretical computer science to describe regular languages, regex is now the standard tool for text searching, validation, and tokenization.

## 2. Literal Characters
The simplest regex is a string of literal characters.
- Regex: `cat`
- Matches: "**cat**", "The **cat** sat", "s**cat**ter"

## 3. Metacharacters & Wildcards
Metacharacters have special meaning.
- **`.` (Wildcard)**: Matches *any* single character except a newline.
  - Regex: `c.t` matches "cat", "cot", "cut", "c!t".
- **`\` (Escape)**: Removes the special meaning of a metacharacter.
  - Regex: `c\.t` matches *only* "c.t".

## 4. Character Classes `[]`
Matches exactly *one* character from a specified set.
- Regex: `c[aeiou]t` matches "cat", "cot", "cut". (Does NOT match "cbt").

### Ranges
You can specify continuous ranges inside character classes.
- `[a-z]`: Any lowercase English letter.
- `[A-Z]`: Any uppercase English letter.
- `[0-9]`: Any digit from 0 to 9.
- `[a-zA-Z0-9]`: Any alphanumeric character.

### Negated Classes `[^...]`
Placing a caret `^` immediately inside the bracket negates the set.
- Regex: `[^aeiou]` matches any character that is NOT a vowel.

## 5. Shorthand Character Classes
Python provides shortcuts for common classes:
- **`\d`**: Any digit. Equivalent to `[0-9]`.
- **`\D`**: Any non-digit. Equivalent to `[^0-9]`.
- **`\w`**: Any word character (alphanumeric + underscore). Equivalent to `[a-zA-Z0-9_]`.
- **`\W`**: Any non-word character.
- **`\s`**: Any whitespace (space, tab, newline). Equivalent to `[ \t\n\r\f\v]`.
- **`\S`**: Any non-whitespace character.

## 6. Quantifiers
Quantifiers specify *how many times* the preceding character or group should be matched.

- **`*` (Asterisk)**: 0 or more times.
  - `ab*c` matches "ac", "abc", "abbbc".
- **`+` (Plus)**: 1 or more times.
  - `ab+c` matches "abc", "abbbc", but NOT "ac".
- **`?` (Question Mark)**: 0 or 1 time (optional).
  - `colou?r` matches "color" or "colour".
- **`{m,n}`**: Between *m* and *n* times (inclusive).
  - `a{2,4}` matches "aa", "aaa", "aaaa".

## 7. Anchors `^` and `$`
Anchors do not match characters; they match *positions*.
- **`^` (Start)**: Matches the start of a string.
  - `^The` matches "The dog", but NOT "I saw The dog".
- **`$` (End)**: Matches the end of a string.
  - `end$` matches "The end", but NOT "endless".

## 8. Grouping `()` and Alternation `|`
- **`|` (OR)**: Matches either the expression before or after it.
  - `cat|dog` matches "cat" or "dog".
- **`()` (Grouping)**: Applies operators to a whole sequence.
  - `(cat|dog)s` matches "cats" or "dogs".

## 9. Exam Preparation
### Must Memorize
- The difference between `*` (0 or more) and `+` (1 or more).
- The definition of `\w` vs `\W` and `\s` vs `\S`.
- The dual use of `^` (Start anchor outside brackets, Negation inside brackets).

### Likely Theory Question
**Question**: What exactly does the regex `^[A-Z][a-z]+$` match?
**Answer**: It strictly matches a string that consists of exactly one capitalized word. `^` ensures it starts at the beginning of the string. `[A-Z]` matches exactly one uppercase letter. `[a-z]+` matches one or more lowercase letters. `$` ensures the string ends immediately after. It would match "Hello", but not "Hello World" or "HELLO".
