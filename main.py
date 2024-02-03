import pygame
import os
pygame.init()

    
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.image.load(os.path.join("Assets", "player.png"))
player = pygame.transform.scale(player, (100, 100))  # Adjusted the size for visibility
bg = pygame.image.load(os.path.join("Assets", "bg.png"))
bg = pygame.transform.scale(bg, (900, 700))
player_x = 400
player_y = 500

def draw_player(x, y):
    screen.blit(player, (x, y))

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(60)  # Set the frame rate to 60 frames per second
    screen.blit(bg, (0, 0))
    draw_player(player_x, player_y)
    speed = 5

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        player_x -= speed
    if pressed_keys[pygame.K_d]:
        player_x += speed
    if pressed_keys[pygame.K_w]:
        player_y -= speed
    if pressed_keys[pygame.K_s]:
        player_y += speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()