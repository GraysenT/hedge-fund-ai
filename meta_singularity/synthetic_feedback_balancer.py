```python
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the simulation
num_episodes = 1000
learning_rate = 0.1
discount_factor = 0.99
epsilon = 0.1

# Define the environment
class Environment:
    def __init__(self):
        self.state_space = [0, 1, 2, 3, 4]  # Example states
        self.action_space = [0, 1]  # Example actions: 0=left, 1=right
        self.current_state = 2

    def reset(self):
        self.current_state = 2
        return self.current_state

    def step(self, action):
        if action == 0:
            next_state = max(0, self.current_state - 1)
        else:
            next_state = min(4, self.current_state + 1)

        reward = 1 if next_state == 4 else -1 if next_state == 0 else 0
        done = next_state == 0 or next_state == 4
        self.current_state = next_state
        return next_state, reward, done

# Initialize Q-table
def initialize_q_table(state_space, action_space):
    return np.zeros((len(state_space), len(action_space)))

# Choose an action using epsilon-greedy policy
def choose_action(state, q_table):
    if np.random.random() < epsilon:
        return np.random.choice(env.action_space)
    else:
        return np.argmax(q_table[state])

# Update Q-table
def update_q_table(q_table, state, action, reward, next_state):
    best_next_action = np.argmax(q_table[next_state])
    td_target = reward + discount_factor * q_table[next_state][best_next_action]
    td_error = td_target - q_table[state][action]
    q_table[state][action] += learning_rate * td_error

# Main training loop
env = Environment()
q_table = initialize_q_table(env.state_space, env.action_space)

for episode in range(num_episodes):
    state = env.reset()
    done = False

    while not done:
        action = choose_action(state, q_table)
        next_state, reward, done = env.step(action)
        update_q_table(q_table, state, action, reward, next_state)
        state = next_state

# Plotting the results
plt.figure(figsize=(10, 5))
plt.imshow(q_table, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Q-table')
plt.xlabel('Actions')
plt.ylabel('States')
plt.xticks(np.arange(len(env.action_space)), env.action_space)
plt.yticks(np.arange(len(env.state_space)), env.state_space)
plt.show()
```