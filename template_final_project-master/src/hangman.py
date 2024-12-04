import pygame

class Hangman():
    def __init__self(self, images, current_stage):
        '''
        Stores the hangman drawing
        - images: (list) List of hangman images
        - current_stage: (int) Current hangman stage based on wrong guesses
        '''
        self.images = [pygame.image.load(f"hangman{i}.png") for i in range(7)]
        self.current_stage = 0

    
    def draw(self, screen): 
        '''
        Renders the current hangman stage on the screen
        args: screen: (obj) surface to be copied onto game screen
        return: None
        '''
        screen.blit(self.images[self.current_stage], (150, 100))
    
    def update_stage(self, wrong_guesses): 
        '''
        Updates the stage based on incorrect guesses
        args: wrong_guesses: (int) Number of incorrect guesses by the user
        return: None
        '''
        self.current_stage = wrong_guesses