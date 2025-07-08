import speech_recognition as sr
import subprocess

COMMANDS = {
    "leaderboard": "python3 dashboards/agent_leaderboard.py",
    "evolution": "python3 evolve.py",
    "capital": "python3 dashboards/portfolio_manager.py"
}

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        audio = r.listen(source)

    try:
        cmd = r.recognize_google(audio).lower()
        print(f"🗣 You said: {cmd}")
        for key, val in COMMANDS.items():
            if key in cmd:
                print(f"🚀 Running: {val}")
                subprocess.run(val.split())
                return
        print("❌ No matching command.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    listen()
