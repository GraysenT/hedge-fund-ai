import os
import subprocess

class StrategyBuilder:
    def __init__(self, plugins_dir="plugins"):
        self.plugins_dir = plugins_dir

    def lint_all(self):
        for file in os.listdir(self.plugins_dir):
            if file.endswith(".py"):
                print(f"🧪 Verifying {file}")
                result = subprocess.run(["flake8", os.path.join(self.plugins_dir, file)], capture_output=True)
                if result.returncode == 0:
                    print("✅ Clean")
                else:
                    print("❌ Issues found:\n", result.stdout.decode())