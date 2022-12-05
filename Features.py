## Import Packages

import pyttsx3 ## Python Text to Speech
import webbrowser ##For Open Web Pages
import wikipedia ## For Getting Summary From Wikipedia While Google Search
from pytube import YouTube ## For Downloading Videos from Youtube
from time import sleep ## For Sleep Program
import pyperclip ## For Copy Paste
import os ## For OS System Calls
# =============================================

## Changing Assistant Sound to Female
Engine = pyttsx3.init()
Voices=Engine.getProperty("voices");
Engine.setProperty("voice",Voices[1].id);
Engine.setProperty('rate',170)

## Speak Function For Command
def Speak(Command):
    Engine.say(Command);
    Engine.runAndWait();

def YoutubeSearch(Query):
    Result="https://www.youtube.com/results?search_query="+Query;
    webbrowser.open(Result);
    Speak("Showing Results I Found on Youtube");

# YoutubeSearch("ARY News");
def GoogleSearch(Query):
    Res="https://www.google.com/search?q="+Query
    webbrowser.open(Res)
    Search=wikipedia.summary(Query,2);
    Speak(Search)

# GoogleSearch("Hello World");
def DownloadVideo():

    sleep(5)
    Value=pyperclip.paste()
    Link=str(Value);

    def Download(Link):
        try:
            URL=YouTube(Link);
            Speak("Initiating The Download");
            print("Initiating The Download : ",Link)
            Video=URL.streams.filter(res="720p").first();
            Video.download('C:\\Users\\Zubair Gujjar\\Downloads\\Video')
            Speak("Video Has Been Downloaded and Saved to Video Folder in Downlods Folder");
            os.startfile('C:\\Users\\Zubair Gujjar\\Downloads\\Video');
        except:
            Speak("Error Occoured, Youtube Video URL or May Be a Network Issue");
    Download(Link);

# DownloadVideo();