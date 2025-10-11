import pygame

class Button():
    def __init__(self, x, y, image, single_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        ## Prevent multiple clicks on one click
        self.clicked = False
        ## type of button
        self.single_click = single_click

    def draw(self, surface):
        action = False
        
        # get mouse position
        mouse_pos = pygame.mouse.get_pos()
        # check mouseover 
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                
                ## For single-click buttons
                if self.single_click: 
                    self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
            self.clicked = False
        #draw image
        surface.blit(self.image, self.rect)

        return action