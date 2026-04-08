from datetime import datetime

def horas():
    return datetime.now().strftime("Agora são %H:%M")