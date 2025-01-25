import pygame
from map1 import *
#from map2 import

pygame.init()

FPS = 60
clock = pygame.time.Clock()
#створи вікно гри

wind_w, wind_h = 700, 500
window = pygame.display.set_mode((wind_w, wind_h))
pygame.display.set_caption("Догонялки")


#задай фон сцени
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (wind_w, wind_h))

#створи 2 спрайти та розмісти їх на сцені
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)


class Sprait:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #5super().(__init__(self, x, y, w, h, image))


class Player(Sprait):
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
    

    def move(self, a, d, s, w):
        keys = pygame.key.get_pressed()
        if keys[d]:
            self.rect.x += 5
        if keys[a]:
            self.rect.x -= 5
        if keys[w]:
            self.rect.y -= 5 
        if keys[s]:
            self.rect.y += 5

blocks = []
blocks_png = pygame.image.load("block.png")
blocks_size = 50
x,y = 0,0
for roy in level1:
    for block in roy:
        if block == "1":
            blocks.append(Sprait(x, y, blocks_size, blocks_size, blocks_png))
        x += blocks_size
    x = 0
    y += blocks_size

player1_img = pygame.image.load("sprite1.png")
player1 = Player(0, 0, 50, 50, player1_img)

img_gold = pygame.image.load("treasure.png")
gold = Sprait(650, 450, 50, 50, img_gold)

#оброби подію «клік за кнопкою "Закрити вікно"»
game = True
while game:
    
    window.blit(background, (0, 0))
    player1.draw()
    player1.move(pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w)

    gold.draw()
   

    for block in blocks:
        block.draw()

    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(FPS)


 
