import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam

def generate_mock_data(seq_len=30, num_samples=500):
    X = np.random.randn(num_samples, seq_len, 1)
    y = np.random.randn(num_samples, 1)
    return X, y

def create_model():
    model = Sequential([
        LSTM(32, input_shape=(30, 1)),
        Dense(1)
    ])
    model.compile(optimizer=Adam(0.001), loss="mse")
    return model

def train_ensemble(n=3):
    models = []
    X, y = generate_mock_data()
    for i in range(n):
        model = create_model()
        model.fit(X, y, epochs=5, verbose=0)
        models.append(model)
    return models

def predict_ensemble(models, input_seq):
    preds = [m.predict(input_seq)[0][0] for m in models]
    return np.mean(preds)

if __name__ == "__main__":
    models = train_ensemble()
    test = np.random.randn(1, 30, 1)
    pred = predict_ensemble(models, test)
    print(f"🎯 Ensemble Prediction: {pred:.4f}")
    