"""
Applies a patch to the 'slow_react_scalper' strategy by replacing or overriding
its main signal function with a protected version that handles failure cases
and adds correction logic.
"""

import importlib
import types

def patch_slow_react_scalper():
    try:
        module = importlib.import_module("strategies.slow_react_scalper")

        if hasattr(module, "generate_signal"):
            original_func = module.generate_signal

            def patched_function(*args, **kwargs):
                try:
                    signal = original_func(*args, **kwargs)
                    # Optional correction or override
                    if signal == "late_buy":
                        return "skip"
                    return signal
                except Exception as e:
                    print(f"[PATCH] slow_react_scalper failed: {e}")
                    return None

            module.generate_signal = types.FunctionType(
                patched_function.__code__, 
                globals(), 
                name="generate_signal"
            )
            print("[PATCH] slow_react_scalper patched successfully.")
        else:
            print("[PATCH] No generate_signal() found to patch.")

    except Exception as e:
        print(f"[PATCH] Failed to patch slow_react_scalper: {e}")