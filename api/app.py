from fastapi import FastAPI
from pydantic import BaseModel
from core.strategy_registry import StrategyRegistry

app = FastAPI(title="Hedge Fund AI API")

registry = StrategyRegistry("strategies")
registry.discover_strategies()
strategies = [cls(name=cls.__name__, parameters={"base": 1}) for cls in registry.get_all()]

class MarketDataInput(BaseModel):
    data: dict

@app.get("/strategies")
def list_strategies():
    return [s.name for s in strategies]

@app.post("/signal")
def get_signal(input: MarketDataInput):
    results = {}
    for s in strategies:
        try:
            signal = s.generate_signal(input.data)
            results[s.name] = signal
        except Exception as e:
            results[s.name] = f"error: {str(e)}"
    return results