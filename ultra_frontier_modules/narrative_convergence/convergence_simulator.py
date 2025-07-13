from .narrative_signal import NarrativeSignal
from .convergence_grid import ConvergenceGrid

def simulate_convergence():
    grid = ConvergenceGrid()

    signals = [
        NarrativeSignal("AI Inflation Hedging", "Equities", "signal_core", 0.74),
        NarrativeSignal("AI Inflation Hedging", "Macro", "macro_oracle", 0.81),
        NarrativeSignal("AI Inflation Hedging", "Crypto", "sentiment_scout", 0.67),
        NarrativeSignal("Green Tech Alpha", "Commodities", "enviro_model", 0.5)
    ]

    for sig in signals:
        grid.register_signal(sig)

    return grid.detect_convergence()

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_convergence())