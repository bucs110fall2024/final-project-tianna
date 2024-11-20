import pygame 
from src.game import Game
from src.hangman import Hangman

class Controller:
    def __init__(self):
        pygame.init()
        pygame.event.pump()
        self.screen = pygame.display.set_mode()

    def mainloop(self):
        while(True): #this can also be a variable instead of just True
            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #2. detect collisions and update models

            #3. Redraw next frame

            #4. Display next frame
            pygame.display.flip()