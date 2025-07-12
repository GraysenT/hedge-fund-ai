Below is a Python code that simulates encoding a simple logic structure into a DNA-like sequence. This code uses a basic mapping from binary (representing simple logic gates) to a DNA sequence (using the bases A, C, G, T). It also includes functions to clone and mutate these DNA sequences.

```python
import random

# Define a mapping from binary to DNA
binary_to_dna = {
    '00': 'A',  # Adenine
    '01': 'C',  # Cytosine
    '10': 'G',  # Guanine
    '11': 'T'   # Thymine
}

dna_to_binary = {v: k for k, v in binary_to_dna.items()}

# Logic gates represented in binary
logic_gates = {
    'AND': '00',
    'OR': '01',
    'NOT': '10',
    'XOR': '11'
}

def encode_logic_to_dna(logic):
    """ Encodes a list of logic gates to a DNA sequence. """
    dna_sequence = ''
    for gate in logic:
        binary = logic_gates[gate]
        dna_sequence += binary_to_dna[binary[:2]]
    return dna_sequence

def decode_dna_to_logic(dna_sequence):
    """ Decodes a DNA sequence back to a list of logic gates. """
    logic = []
    for i in range(0, len(dna_sequence)):
        dna_base = dna_sequence[i]
        binary = dna_to_binary[dna_base]
        for gate, bin_code in logic_gates.items():
            if bin_code == binary:
                logic.append(gate)
                break
    return logic

def clone_dna(dna_sequence):
    """ Clones the DNA sequence. """
    return dna_sequence

def mutate_dna(dna_sequence, mutation_rate=0.1):
    """ Mutates the DNA sequence based on a mutation rate. """
    dna_bases = list(dna_sequence)
    for i in range(len(dna_bases)):
        if random.random() < mutation_rate:
            # Choose a random mutation
            possible_mutations = list(set('ACGT') - set(dna_bases[i]))
            dna_bases[i] = random.choice(possible_mutations)
    return ''.join(dna_bases)

# Example usage
logic_circuit = ['AND', 'OR', 'NOT', 'XOR']
dna_encoded = encode_logic_to_dna(logic_circuit)
print("Encoded DNA:", dna_encoded)

decoded_logic = decode_dna_to_logic(dna_encoded)
print("Decoded Logic:", decoded_logic)

cloned_dna = clone_dna(dna_encoded)
print("Cloned DNA:", cloned_dna)

mutated_dna = mutate_dna(dna_encoded, mutation_rate=0.3)
print("Mutated DNA:", mutated_dna)
print("Decoded Mutated Logic:", decode_dna_to_logic(mutated_dna))
```

This code provides a simplistic model for encoding logic gates into a DNA sequence, cloning it, and introducing mutations. The mutation function randomly changes bases in the DNA sequence based on a specified mutation rate. The encoding and decoding functions map logic gates to DNA sequences and vice versa.