Here's a Python script that logs major decisions and the reasons behind them into a file. This script uses Python's built-in logging module to handle the logging.

```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='decision_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_decision(decision, reason):
    """
    Logs a decision and the reason for making that decision.
    
    Args:
    decision (str): Description of the decision.
    reason (str): Explanation why the decision was made.
    """
    logging.info(f"Decision: {decision}, Reason: {reason}")

def main():
    # Example decisions
    log_decision("Choose Python for project", "Python's simplicity and library support makes it ideal for rapid development.")
    log_decision("Increase budget for marketing", "Market analysis shows potential for higher returns with increased ad spend.")
    log_decision("Hire two new developers", "Project deadlines are approaching and additional manpower is necessary.")

if __name__ == "__main__":
    main()
```

This script will create and write to a file named `decision_log.log`, logging each decision with a timestamp. You can modify the `log_decision` function and the `main` function to suit your specific needs, such as integrating this logging mechanism into a larger application or system.