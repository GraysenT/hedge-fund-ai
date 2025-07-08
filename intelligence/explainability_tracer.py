class ExplainabilityTracer:
    def __init__(self):
        self.traces = {}

    def trace(self, signal):
        key = f"{signal['symbol']}_{signal['strategy']}"
        trace = {
            "symbol": signal["symbol"],
            "strategy": signal["strategy"],
            "confidence": signal["confidence"],
            "factors": signal.get("factors", []),
            "context": signal.get("context", {})
        }
        self.traces[key] = trace
        print(f"[EXPLAIN] Traced signal: {trace}")
        return trace

    def get_trace(self, key):
        return self.traces.get(key)