import pygame
import json
import constants as c
from Tower_Classes.tower_data import FIRE_DATA
from Tower_Classes.projectiles.projectile import Projectile   
class Fire_Ball(Projectile):
    FIRE_BALL_ANIMATION = []
    FIRE_BALL_IMPACT_JSON = []
    FIRE_BALL_IMPACT = []
    FIRE_BALL_DATA = FIRE_DATA
    def __init__(self, level, position, destination, projectile_group):
        if Fire_Ball.FIRE_BALL_ANIMATION == []:
            self.load_assets()
        self.current_sprite = Fire_Ball.FIRE_BALL_ANIMATION
        self.current_json = Fire_Ball.FIRE_BALL_IMPACT_JSON
        self.impact_list = self.process()
        self.damage = Fire_Ball.FIRE_BALL_DATA[level]['Damage']
        super().__init__(Fire_Ball.FIRE_BALL_ANIMATION, self.impact_list, position, destination, self.damage, projectile_group)
        
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
                enemy.current_HP -= self.damage
                self.enemy_knockback(enemy)
                self.has_hit = True
                self.frame = 0
                self.rect.center = enemy.position
                return True
        return False
    
    def enemy_knockback(self, enemy):
        movement = enemy.movement.normalize()
       
        enemy.position[0] -= movement.x * Fire_Ball.FIRE_BALL_DATA[0]['Push_Back']
        enemy.position[1] -= movement.y * Fire_Ball.FIRE_BALL_DATA[0]['Push_Back']
    def load_assets(self):
        
        
        # Fire Ball Animation is same for all level, 8 frames, 32 by 32
        # Load and convert without alpha first
        all_frames = pygame.image.load('assets/tower/fire/fire_projectile.png').convert() 

        # Set the colorkey
        all_frames.set_colorkey((0, 0, 0))
        for i in range(8):
            frame = all_frames.subsurface(i * 32, 0, 32, 32)
            frame = pygame.transform.scale(frame, (48, 48))
            Fire_Ball.FIRE_BALL_ANIMATION.append(frame)
        
        # Impact Animation
        with open('assets/tower/fire/fire_impact.json') as f:
            Fire_Ball.FIRE_BALL_IMPACT_JSON = json.load(f)
        fire_impact_sheet = pygame.image.load('assets/tower/fire/fire_impact.png').convert_alpha()
        fire_impact_sheet.set_colorkey((0, 0, 0))
        Fire_Ball.FIRE_BALL_IMPACT = fire_impact_sheet

    
    def process(self):
        animation_list = []
        for j in range(len(self.current_json['frames'])):
            startX = self.current_json['frames'][f'fire_impact_{j+1:02d}.png']['frame']['x']
            startY = self.current_json['frames'][f'fire_impact_{j+1:02d}.png']['frame']['y']
            width = self.current_json['frames'][f'fire_impact_{j+1:02d}.png']['frame']['w']
            height = self.current_json['frames'][f'fire_impact_{j+1:02d}.png']['frame']['h']
            frame = self.FIRE_BALL_IMPACT.subsurface(startX, startY, width, height)
            animation_list.append(frame)
        return animation_list

    

           
   
    