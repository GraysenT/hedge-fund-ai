def detect_anomaly(state, previous_state, tolerance=0.0001):
    """
    Detects when a state variable is looping or freezing.
    """
    for key in state:
        if key in previous_state:
            delta = abs(state[key] - previous_state[key])
            if delta < tolerance:
                return True  # stagnation or loop detected
    return False