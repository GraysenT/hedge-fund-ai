class AdaptiveFeedbackLoop:
    def __init__(self):
        self.feedbacks = []

    def add_feedback(self, feedback_message):
        """Add feedback based on autonomous decision-making."""
        self.feedbacks.append(feedback_message)
        print(f"Added feedback: {feedback_message}")
    
    def get_feedbacks(self):
        return self.feedbacks