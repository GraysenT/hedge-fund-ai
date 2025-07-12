class SignalContextAnnotator:
    def __init__(self):
        self.annotations = {}

    def annotate(self, signal, regime, sentiment, volume):
        signal_id = f"{signal['symbol']}_{signal['strategy']}"
        context = {
            "regime": regime,
            "sentiment": sentiment,
            "volume": volume
        }
        self.annotations[signal_id] = context
        print(f"[CONTEXT] {signal_id} annotated with {context}")
        return signal_id, context