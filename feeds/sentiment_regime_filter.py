Below is a Python script that filters trading strategies or signals based on the current market sentiment. The script uses the `vaderSentiment` library to analyze sentiment from recent news headlines fetched via the `newsapi`. Depending on the sentiment score, it filters and applies trading strategies or signals accordingly.

First, you need to install the required packages if you haven't already:
```bash
pip install newsapi-python vaderSentiment
```

Here is the Python code:

```python
from newsapi import NewsApiClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime

# Initialize NewsAPI and Sentiment Analyzer
newsapi = NewsApiClient(api_key='YOUR_NEWSAPI_KEY')
analyzer = SentimentIntensityAnalyzer()

def fetch_news_sentiment(query, from_date, to_date):
    # Fetch news articles
    all_articles = newsapi.get_everything(q=query,
                                          from_param=from_date,
                                          to=to_date,
                                          language='en',
                                          sort_by='relevancy',
                                          page_size=100)
    
    total_score = 0
    # Analyze sentiment of fetched articles
    for article in all_articles['articles']:
        text = article['title'] + '. ' + article['description']
        sentiment = analyzer.polarity_scores(text)
        total_score += sentiment['compound']
    
    # Average sentiment score
    average_sentiment = total_score / len(all_articles['articles'])
    return average_sentiment

def filter_strategies(sentiment_score):
    # Define your strategies or signals
    strategies = {
        'bullish': ['Buy', 'Long'],
        'bearish': ['Sell', 'Short'],
        'neutral': ['Hold', 'Do nothing']
    }
    
    # Filter strategies based on sentiment
    if sentiment_score > 0.05:
        return strategies['bullish']
    elif sentiment_score < -0.05:
        return strategies['bearish']
    else:
        return strategies['neutral']

# Main function to execute the script
def main():
    # Define the market or keyword and date range
    market_keyword = 'stock market'
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    last_week = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    
    # Get sentiment score
    sentiment_score = fetch_news_sentiment(market_keyword, last_week, today)
    print(f"Sentiment Score: {sentiment_score}")
    
    # Get filtered strategies
    strategies = filter_strategies(sentiment_score)
    print(f"Recommended Strategies: {strategies}")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **API Keys**: You need to replace `'YOUR_NEWSAPI_KEY'` with your actual NewsAPI key.
2. **Sentiment Analysis**: The script uses VADER sentiment analysis to compute the sentiment score from news headlines and descriptions.
3. **Strategy Filtering**: Based on the sentiment score, it categorizes the market sentiment as bullish, bearish, or neutral and suggests strategies accordingly.
4. **Date Range**: The script currently analyzes news from the past week. You can adjust this range as needed.

This script provides a basic framework and can be expanded with more sophisticated analysis and integration with trading systems.