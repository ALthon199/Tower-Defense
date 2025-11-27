import pygame
import sys
import json
import constants as c

# Import all the new classes
from Screen_Classes.Managers.asset_manager import Asset_Manager
from Screen_Classes.Managers.game_state import GameState
from Screen_Classes.Managers.UI_manager import UI_Manager
from Screen_Classes.Managers.game_drawer import Game_Drawer
from World_Classes.world import World

class Game_Screen():
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.mouse_pos = (0, 0)
        
        #Load all assets
        self.assets = Asset_Manager()

        #Create world
        self.world = self.create_world()

        #Create game components
        self.game_state = GameState(self.world.waypoints)
        self.ui_manager = UI_Manager(self.assets)
        self.renderer = Game_Drawer(self.assets)


        #
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 16)


    def run(self):
        while self.running:
            
            self.mouse_pos = pygame.mouse.get_pos()
            self.current_time = pygame.time.get_ticks()

           



            
            self.handle_events()
            
            # Update
            self.game_state.update_logic(self.current_time)

            # Draw
            ui_action = self.renderer.draw_all(
                self.screen, 
                self.world, 
                self.game_state, 
                self.ui_manager, 
                self.mouse_pos,
                self.assets
            )

            # Check State
            if ui_action == 'home':
                return 'home' # Go back to home screen
            
            if self.game_state.current_lives < 1:
                return 'lost' # Go to game over screen

            if self.game_state.check_win_condition():
                return 'won' # Go to win screen
            

            coord_text = f"self.mouse_pos: {self.mouse_pos[0]}, {self.mouse_pos[1]}"
            text_surface = self.font.render(coord_text, True, (0,0,0)) # (text, antialias, color)
            text_rect = text_surface.get_rect(topleft=(self.mouse_pos[0] + 10, self.mouse_pos[1] + 10))
            self.screen.blit(text_surface, text_rect)


            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if mouse in game area
                if self.mouse_pos[0] < c.SCREEN_WIDTH and self.mouse_pos[1] < c.SCREEN_HEIGHT:
                    
                    if self.game_state.placing_turrets:
                        # Pass assets to know which tower is being built
                        self.game_state.create_tower(self.mouse_pos, self.world, self.assets)
                    else:
                        self.game_state.select_tower(self.mouse_pos)
                
                

    def create_world(self):
        with open('assets/maps/map1.tmj') as file:
            world_data = json.load(file)
            
        world = World(world_data, self.assets.map1_image)
        world.process_data()
        return world
    
    