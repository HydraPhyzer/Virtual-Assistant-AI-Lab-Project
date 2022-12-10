## Import Packages

import pyttsx3 ## Python Text to Speech
import webbrowser ##For Open Web Pages
import wikipedia ## For Getting Summary From Wikipedia While Google Search
from pytube import YouTube ## For Downloading Videos from Youtube
from time import sleep ## For Sleep Program
import pyperclip ## For Copy Paste
import os ## For OS System Calls
import speedtest ## For Checking Internet Speed
import webbrowser
import pyautogui
from time import sleep
import keyboard
import AppOpener
import keyboard
import re as Regex

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

def RunProgramme(App):
    try:
        AppOpener.run(App)
    except:
        Speak("OOPS Error Occured While Opening Programme")

# RunProgramme("weather")

def ShowWindow(Arg):
    try:
        keyboard.press_and_release(f'windows + {int(Arg)}')
    except:
        Speak("Currently Unable to Open Window")

# ShowWindow(2)

def CloseWindow():
    try:
        keyboard.press_and_release('alt+f4')
    except:
        Speak("Currently Unable to Close Window")

# CloseWindow()

def MinimizeWindow():
    try:
        keyboard.press_and_release(f'windows+m')
    except:
        Speak("Currently Unable to Minimize Window")
# MinimizeWindow()

def MaximizeWindow():
    try:
        keyboard.press_and_release(f'windows+{keyboard.KEY_UP}')
    except:
        Speak("Currently Unable to Maximize Window")
# MaximizeWindow()

def MuteAudio():
    try:
        pyautogui.press('volumemute')
    except:
        Speak("Currently Unable to Mute Audio")

# MuteAudio()

def IncreaseAudio(Text):
    try:         
        NumArray = Regex.findall(r'\d+', Text) 
        Ind=0;
        Speak("Increasing Volume")
        while Ind<int(NumArray[0]):
            pyautogui.press('volumeup')
            Ind+=1;
    except:
        Speak("Currently Unable to Mute Audio")

# IncreaseAudio()

def DecreaseAudio(Text):
    try:         
        NumArray = Regex.findall(r'\d+', Text) 
        Ind=0;
        Speak("Decreasing Volume")
        while Ind<int(NumArray[0]):
            pyautogui.press('volumedown')
            Ind+=1;
    except:
        Speak("Currently Unable to Mute Audio")

# DecreaseAudio()

def TurnOnWiFi():
    import ctypes
    commands = u'/k netsh interface set interface "Wi-Fi" enabled && exit'
    ctypes.windll.shell32.ShellExecuteW(None,u"runas",u"cmd.exe",commands,None,1)
    
# TurnOnWiFi()

def TurnOffWiFi():
    import ctypes
    commands = u'/k netsh interface set interface "Wi-Fi" disabled && exit'
    ctypes.windll.shell32.ShellExecuteW(None,u"runas",u"cmd.exe",commands,None,1)
    
# TurnOffWiFi()