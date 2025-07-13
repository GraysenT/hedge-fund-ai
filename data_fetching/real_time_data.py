import websocket
import json

class RealTimeData:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.ws_url = "wss://stream.data.alpaca.markets/v2/iex"

    def get_live_data(self, symbols):
        """Fetch live market data for multiple symbols."""
        ws = websocket.WebSocketApp(self.ws_url, on_message=self.on_message)
        ws.run_forever()

    def on_message(self, ws, message):
        data = json.loads(message)
        print(f"Real-time data received: {data}")