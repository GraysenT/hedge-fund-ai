def simulate_future_belief(state, goal):
    """Think from the future. Not: what do I do? But: what must have happened for this to be true?"""
    return f"If {goal}, then {state} must be caused recursively."