```python
import re

def flag_aggressive_promotion(text):
    """
    Function to detect aggressive self-promotion in text.
    
    Args:
    text (str): Input text that needs to be checked for aggressive self-promotion.
    
    Returns:
    bool: True if aggressive self-promotion is detected, False otherwise.
    """
    # Define aggressive self-promotion patterns
    promotion_patterns = [
        r"\bbuy now\b",
        r"\bnot to be missed\b",
        r"\bguarantee\b",
        r"\blimited time\b",
        r"\bexclusive offer\b",
        r"\bact now\b",
        r"\bfree trial\b",
        r"\bonce in a lifetime\b",
        r"\bunbeatable\b",
        r"\bno risk\b",
        r"\bhot deal\b",
        r"\bsave big\b",
        r"\bdiscount\b",
        r"\bdeal\b",
        r"\boffer\b",
        r"\bpromo\b",
        r"\bspecial\b"
    ]
    
    # Check if any of the promotion patterns are in the text
    for pattern in promotion_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    
    return False

# Example usage
text_input = "Check out this once in a lifetime offer! Limited time only!"
flagged = flag_aggressive_promotion(text_input)
print("Aggressive promotion detected:" if flagged else "No aggressive promotion detected.")
```

This Python function `flag_aggressive_promotion` checks if a given text contains phrases typically associated with aggressive self-promotion. It uses regular expressions to search for these patterns. Adjust the list of patterns as needed based on what is considered too aggressive in your context.