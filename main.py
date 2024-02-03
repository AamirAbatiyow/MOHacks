import pygame
import os

pygame.init()

class Charge:
    def __init__(self, x, y, image):
        self.image = pygame.image.load(os.path.join("Assets", image))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Tile:
    def __init__(self, x, y, image):
        self.image = pygame.image.load(os.path.join("Assets", image))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
player_x = 400
player_y = 500
player_velocity_y = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
<<<<<<< HEAD
player = pygame.image.load(os.path.join("Assets", "player.png"))
player = pygame.transform.scale(player, (100, 100))
=======
player_left = pygame.image.load(os.path.join("Assets", "player_left.png"))
player_right = pygame.image.load(os.path.join("Assets", "player_right.png"))
player = pygame.transform.scale(player_left, (100, 100))  # Adjusted the size for visibility
>>>>>>> 328a59b96f5028ccbe29e74cc9f71aa65856e2d4
bg = pygame.image.load(os.path.join("Assets", "bg.png"))
bg = pygame.transform.scale(bg, (900, 700))
moon = pygame.image.load(os.path.join("Assets", "moon.png"))
moon = pygame.transform.scale(moon, (900, 100))

def draw_player(x, y):
    screen.blit(player, (x, y))

def draw_charges_and_tiles():
    charge1.draw(screen)
    charge2.draw(screen)
    charge3.draw(screen)
    charge4.draw(screen)
    charge5.draw(screen)
    charge6.draw(screen)

    tile1.draw(screen)
    tile2.draw(screen)
    tile3.draw(screen)
    tile4.draw(screen)
    tile5.draw(screen)
    tile6.draw(screen)
    tile7.draw(screen)
    tile8.draw(screen)
    tile9.draw(screen)

clock = pygame.time.Clock()
gravity = 1
jump_velocity = -22
run = True

charge1 = Charge(250, 400, "charge.png")
charge2 = Charge(200, 400, "charge.png")
charge3 = Charge(150, 400, "charge.png")
charge4 = Charge(600, 400, "charge.png")
charge5 = Charge(650, 400, "charge.png")
charge6 = Charge(700, 400, "charge.png")

tile1 = Tile(0, 600, "tile.png")
tile2 = Tile(100, 600, "tile.png")
tile3 = Tile(200, 600, "tile.png")
tile4 = Tile(300, 600, "tile.png")
tile5 = Tile(400, 600, "tile.png")
tile6 = Tile(500, 600, "tile.png")
tile7 = Tile(600, 600, "tile.png")
tile8 = Tile(700, 600, "tile.png")
tile9 = Tile(800, 600, "tile.png")

while run:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    screen.blit(moon, (0, 600))
    draw_player(player_x, player_y)
    draw_charges_and_tiles()

    # Check collisions with charge blocks
    for charge in [charge1, charge2, charge3, charge4, charge5, charge6]:
        if player_rect.colliderect(charge.rect) and player_rect.bottom <= charge.rect.top + 5:
            player_y = charge.rect.top - player_rect.height
            player_velocity_y = 0  # Stop falling

    if player_y < 500 or player_velocity_y < 0:
        player_y += player_velocity_y
        player_velocity_y += gravity

    speed = 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player_y >= 500:
                player_velocity_y = jump_velocity
            if event.key == pygame.K_w and player_y == 500:
                player_velocity_y = jump_velocity

    player_rect = player.get_rect(topleft=(player_x, player_y))
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        player_x -= speed
        player = pygame.transform.scale(player_left,(100,100))

    if pressed_keys[pygame.K_d]:
        player = pygame.transform.scale(player_right,(100,100))
        player_x += speed

    pygame.display.update()

pygame.quit()