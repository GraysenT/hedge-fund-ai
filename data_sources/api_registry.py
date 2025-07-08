from data_sources.base_adapter import BaseAPI
import importlib
import pkgutil

class APIRegistry:
    def __init__(self):
        self.registry = {}

    def discover(self, package="data_sources"):
        for _, modname, ispkg in pkgutil.iter_modules([package]):
            if not ispkg:
                module = importlib.import_module(f"{package}.{modname}")
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if isinstance(obj, type) and issubclass(obj, BaseAPI) and obj is not BaseAPI:
                        instance = obj()
                        self.registry[modname] = instance

    def get_api(self, name):
        return self.registry.get(name)