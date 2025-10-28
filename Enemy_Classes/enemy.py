import pygame
import math
class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, speed, waypoints, HP, value, scale, color):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = sprite_sheet
        self.color = color
        self.scale = scale
        self.size = 64
        self.frame = 0
        self.animation = self.process_sheet()
        self.direction = 'down'
        


        self.position = pygame.math.Vector2(waypoints[0])
        self.speed = speed
        self.waypoints = waypoints
        self.current_waypoint = 1


        self.image = self.animation[self.direction][self.frame]
        self.rect = self.image.get_rect()
        
        self.rect.topleft = self.position


        self.hitbox = pygame.Rect(0,0,60,60)
        self.hitbox.center = self.position
        self.time = 0
        self.HP = HP
        self.worth = value


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
        self.rect.center = self.position
        ## initialize a threshold value to move to next way point

        threshold = 5
        if self.position.distance_to(self.target) < threshold:
            self.current_waypoint += 1
        
        if self.current_waypoint >= len(self.waypoints):
            self.kill()
            return 'exited'
        
            

    def update(self):
        if self.HP < 0:
            self.kill()
            # Killing mob gives gold
            return 'died'
        
        if self.move() == 'exited':
            return 'exited'
        
    def get_image(self, frames, rows):
        # Creates canvas for sprite
        # ZOmbies are 64 NEEED FIX
        
        image = pygame.Surface((64, 64)).convert_alpha() 
        image.blit(self.sprite_sheet, (0, 0), ((self.size * frames), (self.size * rows ), self.size, self.size))
        image = pygame.transform.scale(image, (self.size * self.scale, self.size * self.scale))
        # Removes any background color if present
        image.set_colorkey(self.color)

        return image

    def process_sheet(self):
        directions = ['up', 'left', 'down', 'right']
        animation = {}
        ## 4 by 8 sprite_sheet
        rows = 4
        frames = 9
        for row in range(rows):
            direction = directions[row]
            animation[direction] = []
            for frame in range(frames):
                image = self.get_image(frame, row)
                animation[direction].append(image)
        return animation
        


    

        
