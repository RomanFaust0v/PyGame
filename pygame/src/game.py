import player as player
import world as world
import pygame
import ground as ground
from worldGenerator import generateLevel

running = True
clock = pygame.time.Clock()

#WORLD SETTINGS
WHITE = (255, 255, 255)
FPS = 60
PLAYER_HEIGHT = 83
PLAYER_WIDTH = 40
PLATFORM_HEIGHT = 40
PLATFORM_WIDTH = 40
WORLD_HEIGHT = 800
WORLD_WIDTH = 1024
world_ = None
player_ = None

#INITIALIZE PYGAME
pygame.init()
pygame.display.set_caption("Roman's Game")
screen = pygame.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))

#INITIALIZE GAME OBJECTS
def init_all():
    global world_, player_
    world_ = world.World(WORLD_WIDTH, WORLD_HEIGHT, 0, 0)
    player_ = player.Player(WORLD_WIDTH//2, WORLD_HEIGHT//2, PLATFORM_WIDTH, PLAYER_HEIGHT, world_)
    platform_group, level = generateLevel(WORLD_HEIGHT, WORLD_WIDTH, PLATFORM_HEIGHT, PLATFORM_WIDTH)
    world_.set_platforms(platform_group)
    world_.set_level(level)

init_all()

#GAME PROCESS
while running:
    clock.tick(FPS)
    player_.fall()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player_.move_right()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player_.move_left()
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        player_.get_down()
   
    world_.draw_object(screen)
    world_.get_platforms().draw(screen)
    player_.draw_player(screen)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_.jump()
            if event.key == pygame.K_r:
                init_all()
            if event.key == pygame.K_ESCAPE:
                running = False
                quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_.set_x_speed(0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_.set_x_speed(0)
    pygame.display.update()