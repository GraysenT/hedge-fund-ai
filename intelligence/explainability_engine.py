def explain(signal):
    facts = extract_signal_features(signal)
    return GPTCopilot.generate(f"Explain the following signal: {facts}")