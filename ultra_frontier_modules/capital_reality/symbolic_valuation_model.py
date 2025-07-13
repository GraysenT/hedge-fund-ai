def evaluate_symbolic_value(asset):
    """
    Estimate the symbolic value of an asset.
    Inputs can include: cultural_significance, narrative_attachment, historical_rituals
    """
    cultural = asset.get("cultural_significance", 0.5)
    narrative = asset.get("narrative_attachment", 0.5)
    ritual = asset.get("historical_rituals", 0.3)

    symbolic_value = 0.4 * cultural + 0.4 * narrative + 0.2 * ritual
    return round(symbolic_value, 3)