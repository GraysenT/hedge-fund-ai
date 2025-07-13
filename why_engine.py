```python
class DecisionChain:
    def __init__(self, decision, reason):
        self.decision = decision
        self.reason = reason
        self.sub_decisions = []

    def add_sub_decision(self, decision, reason):
        sub_decision = DecisionChain(decision, reason)
        self.sub_decisions.append(sub_decision)
        return sub_decision

    def display_chain(self, level=0):
        indent = "  " * level
        print(f"{indent}- Decision: {self.decision}, Reason: {self.reason}")
        for sub_decision in self.sub_decisions:
            sub_decision.display_chain(level + 1)

# Example usage
if __name__ == "__main__":
    # Create a main decision
    main_decision = DecisionChain("Expand the company", "Increase market share")

    # Add sub-decisions
    sub_decision1 = main_decision.add_sub_decision("Open a new office in Europe", "Growing demand in European market")
    sub_decision1.add_sub_decision("Choose Germany for new office", "Strong economy and central location")
    sub_decision1.add_sub_decision("Hire new staff", "Need more manpower to handle operations")

    sub_decision2 = main_decision.add_sub_decision("Increase online marketing budget", "Boost online presence and sales")
    sub_decision2.add_sub_decision("Focus on social media ads", "High engagement rates")
    sub_decision2.add_sub_decision("Increase SEO efforts", "Improve organic reach")

    # Display the decision chain
    main_decision.display_chain()
```