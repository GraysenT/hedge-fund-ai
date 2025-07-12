def analyze_belief_conflict(strategies):
    """
    Finds friction between coexisting strategies that hold contradictory truths.
    """
    conflicts = []
    for s1 in strategies:
        for s2 in strategies:
            if s1["id"] != s2["id"] and s1.get("belief") != s2.get("belief"):
                if s1.get("signal") == s2.get("signal") and s1.get("signal") is not None:
                    conflicts.append((s1["id"], s2["id"]))
    return conflicts