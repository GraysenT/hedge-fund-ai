```python
import time

class SignalController:
    def __init__(self, interval, duration):
        """
        Initializes the SignalController.
        
        :param interval: Time in seconds between signal activations.
        :param duration: Time in seconds the signal remains active.
        """
        self.interval = interval
        self.duration = duration
        self.next_activation_time = time.time() + self.interval
        self.active = False

    def update(self):
        """
        Updates the state of the signal based on the current time.
        """
        current_time = time.time()
        if self.active:
            if current_time >= self.next_activation_time:
                self.active = False
                self.next_activation_time = current_time + self.interval
                print("Signal deactivated.")
        else:
            if current_time >= self.next_activation_time:
                self.active = True
                self.next_activation_time = current_time + self.duration
                print("Signal activated.")

    def is_active(self):
        """
        Returns the current state of the signal (active or not).
        
        :return: True if the signal is active, False otherwise.
        """
        return self.active

# Example usage:
if __name__ == "__main__":
    signal = SignalController(interval=10, duration=5)
    
    while True:
        signal.update()
        print("Signal is active:", signal.is_active())
        time.sleep(1)
```

This Python code defines a `SignalController` class that manages the activation and deactivation of a signal based on specified intervals and durations. The `update` method checks the current time and toggles the signal's state accordingly. The example usage in the main block demonstrates how this class can be used to control a signal in a continuous loop, printing the signal's state every second. Adjust the `interval` and `duration` parameters as needed for different timing requirements.