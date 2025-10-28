import pygame
import constants as c
import json
from Tower_Classes.tower import Tower
from Tower_Classes.tower_data import TOWER_DATA
class Zap_Tower(Tower):
   
    BASE_IMAGES = []
    SPRITE_SHEET = []
    SPRITE_SHEET_JSON = []
    


    def __init__(self, tileX, tileY, projectile_group):
        if Zap_Tower.BASE_IMAGES == []:
            self.load_assets()
        animation_list = self.process()
        weapon_offset = (0, -11)
        super().__init__('archer',
            Zap_Tower.BASE_IMAGES, 
            animation_list,
            tileX, 
            tileY, 
            c.TURRET_COST, # Use the standard COST variable
            projectile_group, 
            TOWER_DATA,
            weapon_offset
        )
        
        

    def process(self):
        all_animation = []
        for i in range(len(TOWER_DATA)):
            current_sheet = Zap_Tower.SPRITE_SHEET[i]
            
            animation_data = Zap_Tower.SPRITE_SHEET_JSON[i]
            animation_list = []

            for j in range(len(animation_data['frames'])):
                startX = animation_data['frames'][f'Tower 02 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['x']
                startY = animation_data['frames'][f'Tower 02 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['y']
                width = animation_data['frames'][f'Tower 02 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['w']
                height = animation_data['frames'][f'Tower 02 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['h']
                frame = current_sheet.subsurface(startX, startY, width, height)
                animation_list.append(frame)
            all_animation.append(animation_list)

        return all_animation

    def load_assets(self):
        for i in range(1, len(TOWER_DATA) + 1):
            current_image = pygame.image.load(f'assets/turret/zap/zap_base_0{i}.png')
            current_image = pygame.transform.scale(current_image, (48, 64))
            Zap_Tower.BASE_IMAGES.append(current_image)

         # Shooting 
        self.zap_animations = []
        for i in range(1, len(TOWER_DATA) + 1):
            current_animation = pygame.image.load(f'assets/turret/zap/zap_weapon_0{i}.png').convert_alpha()
            
            Zap_Tower.SPRITE_SHEET.append(current_animation)
        
        for i in range(1, len(TOWER_DATA) + 1):
            path = f'assets/turret/zap/zap_weapon_0{i}.json'
            with open(path) as file:
                arrow_json = json.load(file) 
                Zap_Tower.SPRITE_SHEET_JSON.append(arrow_json)
 