```python
# Define the path to the ethics file
ethics_file_path = 'system_ethics.txt'

# Define the updated ethics content
updated_ethics_content = """
Respect for human autonomy
Prevent harm
Ensure fairness
Be transparent
"""

# Function to update the ethics file
def update_ethics_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print("Ethics file has been updated.")

# Update the ethics file
update_ethics_file(ethics_file_path, updated_ethics_content)
```