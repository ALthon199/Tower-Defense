import pygame
import json
import constants as c

class Projectile(pygame.sprite.Sprite):
    def __init__(self, animation_list, impact_list, position, destination, damage, projectile_group):
        pygame.sprite.Sprite.__init__(self)
        self.original_position = pygame.math.Vector2(position)
        self.position = self.original_position
        self.destination = pygame.math.Vector2(destination)
        self.movement = self.destination - self.position    
        self.movement = self.movement.normalize() * c.PROJECTILE_SPEED
        self.angle = self.movement.angle_to(pygame.math.Vector2(1, 0))
        self.damage = damage
        
        
        self.animation_list = animation_list
        self.impact_sheet = impact_list
       
        self.last_frame = 0
        self.frame = 0
        
        self.image = self.animation_list[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.has_hit = False
    

        self.projectile_group = projectile_group

    def draw(self, surface):
        if self.has_hit:
            base_image = self.impact_sheet[self.frame]
            surface.blit(base_image, (self.rect[0] - base_image.get_width() // 2,self.rect[1] - base_image.get_width() // 2 ) )
        else:
            base_image = self.animation_list[self.frame]
            rotated_image = pygame.transform.rotate(base_image, self.angle - 90)
            self.rect = rotated_image.get_rect()
            self.rect.center = self.position
            surface.blit(rotated_image, (self.rect))

    def update_movement(self):
        self.position = self.position + self.movement
        if pygame.time.get_ticks() - self.last_frame >= c.PROJECTILE_DELAY:
            self.last_frame = pygame.time.get_ticks()
            self.frame += 1
            if self.frame >= len(self.animation_list):
                self.frame = 0        

    def update_enemy(self, enemy_group):
        for enemy in enemy_group:
            if self.rect.colliderect(enemy.hitbox):
                enemy.current_HP -= self.damage
                self.has_hit = True
                self.frame = 0
                self.rect.center = enemy.position
                return True
        return False
        
        
       
               
    def hit_animation(self):
        if self.has_hit:
            if pygame.time.get_ticks() - self.last_frame >= c.PROJECTILE_DELAY:
                self.last_frame = pygame.time.get_ticks()
                self.frame += 1
                if self.frame >= len(self.impact_sheet):
                    self.kill()
            
