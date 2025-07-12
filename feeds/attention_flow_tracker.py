Below is a Python script that uses Google Trends data to track where market attention is moving based on search interest over time. The script utilizes the `pytrends` library, which is an unofficial API for Google Trends. The script will fetch and display the interest over time for a list of keywords, which can be interpreted as indicators of where market attention is shifting.

First, you need to install the `pytrends` package if it's not already installed:

```bash
pip install pytrends
```

Here is the Python code:

```python
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

def fetch_trends(keywords, timeframe='today 5-y', geo='US'):
    # Connect to Google Trends
    pytrends = TrendReq(hl='en-US', tz=360)

    # Build payload
    pytrends.build_payload(kw_list=keywords, timeframe=timeframe, geo=geo)

    # Get interest over time
    data = pytrends.interest_over_time()
    
    # Remove the 'isPartial' column
    if 'isPartial' in data.columns:
        data = data.drop(columns='isPartial')
    
    return data

def plot_trends(data, keywords):
    # Plotting
    plt.figure(figsize=(14, 7))
    for keyword in keywords:
        plt.plot(data.index, data[keyword], label=keyword)
    
    plt.title('Google Search Trends')
    plt.xlabel('Year')
    plt.ylabel('Interest Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

# Keywords to track
keywords = ['electric cars', 'solar energy', 'remote work']

# Fetch trends data
trends_data = fetch_trends(keywords)

# Plot trends data
plot_trends(trends_data, keywords)
```

### Explanation:
1. **Installation**: The script starts by ensuring the `pytrends` library is installed.
2. **Function `fetch_trends`**: This function connects to Google Trends, builds the payload with the specified keywords, timeframe, and geographical focus, and fetches the data.
3. **Function `plot_trends`**: This function takes the fetched data and plots it using `matplotlib` to visualize the trends over time.
4. **Keywords**: You can modify the `keywords` list to include any terms you are interested in tracking.
5. **Timeframe and Geography**: The default timeframe is set to the past 5 years (`'today 5-y'`), and the geographical focus is set to the United States (`'US'`). These can be adjusted as needed.

This script provides a basic framework for tracking market attention shifts using search data. You can expand it by adding more detailed analysis, comparing different regions, or adjusting the timeframe for more granular insights.