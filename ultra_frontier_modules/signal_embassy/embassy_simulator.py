from .signal_embassy import SignalEmbassy
from .embassy_registry import save_embassy_log

def simulate_embassy_activity():
    embassy = SignalEmbassy(name="AsiaMacroObserver", domain="Asia", objective="detect regime shift")

    embassy.report_signal(0.82, {"volatility": 0.34, "macro_regime": "hawkish"})
    embassy.report_signal(0.74, {"liquidity": "tightening", "sentiment": "divergent"})
    embassy.adjust_trust(+0.1)

    save_embassy_log(embassy)
    return embassy.log

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_embassy_activity())