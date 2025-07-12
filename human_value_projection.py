Below is a Python script that estimates how a human might view the fairness, intent, or beauty of a strategy based on input descriptions. The script uses a simple rule-based approach to evaluate the strategy based on keywords and phrases typically associated with fairness, positive intent, and beauty.

```python
import re

def evaluate_fairness(description):
    fairness_keywords = ["equal", "equitable", "balanced", "impartial", "just"]
    unfair_keywords = ["biased", "unjust", "inequitable", "partial", "discriminatory"]
    
    fairness_score = sum(1 for word in fairness_keywords if word in description.lower())
    unfair_score = sum(1 for word in unfair_keywords if word in description.lower())
    
    if fairness_score > unfair_score:
        return "Fair"
    elif fairness_score < unfair_score:
        return "Unfair"
    else:
        return "Neutral"

def evaluate_intent(description):
    positive_intent_keywords = ["helpful", "beneficial", "supportive", "constructive", "kind"]
    negative_intent_keywords = ["harmful", "destructive", "malicious", "negative", "cruel"]
    
    positive_score = sum(1 for word in positive_intent_keywords if word in description.lower())
    negative_score = sum(1 for word in negative_intent_keywords if word in description.lower())
    
    if positive_score > negative_score:
        return "Positive Intent"
    elif positive_score < negative_score:
        return "Negative Intent"
    else:
        return "Neutral Intent"

def evaluate_beauty(description):
    beauty_keywords = ["beautiful", "elegant", "graceful", "aesthetic", "pleasing"]
    not_beauty_keywords = ["ugly", "clumsy", "awkward", "unpleasant", "unattractive"]
    
    beauty_score = sum(1 for word in beauty_keywords if word in description.lower())
    not_beauty_score = sum(1 for word in not_beauty_keywords if word in description.lower())
    
    if beauty_score > not_beauty_score:
        return "Beautiful"
    elif beauty_score < not_beauty_score:
        return "Not Beautiful"
    else:
        return "Neutral Beauty"

def evaluate_strategy(description):
    fairness = evaluate_fairness(description)
    intent = evaluate_intent(description)
    beauty = evaluate_beauty(description)
    
    return {
        "Fairness": fairness,
        "Intent": intent,
        "Beauty": beauty
    }

# Example usage
description = "The strategy aims to provide equitable resources to all participants, ensuring a balanced and supportive environment."
evaluation = evaluate_strategy(description)
print(evaluation)
```

This script defines functions to evaluate fairness, intent, and beauty based on the presence of specific keywords in a given strategy description. It returns a dictionary with the evaluations. Adjust the keyword lists and logic as needed to fit more nuanced or specific criteria.