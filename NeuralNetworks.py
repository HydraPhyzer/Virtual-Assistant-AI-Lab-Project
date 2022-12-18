import numpy as Numpy
import nltk
# nltk.download()
from nltk.stem.porter import PorterStemmer

Stemmer=PorterStemmer()

def Tokenize(Sentence):
    return nltk.word_tokenize(Sentence)

def Stem(Word):
    return Stemmer.stem(Word.lower())

def BagOfWords(TokenizedSentence,Words):
    SentenceWord=[Stem(Word) for Word in TokenizedSentence]

    Bag=Numpy.zeros(len(Words),dtype=Numpy.float32)

    for IDX,W in enumerate(Words):
        if W in SentenceWord:
            Bag[IDX]=1

    return Bag
