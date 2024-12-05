import pygame 
# import pygame_menu
# import random_word
# import random_quotes_generator
from src.game import Game
from src.hangman import Hangman

class Controller:
    def __init__(self):
        '''
        docstring
        '''
        pygame.init()
        pygame.event.pump()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Hangman")

    def mainloop(self):
        '''
        docstring
        '''
        hangman = Hangman(self.screen)       
        run = True 
        while run: 
            self.screen.fill((120, 0, 128))
            hangman.update_stage(self.game.wrong_guesses)
            hangman.draw_stage(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
            pygame.display.flip()
            
        pygame.quit()