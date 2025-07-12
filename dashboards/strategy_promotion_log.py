It seems you are asking for a Python script that logs all promotions of a project or feature from the idea stage to production, including the rationale for each promotion. This can be implemented using a simple logging system that records each stage of the project's lifecycle.

Below is an example Python script that uses a combination of classes and logging to manage and record the lifecycle of a project:

```python
import logging
from datetime import datetime

# Set up basic configuration for logging
logging.basicConfig(filename='project_lifecycle.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Project:
    def __init__(self, name):
        self.name = name
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)
        logging.info(f"Project '{self.name}' promoted to {stage.name} with rationale: {stage.rationale}")

class Stage:
    def __init__(self, name, rationale):
        self.name = name
        self.rationale = rationale

def main():
    # Create a new project
    project = Project("Example Project")

    # Define different stages of the project
    idea = Stage("Idea", "Initial concept for market need")
    prototype = Stage("Prototype", "Proof of concept was successful")
    development = Stage("Development", "Development phase started after successful prototype")
    testing = Stage("Testing", "Testing for bugs and performance issues")
    production = Stage("Production", "Successfully passed all tests and ready for deployment")

    # Promote project through various stages
    project.add_stage(idea)
    project.add_stage(prototype)
    project.add_stage(development)
    project.add_stage(testing)
    project.add_stage(production)

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Logging Setup**: The script uses Python's built-in `logging` library to log information. The log file is named `project_lifecycle.log`.

2. **Project Class**: This class represents a project and contains a list of stages. Each time a stage is added, it logs the promotion along with the rationale.

3. **Stage Class**: Represents a stage in the project lifecycle, with a name and a rationale for why the project is moving to this stage.

4. **main Function**: This function creates a project, defines its stages, and promotes the project through these stages, logging each promotion.

### Usage:
- Run the script to simulate the project lifecycle.
- Check the `project_lifecycle.log` file to see the log of all promotions and their rationales.

This script can be expanded or modified to include more detailed project management features, such as handling multiple projects, more detailed stage information, or integration with project management tools.