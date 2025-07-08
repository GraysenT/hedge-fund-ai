import os

def search_memory(keyword):
    paths = [
        "meta/reflections/",
        "reporting/strategy_memos/",
        "meta/proposals/",
        "meta/dreams/"
    ]

    results = []
    for folder in paths:
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            if not path.endswith(".txt"):
                continue
            with open(path) as f:
                content = f.read()
                if keyword.lower() in content.lower():
                    results.append((file, content[:200]))

    print(f"🔍 Found {len(results)} matches for '{keyword}':")
    for name, snippet in results:
        print(f"📄 {name}:\n{snippet}...\n")

if __name__ == "__main__":
    search_memory(input("🔍 Enter search keyword: "))
    