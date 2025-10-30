


import constants as c
import pygame
from button import Button
class HomeScreen():
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

            
            self.screen.fill('green') 
            self.screen.blit(self.title_image, self.title_rect)
            if self.start_button.draw(self.screen):
                self.running = False
                return "start_game" 


            pygame.display.flip()
            self.clock.tick(60)
        
            
        return "quit" 


    def load_buttons(self):
        self.start_button = Button((c.SCREEN_WIDTH + c.SIDE_PANEL)//2 - self.start_image.get_width()/2, 600, self.start_image, single_click = True)
        

        
    def load_assets(self):
        

        self.start_image = pygame.image.load('assets/buttons/start.png')
        self.start_image = pygame.transform.scale(self.start_image, (200,100))
        self.start_hovered_image = pygame.image.load('assets/buttons/start recolor.png')
        self.title_image = pygame.image.load('assets/buttons/exit.png')
        self.title_image = pygame.transform.scale(self.title_image, (600, 200))
        self.title_rect = self.title_image.get_rect()
        self.title_rect = ((c.SCREEN_WIDTH + c.SIDE_PANEL) /2 -self.title_image.get_width()/2, 100)
       


