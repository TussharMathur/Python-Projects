import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import os
from subprocess import call
import calendar


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am tushi. How may i help you")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Can you please say that again")
        return "None"
    return query
year = 2021
month = 8
cal = calendar.month(year, month)




wishme()
while True:
#if 1:
    query = take_command().lower()
    if 'wikipedia' in query:
        speak('Searching wikipedia..please wait')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, 2)
        speak("according to wikipedia..")
        print(results)
        speak(results)
    elif 'play' in query:
        song= query.replace('play','')
        speak('OK PLAYING..'+ song+'On Youtube')
        pywhatkit.playonyt(song)

    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I %M %p')
        speak('Current time is'+ time)

    elif 'how are you' in query:
        speak('I am fine what about you')

    elif 'joke' in query:
        speak(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif 'google' in query:
        speak("opening google..")
        webbrowser.open("google.com")

    elif 'amazon music' in query:
        speak("Ok..opening amazon music")
        path = "C:\\Users\\TUSSHAR MATHUR\\AppData\\Local\\Amazon Music\\Amazon Music.exe"
        os.startfile(path)

    elif 'calculator' in query:
        call(["calc.exe"])

    elif 'exit' in query:
        speak("ok bye..Have a nice day")
        exit()

    elif 'who is tushar' in query:
        speak("he is smart,intelligent and a cool boy ")

    elif 'calendar' in query:
        speak("Ok..opening calendar")
        print(cal)


