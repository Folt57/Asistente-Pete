import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

name = 'Pete'
musicQuestion = 'reproduce'
musicAnswer = 'Reproduciendo '
timeQuestion = 'hora'
timeAnswer = 'Son las '
exitQuestion = 'Salir'
exitAnswer = 'Saliendo'
unknownQuestion = 'No te he entendido'

flag = 1

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', 0)
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    flag = 1
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()

            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                talk(unknownQuestion + rec)
    except:
        pass
    return flag


def run(rec):
    if musicQuestion in rec:
        music = rec.replace(musicQuestion, '')
        talk(musicAnswer + music)
        pywhatkit.playonyt(music)

    elif timeQuestion in rec:
        hora = datetime.datetime.now().strftime('%H:%M')
        talk(timeAnswer + hora)

    elif exitQuestion in rec:
        flag = 0
        talk(exitAnswer)

    else:
        talk(unknownQuestion + rec)

    return flag


while flag:
    flag = listen()
