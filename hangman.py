from random import *

def pickAWord():

    wordList = []
    file = open("words.txt", 'r')

    for word in file:

        wordList.append(word)

    return wordList[randint(0, len(wordList) - 1)]

def Game():

    word = pickAWord()
    lettersFound = []
    Found = False

    for letter in word:
        lettersFound.append("_")

    while not Found:

        print(f"The word has {len(word)} and you found so far {len(word) - len(lettersFound)}")

        print("Those are: ", end='')

        for letter in lettersFound:

            print(letter, end='')

        answer = input("\nGuess a letter: ")

Game()