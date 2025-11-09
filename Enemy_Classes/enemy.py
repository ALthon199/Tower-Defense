import pygame
import math
class Enemy(pygame.sprite.Sprite):
    def __init__(self, animation_list, speed, waypoints, HP, value, armor, y_offset=0):
        pygame.sprite.Sprite.__init__(self)
        
        # Animation
        self.frame = 0
        self.animation = animation_list
        self.direction = 'down'
        
        # Position and Speed
        self.position = pygame.math.Vector2(waypoints[0])
        self.speed = speed
        self.waypoints = waypoints
        self.current_waypoint = 1

        # Drawing
        self.image = self.animation[self.direction][self.frame]
        self.y_offset = y_offset
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.position[0], self.position[1] + self.y_offset)

        # Game values
        self.hitbox = pygame.Rect(0,0,60,60)
        self.hitbox.center = self.rect.center
        self.time = 0
        self.current_HP = HP
        self.HP = HP
        self.armor = armor
        self.worth = value
        self.hpRect = pygame.Surface((60,10))
        self.hpOffset = (10,0)
       


    def draw(self, screen):
        percent_green = self.current_HP / self.HP
        width = self.hpRect.get_width()
        height = self.hpRect.get_height()
        self.hpRect.fill('Green', (0, 0, width * percent_green, height))
        self.hpRect.fill('Red', (width * percent_green, 0, width, height))
        screen.blit(self.image, self.rect)
        screen.blit(self.hpRect, (self.rect[0] + self.hpOffset[0], self.rect[1]))
        
    def move(self):
        self.image = self.animation[self.direction][self.frame]
        self.time += 1
        if self.time % 25 == 0:
            self.frame += 1
        if self.frame > len(self.animation[self.direction]) - 1:
            self.frame = 0
        
        self.target = pygame.math.Vector2(self.waypoints[self.current_waypoint])
        self.movement = self.target - self.position

        #Calculates direction of movement
        angle = math.atan2(self.movement[1], self.movement[0])
        angle = int(math.degrees(angle))
        
        if -45 <= angle < 45:
            self.direction = 'right'
        elif 45 <= angle < 135:
            self.direction = 'down'
        elif -135 <= angle <= -45:
            self.direction = 'up'
        else:
            self.direction = 'left'
        self.position += self.movement.normalize() * self.speed
        self.rect.midbottom = (self.position[0], self.position[1] + self.y_offset)
        self.hitbox.center = self.rect.center
        ## initialize a threshold value to move to next way point

        threshold = 5
        if self.position.distance_to(self.target) < threshold:
            self.current_waypoint += 1
        
        if self.current_waypoint >= len(self.waypoints):
            self.kill()
            return 'exited'
        
    def take_damage(self, damage):
        self.HP -= (damage - self.armor)        

    def update(self):
        if self.current_HP <= 0:
            self.kill()
            # Killing mob gives gold
            return 'died'
        
        if self.move() == 'exited':
            return 'exited'
        
    

    

        
