import torch.nn as NN ## NN is NeuralNetwork Short Form

class NeuralNetwork(NN.Module):
    def __init__(self,InputSize,HiddenSize,NumClasses) -> None:
        super(NeuralNetwork,self).__init__()

        self.L1=NN.Linear(InputSize,HiddenSize)
        self.L2=NN.Linear(HiddenSize,HiddenSize)
        self.L3=NN.Linear(HiddenSize,NumClasses)

        self.Relu=NN.ReLU()


    def forward(self,X):

        Out=self.L1(X)
        Out=self.Relu(Out)

        Out=self.L2(Out)
        Out=self.Relu(Out)

        Out=self.L3(Out)
        
        return Out