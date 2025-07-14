from governance.ethics_engine import ethics_check

def hold_vote(issue, agents):
    results = [ethics_check(agent, issue) for agent in agents]
    return {"Yes": results.count(True), "No": results.count(False)}