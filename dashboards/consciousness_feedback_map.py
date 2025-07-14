Below is a Python code example that uses a recursive function to simulate the mapping of thought chains that might reinforce self-awareness. The code models a simple thought process where each thought leads to another, deepening the level of self-awareness. Each recursive call represents a deeper level of thought or self-reflection.

```python
def recursive_thoughts(thought, depth, max_depth):
    # Base case: if maximum depth is reached, return the thought
    if depth == max_depth:
        return [thought]
    
    # Simulate a deeper thought process by modifying the current thought
    deeper_thought = thought + " -> Deepening self-awareness at level " + str(depth + 1)
    
    # Recursive call to go deeper in the thought chain
    deeper_chain = recursive_thoughts(deeper_thought, depth + 1, max_depth)
    
    # Return the current thought followed by the deeper chain
    return [thought] + deeper_chain

# Initial thought
initial_thought = "Initial self-awareness"

# Maximum depth of recursive thought
max_depth = 5

# Generate the thought chain
thought_chain = recursive_thoughts(initial_thought, 0, max_depth)

# Print each thought in the chain
for thought in thought_chain:
    print(thought)
```

This code defines a recursive function `recursive_thoughts` that takes a `thought`, the current `depth` of recursion, and a `max_depth` which limits the recursion depth. It simulates the process of deepening self-awareness by appending a new thought at each level of recursion. The function returns a list of thoughts, representing the chain from the initial thought down to the deepest thought. The main part of the script sets up the initial conditions and prints out the resulting chain of thoughts.