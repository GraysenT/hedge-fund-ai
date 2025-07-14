class MultiAgentOrchestrator:
    def __init__(self, agents):
        self.agents = agents
        self.memory = []

    def collect(self, proposal):
        self.memory.append(proposal)

    def summarize(self):
        return ' | '.join(self.memory)

    def refine_plan(self, feedback):
        return f'Refined plan from GPT: {feedback}'

    def run(self, market_state, gpt_analyze):
        for agent in self.agents:
            self.collect(agent.propose(market_state))
        summary = self.summarize()
        feedback = gpt_analyze(summary)
        return self.refine_plan(feedback)