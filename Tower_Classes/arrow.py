import pygame
import json
import constants as c
from Tower_Classes.tower_data import TOWER_DATA
from Tower_Classes.projectile import Projectile   
class Arrow(Projectile):
    ARROW_ANIMATION = []
    ARROW_JSON = []
    ARROW_IMPACT = []
    ARROW_DATA = TOWER_DATA
    def __init__(self, level, position, destination):
        if Arrow.ARROW_ANIMATION == []:
            self.load_assets()
        self.current_sprite = Arrow.ARROW_ANIMATION[level]
        self.current_json = Arrow.ARROW_JSON[level]
        self.animation_list = self.process()
        self.damage = TOWER_DATA[level]['Damage']
        super().__init__(self.animation_list, self.ARROW_IMPACT, position, destination, self.damage)
        
        

    def load_assets(self):
        
        for i in range(1, len(TOWER_DATA) + 1):
                archer_animation = pygame.image.load(f'assets/turret/archer/archer_animation0{i}.png').convert_alpha()
                Arrow.ARROW_ANIMATION.append(archer_animation)
            # Sprite sizes for each animation (non-uniform sizes)
       

        for i in range(1, len(TOWER_DATA) + 1):
            path = f'assets/turret/archer/archer_projectile0{i}.json'
            with open(path) as file:
                arrow_json = json.load(file) 
                Arrow.ARROW_JSON.append(arrow_json)

        # impact animation are all 64 by 64 with a total of 6 frames
        
        impact_sheet = pygame.image.load(f'assets/turret/archer/archer_impact.png').convert_alpha()
        size = impact_sheet.get_height()
        for x in range(6):
            start = 0 + x * size
            frame = impact_sheet.subsurface(start, 0, size, size)
            Arrow.ARROW_IMPACT.append(frame)

    def process(self):
        current_sheet = self.current_sprite
       
        animation_data = self.current_json
        animation_list = []

        for i in range(len(animation_data['frames'])):
            startX = animation_data['frames'][f'{i}']['frame']['x']
            startY = animation_data['frames'][f'{i}']['frame']['y']
            width = animation_data['frames'][f'{i}']['frame']['w']
            height = animation_data['frames'][f'{i}']['frame']['h']
            frame = current_sheet.subsurface(startX, startY, width, height)
            animation_list.append(frame)

        return animation_list