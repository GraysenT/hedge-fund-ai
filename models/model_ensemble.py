def predict_lstm(X):
    return np.mean(X) + np.random.normal(0, 0.01)

def predict_cnn(X):
    return np.mean(X[-10:]) + np.random.normal(0, 0.015)

def predict_transformer(X):
    return np.mean(X) + np.random.normal(0, 0.02)

def full_ensemble_predict(X):
    lstm = predict_lstm(X)
    cnn = predict_cnn(X)
    trf = predict_transformer(X)
    return round(np.mean([lstm, cnn, trf]), 4)

if __name__ == "__main__":
    X = np.random.randn(30)
    print("📈 Ensemble Forecast:", full_ensemble_predict(X))
    