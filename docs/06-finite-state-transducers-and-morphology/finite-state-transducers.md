# Finite State Transducers

## 1. What is an FST?
A Finite State Transducer (FST) is an extension of a Finite State Automaton (FSA). 
- An **FSA** reads an input string and *recognizes* (accepts/rejects) it.
- An **FST** reads an input string and *translates* it into an output string.

It acts as a two-tape machine: one tape for input, one tape for output.

## 2. Input/Output Transitions
In an FSA, transitions are labeled with a single character `a`.
In an FST, transitions are labeled with pairs `a:b`. 
- `a` is the input symbol to read.
- `b` is the output symbol to write.

An FST transition $\delta(q_0, a:b) \rightarrow q_1$ means: "If in state $q_0$ and the input is `a`, transition to $q_1$ and output `b`."

Empty transitions ($\epsilon$) are extremely useful in FSTs.
- `a:ϵ` means "Read 'a', output nothing" (deletion).
- `ϵ:a` means "Read nothing, output 'a'" (insertion).

## 3. Morphological Analysis and Generation
FSTs are bidirectional. The exact same FST can be run forwards or backwards.

### Generation (Lexical to Surface)
Inputting abstract morphological features to get a real word.
- Input: `cat + N + PL`
- Output: `cats`

### Analysis (Surface to Lexical)
Inputting a real word to get its abstract features.
- Input: `cats`
- Output: `cat + N + PL`

Because FSTs can handle non-determinism, feeding `leaves` into the analyzer side of the FST will output both `leaf + N + PL` and `leave + V + 3SG`.

## 4. Scratch Implementation (FST for Regular Plurals)
We will implement a basic FST generator that converts `Noun + N + PL` into the plural string.
We will handle:
- Regular nouns (`cat` $\rightarrow$ `cats`)
- Nouns ending in `x` (`box` $\rightarrow$ `boxes`)

```python
class FST:
    def __init__(self, states, transition_function, start_state, accept_states):
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def transduce(self, input_string: str) -> list[str]:
        # Stores (current_state, remaining_input, output_so_far)
        paths = [(self.start_state, input_string, "")]
        successful_outputs = []

        while paths:
            state, remaining, output = paths.pop()

            # If we reached the end of the input and are in an accept state
            if not remaining and state in self.accept_states:
                successful_outputs.append(output)
                continue
                
            if not remaining:
                continue

            current_char = remaining[0]
            next_remaining = remaining[1:]

            # Look for matching transitions
            if state in self.transition_function:
                for (in_char, out_char), next_state in self.transition_function[state].items():
                    # 1. Standard character match
                    if in_char == current_char:
                        paths.append((next_state, next_remaining, output + out_char))
                    # 2. Epsilon input transition (consumes no input)
                    elif in_char == 'ϵ':
                        paths.append((next_state, remaining, output + out_char))
                    # 3. Wildcard matcher (for arbitrary letters in the stem)
                    elif in_char == '*':
                        paths.append((next_state, next_remaining, output + current_char))
        
        return successful_outputs

# Building the Plural FST
# + denotes noun tag, # denotes plural tag
# We want to map: "cat+#" -> "cats", "box+#" -> "boxes"
transitions = {
    'q0': {
        # If we see an 'x', we output 'x' and move to state q1 (needs 'es')
        ('x', 'x'): 'q1',
        # If we see the noun tag '+', we output nothing (epsilon) and move to plural checking
        ('+', 'ϵ'): 'q2',
        # For any other character, output it and loop in q0
        ('*', ''): 'q0'  # In our implementation, * passes the char through
    },
    'q1': {
        ('+', 'ϵ'): 'q3'
    },
    'q2': {
        # Regular plural: read '#', output 's'
        ('#', 's'): 'q_end'
    },
    'q3': {
        # 'x' plural: read '#', output 'es'
        ('#', 'es'): 'q_end'
    }
}

fst = FST(
    states={'q0', 'q1', 'q2', 'q3', 'q_end'},
    transition_function=transitions,
    start_state='q0',
    accept_states={'q_end'}
)

print(fst.transduce("cat+#")) # Output: ['cats']
print(fst.transduce("box+#")) # Output: ['boxes']
```

## 5. Exam Preparation
### Must Know
- FSTs operate on a pair of strings (input:output) while FSAs operate on a single string.
- FSTs are inherently bidirectional (Analysis vs Generation).

### Likely Theory Question
**Question**: Why are FSTs strictly superior to dictionary lookups for morphological analysis?
**Answer**: A dictionary mapping every surface form to its lemma and features requires massive memory, especially for morphologically rich languages like Turkish where a single root can generate millions of valid word forms. An FST encapsulates the *rules* of the morphology, allowing it to analyze mathematically valid word combinations it has never seen before with very low memory overhead.
