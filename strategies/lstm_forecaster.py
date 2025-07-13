from core.strategy_base import StrategyBase
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

class LSTMForecastStrategy(StrategyBase):
    def __init__(self, name, parameters):
        super().__init__(name, parameters)
        self.model = self._build_model()
        self.trained = False

    def _build_model(self):
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=(10, 1)))
        model.add(LSTM(50))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')
        return model

    def train(self, series):
        data = np.array(series).reshape(-1, 1)
        X, y = [], []
        for i in range(10, len(data)):
            X.append(data[i-10:i])
            y.append(data[i])
        X, y = np.array(X), np.array(y)
        self.model.fit(X, y, epochs=5, verbose=0)
        self.trained = True

    def generate_signal(self, market_data):
        if not self.trained or len(market_data["history"]) < 10:
            return "hold"
        recent = np.array(market_data["history"][-10:]).reshape(1, 10, 1)
        predicted = self.model.predict(recent)[0][0]
        current_price = market_data["price"]
        if predicted > current_price:
            return "buy"
        elif predicted < current_price:
            return "sell"
        return "hold"