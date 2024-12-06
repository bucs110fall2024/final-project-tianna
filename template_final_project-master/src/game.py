from src.hangman import Hangman
import pygame

class Game():
    def __init__(self, screen):
        '''
        Initializes the game state
            - word: (str) The target word for the player to guess
        '''
        self.screen = screen
        self.hangman = Hangman()
        self.running = False
    
    def start(self, difficulty):
        """Start the game with the given difficulty."""
        self.hangman.reset(difficulty)
        self.running = True

    def process_event(self, event):
        """Process player input."""
        if event.type == pygame.KEYDOWN and self.hangman.target_word:
            if event.unicode.isalpha():
                guess = event.unicode.lower()
                self.hangman.make_guess(guess)

    # def check_guess(self, letter):
    #     '''
    #     Validates and updates the game state based on a guessed letter
    #     args: 
    #         letter: (char) Letter input guessed by user
    #     return: None
    #     '''
    #     if letter in self.word and letter not in self.guessed_letters:
    #         self.guessed_letters.append(letter)
    #     elif letter not in self.word:
    #         self.wrong_guesses += 1
    
    def update(self):
        """Update the game state and check win/lose conditions."""
        if self.hangman.is_loser():
            print("You lost! The word was:", self.hangman.target_word)
            self.running = False
        elif self.hangman.is_winner():
            print("You won!")
            self.running = False

    def draw(self):
        FONT = pygame.font.Font(None, 48)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        """Draw the game elements."""
        self.screen.fill(WHITE)
        self.hangman.draw(self.screen)
        word_display = FONT.render(self.hangman.display_word(), True, BLACK)
        self.screen.blit(word_display, (250, 550))

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