```python
import logging
from datetime import datetime

# Setting up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EvolutionLogic:
    def __init__(self):
        self.scores = []
        self.feedback = []

    def log_score(self, score):
        """Logs the score and appends it to the scores list."""
        self.scores.append(score)
        logging.info(f"Score logged: {score}")

    def log_feedback(self, feedback):
        """Logs the feedback and appends it to the feedback list."""
        self.feedback.append(feedback)
        logging.info(f"Feedback logged: {feedback}")

    def evolve_logic(self):
        """Evolves the logic based on scores and feedback."""
        if not self.scores or not self.feedback:
            logging.warning("Insufficient data to evolve logic.")
            return

        average_score = sum(self.scores) / len(self.scores)
        logging.info(f"Average Score: {average_score}")

        # Example evolution logic based on feedback
        positive_feedback = [f for f in self.feedback if 'good' in f.lower()]
        negative_feedback = [f for f in self.feedback if 'bad' in f.lower()]

        logging.info(f"Positive Feedback Count: {len(positive_feedback)}")
        logging.info(f"Negative Feedback Count: {len(negative_feedback)}")

        # Implementing changes based on feedback
        if len(positive_feedback) > len(negative_feedback):
            logging.info("Overall positive feedback. Maintaining current strategies.")
        else:
            logging.info("Overall negative feedback. Consider revising strategies.")

        # Resetting scores and feedback for the next evolution cycle
        self.scores = []
        self.feedback = []
        logging.info("Scores and feedback reset for the next evolution cycle.")

# Example usage
evolution_logic = EvolutionLogic()
evolution_logic.log_score(85)
evolution_logic.log_score(90)
evolution_logic.log_feedback("Good job on the recent update.")
evolution_logic.log_feedback("The performance could be better.")
evolution_logic.evolve_logic()
```