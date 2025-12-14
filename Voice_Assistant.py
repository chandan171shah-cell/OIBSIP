import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import subprocess

# Text to speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speed of voice

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Speech recognizer
r = sr.Recognizer()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command
    except:
        return ""

# To keep track of opened browser
opened_browser = None

while True:
    command = take_command()

    if command == "":
        continue

    # HELLO
    if "hello" in command or "hi" in command:
        speak("Hello Chandan, how can I help you?")

    # TIME
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + now)

    # DATE
    elif "date" in command or "day" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak("Today's date is " + today)

    # OPEN GOOGLE
    elif "open google" in command or "google open" in command:
        speak("Opening Google")
        opened_browser = webbrowser.open("https://www.google.com")

    # SEARCH ANYTHING
    elif "search" in command:
        speak("What should I search?")
        query = take_command()
        url = f"https://www.google.com/search?q={query}"
        speak(f"Searching for {query}")
        webbrowser.open(url)

    # CLOSE GOOGLE
    elif "close google" in command or "google close" in command:
        speak("Closing Google")
        os.system("taskkill /im chrome.exe /f")

    # OPEN YOUTUBE
    elif "open youtube" in command or "youtube open" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # PLAY MUSIC
    elif "play music" in command:
        speak("Playing music")
        webbrowser.open("https://www.youtube.com/results?search_query=radhe+krishna+song")

    # EXIT / STOP
    elif "bye" in command or "stop" in command or "exit" in command:
        speak("Goodbye Chandan, see you soon!")
        break

    # DEFAULT
    else:
        speak("Sorry, I did not understand. Please say again.")