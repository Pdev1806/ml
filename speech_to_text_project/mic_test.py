import sounddevice as sd

fs = 16000
seconds = 5

print("Speak now...")

audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

print("Recording finished")