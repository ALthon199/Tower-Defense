import pygame
from spritesheet import SpriteSheet
from enemy import Enemy
pygame.init()
screen = pygame.display.set_mode((1024, 1024))
clock = pygame.time.Clock()


zombie_image = pygame.image.load('sprites/walk.png')
zombie_scale = 2
# Width/Height of each frame is 64 x 64
zombie_sprite_sheet = SpriteSheet(zombie_image, 64, 64, 'black', zombie_scale)

last_update = pygame.time.get_ticks()
animation_cooldown = 100
directions = 4
maxFrames = 9
zombieAnimation = zombie_sprite_sheet.animationList(maxFrames, directions)
all_values = list(zombieAnimation.values())
print(zombieAnimation)

waypoints = [(0, 0), (0, 600), (600, 600), (600, 200), (700, 200), (900, 200), (900, 100)]
zombie = Enemy(zombieAnimation, maxFrames , 5, waypoints)
enemies = pygame.sprite.Group()
enemies.add(zombie)


map1_image = pygame.image.load('sprites/map1.png') .convert_alpha()


running = True
while running:
    screen.fill('white')
    screen.blit(map1_image, (0,0))
    #Update Animation
    current_time = pygame.time.get_ticks()
    enemies.update()
    enemies.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()