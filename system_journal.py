Here's a Python script that acts as a reflective system journal for logging build cycles. It captures details about what was built, what failed, what changed internally, and suggestions for future improvements. The script uses Python's built-in logging module to handle the logging of events.

```python
import logging
from datetime import datetime
import json

# Configure logging
logging.basicConfig(filename='system_journal.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BuildJournal:
    def __init__(self):
        self.build_history = []

    def log_build(self, build_id, build_status, changes, failures, recommendations):
        """
        Logs details of a build cycle.
        
        :param build_id: Unique identifier for the build
        :param build_status: Status of the build (e.g., 'success', 'failure')
        :param changes: List of changes made in this build
        :param failures: List of failures encountered during the build
        :param recommendations: Suggestions for future builds
        """
        build_info = {
            'build_id': build_id,
            'build_status': build_status,
            'changes': changes,
            'failures': failures,
            'recommendations': recommendations,
            'timestamp': datetime.now().isoformat()
        }
        self.build_history.append(build_info)
        self._log_to_file(build_info)

    def _log_to_file(self, build_info):
        """
        Logs the build information to a file using the logging module.
        """
        logging.info(json.dumps(build_info, indent=4))

def main():
    journal = BuildJournal()
    
    # Example build details
    build_id = "build_001"
    build_status = "success"
    changes = [
        "Added new logging feature",
        "Updated database schema",
        "Refactored authentication module"
    ]
    failures = [
        "Memory leak in module X",
        "Timeout during data migration"
    ]
    recommendations = [
        "Increase unit test coverage for module X",
        "Review timeout settings for heavy operations"
    ]

    # Log the build
    journal.log_build(build_id, build_status, changes, failures, recommendations)

if __name__ == "__main__":
    main()
```

### Explanation:
- **Logging Configuration**: The script configures the Python logging module to write logs to a file named `system_journal.log`. It logs the date, time, log level, and message.
- **BuildJournal Class**: This class manages the build logs. It stores each build's details in a list and logs them to a file.
- **log_build Method**: This method accepts details about the build, such as build ID, status, changes, failures, and recommendations. It logs these details using the `_log_to_file` method.
- **_log_to_file Method**: This private method logs the build information in JSON format for better readability and structured logging.
- **main Function**: This function creates an instance of `BuildJournal` and logs an example build cycle.

This script can be expanded or modified to include more detailed logging, error handling, or integration with other systems like databases or web services for more complex build cycle tracking.