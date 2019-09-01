from random import *

def pickAWord():

    wordList = []
    file = open("words.txt", 'r')

    for word in file:

        wordList.append(word.strip())

    return wordList[randint(0, len(wordList) - 1)]

def Game():

    word = pickAWord()
    lettersFound = []
    Found = False

    numOfTries = 0
    foundSoFar = 0

    for letter in word:
        lettersFound.append("_")

    while not Found and numOfTries < 3:

        print(f"The word has {len(word)} and you found so far {foundSoFar}")

        print("Those are: ", end='')

        for letter in lettersFound:

            print(letter, end='')

        answer = input("\nGuess a letter: ")

        if answer in word:

            print("You found a letter!")

            for i in range(len(word)):

                if word[i] == answer:

                    lettersFound[i] = word[i]
                    foundSoFar += 1

        else:

            print("Wrong answer. This letter doesn't exist on the word")
            numOfTries += 1

        if(numOfTries == 3):

            print(f"You lost....\nThe word was \"{word}\".")

Game()