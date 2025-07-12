```python
def display_nesting(data, level=0):
    for key, value in data.items():
        print('  ' * level + f"{key}")
        if isinstance(value, dict):
            display_nesting(value, level + 1)

# Example data structure
data = {
    'Signal1': {
        'StrategyA': {
            'Decision1': {},
            'Decision2': {}
        },
        'StrategyB': {}
    },
    'Signal2': {
        'StrategyC': {
            'Decision3': {
                'SubDecision1': {}
            }
        }
    }
}

display_nesting(data)
```