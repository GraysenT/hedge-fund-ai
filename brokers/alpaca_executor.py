import os
import requests

class AlpacaExecutor:
    def __init__(self, api_key=None, api_secret=None, base_url=None):
        self.api_key = api_key or os.getenv("ALPACA_API_KEY")
        self.api_secret = api_secret or os.getenv("ALPACA_SECRET_KEY")
        self.base_url = base_url or "https://paper-api.alpaca.markets"
        self.headers = {
            "APCA-API-KEY-ID": self.api_key,
            "APCA-API-SECRET-KEY": self.api_secret
        }

    def place_order(self, symbol, qty, side, order_type="market", time_in_force="gtc"):
        url = f"{self.base_url}/v2/orders"
        order = {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "type": order_type,
            "time_in_force": time_in_force
        }
        response = requests.post(url, json=order, headers=self.headers)
        if response.status_code == 200 or response.status_code == 201:
            return {"status": "success", "data": response.json()}
        else:
            return {"status": "error", "error": response.json()}
