Below is a Python script that uses the `yfinance` library to fetch ETF data and the `pandas` library to analyze cross-asset flows to infer positioning bias. The script will focus on a few major ETFs across different asset classes (equities, bonds, commodities) and calculate the net inflows or outflows over a recent period, which can be indicative of market sentiment or positioning bias.

```python
import yfinance as yf
import pandas as pd

def fetch_data(tickers, start_date, end_date):
    """
    Fetch historical market data from Yahoo Finance.
    """
    data = yf.download(tickers, start=start_date, end=end_date)
    return data['Adj Close']

def calculate_flows(data):
    """
    Calculate net flows based on the adjusted close prices.
    """
    daily_returns = data.pct_change()
    flows = daily_returns.mean() * 100
    return flows

def main():
    # Define ETFs across different asset classes
    tickers = {
        'SPY': 'Equities',  # S&P 500 ETF
        'TLT': 'Long-term Bonds',  # 20+ Year Treasury Bond ETF
        'GLD': 'Commodities'  # Gold ETF
    }
    
    # Define the period for analysis
    start_date = '2023-01-01'
    end_date = '2023-12-01'
    
    # Fetch data
    data = fetch_data(list(tickers.keys()), start_date, end_date)
    
    # Calculate net flows
    flows = calculate_flows(data)
    
    # Display results
    for ticker, flow in flows.iteritems():
        print(f"{ticker} ({tickers[ticker]}): {'Inflow' if flow > 0 else 'Outflow'} of {abs(flow):.2f}%")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Data Fetching**: The script uses `yfinance` to download historical data for selected ETFs representing different asset classes.
2. **Flow Calculation**: It calculates the mean percentage change in the adjusted close prices, which is used as a proxy for net flows. Positive mean change suggests inflows, while negative mean change suggests outflows.
3. **Output**: The script prints whether each ETF experienced an inflow or outflow and the magnitude of that flow in percentage terms.

### Note:
- Ensure you have the necessary libraries installed (`yfinance` and `pandas`) by running `pip install yfinance pandas`.
- The script assumes that a positive average return indicates net inflows (buying pressure) and a negative return indicates net outflows (selling pressure). Adjustments might be needed based on more sophisticated flow calculation methods or additional data sources.