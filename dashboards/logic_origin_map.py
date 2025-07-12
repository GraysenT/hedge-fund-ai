```python
# Define a dictionary to map the origin of each strategy
strategy_origins = {
    "Cost Leadership": {"origin": "Porter's Generic Strategies", "type": "inspired"},
    "Differentiation": {"origin": "Porter's Generic Strategies", "type": "inspired"},
    "Focus Strategy": {"origin": "Porter's Generic Strategies", "type": "inspired"},
    "Blue Ocean Strategy": {"origin": "W. Chan Kim and Renée Mauborgne", "type": "self-built"},
    "Growth Hacking": {"origin": "Sean Ellis", "type": "self-built"},
    "Lean Startup": {"origin": "Eric Ries", "type": "self-built"},
    "Agile Methodology": {"origin": "Software Development", "type": "inspired"},
    "Six Sigma": {"origin": "Motorola", "type": "self-built"},
    "SWOT Analysis": {"origin": "Albert Humphrey", "type": "self-built"},
    "PEST Analysis": {"origin": "Francis Aguilar", "type": "self-built"}
}

# Function to display the origin and type of each strategy
def display_strategy_origins():
    for strategy, details in strategy_origins.items():
        print(f"Strategy: {strategy}")
        print(f"  Origin: {details['origin']}")
        print(f"  Type: {details['type']}\n")

# Call the function to display the information
display_strategy_origins()
```