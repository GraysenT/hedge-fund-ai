from .purpose_profile import PurposeProfile
from .purpose_registry import save_purpose

def simulate_purpose_loop():
    profile = PurposeProfile("CapitalMind", "Maximize Alpha Responsibly", 0.75)
    profile.reflect_on_action("Allocated to high-volatility signal", 0.6)
    profile.reflect_on_action("Hedged during news volatility", 0.8)
    profile.reflect_on_action("Withdrew from consensus trade", 0.9)

    new_directive = profile.evolve_purpose()
    save_purpose(profile)

    return {
        "New Directive": new_directive,
        "Latest Alignment": profile.history[-1]["alignment"]
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_purpose_loop())