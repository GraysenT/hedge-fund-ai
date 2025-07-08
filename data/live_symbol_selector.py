import requests
import os

FINNHUB_KEY = os.getenv("FINNHUB_API_KEY")

def get_trending_symbols(limit=10):
    url = f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_KEY}"
    res = requests.get(url).json()
    symbols = []
    for item in res:
        if "related" in item and item["related"]:
            symbols += item["related"].split(",")
    ranked = sorted(set(symbols))
    return ranked[:limit]

if __name__ == "__main__":
    trending = get_trending_symbols()
    print("🔥 Trending symbols from news:")
    print(trending)
