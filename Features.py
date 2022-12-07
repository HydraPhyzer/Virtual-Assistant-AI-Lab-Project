## Import Packages

import pyttsx3 ## Python Text to Speech
import webbrowser ##For Open Web Pages
import wikipedia ## For Getting Summary From Wikipedia While Google Search
from pytube import YouTube ## For Downloading Videos from Youtube
from time import sleep ## For Sleep Program
import pyperclip ## For Copy Paste
import os ## For OS System Calls
import speedtest ## For Checking Internet Speed
import math
import webbrowser
import pyautogui
from time import sleep
import keyboard
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

def SpeedTest():
    try:
        Speak("Please Hold On, Checking Internet Speed")
        Speed = speedtest.Speedtest()

        DownloadSpeed =  Speed.download()/1024/1024
        String ="Your Download Speed Is : "+"{:.2f}".format(DownloadSpeed)+ "MB";
        print(String)
        Speak(String);

        UploadSpeed = Speed.upload()/1024/1024
        String ="Your Upload Speed Is   : "+"{:.2f}".format(UploadSpeed)+ "MB";
        print(String)
        Speak(String);
    except:
        Speak("Time Out, Please Try Again");
# SpeedTest()

def Calculator(Exp):
    print(Exp)
    try:
        Ans=eval(Exp)
        print(f"Answer of Expression '{Exp}' is = {Ans}")
        Speak(f"Answer of {Exp} is {Ans}")
    except:
        Speak("Expression Error, Your Expression is Faulty")
# Calculator("3 * 2")

def WhatsappMessage(Name,Message):
    try :
        webbrowser.open("https://web.whatsapp.com/")
        sleep(20)
        pyautogui.click(x=289, y=185);
        sleep(3)
        keyboard.write(Name)
        sleep(3)
        pyautogui.click(x=205, y=288)
        sleep(2)
        pyautogui.click(x=1035, y=705)
        sleep(2)
        keyboard.write(Message)
        keyboard.press("enter")
        Speak(f"Message Sent Successfully to {Name}")
    except:
        Speak("Unable to Send Message ")
# WhatsappMessage("Papa Jan","Hello World !!");