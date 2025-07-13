from .loop_defense_engine import LoopDefenseEngine

def simulate_loop_defense():
    engine = LoopDefenseEngine()
    dummy_state = {"confidence": 0.5}

    for _ in range(60):
        allowed, reason = engine.check_safe_to_proceed("signal_loop", dummy_state)
        if not allowed:
            return f"🛑 Blocked: {reason}"
    return "✅ Safe: No loop detected"

if __name__ == "__main__":
    print(simulate_loop_defense())