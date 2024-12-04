import pygame

class Game():
    def __init__self(self, word, guessed_letters):
        '''
        Initializes the game state
            - word: (str) The target word for the player to guess
            - guessed_letters: (list) List of letters the player has guessed
            - wrong_guesses: (int) Number of incorrect guesses
        '''
        self.word = word
        self.guessed_letters = []
        self.wrong_guesses = 0
    
    def check_guess(self, letter):
        '''
        Validates and updates the game state based on a guessed letter
        args: 
            letter: (char) Letter input guessed by user
        return: None
        '''
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word:
            self.wrong_guesses += 1
    
    def is_game_over(self):
        '''
        Checks if the game is over (win or loss)
        args: None
        return: Returns True if number of wrong guesses reaches 6 and False otherwise
        '''
        return self.wrong_guesses >= 6 or all(l in self.guessed_letters for l in self.word)

    
    def get_display_word(self):
        '''
        Returns the word with blanks and correctly guessed letters
        args: None
        return: Returns string containing the letters guessed by the user and dashes
        '''
        return " ".join([l if l in self.guessed_letters else "_" for l in self.word])