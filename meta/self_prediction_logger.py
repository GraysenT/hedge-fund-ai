Below is a Python script that simulates a system making predictions about itself and logs both the predictions and their accuracy. The script uses Python's built-in `logging` module to handle logging.

```python
import logging
import random

# Configure logging
logging.basicConfig(filename='system_predictions.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def system_predict():
    """Simulate a system prediction about its performance."""
    # Randomly predict system performance (e.g., CPU usage percentage)
    return random.randint(50, 100)

def actual_performance():
    """Simulate the actual system performance."""
    # Actual performance might slightly differ from the prediction
    return random.randint(45, 105)

def evaluate_prediction(prediction, actual):
    """Evaluate the accuracy of the prediction."""
    error = abs(prediction - actual)
    accuracy = max(0, 100 - (error / actual * 100))
    return accuracy

def main():
    # System makes a prediction about its own performance
    predicted_performance = system_predict()
    # Get the actual performance
    actual_performance_value = actual_performance()
    # Evaluate how accurate the prediction was
    accuracy = evaluate_prediction(predicted_performance, actual_performance_value)
    
    # Log the prediction, actual performance, and accuracy
    logging.info(f"Predicted Performance: {predicted_performance}%")
    logging.info(f"Actual Performance: {actual_performance_value}%")
    logging.info(f"Prediction Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Logging Configuration**: The logging is set up to write to a file named `system_predictions.log`. It logs the date and time of each entry, the severity level, and the message.

2. **Prediction and Performance Functions**: The `system_predict` function simulates a prediction of system performance (like CPU usage), and `actual_performance` provides a simulated actual performance value.

3. **Accuracy Evaluation**: The `evaluate_prediction` function calculates the accuracy of the prediction based on the absolute error relative to the actual value.

4. **Main Function**: This function orchestrates making a prediction, fetching the actual performance, evaluating the accuracy, and logging all these details.

This script can be run periodically or triggered by specific events depending on the requirements of the system monitoring setup.