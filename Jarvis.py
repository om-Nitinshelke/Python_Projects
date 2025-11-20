import speech_recognition as sr
import pyttsx3 as ts
import webbrowser
from datetime import datetime

r = sr.Recognizer()



def speak(t):
    engine = ts.init()
    engine.setProperty('rate',150)
    engine.say(t)
    engine.runAndWait()
    engine.stop()

current_hour =datetime.now().hour

if 5<=current_hour<=12:
    speak("Good Morning  I am your personal assistant jarvis  what can I do for you")
elif 12<=current_hour<=17:
    speak("Good Afternoon  I am your personal assistant jarvis what can I do for you")
elif 17<=current_hour<=21:
    speak("Good Evening I am your personal assistant jarvis what can I do for you")
else:
    speak("Good Night")


while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Talk")
        print("Say Something")
        audio = r.listen(source,phrase_time_limit=20)
        try:
            text = r.recognize_google(audio).lower()
            print("You said:", text)
            speak("You said: " + text)

            if text == "open geeks for geeks website":
                webbrowser.open("https://www.geeksforgeeks.org")
                continue

            if text == "open youtube":
                webbrowser.open_new("https://www.youtube.com/")
                continue

            if text == "open my github account":
                webbrowser.open_new("https://github.com/")
                continue

            if text=="open chatgpt":
                webbrowser.open_new("https://chatgpt.com/")
                continue

            if text == "exit now":
                break

        except:
            print("Sorry I did not get it")
            speak("Sorry, I did not get it")

speak("Thanks for using this program")