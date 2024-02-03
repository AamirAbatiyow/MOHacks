import pygame
import os
pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
player_sprite = pygame.image.load(os.path.join("Assets", "player.png"))
player_sprite = pygame.transform.scale(player_sprite, (100,100))
player_x =400
player_y =500 
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
def draw_player(x, y):
    screen.blit(player_sprite, (x,y))
BackGround = Background('bg.png',[0,0])
run = True
while run:
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    draw_player(player_x,player_y)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()

