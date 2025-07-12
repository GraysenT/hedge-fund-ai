Below is a Python script that estimates whether an action was driven by reason, survival, or imitation based on user input. The script uses simple decision-making logic based on keywords to categorize the motivation behind an action.

```python
def categorize_action(action_description):
    # Keywords associated with reason, survival, and imitation
    reason_keywords = ['decide', 'think', 'plan', 'calculate', 'reason', 'logical', 'strategy']
    survival_keywords = ['eat', 'drink', 'escape', 'hide', 'survive', 'protect', 'defend']
    imitation_keywords = ['copy', 'imitate', 'follow', 'mimic', 'same', 'replicate', 'emulate']

    # Convert the action description to lower case for comparison
    action_description = action_description.lower()

    # Count occurrences of each type of keyword in the description
    reason_count = sum(action_description.count(word) for word in reason_keywords)
    survival_count = sum(action_description.count(word) for word in survival_keywords)
    imitation_count = sum(action_description.count(word) for word in imitation_keywords)

    # Determine the category with the highest count
    max_count = max(reason_count, survival_count, imitation_count)

    if max_count == 0:
        return "Uncategorized: No clear motivation detected."
    elif max_count == reason_count:
        return "Reason: The action is driven by logical thinking or planning."
    elif max_count == survival_count:
        return "Survival: The action is driven by basic survival instincts."
    elif max_count == imitation_count:
        return "Imitation: The action is driven by copying or mimicking others."

def main():
    # Get user input for the action description
    action_description = input("Describe the action: ")

    # Categorize the action
    result = categorize_action(action_description)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
```

This script prompts the user to describe an action. It then analyzes the description for keywords related to reason, survival, or imitation and categorizes the action accordingly. If no keywords are found, it categorizes the action as "Uncategorized."