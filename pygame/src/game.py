import player
import world
import pygame

WHITE = (255, 255, 255)
running = True
clock = pygame.time.Clock()
FPS = 60

pygame.init()
pygame.display.set_caption("Roman's Game")
#create game world
world_ = world.World(1024, 800)
world_.set_background(pygame.image.load(world_.bckgr_img))
world_.set_background(pygame.transform.scale(world_.get_background(), (world_.width, world_.height)))
screen = pygame.display.set_mode((world_.width, world_.height))


player_ = player.Player(210, 210, 40, 100, world_)
player_.set_image(pygame.image.load(player_.img_file))
player_.set_image(pygame.transform.scale(player_.get_image(), (player_.width, player_.height)))
player_.set_rect(pygame.Rect(0, 0, 35, 80))

while running:
    clock.tick(FPS)
    player_.fall()
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player_.move_right()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player_.move_left()
    # if key[pygame.K_SPACE]:
    #     player_.jump()
    
    screen.blit(world_.get_background(), (0,0))
    screen.blit(pygame.transform.flip(player_.get_image(), player_.flip, False), (player_.get_rect().x, player_.get_rect().y-15))
    pygame.draw.rect(screen, WHITE, player_.get_rect(), 2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_.jump()
    pygame.display.update()