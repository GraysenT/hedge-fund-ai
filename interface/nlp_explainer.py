class NLPExplainer:
    def explain_trade(self, signal):
        symbol = signal.get("symbol")
        strategy = signal.get("strategy")
        confidence = signal.get("confidence")
        action = signal.get("action")

        explanation = (
            f"The system recommends a {action} on {symbol} with {confidence * 100:.1f}% confidence "
            f"based on the active strategy '{strategy}', which has recently shown strong alpha potential."
        )
        print(f"[EXPLAINER] {explanation}")
        return explanation