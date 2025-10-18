import pygame
import sys # Needed for sys.exit()
import json
from enemy import Enemy
from world import World
import constants as c
from tower import Tower
from button import Button
from tower_data import TOWER_DATA
from wave_data import WAVE_DATA
class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL , c.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        #GAME VARIBLES
        self.placing_turrets = False
        self.current_gold = c.COINS
        self.current_lives = c.LIVES
        self.wave = 1
        
        self.current_wave = WAVE_DATA.get(f'wave_{self.wave}')
        self.wave_start_time = 0
        self.spawn_counter = {}
        self.running = True
        self.mouse_pos = pygame.mouse.get_pos()


        #Load Assets
        self.load_assets()
        self.create_buttons()
        self.create_world()
        self.create_groups()
        
            


       
        self.zombie_scale = 1.25
       


        # individual tower image for cursor
        self.RANGE = TOWER_DATA[0].get('Range')
        self.cursor_surface = pygame.Surface((self.RANGE * 2, self.RANGE * 2), pygame.SRCALPHA)


    def run(self):
        while self.running:
            self.mouse_pos = pygame.mouse.get_pos()
            self.current_time = pygame.time.get_ticks()
            self.handle_events()
            self.update()           
            self.draw()


            self.screen.blit(self.coin, (800, 800))
            
            # Fonts
            self.resources_font = pygame.font.SysFont('Calibri', 20, bold = True)
            self.resources_surface = self.resources_font.render(f'{self.current_gold} \n {self.current_lives}', True, (0, 0, 0))
            self.screen.blit(self.coin, (c.SCREEN_WIDTH, 0))
            self.screen.blit(self.resources_surface, (c.SCREEN_WIDTH + self.coin.get_width(), 10))


            self.wave_font = pygame.font.SysFont('Calibri', 40, bold = True)
            self.wave_surface = self.wave_font.render(f'Wave: {self.wave}', True, (100,0,0))
            self.screen.blit(self.wave_surface, (0,0) )
            
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def draw(self):
        
        self.screen.fill('white')
            
           
        if self.turret_button.draw(self.screen):
            
            self.placing_turrets = True

        self.world.draw(self.screen)
        
        self.enemy_group.draw(self.screen)

        for tower in self.tower_group:
            tower.draw(self.screen)
            if not tower.is_selected:
                continue
            elif self.upgrade_button.draw(self.screen):
                ## Upgrades Turrent and updates current gold
                self.current_gold = tower.upgrade(self.current_gold)
                    

        if self.placing_turrets:
            
            # SHOW TURRET
            cursor_rect = self.cursor_tower.get_rect()
           
            cursor_rect.center = self.mouse_pos
            
            self.clear_select()
        
            # Check Bounds
            if self.mouse_pos[0] <= c.SCREEN_WIDTH:
                
                # Check if tile is occupied
                mouse_tileX = self.mouse_pos[0] // c.TILE_SIZE
                mouse_tileY = self.mouse_pos[1] // c.TILE_SIZE
                space = True
                
                for tower in self.tower_group:
                    if mouse_tileX == tower.tile_X and mouse_tileY == tower.tile_Y:
                        
                        space = False
                        pygame.draw.circle(self.cursor_surface, (255, 0, 0, 40), (self.RANGE, self.RANGE), self.RANGE)      
                        self.cursor_surface.blit(self.cursor_tower, (self.RANGE//2 + cursor_rect.width//2,self.RANGE//2 + cursor_rect.width//2))
                        self.screen.blit(self.cursor_surface, (self.mouse_pos[0] - self.RANGE , self.mouse_pos[1]- self.RANGE))
                        

                if space:
                    pygame.draw.circle(self.cursor_surface, (211, 211, 211, 40), (self.RANGE, self.RANGE), self.RANGE)
                    self.cursor_surface.blit(self.cursor_tower, (self.RANGE//2 + cursor_rect.width//2,self.RANGE//2 + cursor_rect.width//2))
                    self.screen.blit(self.cursor_surface, (self.mouse_pos[0] - self.RANGE , self.mouse_pos[1]- self.RANGE))


            

            if self.cancel_button.draw(self.screen):
                
                self.placing_turrets = False

    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    #Check if mouse in game area
                    if self.mouse_pos[0] < c.SCREEN_WIDTH and self.mouse_pos[1] < c.SCREEN_HEIGHT and self.placing_turrets:
                        self.create_tower(self.mouse_pos)
                    else:
                        self.select_tower(self.mouse_pos)

    def update(self):
        for enemy in self.enemy_group:
                # Updates and checks if killed
                value = enemy.update()
                if value == 'died':
                    self.current_gold += enemy.worth
                elif value == 'exited':
                    self.current_lives -= 1
            
        self.tower_group.update(self.enemy_group)
        
            
        if len(self.enemy_group) == 0 and self.wave_start_time == 0:
            
            self.wave_start_time = self.current_time
            
            for i in range(len(self.current_wave.get('spawn_events'))):
                self.spawn_counter[i] = {'count': 0, 'last_spawn' : 0}

        
        if self.wave_start_time > 0:
            
            time_after = pygame.time.get_ticks() - self.wave_start_time
            sub_waves = self.current_wave.get('spawn_events')

            for i, event in enumerate(sub_waves):
                if time_after < event.get('start_time') * 1000:
                    continue
                current_count = self.spawn_counter[i].get('count')
                

                if current_count >= event.get('count'):
                    continue

                
                last_spawn = pygame.time.get_ticks() - self.spawn_counter[i]['last_spawn']

                if last_spawn >= event.get('spawn_delay') * 1000:
                    
                    zombie = Enemy(self.zombie_image, 3, self.waypoints, c.HEALTH, c.DEATH_GOLD, self.zombie_scale, (0, 0, 0))
                    self.enemy_group.add(zombie)
                    
                    self.spawn_counter[i]['count'] += 1
                    self.spawn_counter[i]['last_spawn'] = pygame.time.get_ticks()

            if self.current_time - self.wave_start_time >= self.current_wave.get('duration') * 1000 and len(self.enemy_group) == 0:
                
                self.current_gold += self.current_wave.get('reward')
                self.wave += 1
                self.wave_start_time = 0
                self.current_wave = WAVE_DATA.get(f'wave_{self.wave}')
                self.spawn_counter = {}
    def create_tower(self, mouse_pos):
        
        mouse_tileX = mouse_pos[0] // c.TILE_SIZE 
        mouse_tileY = mouse_pos[1] // c.TILE_SIZE 
        #Calculate tile for tower
        tile = mouse_tileX + mouse_tileY * c.COLS
        
        if self.world.tile_map[tile] == 18:
            space = True
            
            #Check if turrent is already placed
            for tower in self.tower_group:
                if mouse_tileX == tower.tile_X and mouse_tileY == tower.tile_Y:
                    space = False
                    
                
            if space and self.current_gold >= c.TURRET_COST:
                new_tower = Tower(self.turretbase_image, self.turret_animations, 12, mouse_tileX, mouse_tileY,  c.TURRET_COST)
                
                self.tower_group.add(new_tower)
                self.current_gold -= new_tower.cost

    def select_tower(self,mouse_pos):
        
        mouse_tileX = mouse_pos[0] // c.TILE_SIZE
        mouse_tileY = mouse_pos[1] // c.TILE_SIZE
        for tower in self.tower_group:
                if mouse_tileX == tower.tile_X and mouse_tileY == tower.tile_Y:      
                    if tower.is_selected == True:
                        tower.is_selected = False
                    else:
                        self.clear_select()
                        tower.is_selected = True

    def clear_select(self):
        for tower in self.tower_group:
            tower.is_selected = False

    

    def load_assets(self):
        self.cursor_tower = pygame.image.load('assets/turret/archer_1.png').convert_alpha()
        self.cursor_tower = pygame.transform.scale(self.cursor_tower, (48, 64))

        self.turretbase_image = []
        for i in range(1, len(TOWER_DATA)):
            current_image = pygame.image.load(f'assets/turret/archer_{i}.png').convert_alpha()
            current_image = pygame.transform.scale(self.cursor_tower, (48, 64))
            self.turretbase_image.append(current_image)
        self.turret_animations = []
        for i in range(1, len(TOWER_DATA) + 1):
            current_animation = pygame.image.load(f'assets/turret/archer_weapon0{i}.png').convert_alpha()
            self.turret_animations.append(current_animation)

        self.coin = pygame.image.load('assets/icons/coins.png').convert_alpha()
        self.coin = pygame.transform.scale(self.coin, (40, 40))
        self.buy_turret_image = pygame.image.load('assets/buttons/buy_turret.png').convert_alpha()
        self.cancel_buy_image = pygame.image.load('assets/buttons/cancel.png').convert_alpha()
        self.upgrade_image = pygame.image.load('assets/buttons/upgrade.png').convert_alpha()
        self.upgrade_image = pygame.transform.scale(self.upgrade_image, (50, 50))


        self.zombie_image = pygame.image.load('assets/sprites/walk.png')

        self.map1_image = pygame.image.load('assets/maps/map1.png') .convert_alpha()

    def create_buttons(self):
        self.turret_button = Button(c.SCREEN_WIDTH + 10, 120, self.buy_turret_image, single_click= True)
        self.cancel_button = Button(c.SCREEN_WIDTH + 10, 180, self.cancel_buy_image, single_click= True)
        self.upgrade_button = Button(c.SCREEN_WIDTH + 10, 600, self.upgrade_image, single_click = True)

    def create_world(self):
        with open('assets\maps\map1.tmj') as file:
            self.world_data = json.load(file)
            
        self.world = World(self.world_data, self.map1_image)
        self.world.process_data()
        self.waypoints = self.world.waypoints

    def create_groups(self):
        self.enemy_group = pygame.sprite.Group()
        self.tower_group = pygame.sprite.Group()

    

