import os
import importlib.util
from core.strategy_base import StrategyBase

def load_plugins(path="plugins") -> list[StrategyBase]:
    strategies = []
    for filename in os.listdir(path):
        if filename.endswith(".py"):
            spec = importlib.util.spec_from_file_location("plugin", os.path.join(path, filename))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            for obj in vars(mod).values():
                if isinstance(obj, type) and issubclass(obj, StrategyBase) and obj is not StrategyBase:
                    strategies.append(obj(name=obj.__name__, parameters={"base": 1}))
    return strategies