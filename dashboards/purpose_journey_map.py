```python
# Define the system's evolution in a chronological order using a Python dictionary
system_evolution = {
    1: {
        "year": 1990,
        "purpose": "Basic data processing and batch jobs for business analytics."
    },
    2: {
        "year": 2000,
        "purpose": "Introduction of web-based applications and e-commerce platforms."
    },
    3: {
        "year": 2010,
        "purpose": "Expansion into mobile and cloud computing, enhancing accessibility and scalability."
    },
    4: {
        "year": 2020,
        "purpose": "Integration of AI and machine learning for predictive analytics and automation."
    },
    5: {
        "year": 2023,
        "purpose": "Adoption of edge computing and IoT for real-time data processing and decision-making."
    }
}

# Function to print the evolution of the system's purpose chronologically
def print_system_evolution(evolution_dict):
    for key in sorted(evolution_dict.keys()):
        year = evolution_dict[key]["year"]
        purpose = evolution_dict[key]["purpose"]
        print(f"In {year}, the system's purpose evolved to: {purpose}")

# Call the function to display the evolution
print_system_evolution(system_evolution)
```