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

class Energy:
    def __init__(self,x,y,image):
        self.image = pygame.image.load(os.path.join("Assets", image))
        self.image = pygame.transform.scale(self.image, (125,50))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
class Beam:
    def __init__(self, x, y, direction):
        self.image = pygame.image.load(os.path.join("Assets", "beam.png"))
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = direction  # 'left' or 'right'

    def update(self):
        # Move the beam horizontally
        if self.direction == 'left':
            self.rect.x -= 10
        elif self.direction == 'right':
            self.rect.x += 10

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
player_x = 400
player_y = 500
player_velocity_y = 0
energy_level = 119
energy_x = 400
energy_y = 50
playerFacesRight = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
beam = pygame.image.load(os.path.join("Assets", "beam.png"))
energy6 = pygame.image.load(os.path.join("Assets", "energy6.png"))
energy5 = pygame.image.load(os.path.join("Assets", "energy5.png"))
energy4 = pygame.image.load(os.path.join("Assets", "energy4.png"))
energy3 = pygame.image.load(os.path.join("Assets", "energy3.png"))
energy2 = pygame.image.load(os.path.join("Assets", "energy2.png"))
energy1 = pygame.image.load(os.path.join("Assets", "energy1.png"))
player_left = pygame.image.load(os.path.join("Assets", "player_left.png"))
player_right = pygame.image.load(os.path.join("Assets", "player_right.png"))
energy_sprite = pygame.transform.scale(energy6, (125,75))
player = pygame.transform.scale(player_left, (100, 100))  # Initialize player as left-facing

bg = pygame.image.load(os.path.join("Assets", "bg.png"))
bg = pygame.transform.scale(bg, (900, 700))
moon = pygame.image.load(os.path.join("Assets", "moon.png"))
moon = pygame.transform.scale(moon, (900, 100))

# Font setup
font = pygame.font.Font(None, 36)

def draw_player(x, y):
    screen.blit(player, (x, y))

def draw_energy(x, y):
    screen.blit(energy_sprite, (x, y))

def draw_beam(x, y):
    screen.blit(beam, (x,y))

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

energy_increase_delay = 30
current_energy_delay = 0
beams = []  # List to store beam positions

while run:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    screen.blit(moon, (0, 600))
    draw_player(player_x, player_y)
    draw_charges_and_tiles()
    draw_energy(energy_x, energy_y)

    # Update and draw beams
    updated_beams = []
    for beam in beams:
        beam.update()
        screen.blit(beam.image, beam.rect.topleft)
        updated_beams.append(beam)

    beams = updated_beams

    player_rect = player.get_rect(topleft=(player_x, player_y))

    # Check collisions with charge blocks
    for charge in [charge1, charge2, charge3, charge4, charge5, charge6]:
        if player_rect.colliderect(charge.rect) and player_rect.bottom <= charge.rect.top + 5:
            player_y = charge.rect.top - player_rect.height
            player_velocity_y = 0  # Stop falling
            
            # Increase energy level with a delay
            current_energy_delay += 1
            if current_energy_delay >= energy_increase_delay and energy_level<119:
                energy_level += 20
                current_energy_delay = 0

    if player_y < 500 or player_velocity_y < 0:
        player_y += player_velocity_y
        player_velocity_y += gravity

    speed = 5
    if energy_level >= 100:
        energy_sprite = pygame.transform.scale(energy6, (125, 50))
    elif energy_level >= 80:
        energy_sprite = pygame.transform.scale(energy5, (125, 50))
    elif energy_level >= 60:
        energy_sprite = pygame.transform.scale(energy4, (125, 50))
    elif energy_level >= 40:
        energy_sprite = pygame.transform.scale(energy3, (125, 50))
    elif energy_level >= 20:
        energy_sprite = pygame.transform.scale(energy2, (125, 50))
    elif energy_level < 20:
        energy_sprite = pygame.transform.scale(energy1, (125, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player_y >= 500:
                player_velocity_y = jump_velocity
            if event.key == pygame.K_SPACE and energy_level != 0:
                energy_level -= 20
                direction = 'right' if playerFacesRight else 'left'
                beams.append(Beam(player_x, player_y + 20, direction))

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        player_x -= speed
        player = pygame.transform.scale(player_left, (100, 100))
        playerFacesRight = False

    if pressed_keys[pygame.K_d]:
        player_x += speed
        player = pygame.transform.scale(player_right, (100, 100))
        playerFacesRight = True

    # Display clock at the top
    time_passed = pygame.time.get_ticks() // 1000
    time_text = font.render(f"Time: {time_passed}", True, (255, 255, 255))
    screen.blit(time_text, (425, 15))

    pygame.display.update()

pygame.quit()