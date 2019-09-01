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

    while not Found and numOfTries < 10:

        print(f"Number of tries left: {10 - numOfTries}")
        print(f"The word has {len(word)} and you found so far {foundSoFar}")

        print("Those are: ", end='')

        for letter in lettersFound:

            print(letter, end='')

        answer = input("\nGuess a letter: ")

        if answer in word and answer not in lettersFound:

            print("You found a letter!")

            Found = True

            for i in range(len(word)):

                if word[i] == answer:

                    lettersFound[i] = word[i]
                    foundSoFar += 1

                if Found:

                    if lettersFound[i] != word[i]:

                        Found = False

        else:

            print("Wrong answer. This letter doesn't exist on the word")
            numOfTries += 1

        if numOfTries == 10:

            print(f"You lost....\nThe word was \"{word}\".")

        if Found:

            print(f"Congrats! You found the word! It's \"{word}\"")

print("Welcome to the hangman python game!")
gamesPlayed = 0

while(1):

    gamesPlayed += 1
    print(f"This is your {gamesPlayed} game")

    print("Please wait so the program will pick up the word")
    Game()

    answer = input("Do you want to continue? y/n?: ")

    if answer == 'n':

        break;

print(f"It was fun playing with {gamesPlayed} games with you!")

print("End of program")