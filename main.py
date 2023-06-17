import pygame
from sys import exit

# to use pygame, we need to call init, this starts pygame
pygame.init()

# create a display surface, which is the window that the
# player sees + set_mode has to have at least one arg
screen = pygame.display.set_mode((800, 400))
# update our title
pygame.display.set_caption('gary the snail')
# add an icon
favicon = pygame.image.load('snorlax.png') 
pygame.display.set_icon(favicon)
# max frame rate
clock = pygame.time.Clock()
title = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = title.render('gary is passing by...', False, 'black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()

player_rect = player_surface.get_rect(midbottom = (80,300))
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

# create a while true loop to keep our display screen up
# we draw elements + update things in this while loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # constant
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    snail_rect.x -= 4
    if snail_rect.right < 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)

    player_rect.left += 4
    if player_rect.left > 800: player_rect.left = 0
    screen.blit(player_surface,player_rect)

    if player_rect.colliderect(snail_rect): print('collision!')
    # essential line bc it 
    # updates our display 
    pygame.display.update()
    clock.tick(60)