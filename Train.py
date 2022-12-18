import numpy as Numpy
import json
import torch
import torch.nn as NN
from torch.utils.data import Dataset,DataLoader
from NeuralNetworks import BagOfWords,Tokenize,Stem
from Brain import NeuralNetwork

with open('Intents.json','r',encoding="utf8") as File:
    Intents=json.load(File)

AllWords=[]
Tags=[]
Combinations=[]

for Intent in Intents['intents']:
    Tag=Intent['tag']
    Tags.append(Tag)

    for Pattern in Intent['patterns']:
        Token=Tokenize(Pattern)
        AllWords.extend(Token)
        Combinations.append((Token,Tag))

IgnoreWords=[',','?','.','!']

AllWords=[Stem(W) for W in AllWords if W not in IgnoreWords]
AllWords=sorted(set(AllWords))
Tags=sorted(set(Tags))

XTrain=[]
YTrain=[]

for (PaternSentence,Tag) in Combinations:
    Bag=BagOfWords(PaternSentence,AllWords)
    XTrain.append(Bag)

    Label=Tags.index(Tag)
    YTrain.append(Label)

[[0,1,2,3],[3.4,5,6]]

XTrain=Numpy.array(XTrain)
YTrain=Numpy.array(YTrain)

NumEpoch=1000
BatchSize=8
LearningRate=0.001
InputSize=len(XTrain[0])
HiddenSize=8
OutputSize=len(Tags)

print("Training The Model ...");

class ChatDataset(Dataset):
    def __init__(self):
        self.NSamples=len(XTrain)
        self.XData=XTrain
        self.YData=YTrain
    def __getitem__(self,index):
        return self.XData[index],self.YData[index]
    def __len__(self):
        return self.NSamples

Dataset=ChatDataset()
TraonLoader=DataLoader(dataset=Dataset,batch_size=BatchSize,shuffle=True,num_workers=0)
Device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
Model=NeuralNetwork(InputSize,HiddenSize,OutputSize).to(device=Device)
Criterion=NN.CrossEntropyLoss()
Optimizer=torch.optim.Adam(Model.parameters(),lr=LearningRate)

for Epoch in range(NumEpoch):
    for (Words,Labels) in TraonLoader:
        Words=Words.to(Device)
        Labels=Labels.to(dtype=torch.long).to(Device)
        Outputs=Model(Words)
        Loss=Criterion(Outputs,Labels)
        Optimizer.zero_grad()
        Loss.backward()
        Optimizer.step()
    if(Epoch+1)%100==0:
        print(f"Epoch: [{Epoch+1}/{NumEpoch}] , Loss: {Loss.item():.4f}")
print(f"Final Loss: {Loss.item():.4f}")

Data={
    "ModelState":Model.state_dict(),
    "InputSize":InputSize,
    "OutputSize":OutputSize,
    "HiddenSize":HiddenSize,
    "AllWords":AllWords,
    "Tags":Tags
}

File="DataTrain.pth"
torch.save(Data,File)
print("Training Complete and File Saved")