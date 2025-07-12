import traceback

def try_patch_logic(logic_fn, fallback=None):
    """
    Runs a strategy function, attempts fallback or auto-patch if error occurs.
    """
    try:
        return logic_fn()
    except Exception as e:
        print("[AutoPatch] Logic failed. Attempting patch...")
        print(traceback.format_exc())

        if fallback:
            try:
                return fallback()
            except Exception as fallback_error:
                print("[AutoPatch] Fallback failed:", fallback_error)
                return None
        return None