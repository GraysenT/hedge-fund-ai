import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FINNHUB_API_KEY")

def get_quote(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"
    res = requests.get(url)
    return res.json()

def get_news(symbol):
    url = f"https://finnhub.io/api/v1/news?category=general&token={API_KEY}"
    return requests.get(url).json()
