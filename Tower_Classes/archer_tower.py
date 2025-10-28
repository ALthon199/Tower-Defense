import pygame
import constants as c
from Tower_Classes.tower import Tower
from Tower_Classes.tower_data import TOWER_DATA

class Archer_Tower(Tower):
    BASE_IMAGES = []
    SPRITE_SHEET = []
    
   


    def __init__(self, tileX, tileY, projectile_group):
        if Archer_Tower.BASE_IMAGES == []:
            self.load_assets()
        animation_list = self.load_frames()
        weapon_offset = (3,-11)
        super().__init__('archer',
            Archer_Tower.BASE_IMAGES, 
            animation_list,
            tileX, 
            tileY, 
            c.TURRET_COST, # Use the standard COST variable
            projectile_group, 
            TOWER_DATA,
            weapon_offset,
         
        )
        
        pass
    def load_frames(self):
        animation_list = []
        for i in range(len(Archer_Tower.SPRITE_SHEET)):
            current_sheet = Archer_Tower.SPRITE_SHEET[i]
            size = current_sheet.get_height()
            
            current_list = []
            for x in range(c.ANIMATION_FRAMES):
                start = 0 + x * size
                frame = current_sheet.subsurface(start, 0, size, size)
                current_list.append(frame)
            animation_list.append(current_list)
        return animation_list
    
    def load_assets(self):
        # Base
        for i in range(1, len(TOWER_DATA) + 1):
            current_image = pygame.image.load(f'assets/turret/archer/archer_{i}.png').convert_alpha()
            current_image = pygame.transform.scale(current_image, (48, 64))
            Archer_Tower.BASE_IMAGES.append(current_image)
        # Shooting 
        
        for i in range(1, len(TOWER_DATA) + 1):
            current_animation = pygame.image.load(f'assets/turret/archer/archer_weapon0{i}.png').convert_alpha()
            Archer_Tower.SPRITE_SHEET.append(current_animation)
        # Arrow
        
        
        
      