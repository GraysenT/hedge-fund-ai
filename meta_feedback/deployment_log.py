Below is a Python script that logs deployment details including who deployed a particular item and which agent authorized it. The script uses Python's built-in logging module to handle the logging. It assumes you have a function or method to perform the deployment and another for authorization. Adjust the details as necessary for your specific use case.

```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='deployments.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def authorize_deployment(agent_name):
    """
    Simulate an authorization check by an agent.
    """
    # This is a placeholder for actual authorization logic
    return True

def deploy_item(deployer, item, agent):
    """
    Simulate the deployment of an item.
    """
    if authorize_deployment(agent):
        logging.info(f"Item '{item}' was deployed by {deployer} and authorized by {agent}")
        return True
    else:
        logging.error(f"Failed deployment attempt by {deployer} due to unauthorized agent {agent}")
        return False

# Example usage
deployer_name = "John Doe"
item_to_deploy = "Software Update v2.3"
authorizing_agent = "Agent Smith"

# Perform deployment
deploy_item(deployer_name, item_to_deploy, authorizing_agent)
```

This script includes:
- A logging configuration that writes to a file named `deployments.log`.
- A function `authorize_deployment` that should include real authorization logic.
- A function `deploy_item` that logs successful and unsuccessful deployment attempts.

You can run this script in your Python environment. It will log all deployment activities, which you can then review in the `deployments.log` file. Adjust the paths, logging levels, and formats as needed for your environment and standards.