import pygame
import constants as c
from Tower_Classes.tower_data import ARCHER_DATA
from Tower_Classes.tower_data import ZAP_DATA
from Tower_Classes.tower_data import CATAPULT_DATA

class Asset_Manager:
    def __init__(self):
        # Dictionary to find tower data by its base image
        self.towers = {}

        # Load Tower Assets
        self.load_tower_assets()

        # Load UI Assets
        self.coin = pygame.image.load('assets/icons/coins.png').convert_alpha()
        self.coin = pygame.transform.scale(self.coin, (40, 40))
        self.heart = pygame.image.load('assets/icons/heart.png').convert_alpha()
        self.heart = pygame.transform.scale(self.heart, (40, 24))
        
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
            current_image = pygame.image.load(f'assets/tower/archer/archer_{i}.png').convert_alpha()
            current_image = pygame.transform.scale(current_image, (48, 64))
            self.archer_base_image.append(current_image)
   
        
        self.towers[self.archer_base_image[0]] = [self.archer_base_image]
        
        ## Zap Tower
        self.zap_base_image = []
        for i in range(1, len(ZAP_DATA) + 1): 
            current_image = pygame.image.load(f'assets/tower/zap/zap_base_0{i}.png')
            current_image = pygame.transform.scale(current_image, (48, 64))
            self.zap_base_image.append(current_image)
 
            
        self.towers[self.zap_base_image[0]] = [self.zap_base_image]


        ## Catapult Tower
        self.catapult_base_image = []
        for i in range(1, len(CATAPULT_DATA) + 1): 
            current_image = pygame.image.load(f'assets/tower/catapult/catapult_base_0{i}.png')
            current_image = pygame.transform.scale(current_image, (48, 64))
            self.catapult_base_image.append(current_image)
      
            
        self.towers[self.catapult_base_image[0]] = [self.catapult_base_image]