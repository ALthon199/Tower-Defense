import pygame
from Enemy_Classes.wave_data import WAVE_DATA
class Wave_Manager:
    def __init__(self, waypoints, enemy_group, enemy_class_map):
        self.waypoints = waypoints
        self.enemy_group = enemy_group  
        self.wave_data = WAVE_DATA
        self.enemy_class_map = enemy_class_map

        self.wave = 1
        self.current_wave_config = self.wave_data.get(f'wave_{self.wave}')
        self.wave_start_time = 0
        self.spawn_counter = {}
       

    def update(self, current_time):
        reward = 0
        if len(self.enemy_group) == 0 and self.wave_start_time == 0:
            
            self.wave_start_time = current_time
            
            for i in range(len(self.current_wave_config.get('spawn_events'))):
                self.spawn_counter[i] = {'count': 0, 'last_spawn' : 0}

        
        if self.wave_start_time > 0:
            
            time_after = pygame.time.get_ticks() - self.wave_start_time
            sub_waves = self.current_wave_config.get('spawn_events')

            for i, event in enumerate(sub_waves):
                mob_type = event['mob_type']
                if time_after < event.get('start_time') * 1000:
                    continue
                current_count = self.spawn_counter[i].get('count')
                

                if current_count >= event.get('count'):
                    continue

                
                last_spawn = pygame.time.get_ticks() - self.spawn_counter[i]['last_spawn']

                if last_spawn >= event.get('spawn_delay') * 1000:
                    enemy = self.enemy_class_map[mob_type](self.waypoints)     
                    self.enemy_group.add(enemy)
                    
                    self.spawn_counter[i]['count'] += 1
                    self.spawn_counter[i]['last_spawn'] = pygame.time.get_ticks()

            if current_time - self.wave_start_time >= self.current_wave_config.get('duration') * 1000 and len(self.enemy_group) == 0:
                reward = self.current_wave_config.get('reward')
                self.wave += 1
                self.wave_start_time = 0
                self.current_wave_config = self.wave_data.get(f'wave_{self.wave}')
                self.spawn_counter = {}

            return reward
    def get_wave_description(self):
        if self.current_wave_config:
            
            return self.current_wave_config['description']
        return ''