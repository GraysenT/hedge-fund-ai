from strategies.lstm_forecaster import LSTMForecastStrategy
from data.historical_data_loader import get_data

def train_lstm():
    df = get_data("AAPL", "6mo", "1d")
    close_prices = df["Close"].dropna().tolist()

    strat = LSTMForecastStrategy("LSTM", {"type": "ML"})
    strat.train(close_prices)
    print("✅ LSTM model trained.")
    return strat

if __name__ == "__main__":
    train_lstm()