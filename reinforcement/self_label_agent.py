import pandas as pd
from utils.paths import SIGNAL_LOG, TRADE_LOG_FILE, STRATEGY_STATUS_FILE

def self_label_and_reinforce():
    try:
        signals = pd.read_json(SIGNAL_LOG)
        trades = pd.read_csv(TRADE_LOG_FILE)
    except Exception as e:
        print(f"[SelfLabelAgent] Failed to load logs: {e}")
        return

    if signals.empty or trades.empty:
        return

    trades["PnL"] = trades["ExitPrice"] - trades["EntryPrice"]
    trades["Result"] = trades["PnL"].apply(lambda x: 1 if x > 0 else -1)

    scores = trades.groupby("SignalID")["Result"].mean()

    strategy_rewards = trades.groupby("Strategy")["PnL"].mean()
    status = pd.read_json(STRATEGY_STATUS_FILE)
    status = status.set_index("Strategy")
    status["RewardScore"] = strategy_rewards

    status.to_json(STRATEGY_STATUS_FILE, indent=2)
    print("[SelfLabelAgent] Updated strategy reward scores.")