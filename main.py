import pygame
import os

pygame.init()

class Charge:
    def __init__(self, x, y, image):
        charge = pygame.image.load(os.path.join("Assets", image))
        charge = pygame.transform.scale(charge, (50, 50))
        screen.blit(charge, (x, y))
    
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
player_x = 400
player_y = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.image.load(os.path.join("Assets", "player.png"))
player = pygame.transform.scale(player, (100, 100))  # Adjusted the size for visibility
bg = pygame.image.load(os.path.join("Assets", "bg.png"))
bg = pygame.transform.scale(bg, (900, 700))
moon = pygame.image.load(os.path.join("Assets", "moon.png"))
moon = pygame.transform.scale(moon, (900, 100))

def draw_player(x, y):
    screen.blit(player, (x, y))

clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks() #starter tick
gravity = 2
run = True

while run:
    clock.tick(60)  # Set the frame rate to 60 frames per second
    screen.blit(bg, (0, 0))
    screen.blit(moon, (0, 600))
    draw_player(player_x, player_y)
    if player_y < 500:
        player_y += gravity
    speed = 5
    charge1 = Charge(300,300,"charge.png")
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