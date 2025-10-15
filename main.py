import pygame
from spritesheet import Enemy_SpriteSheet
from enemy import Enemy
from world import World
import constants as c
from tower import Tower
from button import Button
from tower_data import TOWER_DATA
from wave_data import WAVE_DATA
import json

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
clock = pygame.time.Clock()

#GAME VARIBLES
placing_turrets = False
current_gold = c.COINS
wave = 1
wave_time = pygame.time.get_ticks()
current_wave = WAVE_DATA.get(f'wave_{wave}')
wave_start_time = 0
spawn_counter = {}
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



enemies = pygame.sprite.Group()


# individual tower image for cursor
RANGE = TOWER_DATA[0].get('Range')
cursor_tower = pygame.image.load('assets/turret/cursor_turret.png').convert_alpha()
cursor_surface = pygame.Surface((RANGE * 2, RANGE * 2), pygame.SRCALPHA)
pygame.draw.circle(cursor_surface, (211, 211, 211, 40), (RANGE, RANGE), RANGE)
tower_group = pygame.sprite.Group()

turret_animations = []
for i in range(1, len(TOWER_DATA) + 1):
    
    current_animation = pygame.image.load(f'assets/turret/turret_{i}.png').convert_alpha()
    turret_animations.append(current_animation)





# icon images
coin = pygame.image.load('assets/icons/coins.png').convert_alpha()
coin = coin.convert_alpha()
coin = pygame.transform.scale(coin, (40, 40))

def create_tower(mouse_pos):
    global current_gold
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
                
            
        if space and current_gold >= c.TURRET_COST:
            new_tower = Tower(turret_animations, mouse_tileX, mouse_tileY,  c.TURRET_COST)
            tower_group.add(new_tower)
            current_gold -= new_tower.cost

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

buy_turret_image = pygame.image.load('assets/buttons/buy_turret.png').convert_alpha()
cancel_buy_image = pygame.image.load('assets/buttons/cancel.png').convert_alpha()
upgrade_image = pygame.image.load('assets/buttons/upgrade.png').convert_alpha()
upgrade_image = pygame.transform.scale(upgrade_image, (50, 50))

# CREATE BUTTONS
turret_button = Button(c.SCREEN_WIDTH + 10, 120, buy_turret_image, single_click= True)
cancel_button = Button(c.SCREEN_WIDTH + 10, 180, cancel_buy_image, single_click= True)
upgrade_button = Button(c.SCREEN_WIDTH + 10, 600, upgrade_image, single_click = True)




running = True
while running:
    
    screen.fill('white')
       

    if turret_button.draw(screen):
        placing_turrets = True

    world.draw(screen)

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

    
    ## UPDATES ##


    #Update Animation
    current_time = pygame.time.get_ticks()

    for enemy in enemies:
        # Updates and checks if killed
        value = enemy.update()
        if value:
            current_gold += value

    tower_group.update(enemies)
   
    
    if len(enemies) == 0 and wave_start_time == 0:
        
        wave_start_time = current_time
        
        for i in range(len(current_wave.get('spawn_events'))):
            spawn_counter[i] = {'count': 0, 'last_spawn' : 0}

    
    if wave_start_time > 0:
        
        time_after = pygame.time.get_ticks() - wave_start_time
        sub_waves = current_wave.get('spawn_events')

        for i, event in enumerate(sub_waves):
            if time_after < event.get('start_time') * 1000:
                continue
            current_count = spawn_counter[i].get('count')
            

            if current_count >= event.get('count'):
                continue

            
            last_spawn = pygame.time.get_ticks() - spawn_counter[i]['last_spawn']

            if last_spawn >= event.get('spawn_delay') * 1000:
                
                zombie = Enemy(zombieAnimation, 8, waypoints, c.HEALTH, c.DEATH_GOLD)
                enemies.add(zombie)
                
                spawn_counter[i]['count'] += 1
                spawn_counter[i]['last_spawn'] = pygame.time.get_ticks()

        if current_time - wave_start_time >= current_wave.get('duration') * 1000:
            
            current_gold += current_wave.get('reward')
            wave += 1
            wave_time = pygame.time.get_ticks()
            current_wave = WAVE_DATA.get(f'wave_{wave}')
            wave_start_time = 0
            spawn_counter = {}
            
    
   

 


  
    ## DRAWINGS ##
    
    enemies.draw(screen)
    for tower in tower_group:
        tower.draw(screen)
        if not tower.is_selected:
            continue
        elif upgrade_button.draw(screen):
            ## Upgrades Turrent and updates current gold
            current_gold = tower.upgrade(current_gold)
            

    if placing_turrets:
        # SHOW TURRET
        cursor_rect = cursor_tower.get_rect()
        cursor_pos = pygame.mouse.get_pos()
        cursor_rect.center = cursor_pos
        clear_select()

        # Check Bounds
        if cursor_pos[0] <= c.SCREEN_WIDTH:
            cursor_surface.blit(cursor_tower, (RANGE//2, RANGE//2))
            screen.blit(cursor_surface, (cursor_pos[0] - RANGE , cursor_pos[1]- RANGE))

        if cancel_button.draw(screen):
            placing_turrets = False


    screen.blit(coin, (800, 800))
    
    # Fonts
    coin_font = pygame.font.SysFont('Calibri', 20, bold = True)
    coin_surface = coin_font.render(f'{current_gold}', True, (0, 0, 0))
    screen.blit(coin, (c.SCREEN_WIDTH, 0))
    screen.blit(coin_surface, (c.SCREEN_WIDTH + coin.get_width(), 10))

    wave_font = pygame.font.SysFont('Calibri', 40, bold = True)
    wave_surface = wave_font.render(f'Wave: {wave}', True, (100,0,0))
    screen.blit(wave_surface, (0,0) )

    
    


    




    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()