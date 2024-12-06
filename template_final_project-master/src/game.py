from src.hangman import Hangman
import pygame

class Game():
    def __init__(self, screen):
        '''
        Initializes the game state
        '''
        self.screen = screen
        self.hangman = Hangman()
        self.running = False

        self.input_text = ""  
        self.input_box = pygame.Rect(300, 600, 200, 50)  
        self.active = False
    
    def start(self, difficulty):
        '''
        Start the game with the given difficulty.
        '''
        self.hangman.reset(difficulty)
        self.running = True

    def process_event(self, event):
        '''
        Process player input.
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.input_text.isalpha():
                        guess = self.input_text.lower()
                        self.hangman.make_guess(guess)
                    self.input_text = ""  
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]  
                else:
                    self.input_text += event.unicode  

    
    def update(self):
        '''
        Update the game state and check win/lose conditions.
        '''
        if self.hangman.is_loser() and self.running:
            self.running = False
            self.hangman.state.controller = "LOSE"
        elif self.hangman.is_winner() and self.running:
            print("You won!")
            self.running = False
            self.hangman.state.controller = "WIN"

    def draw(self):
        '''
        Draw the game elements.
        '''
        FONT = pygame.font.Font(None, 48)
        PURPLE = (120, 0, 128)
        BLACK = (0, 0, 0)
        self.screen.fill(PURPLE)
        self.hangman.draw(self.screen)
        word_display = FONT.render(self.hangman.display_word(), True, BLACK)
        self.screen.blit(word_display, (250, 550))

        color = (0, 255, 0) if self.active else (255, 0, 0)
        pygame.draw.rect(self.screen, color, self.input_box, 2)

        text_surface = FONT.render(self.input_text, True, BLACK)
        self.screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))

        instruction = FONT.render("Enter a letter and press Enter", True, BLACK)
        self.screen.blit(instruction, (200, 700))