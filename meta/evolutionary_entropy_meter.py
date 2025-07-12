```python
import random
import time

class LogicCircuit:
    def __init__(self):
        self.temperature = 25  # Initial temperature in Celsius
        self.threshold = 50    # Temperature threshold in Celsius for cooling

    def increase_temperature(self):
        # Simulate temperature increase due to logic propagation
        self.temperature += random.randint(1, 5)

    def check_temperature(self):
        # Check if the temperature exceeds the threshold
        if self.temperature >= self.threshold:
            self.trigger_cooling()

    def trigger_cooling(self):
        # Simulate cooling mechanism
        print(f"Temperature {self.temperature}°C exceeds threshold. Cooling triggered.")
        self.temperature -= 10
        print(f"Temperature after cooling: {self.temperature}°C")

    def run(self):
        # Simulate the operation of the logic circuit
        for _ in range(10):
            self.increase_temperature()
            print(f"Current temperature: {self.temperature}°C")
            self.check_temperature()
            time.sleep(1)  # Simulate time delay for each logic operation

# Create and run the logic circuit
circuit = LogicCircuit()
circuit.run()
```