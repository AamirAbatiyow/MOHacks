import pygame
import os
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
player = pygame.image.load(os.path.join("Assets", "Player.png"))
player = pygame.transform.scale(player, (600,600))

def draw_player(x, y):
    screen.blit(player, (x,y))
run = True
while run:
    draw_player(400,500)
    speed = 3
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        player_x = player_x - speed
    if pressed_keys[pygame.K_d]:
        player_x = player_x + speed
    if pressed_keys[pygame.K_w]:
        player_y = player_y - speed
    if pressed_keys[pygame.K_s]:
        player_y = player_y + speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
