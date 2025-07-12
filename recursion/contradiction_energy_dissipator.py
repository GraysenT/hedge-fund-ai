def resolve_contradictions(modules):
    """
    Attempts to harmonize modules with conflicting beliefs or outputs.
    """
    resolved = []
    for m in modules:
        if "conflict" in m and m["conflict"]:
            m["status"] = "muted"
            m["notes"] = "Muted due to conflict until retrained."
        resolved.append(m)
    return resolved