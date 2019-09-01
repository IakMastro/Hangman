from random import *

def pickAWord():

    wordList = ["apple", "dog", "cat"]

    return wordList[randint(0, len(wordList) - 1)]

word = pickAWord()