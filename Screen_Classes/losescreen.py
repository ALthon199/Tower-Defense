


import constants as c
import pygame
from World_Classes.button import Button
class Lose_Screen():
    def __init__(self, screen, clock):
        self.screen = screen
        self.running = True
        self.clock = clock
        
        self.load_assets()
        self.load_buttons()

    def run(self):
        while self.running:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return "quit"

            
            
            self.screen.blit(self.title_background, (0,0))
            if self.start_button.draw(self.screen):
                return "home" 


            pygame.display.flip()
            self.clock.tick(60)
        
            
        return "quit" 


    def load_buttons(self):
        self.start_button = Button((c.SCREEN_WIDTH + c.SIDE_PANEL)//2 - self.start_image.get_width()/2, 600, self.start_image, single_click = True)
        

        
    def load_assets(self):
        
        self.start_image = pygame.image.load('assets/buttons/start.png')
        self.start_image = pygame.transform.scale(self.start_image, (200,100))
        self.start_hovered_image = pygame.image.load('assets/buttons/start recolor.png')\
        
        self.title_background = pygame.image.load('assets/images/background.png')
        self.title_background = pygame.transform.scale(self.title_background, (c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
       


