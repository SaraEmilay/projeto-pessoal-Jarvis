import pyttsx3

engine = pyttsx3.init()

# opcional: ajustar voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # pode testar [1]

engine.setProperty('rate', 180)

def falar(texto):
    print("Jarvis:", texto)
    engine.say(texto)
    engine.runAndWait()