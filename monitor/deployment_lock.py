def is_deployment_locked():
    return os.path.exists("memory/deployment_locked.flag")

def lock_deployment():
    with open("memory/deployment_locked.flag", "w") as f:
        f.write("LOCKED")
    print("🔒 Deployment locked due to errors.")

def unlock_deployment():
    try:
        os.remove("memory/deployment_locked.flag")
        print("🔓 Deployment unlocked.")
    except:
        pass