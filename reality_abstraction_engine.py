```python
import random

class Environment:
    def __init__(self, temperature, humidity, light_level):
        self.temperature = temperature  # in degrees Celsius
        self.humidity = humidity        # in percentage
        self.light_level = light_level  # in lumens

    def __str__(self):
        return f"Environment(Temperature: {self.temperature}°C, Humidity: {self.humidity}%, Light Level: {self.light_level} lumens)"

class SymbolicEnvironment:
    def __init__(self, temperature_symbol, humidity_symbol, light_level_symbol):
        self.temperature_symbol = temperature_symbol
        self.humidity_symbol = humidity_symbol
        self.light_level_symbol = light_level_symbol

    def __str__(self):
        return f"SymbolicEnvironment(Temperature: {self.temperature_symbol}, Humidity: {self.humidity_symbol}, Light Level: {self.light_level_symbol})"

def real_to_symbolic(environment):
    # Temperature symbols: Cold, Moderate, Hot
    if environment.temperature <= 10:
        temp_symbol = 'Cold'
    elif environment.temperature <= 25:
        temp_symbol = 'Moderate'
    else:
        temp_symbol = 'Hot'

    # Humidity symbols: Dry, Normal, Humid
    if environment.humidity <= 30:
        humidity_symbol = 'Dry'
    elif environment.humidity <= 70:
        humidity_symbol = 'Normal'
    else:
        humidity_symbol = 'Humid'

    # Light level symbols: Dark, Normal, Bright
    if environment.light_level <= 200:
        light_level_symbol = 'Dark'
    elif environment.light_level <= 500:
        light_level_symbol = 'Normal'
    else:
        light_level_symbol = 'Bright'

    return SymbolicEnvironment(temp_symbol, humidity_symbol, light_level_symbol)

# Example usage
if __name__ == "__main__":
    # Create a real-world environment
    real_env = Environment(temperature=random.randint(-5, 40),
                           humidity=random.randint(10, 90),
                           light_level=random.randint(50, 1000))
    print(real_env)

    # Convert to symbolic environment
    symbolic_env = real_to_symbolic(real_env)
    print(symbolic_env)
```