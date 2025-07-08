import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam

def load_price_sequence(symbol, window=30):
    df = pd.read_csv(f"data/price_history/{symbol}.csv")
    prices = df["close"].values[-window:]
    X = (prices - np.mean(prices)) / np.std(prices)
    return X.reshape(1, window, 1)

def create_model():
    model = Sequential([
        LSTM(32, input_shape=(30, 1)),
        Dense(1)
    ])
    model.compile(optimizer=Adam(0.001), loss="mse")
    return model

def train_ensemble(symbol, n=3):
    X = np.random.randn(500, 30, 1)
    y = np.random.randn(500, 1)
    models = []
    for _ in range(n):
        m = create_model()
        m.fit(X, y, epochs=5, verbose=0)
        models.append(m)
    return models

def predict(symbol):
    input_seq = load_price_sequence(symbol)
    models = train_ensemble(symbol)
    preds = [m.predict(input_seq)[0][0] for m in models]
    return round(np.mean(preds), 4)

if __name__ == "__main__":
    print("🔮 TSLA Prediction:", predict("TSLA"))
