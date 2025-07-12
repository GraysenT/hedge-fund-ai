Below is a Python script that simulates a system with potential feedback loops, detects unmonitored feedback loops, and maps their effects on the system's stability and performance. This example uses a simple model where components of a system can influence each other either positively or negatively, and the script checks for the presence of feedback loops that are not regulated or monitored.

```python
import numpy as np

class SystemSimulator:
    def __init__(self, num_components):
        self.num_components = num_components
        # Randomly generate influence matrix (could be user-defined)
        self.influence_matrix = np.random.randint(-1, 2, (num_components, num_components))
        np.fill_diagonal(self.influence_matrix, 0)  # No component influences itself

    def detect_feedback_loops(self):
        # Use the power of the matrix to find cycles
        path_matrix = np.eye(self.num_components)
        feedback_loops = []

        for _ in range(self.num_components):
            path_matrix = np.dot(path_matrix, self.influence_matrix)
            # Check for cycles of any length up to num_components
            for i in range(self.num_components):
                if path_matrix[i][i] != 0:
                    feedback_loops.append((i, path_matrix[i][i]))

        return feedback_loops

    def analyze_loops(self, feedback_loops):
        loop_effects = {}
        for loop in feedback_loops:
            component, effect = loop
            if effect > 0:
                loop_effects[component] = 'Positive Feedback'
            elif effect < 0:
                loop_effects[component] = 'Negative Feedback'
            else:
                loop_effects[component] = 'Neutral'

        return loop_effects

    def print_system_info(self):
        print("System Influence Matrix:")
        print(self.influence_matrix)

    def simulate(self):
        feedback_loops = self.detect_feedback_loops()
        effects = self.analyze_loops(feedback_loops)
        self.print_system_info()
        print("\nFeedback Loops and Their Effects:")
        for component, effect in effects.items():
            print(f"Component {component}: {effect}")

# Example usage:
num_components = 5  # Define the number of components in the system
simulator = SystemSimulator(num_components)
simulator.simulate()
```

### Explanation:
1. **SystemSimulator Class**: This class simulates a system with a specified number of components. Each component can influence others, and this influence is represented as a matrix.
2. **Influence Matrix**: A square matrix where each element `(i, j)` represents the influence of component `i` on component `j`. Values are randomly set between -1 and 1, where -1 indicates a negative influence, 1 indicates a positive influence, and 0 means no influence.
3. **Detecting Feedback Loops**: The script uses matrix multiplication to detect cycles in the influence matrix. A cycle (or feedback loop) is detected if the diagonal of the matrix raised to successive powers contains non-zero elements.
4. **Analyzing Effects**: The script categorizes each detected feedback loop as positive, negative, or neutral based on the sign of the sum of influences in the loop.
5. **Simulation**: The `simulate` method orchestrates the detection of feedback loops, analyzes their effects, and prints the system information and results.

This script can be adapted to more complex systems, and the influence matrix can be defined based on specific system characteristics for more accurate simulations.