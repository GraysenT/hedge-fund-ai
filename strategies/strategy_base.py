from abc import ABC, abstractmethod

class StrategyBase(ABC):
    def __init__(self, name):
        self.name = name
        self.weight = 1.0  # Initial weight for the strategy

    @abstractmethod
    def generate_signal(self, market_data):
        """Generate a trade signal based on the market data."""
        pass

    @abstractmethod
    def calculate_performance(self, entry_price, exit_price, position_size):
        """Calculate the performance (e.g., PnL) of the trade."""
        pass

    def increase_weight(self):
        """Increase the weight of this strategy."""
        self.weight *= 1.1  # Increase weight by 10% for example
        print(f"Increased weight of {self.name} to {self.weight}")

    def mutate_parameters(self):
        """Mutate the strategy parameters for better performance."""
        # Example: Randomly adjust strategy parameters (e.g., increase the moving average period)
        self.moving_average_period = random.randint(15, 40)  # Example of mutation
        print(f"Mutated {self.name} parameters: moving_average_period set to {self.moving_average_period}")