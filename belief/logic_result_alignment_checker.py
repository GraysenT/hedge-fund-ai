def verify_signal_coherence(signal, outcome):
    """
    Checks if signal logic, belief, and outcome formed a coherent arc.
    """
    logic = signal.get("logic", "")
    belief = signal.get("belief", "")
    if belief in logic and signal.get("outcome") == "matched":
        return True
    return False