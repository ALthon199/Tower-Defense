import pygame

class Enemy_SpriteSheet():
    def __init__(self, image, width, height, color, scale):
        self.sheet = image
        self.width = width
        self.height = height
        self.color = color
        self.scale = scale
 
    def get_image(self, frames, rows):
        # Creates canvas for sprite
        image = pygame.Surface((self.width, self.height)).convert_alpha() 
        image.blit(self.sheet, (0, 0), ((frames * self.width), (rows * self.height  ), self.width, self.height))
        image = pygame.transform.scale(image, (self.width * self.scale, self.height * self.scale))
        # Removes any background color if present
        image.set_colorkey(self.color)

        return image
    
    def animationList(self, frames, rows):
        directions = ['up', 'left', 'down', 'right']
        animation = {}
        
        for row in range(rows):
            direction = directions[row]
            animation[direction] = []
            for frame in range(frames):
                image = self.get_image(frame, row)
                animation[direction].append(image)
        return animation