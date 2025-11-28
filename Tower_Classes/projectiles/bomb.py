import pygame
import json
import constants as c
from Tower_Classes.tower_data import CATAPULT_DATA
from Tower_Classes.projectiles.projectile import Projectile   
class Bomb(Projectile):
    BOMB_ANIMATION = []
    BOMB_JSON = []
    BOMB_IMPACT = []
    BOMB_IMPACT_JSON = []
    CATAPULT_DATA = CATAPULT_DATA
    def __init__(self, level, position, destination, projectile_group):
        if Bomb.BOMB_ANIMATION == []:
            self.load_assets()
        self.level = level
        self.current_sprite = Bomb.BOMB_ANIMATION[level]
        self.current_json = Bomb.BOMB_JSON[level]
        self.all_animation_list, self.all_impact_list = self.process()
        self.animation_list = self.all_animation_list[level]
        self.impact_list = self.all_impact_list[level]



        self.explosion = self.impact_list[0]
        self.damage = Bomb.CATAPULT_DATA[level]['Damage']
        super().__init__(self.animation_list, self.impact_list, position, destination, self.damage, projectile_group)
        
        

    
    def update(self, enemy_group):
        if self.has_hit:
            super().hit_animation()
            return 
        if self.update_enemy(enemy_group):  
            return
        super().update_movement()


    def update_enemy(self, enemy_group):
        
        for enemy in enemy_group:
            if self.rect.colliderect(enemy.hitbox):
                self.explode(enemy_group)
                self.rect.center = enemy.position
                self.has_hit = True
                self.frame = 0
                return True

        
        return False
    def explode(self, enemy_group):

        explosion_rect = pygame.Rect(0, 0, self.explosion.get_width(), self.explosion.get_height())
        explosion_rect.center = self.rect.center



        for enemy in enemy_group:
            if explosion_rect.colliderect(enemy.hitbox):
                enemy.current_HP -= self.damage
    def load_assets(self):
        
        for i in range(1, len(CATAPULT_DATA) + 1):
            Bomb_animation = pygame.image.load(f'assets/tower/catapult/catapult_projectile_0{i}.png').convert_alpha()
            Bomb.BOMB_ANIMATION.append(Bomb_animation)
           
       

        for i in range(1, len(CATAPULT_DATA) + 1):
            path = f'assets/tower/catapult/catapult_projectile_0{i}.json'
            with open(path) as file:
                Bomb_json = json.load(file) 
                Bomb.BOMB_JSON.append(Bomb_json)
            

        for i in range(1, len(CATAPULT_DATA) + 1):
            bomb_impact = pygame.image.load(f'assets/tower/catapult/catapult_impact_0{i}.png').convert_alpha()
            Bomb.BOMB_IMPACT.append(bomb_impact)

        for i in range(1, len(CATAPULT_DATA) + 1):
            path = f'assets/tower/catapult/catapult_impact_0{i}.json'
            with open(path) as file:
                bomb_impact_json = json.load(file) 
                Bomb.BOMB_IMPACT_JSON.append(bomb_impact_json)

            
    def process(self):
        all_animation_list = []
        all_impact_list = []
        for i in range(len(CATAPULT_DATA)):
            # Projectile Animation
            current_sheet = Bomb.BOMB_ANIMATION[i]
            current_sheet.set_colorkey((0,0,0))
            current_sheet = current_sheet.convert_alpha()
            animation_data = Bomb.BOMB_JSON[i]
            animation_list =[]


            # Impact
            current_impact = Bomb.BOMB_IMPACT[i]
            current_impact.set_colorkey((0,0,0))
            current_impact = current_impact.convert_alpha()
            impact_data = Bomb.BOMB_IMPACT_JSON[i]
            impact_list = []
            

            for j in range(len(animation_data['frames'])):
                startX = animation_data['frames'][f'Tower 03 - Level {i+1:02d} - Projectile_{j+1:02d}.png']['frame']['x']
                startY = animation_data['frames'][f'Tower 03 - Level {i+1:02d} - Projectile_{j+1:02d}.png']['frame']['y']
                width = animation_data['frames'][f'Tower 03 - Level {i+1:02d} - Projectile_{j+1:02d}.png']['frame']['w']
                height = animation_data['frames'][f'Tower 03 - Level {i+1:02d} - Projectile_{j+1:02d}.png']['frame']['h']
                frame = current_sheet.subsurface(startX, startY, width, height)
                frame = pygame.transform.rotate(frame, 90)
                animation_list.append(frame)
            all_animation_list.append(animation_list)
            

            for j in range(len(impact_data['frames'])):
                startX = impact_data['frames'][f'Tower 03 - Level {i+1:02d} - Projectile - Impact_{j+1:02d}.png']['frame']['x']
                startY = impact_data['frames'][f'Tower 03 - Level {i+1:02d} - Projectile - Impact_{j+1:02d}.png']['frame']['y']
                width = impact_data['frames'][f'Tower 03 - Level {i+1:02d} - Projectile - Impact_{j+1:02d}.png']['frame']['w']
                height = impact_data['frames'][f'Tower 03 - Level {i+1:02d} - Projectile - Impact_{j+1:02d}.png']['frame']['h']
                frame = current_impact.subsurface(startX, startY, width, height)
                frame = pygame.transform.rotate(frame, 90)
                frame = pygame.transform.scale_by(frame, CATAPULT_DATA[self.level]['explosion_scale'] )
                impact_list.append(frame)
            all_impact_list.append(impact_list)
        


        return all_animation_list, all_impact_list