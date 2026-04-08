import os
import urllib.request
import zipfile

# Caminhos e URL do modelo
MODEL_DIR = "models/vosk-model-small-pt-0.3"
ZIP_PATH = "models/vosk-model-small-pt-0.3.zip"
URL = "https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip"

# Cria pasta models se não existir
os.makedirs("models", exist_ok=True)

# Verifica se o modelo já existe
if os.path.exists(MODEL_DIR):
    print(f"O modelo já está presente em '{MODEL_DIR}'. Nada a fazer.")
else:
    print("Baixando modelo do Vosk...")
    urllib.request.urlretrieve(URL, ZIP_PATH)
    print("Extraindo...")
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall("models/")
    os.remove(ZIP_PATH)
    print(f"Modelo pronto em '{MODEL_DIR}'")