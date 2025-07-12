import argparse
import json
from utils.paths import OVERRIDE_FILE

parser = argparse.ArgumentParser()
parser.add_argument("strategy", type=str)
parser.add_argument("--boost", type=float, default=1.0)
parser.add_argument("--note", type=str, default="Manual CLI override")

args = parser.parse_args()

try:
    overrides = {}
    with open(OVERRIDE_FILE, "r") as f:
        overrides = json.load(f)
except:
    overrides = {}

overrides[args.strategy] = {"boost": args.boost, "note": args.note}

with open(OVERRIDE_FILE, "w") as f:
    json.dump(overrides, f, indent=2)

print(f"✅ CLI override applied to {args.strategy}")