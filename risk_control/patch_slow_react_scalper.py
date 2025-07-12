"""
Patches the generate_signal function in slow_react_scalper to:
- Catch errors
- Override weak signals like 'late_buy'
- Log all patch behavior
"""

from strategies import slow_react_scalper

def patch_slow_react_scalper():
    """
    Wraps slow_react_scalper.generate_signal to apply logic overrides
    and print/log patched behavior.
    """
    if not hasattr(slow_react_scalper, "generate_signal"):
        print("[PATCH] No generate_signal() to patch.")
        return

    original_func = slow_react_scalper.generate_signal

    def wrapped_signal(*args, **kwargs):
        try:
            signal = original_func(*args, **kwargs)
            final_signal = "skip" if signal == "late_buy" else signal
            if signal != final_signal:
                log_line = f"[PATCHED SIGNAL] Original: {signal} → Final: {final_signal}"
                print(log_line)
                with open("logs/patch_log.txt", "a") as f:
                    f.write(log_line + "\n")
            return final_signal
        except Exception as e:
            error_log = f"[PATCH ERROR] slow_react_scalper failed: {e}"
            print(error_log)
            with open("logs/patch_log.txt", "a") as f:
                f.write(error_log + "\n")
            return None

    slow_react_scalper.generate_signal = wrapped_signal
    print("[PATCH] slow_react_scalper patched successfully.")

if __name__ == "__main__":
    patch_slow_react_scalper()