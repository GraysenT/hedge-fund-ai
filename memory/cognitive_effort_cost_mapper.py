def estimate_effort_cost(signal):
    """
    Roughly quantifies cognitive effort based on feature count, logic depth, and explanation length.
    """
    logic_len = len(signal.get("logic", ""))
    explanation_len = len(signal.get("explanation", ""))
    feature_count = len(signal.get("features", []))

    return 0.2 * feature_count + 0.4 * (logic_len / 100) + 0.4 * (explanation_len / 100)
