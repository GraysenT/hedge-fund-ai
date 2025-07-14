from expansion.opportunity_scanner import scan_opportunities

def launch_new_venture(agent):
    idea = scan_opportunities()
    return {
        "type": "Startup",
        "name": f"{agent}_Venture",
        "origin": idea
    }