import shap
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

def explain_model(model: Sequential, sample: np.ndarray):
    explainer = shap.DeepExplainer(model, sample)
    shap_values = explainer.shap_values(sample)
    shap.summary_plot(shap_values[0], sample)

# Example usage
if __name__ == "__main__":
    model = Sequential([
        LSTM(32, input_shape=(10, 1), return_sequences=True),
        LSTM(16),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse")
    dummy_input = np.random.rand(50, 10, 1)
    dummy_output = np.random.rand(50, 1)
    model.fit(dummy_input, dummy_output, epochs=1)

    explain_model(model, dummy_input[:10])