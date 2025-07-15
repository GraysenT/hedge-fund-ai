import asyncio
async def train_all(models):
    for m in models:
        await asyncio.sleep(0.1)
        print(f"Trained: {m}")
