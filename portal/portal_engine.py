from portal.portal_engine import Portal

def connect_realities(agent, from_loop, to_loop):
    p = Portal(from_loop, to_loop)
    p.transport(agent)

class Portal:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def transport(self, agent):
        agent.location = self.target