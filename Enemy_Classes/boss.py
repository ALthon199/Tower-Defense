from Enemy_Classes.enemy import Enemy
from Enemy_Classes.enemy_data import BOSS_STATS
import pygame
class Boss(Enemy):
    BOSS_SPRITESHEET = None
    
    def __init__(self, waypoints):
        if Boss.BOSS_SPRITESHEET == None:
            self.load_assets()
        
        self.size = 64
        self.scale = 1.75
        self.color = 'black'
        self.animation_list =self.process_sheet()

        self.y_offset = 30
        super().__init__(self.animation_list, BOSS_STATS['movespeed'], waypoints, BOSS_STATS['health'], BOSS_STATS['death_gold'], BOSS_STATS['armor'], self.y_offset)
    

    def draw(self, screen):
        percent_green = self.current_HP / self.HP
        width = self.hpRect.get_width()
        height = self.hpRect.get_height()
        self.hpRect.fill('Green', (0, 0, width * percent_green, height))
        self.hpRect.fill('Red', (width * percent_green, 0, width, height))
        screen.blit(self.image, self.rect)
        screen.blit(self.hpRect, (self.rect[0] + 30, self.rect[1]))

    def load_assets(self):
        Boss.BOSS_SPRITESHEET = pygame.image.load('assets/sprites/boss_walk.png').convert_alpha()

    def get_image(self, frames, rows):
       
        
        image = pygame.Surface((self.size, self.size)).convert_alpha() 
        image.blit(Boss.BOSS_SPRITESHEET, (0, 0), ((self.size * frames), (self.size * rows ), self.size, self.size))
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
