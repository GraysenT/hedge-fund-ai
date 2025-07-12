class RecursiveFeedbackLoop:
    def __init__(self):
        self.feedbacks = []

    def integrate_feedback(self, feedback_message):
        """Integrates recursive feedback into capital strategy."""
        self.feedbacks.append(feedback_message)
        print(f"Integrated feedback: {feedback_message}")
    
    def get_feedbacks(self):
        return self.feedbacks