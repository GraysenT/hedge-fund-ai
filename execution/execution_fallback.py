class ExecutionFallback:
    def __init__(self, primary_executor, secondary_executor):
        self.primary = primary_executor
        self.secondary = secondary_executor

    def safe_execute(self, signal):
        try:
            return self.primary.execute_trade(signal)
        except Exception as e:
            print(f"[FALLBACK] Primary executor failed: {e}. Attempting secondary.")
            try:
                return self.secondary.execute_trade(signal)
            except Exception as e2:
                print(f"[FALLBACK ERROR] Secondary executor also failed: {e2}")
                return None