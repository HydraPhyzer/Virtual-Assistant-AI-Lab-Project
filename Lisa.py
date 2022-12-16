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
                    
                else:
                    Speak(Reply)
while True:
    Main()