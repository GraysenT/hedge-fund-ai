import pandas as pd

def evaluate_performance(trades):
    trades["PnL"] = trades["ExitPrice"] - trades["EntryPrice"]
    total_pnl = trades["PnL"].sum()
    win_rate = (trades["PnL"] > 0).mean()
    avg_win = trades[trades["PnL"] > 0]["PnL"].mean()
    avg_loss = trades[trades["PnL"] <= 0]["PnL"].mean()
    sharpe = trades["PnL"].mean() / (trades["PnL"].std() + 1e-6)

    return {
        "TotalPnL": total_pnl,
        "WinRate": win_rate,
        "AvgWin": avg_win,
        "AvgLoss": avg_loss,
        "Sharpe": sharpe
    }