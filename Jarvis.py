import speech_recognition as sr
import pyttsx3 as ts

r=sr.Recognizer()
engine=ts.init()

def speak(t):
    engine.say(t)
    engine.runAndWait()

with sr.Microphone() as source:
    print("Talk")
    print("Say Something")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("You said:",text)
        speak("You said:"+text)

    except:
        print("Sorry I did not get it")
        speak("Sorry,I did not get it")
