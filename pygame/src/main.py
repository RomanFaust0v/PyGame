import pygame

#initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Roman's Game")
running = True

player_img = pygame.image.load('assets/Player.png')
player_img = pygame.transform.scale(player_img, (40, 100))
player_location = [100, 100]

background = pygame.image.load('assets/background.png')
background = pygame.transform.scale(background, (800, 600))
backgroundX = 0
backgroundY = 0

def BG():
    screen.blit(background, (backgroundX, backgroundY))


moving_right = False
moving_left = False
moving_up = False
moving_down = False

# Game Loop
while running:
    screen.fill((0,0,0))
    BG()
    screen.blit(player_img, player_location)
    if moving_right == True:
        player_location[0] += 1
    if moving_left == True:
        player_location[0] -= 1
    if moving_up == True:
        player_location[1] -= 1
    if moving_down == True:
        player_location[1] += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False
                
    pygame.display.update()
