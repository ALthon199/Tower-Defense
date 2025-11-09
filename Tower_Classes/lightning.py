import pygame
import json
import constants as c
from Tower_Classes.tower_data import ZAP_DATA
from Tower_Classes.projectile import Projectile   
class Lightning(Projectile):
    LIGHTNING_ANIMATION = []
    LIGHTNING_JSON = []
    LIGHTNING_IMPACT = []
    LIGHTNING_DATA = ZAP_DATA
    def __init__(self, level, position, destination):
        if Lightning.LIGHTNING_ANIMATION == []:
            self.load_assets()
        self.level = level
        self.current_sprite = Lightning.LIGHTNING_ANIMATION[level]
        self.current_json = Lightning.LIGHTNING_JSON[level]
        self.animation_list = self.process()
        self.damage = ZAP_DATA[level]['Damage']
        self.maxRange = ZAP_DATA[level]['Range']
        super().__init__(self.animation_list, self.LIGHTNING_IMPACT[self.level], position, destination, self.damage)

        
    def update(self, enemy_group):
        self.checkBounds()
        if self.has_hit:
            super().hit_animation()
            return 
        if super().update_enemy(enemy_group):
            return
        super().update_movement()
        
      
        

    def load_assets(self):
        
        for i in range(1, len(ZAP_DATA) + 1):
                archer_animation = pygame.image.load(f'assets/turret/zap/zap_projectile_0{i}.png').convert_alpha()
                Lightning.LIGHTNING_ANIMATION.append(archer_animation)
            # Sprite sizes for each animation (non-uniform sizes)
       

        for i in range(1, len(ZAP_DATA) + 1):
            path = f'assets/turret/zap/zap_projectile_0{i}.json'
            with open(path) as file:
                arrow_json = json.load(file) 
                Lightning.LIGHTNING_JSON.append(arrow_json)

        # 3 impact animations are all 64 by 64 with a total of 5 frames

        for i in range(3):
            full_impact = []
            impact_sheet = pygame.image.load(f'assets/turret/zap/zap_impact_0{i+1}.png').convert_alpha()
            size = impact_sheet.get_height()
            for x in range(5):
                start = 0 + x * size
                frame = impact_sheet.subsurface(start, 0, size, size)
                full_impact.append(frame)
            Lightning.LIGHTNING_IMPACT.append(full_impact)


    def checkBounds(self):
        if abs(self.original_position.distance_to(self.position)) > self.maxRange:
            self.kill()
       
    def process(self):
        current_sheet = self.current_sprite
       
        animation_data = self.current_json
        animation_list = []

        for i in range(len(animation_data['frames'])):
            startX = animation_data['frames'][f'Tower 02 - Level {self.level+1:02d} - Projectile_{i+1:02d}.png']['frame']['x']
            startY = animation_data['frames'][f'Tower 02 - Level {self.level+1:02d} - Projectile_{i+1:02d}.png']['frame']['y']
            width = animation_data['frames'][f'Tower 02 - Level {self.level+1:02d} - Projectile_{i+1:02d}.png']['frame']['w']
            height = animation_data['frames'][f'Tower 02 - Level {self.level+1:02d} - Projectile_{i+1:02d}.png']['frame']['h']
            frame = current_sheet.subsurface(startX, startY, width, height)
            animation_list.append(frame)

        return animation_list