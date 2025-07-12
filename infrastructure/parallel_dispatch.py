Below is a Python example that demonstrates how to parallelize tasks using thread-safe dispatching with the `concurrent.futures` module, which provides a high-level interface for asynchronously executing callables using threads or processes. The example simulates a scenario where multiple "agents" execute different "strategies" concurrently. Each strategy is a function that could represent some computation or task.

```python
import concurrent.futures
import time
import random

def strategy_one(agent_id):
    time.sleep(random.uniform(0.1, 0.5))  # Simulate processing time
    return f"Agent {agent_id} executed Strategy One"

def strategy_two(agent_id):
    time.sleep(random.uniform(0.1, 0.5))  # Simulate processing time
    return f"Agent {agent_id} executed Strategy Two"

def strategy_three(agent_id):
    time.sleep(random.uniform(0.1, 0.5))  # Simulate processing time
    return f"Agent {agent_id} executed Strategy Three"

def execute_strategy(agent_id, strategy):
    result = strategy(agent_id)
    print(result)
    return result

def main():
    agents = 5  # Number of agents
    strategies = [strategy_one, strategy_two, strategy_three]  # List of strategies

    # Using ThreadPoolExecutor to handle tasks concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=agents) as executor:
        # Dispatch tasks
        futures = []
        for agent_id in range(1, agents + 1):
            chosen_strategy = random.choice(strategies)
            future = executor.submit(execute_strategy, agent_id, chosen_strategy)
            futures.append(future)

        # Wait for all futures to complete
        for future in concurrent.futures.as_completed(futures):
            try:
                data = future.result()
            except Exception as exc:
                print(f'Generated an exception: {exc}')
            else:
                print(f'Thread result: {data}')

if __name__ == "__main__":
    main()
```

### Explanation:

1. **Strategy Functions**: `strategy_one`, `strategy_two`, and `strategy_three` are dummy functions representing different tasks that agents might execute. They include a simulated delay to mimic processing time.

2. **execute_strategy Function**: This function takes an agent ID and a strategy function, executes the strategy, and prints the result.

3. **main Function**:
   - Initializes a number of agents and a list of strategy functions.
   - Uses a `ThreadPoolExecutor` to manage a pool of threads. The number of threads is set to the number of agents to allow each agent to potentially run a task concurrently.
   - Tasks are dispatched to the executor, which assigns them to available threads.
   - The `executor.submit` method schedules the `execute_strategy` function to be executed with an agent ID and a randomly chosen strategy.
   - The script waits for all tasks to complete, handling results as they become available.

This example ensures that tasks are dispatched and managed in a thread-safe manner, suitable for scenarios where multiple tasks need to be executed concurrently and independently.