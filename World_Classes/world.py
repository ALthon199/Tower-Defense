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
            
            if layer['name'] == 'Buildable':
                self.tile_map += layer['data']


            elif layer['name'] == 'Pathway':
                for obj in layer["objects"]:
                    waypoint_data = obj["polyline"]
                    offset_x, offset_y =  obj['x'], obj['y']
                    self.process_waypoints(waypoint_data, offset_x, offset_y)
                
    def process_waypoints(self, waypoint_data, offset_x, offset_y):
        #Iterate through waypoints to extract (x,y)
        for point in waypoint_data:
            x, y = point.values()
            self.waypoints.append((offset_x + x,offset_y + y))
       