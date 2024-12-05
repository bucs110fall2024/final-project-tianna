import pygame

class Hangman():
    def __init__self(self, screen):
        '''
        Stores the hangman drawing
        - screen: (obj) Surface of game screen
        - wrong_guesses: (int) Current number of incorrect letter guesses
        '''
        self.screen = screen
        self.wrong_guesses = 0
    
    def draw_stage(self): 
        '''
        Draws the hangman figure based on the number of wrong guesses
        return: None
        '''
        black = (0, 0, 0)
        # Draw the gallows
        pygame.draw.line(self.screen, black, (100, 400), (300, 400), 5)  # Base
        pygame.draw.line(self.screen, black, (200, 400), (200, 100), 5)  # Vertical pole
        pygame.draw.line(self.screen, black, (200, 100), (300, 100), 5)  # Top bar
        pygame.draw.line(self.screen, black, (300, 100), (300, 150), 5)  # Rope
    
    def update_stage(self, wrong_guesses): 
        '''
        Updates the stage based on incorrect guesses
        args: wrong_guesses: (int) Number of incorrect guesses by the user
        return: None
        '''
        self.current_stage = wrong_guesses