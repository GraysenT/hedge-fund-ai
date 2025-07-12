```python
def tag_emotional_resonance(text):
    """
    Simple function to tag text with emotional resonance or interpretation.
    This function uses basic keyword matching for demonstration purposes.
    A more complex implementation might use NLP models to better understand context and sentiment.
    
    Args:
    text (str): Input text to analyze.
    
    Returns:
    str: Emotional tag based on the content of the text.
    """
    # Define simple keyword-emotion dictionary
    emotions = {
        "happy": ["happy", "joy", "pleased", "delighted", "excited"],
        "sad": ["sad", "unhappy", "sorrow", "depressed", "mournful"],
        "angry": ["angry", "mad", "furious", "irate", "annoyed"],
        "fearful": ["fear", "scared", "frightened", "terrified", "anxious"],
        "surprised": ["surprised", "amazed", "astonished", "shocked", "startled"]
    }
    
    # Normalize the text to lower case for matching
    text_lower = text.lower()
    
    # Check each emotion for associated keywords
    for emotion, keywords in emotions.items():
        for keyword in keywords:
            if keyword in text_lower:
                return emotion
    
    # Default tag if no keywords match
    return "neutral"

# Example usage:
text_input = "I am so happy and excited to see you!"
emotional_tag = tag_emotional_resonance(text_input)
print(f"Emotional Tag: {emotional_tag}")
```