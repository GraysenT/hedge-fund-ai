import requests
import os

NEWS_API_KEY = os.getenv("NEWSAPI_KEY")

def fetch_news_sentiment(query="market"):
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&apiKey={NEWS_API_KEY}"
    try:
        res = requests.get(url)
        headlines = res.json().get("articles", [])
        return [
            {
                "source": h["source"]["name"],
                "title": h["title"],
                "url": h["url"],
                "published": h["publishedAt"]
            }
            for h in headlines
        ]
    except Exception as e:
        print(f"[NewsAPI] Error: {e}")
        return []