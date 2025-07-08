import os
import json

def replay_audit_log(date="latest"):
    log_dir = "logs/audit"
    if date == "latest":
        files = sorted(os.listdir(log_dir))[-1:]
    else:
        files = [f"{date}.jsonl"]

    for file in files:
        print(f"\n🔁 Replaying: {file}")
        with open(os.path.join(log_dir, file)) as f:
            for line in f:
                record = json.loads(line)
                print(f"[{record['timestamp']}] {record['type']}: {record['details']}")

if __name__ == "__main__":
    replay_audit_log()