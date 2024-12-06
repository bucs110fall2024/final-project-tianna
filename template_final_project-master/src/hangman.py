import pygame
from random_word import RandomWords
import random_quotes_generator

class Hangman():
    def __init__(self):
        '''
        Handles the hangman drawing and word management.
        '''
        self.target_word = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 6
        self.rw = RandomWords()
    
    def reset(self, difficulty):
        '''
        Reset the game with a new word or phrase based on difficulty.
        '''
        self.guessed_letters.clear()
        self.wrong_guesses = 0
        if difficulty == "Easy":
            self.target_word = self.rw.get_random_word(minLength=3, maxLength=5).lower()
        elif difficulty == "Hard":
            self.target_word = random_quotes_generator.get_random_quotes()

    def make_guess(self, letter):
        '''
        Process a guessed letter.
        '''
        if letter in self.target_word and letter not in self.guessed_letters:
            self.guessed_letters.add(letter)
        else:
            self.wrong_guesses += 1

    def is_winner(self):
        '''
        Check if the player has guessed the word.
        '''
        return all(letter in self.guessed_letters for letter in self.target_word)

    def is_loser(self):
        '''
        Check if the player has lost.
        '''
        return self.wrong_guesses >= self.max_wrong_guesses

    def display_word(self):
        '''
        Return the word with guessed letters revealed.
        '''
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.target_word])


    def draw(self, screen): 
        '''
        Draw the hangman figure.
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