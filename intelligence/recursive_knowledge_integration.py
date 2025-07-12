class RecursiveKnowledgeIntegration:
    def __init__(self):
        self.knowledge_bases = []

    def integrate_knowledge(self, domain, knowledge):
        """Integrate new knowledge into the recursive system across domains."""
        knowledge_base = {"domain": domain, "knowledge": knowledge}
        self.knowledge_bases.append(knowledge_base)
        print(f"Integrated knowledge for domain: {domain}")
    
    def get_knowledge_bases(self):
        return self.knowledge_bases