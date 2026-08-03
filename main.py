import speech_recognition as sr
import pyttsx3 as ts
import webbrowser
from datetime import datetime
import wikipedia
from game import play_game
import os
import time
from speech_recognition import UnknownValueError
import smtplib
from email.message import EmailMessage
import mimetypes


r = sr.Recognizer()
r.pause_threshold = 1.5

sender = os.getenv("JARVIS_EMAIL_SENDER")
password = os.getenv("JARVIS_EMAIL_APP_PASSWORD")

if not sender or not password:
    raise ValueError("Email credentials are missing from environment variables")

def send_email(receiver, message):

    msg = EmailMessage()
    msg["Subject"] = "Message from Jarvis"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content(message)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        return True

    except Exception as e:
        print("Email sending error:", e)
        return False


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

def find_and_send_file_via_gmail(search_path, file_name, gmail_sender,
                                 gmail_app_password,
                                 gmail_receiver):
    found_file = None
    file_name = file_name.lower().strip()

    for root, dirs, files in os.walk(search_path):
        for actual_file in files:
            actual_file_lower = actual_file.lower()

            # Match full name OR name without extension
            actual_name_without_ext = os.path.splitext(actual_file_lower)[0]

            if actual_file_lower == file_name or actual_name_without_ext == file_name:
                found_file = os.path.join(root, actual_file)
                break

        if found_file:
            break

    if not found_file:
        return 0

    msg = EmailMessage()
    msg["Subject"] = "File found and attached"
    msg["From"] = gmail_sender
    msg["To"] = gmail_receiver
    msg.set_content("Hello,\n\nThe file you requested has been found and attached below.\n")

    mime_type, _ = mimetypes.guess_type(found_file)

    if mime_type:
        maintype, subtype = mime_type.split("/", 1)
    else:
        maintype, subtype = "application", "octet-stream"

    try:
        with open(found_file, "rb") as f:
            file_data = f.read()

        msg.add_attachment(
            file_data,
            maintype=maintype,
            subtype=subtype,
            filename=os.path.basename(found_file)
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(gmail_sender, gmail_app_password)
            smtp.send_message(msg)

        return True

    except Exception as e:
        print("File sending error:", e)
        return False

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

            elif "exit now" in text:
                break

            elif "geeks for geeks" in text:
                speak("Opening Geeks for Geeks")
                webbrowser.open("https://www.geeksforgeeks.org")
                time.sleep(2)
                continue

            elif "youtube" in text:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
                time.sleep(2)
                continue

            elif "github" in text:
                speak("Opening GitHub")
                webbrowser.open("https://github.com")
                time.sleep(2)
                continue


            elif "file" in text:
                speak("Tell me the name of your file you want to send")
                file_name=take_command(source).lower()
                speak("Can you give me the email of the receiver")
                address=input("Enter the email:")
                result=find_and_send_file_via_gmail(r"C:\Users\omshelke\Desktop\Om Shelke",file_name,
                                                    sender,password,address)

                if result==0:
                    speak("The file is not present")

                elif result==True:
                    speak("You're file is successfully sent to the destination")
                else:
                    speak("Some error comes during file sending")


            elif "chatgpt" in text:
                speak("Opening ChatGPT")
                webbrowser.open("https://chatgpt.com")
                time.sleep(2)
                continue

            elif "search" in text:
                speak("Tell me what you want to search on Wikipedia")
                query = take_command(source)
                if query:
                    wiki(query)

            elif "email" in text:
                speak("what is the email ID of the person you want to send the email to?")
                destination = input("Email ID:").strip()

                speak("give me the message:")
                message = take_command(source)

                if not message:
                    speak("I could not hear the message")
                    continue

                result = send_email(destination, message)

                if result:
                    speak("Your email is sent successfully")
                else:
                    speak("Some error occurred while sending the email")


            elif "play" in text:
                play_game(source,take_command,speak)

        except sr.UnknownValueError:
            pass
        except sr.WaitTimeoutError:
            pass

speak("Thanks for using me")

