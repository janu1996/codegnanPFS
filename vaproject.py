'''
gTTs -->Google text to Speech
playsound -->only works with python version 11 and 12
playsound --> pip install playsound==1.2.2
pyaudio -->pip install pyaudio
support file for this moudle is pyauido

3 functions we will do
1)Listen (SPeechRecognitions)
2)respond (gTTs)
3)Assistant (Conditions) -->Conversation,Greeting,datetime,
locate a place,open a browser,playa youtube Viedo

from gtts import gTTS
import playsound
text = gTTS("Hello guy's,how are you doing?")
#text.save("audio.mp3")
playsound.playsound("audio.mp3")
'''
#Import the libraries
from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os


# let us create a listen function
def listen():
    """Function for Speech Recogntion"""
    r = sr.Recognizer()
    #we will take microphone as source
    with sr.Microphone() as source:
        print("Ika modaladadammaaaa...")
        audio = r.listen(source,phrase_time_limit = 5) # 10 stands for 10 sec
    #we need to give our text as voice
    data = ""
    #here we will give exceptions(try,except)
    try:
        data = r.recognize_google(audio,language="en-US")
        print("You said:",data)
    except sr.UnknownValueError as e:
        print("Request Failed")
    except sr.RequestError as e:
        print("Speak clearly request is failing")
    return data
        #tts = gTTS(data)
        #tts.save("new.mp3")
        #playsound.playsound("new.mp3")
#listen()   

def respond(String):
    """Function to respond back"""
    print(String)
    tts = gTTS(String)
    tts.save("Speech.mp3")
    # we are using uuid to randamize the content in the audio file
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#here we will make our virtual assitant into action
def va(data):
    """Our Virtual Assistance with the actions"""
    if "hello how are you" in data:
        listening = True
        respond("I am fine! Thanks for asking")
    elif "what are your plans" in data:
        listening = True
        respond("Only Study..one focus in 2026")
    elif "vizag locations" in data:
        listening = True
        respond("Rk.Beach,kaialsagiri,simhachalam,vudapark,yendada,Rushilonda")
    elif "how things going" in data:
        listening = True
        respond("Anthaa okay ika nene set avali")
    elif "time" in data:
        listening = True
        respond(time.ctime())
    elif "stop talking" in data:
        listening = False
        respond("Okay cool...koapdakuu byee prnds")
    try:
        return listening
    except UnboundLocalError as e:
        print("Make sure to speak louder and faster")
respond("Hey Jaan....Good to hear from you.How are you?")
listening = True
while listening:
    data = listen()
    listening = va(data)
