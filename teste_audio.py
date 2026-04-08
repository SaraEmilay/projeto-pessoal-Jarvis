import sounddevice as sd
import numpy as np

sd.default.device = 17  # seu microfone

samplerate = 48000
duration = 5

print("🎤 Gravando...")

audio = sd.rec(int(duration * samplerate),
               samplerate=samplerate,
               channels=1,
               dtype='float32')

sd.wait()

print("🔊 Volume médio:", np.abs(audio).mean())