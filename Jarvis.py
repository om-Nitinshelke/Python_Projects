import speech_recognition as sr
import pyttsx3 as ts
import webbrowser
from datetime import datetime

r = sr.Recognizer()
r.pause_threshold=0.8



def speak(t):
    engine=ts.init()
    engine.setProperty('rate',150)
    engine.say(t)
    engine.runAndWait()
    engine.stop()

current_hour =datetime.now().hour

if 5<=current_hour<12:
    speak("Good Morning  I am your personal assistant jarvis  what can I do for you")
elif 12<=current_hour<17:
    speak("Good Afternoon  I am your personal assistant jarvis what can I do for you")
elif 17<=current_hour<21:
    speak("Good Evening I am your personal assistant jarvis what can I do for you")
else:
    speak("Good Night")

with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)

        while True:
            print("Talk")
            print("Say Something")
            audio = r.listen(source,phrase_time_limit=5)
            try:
                text = r.recognize_google(audio).lower()
                print("You said:", text)
                speak("You said: " + text)

                if "open geeks for geeks" in text:
                    webbrowser.open("https://www.geeksforgeeks.org")
                    continue

                if "open youtube" in text:
                    webbrowser.open_new("https://www.youtube.com/")
                    continue

                if "open github" in text:
                    webbrowser.open_new("https://github.com/")
                    continue

                if "open chatgpt" in text:
                    webbrowser.open_new("https://chatgpt.com/")
                    continue

                if "exit now" in text:
                    speak("Thanks for using me")
                    break

            except sr.UnknownValueError:
                pass
            except sr.WaitTimeoutError:
                pass

