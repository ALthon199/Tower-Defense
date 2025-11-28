import pygame
import constants as c
from World_Classes.button import Button
from Tower_Classes.tower_data import ARCHER_DATA, ZAP_DATA, CATAPULT_DATA
class UI_Manager():
    def __init__(self, assets):
        # UI 
        self.resources_font = assets.resources_font
        self.wave_font = assets.wave_font
        self.coin = assets.coin
        self.heart = assets.heart

        # Create buttons
        self.archer_button = Button(c.SCREEN_WIDTH + 50, 100, assets.archer_base_image[0], single_click=True)
        self.zap_button = Button(c.SCREEN_WIDTH + 190, 100, assets.zap_base_image[0], single_click=True)
        self.catapult_button = Button(c.SCREEN_WIDTH + 50, 230, assets.catapult_base_image[0], single_click=True)
        self.fire_button = Button(c.SCREEN_WIDTH + 190, 230, assets.fire_base_image[0], single_click=True)

        self.exit_button = Button(c.SCREEN_WIDTH + 200, 600, assets.exit_image, single_click=True)

    def draw(self, screen, game_state, assets):
        
        # Draw Purchase UI
        screen.blit(assets.purchase_panel, (c.SCREEN_WIDTH, 0))

        # Draw buttons and check for clicks
        if self.exit_button.draw(screen):
            return 'home' 
        
        if self.archer_button.draw(screen):
            game_state.start_placing("archer", assets)
            
        if self.zap_button.draw(screen):
            game_state.start_placing("zap", assets)

        if self.catapult_button.draw(screen):
            game_state.start_placing("catapult", assets)


        if self.fire_button.draw(screen):
            game_state.start_placing("fire", assets)
        

        
        self.draw_game_info(screen, game_state)
        return None 
    
    def draw_game_info(self, screen, game_state):

        # Draw Resources
        gold_surface = self.resources_font.render(f'Gold: {game_state.current_gold}', True, (255,223,0))
        screen.blit(gold_surface, (c.SCREEN_WIDTH - 100, 10))    
        screen.blit(self.coin, (c.SCREEN_WIDTH - 155, 0))
        lives_surface = self.resources_font.render(f'Lives: {game_state.current_lives}', True, (200,0,0))
        screen.blit(lives_surface, (c.SCREEN_WIDTH  - 100, 50))
        screen.blit(self.heart, (c.SCREEN_WIDTH  - 145, 45))

        # Game variables
        wave_surface = self.wave_font.render(f'Wave: {game_state.wave_manager.wave}', True, (255,0,0))
        screen.blit(wave_surface, (0,0))
        wave_info = self.resources_font.render(f'Enemies Left: {len(game_state.enemy_group)}', True, (255,0,0))
        screen.blit(wave_info, (0,40))

        wave_descripton = self.resources_font.render(f'{game_state.wave_manager.get_wave_description()}', True, (255,255,100))
        screen.blit(wave_descripton, (0,770))


        # Draw Tower costs
        archer_cost = ARCHER_DATA[0].get('Cost')
        archer_cost_surface = self.resources_font.render(f'Cost: {archer_cost}', True, (0,0,0))
        screen.blit(archer_cost_surface, (1060, 180))
        zap_cost = ZAP_DATA[0].get('Cost')
        zap_cost_surface = self.resources_font.render(f'Cost: {zap_cost}', True, (0,0,0))
        screen.blit(zap_cost_surface, (1200, 180))   
        catapult_cost = CATAPULT_DATA[0].get('Cost')
        catapult_cost_surface = self.resources_font.render(f'Cost: {catapult_cost}', True, (0,0,0))
        screen.blit(catapult_cost_surface, (1060, 310))
        fire_cost = CATAPULT_DATA[0].get('Cost')
        fire_cost_surface = self.resources_font.render(f'Cost: {fire_cost}', True, (0,0,0))
        screen.blit(fire_cost_surface, (1200, 310))
       