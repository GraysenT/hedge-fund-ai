def run_dream_cycle(agent):
    dream = agent.generate_dream()
    result = agent.test_dream(dream)
    agent.update_beliefs(result)
    return f'Dream processed for {agent.id}'