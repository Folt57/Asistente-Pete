import datetime

import speech_recognition as sr
import pyttsx3
import pywhatkit

name = 'Pete'
musicQuestion = 'reproduce'
musicAnswer = 'Reproduciendo '
timeQuestion = 'hora'
timeAnswer = 'Son las '


listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec


def run():
    rec = listen()
    if musicQuestion in rec:
        music = rec.replace(musicQuestion, '')
        talk(musicAnswer + music)
        pywhatkit.playonyt(music)

    elif timeQuestion in rec:
        hora = datetime.datetime.now().strftime('%H:%M')
        talk(timeAnswer + hora)


run()
