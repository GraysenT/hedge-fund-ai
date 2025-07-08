class SignalDirectionConsistency:
    def __init__(self):
        self.direction_memory = {}

    def check(self, symbol, new_action):
        last_action = self.direction_memory.get(symbol)
        if last_action and last_action != new_action:
            print(f"[CONSISTENCY] Direction change on {symbol}: {last_action} → {new_action}")
        self.direction_memory[symbol] = new_action