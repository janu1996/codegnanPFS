import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

#Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:",command)
        return command.lower()
    except Exception:
        print("Sorry,please say that again.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning \n I am your  Virtual Assistant")
    elif hour < 18:
        speak("Good Afternoon \n I am your  Virtual Assistant")
    else:
        speak("Good Evening \n I am your  Virtual Assistant")
wish_user()

while True:
    command = take_command()
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
        
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in command:
        webbrowser.open("https://www.google.com/")
    elif "Who is" in command:
        persono = command.replace("Who is","")
        info = wikipedia.summary(command,2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("Goodbye")
        break
        
    
