def detect_fundamental_shift(system_manifest):
    """
    Detects when a new purpose or internal transformation reaches escape velocity
    and replaces the prior dominant purpose model.
    """
    if "resilience" in system_manifest and system_manifest.count("expansion") > 2:
        return "phase_shift_detected"
    return "stable"