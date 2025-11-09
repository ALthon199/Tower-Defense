from Enemy_Classes.enemy import Enemy
from Enemy_Classes.enemy_data import SHIELD_ZOMBIE_STATS
import pygame
class Shield_Zombie(Enemy):
    SHIELD_ZOMBIE_SPRITESHEET = None
    
    def __init__(self, waypoints):
        if Shield_Zombie.SHIELD_ZOMBIE_SPRITESHEET == None:
            self.load_assets()
         # Zmmbies are 64 by 64
        self.size = 64
        self.scale = 1.25
        self.color = 'black'
        self.animation_list =self.process_sheet()
        self.y_offset = 32
        super().__init__(self.animation_list, SHIELD_ZOMBIE_STATS['movespeed'], waypoints, SHIELD_ZOMBIE_STATS['health'], SHIELD_ZOMBIE_STATS['death_gold'], SHIELD_ZOMBIE_STATS['armor'], self.y_offset)

    def load_assets(self):
        Shield_Zombie.SHIELD_ZOMBIE_SPRITESHEET = pygame.image.load('assets/sprites/shield_zombie_walk.png').convert_alpha()

    def get_image(self, frames, rows):
       
        
        image = pygame.Surface((self.size, self.size)).convert_alpha() 
        image.blit(Shield_Zombie.SHIELD_ZOMBIE_SPRITESHEET, (0, 0), ((self.size * frames), (self.size * rows ), self.size, self.size))
        image = pygame.transform.scale(image, (self.size * self.scale, self.size * self.scale))
        # Removes any background color if present
        image.set_colorkey(self.color)

        return image

    def process_sheet(self):
        directions = ['up', 'left', 'down', 'right']
        animation = {}
        ## 4 by 8 sprite_sheet
        rows = 4
        frames = 9
        for row in range(rows):
            direction = directions[row]
            animation[direction] = []
            for frame in range(frames):
                image = self.get_image(frame, row)
                animation[direction].append(image)
        return animation
