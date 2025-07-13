import asyncio
import websockets
import json

class WSRouter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    async def broadcast(self, data):
        for callback in self.subscribers:
            await callback(data)

    async def listen_binance(self):
        uri = "wss://stream.binance.com:9443/ws/btcusdt@trade"
        async with websockets.connect(uri) as websocket:
            while True:
                message = await websocket.recv()
                msg = json.loads(message)
                price = float(msg["p"])
                await self.broadcast({"symbol": "BTCUSDT", "price": price, "source": "binance"})

    async def run(self):
        await asyncio.gather(self.listen_binance())