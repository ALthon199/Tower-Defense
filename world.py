import pygame 


class World():
    def __init__(self, data, map_image):
        self.level_data = data
        self.image = map_image
        self.tile_map = []
        self.waypoints = []
        

    def draw(self, surface):
        surface.blit(self.image, (0,0))
    
  
    def process_data(self):
        #Parse data for info
        for layer in self.level_data['layers']:
            
            if layer['name'] == 'tilemap':
                self.tile_map += layer['data']


            elif layer['name'] == 'waypoints':
                for obj in layer["objects"]:
                    waypoint_data = obj["polyline"]
                    self.process_waypoints(waypoint_data)
                
    def process_waypoints(self, waypoint_data):
        #Iterate through waypoints to extract (x,y)
        for point in waypoint_data:
            x, y = point.values()
            self.waypoints.append((x,y))
       