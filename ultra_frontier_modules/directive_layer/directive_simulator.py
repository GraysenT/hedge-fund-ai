from .sovereign_directive import SovereignDirective
from .directive_dispatcher import save_directive

def simulate_directive_trigger():
    directive = SovereignDirective(
        tag="CapitalDefense",
        conditions={"volatility": ">0.5", "capital_drawdown": ">2%"},
        directive_text="Freeze all high-risk signals and move to capital protection protocols."
    )
    save_directive(directive)
    return directive.serialize()

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_directive_trigger())