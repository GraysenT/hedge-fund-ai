```python
import random

def mutate_logic(base_logic, mutation_rate=0.1, mutation_amount=0.2):
    """
    Mutates a given logical function by randomly adjusting its parameters.
    
    Args:
    base_logic (function): A function representing the base logic.
    mutation_rate (float): The probability of each parameter being mutated.
    mutation_amount (float): The maximum amount by which a parameter can be mutated.
    
    Returns:
    function: A new function with mutated logic.
    """
    # Retrieve the original function's code
    import inspect
    source_code = inspect.getsource(base_logic)
    
    # Define possible mutations
    mutations = {
        '+': '-',
        '-': '+',
        '*': '/',
        '/': '*',
        '>': '<',
        '<': '>',
        '>=': '<=',
        '<=': '>='
    }
    
    # Convert the source code into a list of characters for mutation
    source_code_list = list(source_code)
    
    # Perform mutations based on the mutation rate
    for i in range(len(source_code_list)):
        if random.random() < mutation_rate:
            char = source_code_list[i]
            if char in mutations:
                # Apply mutation with a certain probability
                if random.random() < 0.5:
                    source_code_list[i] = mutations[char]
                else:
                    # Numeric mutation by adding/subtracting a small value
                    if char.isdigit():
                        new_value = str(max(0, int(char) + int(mutation_amount * random.choice([-1, 1]))))
                        source_code_list[i] = new_value
    
    # Join the mutated code back into a string
    mutated_code = ''.join(source_code_list)
    
    # Compile the new function
    exec(mutated_code, globals())
    
    # Return the new function assuming the original function is named 'base_logic'
    return base_logic

# Example usage
def base_logic(x):
    return x * 2 + 10 > 20

# Mutate the base logic
mutated_logic = mutate_logic(base_logic)

# Test the mutated logic
print(mutated_logic(5))  # Output may vary due to random mutation
```