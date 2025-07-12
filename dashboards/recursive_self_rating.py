```python
import random

class SystemRating:
    def __init__(self):
        self.alignment = random.randint(1, 10)
        self.performance = random.randint(1, 10)
        self.coherence = random.randint(1, 10)

    def rate_system(self):
        return {
            'Alignment': self.alignment,
            'Performance': self.performance,
            'Coherence': self.coherence
        }

# Create an instance of SystemRating
system_rating = SystemRating()

# Get the system ratings
ratings = system_rating.rate_system()

# Print the ratings
print("System Ratings:")
for key, value in ratings.items():
    print(f"{key}: {value}")
```