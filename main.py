import pygame
import os
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
screen = pygame.display.setmode((SCREEN_WIDTH,SCREEN_HEIGHT))
#smile_ball = pygame.image.load(os.path.join("Assets", "Ball.jpg"))
#smile_ball = pygame.transform.scale(smile_ball, (600,600))

#def draw_ball(x, y):
#    screen.blit(smile_ball, (x,y))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
