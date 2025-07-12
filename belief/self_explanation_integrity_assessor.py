def assess_explainability(signal):
    """
    Confirms that strategy explanations still match updated signal behavior.
    """
    try:
        explanation = signal.get("explanation", "")
        logic_terms = signal.get("logic", "")
        matched_terms = sum(1 for word in explanation.split() if word in logic_terms)
        ratio = matched_terms / len(explanation.split()) if explanation else 0.0
        return ratio > 0.5  # threshold for valid explainability
    except:
        return False