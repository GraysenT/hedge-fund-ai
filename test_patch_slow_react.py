from risk_control.patch_slow_react_scalper import patch_slow_react_scalper
from strategies import slow_react_scalper

patch_slow_react_scalper()

signal = slow_react_scalper.generate_signal()
print(f"[TEST] Final patched signal: {signal}")