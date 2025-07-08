from collections import defaultdict

class FusionScorer:
    def __init__(self):
        self.signal_stack = defaultdict(list)

    def add_signal(self, signal):
        symbol = signal.get("symbol")
        self.signal_stack[symbol].append(signal)

    def compute_fused_signals(self):
        fused = {}
        for symbol, signals in self.signal_stack.items():
            action_scores = defaultdict(float)
            for signal in signals:
                action = signal.get("action")
                conf = signal.get("confidence", 0)
                action_scores[action] += conf
            best_action = max(action_scores, key=action_scores.get)
            avg_conf = action_scores[best_action] / len(signals)
            fused[symbol] = {
                "symbol": symbol,
                "action": best_action,
                "confidence": round(avg_conf, 3),
                "strategy": "Fusion"
            }
        return fused