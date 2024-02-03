import pygame
import os
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
screen = pygame.display.setmode((SCREEN_WIDTH,SCREEN_HEIGHT))
<<<<<<< HEAD
player = pygame.image.load(os.path.join("Assets", "Player.png"))
player = pygame.transform.scale(player, (600,600))

def draw_player(x, y):
    screen.blit(player, (x,y))
=======
player_sprite = pygame.image.load(os.path.join("Assets", "Ball.jpg"))
player_sprite = pygame.transform.scale(player_sprite, (600,600))

def draw_ball(x, y):
    screen.blit(player_sprite, (x,y))
>>>>>>> b7266c8090422ea2cee31905d64916ba45609a3f
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
