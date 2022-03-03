import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

name = "taric"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            talk("How can i help you?")
            print("How can i help you?")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec.replace(name, "")
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if "reproduce" in rec:
        music = rec.replace("reproduce", "")
        talk("Reproduciendo" + music)
        pywhatkit.playonyt(music)
    elif "hora" in rec:
        hora = datetime.datetime.now().strftime("%I:%M %p")
        talk("La hora actual es "+hora)
    elif "busca" in rec:
        order = rec.replace("busca", "")
        info = wikipedia.summary(order, 1)
        talk(info)
    else:
        talk("I couldn't understand what you told me, try again")
run()