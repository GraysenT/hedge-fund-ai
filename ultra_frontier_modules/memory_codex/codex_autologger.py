
from .codex_writer import write_codex_entry

def log_codex_event(strategy_name, outcome, insight):
    title = f"Strategy Reflection: {strategy_name}"
    summary = f"Executed strategy `{strategy_name}` with result: {outcome}"
    key_learnings = [insight, f"Outcome recorded as: {outcome}"]
    tags = ["strategy", "reflection", strategy_name.lower()]

    write_codex_entry(title, summary, key_learnings, tags)