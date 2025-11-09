import pygame 
import math
import constants as c
from Tower_Classes.arrow import Arrow
class Tower(pygame.sprite.Sprite):
    def __init__(self, type,  base_images, animation_list, tile_X, tile_Y,  projectile_group, tower_stats, weapon_offset):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.tower_stats = tower_stats
        self.level = 0
        ## Firing ANimation
        self.sprite_sheet = base_images
        
        self.projectile_group = projectile_group
        self.all_animation_list = animation_list
        self.animation_list = self.all_animation_list[self.level]
        self.animation_frames = len(self.animation_list)
        #Calculate center
        self.x  = tile_X * c.TILE_SIZE + 0.5 * c.TILE_SIZE
        self.y = tile_Y * c.TILE_SIZE + 0.5 * c.TILE_SIZE
        

        #Animation
        self.last_update = pygame.time.get_ticks()
      
        

        #Stats
        self.range = tower_stats[self.level].get('Range')
        self.cooldown = tower_stats[self.level].get('Cooldown')
        self.damage = tower_stats[self.level].get('Damage')
        self.cost = tower_stats[0].get('Cost')
        self.upgrade_cost = tower_stats[self.level].get('Upgrade')
        self.next_range = tower_stats[self.level + 1].get('Range', None)
        

        #image
        self._layer = tile_Y
        self.angle = 0
        self.frame = 0
        self.is_selected = False
        self.range_image = pygame.Surface((self.next_range * 2, self.next_range * 2), pygame.SRCALPHA)
        self.weapon_offset = weapon_offset
        self.image = base_images[self.level]
        self.weapon_image = self.animation_list[self.frame]
        
       
        self.tile_X = tile_X
        self.tile_Y = tile_Y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def distance(self, position):
        return ((self.x - position[0]) ** 2 + (self.y - position[1]) ** 2) ** 0.5

   
    def draw(self, surface):
        if self.is_selected:
            pygame.draw.circle(self.range_image, (211, 211, 211, 30), (self.next_range, self.next_range), self.next_range)
            pygame.draw.circle(self.range_image, (211, 211, 211, 80), (self.next_range, self.next_range), self.range)
            surface.blit(self.range_image, (self.x - self.next_range , self.y - self.next_range))
            pygame.draw.rect(surface, (0, 100, 0), (c.SCREEN_WIDTH, 0, c.SIDE_PANEL, c.SCREEN_HEIGHT))

        surface.blit(self.image, self.rect)

        if 0 <= self.frame < len(self.animation_list):
            current_weapon_frame = self.animation_list[self.frame]
            rotated_weapon_image = pygame.transform.rotate(current_weapon_frame, self.angle - 90) 
            rotated_rect = rotated_weapon_image.get_rect()

            rotated_rect.center = self.rect.center

            
            surface.blit(rotated_weapon_image, (rotated_rect.topleft[0] + self.weapon_offset[0], rotated_rect.topright[1] + self.weapon_offset[1] ))
                        


       
           
    def upgrade(self, current_gold):
        if self.level < len(self.tower_stats) - 1 and current_gold >= self.upgrade_cost:
            current_gold = current_gold - self.upgrade_cost
            self.level += 1   
            self.range = self.tower_stats[self.level].get('Range')

            if self.level == len(self.tower_stats) - 1:
                self.next_range = self.tower_stats[self.level].get('Range', None)
            else:
                self.next_range = self.tower_stats[self.level+1].get('Range', None) 
            self.range_image = pygame.Surface((self.next_range * 2, self.next_range * 2), pygame.SRCALPHA) 
            self.cooldown = self.tower_stats[self.level].get('Cooldown')
            self.damage = self.tower_stats[self.level].get('Damage')
            self.upgrade_cost = self.tower_stats[self.level].get('Upgrade')
            self.animation_list = self.all_animation_list[self.level]
            self.animation_frames = len(self.animation_list)
            self.frame = 0
            self.image = self.sprite_sheet[self.level]
        
        return current_gold
            

 
  
                
            
