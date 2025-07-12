class RecursiveFeedbackLoop:
    def __init__(self):
        self.feedback_loops = []

    def add_feedback_loop(self, feedback_type, loop_factor):
        """Add infinite feedback loops for recursive enhancement."""
        feedback_loop = {"feedback_type": feedback_type, "loop_factor": loop_factor}
        self.feedback_loops.append(feedback_loop)
        print(f"Added feedback loop of type {feedback_type} with factor: {loop_factor}")
    
    def get_feedback_loops(self):
        return self.feedback_loops