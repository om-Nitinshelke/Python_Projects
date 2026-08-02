import random


def play_game(source, take_command, speak):
    speak("Choose between rock paper or scissor. Say stop game to exit")

    user_points = 0
    jarvis_points = 0

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
            jarvis_points += 1

        elif "rock" in user or "paper" in user or "scissor" in user:
            speak("You win")
            user_points += 1

        else:
            speak("Please choose rock, paper, or scissor")

    print("Your score is:", user_points)
    print("My score is:", jarvis_points)

    if user_points > jarvis_points:
        speak("Congratulations, you have won")
    elif user_points < jarvis_points:
        speak("I won")
    else:
        speak("This match is draw")

    speak("Thanks for playing")


