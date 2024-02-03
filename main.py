import pygame
import os
pygame.init()
class Charge:
    def __init__(self, x, y, image):
        charge = pygame.image.load(os.path.join("Assets", image))
        charge = pygame.transform.scale(charge, (50, 50))
        screen.blit(charge, (x, y))

class Tile:
    def __init__(self, x, y, image):
        tile = pygame.image.load(os.path.join("Assets",image))
        tile = pygame.transform.scale(tile, (100,100))
        screen.blit(tile, (x,y))



   
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player_left = pygame.image.load(os.path.join("Assets", "player_left.png"))
player_right = pygame.image.load(os.path.join("Assets", "player_right.png"))
player = pygame.transform.scale(player_left, (100, 100))  # Adjusted the size for visibility
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
    charge1 = Charge(300,400,"charge.png")
    charge2 = Charge(250,400, "charge.png")
    charge3= Charge(200,400, "charge.png")
    tile1 = Tile(0,600, "tile.png")
    tile2 = Tile(100, 600, "tile.png")
    tile3 = Tile(200, 600, "tile.png")
    tile4 = Tile(300, 600, "tile.png")
    tile5 = Tile(400, 600, "tile.png")
    tile6 = Tile(500, 600, "tile.png")
    tile7 = Tile(600, 600, "tile.png")
    tile8 = Tile(700, 600, "tile.png")
    tile9 = Tile(800, 600, "tile.png")
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        player_x -= speed
        player = pygame.transform.scale(player_left,(100,100))

    if pressed_keys[pygame.K_d]:
        player = pygame.transform.scale(player_right,(100,100))
        player_x += speed
    if pressed_keys[pygame.K_w]:
        player_y -= speed
    if pressed_keys[pygame.K_s]:
        player_y += speed


    for event in pygame.event.get():
        draw_player(player_x, player_y)
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()


pygame.quit()

