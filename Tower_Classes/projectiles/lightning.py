import pygame
import json
import constants as c
from Tower_Classes.tower_data import ZAP_DATA
from Tower_Classes.projectiles.projectile import Projectile   
class Lightning(Projectile):
    LIGHTNING_ANIMATION = []
    LIGHTNING_JSON = []
    LIGHTNING_IMPACT = []
    LIGHTNING_DATA = ZAP_DATA
    def __init__(self, level, position, destination, projectile_group, chain_count = None, already_hit = None):
        if Lightning.LIGHTNING_ANIMATION == []:
            self.load_assets()
        self.level = level
        self.current_sprite = Lightning.LIGHTNING_ANIMATION[level]
        self.current_json = Lightning.LIGHTNING_JSON[level]
        self.animation_list = self.process()
        self.damage = ZAP_DATA[level]['Damage']
        self.maxRange = ZAP_DATA[level]['Range']
        self.chain = ZAP_DATA[level]['Chain'] if chain_count == None else chain_count # How many chains left
        self.already_hit = [] if already_hit == None else already_hit
        
        super().__init__(self.animation_list, self.LIGHTNING_IMPACT[self.level], position, destination, self.damage, projectile_group)

        
    def update(self, enemy_group):
        self.checkBounds()
        if self.has_hit:
            super().hit_animation()
            return 
        
        enemy = self.update_enemy(enemy_group)

        if enemy == None:
            super().update_movement()
        else:
            self.already_hit.append(enemy)
            self.chain_lightning(enemy_group)


    def update_enemy(self, enemy_group):
        for enemy in enemy_group:
            if self.rect.colliderect(enemy.hitbox) and enemy not in self.already_hit:
                enemy.current_HP -= self.damage
                self.has_hit = True
                self.frame = 0
                self.rect.center = enemy.position
                return enemy
        return None

    def chain_lightning(self, enemy_group):
        if self.chain <= 0: # NO more chains
            return 
        enemy = self.find_enemy(enemy_group)

        if enemy == None:
            return
        else:
            new_bolt = Lightning(self.level, self.position, enemy.position, self.projectile_group, self.chain - 1, self.already_hit)
            self.projectile_group.add(new_bolt)



    def find_enemy(self, enemy_group):
        for enemy in enemy_group:
            if enemy not in self.already_hit and (self.original_position - enemy.position).magnitude() < self.maxRange :
                return enemy
        return None

    def load_assets(self):
        
        for i in range(1, len(ZAP_DATA) + 1):
                archer_animation = pygame.image.load(f'assets/tower/zap/zap_projectile_0{i}.png').convert_alpha()
                Lightning.LIGHTNING_ANIMATION.append(archer_animation)
            # Sprite sizes for each animation (non-uniform sizes)
       

        for i in range(1, len(ZAP_DATA) + 1):
            path = f'assets/tower/zap/zap_projectile_0{i}.json'
            with open(path) as file:
                arrow_json = json.load(file) 
                Lightning.LIGHTNING_JSON.append(arrow_json)

        # 3 impact animations are all 64 by 64 with a total of 5 frames

        for i in range(3):
            full_impact = []
            impact_sheet = pygame.image.load(f'assets/tower/zap/zap_impact_0{i+1}.png').convert_alpha()
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