Below is a Python example using reinforcement learning, specifically Q-learning, to create an agent that learns from past strategy failures and trains new agents to avoid them. This example uses a simple grid environment where the agent must find the shortest path to a goal while avoiding traps.

```python
import numpy as np
import random

class Environment:
    def __init__(self, size=5, traps=2, goal=(4, 4)):
        self.size = size
        self.goal = goal
        self.traps = self.generate_traps(traps, goal)
        self.state = (0, 0)
    
    def generate_traps(self, num_traps, goal):
        traps = set()
        while len(traps) < num_traps:
            trap = (random.randint(0, self.size-1), random.randint(0, self.size-1))
            if trap != goal:
                traps.add(trap)
        return traps
    
    def reset(self):
        self.state = (0, 0)
        return self.state
    
    def step(self, action):
        x, y = self.state
        if action == 0:   # up
            x = max(0, x - 1)
        elif action == 1: # down
            x = min(self.size - 1, x + 1)
        elif action == 2: # left
            y = max(0, y - 1)
        elif action == 3: # right
            y = min(self.size - 1, y + 1)
        
        self.state = (x, y)
        
        if self.state in self.traps:
            return self.state, -100, True
        elif self.state == self.goal:
            return self.state, 100, True
        else:
            return self.state, -1, False

class QLearningAgent:
    def __init__(self, env, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.env = env
        self.q_table = np.zeros((env.size, env.size, 4))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
    
    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, 3)  # Explore action space
        else:
            return np.argmax(self.q_table[state])  # Exploit learned values
    
    def learn(self, state, action, reward, next_state):
        old_value = self.q_table[state][action]
        future_optimal_value = np.max(self.q_table[next_state])
        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * future_optimal_value)
        self.q_table[state][action] = new_value
    
    def train(self, episodes=1000):
        for _ in range(episodes):
            state = self.env.reset()
            done = False
            
            while not done:
                action = self.choose_action(state)
                next_state, reward, done = self.env.step(action)
                self.learn(state, action, reward, next_state)
                state = next_state

def main():
    env = Environment()
    agent = QLearningAgent(env)
    agent.train(1000)
    
    # Test the trained agent
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state)
        state, reward, done = env.step(action)
        print(f"Move to {state} with reward {reward}")

if __name__ == "__main__":
    main()
```

This code defines a simple grid environment where an agent learns to navigate to a goal while avoiding traps using Q-learning. The agent updates its strategy based on past failures (negative rewards from traps) and successes (reaching the goal). The Q-table is used to store and update the values based on the agent's experiences, guiding future decisions to maximize rewards and minimize failures.