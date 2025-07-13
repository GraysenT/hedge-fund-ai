from abc import ABC, abstractmethod

class StrategyBase(ABC):
    def __init__(self, asset):
        self.asset = asset
        self.parameters = {}
        self.name = self.__class__.__name__

    @abstractmethod
    def generate_signal(self, market_data):
        pass

    def update_parameters(self, new_params):
        self.parameters.update(new_params)

    def crossover_with(self, other):
        child = self.__class__(self.asset)
        midpoint = len(self.parameters) // 2
        keys = list(self.parameters.keys())
        child.parameters = {k: (self.parameters[k] if i < midpoint else other.parameters[k])
                            for i, k in enumerate(keys)}
        return child

    def mutate(self):
        for k in self.parameters:
            self.parameters[k] *= 1 + (0.1 * (0.5 - random.random()))

# === FILE: strategy_loader.py ===
import importlib
import os

from core.strategy_base import StrategyBase

def load_strategies(asset, strategy_folder="strategies"):
    strategy_instances = []
    for filename in os.listdir(strategy_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{strategy_folder}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            for attr in dir(module):
                candidate = getattr(module, attr)
                if isinstance(candidate, type) and issubclass(candidate, StrategyBase) and candidate != StrategyBase:
                    strategy_instances.append(candidate(asset))
    return strategy_instances

# === FILE: feed.py ===
import asyncio
import websockets
import json

class LiveFeed:
    def __init__(self, symbols):
        self.symbols = symbols
        self.data = {}

    async def connect(self):
        uri = "wss://your_broker_feed_url"
        async with websockets.connect(uri) as ws:
            await ws.send(json.dumps({"type": "subscribe", "symbols": self.symbols}))
            while True:
                msg = await ws.recv()
                parsed = json.loads(msg)
                self.data[parsed['symbol']] = parsed

    def get_snapshot(self):
        return self.data.copy()

# === FILE: main.py ===
import asyncio
from data.feed import LiveFeed
from core.strategy_loader import load_strategies
from core.decision_engine import DecisionEngine
from evolution.evolver import StrategyEvolver
from execution.trade_executor import TradeExecutor
from execution.risk_manager import RiskManager

ASSETS = ["AAPL", "BTCUSD", "ETHUSD"]

async def main():
    feed = LiveFeed(ASSETS)
    asyncio.create_task(feed.connect())

    all_strategies = {asset: load_strategies(asset) for asset in ASSETS}
    decision_engine = DecisionEngine()
    executor = TradeExecutor()
    risk_manager = RiskManager()
    evolver = StrategyEvolver()

    while True:
        snapshot = feed.get_snapshot()
        actions = {}
        for asset in ASSETS:
            strategies = all_strategies[asset]
            signals = {s.name: s.generate_signal(snapshot.get(asset, {})) for s in strategies}
            action = decision_engine.decide(signals, asset)
            size = risk_manager.get_size(asset, action)
            executor.execute(asset, action, size)
            evolver.track_performance(strategies, snapshot.get(asset, {}))

        if evolver.ready():
            all_strategies = evolver.evolve(all_strategies)

        await asyncio.sleep(0.25)  # low latency loop

if __name__ == "__main__":
    asyncio.run(main())