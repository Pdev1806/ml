import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import requests
import pyttsx3
import wave

fs = 16000
seconds = 3

print("loading Whisper model...")
model = WhisperModel("small.en")
print("\nReady")
engine = pyttsx3.init()

def rec_audio():
    print("Speak now...")
    audio = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
    sd.wait()
    print("Recording finished")
    
    audio = (audio * 32767).astype(np.int16)
    with wave.open("input.wav", "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(audio.tobytes())

def transcribe():
    segments, _ = model.transcribe("input.wav", language="en")
    text = " "
    for segment in segments:
        text += segment.text
    return text.strip()

def ask_ai(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False,
        "num_predict": 80
    }
    r = requests.post(url, json=data)
    return r.json()["response"]

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    rec_audio()

    user_text = transcribe()

    print("You said:", user_text)

    if user_text.lower() in ["exit", "quit", "stop"]:
        speak("Goodbye")
        break

    response = ask_ai(user_text)

    print("\nAssistant:", response, "\n")

    speak(response)