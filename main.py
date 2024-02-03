import pygame
import os
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
screen = pygame.display.setmode((SCREEN_WIDTH,SCREEN_HEIGHT))
player = pygame.image.load(os.path.join("Assets", "Player.png"))
player = pygame.transform.scale(player, (600,600))

def draw_player(x, y):
    screen.blit(player, (x,y))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
