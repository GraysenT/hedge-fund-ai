Below is a Python script that calculates a live rolling correlation matrix across different assets, strategies, or signals using pandas and numpy. This script simulates real-time data updates by generating random data and updating the correlation matrix at each step. It uses a rolling window to compute the correlation matrix for the most recent data points.

```python
import numpy as np
import pandas as pd
from time import sleep

def generate_random_data(n_assets, length):
    """ Generate random data to simulate asset returns. """
    return np.random.randn(length, n_assets)

def update_data(df, new_data):
    """ Update the DataFrame with new data and drop the oldest data to maintain the window size. """
    df = df.append(pd.DataFrame(new_data, columns=df.columns), ignore_index=True)
    df = df.drop(index=0)  # Drop the oldest row to maintain the window size
    return df

def calculate_correlation_matrix(df):
    """ Calculate the correlation matrix of the DataFrame. """
    return df.corr()

def main():
    n_assets = 5  # Number of assets, strategies, or signals
    window_size = 60  # Rolling window size
    update_frequency = 1  # Update frequency in seconds

    # Initial random data
    data = generate_random_data(n_assets, window_size)
    asset_names = [f"Asset_{i+1}" for i in range(n_assets)]
    df = pd.DataFrame(data, columns=asset_names)

    # Start the live update simulation
    try:
        while True:
            # Generate new random data for the update
            new_data = generate_random_data(n_assets, 1)
            df = update_data(df, new_data)

            # Calculate the rolling correlation matrix
            corr_matrix = calculate_correlation_matrix(df)
            print("Updated Correlation Matrix:")
            print(corr_matrix)
            print("-" * 50)

            sleep(update_frequency)  # Wait for the next update
    except KeyboardInterrupt:
        print("Live updates stopped.")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Data Generation**: The `generate_random_data` function simulates the generation of new data for assets. In a real scenario, this could be replaced with actual data fetching from live sources.

2. **Data Update**: The `update_data` function appends new data to the DataFrame and removes the oldest data to maintain a fixed window size for the rolling calculation.

3. **Correlation Calculation**: The `calculate_correlation_matrix` function computes the correlation matrix for the DataFrame, which is updated in each iteration.

4. **Main Loop**: The script continuously updates the DataFrame with new data, recalculates the correlation matrix, and prints it. The loop runs until manually stopped.

This script can be adapted to real data sources and more complex scenarios by modifying the data generation and update mechanisms.