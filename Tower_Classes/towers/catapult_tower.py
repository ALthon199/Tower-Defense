import pygame
import constants as c
import json
import math
from Tower_Classes.towers.tower import Tower
from Tower_Classes.tower_data import CATAPULT_DATA
from Tower_Classes.projectiles.bomb import Bomb
class Catapult_Tower(Tower):
   
    BASE_IMAGES = []
    SPRITE_SHEET = []
    SPRITE_SHEET_JSON = []
    


    def __init__(self, tileX, tileY, projectile_group):
        if Catapult_Tower.BASE_IMAGES == []:
            self.load_assets()
        animation_list = self.process()
        weapon_offset = (0, -25)
        upgrade_offset = (-17, -60)
        super().__init__('catapult',
            Catapult_Tower.BASE_IMAGES, 
            animation_list,
            tileX, 
            tileY, 
            projectile_group, 
            CATAPULT_DATA,
            weapon_offset,
            upgrade_offset
        )
        
        

    def process(self):
        all_animation = []
        for i in range(len(CATAPULT_DATA)):
            
            current_sheet = Catapult_Tower.SPRITE_SHEET[i]
            
            animation_data = Catapult_Tower.SPRITE_SHEET_JSON[i]
            animation_list = []

            for j in range(len(animation_data['frames'])):
                startX = animation_data['frames'][f'Tower 03 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['x']
                startY = animation_data['frames'][f'Tower 03 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['y']
                width = animation_data['frames'][f'Tower 03 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['w']
                height = animation_data['frames'][f'Tower 03 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['h']
                frame = current_sheet.subsurface(startX, startY, width, height)
                frame = pygame.transform.rotate(frame, 90)
                animation_list.append(frame)
            all_animation.append(animation_list)

        return all_animation

    def load_assets(self):
        for i in range(1, len(CATAPULT_DATA) + 1):
            current_image = pygame.image.load(f'assets/tower/catapult/catapult_base_0{i}.png')
            current_image = pygame.transform.scale(current_image, (48, 64))
            
            Catapult_Tower.BASE_IMAGES.append(current_image)

         # Shooting 
       
        for i in range(1, len(CATAPULT_DATA) + 1):
            current_animation = pygame.image.load(f'assets/tower/catapult/catapult_weapon_0{i}.png').convert_alpha()
            current_animation.set_colorkey((0,0,0))
            current_animation = current_animation.convert_alpha()
            Catapult_Tower.SPRITE_SHEET.append(current_animation)
        
        for i in range(1, len(CATAPULT_DATA) + 1):
            path = f'assets/tower/catapult/catapult_weapon_0{i}.json'
            with open(path) as file:
                arrow_json = json.load(file) 
                Catapult_Tower.SPRITE_SHEET_JSON.append(arrow_json)
       
       

    def distance(self, position):
        return ((self.x - position[0]) ** 2 + (self.y - position[1]) ** 2) ** 0.5

    def update(self, enemy_group):
        curr_enemy = None
        for enemy in enemy_group:
            
            target_pos = (enemy.position[0], enemy.position[1])
            if self.distance(target_pos) <= self.range:
                curr_enemy = enemy
                
                break

        if curr_enemy == None:
            self.frame = 0
            return
        else:
            if self.frame == 0: 
            # Calculate angle towards the current enemy
                delta_y = curr_enemy.position[1] - self.y
                delta_x = curr_enemy.position[0]- self.x
                self.angle = math.degrees(math.atan2(-delta_y, delta_x)) - 90 
                
        self.play_animation(curr_enemy)
       
    def play_animation(self, enemy):
        # check time
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.cooldown // (self.animation_frames):
            self.frame += 1
            self.last_update = current_time
            if self.frame >= self.animation_frames:
                enemy_position = enemy.position
                new_projectile = Bomb(self.level,(self.tile_X * c.TILE_SIZE, self.tile_Y * c.TILE_SIZE), (enemy_position), self.projectile_group)
                self.projectile_group.add(new_projectile)
                self.frame = 0
 