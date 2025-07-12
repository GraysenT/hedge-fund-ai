Below is a Python code example that demonstrates how to adjust signal weights based on detected market regimes and macro overlays. This example uses a simple regime detection mechanism based on moving averages and adjusts weights based on macroeconomic indicators. The code uses pandas for data handling and numpy for numerical operations.

```python
import pandas as pd
import numpy as np

def detect_market_regime(prices, short_window=40, long_window=100):
    """
    Simple market regime detection based on moving averages.
    Bullish regime: short MA > long MA
    Bearish regime: short MA < long MA
    """
    signals = pd.DataFrame(index=prices.index)
    signals['short_ma'] = prices.rolling(window=short_window, min_periods=1).mean()
    signals['long_ma'] = prices.rolling(window=long_window, min_periods=1).mean()
    signals['regime'] = np.where(signals['short_ma'] > signals['long_ma'], 1, 0)
    return signals['regime']

def adjust_weights_based_on_macro(data, macro_indicator, threshold):
    """
    Adjust weights based on a macroeconomic indicator.
    If the indicator is above a certain threshold, reduce weights as a risk-off strategy.
    """
    weights = np.where(data[macro_indicator] > threshold, 0.5, 1.0)
    return weights

def main():
    # Example data
    np.random.seed(0)
    dates = pd.date_range('2020-01-01', periods=200)
    prices = pd.Series(np.random.randn(200) * 10 + 100, index=dates)
    macro_data = pd.DataFrame({
        'GDP_growth': np.random.randn(200) * 2 + 3,  # Simulated GDP growth
    }, index=dates)

    # Detect market regime
    regime = detect_market_regime(prices)

    # Adjust weights based on GDP growth
    weights = adjust_weights_based_on_macro(macro_data, 'GDP_growth', 4)

    # Combine regime and macro adjustments
    final_weights = weights * np.where(regime == 1, 1.0, 0.5)

    # Print results
    combined_data = pd.DataFrame({
        'Prices': prices,
        'Regime': regime,
        'Macro Adjusted Weights': weights,
        'Final Weights': final_weights
    })
    print(combined_data.tail(10))

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Market Regime Detection**: The function `detect_market_regime` calculates short-term and long-term moving averages of the prices. A bullish regime is identified when the short-term moving average is above the long-term moving average, and vice versa for a bearish regime.

2. **Macro Adjustment**: The function `adjust_weights_based_on_macro` adjusts the investment weights based on a macroeconomic indicator (e.g., GDP growth). If the indicator exceeds a specified threshold, it suggests a risk-off approach by reducing the weights.

3. **Combining Adjustments**: In the `main` function, the weights adjusted for macroeconomic conditions are further modified based on the market regime. During a bearish regime, weights are halved as an additional risk management strategy.

4. **Output**: The script prints the last 10 entries of the combined data including prices, detected regime, macro-adjusted weights, and final weights after considering both market regime and macroeconomic conditions.

This code provides a basic framework and can be expanded or modified to include more sophisticated financial models, additional economic indicators, and different strategies for weight adjustment.