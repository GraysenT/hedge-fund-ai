import sys
from control.override_manager import set_override

def run_cli():
    if len(sys.argv) != 3:
        print("Usage: python cli_control.py <override_key> <true/false>")
        return
    key = sys.argv[1]
    value = sys.argv[2].lower() == "true"
    set_override(key, value)
    print(f"✅ Set override: {key} = {value}")

if __name__ == "__main__":
    run_cli()