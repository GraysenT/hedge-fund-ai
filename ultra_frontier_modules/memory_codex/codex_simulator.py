from .codex_writer import write_codex_entry
from .codex_reader import load_codex

def simulate_codex_entry():
    write_codex_entry(
        title="Market Dislocation Response",
        summary="System successfully exited long positions during an inflation shock.",
        key_learnings=["Trust macro layer more during CPI week", "Avoid high-beta assets under regime volatility"],
        tags=["macro", "risk", "shock", "inflation"]
    )
    return load_codex()

if __name__ == "__main__":
    print(simulate_codex_entry())