import importlib
import pkgutil
from core.strategy_base import StrategyBase

def load_strategies(package: str = "strategies"):
    strategies = []
    imported = importlib.import_module(package)
    for _, name, _ in pkgutil.iter_modules(imported.__path__):
        module = importlib.import_module(f"{package}.{name}")
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(obj, type) and issubclass(obj, StrategyBase) and obj is not StrategyBase:
                strategies.append(obj(name=obj.__name__, parameters={"base": 1}))
    return strategies