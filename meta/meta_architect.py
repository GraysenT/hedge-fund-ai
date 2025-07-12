```python
class EvolutionPhase:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def execute_tasks(self):
        print(f"Executing tasks for {self.name}")
        for task in self.tasks:
            task.execute()

class Task:
    def __init__(self, description, function):
        self.description = description
        self.function = function

    def execute(self):
        print(f"Task: {self.description}")
        self.function()

def task1():
    print("Analyzing data...")

def task2():
    print("Designing model...")

def task3():
    print("Training model...")

def task4():
    print("Evaluating model...")

def task5():
    print("Deploying model...")

class EvolutionOverseer:
    def __init__(self):
        self.phases = []

    def add_phase(self, phase):
        self.phases.append(phase)

    def oversee_evolution(self):
        for phase in self.phases:
            phase.execute_tasks()

# Example usage
def main():
    # Create tasks
    analysis_task = Task("Data Analysis", task1)
    design_task = Task("Model Design", task2)
    training_task = Task("Model Training", task3)
    evaluation_task = Task("Model Evaluation", task4)
    deployment_task = Task("Model Deployment", task5)

    # Create phases
    phase1 = EvolutionPhase("Analysis Phase")
    phase1.add_task(analysis_task)

    phase2 = EvolutionPhase("Design Phase")
    phase2.add_task(design_task)

    phase3 = EvolutionPhase("Training Phase")
    phase3.add_task(training_task)

    phase4 = EvolutionPhase("Evaluation Phase")
    phase4.add_task(evaluation_task)

    phase5 = EvolutionPhase("Deployment Phase")
    phase5.add_task(deployment_task)

    # Create overseer and add phases
    overseer = EvolutionOverseer()
    overseer.add_phase(phase1)
    overseer.add_phase(phase2)
    overseer.add_phase(phase3)
    overseer.add_phase(phase4)
    overseer.add_phase(phase5)

    # Start the evolution process
    overseer.oversee_evolution()

if __name__ == "__main__":
    main()
```