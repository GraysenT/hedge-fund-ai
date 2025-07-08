import os
import shutil
from datetime import datetime

def push_reflection():
    path = sorted(os.listdir("meta/reflections"))[-1]
    dest = f"federation/reflection_pool/{os.getenv('NODE_ID', 'node1')}_{datetime.now().strftime('%Y-%m-%d')}.txt"
    shutil.copy(f"meta/reflections/{path}", dest)
    print(f"🔁 Shared reflection: {dest}")

def view_pool():
    for f in sorted(os.listdir("federation/reflection_pool")):
        print(f"\n📄 {f}")
        print(open(f"federation/reflection_pool/{f}").read()[:300], "...\n")

if __name__ == "__main__":
    os.makedirs("federation/reflection_pool", exist_ok=True)
    push_reflection()
    view_pool()
    