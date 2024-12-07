import pygame
from wonderwords import RandomWord

class Hangman():
    def __init__(self):
        '''
        Initializes the Hangman game, including setting up the word to guess,
        tracking the letters guessed, and setting the number of wrong guesses allowed.
        Args: None
        Return: None
        '''
        self.target_word = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 6
        self.rw = RandomWord()
    
    def reset(self, difficulty):
        '''
        Resets the game, choosing a new word based on the given difficulty.
        Args:
            difficulty (str): The difficulty of the game, either "Easy" or "Hard".
        Return: None
        '''
        self.guessed_letters.clear()
        self.wrong_guesses = 0
        if difficulty == "Easy":
            self.target_word = self.rw.word(word_min_length=3, word_max_length=5).lower()
        elif difficulty == "Hard":
            self.target_word = self.rw.word(word_min_length=6, word_max_length=8).lower()

    def make_guess(self, letter):
        '''
        Processes a player's guess, updating the number of wrong guesses or 
        adding the letter to the guessed letters if correct.
        Args:
            letter (str): The letter guessed by the player.
        Return: None
        '''
        if letter in self.target_word and letter not in self.guessed_letters:
            self.guessed_letters.add(letter)
        else:
            self.wrong_guesses += 1
            self.guessed_letters.add(letter)

    def is_winner(self):
        '''
        Checks if the player has won by guessing all the letters of the word.
        Args: None
        Return:
            bool: True if all letters of the word are guessed, False otherwise.
        '''
        return all(letter in self.guessed_letters for letter in self.target_word if letter.isalpha())


    def is_loser(self):
        '''
        Checks if the player has lost by reaching the maximum number of wrong guesses.
        Args: None
        Return:
            bool: True if the player has lost, False otherwise.
        '''
        return self.wrong_guesses >= self.max_wrong_guesses

    def display_word(self):
        '''
        Returns the word with blanks for unguessed letters and the correct letters revealed.
        Args: None
        Return:
            str: The word to guess with unguessed letters represented by underscores.
        '''
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.target_word])


    def draw(self, screen): 
        '''
        Draws the hangman figure and gallows on the given screen based on the number of wrong guesses.
        Args:
            screen (pygame.Surface): The surface to draw the hangman and gallows on.
        Return: None
        '''
        BLACK = (0, 0, 0)

        # Draw the gallows
        pygame.draw.line(screen, BLACK, (100, 400), (300, 400), 5)  # Base
        pygame.draw.line(screen, BLACK, (200, 400), (200, 100), 5)  # Vertical pole
        pygame.draw.line(screen, BLACK, (200, 100), (300, 100), 5)  # Top bar
        pygame.draw.line(screen, BLACK, (300, 100), (300, 150), 5)  # Rope

        # Draw the hangman parts based on wrong guesses
        if self.wrong_guesses >= 1:  # Head
            pygame.draw.circle(screen, BLACK, (300, 180), 30, 5)
        if self.wrong_guesses >= 2:  # Body
            pygame.draw.line(screen, BLACK, (300, 210), (300, 300), 5)
        if self.wrong_guesses >= 3:  # Left arm
            pygame.draw.line(screen, BLACK, (300, 240), (260, 270), 5)
        if self.wrong_guesses >= 4:  # Right arm
            pygame.draw.line(screen, BLACK, (300, 240), (340, 270), 5)
        if self.wrong_guesses >= 5:  # Left leg
            pygame.draw.line(screen, BLACK, (300, 300), (270, 350), 5)
        if self.wrong_guesses >= 6:  # Right leg
            pygame.draw.line(screen, BLACK, (300, 300), (330, 350), 5)