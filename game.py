import pygame



import constants as c
from Screen_Classes.homescreen import Home_Screen
from Screen_Classes.gamescreen import Game_Screen
from Screen_Classes.losescreen import Lose_Screen


class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL , c.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'home'

        #SCREENS
        self.Home_Screen = Home_Screen(self.screen, self.clock)
        self.Game_Screen = Game_Screen(self.screen, self.clock)
        self.Lose_Screen = Lose_Screen(self.screen, self.clock)


    def run(self):

        while self.running:
            if self.state == 'home':
                self.Home_Screen.running = True
                self.state = self.Home_Screen.run()

            elif self.state == 'start_game':
                self.Game_Screen = Game_Screen(self.screen, self.clock)

                self.state = self.Game_Screen.run()

            elif self.state == 'lost':
                self.state = self.Lose_Screen.run()

            elif self.state == 'quit':
                self.running = False
                
        
        pygame.quit()

   

   

