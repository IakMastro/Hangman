from game import Game

hangman = Game()

print("Got a word")
while hangman.running:
    print(f"Letters found so far: {hangman.letters}")
    print(f"Number of tries: {hangman.tries}")
    guess = input("Guess a letter: ")
    
    if hangman.letter_in_word(guess):
        print("Correct guess!")

        if '_' not in hangman.letters:
            print(f"Congrats! You found the word! It's {hangman.word}")
            hangman.running = False

    else:
        print("Wrong guess")
        if hangman.tries == 0:
            print(f"Game Over! You lost! The word was {hangman.word}")
