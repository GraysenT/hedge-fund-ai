USERS = {
    "graysen": {"role": "admin", "api_key": "graysen123"},
    "alice": {"role": "client", "api_key": "alice456"},
    "bob": {"role": "viewer", "api_key": "bob789"}
}

def get_role(api_key):
    for user, data in USERS.items():
        if data["api_key"] == api_key:
            return data["role"]
    return None

if __name__ == "__main__":
    key = input("🔑 Enter API key: ")
    role = get_role(key)
    print(f"🧾 Access granted as: {role or '❌ unauthorized'}")
