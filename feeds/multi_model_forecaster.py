```python
import numpy as np

def blend_forecasts(forecasts, weights=None):
    """
    Blends forecast outputs from ensemble models into a single system signal driver.
    
    Parameters:
        forecasts (list of np.array): List of forecast outputs from different models.
        weights (list of float, optional): List of weights for each forecast. If None, equal weighting is assumed.
        
    Returns:
        np.array: Blended forecast output.
    """
    if weights is None:
        # If no weights provided, use equal weights
        weights = [1 / len(forecasts)] * len(forecasts)
    else:
        # Normalize weights to sum to 1
        total_weight = sum(weights)
        weights = [w / total_weight for w in weights]
    
    # Initialize blended forecast with zeros
    blended_forecast = np.zeros_like(forecasts[0])
    
    # Weighted sum of forecasts
    for forecast, weight in zip(forecasts, weights):
        blended_forecast += forecast * weight
    
    return blended_forecast

# Example usage
if __name__ == "__main__":
    # Example forecasts from three different models
    forecast1 = np.array([0.1, 0.2, 0.3])
    forecast2 = np.array([0.2, 0.1, 0.4])
    forecast3 = np.array([0.15, 0.25, 0.35])

    # Example weights for each model's forecast
    weights = [0.5, 0.3, 0.2]

    # Blend forecasts
    blended_output = blend_forecasts([forecast1, forecast2, forecast3], weights)
    
    print("Blended Forecast Output:", blended_output)
```

This Python code defines a function `blend_forecasts` that takes a list of forecast arrays from different models and optionally a list of weights for each model. It returns a single blended forecast array. If no weights are provided, it assumes equal weighting for each model. The example demonstrates how to use the function with three different forecast outputs and a set of weights.