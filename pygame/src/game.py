import player
import world
import pygame
import ground
import random

WHITE = (255, 255, 255)
running = True
clock = pygame.time.Clock()
FPS = 60

pygame.init()
pygame.display.set_caption("Roman's Game")
#create game world
world_ = world.World(1024, 800, 0, 0)
player_ = player.Player(210, 210, 40, 100, world_)
platform_ = ground.Platform(500, 500, 30, 30)

platform_group = pygame.sprite.Group()
for p in range(world_.get_max_platforms()):
    p_x = random.randint(0, world_.width-130)
    p_y = random.randint(30, 60)*p
    platform = ground.Platform(p_x, p_y, 130, 30)
    platform_group.add(platform)

screen = pygame.display.set_mode((world_.width, world_.height))

while running:
    clock.tick(FPS)
    player_.fall()
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player_.move_right()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player_.move_left()
    
    world_.draw_object(screen)
    player_.draw_player(screen)
    # platform_.draw_object(screen)
    platform_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_.jump()
    
    pygame.display.update()