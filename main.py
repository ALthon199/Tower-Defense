import pygame
from spritesheet import SpriteSheet
from enemy import Enemy
from world import World
import constants as c
import json



pygame.init()
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
clock = pygame.time.Clock()

#Load json data for level
with open('assets/maps/level.tmj') as file:
    world_data = json.load(file)

#Create World
map1_image = pygame.image.load('assets/maps/level.png') .convert_alpha()
world = World(world_data, map1_image)
world_data = world.process_data()
waypoints = world.process_waypoints(world_data)


zombie_image = pygame.image.load('assets/sprites/walk.png')
zombie_scale = 1.25
# Width/Height of each frame is 64 x 64
zombie_sprite_sheet = SpriteSheet(zombie_image, 64, 64, 'black', zombie_scale)

directions = 4
maxFrames = 9
zombieAnimation = zombie_sprite_sheet.animationList(maxFrames, directions)
all_values = list(zombieAnimation.values())

zombie = Enemy(zombieAnimation , 2, waypoints)
enemies = pygame.sprite.Group()
enemies.add(zombie)






running = True
while running:
    screen.fill('white')
    
    #Draw Level
    world.draw(screen)



    #Update Animation
    current_time = pygame.time.get_ticks()
    enemies.update()
    enemies.draw(screen)
    
    #DRAW HITBOXESSS
    for enemy in enemies:
        # Draw the hitbox rectangle (normal)
        pygame.draw.rect(screen, (0, 255, 0), enemy.rect, 2)
        
        # Draw a small circle at the center of the enemy rect
        center_pos = enemy.rect.center
        pygame.draw.circle(screen, (0, 0, 255), center_pos, 5) 
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()