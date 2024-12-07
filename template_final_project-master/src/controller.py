import pygame 
import pygame_menu
from src.game import Game

class Controller:
    def __init__(self):
        '''
        Initializes pygame, sets up the screen, and starts the main menu.
        Creates an instance of the Game class, which handles the gameplay logic.
        Args: None
        Return: None
        '''
        pygame.init()
        pygame.event.pump()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Hangman")
        self.game = Game(self.screen)
        self.main_menu()

    def main_menu(self):
        '''
        Displays the main menu where the player can choose the game difficulty or quit.
        Args: None
        Return: None
        '''
        menu = pygame_menu.Menu("Hangman", 800, 600, theme = pygame_menu.themes.THEME_GREEN)
        menu.add.button("Easy Mode", lambda: self.start_game("Easy"))
        menu.add.button("Hard Mode", lambda: self.start_game("Hard"))
        menu.add.button("Quit", pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def start_game(self, difficulty):
        '''
        Starts the game with the selected difficulty.
        Returns to the main menu after the game ends.
        Args:
            difficulty (str): The selected difficulty level ("Easy" or "Hard").
        Return: None
        '''
        self.game.start(difficulty)
        self.state = "RUNNING"
        self.mainloop()
        self.main_menu()

    def mainloop(self):
        '''
        Runs the main game loop where player input and events are processed, the game state is updated, 
        and the screen is drawn.
        Args: None
        Return: None
        '''
        run = True 
        while run: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                else:
                    self.game.process_event(event)
            self.game.update()
            self.game.draw()
            pygame.display.flip()
        self.main_menu()