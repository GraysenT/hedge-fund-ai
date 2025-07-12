def simulate_belief_attraction(logic_map):
    """
    Detects which belief structures pull other strategies into similar behavior patterns.
    """
    gravity_fields = {}
    for logic in logic_map:
        attractor = logic.get("core_belief", "undefined")
        if attractor not in gravity_fields:
            gravity_fields[attractor] = 1
        else:
            gravity_fields[attractor] += 1
    return gravity_fields