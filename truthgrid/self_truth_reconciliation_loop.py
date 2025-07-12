def reconcile_truths(system_beliefs):
    """
    Re-aligns the system's belief models if contradictions or unreconciled drift is detected.
    """
    if "volatility_is_noise" in system_beliefs and "volatility_contains_signal" in system_beliefs:
        system_beliefs.remove("volatility_is_noise")
        system_beliefs.append("volatility_is_conditionally_informative")
    return system_beliefs