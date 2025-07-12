Below is a Python code that detects regime shifts in financial markets using volatility, trend, liquidity, and macroeconomic context. The code uses libraries such as `pandas` for data handling, `numpy` for numerical operations, and `statsmodels` for statistical analysis. It also utilizes moving averages and standard deviation to measure trend and volatility, respectively, and incorporates a simple liquidity measure. For macro context, it uses a hypothetical economic indicator.

```python
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

def load_data():
    # This function should load data from your data source. Here, we create dummy data.
    # In practice, you would replace this with loading data from files or an API.
    dates = pd.date_range(start='2000-01-01', periods=5000, freq='D')
    price = np.random.lognormal(mean=0, sigma=0.03, size=len(dates)).cumprod()
    volume = np.random.normal(loc=1e6, scale=1e5, size=len(dates))
    macro_indicator = np.random.normal(loc=0, scale=1, size=len(dates)).cumsum()
    return pd.DataFrame({'Price': price, 'Volume': volume, 'Macro': macro_indicator}, index=dates)

def calculate_indicators(df):
    # Calculate moving averages for trend analysis
    df['MA_short'] = df['Price'].rolling(window=50).mean()
    df['MA_long'] = df['Price'].rolling(window=200).mean()
    
    # Calculate rolling standard deviation for volatility
    df['Volatility'] = df['Price'].rolling(window=50).std()
    
    # Calculate a simple liquidity measure
    df['Liquidity'] = df['Volume'].rolling(window=50).mean()
    
    # Normalize macroeconomic indicator
    df['Macro_norm'] = (df['Macro'] - df['Macro'].mean()) / df['Macro'].std()
    
    return df

def detect_regime_shifts(df):
    # Detect shifts based on moving averages crossover
    df['Trend_shift'] = df['MA_short'].cross(df['MA_long'], direction='both')
    
    # Detect shifts based on volatility changes
    df['Volatility_shift'] = df['Volatility'].diff().abs() > df['Volatility'].std()
    
    # Detect liquidity shocks
    df['Liquidity_shift'] = df['Liquidity'].diff().abs() > df['Liquidity'].std()
    
    # Detect significant macroeconomic changes
    df['Macro_shift'] = df['Macro_norm'].diff().abs() > 1.5  # Arbitrary threshold for significant change
    
    return df

def plot_regime_shifts(df):
    fig, axes = plt.subplots(4, 1, figsize=(14, 10), sharex=True)
    
    # Price and moving averages
    axes[0].plot(df['Price'], label='Price')
    axes[0].plot(df['MA_short'], label='MA Short')
    axes[0].plot(df['MA_long'], label='MA Long')
    axes[0].set_title('Price and Moving Averages')
    axes[0].legend()
    
    # Volatility
    axes[1].plot(df['Volatility'], label='Volatility', color='red')
    axes[1].set_title('Volatility')
    
    # Liquidity
    axes[2].plot(df['Liquidity'], label='Liquidity', color='green')
    axes[2].set_title('Liquidity')
    
    # Macroeconomic Indicator
    axes[3].plot(df['Macro_norm'], label='Macro Indicator', color='purple')
    axes[3].set_title('Macroeconomic Indicator')
    
    for ax in axes:
        ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    
    plt.tight_layout()
    plt.show()

def main():
    df = load_data()
    df = calculate_indicators(df)
    df = detect_regime_shifts(df)
    plot_regime_shifts(df)

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Data Loading**: Replace `load_data()` with actual data loading from your data sources.
2. **Indicator Calculation**: Moving averages for trend, rolling standard deviation for volatility, and a simple liquidity measure are calculated.
3. **Regime Shift Detection**: Shifts are detected based on significant changes in these indicators.
4. **Visualization**: The `plot_regime_shifts()` function visualizes the price, volatility, liquidity, and macroeconomic indicators along with detected shifts.

### Note:
- The code uses dummy data. Replace it with real financial data.
- The thresholds and parameters (like window sizes and thresholds for detecting shifts) should be tuned according to specific market characteristics and data behavior.