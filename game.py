from random import randint

class Game:
    def __init__(self):
        super().__init__()
        words = []
        with open("words.txt", "r") as file:
            for word in file:
                words.append(word.strip())
        self.__word = words[randint(0, len(words) - 1)]

        self.letters = []
        for i in range(len(self.__word)):
            self.letters.append('_')

        self.running = True
        self.tries = len(self.__word) + 5

    def letter_in_word(self, guessed_letter) -> bool:
        if guessed_letter in self.__word:
            possitions = [pos for pos, char in enumerate(self.__word) if char == guessed_letter]
            for possition in possitions:
                self.letters[possition] = guessed_letter
            return True

        else:
            self.tries -= 1
            return False

    def word(self) -> str:
        return self.__word
        
