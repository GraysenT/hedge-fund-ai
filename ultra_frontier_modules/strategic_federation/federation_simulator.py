from .treaty_diplomacy_engine import propose_strategic_treaty

def simulate_federation_activity():
    treaty = propose_strategic_treaty(
        node_a="AtlasNode",
        node_b="MacroGuard",
        terms={
            "share_signals": True,
            "shared_capital_buffer": 200000,
            "risk_sync": True,
            "joint_alerts": True
        }
    )
    return treaty.serialize()

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_federation_activity())