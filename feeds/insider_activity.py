Below is a Python script that tracks insider buying or selling for a given list of stocks using the `yfinance` library to fetch historical data and the `pandas` library to handle data manipulation. The script will then update strategy-level overlays based on the detected insider transactions. This example assumes a simple strategy where increased insider buying might suggest a bullish overlay, while increased selling might suggest a bearish overlay.

```python
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Define a list of stock tickers
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']

# Define a date range (e.g., last 30 days)
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

# Placeholder for actual insider trading data
# This should be replaced with actual data source for insider transactions
insider_trades = {
    'AAPL': {'buys': 100, 'sells': 50},
    'MSFT': {'buys': 50, 'sells': 100},
    'GOOGL': {'buys': 30, 'sells': 10},
    'AMZN': {'buys': 20, 'sells': 60},
    'FB': {'buys': 10, 'sells': 20}
}

# Function to fetch historical stock data
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Strategy overlay based on insider transactions
def update_strategy_overlay(insider_data):
    overlays = {}
    for stock, transactions in insider_data.items():
        if transactions['buys'] > transactions['sells']:
            overlays[stock] = 'Bullish Overlay'
        else:
            overlays[stock] = 'Bearish Overlay'
    return overlays

# Fetch stock data (optional, if needed for further analysis)
stock_data = {}
for stock in stocks:
    stock_data[stock] = fetch_stock_data(stock, start_date, end_date)

# Update strategy overlays based on insider transactions
strategy_overlays = update_strategy_overlay(insider_trades)

# Output the strategy overlays
print("Strategy Overlays based on Insider Transactions:")
for stock, overlay in strategy_overlays.items():
    print(f"{stock}: {overlay}")
```

### Notes:
1. **Insider Trading Data**: The script uses a placeholder for insider trading data (`insider_trades`). In practice, you would need access to a real-time database or API that provides accurate and up-to-date information on insider transactions for the stocks of interest.

2. **Strategy Logic**: The strategy overlay logic in this script is quite simplistic. In a real-world scenario, the strategy would likely be more complex, incorporating additional factors such as the volume of transactions, the roles of the insiders involved, historical data, and other market conditions.

3. **Data Fetching**: The script uses `yfinance` to fetch historical stock data, which can be used for further analysis or to refine the strategy based on market performance.

4. **Real-Time Application**: For real-time applications, you would need to set up this script to run at regular intervals (e.g., daily) and possibly integrate with a notification or trading execution system.