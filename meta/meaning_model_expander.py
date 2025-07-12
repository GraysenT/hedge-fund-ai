def expand_meaning_model_from_experience(memory_logs):
    """
    Learns deeper conceptual significance from recurring strategic behavior.
    """
    meaning_layers = []
    for log in memory_logs[-10:]:
        if "resilient" in log.get("thought", ""):
            meaning_layers.append("resilience_under_stress")
        if "hedge" in log.get("thought", ""):
            meaning_layers.append("protective_capital_frame")
    return list(set(meaning_layers))