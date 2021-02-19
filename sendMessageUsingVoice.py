# pip install pywhatkit
# pip install pyttsx3
# pip install SpeechRecognition


import pywhatkit
import datetime
import pyttsx3
import speech_recognition as rec

listener = rec.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text: str):
    engine.say(text)
    engine.runAndWait()


def hearYou(time=3):
    with rec.Microphone() as source:
        voice = listener.record(source, time)
        command = listener.recognize_google(voice)
        low = command.lower()
    return low


talk("Whom to Send")
friend = hearYou()

talk("What is the message")
message = hearYou(10)

hour = datetime.datetime.now().strftime('%H')
minute = datetime.datetime.now().strftime('%M')

talk(f"Sending message to {friend}")

# This is you contact dictionary. Add as many contacts as you want
mobile = {'contact1': '+91XXYYXXYYXX',
          'contact2': '+91XYXYXYXYXY'}

if mobile[friend] is None:
    talk('Sorry No Contact Found')

try:
    pywhatkit.sendwhatmsg(mobile[friend], message,
                          int(hour), int(minute) + 1, 10, True)

except:
    pass
