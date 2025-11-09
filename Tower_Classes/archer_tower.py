import pygame
import constants as c
import math
from Tower_Classes.tower import Tower
from Tower_Classes.tower_data import ARCHER_DATA
from Tower_Classes.arrow import Arrow

class Archer_Tower(Tower):
    BASE_IMAGES = []
    SPRITE_SHEET = []
    ANIMATION_FRAMES = 6

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
            projectile_group, 
            ARCHER_DATA,
            weapon_offset,
         
        )
        
        pass
    def load_frames(self):
        animation_list = []
        for i in range(len(Archer_Tower.SPRITE_SHEET)):
            current_sheet = Archer_Tower.SPRITE_SHEET[i]
            size = current_sheet.get_height()
            
            current_list = []
            for x in range(Archer_Tower.ANIMATION_FRAMES):
                start = 0 + x * size
                frame = current_sheet.subsurface(start, 0, size, size)
                current_list.append(frame)
            animation_list.append(current_list)
        return animation_list
    
    def load_assets(self):
        # Base
        for i in range(1, len(ARCHER_DATA) + 1):
            current_image = pygame.image.load(f'assets/turret/archer/archer_{i}.png').convert_alpha()
            current_image = pygame.transform.scale(current_image, (48, 64))
            Archer_Tower.BASE_IMAGES.append(current_image)
        # Shooting 
        
        for i in range(1, len(ARCHER_DATA) + 1):
            current_animation = pygame.image.load(f'assets/turret/archer/archer_weapon0{i}.png').convert_alpha()
            Archer_Tower.SPRITE_SHEET.append(current_animation)
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
            
            # Calculate angle towards the current enemy
            delta_y = curr_enemy.position[1] - self.y
            delta_x = curr_enemy.position[0]- self.x
           
            
            self.angle = math.degrees(math.atan2(-delta_y, delta_x))
                
        self.play_animation(curr_enemy)


    
       
    def play_animation(self, curr_enemy):
        # check time
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.cooldown // (self.animation_frames*3) :
            self.frame += 1
            self.last_update = current_time
            if self.frame >= self.animation_frames:
                new_projectile = Arrow(self.level,(self.tile_X * c.TILE_SIZE, self.tile_Y * c.TILE_SIZE), (curr_enemy.position))
                self.projectile_group.add(new_projectile)
                self.frame = 0
        
        
        
      