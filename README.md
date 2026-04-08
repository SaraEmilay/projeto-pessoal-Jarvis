<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Jarvis - README</title>
</head>
<body>

<h1>Jarvis</h1>
<p>Um assistente virtual em Python com reconhecimento de voz em português, integrado a IA para responder perguntas, abrir aplicativos e realizar ações no sistema.</p>

<hr>

<h2>💻 Como usar</h2>

<h3>1. Clonar o repositório</h3>
<pre><code>git clone https://github.com/seu-usuario/jarvis-app.git
cd jarvis-app
</code></pre>

<h3>2. Instalar dependências</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>3. Baixar o modelo do Vosk (necessário para reconhecimento de voz)</h3>
<ul>
    <li>Vosk PT-BR pequeno: <a href="https://alphacephei.com/vosk/models" target="_blank">https://alphacephei.com/vosk/models</a></li>
    <li>Extraia o conteúdo para a pasta: <code>models/vosk-model-small-pt-0.3/</code></li>
</ul>

<h3>4. Rodar o app</h3>
<pre><code>streamlit run app.py</code></pre>

<hr>

<h2>⚡ Automatizar o download do modelo (opcional)</h2>

<p>Você pode criar um script Python chamado <code>setup.py</code>:</p>

<pre><code>import os
import urllib.request
import zipfile

url = "https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip"
output_path = "models/vosk-model-small-pt-0.3.zip"
extract_path = "models/"

os.makedirs(extract_path, exist_ok=True)

print("Baixando modelo do Vosk...")
urllib.request.urlretrieve(url, output_path)

print("Extraindo...")
with zipfile.ZipFile(output_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

os.remove(output_path)
print("Modelo pronto em models/vosk-model-small-pt-0.3")</code></pre>

<p>Rodar:</p>
<pre><code>python setup.py</code></pre>

<p>Depois:</p>
<pre><code>streamlit run app.py</code></pre>

<hr>

<h2>🗂 Estrutura do projeto</h2>

<pre><code>projeto-jarvis/
│
├─ app.py
├─ main.py
├─ requirements.txt
├─ setup.py
├─ README.md
│
├─ core/
│  ├─ assistant.py
│  └─ brain.py
│
├─ features/
│  ├─ open_apps.py
│  ├─ system_info.py
│  └─ web.py
│
├─ models/
│  └─ vosk-model-small-pt-0.3/  # baixado via setup.py
│
├─ voice/
│  ├─ listen.py
│  └─ speak.py
│
└─ utils/
   └─ helpers.py</code></pre>

<hr>

<h2>🚀 Funcionalidades</h2>
<ul>
    <li>Reconhecimento de voz em português (Vosk)</li>
    <li>Respostas inteligentes via IA (módulo <code>brain.py</code>)</li>
    <li>Abrir aplicativos e acessar informações do sistema</li>
    <li>Acesso rápido a funcionalidades web</li>
    <li>Interface simples com Streamlit</li>
</ul>

</body>
</html>
