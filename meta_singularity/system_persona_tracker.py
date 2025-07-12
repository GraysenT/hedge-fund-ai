```python
import random
import time

class Personality:
    def __init__(self):
        self.traits = {
            "curiosity": 5,
            "friendliness": 5,
            "assertiveness": 5,
            "patience": 5,
            "confidence": 5
        }
    
    def evolve(self):
        # Randomly increase or decrease each trait
        for trait in self.traits:
            change = random.randint(-1, 1)
            self.traits[trait] = max(0, min(10, self.traits[trait] + change))
    
    def display_traits(self):
        for trait, value in self.traits.items():
            print(f"{trait.capitalize()}: {value}")

class SystemIdentity:
    def __init__(self):
        self.personality = Personality()
        self.start_time = time.time()
    
    def update_identity(self):
        # Evolve personality over time
        current_time = time.time()
        if current_time - self.start_time > 10:  # Evolve every 10 seconds
            self.personality.evolve()
            self.start_time = current_time
    
    def show_identity(self):
        print("Current System Identity:")
        self.personality.display_traits()

def main():
    system_identity = SystemIdentity()
    
    try:
        while True:
            system_identity.update_identity()
            system_identity.show_identity()
            time.sleep(10)  # Update every 10 seconds
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main()
```