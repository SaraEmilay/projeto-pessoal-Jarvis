import requests

def perguntar_ia(pergunta):
    try:
        resposta = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"Você é um assistente chamado Jarvis. Responda em português: {pergunta}",
                "stream": False
            }
        )
        return resposta.json()["response"]
    except:
        return "Erro ao falar com a IA"