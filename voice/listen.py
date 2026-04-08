import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

sd.default.device = (17, None)

model = WhisperModel("base", compute_type="int8")

def ouvir(duracao=5):
    print("🎤 Fale...")

    device = 17  # seu microfone

    device_info = sd.query_devices(device, 'input')
    samplerate = int(device_info['default_samplerate'])  # 🔥 pega automático

    audio = sd.rec(int(samplerate * duracao),
                   samplerate=samplerate,
                   channels=1,
                   dtype='float32',
                   device=device)

    sd.wait()

    audio = audio.flatten()

    # 🔊 volume pra UI
    volume = float(np.abs(audio).mean())

    # 🔽 reamostra pra Whisper (IMPORTANTÍSSIMO)
    audio = audio[::int(samplerate / 16000)] if samplerate > 16000 else audio

    segments, _ = model.transcribe(audio, language="pt")

    texto = ""
    for segment in segments:
        texto += segment.text

    print("Você:", texto)

    return texto.lower(), volume