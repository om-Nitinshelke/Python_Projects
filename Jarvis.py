import speech_recognition as sr
import pyttsx3 as ts
import webbrowser

r = sr.Recognizer()

def speak(t):
    engine = ts.init()
    engine.say(t)
    engine.runAndWait()
    engine.stop()

while True:
    with sr.Microphone() as source:
        print("Talk")
        print("Say Something")
        audio = r.listen(source)
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

            if text == "exit now":
                break

        except:
            print("Sorry I did not get it")
            speak("Sorry, I did not get it")

speak("Thanks for using this program")