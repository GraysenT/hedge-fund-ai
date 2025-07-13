Here is a Python script using the `sympy` library to create symbolic identities for major logic branches and agents. This script defines symbols for different logic agents and computes various logical operations among them.

```python
from sympy import symbols, And, Or, Not, Implies, Equivalent

# Define symbols for logic agents
A, B, C = symbols('A B C')

# Logical operations
and_operation = And(A, B)
or_operation = Or(A, B)
not_operation = Not(A)
implies_operation = Implies(A, B)
equivalent_operation = Equivalent(A, B)

# Print results of logical operations
print("A AND B:", and_operation)
print("A OR B:", or_operation)
print("NOT A:", not_operation)
print("A IMPLIES B:", implies_operation)
print("A EQUIVALENT TO B:", equivalent_operation)

# More complex logic involving multiple agents
complex_logic = And(A, Or(B, Not(C)))
print("Complex Logic (A AND (B OR NOT C)):", complex_logic)

# Simplifying expressions
from sympy import simplify
simplified_expression = simplify(Implies(A, Or(A, B)))
print("Simplified Expression of Implies(A, Or(A, B)):", simplified_expression)

# Using logical equivalence
equivalence_test = Equivalent(And(A, B), Or(Not(A), Not(B)))
print("Testing Equivalence of (A AND B) and (NOT A OR NOT B):", equivalence_test)
```

This script uses basic logical operations such as AND, OR, NOT, IMPLIES, and EQUIVALENT. It also demonstrates how to define symbols for logic agents, perform operations on them, and simplify expressions using `sympy`. This can be extended or modified to include more complex logic structures and additional agents as needed.