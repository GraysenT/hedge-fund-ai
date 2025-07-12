import pandas as pd

def compute_alpha_attribution(trade_log_path):
    df = pd.read_csv(trade_log_path)
    df["PnL"] = df["ExitPrice"] - df["EntryPrice"]
    df["Strategy"] = df.get("Strategy", "Unknown")

    strat_group = df.groupby("Strategy")["PnL"].sum().sort_values(ascending=False)
    asset_group = df.groupby("Symbol")["PnL"].sum().sort_values(ascending=False)
    signal_group = df.groupby("SignalSource")["PnL"].sum().sort_values(ascending=False)

    return {
        "ByStrategy": strat_group,
        "ByAsset": asset_group,
        "BySignal": signal_group
    }