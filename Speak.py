# Import Packages
import pyttsx3
import speech_recognition as sr
# =============================================

# Changing Assistant Sound to Female
Engine = pyttsx3.init()
Voices = Engine.getProperty("voices")
Engine.setProperty("voice", Voices[1].id)
Engine.setProperty('rate',170)

# Speak Function For Command

def Speak(Command):
    Engine.say(Command)
    Engine.runAndWait()

# Speak("Hello World");