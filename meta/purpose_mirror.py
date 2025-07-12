```python
def behavior_matches_intent(daily_behaviors, long_term_intent):
    """
    Function to check if daily behaviors match the long-term intent.
    
    Parameters:
        daily_behaviors (list of str): List of daily behaviors.
        long_term_intent (str): Description of the long-term intent.
    
    Returns:
        bool: True if daily behaviors match the long-term intent, False otherwise.
    """
    # Convert long-term intent into a set of keywords
    intent_keywords = set(long_term_intent.lower().split())
    
    # Check if any daily behavior matches any of the keywords in the long-term intent
    for behavior in daily_behaviors:
        behavior_keywords = set(behavior.lower().split())
        if behavior_keywords & intent_keywords:
            return True
    
    return False

# Example usage:
daily_behaviors = ["exercise at gym", "read a book", "work on a project"]
long_term_intent = "improve health and fitness"
result = behavior_matches_intent(daily_behaviors, long_term_intent)
print("Do daily behaviors match long-term intent?", result)
```