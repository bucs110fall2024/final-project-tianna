import pygame 
import pygame_menu
from src.game import Game
from src.hangman import Hangman

import random_word
import random_quotes_generator

class Controller:
    def __init__(self):
        '''
        docstring
        '''
        pygame.init()
        pygame.event.pump()
        self.screen = pygame.display.set_mode(800, 600)

    def mainloop(self):
        '''
        docstring
        '''
        hangman = Hangman()        
        run = True 
        while run: 
            self.screen.fill(120, 0, 128)
            hangman.update_stage(self.game.wrong_guesses)
            hangman.draw(self.screen)

            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #2. detect collisions and update models

            #3. Redraw next frame

            #4. Display next frame
            pygame.display.update()
        pygame.quit()