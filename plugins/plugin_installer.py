import json
import os

def install_plugin(submit_file):
    with open(submit_file) as f:
        data = json.load(f)

    name = data["author"] + "_" + str(hash(data["code"]))[:6]
    code = data["code"]

    plugin_path = f"plugins/{name}.py"
    with open(plugin_path, "w") as f:
        f.write(code)

    print(f"✅ Installed plugin: {plugin_path}")
    return name

if __name__ == "__main__":
    install_plugin("plugins/community_submissions/my_strategy.json")
    