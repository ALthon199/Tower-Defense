import pygame 
import math
import constants as c
from Tower_Classes.arrow import Arrow
class Tower(pygame.sprite.Sprite):
    UPGRADE_PANEL = None
    def __init__(self, type,  base_images, animation_list, tile_X, tile_Y,  projectile_group, tower_stats, weapon_offset, upgrade_offset=(0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.tower_stats = tower_stats
        self.level = 0
        ## Firing Animation
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
        self.upgrade_offset = upgrade_offset
        self.image = base_images[self.level]
        self.weapon_image = self.animation_list[self.frame]
        
       
        self.tile_X = tile_X
        self.tile_Y = tile_Y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        # fonts
        pygame.font.init()
        self.font = pygame.font.SysFont('sansserif', 24)
        self.description_font = pygame.font.SysFont('sansserif', 18)


    def distance(self, position):
        return ((self.x - position[0]) ** 2 + (self.y - position[1]) ** 2) ** 0.5

   
    def draw(self, surface):
        if self.is_selected:
            if Tower.UPGRADE_PANEL == None:
                Tower.UPGRADE_PANEL = pygame.image.load('assets/images/upgrade_panel.png').convert_alpha()
            pygame.draw.circle(self.range_image, (211, 211, 211, 30), (self.next_range, self.next_range), self.next_range)
            pygame.draw.circle(self.range_image, (211, 211, 211, 80), (self.next_range, self.next_range), self.range)
            surface.blit(self.range_image, (self.x - self.next_range , self.y - self.next_range))
            surface.blit(Tower.UPGRADE_PANEL, (c.SCREEN_WIDTH , 0))


            # Draw Tower
            upgrade_image = self.sprite_sheet[self.level]
            upgrade_weapon_image = self.animation_list[0]
            
            upgrade_image = pygame.transform.scale_by(upgrade_image, 3)
            upgrade_weapon_image = pygame.transform.scale_by(upgrade_weapon_image, 3)
            upgrade_weapon_image = pygame.transform.rotate(upgrade_weapon_image, -90)
            surface.blit(upgrade_image, (1100, 130))
            surface.blit(upgrade_weapon_image, (1125 + self.upgrade_offset[0], 150 + self.upgrade_offset[1]))


            # Description
            text = self.font.render(f'{self.type} Tower Lv.{self.level}'.upper(), True, (0,0,0))
            description = self.tower_stats[self.level]['Description']
            words = description.split('\n')
            
            
            

            text_rect = text.get_rect()
            text_rect.center = (1174, 40)
            
            surface.blit(text, text_rect)

            for i, line in enumerate(words):
                
                description_text = self.description_font.render(line, True, (0,0,0))
                description_text_rect = description_text.get_rect()
                description_text_rect.topleft = (1084, 440 + i * 20)
                surface.blit(description_text, description_text_rect)


            # Upgrade Stats
            if self.level < len(self.tower_stats) - 1:
                upgrade_stats = self.tower_stats[self.level + 1]
                upgrade_text = self.description_font.render(f'Upgrade Cost: {self.upgrade_cost} Gold', True, (0,0,0))
                upgrade_text_rect = upgrade_text.get_rect()
                upgrade_text_rect.topleft = (1110, 625)
                surface.blit(upgrade_text, upgrade_text_rect)

                damage_text = self.description_font.render(f'Damage: {self.damage}  -->  {upgrade_stats["Damage"]}', True, (0,0,0))
                damage_text_rect = damage_text.get_rect()
                damage_text_rect.topleft = (1110, 650)
                surface.blit(damage_text, damage_text_rect)

                range_text = self.description_font.render(f'Range: {self.range}  -->  {upgrade_stats["Range"]}', True, (0,0,0))
                range_text_rect = range_text.get_rect()
                range_text_rect.topleft = (1110, 675)
                surface.blit(range_text, range_text_rect)

                cooldown_text = self.description_font.render(f'Cooldown: {self.cooldown}ms  -->  {upgrade_stats["Cooldown"]}ms', True, (0,0,0))
                cooldown_text_rect = cooldown_text.get_rect()
                cooldown_text_rect.topleft = (1110, 700)
                surface.blit(cooldown_text, cooldown_text_rect)
            else:
                maxed_text = self.font.render('MAX LEVEL REACHED', True, (255,0,0))
                maxed_text_rect = maxed_text.get_rect()
                maxed_text_rect.topleft = (1110, 625)
                surface.blit(maxed_text, maxed_text_rect)
            
            

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
            

 
  
                
            
