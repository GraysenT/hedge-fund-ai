import importlib.util
import os

PLUGINS_DIR = "plugins"

def load_and_run(plugin_name):
    path = os.path.join(PLUGINS_DIR, plugin_name + ".py")
    if not os.path.exists(path):
        print("❌ Plugin not found.")
        return

    spec = importlib.util.spec_from_file_location(plugin_name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        if hasattr(mod, "run"):
            mod.run()
        else:
            print("⚠️ Plugin does not have a `run()` method.")
    except Exception as e:
        print(f"❌ Plugin failed: {e}")

if __name__ == "__main__":
    print("📦 Available plugins:", [f[:-3] for f in os.listdir(PLUGINS_DIR) if f.endswith(".py")])
    name = input("🔌 Plugin to load: ")
    load_and_run(name)
