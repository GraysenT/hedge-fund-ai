Here is a Python code that decodes DNA strings into executable logic fragments for reuse. This example assumes a simple mapping from DNA bases to Python code snippets, which you can extend or modify according to your specific requirements:

```python
def dna_to_code(dna_sequence):
    # Define a mapping from DNA bases to Python code snippets
    dna_to_python = {
        'A': 'print("Hello, World!")',  # Example Python code for 'A'
        'T': 'x = 10',                  # Example Python code for 'T'
        'C': 'if x > 5: print("x is greater than 5")',  # Example Python code for 'C'
        'G': 'for i in range(x): print(i)',             # Example Python code for 'G'
    }

    # Split the DNA sequence into individual characters
    dna_bases = list(dna_sequence)

    # Convert each DNA base to the corresponding Python code
    code_fragments = [dna_to_python[base] for base in dna_bases if base in dna_to_python]

    # Join all code fragments into a single executable script
    executable_script = '\n'.join(code_fragments)

    return executable_script

def execute_dna_code(dna_sequence):
    # Convert the DNA sequence to Python code
    python_code = dna_to_code(dna_sequence)

    # Execute the generated Python code
    exec(python_code)

# Example DNA sequence
dna_sequence = "ATCG"

# Execute the code generated from the DNA sequence
execute_dna_code(dna_sequence)
```

This script defines two functions:
1. `dna_to_code`: Converts a DNA sequence into Python code based on predefined mappings.
2. `execute_dna_code`: Executes the Python code generated from a DNA sequence.

You can modify the `dna_to_python` dictionary to include more complex mappings or to handle different logic based on your application's needs.