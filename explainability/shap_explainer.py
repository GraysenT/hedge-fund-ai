import shap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os

MODEL_PATH = "models/lstm_model.pkl"
EXPLAIN_DATA = "logs/last_prediction_input.csv"

def explain_latest_prediction():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(EXPLAIN_DATA):
        print("❌ Missing model or input.")
        return

    model = joblib.load(MODEL_PATH)
    X = pd.read_csv(EXPLAIN_DATA)

    explainer = shap.Explainer(model.predict, X)
    shap_values = explainer(X)

    print("📉 SHAP values computed for latest prediction.")
    shap.plots.bar(shap_values[0], max_display=10)

if __name__ == "__main__":
    explain_latest_prediction()