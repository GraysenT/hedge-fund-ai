Here's a Python script that simulates how well agents retain learning over time and across recursion. The script uses a simple reinforcement learning model where agents learn to navigate a grid to reach a goal. The learning retention is modeled by a decay in the learned values over time and recursive calls. This example uses a basic Q-learning algorithm.

```python
import numpy as np

class GridWorld:
    def __init__(self, size=5, goal_position=(4, 4)):
        self.size = size
        self.goal_position = goal_position
        self.grid = np.zeros((size, size))
        self.grid[goal_position] = 1  # Mark the goal position

    def is_goal(self, position):
        return position == self.goal_position

class Agent:
    def __init__(self, learning_rate=0.1, discount_factor=0.9, decay_rate=0.99):
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.decay_rate = decay_rate

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0)

    def set_q_value(self, state, action, value):
        self.q_table[(state, action)] = value

    def choose_action(self, state, actions):
        if np.random.rand() < 0.1:  # Exploration chance
            return np.random.choice(actions)
        q_values = [self.get_q_value(state, action) for action in actions]
        max_q = max(q_values)
        # In case there are several actions with the same q-value
        return np.random.choice([actions[i] for i in range(len(actions)) if q_values[i] == max_q])

    def update_q_table(self, old_state, action, reward, new_state, possible_actions):
        old_q = self.get_q_value(old_state, action)
        future_q = max([self.get_q_value(new_state, a) for a in possible_actions])
        new_q = old_q + self.learning_rate * (reward + self.discount_factor * future_q - old_q)
        self.set_q_value(old_state, action, new_q)

    def decay_learning(self):
        for key in self.q_table:
            self.q_table[key] *= self.decay_rate

def simulate_learning(grid, agent, episodes, max_steps_per_episode):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for episode in range(episodes):
        state = (0, 0)  # Start at top-left corner
        for step in range(max_steps_per_episode):
            actions = [(state[0] + move[0], state[1] + move[1]) for move in moves
                       if 0 <= state[0] + move[0] < grid.size and 0 <= state[1] + move[1] < grid.size]
            action = agent.choose_action(state, actions)
            new_state = action
            reward = 1 if grid.is_goal(new_state) else 0
            agent.update_q_table(state, action, reward, new_state, actions)
            state = new_state
            if grid.is_goal(state):
                break
        agent.decay_learning()  # Decay learning after each episode

    return agent.q_table

# Parameters
grid_size = 5
goal_position = (4, 4)
learning_rate = 0.1
discount_factor = 0.9
decay_rate = 0.99
episodes = 100
max_steps_per_episode = 50

# Simulation
grid = GridWorld(grid_size, goal_position)
agent = Agent(learning_rate, discount_factor, decay_rate)
q_table = simulate_learning(grid, agent, episodes, max_steps_per_episode)

# Output the learned Q-values
print("Learned Q-values:")
for key, value in q_table.items():
    print(f"State {key[0]} Action {key[1]}: Q-value = {value:.2f}")
```

This script initializes a grid and an agent, then simulates the agent's learning process over a specified number of episodes. The agent's Q-values decay after each episode to simulate forgetting or retention loss. The final Q-values are printed out, showing what the agent has learned.