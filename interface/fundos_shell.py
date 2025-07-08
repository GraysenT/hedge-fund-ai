import subprocess

def shell():
    print("💼 FundOS Shell — Type 'help' for commands")
    while True:
        cmd = input("FundOS> ").strip().lower()

        if cmd == "exit":
            break
        elif cmd == "evolve":
            subprocess.run(["python3", "evolve.py"])
        elif cmd == "audit":
            subprocess.run(["python3", "reporting/full_audit_report.py"])
        elif cmd == "top":
            subprocess.run(["python3", "dashboards/strategy_leaderboard.py"])
        elif cmd.startswith("run plugin "):
            name = cmd.replace("run plugin ", "")
            subprocess.run(["python3", "plugins/plugin_sandbox.py", name])
        elif cmd == "help":
            print("""
Commands:
 evolve         → Run full evolution cycle
 audit          → Generate full system audit
 top            → Show top performing strategies
 run plugin X   → Execute a plugin by name
 exit           → Exit the shell
""")
        else:
            print("❌ Unknown command. Type 'help'.")

if __name__ == "__main__":
    shell()
    