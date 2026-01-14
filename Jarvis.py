import speech_recognition as sr
import pyttsx3 as ts
import webbrowser
from datetime import datetime
import wikipedia
import random
import os


r = sr.Recognizer()
r.pause_threshold=1.5



def search_file(file_name,path):
    for root,directory,files in os.walk(path):
        if file_name in files:
            print("File is present")
            return os.path.join(root,file_name)

    print("File is not present")
    return None

def speak(t):
    engine=ts.init()
    engine.setProperty('rate',150)
    engine.say(t)
    engine.runAndWait()
    engine.stop()

def wiki(query):
    try:
        info = wikipedia.summary(query, sentences=5)
        print(info)
        speak(info)

    except wikipedia.exceptions.DisambiguationError as e:
        print("Your query has multiple meanings. Please be more specific.")
        speak("Your query has multiple meanings. Please be more specific.")

    except wikipedia.exceptions.PageError:
        print("Sorry, I couldn't find anything on that topic.")
        speak("Sorry, I couldn't find anything on that topic.")

    except wikipedia.exceptions.HTTPTimeoutError:
        print("Internet issue. Try again later")
        speak("Internet issue. Try again later")

    except Exception as e:
        print(e)
        speak("Something went wrong while searching Wikipedia.")

    print("Do you want to search something else now If not you can say no")
    speak("Do you want to search something else now If not you can say no")
    audio3 = r.listen(source, phrase_time_limit=5)
    message = r.recognize_google(audio3).lower()
    if "search" in message:
        print("Tell me the next title for searching")
        speak("Tell me the next title for searching")
        audio4 = r.listen(source, phrase_time_limit=5)
        message1 = r.recognize_google(audio4).lower()
        wiki(message1)
    if "no" in message:
        print("Tell me something more I can do for you")
        speak("Tell me something more I can do for you")

def game():
    print("I will ask you about your choice so choose between rock,paper and scissors and if you want to stop the game you can say stop the game")
    speak("I will ask you about your choice so choose between rock,paper and scissors and if you want to stop the game you can say stop the game")
    while True:
        print("Your choice:")
        speak("Your choice")
        choose=r.listen(source,phrase_time_limit=5)
        user=r.recognize_google(choose).lower()
        jarvis=random.choice(["rock","paper","scissor"])
        print("Your choice is:" + user)
        speak("Your choice is:"+user)
        if "stop" in user:
            print("Exiting the game")
            speak("Exiting the game")
            break
        print("My choice is:"+jarvis)
        speak("My choice is:"+jarvis)

        if user==jarvis:
            print("This round is a draw")
            speak("This round is a draw")
            continue
        elif "rock" in user and "paper" in jarvis:
            print("You lose")
            speak("You lose")
            continue
        elif "paper" in user and "scissor" in jarvis:
            print("You lose")
            speak("You lose")
            continue
        elif "scissor" in user and "rock" in jarvis:
            print("You lose")
            speak("You lose")
            continue
        else:
            print("You Win")
            speak("You Win")
            continue

    print("thanks for playing")
    speak("thanks for playing")




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

                if "send" in text:
                    print("Which file do you want to send")
                    speak("Which file do you want to send")
                    audio_for_File=r.listen(source,phrase_time_limit=5)
                    text_for_File=r.recognize_google(audio_for_File).lower()
                    print("You said:",text_for_File)
                    speak("You said:"+text_for_File)
                    details=text_for_File.split()
                    speak("Enter the email id of person whom you want to send this file")
                    Receiver=input("Enter the email id:")
                    print("File Name:",details[-1],"To:",Receiver)
                    file_path=search_file(details[-1],r"C:\Users\omshelke\Desktop\Om Shelke")
                    print(file_path)
                    continue

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

                if "search" in text:
                    speak("Tell me what to search on Wikipedia")
                    audio2 = r.listen(source, phrase_time_limit=5)
                    title = r.recognize_google(audio2).lower()
                    wiki(title)

                if "play" in text:
                    print("Sure let's play rock paper and scissors game")
                    game()


                if "exit now" in text:
                    break

            except sr.UnknownValueError:
                pass
            except sr.WaitTimeoutError:
                pass



speak("Thanks for using me")
