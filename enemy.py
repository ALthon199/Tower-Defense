import pygame
import math
class Enemy(pygame.sprite.Sprite):
    def __init__(self, animation, total_frames, speed, waypoints):
        pygame.sprite.Sprite.__init__(self)
        self.animation = animation
        self.direction = 'down'
        self.frame = 0
        self.position = pygame.math.Vector2(waypoints[0])
        self.speed = speed
        self.waypoints = waypoints
        self.current_waypoint = 1
        self.image = self.animation[self.direction][self.frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position


    def move(self):
        self.image = self.animation[self.direction][self.frame]
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
        self.rect.center = self.position
        ## initialize a threshold value to move to next way point

        threshold = 5
        if self.position.distance_to(self.target) < threshold:
            self.current_waypoint += 1
        
        if self.current_waypoint >= len(self.waypoints):
            self.current_waypoint = 0

    def update(self):
        self.move()

    


    

        
