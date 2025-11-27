import pygame
import constants as c
from Screen_Classes.Managers.wave_manager import Wave_Manager
from Enemy_Classes.zombie import Zombie
from Enemy_Classes.shield_zombie import Shield_Zombie
from Enemy_Classes.boss import Boss
from Tower_Classes.archer_tower import Archer_Tower
from Tower_Classes.zap_tower import Zap_Tower
from Tower_Classes.catapult_tower import Catapult_Tower
from Tower_Classes.tower_data import ARCHER_DATA
from Tower_Classes.tower_data import ZAP_DATA
from Tower_Classes.tower_data import CATAPULT_DATA
import functions

class GameState():
    def __init__(self, waypoints):
        # Game Variables
        self.placing_turrets = False
        self.current_gold = c.COINS 
        self.current_lives = c.LIVES
        
        # For ghost tower
        self.cursor_tower = None
        self.tower_cost = 0
        self.tower_range = 0
        self.cursor_surface = None

        # Create Groups
        self.enemy_map = {
            'Zombie': Zombie,
            'Shield_Zombie': Shield_Zombie,
            'Boss': Boss
        }
        self.enemy_group = pygame.sprite.Group()
        self.tower_group = pygame.sprite.LayeredUpdates()
        self.projectile_group = pygame.sprite.Group()

        # Wave Manager
        self.wave_manager = Wave_Manager(waypoints, self.enemy_group, self.enemy_map)

    def update_logic(self, current_time):
        # Update enemies/gold/lives
        for enemy in self.enemy_group:
            value = enemy.update()
            if value == 'died':
                self.current_gold += enemy.worth
            elif value == 'exited':
                self.current_lives -= 1
                
        # Update towers and projectiles
        self.tower_group.update(self.enemy_group)
        self.projectile_group.update(self.enemy_group)
        
        # Update waves and get gold
        self.current_gold += self.wave_manager.update(current_time)

    def check_win_condition(self):
        if len(self.enemy_group) == 0 and self.wave_manager.wave > len(self.wave_manager.wave_data):
            return True
        return False

    def start_placing(self, tower_type, assets):
        if tower_type == "archer":
            
            self.tower_cost = ARCHER_DATA[0].get('Cost')
            self.tower_range = ARCHER_DATA[0].get('Range')
            self.cursor_tower = assets.archer_base_image[0]
        elif tower_type == "zap":
            self.tower_cost = ZAP_DATA[0].get('Cost')
            self.tower_range = ZAP_DATA[0].get('Range')
            self.cursor_tower = assets.zap_base_image[0]

        elif tower_type == "catapult":
            self.tower_cost = CATAPULT_DATA[0].get('Cost')
            self.tower_range = CATAPULT_DATA[0].get('Range')
            self.cursor_tower = assets.catapult_base_image[0]
            
        
        self.placing_turrets = True
        self.cursor_surface = pygame.Surface((self.tower_range * 2, self.tower_range * 2), pygame.SRCALPHA)
        self.clear_select()

    def can_build(self, mouse_pos, world):
        mouse_tileX = mouse_pos[0] // c.TILE_SIZE
        mouse_tileY = mouse_pos[1] // c.TILE_SIZE

        occupied = False
        is_buildable = functions.checkBorder(world.tile_map, mouse_tileX, mouse_tileY)
        
        # Check if 3 by 3 spot is occupied already
        for tower in self.tower_group:
            if ( tower.tile_X - 2 <= mouse_tileX <= tower.tile_X + 2 and tower.tile_Y-2<=mouse_tileY <= tower.tile_Y + 2):
                occupied = True

        enough_gold = self.current_gold >= self.tower_cost
        return not (occupied or not is_buildable) and enough_gold

    def create_tower(self, mouse_pos, world, assets):
        mouse_tileX = mouse_pos[0] // c.TILE_SIZE 
        mouse_tileY = mouse_pos[1] // c.TILE_SIZE 
        
        is_allowed = self.can_build(mouse_pos, world)

        if is_allowed and self.cursor_tower == assets.archer_base_image[0]:
            if self.current_gold >= self.tower_cost: 
                new_tower = Archer_Tower(mouse_tileX, mouse_tileY, self.projectile_group)
                self.tower_group.add(new_tower)
                self.current_gold -= new_tower.cost
        
        elif is_allowed and self.cursor_tower == assets.zap_base_image[0]:
            if self.current_gold >= self.tower_cost:
                
                new_tower = Zap_Tower(mouse_tileX, mouse_tileY, self.projectile_group)
                self.tower_group.add(new_tower)
                self.current_gold -= new_tower.cost
        
        elif is_allowed and self.cursor_tower == assets.catapult_base_image[0]:
            if self.current_gold >= self.tower_cost:
                
                new_tower = Catapult_Tower(mouse_tileX, mouse_tileY, self.projectile_group)
                self.tower_group.add(new_tower)
                self.current_gold -= new_tower.cost

    def select_tower(self, mouse_pos):
        mouse_tileX = mouse_pos[0] // c.TILE_SIZE
        mouse_tileY = mouse_pos[1] // c.TILE_SIZE
        
        # Check if we clicked a tower
        clicked_tower = None
        for tower in self.tower_group:
            if (tower.tile_X - 2 <= mouse_tileX <= tower.tile_X + 2 and tower.tile_Y-2<=mouse_tileY <= tower.tile_Y + 2):
                clicked_tower = tower
                break
        
        if clicked_tower:
            if clicked_tower.is_selected:
                clicked_tower.is_selected = False
            else:
                self.clear_select()
                clicked_tower.is_selected = True
        else:
            # Clicked on grass, clear selection
            self.clear_select()

    def clear_select(self):
        for tower in self.tower_group:
            tower.is_selected = False