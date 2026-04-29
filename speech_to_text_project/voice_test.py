import numpy as np
import sounddevice as sd
import wave
from faster_whisper import WhisperModel

fs = 16000
seconds = 3
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


print("Loading Whisper model...")

model = WhisperModel("medium")

segments, _ = model.transcribe("input.wav", language="en")

print("You said:")

for segment in segments:
    print(segment.text)