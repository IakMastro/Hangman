from random import *

def pickAWord():

    wordList = []
    file = open("words.txt", 'r')

    for word in file:

        wordList.append(word)

    return wordList[randint(0, len(wordList) - 1)]

word = pickAWord()
print(word)