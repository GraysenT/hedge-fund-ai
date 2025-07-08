from abc import ABC, abstractmethod

class BaseAPI(ABC):
    @abstractmethod
    def fetch(self, symbol, start, end):
        """Return a DataFrame with historical price or news data."""
        pass