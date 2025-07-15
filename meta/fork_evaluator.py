from registry.agent_registry import retire_agent

def evaluate_forks(fork_agents):
    for agent in fork_agents:
        if agent.runtime_seconds() > 86400:
            if agent.sharpe < 0.5:
                retire_agent(agent.id)
            elif agent.sharpe > 2.5:
                agent.parent.absorb(agent.config)