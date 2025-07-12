```python
# Define the system's mission and actions
system_mission = "to promote health and wellness in the community"
system_actions = [
    "organized a community health fair",
    "distributed healthy eating flyers",
    "sponsored a marathon",
    "hosted a fast food festival"
]

# Function to check if actions align with the mission
def check_mission_alignment(mission, actions):
    divergent_actions = []
    keywords = mission.split()
    
    for action in actions:
        if not any(keyword in action for keyword in keywords):
            divergent_actions.append(action)
    
    return divergent_actions

# Identify divergent actions
divergent_actions = check_mission_alignment(system_mission, system_actions)

# Output divergent actions
print("Actions that diverged from the mission:")
for action in divergent_actions:
    print(action)
```