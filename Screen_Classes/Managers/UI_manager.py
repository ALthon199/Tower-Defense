import pygame
import constants as c
from World_Classes.button import Button

class UI_Manager():
    def __init__(self, assets):
        # UI 
        self.resources_font = assets.resources_font
        self.wave_font = assets.wave_font
        self.coin = assets.coin
        self.heart = assets.heart

        # Create buttons
        self.archer_button = Button(c.SCREEN_WIDTH + 10, 120, assets.archer_base_image[0], single_click=True)
        self.zap_button = Button(c.SCREEN_WIDTH + 100, 120, assets.zap_base_image[0], single_click=True)
        self.catapult_button = Button(c.SCREEN_WIDTH + 190, 120, assets.catapult_base_image[0], single_click=True)
        self.exit_button = Button(c.SCREEN_WIDTH + 200, 300, assets.exit_image, single_click=True)

    def draw(self, screen, game_state, assets):

        # Draw buttons and check for clicks
        if self.exit_button.draw(screen):
            return 'home' 
        
        if self.archer_button.draw(screen):
            game_state.start_placing("archer", assets)
            
        if self.zap_button.draw(screen):
            game_state.start_placing("zap", assets)

        if self.catapult_button.draw(screen):
            game_state.start_placing("catapult", assets)

        # Game Variables

        # Draw Resources
        gold_surface = self.resources_font.render(f'Gold: {game_state.current_gold}', True, (255,223,0))
        screen.blit(gold_surface, (c.SCREEN_WIDTH - 100, 10))    
        screen.blit(self.coin, (c.SCREEN_WIDTH - 155, 0))
        lives_surface = self.resources_font.render(f'Lives: {game_state.current_lives}', True, (200,0,0))
        screen.blit(lives_surface, (c.SCREEN_WIDTH  - 100, 50))
        screen.blit(self.heart, (c.SCREEN_WIDTH  - 145, 45))
        
        # Game Info
        wave_surface = self.wave_font.render(f'Wave: {game_state.wave_manager.wave}', True, (100,0,0))
        screen.blit(wave_surface, (0,0))

        

        return None 