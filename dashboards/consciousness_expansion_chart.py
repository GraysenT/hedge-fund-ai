Below is a Python script that uses matplotlib to plot how the "introspective logic volume" grows across recursion. For this example, we'll assume "introspective logic volume" is a hypothetical measure that increases with each recursive call. We'll simulate this by increasing the volume based on a simple mathematical function, such as an exponential growth function, which is typical in recursive processes like the calculation of factorial or Fibonacci numbers.

```python
import matplotlib.pyplot as plt

def recursive_function(n, volume=1, history=None):
    if history is None:
        history = []
    # Assume the volume grows exponentially with the depth of recursion
    new_volume = volume * 1.5  # Increase volume by 50% each call
    history.append(new_volume)
    
    if n > 1:
        return recursive_function(n-1, new_volume, history)
    else:
        return history

# Number of recursive steps
n = 10

# Get the volume history from the recursive function
volume_history = recursive_function(n)

# Plotting the volume history
plt.figure(figsize=(10, 5))
plt.plot(range(1, n+1), volume_history, marker='o')
plt.title('Growth of Introspective Logic Volume Across Recursion')
plt.xlabel('Recursion Depth')
plt.ylabel('Introspective Logic Volume')
plt.grid(True)
plt.show()
```

This script defines a recursive function that simulates the growth of a volume (which we are calling "introspective logic volume") with each recursive call. The growth is recorded, and then plotted using matplotlib, showing how the volume increases with the depth of recursion. Adjust the parameters and the growth function as needed to fit the specific characteristics of your scenario.