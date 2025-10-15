import pygame 
import math
import constants as c
from tower_data import TOWER_DATA
class Tower(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, tile_X, tile_Y, cost):
        pygame.sprite.Sprite.__init__(self)
        ## Spritesheet
        self.level = 0
        self.sprite_sheet = sprite_sheet
        
        self.animation_list = self.load_frames()
        
        #Calculate center
        self.x  = tile_X * c.TILE_SIZE + 0.5 * c.TILE_SIZE
        self.y = tile_Y * c.TILE_SIZE + 0.5 * c.TILE_SIZE


        #Animation
        self.last_update = pygame.time.get_ticks()
        self.last_shot = None
        
    
        #Stats
        self.range = TOWER_DATA[self.level].get('Range')
        self.cooldown = TOWER_DATA[self.level].get('Cooldown')
        self.damage = TOWER_DATA[self.level].get('Damage')
        self.cost = cost
        self.upgrade_cost = TOWER_DATA[self.level].get('Upgrade')
        self.next_range = TOWER_DATA[self.level + 1].get('Range', None)
        

        #image
        self.last_angle = 0
        self.frame = 0
        self.is_selected = False
        self.range_image = pygame.Surface((self.next_range * 2, self.next_range * 2), pygame.SRCALPHA)

        self.image = self.animation_list[self.frame]
        self.tile_X = tile_X
        self.tile_Y = tile_Y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    ## Extract Frames
    def load_frames(self):
        current_sheet = self.sprite_sheet[self.level]
        size = current_sheet.get_height()
        
        animation_list = []
        for x in range(c.ANIMATION_FRAMES):
            start = 0 + x * size
            frame = current_sheet.subsurface(start, 0, size, size)
            animation_list.append(frame)
        return animation_list

    def update(self, enemy_group):
        curr_enemy = None
        for enemy in enemy_group:
            target_pos = (enemy.position[0], enemy.position[1])
            if self.distance(target_pos) <= self.range:
                curr_enemy = enemy
                
                break

        if curr_enemy == None:
            self.frame = 0
            base_image = self.animation_list[self.frame]
            rotatedImage = pygame.transform.rotate(base_image, -self.last_angle - 90)
            self.image = rotatedImage
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.play_animation()
            return 
                
    
        ## Need to fix first shot
        if self.last_shot == None or pygame.time.get_ticks() - self.last_shot >= self.cooldown:
            self.angle = math.degrees(math.atan2(curr_enemy.position[1] - self.y, curr_enemy.position[0] - self.x))
            self.last_angle = self.angle
            self.last_shot = pygame.time.get_ticks()
            curr_enemy.HP -= self.damage
    
        base_image = self.animation_list[self.frame]
        rotatedImage = pygame.transform.rotate(base_image, -self.angle - 90)
        self.image = rotatedImage
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.play_animation()
        
           
    def upgrade(self, current_gold):
        if self.level < len(TOWER_DATA) - 1 and current_gold >= self.upgrade_cost:
            current_gold = current_gold - self.upgrade_cost
            self.level += 1   
            self.range = TOWER_DATA[self.level].get('Range')
            if self.level == len(TOWER_DATA) - 1:
                self.next_range = TOWER_DATA[self.level].get('Range', None)
            else:
                self.next_range = TOWER_DATA[self.level+1].get('Range', None)
            self.range_image = pygame.Surface((self.next_range * 2, self.next_range * 2), pygame.SRCALPHA) 
            self.cooldown = TOWER_DATA[self.level].get('Cooldown')
            self.damage = TOWER_DATA[self.level].get('Damage')
            self.upgrade_cost = TOWER_DATA[self.level].get('Upgrade')
            self.animation_list = self.load_frames()
        
        return current_gold
            


            
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.is_selected:
            pygame.draw.circle(self.range_image, (211, 211, 211, 30), (self.next_range, self.next_range), self.next_range)
            pygame.draw.circle(self.range_image, (211, 211, 211, 80), (self.next_range, self.next_range), self.range)
            surface.blit(self.range_image, (self.x - self.next_range , self.y - self.next_range))
            pygame.draw.rect(surface, (0, 100, 0), (c.SCREEN_WIDTH, 0, c.SIDE_PANEL, c.SCREEN_HEIGHT))
        
       

    def distance(self, position):
        return ((self.x - position[0]) ** 2 + (self.y - position[1]) ** 2) ** 0.5

    
       
    def play_animation(self):
        # check time
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= c.ANIMATION_DELAY:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= c.ANIMATION_FRAMES:
                self.frame = 0
                
            
