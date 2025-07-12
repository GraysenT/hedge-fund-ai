import os

def patch_generate_signal(folder="strategies"):
    fixed = 0

    for fname in os.listdir(folder):
        if not fname.endswith(".py"):
            continue

        path = os.path.join(folder, fname)

        with open(path, "r") as f:
            content = f.read()

        if "def generate_signal()" in content:
            continue

        # Append stub
        with open(path, "a") as f:
            f.write("\n\ndef generate_signal():\n    return 'skip'\n")

        print(f"[PATCHED] {fname}")
        fixed += 1

    print(f"✅ Patched {fixed} strategy files with missing generate_signal().")

if __name__ == "__main__":
    patch_generate_signal()