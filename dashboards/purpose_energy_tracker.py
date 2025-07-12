Below is a Python script that estimates how much logic (in terms of computational resources like time or memory) is being spent to pursue each goal or value in a given set of tasks. The script uses a simple model where each task has an associated cost and a set of values or goals it contributes to. The script calculates the total cost spent on each goal based on the tasks that contribute to that goal.

```python
import time

# Define tasks with their costs and the goals they contribute to
tasks = {
    'task1': {'cost': 10, 'goals': ['education', 'health']},
    'task2': {'cost': 20, 'goals': ['health', 'environment']},
    'task3': {'cost': 15, 'goals': ['education']},
    'task4': {'cost': 5,  'goals': ['environment']},
    'task5': {'cost': 25, 'goals': ['economy', 'education']}
}

# Function to simulate task execution (for demonstration)
def execute_task(task_name, cost):
    print(f"Executing {task_name} with cost {cost}")
    time.sleep(cost / 100)  # Simulate time taken by task

# Calculate total cost per goal
goal_costs = {}

for task, details in tasks.items():
    cost = details['cost']
    goals = details['goals']
    execute_task(task, cost)  # Simulate task execution
    for goal in goals:
        if goal in goal_costs:
            goal_costs[goal] += cost
        else:
            goal_costs[goal] = cost

# Display the total logic (cost) spent on each goal
print("\nTotal logic spent on each goal:")
for goal, total_cost in goal_costs.items():
    print(f"{goal}: {total_cost}")
```

This script defines a set of tasks, each with a specific cost and associated goals. It simulates the execution of each task (using a sleep function to mimic time consumption) and aggregates the costs for each goal. Finally, it prints out how much "logic" (in this context, computational resources like time) is spent on each goal. Adjust the `tasks` dictionary and the `execute_task` function as needed to fit the actual computation or resource usage scenario.