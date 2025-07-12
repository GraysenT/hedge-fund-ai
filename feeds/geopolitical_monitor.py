Here's a Python script that uses the Event Registry API to monitor global news for specific types of events such as elections, conflicts, treaties, and disruptions. This script will periodically fetch news articles related to these topics and print out relevant details. You'll need an API key from Event Registry to use this script.

```python
import requests
import time

# Constants
API_KEY = 'YOUR_EVENT_REGISTRY_API_KEY'
EVENT_REGISTRY_ENDPOINT = 'http://eventregistry.org/api/v1/article/getArticles'
SLEEP_TIME = 3600  # Time between queries in seconds (1 hour)

# Query parameters
query_params = {
    'apiKey': API_KEY,
    'action': 'getArticles',
    'keyword': 'election OR conflict OR treaty OR disruption',
    'lang': 'eng',
    'isDuplicateFilter': 'skipDuplicates',
    'dataType': 'news',
    'resultType': 'articles',
    'articlesSortBy': 'date',
    'articlesCount': 10,
    'articlesArticleBodyLen': 300  # Length of the article body preview
}

def fetch_news():
    try:
        response = requests.get(EVENT_REGISTRY_ENDPOINT, params=query_params)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', {}).get('results', [])
        print("Fetched news articles:")
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}")
            print(f"Source: {article['source']['title']}")
            print(f"Date: {article['dateTime']}")
            print(f"Body: {article['body'][:300]}...")  # Print first 300 characters
            print("-" * 80)
    except requests.RequestException as e:
        print(f"Failed to fetch news: {e}")

def main():
    while True:
        fetch_news()
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
```

### How to Use This Script
1. Replace `'YOUR_EVENT_REGISTRY_API_KEY'` with your actual Event Registry API key.
2. You can adjust `SLEEP_TIME` to change how frequently the script checks for updates.
3. Run the script. It will continuously monitor for news articles related to elections, conflicts, treaties, and disruptions, and print out the details.

### Note
- Ensure you handle the API key securely and do not expose it in shared or public environments.
- You might need to adjust the query parameters based on your specific needs or based on the capabilities of the API.
- This script uses a simple polling mechanism. Depending on your use case, you might want to implement more sophisticated error handling or data processing.