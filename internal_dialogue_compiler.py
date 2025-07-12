Below is a Python script that simulates recursive internal debates and compiles them into explainable transcripts. The script uses a recursive function to simulate the process of internal debating on a topic, with each level of recursion representing a deeper layer of thought or counterargument. The results are then formatted into a readable transcript.

```python
def debate_topic(topic, depth, max_depth):
    """
    Recursively debates a topic, generating a transcript of the internal debate.
    
    Args:
    topic (str): The topic being debated.
    depth (int): Current depth of recursion.
    max_depth (int): Maximum depth of recursion allowed.
    
    Returns:
    str: A formatted string representing the debate at the current level.
    """
    indent = "  " * depth  # Create indentation based on recursion depth
    if depth == max_depth:
        return f"{indent}Conclusion on '{topic}': reached maximum depth of reasoning.\n"

    # Simulate internal debate
    pro_argument = f"{indent}Pro Argument on '{topic}': It is beneficial because of reason {depth}.\n"
    con_argument = f"{indent}Con Argument on '{topic}': It might be problematic because of issue {depth}.\n"
    
    # Recurse deeper into the debate
    deeper_pro_debate = debate_topic(topic + f" (reason {depth})", depth + 1, max_depth)
    deeper_con_debate = debate_topic(topic + f" (issue {depth})", depth + 1, max_depth)
    
    # Compile the debate at this level
    debate_transcript = pro_argument + deeper_pro_debate + con_argument + deeper_con_debate
    return debate_transcript

def compile_debate(topic, max_depth):
    """
    Initiates the debate on a topic and compiles the transcript.
    
    Args:
    topic (str): The topic to be debated.
    max_depth (int): Maximum depth of recursion for the debate.
    
    Returns:
    str: The complete transcript of the debate.
    """
    initial_statement = f"Initiating debate on the topic: '{topic}'\n"
    debate_transcript = debate_topic(topic, 0, max_depth)
    return initial_statement + debate_transcript

# Example usage
topic = "the adoption of renewable energy"
max_depth = 3
transcript = compile_debate(topic, max_depth)
print(transcript)
```

This script defines a recursive function `debate_topic` that generates arguments for and against a topic, diving deeper into each argument recursively. The `compile_debate` function starts the debate and compiles the entire transcript. The example usage at the end of the script initiates a debate on "the adoption of renewable energy" with a maximum recursion depth of 3. Adjust the `topic` and `max_depth` as needed to explore different topics or levels of debate complexity.