from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Hedge Fund AI is running"}

@app.post("/mute_strategy/{strategy}")
def mute_strategy(strategy: str):
    os.system(f"python3 -m strategy_router.mute {strategy}")
    return {"message": f"{strategy} muted"}

@app.post("/promote_strategy/{strategy}")
def promote_strategy(strategy: str):
    os.system(f"python3 -m strategy_router.promote {strategy}")
    return {"message": f"{strategy} promoted"}