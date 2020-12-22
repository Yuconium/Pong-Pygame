import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_w, K_s)
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, up, down):
        super(Player, self).__init__()
        
        self.surf = pygame.Surface((5, 80))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (x, y))

    def update(self, Taste, up, down):
        if Taste[up]:
            self.rect.move_ip(0, -5)

        if Taste[down]:
            self.rect.move_ip(0, 5)

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((50, 50, 250))
        self.rect = self.surf.get_rect(center = ((screen_width / 2), (screen_height / 2)))
        self.vektorx = 7
        self.vektory = -7

    def update(self):
        self.rect.move_ip(self.vektorx /2 , self.vektory / 2)

        if self.rect.right > screen_width:
            self.vektorx = -7

        if self.rect.left < 0:
            self.vektorx = 7

        if self.rect.top <= 0:
            self.vektory = 7

        if self.rect.bottom > screen_height:
            self.vektory = -7

        if pygame.sprite.spritecollideany(ball, bricks):
            self.vektory = 7



pygame.init()

clock = pygame.time.Clock()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
bricklist = []
player_one = Player(550, 200, K_UP, K_DOWN)
player_two = Player(50, 200, K_w, K_s)
ball = Ball()
x = 50
y = 20

    
kollision = pygame.sprite.Group()
kollision2 = pygame.sprite.Group()
ballgroup = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


kollision2.add(player_two)
kollision.add(player_one)
all_sprites.add(ball, player_one, player_two)
bricks = pygame.sprite.Group()

mainloop = True

while mainloop:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False


    screen.fill((0, 0, 0))

    Taste = pygame.key.get_pressed()
    player_one.update(Taste, K_UP, K_DOWN)
    player_two.update(Taste, K_w, K_s)
    ball.update()
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)
    
    
    if pygame.sprite.spritecollideany(ball, kollision):
        ball.vektorx = -7
    if pygame.sprite.spritecollideany(ball, kollision2):
        ball.vektorx = 7  
    clock.tick(60)
    pygame.display.flip()

pygame.quit()

