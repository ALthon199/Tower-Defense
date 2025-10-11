import pygame 
import math
import constants as c
class Tower(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, tile_X, tile_Y, range, damage):
        pygame.sprite.Sprite.__init__(self)
        ## Spritesheet
        self.sprite_sheet = sprite_sheet
        self.animation_list = self.load_frames()
        
        #Calculate center
        self.x  = tile_X * c.TILE_SIZE + 0.5 * c.TILE_SIZE
        self.y = tile_Y * c.TILE_SIZE + 0.5 * c.TILE_SIZE
        self.range = range
        self.lastAngle = 0

        #Animation
        self.last_update = pygame.time.get_ticks()
        self.last_shot = pygame.time.get_ticks()
        self.cooldown = 500
    
        #Stats
        self.damage = damage

        #image
        self.frame = 0
        self.is_selected = False
        self.range_image = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)

        self.image = self.animation_list[self.frame]
        self.tile_X = tile_X
        self.tile_Y = tile_Y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    ## Extract Frames
    def load_frames(self):
        size = self.sprite_sheet.get_height()
        
        animation_list = []
        for x in range(c.ANIMATION_FRAMES):
            start = 0 + x * size
            frame = self.sprite_sheet.subsurface(start, 0, size, size)
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
            return
        self.play_animation()
        rotateAngle = math.atan2(curr_enemy.position[1] - self.y, curr_enemy.position[0] - self.x)
        rotateAngle *= 180 / math.pi
        base_image = self.animation_list[self.frame]
        rotatedImage = pygame.transform.rotate(base_image, -rotateAngle - 90)
        self.image = rotatedImage
        self.rect = self.image.get_rect(center = (self.x, self.y))
        if pygame.time.get_ticks() - self.last_shot >= self.cooldown:
            self.last_shot = pygame.time.get_ticks()
            curr_enemy.HP -= self.damage
            

            
        
        
           

                                
                
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.is_selected:
            pygame.draw.circle(self.range_image, (211, 211, 211, 40), (self.range, self.range), self.range)
            
            surface.blit(self.range_image, (self.x - self.range , self.y- self.range))
        
       

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
                
            
