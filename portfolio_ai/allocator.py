Below is a Python script that allocates capital across different investment strategies based on their performance, risk, and reinforcement learning to optimize the allocation dynamically. This script uses a simple reinforcement learning model (Q-learning) to learn the best allocation strategy over time.

```python
import numpy as np
import pandas as pd

# Parameters
n_strategies = 5
initial_capital = 1000000
risk_aversion = 0.5
learning_rate = 0.1
discount_factor = 0.95
random_action_probability = 0.1
n_episodes = 1000

# Simulated returns and risks for each strategy
np.random.seed(42)
strategy_returns = np.random.normal(0.01, 0.005, (n_episodes, n_strategies))
strategy_risks = np.random.uniform(0.01, 0.03, n_strategies)

# Initialize Q-table
Q_table = np.zeros((n_strategies, n_strategies))

def choose_action(state, epsilon):
    if np.random.rand() < epsilon:
        return np.random.randint(0, n_strategies)
    else:
        return np.argmax(Q_table[state])

def update_q_table(state, action, reward, next_state):
    best_next_action = np.argmax(Q_table[next_state])
    td_target = reward + discount_factor * Q_table[next_state][best_next_action]
    td_error = td_target - Q_table[state][action]
    Q_table[state][action] += learning_rate * td_error

def calculate_reward(capital, returns, risks):
    adjusted_returns = returns - risk_aversion * risks
    return capital * np.sum(adjusted_returns)

# Simulation loop
for episode in range(n_episodes):
    state = np.random.randint(0, n_strategies)  # Random initial state
    capital = initial_capital
    for t in range(100):  # Assume 100 time steps
        action = choose_action(state, random_action_probability)
        current_returns = strategy_returns[episode]
        current_risks = strategy_risks
        
        # Calculate reward
        reward = calculate_reward(capital, current_returns[action], current_risks[action])
        
        # Update capital
        capital += reward
        
        # Observe the new state
        next_state = action
        
        # Update Q-table
        update_q_table(state, action, reward, next_state)
        
        state = next_state

# Output the learned Q-values and the optimal policy
print("Q-table:")
print(Q_table)
print("Optimal policy (best actions per state):")
print(np.argmax(Q_table, axis=1))
```

### Explanation:
1. **Initialization**: We define the number of strategies, initial capital, risk aversion, learning parameters, and simulate returns and risks for simplicity.
2. **Q-learning Setup**: A Q-table is initialized to store the value of taking each action from each state.
3. **Choosing an Action**: Actions are chosen either randomly (exploration) or by selecting the best-known action (exploitation) based on the Q-table.
4. **Reward Calculation**: The reward is calculated as the capital gain adjusted for risk aversion.
5. **Q-table Update**: The Q-table is updated using the temporal difference learning method, incorporating the reward received and the discounted value of the next state.
6. **Simulation Loop**: The model simulates several episodes, updating the Q-table based on the observed rewards and transitions.

This script provides a foundational approach to capital allocation using reinforcement learning, which can be expanded and refined with more sophisticated financial models and RL algorithms.