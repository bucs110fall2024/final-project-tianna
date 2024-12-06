import pygame 
import pygame_menu
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
        self.game = Game(self.screen)

    def main_menu(self):
        """Display the main menu."""
        menu = pygame_menu.Menu("Hangman", 800, 600, theme=pygame_menu.themes.THEME_DARK)
        menu.add.button("Easy Mode", lambda: self.start_game("Easy"))
        menu.add.button("Hard Mode", lambda: self.start_game("Hard"))
        menu.add.button("Quit", pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def start_game(self, difficulty):
        """Start the game with the selected difficulty."""
        self.game.start(difficulty)
        self.game_loop()

    def mainloop(self):
        '''
        docstring
        '''
        run = True 
        while run: 
            self.screen.fill((120, 0, 128))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                else:
                    self.game.process_event(event)
            
            self.game.update()
            self.game.draw()
            pygame.display.flip()

        pygame.quit()