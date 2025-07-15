import importlib

def dynamic_strategy_loader(name):
    try:
        module = importlib.import_module(f"strategies.{name}")
        class_name = name.replace("_", "").capitalize()
        return getattr(module, class_name)
    except Exception as e:
        print(f"⚠️ Could not load strategy '{name}': {e}")
        return None

class AIAgent:
    def __init__(self, name, strategy_name=None, memory_enabled=True, goal=None):
        self.name = name
        self.strategy_name = strategy_name
        self.memory_enabled = memory_enabled
        self.goal = goal or "Improve hedge fund AI"
        self.memory_log = []
        self.code_evolution_log = []
        self.strategy = self.load_strategy(strategy_name) if strategy_name else None

    def load_strategy(self, strategy_name):
        strategy_class = dynamic_strategy_loader(strategy_name)
        if strategy_class:
            return strategy_class()
        return None

    def think(self, market_data):
        if self.strategy:
            signal = self.strategy.generate_signal(market_data)
            if self.memory_enabled:
                self.memory_log.append({"input": market_data, "signal": signal})
            return signal
        return "no-strategy"

    def evolve(self):
        upgrade = f"# Patch by {self.name} to evolve {self.strategy_name}"
        self.code_evolution_log.append(upgrade)
        return upgrade