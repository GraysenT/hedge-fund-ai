import speech_recognition as sr
from nlp.strategy_compiler import parse_instruction, save_strategy, run_in_sandbox

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Speak your strategy idea:")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"🗣 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand")
        return None

if __name__ == "__main__":
    idea = listen()
    if idea:
        name = "voice_" + str(abs(hash(idea)))[:6]
        code = parse_instruction(idea)
        save_strategy(code, name)
        run_in_sandbox(name)
    