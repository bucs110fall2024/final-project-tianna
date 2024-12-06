from src.hangman import Hangman
import pygame

class Game():
    def __init__(self, screen):
        '''
        Initializes the game state, including setting up the screen and initializing the Hangman object.
        Args:
            screen (pygame.Surface): The pygame screen object where the game will be displayed.
        Return: None
        '''
        self.screen = screen
        self.hangman = Hangman()
        self.running = False
        self.game_state = "playing"
        self.input_text = ""  
        self.input_box = pygame.Rect(300, 500, 200, 50)  
        self.active = False
    
    def start(self, difficulty):
        '''
        Starts the game with the specified difficulty level by resetting the Hangman object.
        Args:
            difficulty (str): The difficulty level, either "Easy" or "Hard".
        Return: None
        '''
        self.hangman.reset(difficulty)
        self.running = True

    def process_event(self, event):
        '''
        Processes player input from mouse and keyboard events.
        Args:
            event (pygame.event.Event): The event that occurred (ex: mouse button click, key press).
        Return: None
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
        Updates the game state by checking if the player has won or lost.
        Args: None
        Return: None
        '''
        if self.hangman.is_loser():
            self.running = False
            self.game_state = "lost"
        elif self.hangman.is_winner():
            self.running = False
            self.game_state = "won"

    def draw(self):
        '''
        Draws the game elements, including the word to be guessed, guessed letters, and the hangman figure.
        Displays win or loss screens when the game is over.
        Args: None
        Return: None
        '''
        font1 = pygame.font.Font(None, 48)
        font2 = pygame.font.Font(None, 36)
        PURPLE = (120, 0, 128)
        BLACK = (0, 0, 0)
        self.screen.fill(PURPLE)

        if self.game_state == "playing":
            self.hangman.draw(self.screen)
            word_display = font1.render(self.hangman.display_word(), True, BLACK)
            self.screen.blit(word_display, (250, 550))

            guessed_letters_text = "Guessed Letters: " + ", ".join(sorted(self.hangman.guessed_letters))
            guessed_letters_display = font2.render(guessed_letters_text, True, BLACK)
            self.screen.blit(guessed_letters_display, (400, 200)) 

            color = (0, 255, 0) if self.active else (255, 0, 0)
            pygame.draw.rect(self.screen, color, self.input_box, 2)

            text_surface = font1.render(self.input_text, True, BLACK)
            self.screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))

            instruction = font2.render("Enter a letter and press Enter", True, BLACK)
            self.screen.blit(instruction, (200, 450))

        elif self.game_state == "won":
            win_text = font1.render("You Win!", True, BLACK)
            self.screen.blit(win_text, (300, 250))

        elif self.game_state == "lost":
            lose_text = font1.render("You Lose!", True, BLACK)
            self.screen.blit(lose_text, (300, 250))

            target_word_text = font2.render(f"The word was: {self.hangman.target_word}", True, BLACK)
            self.screen.blit(target_word_text, (250, 350))