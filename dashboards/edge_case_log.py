```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='outlier_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_outlier_decision(value, threshold, decision_type):
    """
    Logs information about outlier decisions or rare conditions.
    
    :param value: The value being checked
    :param threshold: The threshold used for determining outliers
    :param decision_type: Type of decision or condition e.g., 'HIGH', 'LOW', 'EDGE_CASE'
    """
    logging.info(f"Outlier decision logged: Value: {value}, Threshold: {threshold}, Decision Type: {decision_type}")

def check_temperature(temperature):
    """
    Example function to check if a temperature reading is an outlier.
    
    :param temperature: The temperature reading to check
    """
    # Define temperature thresholds
    low_threshold = -10
    high_threshold = 50
    
    if temperature < low_threshold:
        log_outlier_decision(temperature, low_threshold, 'LOW')
    elif temperature > high_threshold:
        log_outlier_decision(temperature, high_threshold, 'HIGH')
    else:
        logging.info(f"Temperature within normal range: {temperature}")

# Example usage
check_temperature(-15)
check_temperature(55)
check_temperature(20)
```