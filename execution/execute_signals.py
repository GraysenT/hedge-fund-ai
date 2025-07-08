import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from execution.signal_gate import SignalGate

# Mock execution function (replace with real logic)
def execute_trade(signal):
    print(f"✅ Executed: {signal['asset']} - {signal['direction']}")

# Optional: log skipped signals for dashboard or CSV
def log_skipped(signal, reason):
    print(f"⛔ Skipped: {signal['asset']} - {reason}")

# Main signal processor
def process_signals(signal_list):
    gate = SignalGate()
    for signal in signal_list:
        if gate.is_signal_allowed(signal):
            execute_trade(signal)
        else:
            log_skipped(signal, reason="Market Closed")

# Example usage
if __name__ == "__main__":
    test_signals = [
        {"asset": "SPY_US", "type": "stock", "region": "US", "confidence": 0.9, "direction": "buy"},
        {"asset": "BTC", "type": "crypto", "region": "Global", "confidence": 0.95, "direction": "buy"},
        {"asset": "DAX_UK", "type": "stock", "region": "UK", "confidence": 0.85, "direction": "sell"}
    ]
    process_signals(test_signals)
    