import speech_recognition as sr
import subprocess

COMMANDS = {
    "buy tsla": lambda: print("🟢 Signal: BUY TSLA"),
    "show top": lambda: subprocess.run(["python3", "dashboards/strategy_leaderboard.py"]),
    "mute": lambda strat: print(f"🔇 Strategy muted: {strat}")
}

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Speak...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).lower()
        print(f"🗣 You said: {text}")

        if "buy tsla" in text:
            COMMANDS["buy tsla"]()
        elif "show top" in text:
            COMMANDS["show top"]()
        elif "mute" in text:
            strat = text.split("mute ")[-1].strip()
            COMMANDS["mute"](strat)
        else:
            print("❌ Command not recognized.")
    except Exception as e:
        print("❌ Voice input failed:", e)

if __name__ == "__main__":
    listen()
    