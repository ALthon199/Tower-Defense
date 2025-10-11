import pygame
from spritesheet import Enemy_SpriteSheet
from enemy import Enemy
from world import World
import constants as c
from tower import Tower
from button import Button
import json



pygame.init()
screen = pygame.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
clock = pygame.time.Clock()

#GAME VARIBLES
placing_turrets = False

#Load json data for level
with open('assets\maps\level.tmj') as file:
    world_data = json.load(file)

#Create World
map1_image = pygame.image.load('assets/maps/level.png') .convert_alpha()
world = World(world_data, map1_image)
world_data = world.process_data()
waypoints = world.waypoints


zombie_image = pygame.image.load('assets/sprites/walk.png')
zombie_scale = 1.25
# Width/Height of each zombie: frame is 64 x 64
zombie_sprite_sheet = Enemy_SpriteSheet(zombie_image, 64, 64, 'black', zombie_scale)

directions = 4
maxFrames = 9
zombieAnimation = zombie_sprite_sheet.animationList(maxFrames, directions)
all_values = list(zombieAnimation.values())

zombie = Enemy(zombieAnimation , 2, waypoints, c.HEALTH)
enemies = pygame.sprite.Group()
enemies.add(zombie)

# individual tower image for cursor
range = 100
cursor_tower = pygame.image.load('assets/turret/cursor_turret.png').convert_alpha()
cursor_surface = pygame.Surface((range * 2, range * 2), pygame.SRCALPHA)
pygame.draw.circle(cursor_surface, (211, 211, 211, 40), (range, range), range)
tower_group = pygame.sprite.Group()
turret_animations = pygame.image.load('assets/turret/turret_1.png').convert_alpha()



def create_tower(mouse_pos):
    mouse_tileX = mouse_pos[0] // c.TILE_SIZE
    mouse_tileY = mouse_pos[1] // c.TILE_SIZE
    #Calculate tile for tower
    tile = mouse_tileX + mouse_tileY * c.COLS
    if world.tile_map[tile] == 7:
        space = True
        #Check if turrent is already placed
        for tower in tower_group:
            if mouse_tileX == tower.tile_X and mouse_tileY == tower.tile_Y:
                space = False
            
        if space:
            new_tower = Tower(turret_animations, mouse_tileX, mouse_tileY, 200, c.DAMAGE)
            tower_group.add(new_tower)
def select_tower(mouse_pos):
    
    mouse_tileX = mouse_pos[0] // c.TILE_SIZE
    mouse_tileY = mouse_pos[1] // c.TILE_SIZE
    for tower in tower_group:
            if mouse_tileX == tower.tile_X and mouse_tileY == tower.tile_Y:      
                if tower.is_selected == True:
                    tower.is_selected = False
                else:
                    clear_select()
                    tower.is_selected = True

def clear_select():
    for tower in tower_group:
        tower.is_selected = False
                
            
# LOAD BUTTONS

buy_turret_image = pygame.image.load('assets/buttons/buy_turret.png')
cancel_buy_image = pygame.image.load('assets/buttons/cancel.png')

# CREATE BUTTONS
turret_button = Button(c.SCREEN_WIDTH + 30, 120, buy_turret_image, single_click= True)
cancel_button = Button(c.SCREEN_WIDTH + 50, 180, cancel_buy_image, single_click= True)
last_time = pygame.time.get_ticks()



running = True
while running:
    screen.fill('white')
    
    ## UPDATES ##

    #Update Animation
    current_time = pygame.time.get_ticks()
    enemies.update()
    tower_group.update(enemies)

    if len(enemies) < 20 and current_time - last_time > 750:
        zombie = Enemy(zombieAnimation , 2, waypoints, c.HEALTH)
        enemies.add(zombie)
        last_time = current_time
  

    
    
 
    ## DRAWINGS ##

    world.draw(screen)
    enemies.draw(screen)
    
    for tower in tower_group:
        tower.draw(screen)
    
    # Button
    if turret_button.draw(screen):
        placing_turrets = True

    if placing_turrets:
        # SHOW TURRET
        cursor_rect = cursor_tower.get_rect()
        cursor_pos = pygame.mouse.get_pos()
        cursor_rect.center = cursor_pos
        clear_select()

        # Check Bounds
        if cursor_pos[0] <= c.SCREEN_WIDTH:
            
            cursor_surface.blit(cursor_tower, (range//2, range//2))
            screen.blit(cursor_surface, (cursor_pos[0] - range , cursor_pos[1]- range))
        if cancel_button.draw(screen):
            placing_turrets = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            #Check if mouse in game area
            if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT and placing_turrets:
                create_tower(mouse_pos)
            else:
                select_tower(mouse_pos)
                
            



    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()