import pygame
import constants as c
from Tower_Classes.tower_data import ARCHER_DATA
from Tower_Classes.tower_data import ZAP_DATA

class Asset_Manager:
    def __init__(self):
        # Dictionary to find tower data by its base image
        self.towers = {}

        # Load Tower Assets
        self.load_tower_assets()

        # Load UI Assets
        self.coin = pygame.image.load('assets/icons/coins.png').convert_alpha()
        self.coin = pygame.transform.scale(self.coin, (40, 40))
        
        self.cancel_buy_image = pygame.image.load('assets/buttons/cancel.png').convert_alpha()
        self.upgrade_image = pygame.image.load('assets/buttons/upgrade.png').convert_alpha()
        self.upgrade_image = pygame.transform.scale(self.upgrade_image, (50, 50))
        self.exit_image = pygame.image.load('assets/buttons/exit.png').convert_alpha()
        self.exit_image = pygame.transform.scale(self.exit_image, (50, 50))
        
        self.map1_image = pygame.image.load('assets/maps/map1.png').convert_alpha()
        
        # Load Fonts
        self.resources_font = pygame.font.SysFont('Calibri', 20, bold=True)
        self.wave_font = pygame.font.SysFont('Calibri', 40, bold=True)

    def load_tower_assets(self):
        ## Archer Tower
        self.archer_base_image = []
        for i in range(1, len(ARCHER_DATA) + 1):
            current_image = pygame.image.load(f'assets/turret/archer/archer_{i}.png').convert_alpha()
            current_image = pygame.transform.scale(current_image, (48, 64))
            self.archer_base_image.append(current_image)
        # Shooting 
        self.archer_animations = []
        for i in range(1, len(ARCHER_DATA) + 1):
            current_animation = pygame.image.load(f'assets/turret/archer/archer_weapon0{i}.png').convert_alpha()
            self.archer_animations.append(current_animation)
        # Arrow
        self.arrow_animation = []
        for i in range(1, len(ARCHER_DATA) + 1):
            archer_animation = pygame.image.load(f'assets/turret/archer/archer_animation0{i}.png').convert_alpha()
            self.arrow_animation.append(archer_animation)
        
        self.towers[self.archer_base_image[0]] = [self.archer_base_image, self.archer_animations]
        
        ## Zap Tower
        self.zap_base_image = []
        for i in range(1, len(ZAP_DATA) + 1): 
            current_image = pygame.image.load(f'assets/turret/zap/zap_base_0{i}.png')
            current_image = pygame.transform.scale(current_image, (48, 64))
            self.zap_base_image.append(current_image)
        # Shooting 
        self.zap_animations = []
        for i in range(1, len(ZAP_DATA) + 1):
            current_animation = pygame.image.load(f'assets/turret/zap/zap_weapon_0{i}.png').convert_alpha()
            self.zap_animations.append(current_animation)
        # Lightning
        self.lightning_animation = []
        for i in range(1, len(ZAP_DATA) + 1): 
            lightning_animation = pygame.image.load(f'assets/turret/zap/zap_projectile_0{i}.png').convert_alpha()
            self.lightning_animation.append(lightning_animation)
            
        self.towers[self.zap_base_image[0]] = [self.zap_base_image, self.zap_animations]