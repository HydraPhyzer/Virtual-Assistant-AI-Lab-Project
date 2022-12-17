import random
import json
import torch
from Brain import NeuralNetwork
from NeuralNetworks import BagOfWords,Tokenize
import Features


Device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('Intents.json','r',encoding='utf8') as JSONData:
    Intents=json.load(JSONData)

Data=torch.load('DataTrain.pth')

ModelState=Data['ModelState']
InputSize=Data['InputSize']
OutputSize=Data['OutputSize']
HiddenSize=Data['HiddenSize']
AllWords=Data['AllWords']
Tags=Data['Tags']

Model=NeuralNetwork(InputSize,HiddenSize,OutputSize).to(Device)
Model.load_state_dict(ModelState)
Model.eval()

from Listen import Listen
from Speak import Speak
def Main():
    Sentence=Listen("Listening")
    Original=Sentence
    print(Sentence)
    Sentence=Tokenize(Sentence)
    X=BagOfWords(Sentence,AllWords)
    X=X.reshape(1,X.shape[0])
    X=torch.from_numpy(X).to(Device)

    Output=Model(X)

    _,Predicted=torch.max(Output,dim=1)
    Tag=Tags[Predicted.item()]
    Probs=torch.softmax(Output,dim=1)
    Prob=Probs[0][Predicted.item()]

    if Prob.item()>0.75:
        for Intent in Intents['intents']:
            if Tag==Intent['tag']:
                Reply=random.choice(Intent['responses'])

                if Reply=="youtubesearch":
                    Tokenized = Original.replace("youtube search", "")
                    Features.YoutubeSearch(Tokenized)
                elif Reply=="googlesearch":
                    Tokenized = Original.replace("google search", "")
                    Features.GoogleSearch(Tokenized)
                elif Reply=="download" :
                    Features.DownloadVideo();
                elif Reply=="testinternetspeed":
                    Features.SpeedTest();
                elif Reply=="whatsappmessage":
                    Speak("Tell The Recipient Name");
                    Name=Listen("Recording");
                    print(f"--> User Name Is : {Name}")
                    Speak("Record Your Message")
                    Message=Listen("Recording");
                    print(f"--> Message Is : {Message}")
                    Features.WhatsappMessage(Name,Message)
                elif Reply=="open":
                    Tokenized=Original.replace("open","");
                    Features.RunProgramme(Tokenized)
                elif Reply=="respond":
                    Speak(Reply)
                elif Reply=="calculate":
                    Tokenized = Original.replace("calculate", "")
                    Tokenized=Tokenized.replace("divided by","/")
                    Tokenized=Tokenized.replace("divide","/")
                    Tokenized=Tokenized.replace("x","*")

                    NewExp = "".join(i for i in Tokenized if i in "0123456789+*/-()")

                    Features.Calculator(NewExp)
                elif Reply=="show" :
                # Tokenize=Results.replace("show window","");
                    Tokenized=Original.split();
                    Features.ShowWindow(Tokenized[-1])
                elif Reply=="close":
                    Features.CloseWindow()
                elif Reply=="minimize":
                    Features.MinimizeWindow()
                elif Reply=="maximize":
                    Features.MaximizeWindow()

                # ==============Volume Control=================
                elif Reply=="mute" :
                    Features.MuteAudio()
                elif Reply=="increase":
                    Features.IncreaseAudio(Original)
                elif Reply=="decrease":
                    Features.DecreaseAudio(Original)
                # ==============Wi-Fi Control=================
                elif Reply=="onwifi":
                    Features.TurnOnWiFi()
                elif Reply=="offwifi":
                    Features.TurnOffWiFi()
                # ==============Jokes API=================
                elif Reply=="joke"  :
                    Features.TellJoke()
                # ===========Functionalities==============
                elif Reply=="screenshot":
                    Features.ScreenShot()
                elif Reply=="time" :
                    Features.CurrentTime()
                elif Reply=="note":
                    Speak("Record Your Note, Go Ahead");
                    Note = Listen("Recording")
                    Features.WriteNote(Note)
                elif Reply=="weather":
                    Features.Weather()
                else:
                    Speak(Reply)
    else:
        Speak("Pardon, Currently, I Don't Know The Answer to This Question. I May occasionally generate incorrect information, Because, I Have Limited Knowledge of World. I am Under Trainig")

while True:
    Main()