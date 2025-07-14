import importlib
import pkgutil
from typing import Type, List
from core.strategy_base import StrategyBase

class StrategyRegistry:
    def __init__(self, package: str):
        self.package = package
        self.registry: List[Type[StrategyBase]] = []

    def discover_strategies(self):
        package = importlib.import_module(self.package)
        for _, modname, ispkg in pkgutil.iter_modules(package.__path__):
            if not ispkg:
                module = importlib.import_module(f"{self.package}.{modname}")
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if isinstance(obj, type) and issubclass(obj, StrategyBase) and obj is not StrategyBase:
                        self.registry.append(obj)

    def get_all(self) -> List[Type[StrategyBase]]:
        return self.registry
