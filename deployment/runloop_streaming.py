import asyncio
from core.realtime.ws_router import WSRouter
from core.router.signal_router import SignalRouter
from core.event_bus import EventBus
from data.signal_recorder import SignalRecorder
from strategies.trend_following import TrendFollowingStrategy
from core.trade_executor import TradeExecutor
from core.portfolio_manager import PortfolioManager

router = WSRouter()
bus = EventBus()
portfolio = PortfolioManager()
executor = TradeExecutor(MockBroker())
router = SignalRouter(executor, portfolio)
recorder = SignalRecorder()
strategy = TrendFollowingStrategy("Trend", {"base": 1})

async def process_event(event):
    price = event["price"]
    signal = strategy.generate_signal({"price": price, "ma": price * 0.98})
    if signal in ["buy", "sell"]:
        router.route("BTCUSDT", signal, price)
        recorder.log(strategy.name, "BTCUSDT", signal, price)

async def main():
    bus.subscribe(lambda e: asyncio.create_task(process_event(e)))
    router.subscribe(lambda e: bus.publish(e))
    await router.run()

class MockBroker:
    def buy(self, symbol, qty): print(f"BUY {symbol} x {qty}")
    def sell(self, symbol, qty): print(f"SELL {symbol} x {qty}")

if __name__ == "__main__":
    asyncio.run(main())