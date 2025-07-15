import requests

def get_fear_greed_index():
    try:
        r = requests.get("https://api.alternative.me/fng/")
        return int(r.json()["data"][0]["value"])
    except:
        return 50  # neutral fallback

def get_fed_rate():
    # Placeholder – replace with real macro feed
    return 5.25