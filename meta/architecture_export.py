import os
from datetime import datetime

def export():
    folders = ["meta", "models", "agents", "execution", "reporting", "plugins", "dashboards"]
    lines = ["# 🔧 Full AI Fund Architecture Overview", f"Exported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ""]

    for folder in folders:
        lines.append(f"## 📁 {folder}/")
        for f in os.listdir(folder):
            if f.endswith(".py") or f.endswith(".json"):
                lines.append(f" - {f}")
        lines.append("")

    path = "meta/final_architecture.md"
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"📦 Architecture exported to {path}")

if __name__ == "__main__":
    export()
    