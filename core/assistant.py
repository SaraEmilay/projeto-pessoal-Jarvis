from voice.listen import ouvir
from voice.speak import falar
from core.brain import perguntar_ia

def run():
    print("Jarvis iniciado")

    while True:
        comando = ouvir()

        if "sair" in comando:
            falar("Encerrando")
            break

        resposta = perguntar_ia(comando)
        falar(resposta)