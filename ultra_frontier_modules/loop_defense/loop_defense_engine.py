from .recursion_guard import RecursionTracker
from .anomaly_detector import detect_anomaly

class LoopDefenseEngine:
    def __init__(self):
        self.guard = RecursionTracker()
        self.prev_states = {}

    def check_safe_to_proceed(self, module_name, new_state):
        if not self.guard.track(module_name):
            return (False, "Recursion limit reached")

        prev_state = self.prev_states.get(module_name)
        self.prev_states[module_name] = new_state

        if prev_state and detect_anomaly(new_state, prev_state):
            return (False, "Anomalous static loop detected")

        return (True, "Clear")