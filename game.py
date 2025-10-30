import pygame



import constants as c
from homescreen import HomeScreen
from gamescreen import GameScreen
from losescreen import LoseScreen


class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL , c.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'home'

        #SCREENS
        self.Homescreen = HomeScreen(self.screen, self.clock)
        self.Gamescreen = GameScreen(self.screen, self.clock)
        self.Losescreen = LoseScreen(self.screen, self.clock)


    def run(self):

        while self.running:
            print(self.state)
            if self.state == 'home':
                self.Homescreen.running = True
                self.state = self.Homescreen.run()

            elif self.state == 'start_game':
                self.state = self.Gamescreen.run()

            elif self.state == 'lost':
                self.state = self.Losescreen.run()

            elif self.state == 'quit':
                self.running = False
                
        
        pygame.quit()

   

   

