import asyncio
async def stream_prices():
    while True:
        yield {'symbol': 'BTC', 'price': 34200.22}
        await asyncio.sleep(0.1)