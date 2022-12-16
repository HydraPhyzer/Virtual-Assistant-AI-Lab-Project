# Import Packages
import speech_recognition as sr

def Listen(Message):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("=============================")
        print(f"Say Something! ({Message}) 🎤")
        print("=============================")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        Query = r.recognize_google(audio)
        # print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        return Query.lower()
    except:
        return ""

# Listen("Listening");
