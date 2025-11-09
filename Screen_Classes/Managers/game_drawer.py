import pygame
import constants as c
from World_Classes.button import Button

class Game_Drawer():
    def __init__(self, assets):
        # Tower Upgrade/Cancel Buttons
        self.cancel_button = Button(c.SCREEN_WIDTH + 10, 300, assets.cancel_buy_image, single_click=True)
        self.upgrade_button = Button(c.SCREEN_WIDTH + 10, 600, assets.upgrade_image, single_click=True)

    def draw_all(self, screen, world, game_state, ui_manager, mouse_pos, assets):
        screen.fill('white')

        # World
        world.draw(screen)

       
        
        # 4. Draw Static UI (and check its clicks)
        ui_action = ui_manager.draw(screen, game_state, assets)
        




         # Games object
        for enemy in game_state.enemy_group:
            enemy.draw(screen)

        for tower in game_state.tower_group:
            tower.draw(screen)
        
        for projectile in game_state.projectile_group:
            projectile.draw(screen)

         # Game UI
        
        self.draw_placing_tower_ui(screen, game_state, mouse_pos, world)
        self.draw_selected_tower_ui(screen, game_state)

        
        return ui_action

    def draw_selected_tower_ui(self, screen, game_state):
        for tower in game_state.tower_group:
            if tower.is_selected:
                # Draw upgrade button
                if self.upgrade_button.draw(screen):
                    game_state.current_gold = tower.upgrade(game_state.current_gold)
                break # Only one can be selected

    def draw_placing_tower_ui(self, screen, game_state, mouse_pos, world):
        if game_state.placing_turrets:
            cursor_rect = game_state.cursor_tower.get_rect()
            cursor_rect.center = mouse_pos
            
            # Check Bounds
            if mouse_pos[0] <= c.SCREEN_WIDTH:
                # Get range and surface from game_state
                tower_range = game_state.tower_range
                cursor_surface = game_state.cursor_surface

                if not game_state.can_build(mouse_pos, world):
                    pygame.draw.circle(cursor_surface, (255, 0, 0, 40), (tower_range, tower_range), tower_range)
                else:
                    pygame.draw.circle(cursor_surface, (211, 211, 211, 40), (tower_range, tower_range), tower_range)
                
                cursor_surface.blit(game_state.cursor_tower, (tower_range - cursor_rect.width//2, tower_range - cursor_rect.width//2))
                screen.blit(cursor_surface, (mouse_pos[0] - tower_range, mouse_pos[1] - tower_range))
            
            # Draw cancel button
            if self.cancel_button.draw(screen):
                game_state.placing_turrets = False