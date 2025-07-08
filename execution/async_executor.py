import asyncio
import json
import time

queue = asyncio.Queue()

async def signal_producer():
    while True:
        await asyncio.sleep(1.5)  # simulate signal every ~1.5s
        signal = {"symbol": "TSLA", "action": "buy", "confidence": 0.91}
        await queue.put(signal)
        print(f"📤 Signal queued: {signal}")

async def order_executor():
    while True:
        signal = await queue.get()
        # Simulate order execution
        print(f"⚡ Executing order: {signal['action'].upper()} {signal['symbol']}")
        await asyncio.sleep(0.2)  # simulate latency
        queue.task_done()

async def main():
    await asyncio.gather(signal_producer(), order_executor())

if __name__ == "__main__":
    asyncio.run(main())
