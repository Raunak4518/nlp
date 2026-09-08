# Nondeterministic Finite Automata (NFA)

## 1. What is an NFA?
A Nondeterministic Finite Automaton (NFA) relaxes the strict rules of a DFA. In an NFA:
1. **Multiple Transitions**: A single state can have *multiple* valid transitions for the *same* input symbol.
2. **Missing Transitions**: A state might have *no* valid transition for a specific input symbol (which causes that path to die/reject).
3. **Epsilon ($\epsilon$) Transitions**: An NFA can transition from one state to another *without reading any input symbol at all*.

## 2. Intuition
Imagine walking through a maze. 
- In a **DFA**, at every intersection, there is a sign telling you exactly which way to go based on the color of your ticket.
- In an **NFA**, you might arrive at an intersection and see *two* signs for a "red" ticket. You have to "guess" which path leads to the exit. If you guess wrong and hit a dead end, you have to backtrack and try the other path.

An NFA **accepts** a string if there exists *at least one* valid path through the machine that consumes the entire string and ends in an accepting state.

## 3. DFA vs NFA
| Feature | DFA | NFA |
|---------|-----|-----|
| Transitions per symbol | Exactly one | Zero, one, or multiple |
| Empty transitions ($\epsilon$) | Not allowed | Allowed |
| Execution | Simple, linear | Complex, requires search/backtracking |
| Expressive Power | Equal | Equal (Kleene's Theorem) |

*Important*: Even though NFAs seem more powerful because they can "guess", any NFA can be converted into an equivalent DFA using the **Subset Construction Algorithm**.

## 4. Scratch Implementation (NFA Recognizer)
Because an NFA can be in multiple states simultaneously (or requires backtracking), we implement it by keeping track of the *set* of all possible states the machine could currently be in.

```python
class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def get_epsilon_closure(self, state_set: set) -> set:
        """Finds all states reachable via empty string (epsilon) transitions."""
        closure = set(state_set)
        stack = list(state_set)
        
        while stack:
            current = stack.pop()
            # If there are epsilon transitions from this state
            if current in self.transition_function and '' in self.transition_function[current]:
                for next_state in self.transition_function[current]['']:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def recognize(self, string: str) -> bool:
        # Start at the epsilon closure of the start state
        current_states = self.get_epsilon_closure({self.start_state})
        
        for symbol in string:
            if symbol not in self.alphabet:
                return False
                
            next_states = set()
            for state in current_states:
                # If there's a transition for this symbol
                if state in self.transition_function and symbol in self.transition_function[state]:
                    for target_state in self.transition_function[state][symbol]:
                        next_states.add(target_state)
            
            # Update current states, including any new epsilon transitions
            current_states = self.get_epsilon_closure(next_states)
            
        # Accept if the intersection of current states and accept states is not empty
        return not current_states.isdisjoint(self.accept_states)

# Define an NFA that accepts strings ending in 'ab' over {a, b}
# It stays in q0 on any input, but can "guess" when the end is near and jump to q1
transitions = {
    'q0': {'a': ['q0', 'q1'], 'b': ['q0']},
    'q1': {'b': ['q2']},
    'q2': {}
}

nfa = NFA(
    states={'q0', 'q1', 'q2'},
    alphabet={'a', 'b'},
    transition_function=transitions,
    start_state='q0',
    accept_states={'q2'}
)

print(nfa.recognize("aab")) # True
print(nfa.recognize("aba")) # False
```

## 5. Exam Preparation
### Must Know
- The definition of an Epsilon transition.
- Kleene's Theorem: NFAs and DFAs have exactly the same computational power.

### Likely Theory Question
**Question**: Since NFAs require complex backtracking or parallel state tracking (making them slower to execute than DFAs), why do we use them?
**Answer**: NFAs are vastly easier to construct from Regular Expressions. When you compile a Regex, the engine first builds an NFA because the logic perfectly mirrors the regex tree. It then converts that NFA into a highly optimized DFA for actual execution.
