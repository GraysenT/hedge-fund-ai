class PurposeFeedbackGrid:
    def __init__(self):
        self.feedback = []

    def add_feedback(self, feedback_message):
        """Monitor capital-purpose harmony."""
        self.feedback.append(feedback_message)
        print(f"Feedback added: {feedback_message}")
    
    def get_feedback(self):
        return self.feedback