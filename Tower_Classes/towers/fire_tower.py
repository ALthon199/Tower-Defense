import pygame
import constants as c
from Tower_Classes.towers.tower import Tower
from Tower_Classes.tower_data import FIRE_DATA
from Tower_Classes.projectiles.fireball import Fire_Ball
import json

class Fire_Tower(Tower):
    BASE_IMAGES = []
    SPRITE_SHEET = []
    SPRITE_SHEET_JSON = []
    
    FIRE_DATA = FIRE_DATA
    def __init__(self, tileX, tileY, projectile_group):
        if Fire_Tower.BASE_IMAGES == []:
            self.load_assets()
        animation_list = self.process()
        weapon_offset = (0, -20)
        upgrade_offset = (0, -20)
        super().__init__('fire',
            Fire_Tower.BASE_IMAGES, 
            animation_list,
            tileX, 
            tileY, 
            projectile_group, 
            FIRE_DATA,
            weapon_offset,
            upgrade_offset
        )

    def update(self, enemy_group):
        curr_enemy = None
        for enemy in enemy_group:
            
            target_pos = (enemy.position[0], enemy.position[1])
            if self.distance(target_pos) <= self.range:
                curr_enemy = enemy
                self.play_animation(curr_enemy)
                break

        if curr_enemy == None:
            self.frame = 0
            return
    
    def play_animation(self, curr_enemy):
        # check time
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.cooldown // (self.animation_frames) :
            self.frame += 1
            self.last_update = current_time
            if self.frame >= self.animation_frames:
                for direction in FIRE_DATA[self.level]['Pattern']:
                    endpoint = Fire_Tower.get_destination_point((self.tile_X * c.TILE_SIZE, self.tile_Y * c.TILE_SIZE), direction)
                    new_projectile = Fire_Ball(self.level,(self.tile_X * c.TILE_SIZE, self.tile_Y * c.TILE_SIZE), endpoint, self.projectile_group)
                
                    self.projectile_group.add(new_projectile)
                self.frame = 0

                


    def process(self):
        all_animation = []
        for i in range(len(FIRE_DATA)):
            current_sheet = Fire_Tower.SPRITE_SHEET[i]
            animation_data = Fire_Tower.SPRITE_SHEET_JSON[i]
        
            animation_list = []
            for j in range(len(animation_data['frames'])):
                startX = animation_data['frames'][f'Tower 07 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['x']
                startY = animation_data['frames'][f'Tower 07 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['y']
                width = animation_data['frames'][f'Tower 07 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['w']
                height = animation_data['frames'][f'Tower 07 - Level {i+1:02d} - Weapon_{j+1:02d}.png']['frame']['h']
                frame = current_sheet.subsurface(startX, startY, width, height)
                frame = pygame.transform.rotate(frame, 180)
                animation_list.append(frame)
            all_animation.append(animation_list)
            
        return all_animation
    
    def load_assets(self): 
        for i in range(1, len(FIRE_DATA) + 1):
            current_image = pygame.image.load(f'assets/tower/fire/fire_base_0{i}.png').convert_alpha()
            current_image = pygame.transform.scale(current_image, (48, 64))
            Fire_Tower.BASE_IMAGES.append(current_image)
        
        # Shooting
        

        for i in range(1, len(FIRE_DATA) + 1):
            current_animation = pygame.image.load(f'assets/tower/fire/fire_weapon_0{i}.png').convert_alpha()
            Fire_Tower.SPRITE_SHEET.append(current_animation)
        

        for i in range(1, len(FIRE_DATA) + 1):
            path = f'assets/tower/fire/fire_weapon_0{i}.json'
            with open(path) as file:
                arrow_json = json.load(file) 
                Fire_Tower.SPRITE_SHEET_JSON.append(arrow_json)

        
    def get_destination_point(start_pos, direction):
    
        x, y = start_pos
       
        large_distance = c.SCREEN_WIDTH * 2  #

        if direction == "LEFT":
            # Far to the left
            return (x - large_distance, y)
        elif direction == "RIGHT":
            # Far to the right
            return (x + large_distance, y)
        elif direction == "UP":
            # Far up
            return (x, y - large_distance)
        elif direction == "DOWN":
            # Far down
            return (x, y + large_distance)
        return start_pos