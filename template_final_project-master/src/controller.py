import pygame 
import pygame_menu
from src.game import Game

class Controller:
    def __init__(self):
        '''
        Handles the main menu and game loop.
        '''
        pygame.init()
        pygame.event.pump()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Hangman")
        self.game = Game(self.screen)
        self.state = "MENU"
        self.clock = pygame.time.Clock()

    def main_menu(self):
        '''
        Display the main menu.
        '''
        menu = pygame_menu.Menu("Hangman", 800, 600, theme = pygame_menu.themes.THEME_GREEN)
        menu.add.button("Easy Mode", lambda: self.start_game("Easy"))
        menu.add.button("Hard Mode", lambda: self.start_game("Hard"))
        menu.add.button("Quit", pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def start_game(self, difficulty):
        '''
        Start the game with the selected difficulty.
        '''
        self.game.start(difficulty)
        self.mainloop()
        self.main_menu()
    
    def show_end_screen(self, win):
        '''
        Display the win or lose screen.
        '''
        menu = pygame_menu.Menu
        if win:
            menu.add.label("You Win!", max_char=-1, font_size=50)
        else:
            menu.add.label("You Lose!", max_char=-1, font_size=50)
            menu.add.label(f"The word was: {self.game.hangman.selected_word}", font_size=30)
        
        menu.add.button("Play Again", self.main_menu)
        menu.add.button("Quit", pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def mainloop(self):
        '''
        Run the main game loop.
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
        # self.main_menu()
        pygame.quit()