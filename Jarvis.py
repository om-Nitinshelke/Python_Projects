import speech_recognition as sr
import pyttsx3 as ts
import webbrowser
from datetime import datetime
import wikipedia
import random
import os
import time
from speech_recognition import UnknownValueError


r = sr.Recognizer()
r.pause_threshold = 1.5


def speak(t):
    engine=ts.init()
    engine.setProperty('rate',150)
    engine.say(t)
    engine.runAndWait()
    engine.stop()

def take_command(source):
    try:
        audio_for_task = r.listen(source, phrase_time_limit=7)
        text_for_task = r.recognize_google(audio_for_task).lower()
        return text_for_task
    except UnknownValueError:
        return ""

def search_file(file_name, path):
    for root, directory, files in os.walk(path):
        if file_name in files:
            print("File is present")
            return os.path.join(root, file_name)

    print("File is not present")
    return None

def wiki(query):
    try:
        info = wikipedia.summary(query, sentences=5)
        print(info)
        speak(info)

    except wikipedia.exceptions.DisambiguationError:
        speak("Your query has multiple meanings. Please be more specific.")

    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find anything on that topic.")

    except wikipedia.exceptions.HTTPTimeoutError:
        speak("Internet issue. Try again later")

    except Exception as e:
        print(e)
        speak("Something went wrong while searching Wikipedia.")

def game():
    speak("Choose between rock paper or scissor. Say stop game to exit")

    while True:
        user = take_command(source)
        if not user:
            continue

        jarvis = random.choice(["rock", "paper", "scissor"])

        if "stop" in user:
            speak("Exiting the game")
            break

        if user == jarvis:
            speak("This round is a draw")
        elif ("rock" in user and jarvis == "paper") or \
             ("paper" in user and jarvis == "scissor") or \
             ("scissor" in user and jarvis == "rock"):
            speak("You lose")
        else:
            speak("You win")

    speak("Thanks for playing")


current_hour = datetime.now().hour

if 5 <= current_hour < 12:
    speak("Good Morning I am your personal assistant Jarvis")
elif 12 <= current_hour < 17:
    speak("Good Afternoon I am your personal assistant Jarvis")
elif 17 <= current_hour < 21:
    speak("Good Evening I am your personal assistant Jarvis")
else:
    speak("Good Night")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)

    while True:
        try:
            print("Listening...")
            text = take_command(source)

            if not text:
                continue

            if "exit now" in text:
                break

            if "geeks for geeks" in text:
                speak("Opening Geeks for Geeks")
                webbrowser.open("https://www.geeksforgeeks.org")
                time.sleep(2)  # FIX 3
                continue

            if "youtube" in text:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
                time.sleep(2)
                continue

            if "github" in text:
                speak("Opening GitHub")
                webbrowser.open("https://github.com")
                time.sleep(2)
                continue

            if "chatgpt" in text:
                speak("Opening ChatGPT")
                webbrowser.open("https://chatgpt.com")
                time.sleep(2)
                continue

            if "search" in text:
                speak("Tell me what you want to search on Wikipedia")
                query = take_command(source)
                if query:
                    wiki(query)

            if "play" in text:
                game()

        except sr.UnknownValueError:
            pass
        except sr.WaitTimeoutError:
            pass

speak("Thanks for using me")

