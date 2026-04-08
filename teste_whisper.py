import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

sd.default.device = (17, None)

model = WhisperModel("base", compute_type="int8")

print("🎤 Fale por 5 segundos...")

samplerate = 48000
duration = 5

audio = sd.rec(int(samplerate * duration),
               samplerate=samplerate,
               channels=1,
               dtype='float32')

sd.wait()

audio = audio.flatten()

# 🔄 CONVERTE 48000 → 16000
audio = audio[::3]

segments, _ = model.transcribe(audio, language="pt")

for segment in segments:
    print("Você disse:", segment.text)