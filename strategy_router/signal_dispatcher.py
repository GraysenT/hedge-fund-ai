from execution.executor import TradeExecutor

class SignalDispatcher:
    def __init__(self, mode='paper'):
        self.executor = TradeExecutor(mode=mode)

    def dispatch(self, signal_candidates):
        for signal in signal_candidates:
            if self._validate_signal(signal):
                executed = self.executor.execute_trade(signal)
                print(f"[DISPATCHED] {executed}")

    def _validate_signal(self, signal):
        return signal.get("confidence", 0) > 0.7