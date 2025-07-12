To parse options market data for institutional bets, sweep activity, and sentiment reversal, you'll need access to options data, which can be obtained from financial data providers like Bloomberg, Yahoo Finance, or through APIs like Alpha Vantage, Tradier, or Interactive Brokers. Below is a Python script that demonstrates how to fetch and analyze options data to identify potential institutional activities and sentiment reversals. This script uses the `yfinance` library to fetch data and `pandas` for data manipulation.

First, ensure you have the necessary libraries installed:
```bash
pip install yfinance pandas
```

Here's the Python code:

```python
import yfinance as yf
import pandas as pd

def fetch_options_data(ticker):
    """
    Fetch options data for a given ticker.
    """
    stock = yf.Ticker(ticker)
    options_dates = stock.options
    options_data = pd.DataFrame()

    for date in options_dates:
        opt = stock.option_chain(date)
        calls = opt.calls
        puts = opt.puts
        calls['expiry'] = date
        puts['expiry'] = date
        calls['type'] = 'call'
        puts['type'] = 'put'
        options_data = pd.concat([options_data, calls, puts])
    
    return options_data

def filter_sweep_activity(options_data):
    """
    Filter options data to find potential sweep activities.
    """
    # Assuming 'sweep' can be identified by large volume trades
    threshold = options_data['volume'].quantile(0.95)  # top 5% volume
    sweep_activity = options_data[options_data['volume'] >= threshold]
    return sweep_activity

def detect_sentiment_reversal(options_data):
    """
    Detect sentiment reversal based on changes in open interest and volume.
    """
    # Criteria for sentiment reversal might include a significant increase in open interest
    # combined with unusual trading volume
    interest_threshold = options_data['openInterest'].quantile(0.90)  # top 10% open interest
    volume_threshold = options_data['volume'].quantile(0.90)  # top 10% volume
    sentiment_reversal = options_data[(options_data['openInterest'] >= interest_threshold) &
                                      (options_data['volume'] >= volume_threshold)]
    return sentiment_reversal

def main():
    ticker = 'AAPL'  # Example ticker
    options_data = fetch_options_data(ticker)
    sweep_activity = filter_sweep_activity(options_data)
    sentiment_reversal = detect_sentiment_reversal(options_data)

    print("Sweep Activity:")
    print(sweep_activity[['strike', 'lastPrice', 'volume', 'openInterest', 'expiry', 'type']])
    
    print("\nSentiment Reversal:")
    print(sentiment_reversal[['strike', 'lastPrice', 'volume', 'openInterest', 'expiry', 'type']])

if __name__ == "__main__":
    main()
```

### Explanation:
1. **fetch_options_data**: This function fetches options data for all available expiry dates for a given ticker using `yfinance`.
2. **filter_sweep_activity**: Identifies potential sweep activities by filtering options with unusually high volume (top 5%).
3. **detect_sentiment_reversal**: Looks for options where there is a significant increase in both open interest and volume, which might indicate a sentiment reversal.
4. **main**: The main function orchestrates the fetching, filtering, and detection processes, and prints the results.

### Note:
- The thresholds and criteria for identifying "sweep activity" and "sentiment reversal" are set arbitrarily in this example. You may need to adjust these based on specific trading strategies or deeper market analysis.
- Real-time trading decisions should consider more comprehensive data and possibly more sophisticated algorithms or machine learning models.