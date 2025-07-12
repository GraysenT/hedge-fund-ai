def resolve_doubt_signal(strategy_metrics):
    """
    If performance confidence drops or purpose coherence weakens,
    this initiates self-reflection and temporary signal restraint.
    """
    confidence = strategy_metrics.get("confidence", 0.5)
    coherence = strategy_metrics.get("belief_score", 0.5)

    if confidence < 0.4 and coherence < 0.5:
        return {"doubt_flag": True, "action": "self-review"}
    return {"doubt_flag": False, "action": "continue"}