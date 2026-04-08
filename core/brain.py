import requests

def perguntar_ia(pergunta):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": pergunta,
        "stream": False
    }

    response = requests.post(url, json=data)
    resultado = response.json()

    return resultado["response"]