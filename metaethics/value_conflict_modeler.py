def detect_value_conflicts(strategies):
    """
    Flags strategies whose logic or outcomes contradict the system's declared capital values.
    """
    conflicts = []
    for strat in strategies:
        if "exploit_weakness" in strat.get("tags", []) and "preserve_resilience" in strat.get("values", []):
            conflicts.append(strat["name"])
    return conflicts