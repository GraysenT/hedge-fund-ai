def trace_goal_alignment(signal, strategy_manifest):
    """
    Builds a path from signal → logic → belief → declared purpose.
    """
    return {
        "signal": signal.get("id"),
        "logic": signal.get("logic"),
        "belief": strategy_manifest.get("belief"),
        "purpose": strategy_manifest.get("purpose")
    }