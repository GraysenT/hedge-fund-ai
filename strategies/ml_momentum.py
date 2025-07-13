from core.strategy_base import StrategyBase
import numpy as np
from sklearn.linear_model import LogisticRegression

class MLMomentumStrategy(StrategyBase):
    def __init__(self, name, parameters):
        super().__init__(name, parameters)
        self.model = LogisticRegression()
        self.trained = False

    def train(self, features, labels):
        self.model.fit(features, labels)
        self.trained = True

    def generate_signal(self, market_data):
        if not self.trained or "features" not in market_data:
            return "hold"
        X = np.array(market_data["features"]).reshape(1, -1)
        pred = self.model.predict(X)[0]
        return "buy" if pred == 1 else "sell"