import pygame
from Enemy_Classes.enemy_data import ZOMBIE_STATS
from Enemy_Classes.enemy import Enemy

class Zombie(Enemy):
    ZOMBIE_SPRITESHEET = None
    
    def __init__(self, waypoints):
        if Zombie.ZOMBIE_SPRITESHEET == None:
            self.load_assets()
         # Zmmbies are 64 by 64
        self.size = 64
        self.scale = 1.25
        self.color = 'black'
        self.y_offset = 32
        self.animation_list =self.process_sheet()
        super().__init__(self.animation_list, ZOMBIE_STATS['movespeed'], waypoints, ZOMBIE_STATS['health'], ZOMBIE_STATS['death_gold'], ZOMBIE_STATS['armor'], self.y_offset)

    def load_assets(self):
        Zombie.ZOMBIE_SPRITESHEET = pygame.image.load('assets/sprites/walk.png').convert_alpha()

    def get_image(self, frames, rows):
       
        
        image = pygame.Surface((self.size, self.size)).convert_alpha() 
        image.blit(Zombie.ZOMBIE_SPRITESHEET, (0, 0), ((self.size * frames), (self.size * rows ), self.size, self.size))
        image = pygame.transform.scale(image, (self.size * self.scale, self.size * self.scale))
        # Removes any background color if present
        image.set_colorkey(self.color)

        return image

    def process_sheet(self):
        directions = ['up', 'left', 'down', 'right']
        animation = {}
        # 4 by 9 sprite_sheet
        rows = 4
        frames = 9
        for row in range(rows):
            direction = directions[row]
            animation[direction] = []
            for frame in range(frames):
                image = self.get_image(frame, row)
                animation[direction].append(image)
        return animation
