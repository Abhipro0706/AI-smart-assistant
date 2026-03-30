import pyttsx3
import speech_recognition as sr
import datetime
import setuptools
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')

try:
    engine = pyttsx3.init('sapi5')
except Exception as e:
    print(f"Driver error: {e}. Falling back to default.")
    engine = pyttsx3.init()

engine.say("Testing speakers")
engine.runAndWait()

voices = engine.getProperty('voices')
if len(voices) > 0:

    engine.setProperty('voices', voices[0].id)

def speak(audio):
    print(f"JARVIS: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening") 

    speak("I am your assistant. How can I help you today?")

def takeCommand():

    r = sr.Recognizer()


    with sr.Microphone() as source:
        print("Listening...")

        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

        print(f"User said: {query}\n")

    except Exception as e:

        print("Could not understand audio")
        return "None"

    return query

if __name__ == "__main__":
    
    speak("Initializing JARVIS...") 
    
    
    wishMe()

    
    while True:

        query = takeCommand()

        
        if query == "None":
            continue

        query = query.lower()

        
        if 'wikipedia' in query:

            speak('Searching Wikipedia...')

            query = query.replace("wikipedia", "")

            
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            except:
                speak("Sorry, I couldn't find information on that.")


        elif 'open youtube' in query:

            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:

            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        

        elif 'stop' in query or 'exit' in query:
            speak("Goodbye! Have a great day.")
            break