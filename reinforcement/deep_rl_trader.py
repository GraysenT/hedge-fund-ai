class DeepRLTrader:
    def __init__(self):
        self.policy = {}

    def choose_action(self, state):
        return self.policy.get(state, 'hold')

    def learn(self, state, action, reward, next_state):
        self.policy[state] = action