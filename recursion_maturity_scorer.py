```python
def evaluate_logic_path(path):
    """
    Evaluates a recursive logic path based on clarity, depth, and productive output.
    
    Args:
    path (str): A string representation of the recursive logic path.

    Returns:
    tuple: A tuple containing scores for clarity, depth, and productive output.
    """
    # Define scoring criteria
    clarity_score = 0
    depth_score = 0
    output_score = 0
    
    # Evaluate clarity: fewer nested conditions and clear variable names improve clarity
    clarity_indicators = ['if', 'else', 'elif', 'while', 'for']
    nested_depth = 0
    max_depth = 0
    
    lines = path.split('\n')
    for line in lines:
        stripped_line = line.strip()
        
        # Calculate nesting depth
        current_depth = (len(line) - len(stripped_line)) // 4  # assuming 4 spaces per indent level
        if any(indicator in stripped_line for indicator in clarity_indicators):
            nested_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
    
    # Clarity score decreases with the number of nested structures
    clarity_score = max(10 - nested_depth, 0)
    
    # Depth score is based on the maximum depth of recursion
    depth_score = max_depth
    
    # Productive output score: checks if the path returns or yields useful results
    productive_keywords = ['return', 'yield']
    output_lines = [line.strip() for line in lines if any(keyword in line for keyword in productive_keywords)]
    output_score = len(output_lines)
    
    return clarity_score, depth_score, output_score

# Example usage
recursive_logic = """
def recursive_function(n):
    if n > 0:
        return recursive_function(n-1)
    else:
        return n
"""

clarity, depth, output = evaluate_logic_path(recursive_logic)
print(f"Clarity Score: {clarity}, Depth Score: {depth}, Output Score: {output}")
```