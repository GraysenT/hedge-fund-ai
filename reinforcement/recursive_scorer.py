```python
def score_paths(signal_paths):
    """
    Recursively scores signal paths based on their fidelity and complexity.
    Each path is a tuple (fidelity, complexity).

    Args:
    signal_paths (list of tuples): List of paths where each path is represented as a tuple (fidelity, complexity).

    Returns:
    int: The highest score calculated from the paths.
    """
    if not signal_paths:
        return 0

    def score_path(index, current_fidelity, current_complexity):
        if index == len(signal_paths):
            # Calculate score: here, we assume a simple scoring function
            return current_fidelity - current_complexity

        # Include this path
        path_fidelity, path_complexity = signal_paths[index]
        include_score = score_path(index + 1, current_fidelity + path_fidelity, current_complexity + path_complexity)

        # Exclude this path
        exclude_score = score_path(index + 1, current_fidelity, current_complexity)

        # Return the maximum score between including and excluding the current path
        return max(include_score, exclude_score)

    # Start recursive scoring from the first path
    return score_path(0, 0, 0)

# Example usage
paths = [(10, 3), (15, 5), (20, 10)]
print(score_paths(paths))  # Output will depend on the scoring logic defined in score_path
```