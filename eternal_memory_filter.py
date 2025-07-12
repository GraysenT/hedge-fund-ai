```python
import numpy as np

class Memory:
    def __init__(self, content, long_term_value, mission_alignment):
        self.content = content
        self.long_term_value = long_term_value
        self.mission_alignment = mission_alignment

def filter_memories(memories, value_threshold, alignment_threshold):
    """
    Filters memories based on their long-term value and mission alignment.
    
    Parameters:
        memories (list of Memory): List of Memory objects.
        value_threshold (float): Minimum threshold for long-term value.
        alignment_threshold (float): Minimum threshold for mission alignment.
    
    Returns:
        list of Memory: Filtered list of memories.
    """
    filtered_memories = [
        memory for memory in memories
        if memory.long_term_value >= value_threshold and memory.mission_alignment >= alignment_threshold
    ]
    return filtered_memories

# Example usage
memories = [
    Memory("Memory 1", 0.9, 0.8),
    Memory("Memory 2", 0.4, 0.9),
    Memory("Memory 3", 0.7, 0.6),
    Memory("Memory 4", 0.95, 0.95)
]

value_threshold = 0.7
alignment_threshold = 0.7

filtered_memories = filter_memories(memories, value_threshold, alignment_threshold)

for memory in filtered_memories:
    print(f"Filtered Memory: {memory.content}, Value: {memory.long_term_value}, Alignment: {memory.mission_alignment}")
```