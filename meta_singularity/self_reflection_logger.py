Here is a Python code snippet that simulates a system logging its reflective moments when it learns from itself. This example uses a simple machine learning model that updates its knowledge based on new data, and logs important steps in the learning process.

```python
import logging
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SelfLearningSystem:
    def __init__(self):
        self.data = load_iris()
        self.model = RandomForestClassifier()
        logging.info("System initialized and model created.")

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        logging.info("Model training completed.")

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        logging.info(f"Model evaluation completed with accuracy: {accuracy}")
        return accuracy

    def update_and_reflect(self, X_update, y_update):
        initial_accuracy = self.evaluate(X_update, y_update)
        self.model.fit(X_update, y_update)
        updated_accuracy = self.evaluate(X_update, y_update)
        if updated_accuracy > initial_accuracy:
            logging.info("Model improved after self-reflection and learning.")
        else:
            logging.info("Model did not improve after self-reflection.")

    def run(self):
        X_train, X_test, y_train, y_test = train_test_split(self.data.data, self.data.target, test_size=0.3, random_state=42)
        self.train(X_train, y_train)
        self.evaluate(X_test, y_test)
        self.update_and_reflect(X_test, y_test)

if __name__ == "__main__":
    system = SelfLearningSystem()
    system.run()
```

This code does the following:
1. Initializes a logging system to record the process.
2. Loads the Iris dataset and splits it into training and testing sets.
3. Trains a RandomForestClassifier on the training data.
4. Evaluates the model on the test data and logs the accuracy.
5. Simulates a self-learning process where the model is retrained on the test data and evaluates if there has been an improvement in accuracy, logging the outcome.

This example can be extended or modified to fit more complex scenarios or different types of machine learning models and self-reflection mechanisms.