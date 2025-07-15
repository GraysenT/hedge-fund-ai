def build_features(raw):
    return {k: v * 0.01 for k, v in raw.items()}