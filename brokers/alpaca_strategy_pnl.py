import os
import json
from datetime import datetime
import alpaca_trade_api as tradeapi

def load_trade_logs():
    folder = "memory/trade_logs"
    if not os.path.exists(folder):
        return {}

    strategy_map = {}
    for file in sorted(os.listdir(folder)):
        with open(os.path.join(folder, file)) as f:
            trades = json.load(f)
            for t in trades:
                strat = t["strategy"]
                symbol = t["symbol"]
                if strat not in strategy_map:
                    strategy_map[strat] = set()
                strategy_map[strat].add(symbol)
    return strategy_map

def get_symbol_pnls(api_key, secret_key, base_url="https://paper-api.alpaca.markets"):
    api = tradeapi.REST(api_key, secret_key, base_url, api_version='v2')
    today = datetime.now().date().isoformat()
    pnl_by_symbol = {}

    acts = api.get_activities(activity_types="FILL")
    for act in acts:
        if act.transaction_time.date().isoformat() != today:
            continue
        symbol = act.symbol
        qty = float(act.qty)
        price = float(act.price)
        side = act.side
        cost = qty * price * (-1 if side == 'buy' else 1)

        if symbol not in pnl_by_symbol:
            pnl_by_symbol[symbol] = 0.0
        pnl_by_symbol[symbol] += cost

    return pnl_by_symbol

def map_strategy_pnls(strategy_map, pnl_by_symbol):
    strat_pnl = {}
    for strat, symbols in strategy_map.items():
        total = 0.0
        for sym in symbols:
            total += pnl_by_symbol.get(sym, 0.0)
        strat_pnl[strat] = round(total, 2)
    return strat_pnl

if __name__ == "__main__":
    API_KEY = os.getenv("ALPACA_API_KEY")
    SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

    strategy_symbols = load_trade_logs()
    pnl_by_symbol = get_symbol_pnls(API_KEY, SECRET_KEY)
    strat_pnls = map_strategy_pnls(strategy_symbols, pnl_by_symbol)

    print("📊 Real PnL by Strategy:")
    for strat, pnl in strat_pnls.items():
        arrow = "📈" if pnl > 0 else "📉"
        print(f"{arrow} {strat}: ${pnl}")
