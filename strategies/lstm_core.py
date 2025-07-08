import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

class LSTMStrategy:
    def __init__(self):
        self.model = None
        self.scaler = MinMaxScaler()

    def train(self, prices: pd.Series):
        data = self.scaler.fit_transform(prices.values.reshape(-1, 1))
        X, y = [], []
        for i in range(50, len(data)):
            X.append(data[i-50:i])
            y.append(data[i])

        X, y = np.array(X), np.array(y)

        self.model = Sequential()
        self.model.add(LSTM(64, return_sequences=False, input_shape=(X.shape[1], 1)))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mse')
        self.model.fit(X, y, epochs=10, verbose=0)

    def predict(self, prices: pd.Series):
        data = self.scaler.transform(prices.values.reshape(-1, 1))
        last_window = data[-50:].reshape(1, 50, 1)
        prediction = self.model.predict(last_window)[0][0]
        prediction = self.scaler.inverse_transform([[prediction]])[0][0]

        last_price = prices.values[-1]
        confidence = min(abs(prediction - last_price) / last_price, 1.0)
        action = "BUY" if prediction > last_price else "SELL"

        return {
            "symbol": prices.name,
            "confidence": round(confidence, 2),
            "action": action,
            "strategy": "LSTM"
        }