from .ego_agent import EgoAgent
import random

def simulate_conflict(topic):
    agent1 = EgoAgent("MomentumAI", "aggressive", 0.7, 0.2)
    agent2 = EgoAgent("MacroThinker", "cautious", 0.5, 0.5)

    # Both receive conflicting signals
    agent1.update_belief(topic, new_value=0.8, signal_strength=0.9)
    agent2.update_belief(topic, new_value=0.3, signal_strength=0.2)

    return {
        "agent_1": agent1.express_opinion(topic),
        "agent_2": agent2.express_opinion(topic),
        "disagreement": abs(agent1.beliefs[topic] - agent2.beliefs[topic])
    }