import requests
import os

API_KEY = os.getenv("FINNHUB_API_KEY")

def get_macro_news():
    url = f"https://finnhub.io/api/v1/news?category=general&token={API_KEY}"
    news = requests.get(url).json()
    relevant = [n for n in news if any(x in n["headline"] for x in ["Fed", "SEC", "regulation", "inflation"])]
    for item in relevant[:5]:
        print(f"📰 {item['headline']}")
        print(f"📝 {item['summary'][:200]}...\n")

if __name__ == "__main__":
    get_macro_news()
    