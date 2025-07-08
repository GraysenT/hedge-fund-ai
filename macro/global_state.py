import requests
import os

FINNHUB_KEY = os.getenv("FINNHUB_API_KEY")

def get_macro_data():
    vix = requests.get(f"https://finnhub.io/api/v1/quote?symbol=VIX&token={FINNHUB_KEY}").json()
    fed = requests.get(f"https://finnhub.io/api/v1/economic?symbol=FEDFUNDS&token={FINNHUB_KEY}").json()
    cpi = requests.get(f"https://finnhub.io/api/v1/economic?symbol=CPI&token={FINNHUB_KEY}").json()

    print("🌍 Global Market State:")
    print(f"VIX: {vix.get('c')}")
    print(f"Fed Funds Rate: {fed[-1].get('value') if fed else 'N/A'}")
    print(f"CPI: {cpi[-1].get('value') if cpi else 'N/A'}")

    return {
        "vix": vix.get("c"),
        "fed_funds": fed[-1].get("value") if fed else None,
        "cpi": cpi[-1].get("value") if cpi else None
    }

if __name__ == "__main__":
    get_macro_data()

