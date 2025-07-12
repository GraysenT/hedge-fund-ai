```python
# File: blueprint_spec.py

class Blueprint:
    def __init__(self, name, description, impact_level, files_needed):
        self.name = name
        self.description = description
        self.impact_level = impact_level
        self.files_needed = files_needed

    def display_blueprint(self):
        print(f"Blueprint: {self.name}")
        print(f"Description: {self.description}")
        print(f"Impact Level: {self.impact_level}")
        print("Files Required:")
        for file in self.files_needed:
            print(f" - {file}")

def main():
    # Example blueprint for a major logic upgrade
    files = [
        "logic_processor.py",
        "data_handler.py",
        "ui_updater.py",
        "test_suite.py"
    ]

    major_logic_upgrade = Blueprint(
        name="Major Logic Upgrade",
        description="Enhances the core processing algorithms to improve performance and accuracy.",
        impact_level="High",
        files_needed=files
    )

    major_logic_upgrade.display_blueprint()

if __name__ == "__main__":
    main()
```